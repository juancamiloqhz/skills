#!/usr/bin/env python3
"""Exercise exact PR/head ledger keys using synthetic evidence and the real CLI."""

import argparse
import csv
import io
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

# Synthetic SHA-shaped identifiers, never observed Git commits.
HEAD_A = "a12c34e56f7890ab12cd34ef567890ab12cd34ef"
HEAD_B = "b98e76d54c3210fe98dc76ba543210fe98dc76ba"
PR = "1"
PASS = "unit-test-verified"


def require(condition, message):
    # Deliberately not a Python assert: all checks must survive python -O.
    if not condition:
        raise RuntimeError(message)


def exercise(cli, root, bun):
    store = root / "store"
    evidence_dir = root / "synthetic-evidence"
    evidence_dir.mkdir()
    ledger = store / "ledger.tsv"

    def call(*args, code=0):
        command = [bun, str(cli), "--store", str(store), "--json", *args]
        result = subprocess.run(command, text=True, capture_output=True, timeout=20)
        with (root / "commands.jsonl").open("a") as log:
            log.write(json.dumps({"command": command, "exit": result.returncode,
                                  "stdout": result.stdout, "stderr": result.stderr}) + "\n")
        require(result.returncode == code,
                f"{args}: expected exit {code}, got {result.returncode}: {result.stderr}")
        return json.loads(result.stdout)

    def fixture(name, head, verdict):
        path = evidence_dir / f"{name}.json"
        path.write_text(json.dumps({"synthetic": True, "round": name, "pr": PR,
                                    "sha": head, "verdict": verdict}, indent=2) + "\n")
        return path

    def record(head, verdict, evidence):
        row = call("ledger", "record", PR, head, verdict,
                   "--evidence", str(evidence), "--verifier", "synthetic-fixture")
        require(row["pr"] == PR and row["sha"] == head
                and row["verdict"] == verdict and row["evidence"] == str(evidence),
                "record JSON did not preserve the supplied key/verdict/evidence")
        return row

    def snapshot(name):
        data = ledger.read_bytes()
        (root / f"{name}.tsv").write_bytes(data)
        return data

    def rows(data):
        return list(csv.DictReader(io.StringIO(data.decode()), delimiter="\t"))

    call("init")
    evidence_a = fixture("A-pass", HEAD_A, PASS)
    evidence_a_bytes = evidence_a.read_bytes()
    original_a = record(HEAD_A, PASS, evidence_a)
    require(call("ledger", "check", PR, HEAD_A) == original_a, "A pass lookup differs")
    a_only = snapshot("01-A-pass")
    require(rows(a_only) == [original_a], "A ledger bytes differ from JSON")

    for pr, head in [(PR, HEAD_B), ("2", HEAD_A)]:
        missing = call("ledger", "check", pr, head, code=2)
        require(missing == {"pr": pr, "sha": head, "verdict": "NOT-VERIFIED"},
                "a different PR/head unexpectedly matched A")
        require(ledger.read_bytes() == a_only, "missing lookup changed the ledger")

    negative_evidence = fixture("B-negative", HEAD_B, "verifier-failed")
    negative_bytes = negative_evidence.read_bytes()
    negative_b = record(HEAD_B, "verifier-failed", negative_evidence)
    # call requires exit 0; a successful lookup is not a passing verdict.
    lookup_b = call("ledger", "check", PR, HEAD_B)
    require(lookup_b == negative_b and lookup_b["verdict"] != PASS,
            "exit-zero negative lookup was treated as passing")
    before_stale = snapshot("02-B-negative")
    require(rows(before_stale) == [original_a, negative_b], "negative B changed A")

    # Simulate an old successful report arriving while B is current. This local
    # decision is the caller's, not authentication or precedence enforced by orch.
    stale = json.loads(evidence_a.read_text())
    require(stale["synthetic"] and stale["verdict"] == PASS, "stale fixture is not A success")
    accepted = (stale["pr"], stale["sha"]) == (PR, HEAD_B)
    require(not accepted, "stale A report approved current B")
    (root / "synthetic-stale-decision.json").write_text(json.dumps({
        "synthetic": True, "caller_decision": "stale; no ledger write",
        "reported": stale, "current": {"pr": PR, "sha": HEAD_B},
    }, indent=2) + "\n")
    require(call("ledger", "check", PR, HEAD_A) == original_a, "stale arrival relabelled A")
    require(call("ledger", "check", PR, HEAD_B) == negative_b, "stale arrival changed B")
    require(snapshot("03-after-stale-A") == before_stale, "stale arrival changed ledger bytes")
    require(evidence_a.read_bytes() == evidence_a_bytes, "A evidence was relabelled")

    # A separately labelled synthetic new verification round supplies B's pass.
    # orch permits replacement; it does not authorize this round or its evidence.
    evidence_b = fixture("B-fresh-pass", HEAD_B, PASS)
    require(evidence_b not in (evidence_a, negative_evidence), "B reused old evidence")
    fresh = json.loads(evidence_b.read_text())
    require(fresh["synthetic"] and fresh["sha"] == HEAD_B and fresh["verdict"] == PASS,
            "fresh evidence does not describe B passing")
    fresh_b = record(HEAD_B, PASS, evidence_b)
    require(call("ledger", "check", PR, HEAD_B) == fresh_b, "fresh B pass missing")
    require(call("ledger", "check", PR, HEAD_A) == original_a, "fresh B removed A")
    require(rows(snapshot("04-B-fresh-pass")) == [original_a, fresh_b],
            "final ledger bytes differ from the two exact-key results")
    require(evidence_a.read_bytes() == evidence_a_bytes, "final A evidence changed")
    require(negative_evidence.read_bytes() == negative_bytes, "negative evidence changed")
    summary = {"result": "PASS", "synthetic": True, "pr": PR,
               "head_a": HEAD_A, "head_b": HEAD_B, "scratch": str(root)}
    (root / "result.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", required=True, type=Path, help="installed orch.ts path")
    parser.add_argument("--scratch", type=Path, help="parent for a fresh retained run directory")
    args = parser.parse_args()
    cli = args.cli.resolve()
    source = Path(__file__).resolve().parents[4] / "skills/jstack/jstack-juan-mode/scripts/orch"
    for name in ("orch.ts", "store.ts"):
        require((cli.parent / name).read_bytes() == (source / name).read_bytes(),
                f"installed {name} differs from checkout; no test run")
    bun = shutil.which("bun")
    require(bun is not None, "installed Bun is required; nothing will be installed")
    if args.scratch:
        args.scratch.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix="orch-current-head-", dir=args.scratch))
    print(f"Retaining synthetic exercise evidence in {root}", flush=True)
    exercise(cli, root, bun)


if __name__ == "__main__":
    main()
