import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def run(args, timeout=30):
    return subprocess.check_output(args, env={**os.environ, "GIT_OPTIONAL_LOCKS": "0"}, stderr=subprocess.PIPE, timeout=timeout)


def git(repo, *args):
    return run(["git", "-c", "core.fsmonitor=false", "-C", str(repo), *args])


def records(data):
    result, entry = [], {}
    for field in data.decode(errors="surrogateescape").split("\0"):
        if not field:
            if entry:
                result.append(entry)
                entry = {}
            continue
        key, _, value = field.partition(" ")
        entry[key] = value
    if entry:
        result.append(entry)
    return result


def snapshot(path, kind):
    if path is None:
        return []
    rows = json.loads(path.read_text())
    if not isinstance(rows, list):
        raise ValueError(f"{kind} snapshot must be a list")
    seen = set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"invalid {kind} record")
        if kind == "PR":
            if not isinstance(row.get("headRefName"), str) or row.get("state") not in ("OPEN", "CLOSED", "MERGED"):
                raise ValueError("PR records need headRefName and OPEN/CLOSED/MERGED state")
        else:
            if not all(isinstance(row.get(k), str) and row[k] for k in ("path", "head", "source", "observedAt")):
                raise ValueError("usage records need path, head, source and observedAt")
            if not Path(row["path"]).is_absolute() or row["state"] not in ("active", "pinned", "unused", "unknown"):
                raise ValueError("invalid usage path or state")
            key = str(Path(row["path"]).resolve())
            if key in seen:
                raise ValueError("duplicate usage path")
            seen.add(key)
            stamp = datetime.fromisoformat(row["observedAt"].replace("Z", "+00:00"))
            if stamp.tzinfo is None or stamp.timestamp() > time.time() + 60:
                raise ValueError("usage observedAt must be a past timestamp with timezone")
    return rows


def changes(repo):
    fields = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored=matching").decode(errors="surrogateescape").split("\0")
    result = {"tracked": [], "untracked": [], "ignored": []}
    i = 0
    while i < len(fields):
        field = fields[i]
        i += 1
        if not field:
            continue
        code, name = field[:2], field[3:]
        result["untracked" if code == "??" else "ignored" if code == "!!" else "tracked"].append(name)
        if "R" in code or "C" in code:
            i += 1
    return result


def bucket(row):
    if row["main"] or row["current"]:
        return "hold-current-or-main"
    if row["locked"] or row["prunable"] or row["bare"]:
        return "hold-registration"
    if row["errors"]:
        return "hold-incomplete"
    for kind in ("tracked", "untracked", "ignored"):
        if row["changes"][kind]:
            return "hold-" + kind
    if any(pr["state"] == "OPEN" for pr in row["prs"]):
        return "hold-open-pr"
    if row["usage"] in ("active", "pinned"):
        return "hold-in-use"
    if not row["merged"]:
        return "hold-unmerged"
    if row["usage"] != "unused":
        return "verify-usage"
    return "candidate"


def audit(repo, base_ref, prs, usage):
    base = git(repo, "rev-parse", "--verify", base_ref + "^{commit}").decode().strip()
    current = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    common = Path(git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip()).resolve()
    inventory = records(git(repo, "worktree", "list", "--porcelain", "-z"))
    rows = []
    for index, entry in enumerate(inventory):
        path = Path(entry["worktree"])
        branch = entry.get("branch", "").removeprefix("refs/heads/")
        row = dict(path=str(path), head=entry.get("HEAD"), branch=branch or None,
                   main=index == 0, current=path.resolve() == current,
                   locked="locked" in entry, prunable="prunable" in entry, bare="bare" in entry,
                   sizeKiB=None, ageDays=None, merged=False, changes={}, remote="detached" if not branch else "no-remote",
                   prs=[p for p in prs if p["headRefName"] == branch], usage="unknown", usageEvidence=None, errors=[])
        evidence = next((u for u in usage if Path(u["path"]).resolve() == path.resolve()), None)
        if evidence:
            row["usageEvidence"] = evidence
            if evidence["head"] == row["head"]:
                row["usage"] = evidence["state"]
        try:
            if path.is_symlink():
                raise ValueError("registered worktree path is a symlink")
            if Path(git(path, "rev-parse", "--show-toplevel").decode().strip()).resolve() != path.resolve():
                raise ValueError("registered path is not this checkout root")
            if Path(git(path, "rev-parse", "--path-format=absolute", "--git-common-dir").decode().strip()).resolve() != common:
                raise ValueError("registered path belongs to a different repository")
            if git(path, "rev-parse", "HEAD").decode().strip() != row["head"]:
                raise ValueError("HEAD changed during inventory")
            row["changes"] = changes(path)
            row["sizeKiB"] = int(run(["du", "-sk", str(path)]).split()[0])
            stamp = int(git(path, "log", "-1", "--format=%ct", "HEAD"))
            row["ageDays"] = max(0, int((time.time() - stamp) // 86400))
            try:
                git(repo, "merge-base", "--is-ancestor", row["head"], base)
                row["merged"] = True
            except subprocess.CalledProcessError as error:
                if error.returncode != 1:
                    raise
            if branch:
                ref = "refs/remotes/origin/" + branch
                found = git(repo, "for-each-ref", "--format=%(objectname)", ref).decode().splitlines()
                if found:
                    remote = git(repo, "rev-parse", "--verify", ref).decode().strip()
                    ahead = int(git(repo, "rev-list", "--count", remote + ".." + row["head"]))
                    behind = int(git(repo, "rev-list", "--count", row["head"] + ".." + remote))
                    row["remote"] = "pushed" if remote == row["head"] else f"ahead:{ahead}/behind:{behind}"
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            row["errors"].append(str(error))
        row["bucket"] = bucket(row)
        rows.append(row)
    rows.sort(key=lambda r: r["sizeKiB"] if r["sizeKiB"] is not None else -1, reverse=True)
    return dict(observedAt=datetime.now(timezone.utc).isoformat(), baseRef=base_ref, baseCommit=base,
                advisoryOnly=True, prEvidence="supplied" if prs else "unavailable-or-empty", worktrees=rows)


def main():
    parser = argparse.ArgumentParser(description="Read-only advisory worktree audit; never fetches or deletes.")
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--pr-json", type=Path)
    parser.add_argument("--usage-json", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = audit(args.repo, args.base_ref, snapshot(args.pr_json, "PR"), snapshot(args.usage_json, "usage"))
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
        print(f"incomplete audit: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("SIZE_KIB\tAGE_DAYS\tMERGED\tDIRTY\tREMOTE\tPR\tLAST_CHAT\tBUCKET\tWORKTREE")
        for row in result["worktrees"]:
            dirty = ",".join(f"{k}:{len(v)}" for k, v in row["changes"].items() if v) or ("unknown" if row["errors"] else "clean")
            pr = ",".join(f"#{p.get('number', '?')}/{p['state']}" for p in row["prs"]) or "unknown"
            chat = (row["usageEvidence"] or {}).get("lastChat", "unknown")
            print("\t".join(str(v) for v in (row["sizeKiB"], row["ageDays"], row["merged"], dirty, row["remote"], pr, json.dumps(chat), row["bucket"], json.dumps(row["path"]))))
    return 2 if any(r["errors"] for r in result["worktrees"]) else 0


if __name__ == "__main__":
    sys.exit(main())
