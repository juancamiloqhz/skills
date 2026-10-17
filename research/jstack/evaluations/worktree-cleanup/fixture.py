from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[4]
AUDIT = ROOT / "skills/jstack/jstack-juan-mode/scripts/worktree-audit.sh"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE, text=True).strip()


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "Cleanup Fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    (repo / "app.txt").write_text("Merged application.\n")
    (repo / ".gitignore").write_text("cache/\n")
    git(repo, "add", "app.txt", ".gitignore")
    git(repo, "commit", "-m", "test: seed cleanup fixture")
    head = git(repo, "rev-parse", "HEAD")
    paths = {}
    for key, name in [("merged", "merged space"), ("closed", "closed-unmerged"), ("active", "detached-active"),
                      ("untracked", "valuable-untracked"), ("ignored", "ignored-cache"), ("wip", "tracked-wip"),
                      ("open", "open-pr"), ("locked", "locked"), ("unknown", "unknown-owner"),
                      ("stale", "stale-owner"), ("newline", "merged\nline")]:
        path = root / name
        git(repo, "worktree", "add", *( ["--detach"] if key == "active" else ["-b", key] ), str(path), "main")
        paths[key] = str(path)
    closed = Path(paths["closed"])
    (closed / "unique.txt").write_text("Unmerged work.\n")
    git(closed, "add", "unique.txt")
    git(closed, "commit", "-m", "feat: unmerged change")
    (Path(paths["untracked"]) / "valuable.py").write_text("print('user source')\n")
    cache = Path(paths["ignored"]) / "cache"
    cache.mkdir()
    (cache / "valuable.db").write_bytes(b"not-known-to-be-disposable\n")
    (Path(paths["wip"]) / "app.txt").write_text("Uncommitted implementation.\n")
    git(repo, "worktree", "lock", paths["locked"], "--reason", "fixture owner")
    git(repo, "update-ref", "refs/remotes/origin/merged", head)
    now = datetime.now(timezone.utc).isoformat()
    usage = []
    for key, path in paths.items():
        if key == "unknown":
            continue
        usage.append(dict(path=path, head="0" * 40 if key == "stale" else git(path, "rev-parse", "HEAD"),
                          state="active" if key == "active" else "unused", source="Synthetic fixture ownership, not live T3 state", observedAt=now))
    (root / "usage.json").write_text(json.dumps(usage, indent=2) + "\n")
    (root / "prs.json").write_text(json.dumps([dict(number=1, headRefName="closed", state="CLOSED"), dict(number=2, headRefName="open", state="OPEN")], indent=2) + "\n")
    manifest = dict(repo=str(repo), base=head, paths=paths, usage=str(root / "usage.json"), prs=str(root / "prs.json"))
    (root / "fixture.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def audit(root, manifest, *extra, expected=0):
    command = ["bash", str(AUDIT), manifest["repo"], "--base-ref", "main", "--pr-json", manifest["prs"], "--usage-json", manifest["usage"], "--json", *extra]
    result = subprocess.run(command, capture_output=True, text=True)
    assert result.returncode == expected, (result.returncode, result.stderr)
    return json.loads(result.stdout) if result.stdout else None


def file_hashes(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in root.rglob("*") if p.is_file() and p.name not in ("fixture.json",)}


def check(root, manifest):
    before = file_hashes(root)
    result = audit(root, manifest)
    assert before == file_hashes(root), "audit mutated fixture files or Git metadata"
    rows = {r["path"]: r for r in result["worktrees"]}
    assert len(rows) == 12
    expected = dict(merged="candidate", closed="hold-unmerged", active="hold-in-use", untracked="hold-untracked", ignored="hold-ignored", wip="hold-tracked", open="hold-open-pr", locked="hold-registration", unknown="verify-usage", stale="verify-usage", newline="candidate")
    for name, verdict in expected.items():
        assert rows[manifest["paths"][name]]["bucket"] == verdict, (name, rows[manifest["paths"][name]])
    assert rows[manifest["repo"]]["bucket"] == "hold-current-or-main"
    assert rows[manifest["paths"]["active"]]["branch"] is None
    assert rows[manifest["paths"]["untracked"]]["changes"]["untracked"] == ["valuable.py"]
    assert "cache/" in rows[manifest["paths"]["ignored"]]["changes"]["ignored"]
    assert rows[manifest["paths"]["merged"]]["remote"] == "pushed"
    table = subprocess.check_output(["bash", str(AUDIT), manifest["repo"], "--base-ref", "main"], text=True)
    assert len(table.splitlines()) == 13 and 'merged\\nline' in table
    linked = audit(root, {**manifest, "repo": manifest["paths"]["merged"]})
    assert next(r for r in linked["worktrees"] if r["path"] == manifest["paths"]["merged"])["bucket"] == "hold-current-or-main"
    pr_path = Path(manifest["prs"])
    original_prs = pr_path.read_text()
    pr_path.write_text(original_prs.replace('"CLOSED"', '"MERGED"'))
    assert next(r for r in audit(root, manifest)["worktrees"] if r["path"] == manifest["paths"]["closed"])["bucket"] == "hold-unmerged"
    pr_path.write_text(original_prs)
    audit(root, manifest, "--base-ref", "missing-base", expected=1)
    broken = root / "invalid.json"
    broken.write_text('[{"path":"relative"}]\n')
    audit(root, manifest, "--usage-json", str(broken), expected=1)
    source = Path(manifest["paths"]["unknown"])
    moved = root / "offline-retained"
    source.rename(moved)
    missing = audit(root, manifest, expected=2)
    assert next(r for r in missing["worktrees"] if r["path"] == str(source))["errors"]
    source.symlink_to(moved, target_is_directory=True)
    aliased = audit(root, manifest, expected=2)
    assert next(r for r in aliased["worktrees"] if r["path"] == str(source))["bucket"] == "hold-incomplete"
    source.unlink()
    moved.rename(source)
    candidate = manifest["paths"]["merged"]
    drift = Path(candidate) / "late-user-file.txt"
    drift.write_text("Arrived after the first audit.\n")
    assert next(r for r in audit(root, manifest)["worktrees"] if r["path"] == candidate)["bucket"] == "hold-untracked"
    drift.unlink()
    latest = {r["path"]: r for r in audit(root, manifest)["worktrees"]}
    assert latest[candidate]["bucket"] == "candidate"
    git(manifest["repo"], "worktree", "remove", "--", candidate)
    assert not Path(candidate).exists()
    assert git(manifest["repo"], "rev-parse", "merged") == manifest["base"]
    assert all(Path(p).exists() for key, p in manifest["paths"].items() if key != "merged")
    remaining = audit(root, manifest)
    assert len(remaining["worktrees"]) == 11
    print("PASS: complete NUL-delimited inventory; 12 classifications; unchanged bytes and Git metadata; invalid input/base and missing path held; one scoped removal preserves refs and every other tree")


if __name__ == "__main__":
    directory = Path(sys.argv[1]).resolve()
    state = create(directory)
    if "--check" in sys.argv[2:]:
        check(directory, state)
    print(directory / "fixture.json")
