#!/usr/bin/env python3
"""Compare Swarm's complete source and the shared resolver additions."""
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
component = next(item for item in manifest['skills'] if item['name'] == 'swarm')
setup = next(item for item in manifest['skills'] if item['name'] == 'setup-jstack')
pin = component['adaptedFrom']
base = '36e489aa73c35c8e0bf84f1e0bc9a7f1298a57b5'


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
companion = []
for relative in ('scripts/models.py', 'scripts/test_models.py', 'references/configuration.md'):
    path = setup['localPath']+'/'+relative
    before = subprocess.check_output(['git', '-C', str(root), 'show', base+':'+path])
    after = (root/path).read_bytes()
    companion.append({'path': path, 'localSha256': digest(after),
                      'diffFromMergedBase': diff(before, after, base+':'+path, path)})
setup_source = setup['upstreamPath']+'/SKILL.md'
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
    'sharedResolver': {
        'base': base, 'changes': companion,
        'primarySetupPin': setup['adaptedFrom'], 'sourcePath': setup_source,
        'sourceSha256': digest(upstream('show', setup['adaptedFrom']+':'+setup_source)),
        'sourceRule': 'Step 3(c): swarm workers is default unless race/comparison assigns per-arm models.',
        'localSupport': 'Resolver and contract have no direct upstream file equivalents.',
    },
}, indent=2))
