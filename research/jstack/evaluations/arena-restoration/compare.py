#!/usr/bin/env python3
"""Compare Arena's complete source and record its narrow Architect caller edit."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--cache', type=Path, default=Path.home()/'.cache/jstack/upstream/upstream.git')
args = parser.parse_args()
root = Path(__file__).resolve().parents[4]
manifest = json.loads((root/'research/jstack/upstream.json').read_text())
component = next(item for item in manifest['skills'] if item['name'] == 'arena')
pin = component['adaptedFrom']


def upstream(*argv):
    return subprocess.check_output(['git', '--git-dir='+str(args.cache), *argv])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def diff(before, after, source, target):
    return ''.join(difflib.unified_diff(before.decode().splitlines(True),
                                      after.decode().splitlines(True),
                                      fromfile=source, tofile=target))


paths = upstream('ls-tree', '-r', '--name-only', pin, '--', component['upstreamPath']).decode().splitlines()
assert paths == [component['upstreamPath']+'/SKILL.md']
source = upstream('show', pin+':'+paths[0])
local = root/component['localPath']/'SKILL.md'
target = local.read_bytes()
assert (local.parent/'LICENSE').read_bytes() == upstream('show', pin+':pstack/LICENSE')
architect_path = 'skills/jstack/architect/SKILL.md'
base = 'efd2afebcd4335e6ef54292316dc1817e2332f65'
architect_before = subprocess.check_output(['git', '-C', str(root), 'show', base+':'+architect_path])
architect_after = (root/architect_path).read_bytes()
expected = architect_before.replace(
    b'At least two viable configured candidates are required by the current Arena contract.',
    b"This Architect caller requires at least two viable configured candidates; Arena's ordinary one-survivor fallback does not satisfy that requirement.")
assert architect_after == expected
print(json.dumps({
    'pin': pin, 'sourcePath': paths[0], 'localPath': str(local.relative_to(root)),
    'sourceSha256': digest(source), 'localSha256': digest(target),
    'diff': diff(source, target, paths[0], str(local.relative_to(root))),
    'licenseMatchesPin': True,
    'jstackSupportFiles': [
        {'localPath': str(path.relative_to(root)), 'sha256': digest(path.read_bytes())}
        for path in sorted(local.parent.rglob('*'))
        if path.is_file() and path.name not in ('SKILL.md', 'LICENSE')
    ],
    'architectCaller': {
        'base': base, 'path': architect_path,
        'localSha256': digest(architect_after),
        'sourcePath': 'pstack/skills/architect/SKILL.md', 'sourcePin': pin,
        'sourceSha256': digest(upstream('show', pin+':pstack/skills/architect/SKILL.md')),
        'onlyCallerSentenceChanged': True,
        'diffFromMergedBase': diff(architect_before, architect_after, base+':'+architect_path, architect_path),
        'fullPriorComparison': '../design-review-restoration/source-comparison.json',
    },
}, indent=2))
