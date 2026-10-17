"""Replay measured candidates; agent dispatch and judgment are not simulated."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys


def run(command, *, cwd, input=None):
    return subprocess.run(command, cwd=cwd, input=input, text=True, check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scratch", type=Path, help="New directory outside the repository")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    repo = here.parents[3]
    scratch = args.scratch.resolve()
    if scratch == repo or repo in scratch.parents:
        parser.error("Use a scratch directory outside the repository")
    scratch.mkdir(parents=True, exist_ok=False)
    fixtures = here.parent / "perf-issue"
    recorded = json.loads((here / "results.json").read_text())
    for name in ("generate.py", "parent-verify.py"):
        shutil.copy2(fixtures / name, scratch / name)
    shutil.copy2(here / "benchmark.py", scratch / "benchmark.py")
    baseline = scratch / "baseline"
    shutil.copytree(fixtures / "baseline", baseline)
    shutil.copy2(fixtures / "app/summary.test.cjs", baseline / "summary.test.cjs")
    run([sys.executable, "generate.py"], cwd=scratch)
    run(["node", "--test", "summary.test.cjs"], cwd=baseline)
    events = json.loads((scratch / "events.json").read_text())[:80]
    rules = json.loads((scratch / "rules.json").read_text())
    totals = {}
    accepted = 0
    for event in events:
        rule = rules.get(event["type"])
        if rule and event["amount"] >= rule["minimum"]:
            accepted += 1
            totals[event["type"]] = totals.get(event["type"], 0) + event["amount"] * rule["multiplier"]
    (scratch / "small.json").write_text(json.dumps(events))
    (scratch / "small-expected.json").write_text(json.dumps({
        "processed": len(events), "accepted": accepted,
        "rejected": len(events) - accepted, "totals": totals,
    }))

    def measure(a, b, name, extra=(), allow_errors=False):
        command = [sys.executable, "benchmark.py", "--a", str(a), "--b", str(b),
                   "--out", str(scratch / name), *extra]
        process = subprocess.run(command, cwd=scratch, text=True)
        result = json.loads((scratch / name).read_text())
        assert process.returncode == int(bool(result["errors"]))
        assert allow_errors or result["errors"] == 0
        return result

    sensitivity = measure(baseline, baseline, "sensitivity.json", [
        "--events-a", "small.json", "--expected-a", "small-expected.json"])
    assert sensitivity["a"]["range_ms"][1] < sensitivity["b"]["range_ms"][0]
    current = baseline
    outcomes = []
    for attempt in recorded["attempts"]:
        candidate = scratch / f"attempt{attempt['id']}"
        shutil.copytree(current, candidate)
        run(["git", "apply", "-"], cwd=candidate, input=attempt["patch"])
        run(["node", "--test", "summary.test.cjs"], cwd=candidate)
        measurement = measure(current, candidate, f"attempt{attempt['id']}.json")
        outcomes.append({"attempt": attempt["id"], "pastNoiseNow": measurement["past_noise"],
                         "recordedVerdict": attempt["verdict"]})
        if attempt["verdict"] == "kept":
            current = candidate
    shutil.copytree(current, scratch / "app")
    run([sys.executable, "parent-verify.py"], cwd=scratch)
    same = measure(current, current, "same-source.json")
    negative = scratch / "negative"
    shutil.copy2(current / "summary.cjs", negative / "summary.cjs")
    bad = measure(current, negative, "incorrect-output.json", allow_errors=True)
    assert bad["errors"] == 7
    print(json.dumps({"attempts": outcomes, "sameSourcePastNoise": same["past_noise"],
                      "incorrectSamplesRejected": bad["errors"], "scratch": str(scratch)}, indent=2))


if __name__ == "__main__":
    main()
