"""Exercise merge-result behavior in disposable Git worktrees; no forge or installs."""

from pathlib import Path
import subprocess
import sys
import tempfile


def command(*args, cwd=None, check=True):
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True, timeout=20)
    if check and result.returncode:
        raise RuntimeError(f"{args!r}: {result.stderr}")
    return result


def git(repo, *args, check=True):
    return command("git", "-c", "core.hooksPath=/dev/null", "-C", str(repo), *args, check=check)


def commit(repo, files, message):
    for path, text in files.items():
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
    git(repo, "add", *files)
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD").stdout.strip()


def run(root):
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "Autopilot fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "config", "commit.gpgsign", "false")
    base = commit(repo, {
        "api.py": "def total(values):\n    return len(values)\n",
        "caller.py": "from api import total\nprint(total([1, 2]))\n",
    }, "fixture: base")
    git(repo, "switch", "-c", "feature")
    head = commit(repo, {"api.py": "def total(values):\n    return sum(values)\n"}, "fixture: sum values")
    assert command(sys.executable, "-B", "caller.py", cwd=repo).stdout == "3\n"
    own_paths = set(git(repo, "diff", "--name-only", base, head).stdout.splitlines())
    original_branch = git(repo, "symbolic-ref", "HEAD").stdout

    for name, files, expected in [
        ("unrelated", {"notes.md": "Documentation change.\n"}, "3\n"),
        ("caller-compatible", {"caller.py": "from api import total\nprint(total([2, 4]))\n"}, "6\n"),
        ("caller-incompatible", {"caller.py": "from api import total\nprint(total(['a', 'b']))\n"}, None),
        ("ci-selection", {".github/workflows/check.yml": "name: changed gate selection\n"}, "3\n"),
    ]:
        trunk = root / (name + "-trunk")
        git(repo, "worktree", "add", "-b", name, str(trunk), base)
        tip = commit(trunk, files, "fixture: " + name)
        assert command(sys.executable, "-B", "caller.py", cwd=trunk).stdout == "2\n"
        drift_paths = set(git(repo, "diff", "--name-only", base, tip).stdout.splitlines())
        assert own_paths.isdisjoint(drift_paths)
        merged = git(repo, "merge-tree", "--write-tree", head, tip).stdout.splitlines()[0]
        # Materialize the actual merge tree, without changing the feature branch.
        commit_oid = git(repo, "commit-tree", merged, "-p", head, "-p", tip, "-m", "fixture: merge result").stdout.strip()
        result_dir = root / (name + "-result")
        git(repo, "worktree", "add", "--detach", str(result_dir), commit_oid)
        result = command(sys.executable, "-B", "caller.py", cwd=result_dir, check=False)
        if expected is None:
            assert result.returncode != 0 and "TypeError" in result.stderr
        else:
            assert result.returncode == 0 and result.stdout == expected
        assert (result_dir / next(iter(files))).read_text() == next(iter(files.values()))
        assert git(repo, "rev-parse", "feature").stdout.strip() == head
        assert git(repo, "symbolic-ref", "HEAD").stdout == original_branch
    print("PASS: disjoint caller change can fail only in the clean merge result; compatible caller passes")
    print("PASS: unrelated and CI-selection changes materialize without rewriting the feature head")

    conflict = root / "conflict"
    git(repo, "worktree", "add", "-b", "conflict", str(conflict), base)
    other = commit(conflict, {"api.py": "def total(values):\n    return len(values) + 10\n"}, "fixture: conflicting API")
    result = git(repo, "merge-tree", "--write-tree", head, other, check=False)
    assert result.returncode == 1 and "CONFLICT" in result.stdout
    assert git(repo, "status", "--porcelain").stdout == ""
    print("PASS: conflicting merge is rejected; original checkout and feature ref remain clean")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="jstack-autopilot-") as name:
        run(Path(name))
