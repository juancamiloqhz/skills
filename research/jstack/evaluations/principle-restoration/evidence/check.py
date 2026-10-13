import collections
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time

base = Path(__file__).resolve().parent
results = []
with tempfile.TemporaryDirectory(prefix='jstack-principle-evidence-') as scratch:
    root = Path(scratch)
    heartbeat = root / 'heartbeat'
    code = "from pathlib import Path; import sys,time; Path(sys.argv[1]).write_text('alive'); time.sleep(60)"
    proc = subprocess.Popen([sys.executable, '-c', code, str(heartbeat)])
    try:
        deadline = time.monotonic() + 5
        while not heartbeat.exists() and time.monotonic() < deadline:
            time.sleep(.01)
        assert heartbeat.exists()
        assert proc.poll() is None
        results.append({'test': 'heartbeat live process direct poll', 'running': True})
        proc.terminate()
        proc.wait(timeout=5)
        age = time.time() - heartbeat.stat().st_mtime
        assert age < 5 and proc.poll() is not None
        results.append({'test': 'fresh heartbeat survives stopped process', 'heartbeatAgeSeconds': round(age, 4), 'returncode': proc.returncode, 'running': False})
    finally:
        if proc.poll() is None:
            proc.kill()
            proc.wait()

    # This encodes the counts supplied by the scenario; it is not production telemetry.
    events = ['A'] * 100 + ['B'] * 100
    census = dict(collections.Counter(events))
    assert census == {'A': 100, 'B': 100}
    results.append({'test': 'rerunnable supplied-scenario census', 'counts': census, 'conclusion': 'Observed count skew absent; causal effect not established.'})

    expected = [{'id': 1, 'value': 'a'}, {'id': 2, 'value': 'b'}]
    for stage in ['before_write', 'partial_write', 'before_publish', 'after_publish']:
        directory = root / stage
        directory.mkdir()
        output = directory / 'export.json'
        output.write_text('[{"previous":"complete"}]')
        failed = subprocess.run([sys.executable, str(base / 'export.py'), str(directory), stage], capture_output=True, text=True)
        assert failed.returncode == 75
        prior = json.loads(output.read_text())
        assert prior == (expected if stage == 'after_publish' else [{'previous': 'complete'}])
        for attempt in range(2):
            rerun = subprocess.run([sys.executable, str(base / 'export.py'), str(directory)], capture_output=True, text=True)
            assert rerun.returncode == 0, rerun.stderr
            assert json.loads(output.read_text()) == expected
            assert not (directory / 'export.pending').exists()
        results.append({'test': 'export crash and two retries', 'crashStage': stage, 'crashExitCode': failed.returncode, 'completeOutputPreserved': True, 'retryCount': 2, 'passed': True})
print(json.dumps(results, indent=2))
