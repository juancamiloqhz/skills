#!/usr/bin/env python3
import json, shutil, subprocess, sys, tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[4]
feature=sys.argv[1]; evidence=Path(sys.argv[2]).resolve()
if evidence.exists(): raise SystemExit('refuse to overwrite evidence')
evidence.parent.mkdir(parents=True,exist_ok=True)
report={'feature':feature,'calls':[]}; data=None; status=0

def call(args, expected=0):
    p=subprocess.run([sys.executable,str(root/'ledger.py'),*args],capture_output=True,text=True)
    report['calls'].append({'args':args,'stdout':p.stdout,'stderr':p.stderr,'returncode':p.returncode})
    assert p.returncode==expected, f'exit {p.returncode}, expected {expected}'
    return p.stdout
try:
    if feature=='doctor':
        assert call(['--version']).strip()=='ledger 2', 'wrong app identity'
    else:
        data=Path(tempfile.mkdtemp(prefix='ledger-verify-'))
        report['data']=str(data)
        if feature in ('create','read'):
            got=json.loads(call(['--data',str(data),'create','--body','Case Sensitive']))
            assert got=={'body':'Case Sensitive'}, got
            assert json.loads((data/'note.json').read_text())==got
            if feature=='read':
                got=json.loads(call(['--data',str(data),'get']))
                assert got=={'body':'Case Sensitive'}, got
        elif feature=='export':
            target=data/'absent'
            got=json.loads(call(['--data',str(target),'export'], expected=3))
            assert got=={'error':'export entitlement unavailable'}, got
            assert report['calls'][-1]['stderr']=='', report['calls'][-1]['stderr']
            assert not target.exists(), 'export created data without entitlement'
            report['outcome']='verified-unreachable'
            report['prerequisite']='licensed-export entitlement unavailable; cannot obtain it in this fixture'
            report['data_created']=False
        else: raise ValueError(feature)
    report.setdefault('outcome','passed')
except Exception as exc:
    report['outcome']='failed'; report['error']=str(exc); status=1
finally:
    if data is not None: shutil.rmtree(data)
    report['cleanup']=data is None or not data.exists()
    evidence.write_text(json.dumps(report,indent=2)+'\n')
raise SystemExit(status)
