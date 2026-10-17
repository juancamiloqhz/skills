"""Replay three saved completion observations with one writer.

The parent must authenticate observations and inspect reports. This local
process-exit exercise does not query T3 or prove host-restart/exactly-once safety.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess


def save(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root', type=Path)
    parser.add_argument('observations', type=Path)
    parser.add_argument('--cli', type=Path, required=True)
    parser.add_argument('--phase', choices=['claim', 'resume'], required=True)
    parser.add_argument('--interrupt-after-first-apply', action='store_true',
                        help='resume only: exit 75 after one update, before saving its decision')
    args = parser.parse_args()
    if args.interrupt_after_first_apply and args.phase != 'resume':
        parser.error('--interrupt-after-first-apply requires --phase resume')
    root = args.root.resolve()
    observations = json.loads(args.observations.read_text())
    assert len(observations) == 3
    by_task = {row['taskId']: row for row in observations}
    assert len(by_task) == 3 and len({row['unit'] for row in observations}) == 3
    evidence = []
    report_hashes = {}
    for row in observations:
        assert row['status'] == 'completed' and row['workState'] == 'result_available'
        assert not row['hasPendingChildRuns'] and not row['hasPendingQuestion']
        assert row['childRunId'] and row['resultContextTransferId']
        report = Path(row['reportPath']).read_bytes()
        assert report.strip()
        report_hashes[row['taskId']] = hashlib.sha256(report).hexdigest()
        evidence.append({'observation': row, 'reportSha256': report_hashes[row['taskId']]})

    def orch(*words):
        result = subprocess.run(['bun', str(args.cli.resolve()), '--store', str(root / 'store'),
                                 '--json', *words], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    receipt = root / 'receipt.json'
    if args.phase == 'claim':
        root.mkdir(parents=True, exist_ok=False)
        save(root / 'evidence.json', evidence)
        orch('init')
        orch('standing', 'add', 'Evaluation bookkeeping only. No PR verdicts, dispatch, merge or schedule.')
        for row in observations:
            orch('unit', 'add', row['unit'], '--track', 'authoring')
            orch('inbox', 'push', row['taskId'], row['unit'], 'completed', '--report', row['reportPath'])
        row = observations[-1]
        orch('inbox', 'push', row['taskId'], row['unit'], 'completed', '--report', row['reportPath'])
        batch = orch('inbox', 'claim')
        assert len(batch['entries']) == 4
        save(root / 'claimed.json', batch)
        save(receipt, [])
        print('Four pointers claimed; no decisions applied; exiting before acknowledgement.')
        return

    assert evidence == json.loads((root / 'evidence.json').read_text()), 'observation or report changed'
    batch = json.loads((root / 'claimed.json').read_text())
    current = json.loads((root / 'store' / 'inbox-batch.json').read_text())
    assert current['id'] == batch['id'] and current['entries'] == batch['entries'], 'batch changed'
    expected = []
    seen = set()
    for entry in batch['entries']:
        pointer = entry['pointer']
        row = by_task[pointer['agent']]
        assert (pointer['unit'], pointer['status'], pointer['report']) == (
            row['unit'], 'completed', row['reportPath']), 'pointer does not match observation'
        identity = (row['taskId'], row['childRunId'], row['resultContextTransferId'])
        expected.append({'filename': entry['filename'], 'taskId': row['taskId'],
                         'childRunId': row['childRunId'], 'result': row['resultContextTransferId'],
                         'unit': row['unit'], 'reportPath': row['reportPath'],
                         'classification': 'duplicate' if identity in seen else 'assessed',
                         'reportSha256': report_hashes[row['taskId']]})
        seen.add(identity)
    decisions = json.loads(receipt.read_text())
    assert decisions == expected[:len(decisions)], 'saved decisions changed'
    assert len(decisions) <= len(expected)
    units = {row['id']: row for row in orch('unit', 'list')}
    assert set(units) == {row['unit'] for row in observations}
    for row in units.values():
        assert row == dict(id=row['id'], track='authoring', state=row['state'],
                           branch='', pr='', sha='', brief=''), 'unit identity changed'
        assert row['state'] in {'pending', 'assessed'}
    for decision in decisions:
        assert units[decision['unit']]['state'] == 'assessed', 'saved effect missing'

    if current['state'] == 'acknowledged':
        assert decisions == expected, 'acknowledged batch lacks decisions'
        assert current['receipt']['sha256'] == hashlib.sha256(receipt.read_bytes()).hexdigest()
        assert orch('inbox', 'ack', batch['id'], '--receipt', str(receipt)) == current
        print('Batch already acknowledged; no unit updates or decision writes.')
        return

    assert orch('inbox', 'claim') == batch
    for decision in expected[len(decisions):]:
        unit = decision['unit']
        if decision['classification'] == 'assessed' and units[unit]['state'] == 'pending':
            units[unit] = orch('unit', 'set', unit, '--state', 'assessed')
            if args.interrupt_after_first_apply:
                print('Injected process exit after first application; decision unsaved; batch pending.')
                raise SystemExit(75)
        assert units[unit]['state'] == 'assessed'
        decisions.append(decision)
        save(receipt, decisions)
    orch('status')
    ack = orch('inbox', 'ack', batch['id'], '--receipt', str(receipt))
    assert ack['receipt']['sha256'] == hashlib.sha256(receipt.read_bytes()).hexdigest()
    assert orch('inbox', 'ack', batch['id'], '--receipt', str(receipt)) == ack
    assert orch('inbox', 'drain', '--peek') == []
    assert all(row['state'] == 'assessed' for row in orch('unit', 'list'))
    print('Three assessed units, one duplicate, stable acknowledgement, empty inbox.')


if __name__ == '__main__':
    main()
