#!/usr/bin/env python3
"""Reproduce the coverage census from Git objects; do not execute upstream code."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess


UPSTREAM = "0148b78c56c72a1b8412055913c79f767095b217"
LOCAL = "1f5a8d7184d24a0d95be9626ae63642c4163e09d"


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def paths(repo, revision, prefix):
    return set(filter(None, git(repo, "ls-tree", "-r", "--name-only", "-z", revision, "--", prefix).split("\0")))


def census(upstream, upstream_ref, local, local_ref):
    upstream_ref = git(upstream, "rev-parse", upstream_ref + "^{commit}").strip()
    local_ref = git(local, "rev-parse", local_ref + "^{commit}").strip()
    manifest = json.loads(git(local, "show", f"{local_ref}:research/jstack/upstream.json"))
    mappings = {s["upstreamPath"]: s for s in manifest["skills"]}
    source_files = paths(upstream, upstream_ref, "pstack")
    local_files = paths(local, local_ref, "skills/jstack")
    groups = Counter()
    for path in sorted(source_files):
        if path.startswith("pstack/skills/"):
            package = "/".join(path.split("/")[:3])
            group = "mapped skill trees" if package in mappings else "external Unslop" if package.endswith("/unslop") else "unported skill trees"
        elif path.startswith("pstack/automations/"):
            group = "automations"
        elif path.startswith("pstack/docs/"):
            group = "docs"
        elif path.startswith("pstack/agents/"):
            group = "agents"
        elif path in {"pstack/.cursor-plugin/plugin.json", "pstack/.gitignore", "pstack/LICENSE", "pstack/README.md", "pstack/assets/logo.png", "pstack/plugin.json"}:
            group = "root and branding"
        else:
            raise ValueError(f"Unclassified pstack path: {path}")
        groups[group] += 1
    skills = sorted(p.rsplit("/", 1)[0] for p in source_files if p.endswith("/SKILL.md") and p.count("/") == 3)
    mapped = []
    for path, skill in mappings.items():
        files = paths(upstream, upstream_ref, path)
        changed = list(filter(None, git(upstream, "diff", "--name-only", "-z", skill["adaptedFrom"], upstream_ref, "--", path).split("\0")))
        missing = [p for p in sorted(files) if skill["localPath"] + p[len(path):] not in local_files]
        mapped.append({"name": skill["name"], "source": path, "pin": skill["adaptedFrom"],
                       "sourceFileCount": len(files), "changedPaths": changed,
                       "sameRelativePathAbsent": missing})
    upstream_playbooks = {p.rsplit("/", 1)[1] for p in source_files if p.startswith("pstack/skills/poteto-mode/playbooks/")}
    local_playbooks = {p.rsplit("/", 1)[1] for p in local_files if p.startswith("skills/jstack/jstack-juan-mode/playbooks/")}
    nested = sorted(p for p in source_files if p.endswith("/SKILL.md") and p.count("/") != 3)
    return {"upstream": upstream_ref, "local": local_ref, "pstackFiles": len(source_files),
            "fileGroups": dict(sorted(groups.items())), "topLevelSkills": len(skills),
            "mappedPstackSkills": sum(p in mappings for p in skills),
            "unmappedSkills": [p for p in skills if p not in mappings], "nestedSkills": nested,
            "mappedPackages": mapped, "changedMappedPackages": sum(bool(p["changedPaths"]) for p in mapped),
            "changedMappedPaths": sum(len(p["changedPaths"]) for p in mapped),
            "playbooks": {"upstream": len(upstream_playbooks), "local": len(local_playbooks),
                          "missing": sorted(upstream_playbooks - local_playbooks)},
            "generatedHarnessFiles": len(paths(upstream, upstream_ref, "harness/pstack"))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True, help="Local Git clone containing the audited revision and source pins")
    parser.add_argument("--upstream-ref", default=UPSTREAM)
    parser.add_argument("--local", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--local-ref", default=LOCAL)
    args = parser.parse_args()
    print(json.dumps(census(args.upstream, args.upstream_ref, args.local, args.local_ref), indent=2))


if __name__ == "__main__":
    main()
