"""Exercise saved live completion identities across fresh CLI processes.

Input is a list of parent-observed task_status records enriched with unit and
reportPath. This does not authenticate input or query the provider itself.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('observations', type=Path)
    parser.add_argument('--cli', type=Path, required=True)
    parser.add_argument('--phase', choices=['claim', 'resume'], required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    observations = json.loads(args.observations.read_text())
    assert len(observations) == 3
    by_task = {row['taskId']: row for row in observations}
    assert len(by_task) == 3
    for row in observations:
        assert row['status'] == 'completed' and row['workState'] == 'result_available'
        assert not row['hasPendingChildRuns'] and not row['hasPendingQuestion']
        assert row['childRunId'] and row['resultContextTransferId']
        assert Path(row['reportPath']).read_text().strip()

    def orch(*words):
        result = subprocess.run(['bun', str(args.cli.resolve()), '--store', str(root / 'store'),
                                 '--json', *words], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    if args.phase == 'claim':
        root.mkdir(parents=True, exist_ok=False)
        orch('init')
        orch('standing', 'add', 'Evaluation bookkeeping only. No PR verdicts, dispatch, merge or schedule.')
        for row in observations:
            orch('unit', 'add', row['unit'], '--track', 'authoring')
            orch('inbox', 'push', row['taskId'], row['unit'], 'completed', '--report', row['reportPath'])
        row = observations[-1]
        orch('inbox', 'push', row['taskId'], row['unit'], 'completed', '--report', row['reportPath'])
        batch = orch('inbox', 'claim')
        assert len(batch['entries']) == 4
        (root / 'claimed.json').write_text(json.dumps(batch, indent=2) + '\n')
        print('Four pointers claimed; no decisions applied; process exiting before acknowledgement.')
        return

    batch = orch('inbox', 'claim')
    assert batch == json.loads((root / 'claimed.json').read_text())
    decisions = []
    seen = set()
    for entry in batch['entries']:
        row = by_task[entry['pointer']['agent']]
        identity = (row['taskId'], row['childRunId'], row['resultContextTransferId'])
        duplicate = identity in seen
        if not duplicate:
            orch('unit', 'set', row['unit'], '--state', 'assessed')
        seen.add(identity)
        decisions.append({'filename': entry['filename'], 'taskId': row['taskId'],
                          'childRunId': row['childRunId'], 'result': row['resultContextTransferId'],
                          'classification': 'duplicate' if duplicate else 'assessed',
                          'reportSha256': hashlib.sha256(Path(row['reportPath']).read_bytes()).hexdigest()})
    assert len(seen) == 3 and sum(d['classification'] == 'duplicate' for d in decisions) == 1
    orch('status')
    receipt = root / 'receipt.json'
    receipt.write_text(json.dumps(decisions, indent=2) + '\n')
    ack = orch('inbox', 'ack', batch['id'], '--receipt', str(receipt))
    assert ack['receipt']['sha256'] == hashlib.sha256(receipt.read_bytes()).hexdigest()
    assert orch('inbox', 'ack', batch['id'], '--receipt', str(receipt)) == ack
    assert orch('inbox', 'drain', '--peek') == []
    units = orch('unit', 'list')
    assert len(units) == 3 and all(row['state'] == 'assessed' for row in units)
    print('Recovered the same batch; three assessed units, one duplicate, stable acknowledgement, empty inbox.')


if __name__ == '__main__':
    main()
