#!/usr/bin/env python3
"""Exercise Pocket's public CLI and retain evidence after owned-state cleanup."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import traceback

REPO = Path(__file__).resolve().parents[4]
APP = REPO / "pocket.py"

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-root", type=Path, default=REPO / ".verification-evidence")
    args = parser.parse_args()
    args.evidence_root.mkdir(parents=True, exist_ok=True)
    evidence = Path(tempfile.mkdtemp(prefix="pocket-", dir=args.evidence_root.resolve()))
    scratch = None
    status = {"app": str(APP), "evidence": str(evidence), "passed": False}
    print(f"Evidence: {evidence}", flush=True)
    originals = {name: hashlib.sha256((REPO / name).read_bytes()).hexdigest()
                 for name in ("pocket.py", "README.md")}
    (evidence / "identity.json").write_text(json.dumps({"repo": str(REPO), "sha256": originals,
        "python": sys.version, "executable": sys.executable}, indent=2) + "\n")

    def command(feature, *arguments, expected_code=0, expected=None, error=None):
        argv = [sys.executable, str(APP), *map(str, arguments)]
        result = subprocess.run(argv, cwd=REPO, text=True, capture_output=True, timeout=15)
        record = {"feature": feature, "argv": argv, "exit_code": result.returncode,
                  "stdout": result.stdout, "stderr": result.stderr}
        with (evidence / "commands.jsonl").open("a") as log:
            log.write(json.dumps(record) + "\n")
        require(result.returncode == expected_code, f"{feature}: wrong exit code: {record}")
        if expected is not None:
            require(json.loads(result.stdout) == expected, f"{feature}: unexpected JSON: {record}")
        if error is not None:
            require(error in result.stderr, f"{feature}: missing error: {record}")
        return result.stdout

    try:
        # Doctor checks identity without creating or repairing application state.
        version = command("doctor", "--version")
        require(version.strip() == "Pocket 1.0", "Unexpected Pocket identity")
        scratch = Path(tempfile.mkdtemp(prefix=".pocket-verify-", dir=REPO))
        data = scratch / "data"
        status["scratch"] = str(scratch)
        def drive(feature, *arguments, **kwargs):
            return command(feature, "--data-dir", data, *arguments, **kwargs)
        drive("list-empty", "list", expected=[])
        require(not data.exists(), "Empty list created application state")
        first = {"id": 1, "title": "Packing list", "body": "Passport and charger"}
        drive("add-trim", "add", "--title", "  Packing list  ", "--body", first["body"], expected=first)
        notes = data / "notes.json"
        require(json.loads(notes.read_text()) == [first], "First note not persisted")
        before = notes.read_bytes()
        drive("show-existing", "show", "1", expected=first)
        drive("list-one", "list", expected=[first])
        require(notes.read_bytes() == before, "Read commands changed storage")
        drive("add-blank", "add", "--title", "   ", expected_code=2, error="title must not be blank")
        require(notes.read_bytes() == before, "Rejected title changed storage")
        drive("show-missing", "show", "999", expected_code=2, error="note not found")
        require(notes.read_bytes() == before, "Missing-note read changed storage")
        second = {"id": 2, "title": "Groceries", "body": ""}
        drive("add-default-body", "add", "--title", "Groceries", expected=second)
        drive("show-second", "show", "2", expected=second)
        drive("list-two", "list", expected=[first, second])
        require(json.loads(notes.read_text()) == [first, second], "Final persisted notes mismatch")
        (evidence / "notes.json").write_bytes(notes.read_bytes())
        require(all(hashlib.sha256((REPO / name).read_bytes()).hexdigest() == digest
                    for name, digest in originals.items()), "Application sources changed")
        status["passed"] = True
    except BaseException:
        (evidence / "failure.txt").write_text(traceback.format_exc())
        raise
    finally:
        try:
            if scratch is not None:
                require(scratch.parent == REPO and not scratch.is_symlink(), "Scratch ownership changed")
                shutil.rmtree(scratch)
                require(not scratch.exists(), "Scratch cleanup failed")
            status["cleanup"] = "owned scratch removed; subprocesses completed; evidence retained"
        except BaseException:
            status["passed"] = False
            status["cleanup"] = traceback.format_exc()
            raise
        finally:
            (evidence / "summary.json").write_text(json.dumps(status, indent=2) + "\n")
            require((evidence / "identity.json").is_file(), "Evidence missing after cleanup")
    print("PASS: add, show, list; evidence retained; scratch removed")

if __name__ == "__main__":
    main()
