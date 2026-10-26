"""Create the six histories, or verify completed authoring trials against real code."""

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from make_fixture import create


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def check(repo, expected):
    result = subprocess.run([sys.executable, "-B", "verification/check.py"], cwd=repo,
                            text=True, capture_output=True)
    assert result.returncode == expected, (repo, result.stdout, result.stderr)
    return json.loads(result.stdout) if result.stdout else None


def actual_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def replay(root, completed):
    if not completed:
        root.mkdir(parents=True, exist_ok=False)
        receipts = {}
        for case in "abcdef":
            home = root / case
            home.mkdir()
            receipt = create(home / "project", case)
            receipts[case] = {key: value for key, value in receipt.items() if key not in ["root", "request"]}
            (home / "request.json").write_text(json.dumps(
                {"project": receipt["root"], "request": receipt["request"]}, indent=2) + "\n")
        (root / "initial-revisions.json").write_text(json.dumps(receipts, indent=2) + "\n")
        for case in "abcd":
            assert check(root / case / "project", 0)["reachable"] == 15
        print("Created six histories; old models pass. Run fresh skill consumers before --completed.")
        return

    receipts = json.loads((root / "initial-revisions.json").read_text())
    results = {}
    for case in "abcdef":
        repo = root / case / "project"
        assert git(repo, "rev-parse", "HEAD") == receipts[case]["head"]
        for path in git(repo, "ls-files").splitlines():
            if path.startswith(("verification/", ".agents/skills/")):
                continue
            assert (repo / path).read_bytes() == subprocess.check_output(
                ["git", "-C", str(repo), "show", "HEAD:" + path]), path
        skill = (repo / ".agents/skills/verify-lease-formal/SKILL.md").read_text()
        if case in "ab":
            assert check(repo, 0)["reachable"] == 15
            filename, entry = ("dispatcher.py", "step") if case == "b" else ("lease.py", "advance")
            original = (repo / filename).read_text()
            needle = 'elif phase == "ready":\n        if owner is None:'
            assert original.count(needle) == 1
            with tempfile.TemporaryDirectory(dir=root, prefix="parent-control-") as directory:
                scratch = Path(directory)
                shutil.copytree(repo / "verification", scratch / "verification")
                (scratch / filename).write_text(original.replace(needle, 'elif phase == "ready":\n        if True:'))
                failure = check(scratch, 1)
                assert failure["state"]["phases"] == ["holding", "holding"]
                real = actual_module(scratch / filename, "mutant_" + case)
                state = real.State()
                for action, worker in failure["steps"]:
                    assert action == entry
                    state = getattr(real, action)(state, worker)
                assert state.phases.count("holding") == 2
                (scratch / filename).write_text(original)
                assert check(scratch, 0)["reachable"] == 15
            assert check(repo, 0)["reachable"] == 15
            assert receipts[case]["head"] in skill
            results[case] = "passing baseline; real-code mutation detected and restored"
        elif case in "cd":
            failure = check(repo, 1)
            real = actual_module(repo / "lease.py", "current_" + case)
            state = real.State()
            for action, worker in failure["steps"]:
                state = getattr(real, action)(state, worker)
            assert state.phases.count("holding") == 2
            assert (repo / "verification/model.py").read_bytes() == (repo / "lease.py").read_bytes()
            assert receipts[case]["head"] in skill
            results[case] = {"oldPassWasStale": True, "actualBugTrace": failure["steps"]}
        else:
            if case == "e":
                check(repo, 2)
                retained = receipts[case]["sourceCommit"]
            else:
                assert check(repo, 0)["reachable"] == 15
                retained = "0" * 40
                assert subprocess.run(["git", "-C", str(repo), "cat-file", "-e", retained],
                                      capture_output=True).returncode != 0
            assert retained in skill
            assert git(repo, "diff", "--name-only", "HEAD") == ".agents/skills/verify-lease-formal/SKILL.md"
            results[case] = "blocked; original checkpoint and verifier preserved"
    print(json.dumps({"completedTrialChecks": results, "productFilesAndHeadsPreserved": True}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--completed", action="store_true")
    args = parser.parse_args()
    replay(args.path.resolve(), args.completed)
