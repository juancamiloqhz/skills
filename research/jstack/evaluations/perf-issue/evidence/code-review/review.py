import collections
import difflib
import hashlib
import json
from pathlib import Path
import statistics
import subprocess

root = Path('/tmp/jstack-perf-issue-20261016')
out = root / 'evidence/code-review'
records = []

def run(command, label):
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    record = dict(command=command, cwd=str(root), stdout=result.stdout,
                  stderr=result.stderr, exit_code=result.returncode)
    (out / (label + '.json')).write_text(json.dumps(record, indent=2) + '\n')
    records.append(dict(label=label, command=command, exit_code=result.returncode))
    assert result.returncode == 0, record
    return result.stdout

identity = dict(task='/root/perf_issue_forward/code_review',
                selection='inherited codex gpt-6-astra',
                evidence='../commands/preflight-code-review.json and parent brief',
                limitation='Configuration evidence is not independent runtime model attestation. Same-family independent context is not model diversity.',
                overrides=False, descendants=False)
(out / 'identity.json').write_text(json.dumps(identity, indent=2) + '\n')

reads = ['benchmark.py', 'verify.cjs', 'parse_probe.cjs', 'generate.py',
         'app/summary.cjs', 'app/summary.test.cjs', 'app/cli.cjs',
         'baseline/summary.cjs', 'baseline/summary.test.cjs', 'baseline/cli.cjs',
         'evidence/final.diff', 'evidence/implementation/report.md',
         'evidence/comments/report.md', 'evidence/commands/parent-tests.json',
         'evidence/commands/parent-compatibility.json',
         'evidence/commands/environment.json',
         'evidence/commands/baseline-parsed.json', 'evidence/commands/post-parsed.json',
         'evidence/commands/baseline-parse-probe.json', 'evidence/commands/post-parse-probe.json']
run(['cat', *reads], 'read-replay')
run(['node', '--test', 'app/summary.test.cjs'], 'tests')
run(['node', 'verify.cjs', 'evidence/code-review/compatibility'], 'compatibility')

expected = json.loads((root / 'expected.json').read_text())
events = json.loads((root / 'events.json').read_text())
rules = json.loads((root / 'rules.json').read_text())
totals = collections.defaultdict(int)
accepted = 0
for event in events:
    rule = rules.get(event['type'])
    if rule and event['amount'] >= rule['minimum']:
        accepted += 1
        totals[event['type']] += event['amount'] * rule['multiplier']
assert expected == dict(processed=len(events), accepted=accepted,
                        rejected=len(events)-accepted, totals=dict(totals))
summary = json.loads((root / 'evidence/benchmark/summary.json').read_text())
rows = []
for pair in range(5):
    for side in ['baseline', 'app']:
        row = json.loads((root / f'evidence/benchmark/{pair}-{side}.json').read_text())
        assert row['side'] == side and row['pair'] == pair
        assert row['command'] == ['node', 'cli.cjs', '../events.json', '../rules.json']
        assert row['cwd'] == str(root / side)
        assert row['exit_code'] == 0 and row['stderr'] == '' and row['correct']
        assert json.loads(row['stdout']) == expected
        assert row['stdout'].endswith('\n') and row['stdout'].count('\n') == 1
        rows.append(row)
assert [r['recorded'] for r in rows] == sorted(r['recorded'] for r in rows)
for side in ['baseline', 'app']:
    times = [r['seconds'] for r in rows if r['side'] == side]
    assert summary[side] == dict(median_seconds=statistics.median(times),
                                 min_seconds=min(times), max_seconds=max(times), runs=times)
reduction = 100 * (1-summary['app']['median_seconds']/summary['baseline']['median_seconds'])
assert reduction == summary['reduction_percent'] and reduction >= 30
for name, digest in summary['input_sha256'].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest
assert (root / 'app/cli.cjs').read_bytes() == (root / 'baseline/cli.cjs').read_bytes()
actual_diff = ''.join(''.join(difflib.unified_diff(
    (root / 'baseline' / name).read_text().splitlines(True),
    (root / 'app' / name).read_text().splitlines(True),
    fromfile='baseline/'+name, tofile='app/'+name))
    for name in ['summary.cjs', 'summary.test.cjs'])
assert actual_diff == (root / 'evidence/final.diff').read_text()
for name in ['summary.cjs', 'summary.test.cjs']:
    assert (root / 'app' / name).read_bytes() == (root / 'evidence/review-snapshot' / name).read_bytes()

profile_results = {}
for side in ['baseline', 'post']:
    profile = json.loads((root / f'evidence/{side}.cpuprofile').read_text())
    assert len(profile['samples']) == len(profile['timeDeltas'])
    frames = {node['id']: node['callFrame'] for node in profile['nodes']}
    times = collections.Counter()
    for sample, delta in zip(profile['samples'], profile['timeDeltas']):
        frame = frames[sample]
        times[(frame['functionName'], frame['url'])] += delta
    profile_results[side] = dict(total_us=sum(times.values()),
        top=[dict(function=key[0], url=key[1], us=value) for key, value in times.most_common(6)])
    parsed = json.loads(json.loads((root / f'evidence/commands/{side}-parsed.json').read_text())['stdout'])
    assert parsed['total_sample_us'] == sum(times.values())
    assert parsed['top_self'][0]['self_us'] == times.most_common(1)[0][1]

result = dict(status='pass', raw_runs_checked=len(rows), failures=0,
              expected_recomputed=True, source_diff_matches=True,
              snapshot_matches=True, cli_unchanged=True,
              baseline=summary['baseline'], app=summary['app'],
              reduction_percent=reduction, profiles=profile_results)
(out / 'evidence-check.json').write_text(json.dumps(result, indent=2) + '\n')
(out / 'commands.json').write_text(json.dumps(dict(
    note='Initial read-only bootstrap commands remain in the tool transcript. read-replay repeats the source and evidence reads; it is not a claim to capture the original executions.',
    commands=records), indent=2) + '\n')
print(json.dumps(result, indent=2))
