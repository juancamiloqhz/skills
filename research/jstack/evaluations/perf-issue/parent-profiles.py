from pathlib import Path
import json,sqlite3,hashlib
root=Path(__file__).resolve().parent;dest=root/'parent-evidence'
db=sqlite3.connect(':memory:')
db.executescript('CREATE TABLE frames(side TEXT,node INTEGER,function TEXT,url TEXT,line INTEGER,PRIMARY KEY(side,node)); CREATE TABLE samples(side TEXT,ordinal INTEGER,node INTEGER,us INTEGER);')
inputs={}
for side,file in [('baseline','baseline.cpuprofile'),('app','post.cpuprofile')]:
 p=root/'evidence'/file;j=json.loads(p.read_text());nodes={n['id']:n for n in j['nodes']}
 assert len(j['samples'])==len(j['timeDeltas']) and set(j['samples'])<=nodes.keys() and all(t>=0 for t in j['timeDeltas'])
 inputs[side]={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'samples':len(j['samples']),'nodes':len(nodes),'totalSampleUs':sum(j['timeDeltas'])}
 for n in nodes.values():
  f=n['callFrame'];db.execute('INSERT INTO frames VALUES(?,?,?,?,?)',(side,n['id'],f['functionName'],f['url'],f['lineNumber']+1))
 db.executemany('INSERT INTO samples VALUES(?,?,?,?)',[(side,i,n,t)for i,(n,t)in enumerate(zip(j['samples'],j['timeDeltas']))])
query='SELECT s.side,f.function,f.url,f.line,SUM(s.us) AS self_us FROM samples s JOIN frames f USING(side,node) GROUP BY s.side,f.function,f.url,f.line ORDER BY s.side,self_us DESC'
rows=[dict(zip(['side','function','url','line','selfUs'],row))for row in db.execute(query)]
result={'interpretation':'Separate profiled CLI runs support hotspot attribution only; sampled durations are not acceptance timings. SQL join preserves sample/frame identity and microsecond weights. Native parsing is charged to summarize; the separate parse probe supplies mechanism evidence.','inputs':inputs,'query':query,'allFrames':rows,'summarize':{side:sum(row['selfUs']for row in rows if row['side']==side and row['function']=='summarize')for side in inputs}}
(dest/'profiles.sql').write_text('\n'.join(db.iterdump())+'\n');(dest/'profiles.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['inputs','summarize']},indent=2))
