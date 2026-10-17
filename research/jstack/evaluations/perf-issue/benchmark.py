import datetime, hashlib, json, os, pathlib, statistics, subprocess, sys, time
root = pathlib.Path('/tmp/jstack-perf-issue-20261016')
destination = pathlib.Path(sys.argv[1])
destination.mkdir(parents=True, exist_ok=False)
expected = json.loads((root / 'expected.json').read_text())
rows = []
for pair in range(5):
    for side in ('baseline', 'app'):
        command = ['node', 'cli.cjs', '../events.json', '../rules.json']
        start = time.perf_counter()
        process = subprocess.run(command, cwd=root / side, capture_output=True, timeout=120)
        elapsed = time.perf_counter() - start
        row = {'pair': pair, 'side': side, 'command': command, 'cwd': str(root / side), 'seconds': elapsed, 'exit_code': process.returncode, 'stdout': process.stdout.decode(), 'stderr': process.stderr.decode(), 'recorded': datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            output = json.loads(process.stdout)
            row['correct'] = output == expected and output['processed'] == output['accepted'] + output['rejected'] == 80000
        except Exception as error:
            row['correct'] = False
            row['validation_error'] = str(error)
        (destination / f'{pair}-{side}.json').write_text(json.dumps(row, indent=2))
        rows.append(row)
        if process.returncode or process.stderr or not row['correct']:
            raise RuntimeError(f'Invalid measured work in {side}, pair {pair}')
summary = {'environment': {'node': subprocess.check_output(['node', '--version'], text=True).strip(), 'load': os.getloadavg(), 'cpu_count': os.cpu_count()}, 'runs_per_side': 5, 'clock': 'time.perf_counter, subprocess spawn through capture and wait', 'profiling': False, 'failures': 0, 'expected': expected, 'input_sha256': {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in ('events.json', 'rules.json')}}
for side in ('baseline', 'app'):
    times = [row['seconds'] for row in rows if row['side'] == side]
    summary[side] = {'median_seconds': statistics.median(times), 'min_seconds': min(times), 'max_seconds': max(times), 'runs': times}
summary['reduction_percent'] = 100 * (1 - summary['app']['median_seconds'] / summary['baseline']['median_seconds'])
summary['passes_30_percent'] = summary['reduction_percent'] >= 30
(destination / 'summary.json').write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
