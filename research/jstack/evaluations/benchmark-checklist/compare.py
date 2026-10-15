#!/usr/bin/env python3
"""Compare the complete benchmark skill and its updated mode caller."""
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
base = '8ad4c48e1351ee2a3c6f857d56f530476e02569d'


def source(pin, path):
    return subprocess.check_output(['git', '--git-dir='+str(args.cache), 'show', pin+':'+path])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def diff(before, after, old, new):
    return ''.join(difflib.unified_diff(before.decode().splitlines(True),
                                      after.decode().splitlines(True), fromfile=old, tofile=new))


records = []
for name in ('benchmark-checklist', 'juan-mode'):
    item = next(x for x in manifest['skills'] if x['name'] == name)
    upstream_path = item['upstreamPath']+'/SKILL.md'
    local_path = item['localPath']+'/SKILL.md'
    before = source(item['adaptedFrom'], upstream_path)
    after = (root/local_path).read_bytes()
    assert (root/item['localPath']/'LICENSE').read_bytes() == source(item['adaptedFrom'], 'pstack/LICENSE')
    record = {'name': name, 'pin': item['adaptedFrom'], 'sourcePath': upstream_path,
              'localPath': local_path, 'sourceSha256': digest(before), 'localSha256': digest(after),
              'licenseMatchesPin': True, 'fullSourceDiff': diff(before, after, upstream_path, local_path)}
    if name == 'benchmark-checklist':
        paths = subprocess.check_output(['git', '--git-dir='+str(args.cache), 'ls-tree', '-r',
                                         '--name-only', item['adaptedFrom'], '--', item['upstreamPath']], text=True).splitlines()
        assert paths == [upstream_path]
        assert sorted(p.name for p in (root/item['localPath']).iterdir()) == ['LICENSE', 'SKILL.md']
        record['completeSourceInventory'] = paths
    else:
        old = subprocess.check_output(['git', '-C', str(root), 'show', base+':'+local_path])
        expected = old.replace(b'figure-it-out and show-me-your-work separately.',
                               b'figure-it-out, show-me-your-work and benchmark-checklist separately.').replace(
                                   b'Technical-writing, no-comments and benchmark-checklist are not yet packaged',
                                   b'Technical-writing and no-comments are not yet packaged')
        assert after == expected
        record['diffFromMergedBase'] = diff(old, after, base+':'+local_path, local_path)
        record['priorComparison'] = '../mode-restoration/source-comparison.json'
    records.append(record)
print(json.dumps({'base': base, 'files': records}, indent=2))
