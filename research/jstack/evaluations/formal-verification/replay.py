"""Replay the evaluated generated lease verifier in a fresh owned repository."""

import argparse
from pathlib import Path
import subprocess
import sys

from make_fixture import create


def run(root, *args):
    result = subprocess.run([sys.executable, "-B", *args], cwd=root, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def replay(root):
    root.mkdir(parents=True, exist_ok=False)
    repo = root / "lease"
    create(repo)
    product_paths = ["lease.py", "display.py", "README.md", "tests/test_lease.py"]
    original = {name: (repo / name).read_bytes() for name in product_paths}
    patch = Path(__file__).with_name("solution.patch").resolve()
    subprocess.run(["git", "-C", str(repo), "apply", str(patch)], check=True)
    skill = repo / ".agents/skills/verify-lease-formal"
    linked = repo / ".claude/skills/verify-lease-formal"
    assert linked.is_symlink() and linked.resolve() == skill.resolve()
    for name in ["SKILL.md", "check.py", "mutation_check.py"]:
        assert (linked / name).resolve() == (skill / name).resolve()
    output = run(repo, str(skill / "check.py"))
    assert "reachable_states=15 evaluated_transitions=30" in output, output
    print(output.strip())
    mutation = run(repo, str(skill / "mutation_check.py"), "--scratch-root", str(root / "mutation"))
    assert "removed acquisition recheck: exit=1" in mutation, mutation
    assert "phases=('holding', 'holding')" in mutation, mutation
    assert "restored copy: exit=0" in mutation, mutation
    assert not list((root / "mutation").iterdir())
    print("Mutation rejected with two holders; restored copy passes; temporary mutation files removed")
    assert run(repo, str(linked / "check.py")) == output
    run(repo, "-m", "unittest", "discover", "-s", "tests")
    assert all((repo / name).read_bytes() == data for name, data in original.items())
    print("Claude link resolves all generated files; linked check and original test pass; product unchanged")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="New task-owned directory outside the skills checkout")
    replay(parser.parse_args().path.resolve())
