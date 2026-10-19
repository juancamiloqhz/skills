#!/usr/bin/env python3
"""Preview or copy the dormant Benny pack; differing files require manual review."""

import argparse
import json
from pathlib import Path

PACK = Path(__file__).resolve().parents[2] / 'automations/jstack/benny'
DESTINATION = Path('.agents/automations/benny')


def plain_path(path):
    for entry in (path, *path.parents):
        if entry.is_symlink():
            raise ValueError(f'Symlink requires manual review: {entry}')
    return path


def copy_pack(source, target, *, apply=False):
    """Single-writer setup helper. Never replace a destination file or delete anything."""
    source = plain_path(source.absolute()).resolve(strict=True)
    target = plain_path(target.absolute()).resolve(strict=True)
    if not source.is_dir() or not target.is_dir():
        raise ValueError('Source pack and target repository must be existing directories')
    destination = plain_path(target / DESTINATION)
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError('Source and destination must be separate trees')
    required = ['FOR_AGENTS.md', 'README.md', 'LICENSE',
                'skills/setup-benny/SKILL.md', 'skills/triage-issue-reports/SKILL.md',
                'skills/reproduce-and-fix-issues/SKILL.md',
                'skills/triage-issue-reports/references/routing.example.md',
                'skills/reproduce-and-fix-issues/references/control-adapter.md',
                'skills/reproduce-and-fix-issues/references/feature-map.example.md',
                'skills/reproduce-and-fix-issues/references/verify-existing-fix.md',
                'templates/configuration.example.yaml', 'templates/triage-automation-prompt.md',
                'templates/reproduce-automation-prompt.md']
    if any(not (source / p).is_file() for p in required):
        raise ValueError('Source is not a complete Benny pack')
    additions, same, conflicts = [], [], []
    for entry in sorted(source.rglob('*')):
        plain_path(entry)
        if entry.is_dir():
            continue
        if not entry.is_file():
            raise ValueError(f'Not a regular pack file: {entry}')
        relative = entry.relative_to(source)
        output = plain_path(destination / relative)
        for parent in output.parents:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f'Destination parent is not a directory: {parent}')
        if output.exists():
            if output.is_file() and output.read_bytes() == entry.read_bytes():
                same.append(str(relative))
            else:
                conflicts.append(str(relative))
        else:
            additions.append(str(relative))
    report = dict(destination=str(destination), added=[], missing=additions,
                  matching=same, conflicts=conflicts,
                  outcome='conflicts' if conflicts else 'preview')
    if apply and not conflicts:
        for relative in additions:
            output = plain_path(destination / relative)
            output.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects a file added after the preview.
            with output.open('xb') as stream:
                stream.write((source / relative).read_bytes())
            report['added'].append(relative)
        report.update(outcome='copied', missing=[])
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=PACK)
    parser.add_argument('--target-root', type=Path, required=True)
    parser.add_argument('--apply', action='store_true', help='Copy missing files only if there are no conflicts')
    args = parser.parse_args()
    try:
        result = copy_pack(args.source, args.target_root, apply=args.apply)
    except (OSError, ValueError) as error:
        print(json.dumps(dict(outcome='incomplete', error=str(error))))
        return 2
    print(json.dumps(result, indent=2))
    return int(bool(result['conflicts']))


if __name__ == '__main__':
    raise SystemExit(main())
