import argparse, hashlib, json, os, pathlib, statistics, subprocess, sys, time

root = pathlib.Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument('--a', required=True)
p.add_argument('--b', required=True)
p.add_argument('--events-a', default=str(root / 'events.json'))
p.add_argument('--events-b', default=str(root / 'events.json'))
p.add_argument('--expected-a', default=str(root / 'expected.json'))
p.add_argument('--expected-b', default=str(root / 'expected.json'))
p.add_argument('--out', required=True)
args = p.parse_args()
rules = str(root / 'rules.json')
result = {'harness_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(), 'samples': [], 'errors': 0, 'work': 0, 'count': 7, 'unit': 'ms'}
for i in range(7):
    for side in ('a', 'b'):
        root = pathlib.Path(getattr(args, side)).resolve()
        events = pathlib.Path(getattr(args, 'events_' + side))
        expected = json.loads(pathlib.Path(getattr(args, 'expected_' + side)).read_text())
        command = ['node', str(root / 'cli.cjs'), str(events), rules]
        before = time.perf_counter_ns()
        try:
            run = subprocess.run(command, capture_output=True, timeout=30, env={**os.environ, 'NODE_OPTIONS': '', 'LC_ALL': 'C'})
            elapsed = (time.perf_counter_ns() - before) / 1e6
            try:
                output = json.loads(run.stdout)
            except (ValueError, UnicodeError):
                output = None
            correct = run.returncode == 0 and not run.stderr and output == expected
            sample = {'side': side, 'index': i, 'ms': elapsed, 'command': command, 'exit': run.returncode, 'stdout_bytes': len(run.stdout), 'stdout_sha256': hashlib.sha256(run.stdout).hexdigest(), 'output': output, 'stderr': run.stderr.decode(errors='replace'), 'correct': correct, 'work': output.get('processed', 0) if isinstance(output, dict) else 0}
        except subprocess.TimeoutExpired as error:
            sample = {'side': side, 'index': i, 'ms': (time.perf_counter_ns() - before) / 1e6, 'command': command, 'exit': 'timeout', 'correct': False, 'work': 0, 'stderr': str(error)}
        sample['source_hashes'] = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in ('cli.cjs', 'summary.cjs')}
        sample['input_hashes'] = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in (events, pathlib.Path(rules))}
        result['samples'].append(sample)
        result['errors'] += int(not sample['correct'])
        result['work'] += sample['work']
for side in ('a', 'b'):
    values = [s['ms'] for s in result['samples'] if s['side'] == side]
    result[side] = {'raw_ms': values, 'median_ms': statistics.median(values), 'range_ms': [min(values), max(values)]}
result['reduction_percent'] = 100 * (1 - result['b']['median_ms'] / result['a']['median_ms'])
result['past_noise'] = result['b']['range_ms'][1] < result['a']['range_ms'][0]
pathlib.Path(args.out).write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'samples'}))
sys.exit(bool(result['errors']))
