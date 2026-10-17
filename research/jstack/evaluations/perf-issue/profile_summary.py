import collections,json,pathlib,sys
p=json.loads(pathlib.Path(sys.argv[1]).read_text())
nodes={n['id']:n for n in p['nodes']}
times=collections.Counter()
for sample,delta in zip(p['samples'],p['timeDeltas']):
    n=nodes[sample]['callFrame']
    times[(n['functionName'],n['url'],n['lineNumber']+1)]+=delta
print(json.dumps({'profile':sys.argv[1],'total_sample_us':sum(times.values()),'top_self':[{'function':k[0],'file':k[1],'line':k[2],'self_us':v,'share':v/sum(times.values())} for k,v in times.most_common(12)]},indent=2))
