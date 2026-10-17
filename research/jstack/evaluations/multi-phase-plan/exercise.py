import re
from pathlib import Path
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[4]
MODE = ROOT / "skills/jstack/jstack-juan-mode"


def plan():
    source = (MODE / "playbooks/multi-phase-plan.md").read_text()
    body = source.split("````markdown\n", 1)[1].split("\n````", 1)[0]
    body = body.replace("<swarm workers model>", "codex gpt-6.1-sol medium")
    body = body.replace("<PR id>", "P1").replace("<slug>", "proof")
    return re.sub(r"<[^<>\n]+>", "fixture-value", body) + "\n"


def run(checker, file):
    result = subprocess.run(["node", str(checker), str(file)], capture_output=True, text=True, timeout=10)
    return result.returncode, result.stdout + result.stderr


def exercise(directory):
    good = plan()
    file = directory / "plan.md"
    file.write_text(good)
    checker = MODE / "scripts/check-plan.mjs"
    code, output = run(checker, file)
    assert code == 0, output
    cases = [
        ("missing-title", "# fixture-value plan", "fixture-value plan", "no H1"),
        ("missing-read-guide", "## How to read this", "## Reading", "How to read this"),
        ("missing-program", "## Program checklist", "## Program", "Program checklist"),
        ("wrong-program-order", "### Arm the program", "### Spawn owners", "Arm the program"),
        ("missing-scheduler", "`schedule_task`", "`unsupported`", "schedule_task"),
        ("wrong-cadence", '"everyMs":3600000', '"everyMs":60000', "everyMs"),
        ("missing-file-block", "**Files.**", "**Paths.**", "sub-blocks"),
        ("missing-rule", "**Verify, unit.** Tests alone", "**Verify, unit.** Checks alone", "does not open with the rule"),
        ("missing-model", "Ten lanes on `codex gpt-6.1-sol medium`", "Ten lanes on ``", "model filled in"),
        ("duplicate-lane", "Lane 10.", "Lane 9.", "expected 1 to 10"),
        ("missing-proof-path", "Save `proof.png`.", "Capture proof.", "names no screenshot"),
        ("missing-predicate", "Pass when", "Observe when", "no pass predicate"),
        ("missing-perf-baseline", "- [ ] Baseline.", "- [ ] Starting point.", "perf boxes"),
        ("review-none-with-boxes", "**Review gate.** The operator reviews before merge.", "**Review gate.** None. P1 is not review-gated.", "None but has boxes"),
        ("missing-review-video", "video", "recording", 'lacks "video"'),
        ("missing-prototypes", "## Appendix A. Prototype evidence", "## Appendix A. Evidence", "Prototype evidence"),
    ]
    for name, old, new, diagnostic in cases:
        assert old in good, name
        file.write_text(good.replace(old, new))
        code, output = run(checker, file)
        assert code == 1 and diagnostic in output, (name, code, output)
    gate_start = good.index("**Review gate.**")
    gate_end = good.index("**Merge.**", gate_start)
    file.write_text(good[:gate_start] + "**Review gate.** None. P1 is not review-gated.\n\n" + good[gate_end:])
    assert run(checker, file)[0] == 0
    pr_start = good.index("## fixture-value (P1)")
    pr_end = good.index("## Close the program")
    file.write_text(good[:pr_end] + good[pr_start:pr_end].replace("P1", "P2") + good[pr_end:])
    code, output = run(checker, file)
    assert code == 0 and "2 PR sections, 0 problems" in output, output
    file.write_text(good.replace("fixture-value", "<unresolved>"))
    assert run(checker, file)[0] == 0
    result = subprocess.run(["node", str(checker)], capture_output=True, text=True, timeout=10)
    assert result.returncode == 2 and "Usage:" in result.stderr
    print("PASS: one/two-PR plans, no-review gate, 16 rejection cases and usage error")
    print("SOURCE LIMIT: generic unresolved placeholders still pass; semantic review remains required")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="jstack-plan-") as name:
        exercise(Path(name))
