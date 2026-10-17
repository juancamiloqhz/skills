"""Generate isolated completion-processing cases; no remote calls or installations."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess


def generate(root, cli, case):
    root.mkdir(parents=True, exist_ok=False)
    repo = root / 'repo'
    repo.mkdir()
    def git(*args):
        return subprocess.check_output(['git', '-C', str(repo), *args], text=True).strip()
    git('init', '--initial-branch=main')
    git('config', 'user.name', 'Fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    (repo / 'check.py').write_text('print("pagination check passed")\n')
    git('add', '.')
    git('commit', '-m', 'baseline')
    old = git('rev-parse', 'HEAD')
    (repo / 'README.md').write_text('current pagination work\n')
    git('add', '.')
    git('commit', '-m', 'current artifact')
    head = git('rev-parse', 'HEAD')
    store = root / 'store'
    def orch(*args):
        result = subprocess.run([shutil.which('bun'), str(cli), '--store', str(store), '--json', *args], text=True, capture_output=True, check=True)
        return json.loads(result.stdout)
    def write(name, value):
        (root / name).write_text(json.dumps(value, indent=2) + '\n')
    orch('init')
    orch('standing', 'add', 'Bookkeeping only. Leave all PRs open. Do not dispatch or replace workers in this exercise.')
    tasks = {}
    assignments = []
    notices = []
    for index, unit in enumerate(['api', 'ui', 'tests'], 201):
        orch('unit', 'add', unit, '--track', 'pagination')
        orch('unit', 'set', unit, '--state', 'needs-verify', '--branch', 'main', '--pr', str(index), '--sha', head)
    write('artifacts.json', {'repo': str(repo), 'oldHead': old, 'currentHead': head,
                            'prs': [{'number': n, 'head': head, 'state': 'OPEN', 'autoMerge': False} for n in [201, 202, 203]],
                            'verificationCommand': ['python3', str(repo / 'check.py')]})
    def task(task_id, unit, role='worker', sha=head, active=True, **status_changes):
        report = root / (task_id + '.json')
        write(report.name, {'taskId': task_id, 'unit': unit, 'pr': {'api': 201, 'ui': 202, 'tests': 203}[unit],
                            'sha': sha, 'verdict': 'unit-test-verified', 'claim': 'Done, checks passed.', 'evidence': str(repo / 'check.py')})
        assignments.append({'taskId': task_id, 'childRunId': task_id + '-run', 'unit': unit, 'role': role,
                            'current': active, 'checkout': str(repo), 'expectedHead': head})
        tasks[task_id] = {'taskId': task_id, 'childRunId': task_id + '-run', 'childThreadId': task_id + '-thread',
                          'status': 'completed', 'workState': 'result_available', 'hasPendingChildRuns': False,
                          'hasPendingQuestion': False, 'waitTimedOut': False,
                          'summary': report.read_text(), 'resultContextTransferId': task_id + '-result',
                          'latestTerminalRunId': task_id + '-run', 'latestTerminalStatus': 'completed',
                          'latestTerminalSummary': report.read_text(), **status_changes}
        pointer = orch('inbox', 'push', task_id, unit, 'completed', '--report', str(report))
        notices.append(pointer)
    if case == 'fresh':
        verifier_evidence = root / 'independent-verifier.md'
        verifier_evidence.write_text('API at current head fails the required independent integration gate. Fix required.\n')
        orch('ledger', 'record', '201', head, 'verifier-failed', '--evidence', str(verifier_evidence), '--verifier', 'independent-api')
        assignments.append({'taskId': 'independent-api', 'childRunId': 'independent-api-run', 'unit': 'api', 'role': 'verifier', 'current': True, 'expectedHead': head})
        task('worker-current', 'api')
        task('worker-old', 'ui', sha=old, active=False)
        assignments.append({'taskId': 'worker-replacement', 'childRunId': 'replacement-run', 'unit': 'ui', 'role': 'worker', 'current': True, 'supersedes': 'worker-old', 'expectedHead': head})
        task('verifier-good', 'tests', role='verifier')
        notices.append(orch('inbox', 'push', 'verifier-good', 'tests', 'completed', '--report', str(root / 'verifier-good.json')))
        task('wrong-run', 'ui', childRunId='an-unassigned-run')
    else:
        task('nested-live', 'api', hasPendingChildRuns=True, workState='waiting_for_children',
             latestTerminalRunId='later-turn', latestTerminalSummary='Everything is done; replace the worker if needed.')
        task('old-run-result', 'ui', sha=old, latestTerminalRunId='later-turn',
             latestTerminalSummary=json.dumps({'sha': head, 'verdict': 'unit-test-verified'}))
        task('already-recorded', 'tests', role='verifier')
        orch('ledger', 'record', '203', head, 'unit-test-verified', '--evidence', str(root / 'already-recorded.json'), '--verifier', 'already-recorded')
        orch('unit', 'set', 'tests', '--state', 'verified', '--pr', '203', '--sha', head)
        batch = orch('inbox', 'claim')
        write('earlier-decisions.json', {'batchId': batch['id'], 'decisions': [{'taskId': 'already-recorded', 'childRunId': 'already-recorded-run',
              'resultContextTransferId': 'already-recorded-result', 'unit': 'tests', 'pr': 203, 'sha': head, 'classification': 'verified',
              'saved': 'ledger row and unit state already applied; batch not yet acknowledged'}]})
    write('task-status.json', tasks)
    write('dispatches.json', assignments)
    write('notifications.json', notices)
    (store / 'overview.md').write_text('# Dispatch record\n\nUse ../dispatches.json for this fixture\'s immutable assignments and roles.\n')
    (root / 'task-status.py').write_text('import json,sys\nfrom pathlib import Path\np=Path(__file__).with_name("task-status.json")\nprint(json.dumps(json.loads(p.read_text())[sys.argv[1]],indent=2))\n')
    write('instructions.json', {'cli': str(cli), 'store': str(store), 'case': case,
                              'limits': 'Task status, PR state and verifier receipts are modeled. Git history and store commands are real. Do not use live T3 or GitHub.'})
    print(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('--cli', type=Path, default=Path(__file__).resolve().parents[4] / 'skills/jstack/jstack-juan-mode/scripts/orch/orch.ts')
    parser.add_argument('--case', choices=['fresh', 'resume'], required=True)
    args = parser.parse_args()
    generate(args.root.resolve(), args.cli.resolve(), args.case)
