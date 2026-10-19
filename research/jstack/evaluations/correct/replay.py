"""Replay the evaluated fix and both historical failures in a new owned directory."""

import argparse
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

from make_fixture import create


def tests(root, expected):
    result = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests"],
        cwd=root, capture_output=True, text=True,
    )
    assert result.returncode == expected, result.stdout + result.stderr
    return result.stderr


def archive(repo, revision, destination):
    destination.mkdir()
    data = subprocess.check_output(["git", "-C", str(repo), "archive", revision])
    with tarfile.open(fileobj=io.BytesIO(data)) as files:
        files.extractall(destination, filter="data")


def replay(root):
    root.mkdir(parents=True, exist_ok=False)
    current = root / "current"
    initial = create(current)["head"]
    original = root / "original"
    archive(current, initial, original)
    subprocess.run(
        ["git", "-C", str(current), "apply", str(Path(__file__).with_name("solution.patch").resolve())],
        check=True,
    )
    tests(current, 0)
    print("Current corrected fixture: four tests pass")
    for name in ["csv", "tsv"]:
        past = root / ("mistake-" + name)
        archive(current, "mistake-" + name, past)
        tests(past, 0)
        shutil.copyfile(current / "tests/test_format_registry.py", past / "tests/test_format_registry.py")
        failure = tests(past, 1)
        assert "test_every_registered_format_is_accepted" in failure, failure
        assert f"invalid choice: '{name}'" in failure, failure
        shutil.copyfile(current / "cli.py", past / "cli.py")
        tests(past, 0)
        print(f"{name}: old tests pass; new checks reject historical omission; structural fix passes")
    for args in [["--format", f] for f in ["json", "csv", "tsv", "invalid"]] + [[]]:
        before, after = [
            subprocess.run([sys.executable, "-B", "cli.py", *args], cwd=p, capture_output=True)
            for p in [original, current]
        ]
        assert (before.returncode, before.stdout, before.stderr) == (
            after.returncode, after.stdout, after.stderr
        ), args
    print("Existing format outputs and invalid/missing-argument behavior unchanged")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="New task-owned directory outside the skills checkout")
    replay(parser.parse_args().path.resolve())
