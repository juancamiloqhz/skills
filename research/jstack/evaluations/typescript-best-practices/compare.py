#!/usr/bin/env python3
"""Compare the complete TypeScript package and its principle caller with pinned source."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

BASE = '39da90d4d922be87e24bbbd0a8346ad81a8a4b84'
PIN = '11713c683fe4add4fd403ea880580abbc9e0875f'
ROOT = Path(__file__).resolve().parents[4]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=Path.home()/'.cache/jstack/upstream/upstream.git')
    args = parser.parse_args()

    def source(path):
        return subprocess.check_output(['git', '--git-dir='+str(args.cache), 'show', PIN+':'+path])

    def baseline(path):
        return subprocess.check_output(['git', '-C', str(ROOT), 'show', BASE+':'+path])

    def difference(a, b, left, right):
        return ''.join(difflib.unified_diff(a.decode().splitlines(True), b.decode().splitlines(True),
                                          fromfile=left, tofile=right))

    path = 'research/jstack/upstream.json'
    before, after = json.loads(baseline(path)), json.loads((ROOT/path).read_text())
    assert {k: v for k, v in before.items() if k != 'skills'} == {k: v for k, v in after.items() if k != 'skills'}
    assert len(after['skills']) == len(before['skills'])+1
    for old in before['skills']:
        expected = dict(old)
        if old['name'] == 'jstack-principle-type-system-discipline':
            expected['contextPaths'] = list(old['contextPaths'])
            if 'pstack/skills/typescript-best-practices' not in expected['contextPaths']:
                expected['contextPaths'].append('pstack/skills/typescript-best-practices')
        assert next(s for s in after['skills'] if s['name'] == old['name']) == expected
    package = 'skills/jstack/jstack-typescript-best-practices'
    upstream = 'pstack/skills/typescript-best-practices'
    inventory = subprocess.check_output(['git', '--git-dir='+str(args.cache), 'ls-tree', '-r', '--name-only', PIN, upstream], text=True).splitlines()
    assert inventory == [upstream+'/SKILL.md', upstream+'/references/patterns.md']
    assert sorted(str(p.relative_to(ROOT/package)) for p in (ROOT/package).rglob('*') if p.is_file()) == ['LICENSE', 'SKILL.md', 'references/patterns.md']
    assert (ROOT/package/'LICENSE').read_bytes() == source('pstack/LICENSE')
    caller = 'skills/jstack/jstack-principle-type-system-discipline/SKILL.md'
    old, current = baseline(caller), (ROOT/caller).read_bytes()
    assert current == old.replace(b'`typescript-best-practices` skill', b'`jstack-typescript-best-practices` skill')
    pairs = [(p, package+p.removeprefix(upstream)) for p in inventory]
    pairs.append(('pstack/skills/principle-type-system-discipline/SKILL.md', caller))
    records = []
    for src, local in pairs:
        a, b = source(src), (ROOT/local).read_bytes()
        records.append({'upstreamPath': src, 'localPath': local, 'upstreamSha256': hashlib.sha256(a).hexdigest(),
                        'localSha256': hashlib.sha256(b).hexdigest(), 'fullSourceDiff': difference(a, b, src, local)})
    print(json.dumps({'base': BASE, 'pin': PIN, 'completeSourceInventory': inventory,
                      'licenseMatchesPin': True, 'checkpointAndExistingPinsPreserved': True,
                      'callerDiffFromBase': difference(old, current, BASE+':'+caller, caller), 'files': records}, indent=2))


if __name__ == '__main__':
    main()
