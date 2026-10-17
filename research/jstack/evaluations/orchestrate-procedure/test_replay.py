"""Subprocess checks against the real orch CLI, using explicitly synthetic data."""
import argparse
import collections
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


SCRIPT = Path(__file__).with_name('replay.py')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cli', type=Path, required=True)
    parser.add_argument('--scratch', type=Path,
                        default=Path('/tmp/jstack-recovery-pilot-20261017/worker'))
    args = parser.parse_args()
    args.scratch.mkdir(parents=True, exist_ok=True)
    scratch = Path(tempfile.mkdtemp(prefix='replay-test-', dir=args.scratch))
    bun = shutil.which('bun')
    assert bun, 'Bun must already be installed'
    shim = scratch / 'bin'
    shim.mkdir()
    audit = scratch / 'cli-calls.jsonl'
    wrapper = shim / 'bun'
    wrapper.write_text(
        '#!' + sys.executable + '\n'
        'import json, os, sys\n'
        'with open(os.environ["REPLAY_AUDIT"], "a") as log:\n'
        '    log.write(json.dumps(sys.argv[1:]) + "\\n")\n'
        'os.execv(os.environ["REPLAY_REAL_BUN"], [os.environ["REPLAY_REAL_BUN"], *sys.argv[1:]])\n')
    wrapper.chmod(0o755)
    env = dict(os.environ, PATH=str(shim) + os.pathsep + os.environ['PATH'],
               REPLAY_AUDIT=str(audit), REPLAY_REAL_BUN=bun)

    def cli(root, *words):
        result = subprocess.run([bun, str(args.cli.resolve()), '--store', str(root / 'store'),
                                 '--json', *words], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def replay(root, observations, phase, *flags, code=0):
        result = subprocess.run([sys.executable, '-B', str(SCRIPT), str(root), str(observations),
                                 '--cli', str(args.cli.resolve()), '--phase', phase, *flags],
                                capture_output=True, text=True, env=env, timeout=60)
        with (scratch / 'processes.log').open('a') as log:
            log.write(f'{phase} {flags}: exit {result.returncode}\n{result.stdout}{result.stderr}')
        assert result.returncode == code, (result.returncode, result.stdout, result.stderr)
        return result

    def applications():
        calls = [json.loads(line)[4:] for line in audit.read_text().splitlines()]
        return [call[2] for call in calls if call[:2] == ['unit', 'set']]

    def snapshot(root):
        paths = [root / 'store' / 'units.tsv', root / 'receipt.json',
                 root / 'store' / 'inbox-batch.json']
        return [(path.read_bytes(), path.stat().st_ino, path.stat().st_mtime_ns) for path in paths]

    for interrupted in (True, False):
        case = scratch / ('interrupted' if interrupted else 'normal')
        case.mkdir()
        records = []
        for i in range(1, 4):
            report = case / f'synthetic-report-{i}.md'
            report.write_text(f'Synthetic report {i}. No live T3 execution.\n')
            records.append(dict(taskId=f'synthetic-task-{i}', childRunId=f'synthetic-run-{i}',
                                resultContextTransferId=f'synthetic-result-{i}', unit=f'unit-{i}',
                                reportPath=str(report), status='completed', workState='result_available',
                                hasPendingChildRuns=False, hasPendingQuestion=False,
                                evidenceOrigin='generated test fixture, not a live T3 status'))
        observations = case / 'observations.json'
        observations.write_text(json.dumps(records))
        root = case / 'replay'
        before_calls = len(applications()) if audit.exists() else 0
        replay(root, observations, 'claim')
        batch = cli(root, 'inbox', 'claim')
        assert len(batch['entries']) == 4 and batch['state'] == 'pending'
        assert [row['state'] for row in cli(root, 'unit', 'list')] == ['pending'] * 3
        assert json.loads((root / 'receipt.json').read_text()) == []
        if interrupted:
            replay(root, observations, 'resume', '--interrupt-after-first-apply', code=75)
            assert cli(root, 'inbox', 'claim') == batch
            assert cli(root, 'inbox', 'count') == {'count': 4}
            assert [(row['id'], row['state']) for row in cli(root, 'unit', 'list')] == [
                ('unit-1', 'assessed'), ('unit-2', 'pending'), ('unit-3', 'pending')]
            assert json.loads((root / 'receipt.json').read_text()) == []
            assert applications()[before_calls:] == ['unit-1']
            baseline = snapshot(root)
            audit_before = audit.read_bytes()
            for field in ('taskId', 'childRunId', 'resultContextTransferId', 'unit', 'reportPath'):
                changed = json.loads(observations.read_text())
                changed[-1][field] += '-changed'
                if field == 'reportPath':
                    Path(changed[-1][field]).write_text('Different synthetic report.\n')
                observations.write_text(json.dumps(changed))
                result = replay(root, observations, 'resume', code=1)
                assert 'observation or report changed' in result.stderr
                assert snapshot(root) == baseline and audit.read_bytes() == audit_before
                observations.write_text(json.dumps(records))
            report = Path(records[-1]['reportPath'])
            original = report.read_bytes()
            report.write_text('Changed synthetic content.\n')
            result = replay(root, observations, 'resume', code=1)
            assert 'observation or report changed' in result.stderr
            assert snapshot(root) == baseline and audit.read_bytes() == audit_before
            report.write_bytes(original)
        replay(root, observations, 'resume')
        rows = cli(root, 'unit', 'list')
        assert rows == [dict(id=f'unit-{i}', track='authoring', state='assessed',
                             branch='', pr='', sha='', brief='') for i in range(1, 4)]
        decisions = json.loads((root / 'receipt.json').read_text())
        assert [row['classification'] for row in decisions] == ['assessed'] * 3 + ['duplicate']
        assert [row['taskId'] for row in decisions] == [
            'synthetic-task-1', 'synthetic-task-2', 'synthetic-task-3', 'synthetic-task-3']
        assert [row['unit'] for row in decisions] == ['unit-1', 'unit-2', 'unit-3', 'unit-3']
        for decision, i in zip(decisions, (1, 2, 3, 3)):
            assert decision['childRunId'] == f'synthetic-run-{i}'
            assert decision['result'] == f'synthetic-result-{i}'
            assert decision['reportPath'] == str(case / f'synthetic-report-{i}.md')
            assert decision['reportSha256'] == hashlib.sha256(
                f'Synthetic report {i}. No live T3 execution.\n'.encode()).hexdigest()
        assert [row['filename'] for row in decisions] == [row['filename'] for row in batch['entries']]
        assert collections.Counter(applications()[before_calls:]) == {
            'unit-1': 1, 'unit-2': 1, 'unit-3': 1}
        acknowledged = json.loads((root / 'store' / 'inbox-batch.json').read_text())
        assert acknowledged['id'] == batch['id'] and acknowledged['state'] == 'acknowledged'
        assert cli(root, 'inbox', 'count') == {'count': 0}
        assert cli(root, 'inbox', 'drain', '--peek') == []
        baseline = snapshot(root)
        calls_before = applications()
        replay(root, observations, 'resume')
        assert snapshot(root) == baseline and applications() == calls_before
        assert cli(root, 'unit', 'list') == rows
        changed = json.loads(observations.read_text())
        changed[-1]['childRunId'] = 'different-synthetic-run'
        observations.write_text(json.dumps(changed))
        result = replay(root, observations, 'resume', code=1)
        assert 'observation or report changed' in result.stderr
        assert snapshot(root) == baseline and applications() == calls_before
        print(f'PASS {case.name}: three applications, four decisions, harmless acknowledged replay')
    print(f'PASS changed task/run/result/unit/report path/content rejected before CLI access. Evidence: {scratch}')


if __name__ == '__main__':
    main()
