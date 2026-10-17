import hashlib
import json
from pathlib import Path
import subprocess
import sys

CASES = [
    ('empty', [], ''),
    ('ordinary', [
        {'currency': 'USD', 'status': 'settled', 'amount': '12.50'},
        {'currency': 'EUR', 'status': 'settled', 'amount': '2.00'},
        {'currency': 'USD', 'status': 'cancelled', 'amount': '7.00'},
    ], 'USD\t1\t1250\nEUR\t1\t200\n'),
    ('fraction', [{'currency': 'USD', 'status': 'settled', 'amount': '0.29'}], 'USD\t1\t29\n'),
    ('refund', [{'currency': 'USD', 'status': 'settled', 'amount': '-0.29'}], 'USD\t1\t-29\n'),
    ('combined', [
        {'currency': 'JPY', 'status': 'pending', 'amount': '99.00'},
        {'currency': 'EUR', 'status': 'settled', 'amount': '0.58'},
        {'currency': 'USD', 'status': 'settled', 'amount': '1.15'},
        {'currency': 'EUR', 'status': 'settled', 'amount': '-0.29'},
        {'currency': 'USD', 'status': 'settled', 'amount': '0.29'},
    ], 'EUR\t2\t29\nUSD\t2\t144\n'),
    ('excluded', [{'currency': 'USD', 'status': 'cancelled', 'amount': '0.29'}], ''),
]


def inspect(work, output):
    output.mkdir(parents=True, exist_ok=False)
    evidence = []
    for name, rows, expected in CASES:
        source = output / f'{name}.json'
        source.write_text(json.dumps(rows) + '\n')
        before = hashlib.sha256(source.read_bytes()).hexdigest()
        run = subprocess.run([sys.executable, str(work / 'receipts.py'), str(source)],
                             cwd=work, text=True, capture_output=True, timeout=15)
        preserved = before == hashlib.sha256(source.read_bytes()).hexdigest()
        evidence.append({'case': name, 'exitCode': run.returncode, 'stdout': run.stdout,
                         'stderr': run.stderr, 'expected': expected, 'inputPreserved': preserved,
                         'pass': run.returncode == 0 and run.stdout == expected and not run.stderr and preserved})
    (output / 'observations.json').write_text(json.dumps(evidence, indent=2) + '\n')
    return evidence


if __name__ == '__main__':
    if '--include-large' in sys.argv[3:]:
        CASES.append(('large', [{'currency': 'USD', 'status': 'settled',
                                'amount': '123456789012345678901234567890.12'}],
                      'USD\t1\t12345678901234567890123456789012\n'))
    rows = inspect(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
    print(json.dumps({'passed': sum(row['pass'] for row in rows), 'total': len(rows)}))
