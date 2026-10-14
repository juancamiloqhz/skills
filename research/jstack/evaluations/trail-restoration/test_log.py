#!/usr/bin/env python3
"""Exercise the distributed logger through its CLI in temporary directories."""
import csv
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / 'skills/jstack/show-me-your-work/scripts/log.sh'
TEMPLATE = ROOT / 'skills/jstack/show-me-your-work/references/decision-log-template.tsv'


def main():
    checks = []
    with tempfile.TemporaryDirectory(prefix='jstack-trail-cli-') as temp:
        log = Path(temp) / 'nested dir/decisions.tsv'
        def append(*cells):
            subprocess.run([str(SCRIPT), str(log), *cells], check=True, capture_output=True)
        for count in (0, 5, 7):
            result = subprocess.run([str(SCRIPT), *(['unused'] * count)], capture_output=True)
            assert result.returncode == 1 and b'usage:' in result.stderr
        assert not log.exists()
        checks.append('invalid argument counts reject without log creation')
        append('frame', 'counted units', 'scope first', '/evidence/frame.json', 'open')
        first = log.read_bytes()
        assert first.startswith(TEMPLATE.read_bytes())
        append('unit', 'verified unit', 'predicate matched', '/evidence/check.json', 'VERIFIED')
        assert log.read_bytes().startswith(first)
        rows = list(csv.reader(log.read_text().splitlines(), delimiter='\t'))
        assert len(rows) == 3 and all(len(row) == 6 for row in rows)
        assert all(re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z', row[0]) for row in rows[1:])
        checks.append('nested directory, template header, UTC stamps and preserved prior bytes')
        append('a\tb\nc\rd', '=SUM(1)', '+formula', '-formula', '@formula')
        row = list(csv.reader(log.read_text().splitlines(), delimiter='\t'))[-1]
        assert row[1:] == ['a b c d', "'=SUM(1)", "'+formula", "'-formula", "'@formula"]
        checks.append('embedded tab/newline/CR normalized; all four formula prefixes quoted')
        append('', '', '', '', '')
        assert list(csv.reader(log.read_text().splitlines(), delimiter='\t'))[-1][1:] == [''] * 5
        before = log.read_bytes()
        append('correct', 'supersedes prior claim', 'observed failure', '/evidence/failure.json', 'NOT VERIFIED')
        assert log.read_bytes().startswith(before)
        checks.append('empty cells stay six columns; corrections append without rewriting history')
        log.write_bytes(b'')
        append('frame', 'empty existing log', 'new run', '/evidence/frame.json', 'open')
        assert log.read_bytes().startswith(TEMPLATE.read_bytes())
        checks.append('existing empty log gets a header')
    print(json.dumps({'passed': checks, 'limits': ['serial writers only; no network-mount fault injection or concurrent append test']}, indent=2))


if __name__ == '__main__':
    main()
