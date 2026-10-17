import datetime, json, pathlib, subprocess, sys, time
root = pathlib.Path('/tmp/jstack-perf-issue-20261016/evidence/commands')
label, cwd, *cmd = sys.argv[1:]
record = {'command': cmd, 'cwd': cwd, 'started': datetime.datetime.now(datetime.timezone.utc).isoformat()}
start = time.perf_counter()
try:
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120)
    record.update(stdout=p.stdout, stderr=p.stderr, exit_code=p.returncode)
except subprocess.TimeoutExpired as e:
    record.update(stdout=str(e.stdout), stderr=str(e.stderr), exit_code=None, timeout=True)
record['seconds'] = time.perf_counter() - start
path = root / (label + '.json')
with path.open('x') as f:
    json.dump(record, f, indent=2)
print(json.dumps(record))
sys.exit(record['exit_code'] if record['exit_code'] is not None else 124)
