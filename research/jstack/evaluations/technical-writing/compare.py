#!/usr/bin/env python3
"""Compare the complete writing package, mode caller and external Unslop dependency."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

BASE = '7490738e484e81824538ea75aab238b0090223a8'
PIN = '11713c683fe4add4fd403ea880580abbc9e0875f'
ROOT = Path(__file__).resolve().parents[4]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def difference(before, after, left, right):
    return ''.join(difflib.unified_diff(before.decode().splitlines(True),
                                      after.decode().splitlines(True), fromfile=left, tofile=right))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=Path.home()/'.cache/jstack/upstream/upstream.git')
    parser.add_argument('--unslop', type=Path, default=Path('/home/ubuntu/.agents/skills/unslop/SKILL.md'))
    args = parser.parse_args()

    def source(path):
        return subprocess.check_output(['git', '--git-dir='+str(args.cache), 'show', PIN+':'+path])

    def baseline(path):
        return subprocess.check_output(['git', '-C', str(ROOT), 'show', BASE+':'+path])

    manifest = json.loads((ROOT/'research/jstack/upstream.json').read_text())
    before_manifest = json.loads(baseline('research/jstack/upstream.json'))
    assert {k: v for k, v in manifest.items() if k != 'skills'} == {
        k: v for k, v in before_manifest.items() if k != 'skills'}
    for old in before_manifest['skills']:
        current = next(s for s in manifest['skills'] if s['name'] == old['name'])
        expected = dict(old)
        if old['name'] == 'jstack-juan-mode':
            expected['contextPaths'] = old['contextPaths'] + ['pstack/skills/technical-writing',
                                                           'pstack/skills/unslop']
        assert current == expected, old['name']
    assert len(manifest['skills']) == len(before_manifest['skills']) + 1
    records = []
    for name in ['jstack-technical-writing', 'jstack-juan-mode']:
        skill = next(s for s in manifest['skills'] if s['name'] == name)
        assert skill['adaptedFrom'] == PIN
        upstream = skill['upstreamPath']+'/SKILL.md'
        local = skill['localPath']+'/SKILL.md'
        before, after = source(upstream), (ROOT/local).read_bytes()
        assert (ROOT/skill['localPath']/'LICENSE').read_bytes() == source('pstack/LICENSE')
        record = {'name': name, 'pin': PIN, 'upstreamPath': upstream, 'localPath': local,
                  'upstreamSha256': digest(before), 'localSha256': digest(after),
                  'licenseMatchesPin': True, 'fullSourceDiff': difference(before, after, upstream, local)}
        if name == 'jstack-technical-writing':
            inventory = subprocess.check_output(['git', '--git-dir='+str(args.cache), 'ls-tree', '-r',
                                                 '--name-only', PIN, skill['upstreamPath']], text=True).splitlines()
            assert inventory == [upstream]
            assert sorted(p.name for p in (ROOT/skill['localPath']).iterdir()) == ['LICENSE', 'SKILL.md']
            record['completeSourceInventory'] = inventory
        else:
            old = baseline(local)
            expected = old.replace(b'**technical-writing** skill (`/technical-writing`)',
                                   b'**jstack-technical-writing** skill (`/jstack-technical-writing`)').replace(
                b'jstack-show-me-your-work and jstack-benchmark-checklist separately.',
                b'jstack-show-me-your-work, jstack-benchmark-checklist and jstack-technical-writing separately.').replace(
                b'Technical-writing and no-comments are not yet packaged by jstack;',
                b'No-comments is not yet packaged by jstack;')
            assert after == expected
            record['diffFromMergedBase'] = difference(old, after, BASE+':'+local, local)
            for path in (ROOT/skill['localPath']).rglob('*'):
                if path.is_file() and '__pycache__' not in path.parts and path.name != 'SKILL.md':
                    assert path.read_bytes() == baseline(str(path.relative_to(ROOT)))
            record['supportFilesUnchanged'] = True
        records.append(record)
    upstream = source('pstack/skills/unslop/SKILL.md')
    installed = args.unslop.read_bytes()
    records.append({'name': 'external-unslop', 'pin': PIN,
                    'upstreamPath': 'pstack/skills/unslop/SKILL.md', 'installedPath': str(args.unslop),
                    'upstreamSha256': digest(upstream), 'installedSha256': digest(installed),
                    'fullSourceDiff': difference(upstream, installed, 'pinned unslop', str(args.unslop))})
    print(json.dumps({'base': BASE, 'checkpointAndExistingPinsPreserved': True,
                      'files': records}, indent=2))


if __name__ == '__main__':
    main()
