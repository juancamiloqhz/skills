#!/usr/bin/env python3
"""Compare shipped principle instructions with their exact manifest source pins."""
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
    if not component['name'].startswith('principle-'):
        continue
    source_path = component['upstreamPath'] + '/SKILL.md'
    source = subprocess.check_output(['git', '--git-dir=' + str(args.cache), 'show', component['adaptedFrom'] + ':' + source_path])
    local_path = component['localPath'] + '/SKILL.md'
    local = (root / local_path).read_bytes()
    notice = subprocess.check_output(['git', '--git-dir=' + str(args.cache), 'show', component['adaptedFrom'] + ':pstack/LICENSE'])
    results.append({
        'name': component['name'], 'pin': component['adaptedFrom'],
        'upstreamPath': source_path, 'localPath': local_path,
        'upstreamSha256': hashlib.sha256(source).hexdigest(),
        'localSha256': hashlib.sha256(local).hexdigest(),
        'licenseMatchesPin': (root / component['localPath'] / 'LICENSE').read_bytes() == notice,
        'diff': ''.join(difflib.unified_diff(source.decode().splitlines(True), local.decode().splitlines(True), fromfile=source_path, tofile=local_path)),
    })
print(json.dumps({'scope': 'Source comparison only; differences require semantic review.', 'components': results}, indent=2))
if len(results) != 24 or not all(item['licenseMatchesPin'] for item in results):
    raise SystemExit(1)
