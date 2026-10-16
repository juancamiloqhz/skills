import argparse
import collections
import json
import pathlib

parser = argparse.ArgumentParser(description='Throwaway batch import behavior experiment')
parser.add_argument('--variant', choices=['atomic', 'first-valid', 'reject-duplicate-groups', 'all'], default='all')
args = parser.parse_args()
cases = json.loads(pathlib.Path('/tmp/jstack-prototype-input-20261016/cases.json').read_text())
variants = ['atomic', 'first-valid', 'reject-duplicate-groups'] if args.variant == 'all' else [args.variant]
for variant in variants:
    for case, rows in cases.items():
        id_counts = collections.Counter(row['id'] for row in rows if isinstance(row.get('id'), str) and row['id'] != '')
        accepted = []
        rejected = []
        accepted_ids = set()
        for number, row in enumerate(rows, start=1):
            reasons = []
            for field in ['id', 'email']:
                if not isinstance(row.get(field), str) or row[field] == '':
                    reasons.append(field + ' must be a nonempty string')
            if isinstance(row.get('id'), str) and row['id'] != '':
                if variant in ['atomic', 'reject-duplicate-groups'] and id_counts[row['id']] > 1:
                    reasons.append('ID repeats within this upload')
                elif variant == 'first-valid' and row['id'] in accepted_ids:
                    reasons.append('ID already accepted from an earlier valid row')
            record = {'row': number, 'data': row}
            if reasons:
                rejected.append({**record, 'reasons': reasons})
            else:
                accepted.append(record)
                accepted_ids.add(row['id'])
        if variant == 'atomic' and rejected:
            for record in accepted:
                rejected.append({**record, 'reasons': ['Upload rejected because another row has an error']})
            accepted = []
            rejected.sort(key=lambda record: record['row'])
        print(json.dumps({'variant': variant, 'case': case, 'accepted': accepted, 'rejected': rejected}, sort_keys=True))
