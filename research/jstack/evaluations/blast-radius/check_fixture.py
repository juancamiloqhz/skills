"""Check the generated fixture contract; HEAD intentionally fails until the product is fixed."""

import argparse
import json
import subprocess
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('root', type=Path, help='Owned repository created by make_fixture.py')
parser.add_argument('revision', nargs='?', default='HEAD')
args = parser.parse_args()
ROOT = args.root.resolve()
revision = args.revision
commit = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', revision], text=True).strip()
source = subprocess.check_output(['git', '-C', str(ROOT), 'show', f'{commit}:producer.py'], text=True)
namespace = {}
exec(compile(source, f'{commit}:producer.py', 'exec'), namespace)
consumer = ROOT / 'web/cache.cjs'
node = '''
const fs = require('node:fs');
const {indexRecords} = require(process.argv[1]);
const payload = fs.readFileSync(0, 'utf8');
console.log(JSON.stringify({
  parsedIds: JSON.parse(payload).map(row => String(row.id)),
  cache: indexRecords(payload)
}));
'''
cases = {
    'safe-integer controls': [
        {'id': 0, 'label': 'zero'},
        {'id': 7, 'label': 'small'},
        {'id': 9007199254740991, 'label': 'max safe'},
    ],
    'repository samples': json.loads((ROOT / 'samples.json').read_text()),
}
failed = False
print(f'revision={commit}')
for name, records in cases.items():
    payload = namespace['export_records'](records)
    result = json.loads(subprocess.check_output(
        ['node', '-e', node, str(consumer)], input=payload, text=True
    ))
    expected = {str(row['id']): row['label'] for row in records}
    passed = result['cache'] == expected
    failed |= not passed
    print(f'{name}: {"PASS" if passed else "FAIL"}')
    print('payload=' + payload)
    print('parsedIds=' + json.dumps(result['parsedIds']))
    print('expected=' + json.dumps(expected, sort_keys=True))
    print('actual=' + json.dumps(result['cache'], sort_keys=True))
if failed:
    print('FAIL: consumer did not preserve every exact ID and label')
    sys.exit(1)
print('PASS: consumer preserved every exact ID and label')
