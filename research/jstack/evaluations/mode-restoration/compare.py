#!/usr/bin/env python3
"""Compare restored mode files and inventory procedures/tools still pending."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--cache',type=Path,default=Path.home()/'.cache/jstack/upstream/upstream.git')
a=parser.parse_args()
root=Path(__file__).resolve().parents[4]
manifest=json.loads((root/'research/jstack/upstream.json').read_text())
c=next(x for x in manifest['skills'] if x['name']=='juan-mode')
pin=c['adaptedFrom']
def git(*args): return subprocess.check_output(['git','--git-dir='+str(a.cache),*args])
def digest(b): return hashlib.sha256(b).hexdigest()
paths=git('ls-tree','-r','--name-only',pin,'--',c['upstreamPath']).decode().splitlines()
files=[]; pending=[]
for path in paths:
    source=git('show',pin+':'+path)
    relative=path[len(c['upstreamPath'])+1:]
    local=root/c['localPath']/relative
    if relative in ('SKILL.md','references/bugbot-triage.md'):
        target=local.read_bytes()
        files.append({'sourcePath':path,'localPath':str(local.relative_to(root)),'sourceSha256':digest(source),'localSha256':digest(target),'diff':''.join(difflib.unified_diff(source.decode().splitlines(True),target.decode().splitlines(True),fromfile=path,tofile=str(local.relative_to(root))))})
    else:
        assert not local.exists(),relative
        pending.append({'sourcePath':path,'sourceSha256':digest(source),'status':'pending procedure or supporting tooling; not restored in this correction'})
assert len(files)==2
assert (root/c['localPath']/'LICENSE').read_bytes()==git('show',pin+':pstack/LICENSE')
wrapper='pstack/agents/poteto-agent.md'
extras=[]
for p in sorted((root/c['localPath']).rglob('*')):
    if p.is_file() and str(p.relative_to(root)) not in [x['localPath'] for x in files] and p.name!='LICENSE':
        extras.append({'localPath':str(p.relative_to(root)),'sha256':digest(p.read_bytes())})
print(json.dumps({'pin':pin,'restoredFiles':files,'licenseMatchesPin':True,'wrapperContext':{'sourcePath':wrapper,'sha256':digest(git('show',pin+':'+wrapper)),'localImplementation':'SKILL.md Subagents plus references/execution.md; native/T3 full-read brief replaces Cursor subagent_type'},'jstackSupportFiles':extras,'removedSummary':'references/routes.md','pending':pending},indent=2))
