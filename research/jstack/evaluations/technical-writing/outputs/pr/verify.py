import hashlib
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys

root = Path('/tmp/jstack-writing-eval-20261015/pr')
fixtures = Path('/home/ubuntu/Dev/skills/research/jstack/evaluations/technical-writing/fixtures')
log = [f'Python: {sys.version}', 'All CLI data directories are under ' + str(root)]
checks = 0
for name in ('before.py', 'pocket.py'):
    source = fixtures / name
    target = root / name
    shutil.copyfile(source, target)
    log.append(f'{name} SHA256: {hashlib.sha256(source.read_bytes()).hexdigest()}')

def run(name, directory, *args):
    cmd = [sys.executable, '-B', str(root / name), '--data-dir', str(directory), *args]
    result = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
    log.extend(['$ ' + shlex.join(cmd), f'exit: {result.returncode}', 'stdout: ' + result.stdout.rstrip(), 'stderr: ' + result.stderr.rstrip()])
    return result

try:
    for name in ('before.py', 'pocket.py'):
        for label, title in [('padded', '  groceries  '), ('blank', ' \t\n '), ('empty', '')]:
            directory = root / 'data' / name.removesuffix('.py') / label
            assert not directory.exists(), 'Use a fresh run directory'
            result = run(name, directory, 'add', '--title', title, '--body', 'keep this body')
            rejected = name == 'pocket.py' and label != 'padded'
            if rejected:
                assert result.returncode == 2
                assert 'title must not be blank' in result.stderr
                assert not directory.exists()
            else:
                assert result.returncode == 0
                note = json.loads(result.stdout)
                assert note['title'] == (title.strip() if name == 'pocket.py' else title)
                assert note['body'] == 'keep this body'
                assert json.loads((directory / 'notes.json').read_text()) == [note]
            checks += 1
            log.append('PASS: ' + name + ' ' + label)
    directory = root / 'data' / 'existing'
    directory.mkdir(parents=True)
    old = [{'id': 7, 'title': '  old title  ', 'body': 'old body'}]
    notes = directory / 'notes.json'
    notes.write_text(json.dumps(old, indent=2) + '\n')
    original = notes.read_bytes()
    result = run('pocket.py', directory, 'add', '--title', '   ')
    assert result.returncode == 2 and notes.read_bytes() == original
    checks += 1
    log.append('PASS: rejected add preserves existing notes byte for byte')
    result = run('pocket.py', directory, 'add', '--title', '  new title  ', '--body', '  body remains  ')
    assert result.returncode == 0
    new = json.loads(result.stdout)
    assert new == {'id': 8, 'title': 'new title', 'body': '  body remains  '}
    assert json.loads(notes.read_text()) == old + [new]
    checks += 1
    log.append('PASS: valid add trims new title, preserves old note and body, and assigns next ID')
    for args, expected in [(('show', '8'), new), (('list',), old + [new])]:
        result = run('pocket.py', directory, *args)
        assert result.returncode == 0 and json.loads(result.stdout) == expected
        checks += 1
        log.append('PASS: ' + args[0])
    log.append(f'PASS: {checks} behavior checks')
finally:
    (root / 'evidence.txt').write_text('\n'.join(log) + '\n')
print('\n'.join(line for line in log if line.startswith('PASS:')))
