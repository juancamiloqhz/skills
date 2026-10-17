from pathlib import Path
import subprocess, json, hashlib, time, statistics, random, shutil
root=Path(__file__).resolve().parent
out=root/'parent-evidence';out.mkdir(exist_ok=True)
expected=json.loads((root/'expected.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def call(args):
 start=time.perf_counter_ns();r=subprocess.run(args,text=True,capture_output=True,cwd=root)
 return {'argv':list(map(str,args)),'elapsedMs':(time.perf_counter_ns()-start)/1e6,'exitCode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
meta={'claim':'At least 30% lower median end-to-end wall time for this synthetic 80,000-event CLI workload, with unchanged output. No production or model performance inference.','timedRegion':'Fresh Node startup, reading both files, JSON parsing, summarization and consumed stdout through process termination. No profiler in timed runs. Same Node, input, flags and host on both sides.','loadBefore':call(['uptime']),'cores':call(['nproc']),'processesBefore':call(['ps','-eo','pid,comm,pcpu,pmem','--sort=-pcpu']),'node':call(['node','--version']),'hashes':{str(p.relative_to(root)):sha(p) for p in [root/'events.json',root/'rules.json',root/'expected.json',root/'baseline/summary.cjs',root/'app/summary.cjs',root/'app/cli.cjs']}}
rows=[]
for pair in range(7):
 for side in ['baseline','app']:
  row=call(['node',str(root/side/'cli.cjs'),str(root/'events.json'),str(root/'rules.json')]);row.update(pair=pair,side=side)
  row['correct']=row['exitCode']==0 and not row['stderr'] and json.loads(row['stdout'])==expected
  rows.append(row)
meta['loadAfter']=call(['uptime'])
meta['runs']=rows
meta['summaries']={side:{'runs':len(xs:=[row['elapsedMs'] for row in rows if row['side']==side]),'medianMs':statistics.median(xs),'minMs':min(xs),'maxMs':max(xs)}for side in ['baseline','app']}
a=meta['summaries']['baseline'];b=meta['summaries']['app'];meta['reductionPercent']=100*(1-b['medianMs']/a['medianMs']);meta['nonoverlap']=b['maxMs']<a['minMs'];meta['allCorrect']=all(row['correct']for row in rows)
negative=root/'negative';negative.mkdir(exist_ok=True)
(negative/'cli.cjs').write_text("process.stdout.write(JSON.stringify({processed:80000,accepted:0,rejected:80000,totals:{}})+'\\n');\n")
n=call(['node',str(negative/'cli.cjs'),str(root/'events.json'),str(root/'rules.json')]);n['acceptedByCorrectnessGate']=n['exitCode']==0 and json.loads(n['stdout'])==expected;meta['negativeControl']=n
rng=random.Random(20261016);cases=[]
for i in range(120):
 rules={f'kind-{j}':{'minimum':rng.randrange(-4,20),'multiplier':rng.randrange(-3,5)}for j in range(8)}
 events=[{'type':f'kind-{rng.randrange(10)}','amount':rng.randrange(-5,200)}for _ in range(rng.randrange(200))]
 cases.append([events,json.dumps(rules)])
cases.extend([[[],'bad'],[[{'type':'x','amount':1}],'bad'],[[],'null'],[[{'type':'x','amount':1}],'null'],[[],'{}']])
(root/'parent-cases.json').write_text(json.dumps(cases))
probe=root/'api-check.cjs';probe.write_text("const fs=require('node:fs');const f=require(process.argv[2]).summarize;const cases=JSON.parse(fs.readFileSync(process.argv[3],'utf8'));console.log(JSON.stringify(cases.map(c=>{try{return{ok:true,value:f(...c)}}catch(e){return{ok:false,name:e.name,message:e.message}}})));\n")
api={side:call(['node',str(probe),str(root/side/'summary.cjs'),str(root/'parent-cases.json')])for side in ['baseline','app']}
meta['apiCases']=len(cases);meta['api']=api;meta['apiEqual']=all(v['exitCode']==0 for v in api.values())and api['baseline']['stdout']==api['app']['stdout']
meta['originalTests']=call(['node','--test',str(root/'app/summary.test.cjs')])
meta['callerUnchanged']=(root/'baseline/cli.cjs').read_bytes()==(root/'app/cli.cjs').read_bytes()
(out/'verification.json').write_text(json.dumps(meta,indent=2)+'\n')
assert meta['allCorrect']and meta['apiEqual']and meta['originalTests']['exitCode']==0 and meta['callerUnchanged'] and not n['acceptedByCorrectnessGate']
assert meta['reductionPercent']>=30 and meta['nonoverlap']
print(json.dumps({k:meta[k]for k in ['summaries','reductionPercent','nonoverlap','allCorrect','apiCases','apiEqual','callerUnchanged']},indent=2))
