"""Replay the retained generated-input checker in a fresh disposable repository."""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


def replay(root):
    root.mkdir(parents=True, exist_ok=False)
    packet = json.loads(Path(__file__).with_name("cases.json").read_text())
    for name, body in packet["productFiles"].items():
        (root / name).write_text(body)
    git = ["git", "-c", "core.hooksPath=/dev/null", "-C", str(root)]
    for args in [["init", "-b", "main"], ["config", "user.name", "Fixture author"],
                 ["config", "user.email", "fixture@example.invalid"],
                 ["config", "commit.gpgsign", "false"], ["add", "."],
                 ["commit", "-m", "Add parser and input contract"]]:
        subprocess.run(git + args, check=True, capture_output=True)
    subprocess.run(git + ["apply", str(Path(__file__).with_name("solution.patch").resolve())], check=True)
    skill = root / ".agents/skills/verify-limits-formal"
    link = root / ".claude/skills/verify-limits-formal"
    assert link.is_symlink() and link.readlink() == Path("../../.agents/skills/verify-limits-formal")
    for name in ["SKILL.md", "check.py"]:
        assert (link / name).resolve() == (skill / name).resolve()
    result = subprocess.run([sys.executable, "-B", str(link / "check.py"), "--self-test"],
                            cwd=root, check=True, capture_output=True, text=True)
    evidence = json.loads(result.stdout)
    assert evidence["status"] == "pass" and evidence["product_source_unchanged"]
    assert evidence["baseline"] == evidence["restored"]
    assert len(evidence["mutations"]) == 5 and all(x["detected"] for x in evidence["mutations"])
    assert not list(skill.glob("mutation-*"))
    for name, body in packet["productFiles"].items():
        assert (root / name).read_text() == body, name
    subprocess.run(git + ["diff", "--exit-code", "HEAD", "--"], check=True)
    # Only after the known source and actual checks agree, confirm this replay's commit.
    text = (skill / "SKILL.md").read_text()
    previous = re.search(r"Confirmed sync commit: `([0-9a-f]{40})`", text).group(1)
    head = subprocess.check_output(git + ["rev-parse", "HEAD"], text=True).strip()
    (skill / "SKILL.md").write_text(text.replace(previous, head))
    print(json.dumps({"outcome": "complete", "method": "generated-input testing, not formal proof",
                      "cases_per_baseline": evidence["baseline"]["cases"],
                      "detected_mutations": len(evidence["mutations"]),
                      "source_and_link_preserved": True, "confirmed_sync_commit": head}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    replay(parser.parse_args().path.resolve())
