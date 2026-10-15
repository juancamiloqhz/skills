"""Synthetic NDJSON export library. Single worker, UTF-8, no filesystem I/O."""
import hashlib
import json

OPTIONS = dict(ensure_ascii=False, separators=(',', ':'), sort_keys=True)


def records(count):
    return [{'id': i, 'name': 'café-' + str(i), 'active': i % 3 == 0,
             'fingerprint': hashlib.sha256(str(i).encode()).hexdigest()}
            for i in range(count)]


def encode_rows(rows, variant):
    if variant == 'A':
        return '\n'.join(json.dumps(row, **OPTIONS) for row in rows) + '\n'
    if variant == 'B':
        encoder = json.JSONEncoder(**OPTIONS)
        return '\n'.join(encoder.encode(row) for row in rows) + '\n'
    raise ValueError('unknown variant')


def export(count, variant):
    return encode_rows(records(count), variant).encode('utf-8')
