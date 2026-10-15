#!/usr/bin/env python3
"""Recompute retained summaries and verify fixture outputs without benchmarking."""
import hashlib
import importlib.util
import json
from pathlib import Path
import statistics
import sys

sys.dont_write_bytecode = True
root = Path(__file__).resolve().parent
runtime = json.loads((root/'runtime-record.json').read_text())
cases = json.loads((root/'cases-record.json').read_text())
for archive in (runtime, cases):
    for path, value in archive['files'].items():
        assert hashlib.sha256(value.encode()).hexdigest() == archive['sha256'][path], path


def artifact(archive, path):
    return json.loads(archive['files'][path])


runs = artifact(runtime, 'output/runs.json')
summary = artifact(runtime, 'output/summary.json')
checks = artifact(runtime, 'output/checks.json')
assert len(runs) == 36 and len(checks) == 42
for path in ('export', 'encode_rows'):
    selected = [r for r in runs if r['path'] == path]
    assert [(r['run'], r['variant']) for r in selected] == [
        (i, variant) for i in range(1, 10) for variant in ('A', 'B')]
    for variant in ('A', 'B'):
        values = [r for r in selected if r['variant'] == variant]
        assert all(r['exception'] is None for r in values)
        wall = [r['wall_ms'] for r in values]
        cpu = [r['cpu_ms'] for r in values]
        assert summary[path][variant] == dict(n=9, median_ms=statistics.median(wall),
                                            min_ms=min(wall), max_ms=max(wall),
                                            median_cpu_ms=statistics.median(cpu))
assert summary['exceptions'] == summary['content_failures'] == summary['ndjson_failures'] == 0
spec = importlib.util.spec_from_file_location('fixture', root/'fixture.py')
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)
assert (root/'fixture.py').read_text() == runtime['files']['exporter.py']
for count in (2000, 20000):
    outputs = [fixture.export(count, variant) for variant in ('A', 'B')]
    assert outputs[0] == outputs[1]
    raw = outputs[0]
    rows = [json.loads(line) for line in raw.decode().splitlines()]
    assert len(rows) == count and raw.endswith(b'\n')
    for i, row in enumerate(rows):
        assert row == dict(id=i, name='café-'+str(i), active=i % 3 == 0,
                           fingerprint=hashlib.sha256(str(i).encode()).hexdigest())
    digest = hashlib.sha256(raw).hexdigest()
    if count == 20000:
        assert all(c['sha256'] == digest and c['rows'] == count and c['bytes'] == len(raw)
                   and c['content_ok'] and c['byte_exact'] and c['ndjson_ok'] for c in checks)
    else:
        single = artifact(cases, 'output/c5-stdout.json')
        assert single['run_count'] == 1 and single['rows_validated'] == count
        assert single['output_sha256'] == digest and single['bytes_produced'] == len(raw)
        assert single['export_errors'] == 0 and single['validation_errors'] == []
        assert cases['excluded']['output/c5-export.ndjson']['sha256'] == digest
print(json.dumps({'archiveHashes': 'match', 'alternatingMeasuredCalls': 36,
                  'completedRuntimeChecks': 42, 'recomputedSummaries': 'match',
                  'unmeasuredOutputReplay': 'both variants match all expected fields and retained hashes at 2000/20000 rows',
                  'timingReplay': 'not performed; historical timings are observations, not repeatable assertions'}, indent=2))
