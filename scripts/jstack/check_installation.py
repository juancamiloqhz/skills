#!/usr/bin/env python3
"""Compare installed package bytes with Git-tracked files in this checkout."""

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import subprocess


def compare(repo, installed):
    if not installed.is_dir():
        raise ValueError(f"Installed root is not a directory: {installed}")
    manifest = json.loads((repo / "research/jstack/upstream.json").read_text())
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be an object")
    skills = manifest.get("skills")
    if not isinstance(skills, list) or not skills:
        raise ValueError("Manifest must contain a nonempty skills list")
    tracked = set(subprocess.check_output(
        ["git", "-C", str(repo), "ls-files", "-z"], text=True
    ).split("\0"))
    packages = []
    names = set()
    for skill in skills:
        if not isinstance(skill, dict):
            raise ValueError("Invalid manifest skill")
        name, local = skill.get("name"), skill.get("localPath")
        if not isinstance(name, str) or not re.fullmatch(r"jstack-[a-z0-9-]+", name) or name in names:
            raise ValueError(f"Invalid or duplicate skill name: {name!r}")
        names.add(name)
        if not isinstance(local, str) or PurePosixPath(local).is_absolute() or ".." in PurePosixPath(local).parts or local != f"skills/jstack/{name}":
            raise ValueError(f"Invalid package path: {local!r}")
        if f"{local}/SKILL.md" not in tracked:
            raise ValueError(f"Package has no tracked SKILL.md: {local}")
        files = sorted(p[len(local) + 1:] for p in tracked if p.startswith(local + "/"))
        missing, changed = [], []
        for relative in files:
            source = (repo / local / relative).read_bytes()
            try:
                target = (installed / name / relative).read_bytes()
            except FileNotFoundError:
                missing.append(relative)
            else:
                if source != target:
                    changed.append(relative)
        status = "missing" if "SKILL.md" in missing else "different" if missing or changed else "matching"
        packages.append(dict(name=name, status=status, missingFiles=missing, changedFiles=changed))
    return dict(outcome="complete", packages=packages,
                summary={status: sum(p["status"] == status for p in packages)
                         for status in ("matching", "missing", "different")})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--installed-root", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = compare(args.repo_root.resolve(), args.installed_root.expanduser().resolve())
        code = int(bool(report["summary"]["missing"] or report["summary"]["different"]))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        report, code = dict(outcome="incomplete", error=str(error)), 2
    if args.json:
        print(json.dumps(report, indent=2))
    elif code == 2:
        print(f"Incomplete: {report['error']}")
    else:
        print(", ".join(f"{count} {status}" for status, count in report["summary"].items()))
        for package in report["packages"]:
            if package["status"] != "matching":
                print(f"{package['name']}: {package['status']} "
                      f"({len(package['missingFiles'])} missing files, {len(package['changedFiles'])} changed files)")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
