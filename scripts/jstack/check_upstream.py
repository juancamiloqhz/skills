#!/usr/bin/env python3
"""Detect upstream changes without editing skills or advancing review decisions."""

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[2]
SHA = re.compile(r"[0-9a-f]{40}")


class CheckError(Exception):
    pass


def git(directory, *args, allowed=(0,)):
    result = subprocess.run(
        ["git", "--literal-pathspecs", "-c", "core.hooksPath=/dev/null", "-c", "protocol.ext.allow=never",
         "-C", str(directory), *args],
        capture_output=True, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        timeout=120,
    )
    if result.returncode not in allowed:
        # Git stderr can contain credential-bearing URLs supplied by local config.
        raise CheckError(f"git {args[0]} failed (exit {result.returncode}); check source access and history")
    return result


def revision(value):
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise CheckError("revision must be a full lowercase 40-character commit SHA")
    return value


def relative_path(value):
    if (not isinstance(value, str) or not value or value.startswith("-")
            or PurePosixPath(value).is_absolute()
            or any(p in ("", ".", "..") for p in value.split("/"))
            or any(c in value for c in "*?[]:\\\n\r\0")):
        raise CheckError("manifest paths must be literal repository-relative paths")
    return value


def within(path, prefix):
    return path == prefix or path.startswith(prefix + "/")


def load_manifest(path, root):
    raw = path.read_bytes()
    m = json.loads(raw)
    if m["schemaVersion"] != 1:
        raise CheckError("unsupported manifest schemaVersion")
    source = m["repository"]
    # Local repositories support offline regression tests.
    if not (re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\.git", source)
            or Path(source).is_absolute()):
        raise CheckError("repository must be a GitHub HTTPS URL or absolute local fixture path")
    branch = m["branch"]
    if not isinstance(branch, str) or not branch or branch.startswith("-"):
        raise CheckError("invalid upstream branch")
    git(root, "check-ref-format", "refs/heads/" + branch)
    revision(m["initialRevision"])
    if m["reviewedThrough"] is not None:
        revision(m["reviewedThrough"])
    if not m["watchPaths"] or not m["skills"]:
        raise CheckError("watchPaths and skills must not be empty")
    for p in m["watchPaths"]:
        relative_path(p)
    names = set()
    for skill in [*m["skills"], *m.get("automationPacks", [])]:
        if not isinstance(skill["name"], str) or skill["name"] in names:
            raise CheckError("skill and automation pack names must be unique strings")
        names.add(skill["name"])
        revision(skill["adaptedFrom"])
        for key in ("localPath", "differences", "upstreamPath"):
            relative_path(skill[key])
        for p in [skill["upstreamPath"], *skill["contextPaths"]]:
            relative_path(p)
            if not any(within(p, w) for w in m["watchPaths"]):
                raise CheckError("every mapped upstream path must be watched")
        for key in ("localPath", "differences"):
            p = (root / skill[key]).resolve()
            if not p.is_relative_to(root) or not p.exists():
                raise CheckError("local package and attribution paths must exist inside the repository")
    ids = set()
    for d in m["decisions"]:
        if d["id"] in ids or d["disposition"] not in ("adopt", "adapt", "keep", "defer"):
            raise CheckError("decisions need unique IDs and a supported disposition")
        ids.add(d["id"])
        revision(d["from"])
        revision(d["to"])
        if not d["reason"] or not d["paths"]:
            raise CheckError("decisions need a reason and source paths")
        for p in d["paths"]:
            relative_path(p)
        report = root / relative_path(d["report"])
        if not report.resolve().is_relative_to(root) or not report.is_file():
            raise CheckError("decision report must exist inside the repository")
        if d.get("appliedCommit") is not None:
            revision(d["appliedCommit"])
            if d["disposition"] not in ("adopt", "adapt"):
                raise CheckError("only adopted or adapted changes can have an appliedCommit")
            git(root, "merge-base", "--is-ancestor", d["appliedCommit"], "refs/remotes/origin/main")
    return m, hashlib.sha256(raw).hexdigest()


def changes_from(raw):
    fields = raw.decode("utf-8").split("\0")
    changes = []
    i = 0
    while i < len(fields) - 1:
        status, old = fields[i:i + 2]
        i += 2
        change = {"status": status, "path": old}
        if status.startswith(("R", "C")):
            change.update(previousPath=old, path=fields[i])
            i += 1
        changes.append(change)
    return changes


def classify(changes, manifest):
    result = []
    for c in changes:
        paths = [c["path"], c.get("previousPath", c["path"])]
        if not any(within(p, w) for p in paths for w in manifest["watchPaths"]):
            continue
        c["directSkills"] = [s["name"] for s in manifest["skills"]
                             if any(within(p, s["upstreamPath"]) for p in paths)]
        c["contextSkills"] = [s["name"] for s in manifest["skills"]
                              if any(within(p, w) for p in paths for w in s["contextPaths"])]
        if manifest.get("automationPacks"):
            c["directAutomationPacks"] = [p["name"] for p in manifest["automationPacks"]
                                           if any(within(path, p["upstreamPath"]) for path in paths)]
            c["contextAutomationPacks"] = [p["name"] for p in manifest["automationPacks"]
                                            if any(within(path, w) for path in paths for w in p["contextPaths"])]
        result.append(c)
    return result


def atomic_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def encoded(data):
    return (json.dumps(data, indent=2, ensure_ascii=True) + "\n").encode()


@contextmanager
def cache_lock(cache, root):
    if cache.is_relative_to(root):
        raise CheckError("cache must be outside the jstack checkout")
    cache.mkdir(parents=True, exist_ok=True)
    with (cache / "check.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as e:
            raise CheckError("another upstream check is running in this cache") from e
        yield


def detect(args, cache):
    root = args.repo_root.resolve()
    m, manifest_hash = load_manifest(args.manifest, root)
    packages = [*m["skills"], *m.get("automationPacks", [])]
    local_paths = [s["localPath"] for s in packages]
    if git(root, "status", "--porcelain", "--", *local_paths).stdout:
        raise CheckError("commit or isolate local skill changes before reviewing upstream")
    jstack_commit = git(root, "rev-parse", "HEAD").stdout.decode().strip()
    source = cache / "upstream.git"
    if not source.exists():
        git(cache, "init", "--bare", str(source))
    if git(source, "rev-parse", "--is-bare-repository").stdout.strip() != b"true":
        raise CheckError("upstream cache must be a bare repository")
    git(source, "fetch", "--no-tags", "--no-recurse-submodules", m["repository"],
        f"+refs/heads/{m['branch']}:refs/heads/watched")
    base = revision(args.base or m["reviewedThrough"] or m["initialRevision"])
    live_head = git(source, "rev-parse", "refs/heads/watched").stdout.decode().strip()
    head = revision(args.head or live_head)
    for sha in (base, head):
        if git(source, "cat-file", "-e", sha + "^{commit}", allowed=(0, 1, 128)).returncode:
            git(source, "fetch", "--no-tags", "--no-recurse-submodules", m["repository"], sha)
    if git(source, "merge-base", "--is-ancestor", base, head, allowed=(0, 1)).returncode:
        raise CheckError("upstream history diverged or moved backwards; review the baseline explicitly")
    if git(source, "merge-base", "--is-ancestor", head, live_head, allowed=(0, 1)).returncode:
        raise CheckError("requested head is not part of the fetched branch history")
    raw = git(source, "diff", "--no-color", "--no-ext-diff", "--no-textconv", "--name-status", "-z",
              "--find-renames", base, head, "--").stdout
    changes = classify(changes_from(raw), m)
    missing = [s["upstreamPath"] for s in packages
               if not git(source, "ls-tree", head, "--", s["upstreamPath"]).stdout]
    # Include both sides of renames across the watched boundary in the saved diff.
    diff_paths = sorted({p for c in changes for p in (c["path"], c.get("previousPath", c["path"]))})
    patch = (git(source, "diff", "--no-color", "--no-ext-diff", "--no-textconv", "--find-renames",
                 base, head, "--", *diff_paths).stdout if diff_paths else b"")
    pending = [d for d in m["decisions"]
               if d["disposition"] in ("adopt", "adapt", "defer") and not d.get("appliedCommit")]
    identity = {"checkerVersion": 1, "repository": m["repository"], "base": base,
                "head": head, "jstackCommit": jstack_commit, "manifestSha256": manifest_hash}
    report_id = hashlib.sha256(encoded(identity)).hexdigest()[:20]
    report = {**identity, "reportId": report_id,
              "status": "changes" if changes or missing else "no_changes",
              "reviewStatus": "not_reviewed", "changes": changes,
              "missingSources": missing, "pendingDecisions": pending,
              "patchSha256": hashlib.sha256(patch).hexdigest()}
    if m["repository"].startswith("https://github.com/"):
        report["compareUrl"] = m["repository"][:-4] + f"/compare/{base}...{head}"
    report_file = cache / "reports" / (report_id + ".json")
    patch_file = report_file.with_suffix(".patch")
    reused = report_file.exists()
    if reused and report_file.read_bytes() != encoded(report):
        raise CheckError("existing report differs for the same identity; preserve it and investigate")
    atomic_write(patch_file, patch)
    if not reused:
        atomic_write(report_file, encoded(report))
    return {"status": report["status"], "reportId": report_id, "reused": reused,
            "base": base, "head": head, "changedFiles": len(changes),
            "directSkills": sorted({s for c in changes for s in c["directSkills"]}),
            "directAutomationPacks": sorted({p for c in changes for p in c.get("directAutomationPacks", [])}),
            "pendingDecisions": len(pending), "missingSources": missing,
            "report": str(report_file), "patch": str(patch_file)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, help="default: research/jstack/upstream.json in repo-root")
    parser.add_argument("--cache-dir", type=Path, default=Path.home() / ".cache/jstack/upstream")
    parser.add_argument("--base", help="full SHA for a historical trial; does not advance reviewedThrough")
    parser.add_argument("--head", help="full SHA for a reproducible trial; default: freshly fetched branch head")
    args = parser.parse_args()
    args.manifest = args.manifest or args.repo_root / "research/jstack/upstream.json"
    cache = args.cache_dir.resolve()
    try:
        with cache_lock(cache, args.repo_root.resolve()):
            try:
                result = detect(args, cache)
            except (CheckError, OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as e:
                result = {"status": "error", "error": str(e)}
            atomic_write(cache / "last-run.json", encoded({
                **result, "checkedAt": datetime.now(timezone.utc).isoformat()}))
    except (CheckError, OSError) as e:
        result = {"status": "error", "error": str(e)}
    print(json.dumps(result))
    return 2 if result["status"] == "error" else 0


if __name__ == "__main__":
    sys.exit(main())
