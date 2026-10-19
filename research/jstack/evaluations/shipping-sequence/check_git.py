"""Exercise Shipping's Git mechanics in disposable repositories, without a forge."""

from pathlib import Path
import subprocess
import sys
import tempfile


def command(*args, cwd=None, check=True, data=None):
    result = subprocess.run(
        args, cwd=cwd, input=data, text=True, capture_output=True, timeout=20,
    )
    if check and result.returncode:
        raise RuntimeError(f"{args!r}: {result.stderr}")
    return result


def git(repo, *args, check=True):
    return command("git", "-c", "core.hooksPath=/dev/null", "-C", str(repo), *args, check=check)


def oid(repo, ref):
    return git(repo, "rev-parse", "--verify", ref + "^{commit}").stdout.strip()


def commit_file(repo, name, contents):
    (repo / name).write_text(contents)
    git(repo, "add", name)
    git(repo, "commit", "-m", "fixture: " + name)
    return oid(repo, "HEAD")


def patch_id(repo, base, head):
    diff = git(repo, "diff", base, head).stdout
    fields = command("git", "patch-id", "--stable", data=diff).stdout.split()
    if not fields:
        raise ValueError("No patch identity")
    return fields[0]


def published(repo, branch):
    return git(repo, "ls-remote", "origin", "refs/heads/" + branch).stdout.split()[0]


def run(root):
    repo = root / "work"
    repo.mkdir()
    remote = root / "remote.git"
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "Shipping fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "config", "commit.gpgsign", "false")
    git(repo, "init", "--bare", str(remote))
    git(repo, "remote", "add", "origin", str(remote))
    base = commit_file(repo, "base.py", "BASE = 10\n")

    git(repo, "switch", "-c", "a")
    a = commit_file(repo, "alpha.txt", "alpha\n")
    git(repo, "switch", "-c", "b")
    b = commit_file(repo, "blocked_api.py", "def value():\n    return 42\n")
    git(repo, "switch", "-c", "c")
    c = commit_file(repo, "independent.py", "from base import BASE\nprint(BASE + 1)\n")
    cuts = {"a": base, "b": a, "c": b}
    original = {"a": a, "b": b, "c": c}
    identities = {name: patch_id(repo, cuts[name], head) for name, head in original.items()}
    git(repo, "push", "origin", "main", "a", "b", "c")

    git(repo, "switch", "-c", "extracted", base)
    git(repo, "cherry-pick", c)
    assert patch_id(repo, base, oid(repo, "HEAD")) == identities["c"]
    assert not (repo / "blocked_api.py").exists()
    assert command(sys.executable, "-B", "independent.py", cwd=repo).stdout == "11\n"
    git(repo, "switch", "-c", "dependent", b)
    dependent = commit_file(repo, "dependent.py", "from blocked_api import value\nprint(value())\n")
    assert command(sys.executable, "-B", "dependent.py", cwd=repo).stdout == "42\n"
    git(repo, "switch", "-c", "extracted-dependent", base)
    git(repo, "cherry-pick", dependent)
    failed = command(sys.executable, "-B", "dependent.py", cwd=repo, check=False)
    assert failed.returncode != 0 and "No module named 'blocked_api'" in failed.stderr
    print("PASS: conflict-free extraction can work or lose a runtime dependency; both need fresh assessment")

    expected = {"base.py"}
    for index, (name, added) in enumerate([
        ("a", "alpha.txt"), ("b", "blocked_api.py"), ("c", "independent.py"),
    ]):
        git(repo, "switch", "main")
        current_base, head = oid(repo, "main"), oid(repo, name)
        assert patch_id(repo, current_base, head) == identities[name]
        assert git(repo, "rev-list", "--count", current_base + ".." + head).stdout.strip() == "1"
        git(repo, "merge", "--squash", name)
        git(repo, "commit", "-m", "fixture: squash " + name)
        merged = oid(repo, "main")
        assert merged != head
        git(repo, "push", "origin", "main")
        git(repo, "fetch", "origin", "main")
        git(repo, "merge-base", "--is-ancestor", merged, "origin/main")
        expected.add(added)
        assert set(git(repo, "ls-tree", "--name-only", "main").stdout.splitlines()) == expected

        if index < 2:
            child = ["b", "c"][index]
            child_before = oid(repo, child)
            higher_before = oid(repo, "c")
            git(repo, "merge-base", "--is-ancestor", cuts[child], child)
            git(repo, "rebase", "--onto", merged, cuts[child], child)
            child_after = oid(repo, child)
            assert child_after != child_before
            assert patch_id(repo, merged, child_after) == identities[child]
            assert git(repo, "rev-list", "--count", merged + ".." + child).stdout.strip() == "1"
            git(repo, "push", "origin", f"--force-with-lease=refs/heads/{child}:{child_before}", f"{child}:refs/heads/{child}")
            assert published(repo, child) == child_after
            if child == "b":
                assert oid(repo, "c") == higher_before == c
                assert published(repo, "c") == c
                assert git(repo, "merge-base", "--is-ancestor", child_after, "c", check=False).returncode == 1
    print("PASS: three squash landings; only the immediate child moves; original cut points preserve one patch per PR")

    git(repo, "push", "origin", f"{b}:refs/heads/lease-probe")
    git(repo, "push", "origin", f"{c}:refs/heads/lease-probe")
    refused = git(repo, "push", "origin", f"--force-with-lease=refs/heads/lease-probe:{b}", "main:refs/heads/lease-probe", check=False)
    assert refused.returncode != 0 and "stale info" in refused.stderr
    assert published(repo, "lease-probe") == c
    print("PASS: a stale expected-ref lease rejects the push and preserves the competing writer's ref")

    try:
        patch_id(repo, "main", "main")
    except ValueError:
        pass
    else:
        raise AssertionError("An empty diff was accepted")
    assert patch_id(repo, base, "c") != identities["c"]
    print("PASS: empty identity is rejected and the wrong comparison base changes the patch identity")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="jstack-shipping-sequence-") as directory:
        run(Path(directory))
