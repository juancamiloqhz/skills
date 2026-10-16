#!/usr/bin/env python3
"""Retain complete pinned source diffs and check unchanged caller support and pins."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

BASE = '75a16ff2e022bcacffc8dfd469a2f6138fcad4ab'
PIN = '11713c683fe4add4fd403ea880580abbc9e0875f'
ROOT = Path(__file__).resolve().parents[4]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, default=Path.home()/'.cache/jstack/upstream/upstream.git')
    args = parser.parse_args()

    def upstream(path):
        return subprocess.check_output(['git', '--git-dir='+str(args.cache), 'show', PIN+':'+path])

    def baseline(path):
        return subprocess.check_output(['git', '-C', str(ROOT), 'show', BASE+':'+path])

    def diff(a, b, left, right):
        return ''.join(difflib.unified_diff(a.decode().splitlines(True), b.decode().splitlines(True),
                                          fromfile=left, tofile=right))

    manifest = json.loads((ROOT/'research/jstack/upstream.json').read_text())
    old = json.loads(baseline('research/jstack/upstream.json'))
    assert {k: v for k, v in manifest.items() if k != 'skills'} == {
        k: v for k, v in old.items() if k != 'skills'}
    assert len(manifest['skills']) == len(old['skills']) + 1
    for previous in old['skills']:
        expected = dict(previous)
        if previous['name'] == 'jstack-juan-mode':
            expected['contextPaths'] = previous['contextPaths'] + ['pstack/skills/no-comments',
                                                                  'pstack/agents/comment-sicko.md']
        assert next(s for s in manifest['skills'] if s['name'] == previous['name']) == expected
    package = 'skills/jstack/jstack-no-comments'
    assert sorted(str(p.relative_to(ROOT/package)) for p in (ROOT/package).rglob('*') if p.is_file()) == [
        'LICENSE', 'SKILL.md', 'agents/comment-sicko.md', 'references/execution.md']
    inventory = subprocess.check_output(['git', '--git-dir='+str(args.cache), 'ls-tree', '-r', '--name-only',
                                         PIN, 'pstack/skills/no-comments', 'pstack/agents/comment-sicko.md'], text=True).splitlines()
    assert inventory == ['pstack/agents/comment-sicko.md', 'pstack/skills/no-comments/SKILL.md']
    records = []
    pairs = [('pstack/skills/no-comments/SKILL.md', package+'/SKILL.md'),
             ('pstack/agents/comment-sicko.md', package+'/agents/comment-sicko.md'),
             ('pstack/skills/poteto-mode/SKILL.md', 'skills/jstack/jstack-juan-mode/SKILL.md')]
    for source, local in pairs:
        a, b = upstream(source), (ROOT/local).read_bytes()
        records.append({'upstreamPath': source, 'localPath': local,
                        'upstreamSha256': hashlib.sha256(a).hexdigest(),
                        'localSha256': hashlib.sha256(b).hexdigest(),
                        'fullSourceDiff': diff(a, b, source, local)})
    mode = 'skills/jstack/jstack-juan-mode/SKILL.md'
    previous, current = baseline(mode), (ROOT/mode).read_bytes()
    expected = previous.replace(b'**no-comments** skill (`/no-comments`)', b'**jstack-no-comments** skill (`/jstack-no-comments`)').replace(
        b'jstack-benchmark-checklist and jstack-technical-writing separately.',
        b'jstack-benchmark-checklist, jstack-technical-writing and jstack-no-comments separately.').replace(
        b'No-comments is not yet packaged by jstack; Deslop', b'Deslop')
    assert current == expected
    for p in (ROOT/Path(mode).parent).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts and p.name != 'SKILL.md':
            assert p.read_bytes() == baseline(str(p.relative_to(ROOT)))
    assert (ROOT/package/'LICENSE').read_bytes() == upstream('pstack/LICENSE')
    print(json.dumps({'base': BASE, 'pin': PIN, 'completeSourceInventory': inventory,
                      'checkpointAndExistingPinsPreserved': True, 'modeSupportUnchanged': True,
                      'licenseMatchesPin': True, 'modeDiffFromBase': diff(previous, current, BASE+':'+mode, mode),
                      'files': records}, indent=2))


if __name__ == '__main__':
    main()
