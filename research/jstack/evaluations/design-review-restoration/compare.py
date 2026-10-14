#!/usr/bin/env python3
"""Emit exact pinned-source diffs for Architect, Interrogate and Reflect, including all references."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--cache', type=Path, default=Path.home() / '.cache/jstack/upstream/upstream.git')
args = parser.parse_args()
root = Path(__file__).resolve().parents[4]
manifest = json.loads((root / 'research/jstack/upstream.json').read_text())
results = []
for component in manifest['skills']:
    if component['name'] not in ('architect', 'interrogate', 'reflect'):
        continue
    pin = component['adaptedFrom']
    def git(*argv):
        return subprocess.check_output(['git', '--git-dir=' + str(args.cache), *argv])
    files = git('ls-tree', '-r', '--name-only', pin, '--', component['upstreamPath']).decode().splitlines()
    for path in files:
        source = git('show', pin + ':' + path)
        local_path = component['localPath'] + path[len(component['upstreamPath']):]
        local = (root / local_path).read_bytes()
        results.append({'pin': pin, 'upstreamPath': path, 'localPath': local_path,
                        'sourceSha256': hashlib.sha256(source).hexdigest(),
                        'localSha256': hashlib.sha256(local).hexdigest(),
                        'diff': ''.join(difflib.unified_diff(source.decode().splitlines(True), local.decode().splitlines(True), fromfile=path, tofile=local_path))})
    assert (root / component['localPath'] / 'LICENSE').read_bytes() == git('show', pin + ':pstack/LICENSE')
assert len(results) == 14
extras = []
for name in ('interrogate', 'reflect'):
    path = f'skills/jstack/{name}/references/execution.md'
    extras.append({'localPath': path, 'localSha256': hashlib.sha256((root / path).read_bytes()).hexdigest(),
                   'purpose': 'Existing jstack configuration and T3 execution contract; unchanged in this restoration.'})
print(json.dumps({'scope': 'All 14 mapped source files; semantic differences require review.', 'licenseMatchesPin': True, 'files': results, 'jstackOnlyReferences': extras, 'removedJstackSummaries': ['skills/jstack/interrogate/references/review-criteria.md', 'skills/jstack/reflect/references/assessment.md']}, indent=2))
