"""Single-writer local export: deterministic complete file + atomic publication."""
import json
import os
from pathlib import Path
import sys

root = Path(sys.argv[1])
stage = sys.argv[2] if len(sys.argv) > 2 else ''
root.mkdir(parents=True, exist_ok=True)
pending = root / 'export.pending'
output = root / 'export.json'

def crash(point):
    if stage == point:
        os._exit(75)

# Single-writer assumption makes an existing pending file abandoned work.
pending.unlink(missing_ok=True)
crash('before_write')
with pending.open('wb') as stream:
    stream.write(b'[')
    stream.flush()
    crash('partial_write')
    stream.seek(0)
    stream.write(json.dumps([{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}], sort_keys=True).encode())
    stream.truncate()
    stream.flush()
    os.fsync(stream.fileno())
crash('before_publish')
os.replace(pending, output)
crash('after_publish')
print(output.read_text())
