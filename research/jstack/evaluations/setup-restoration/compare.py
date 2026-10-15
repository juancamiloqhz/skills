#!/usr/bin/env python3
"""Compare setup with its exact pin and inventory runtime support files."""
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
component = next(item for item in manifest['skills'] if item['name'] == 'setup-jstack')
pin = component['adaptedFrom']


def git(*argv):
    return subprocess.check_output(['git', '--git-dir='+str(args.cache), *argv])


def digest(data):
    return hashlib.sha256(data).hexdigest()


paths = git('ls-tree', '-r', '--name-only', pin, '--', component['upstreamPath']).decode().splitlines()
assert paths == [component['upstreamPath']+'/SKILL.md'], paths
source = git('show', pin+':'+paths[0])
local = root/component['localPath']/'SKILL.md'
target = local.read_bytes()
assert (local.parent/'LICENSE').read_bytes() == git('show', pin+':pstack/LICENSE')
support = [
    {'localPath': str(path.relative_to(root)), 'sha256': digest(path.read_bytes())}
    for path in sorted(local.parent.rglob('*'))
    if path.is_file() and path.name not in ('SKILL.md', 'LICENSE')
]
example = json.loads(target.decode().split('```json\n', 1)[1].split('```', 1)[0])
template = json.loads(subprocess.check_output([
    'python3', '-B', str(local.parent/'scripts/models.py'), 'template', '--preset', 'medium']))
assert example == template
print(json.dumps({
    'pin': pin,
    'sourcePath': paths[0],
    'localPath': str(local.relative_to(root)),
    'sourceSha256': digest(source),
    'localSha256': digest(target),
    'diff': ''.join(difflib.unified_diff(
        source.decode().splitlines(True), target.decode().splitlines(True),
        fromfile=paths[0], tofile=str(local.relative_to(root)))),
    'licenseMatchesPin': True,
    'inlineExampleMatchesTemplate': True,
    'jstackSupportFiles': support,
    'additionalInvestigationSource': {
        'pin': '11713c683fe4add4fd403ea880580abbc9e0875f',
        'sourcePath': 'pstack/skills/why',
        'localPath': 'skills/jstack/setup-jstack/references/investigation.md',
        'status': 'unchanged shared consumer contract; separately attributed in adaptation record',
    },
}, indent=2))
