import hashlib, json, pathlib, subprocess
root = pathlib.Path('/tmp/jstack-perf-issue-20261016')
initial = json.loads((root / 'evidence/commands/input-manifest.json').read_text())['stdout'].splitlines()
checks = {}
for line in initial:
    if '  ' not in line:
        continue
    digest, name = line.split('  ', 1)
    if len(digest) != 64 or not all(character in '0123456789abcdef' for character in digest):
        continue
    if name in ('app/summary.cjs', 'app/summary.test.cjs'):
        continue
    actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
    checks[name] = actual == digest
    assert actual == digest, name
for name in ('summary.cjs', 'summary.test.cjs'):
    assert (root / 'app' / name).read_bytes() == (root / 'evidence/review-snapshot' / name).read_bytes(), name
template = subprocess.run(['python3', '/home/ubuntu/Dev/skills/skills/jstack/jstack-setup/scripts/models.py', 'template', '--preset', 'medium'], capture_output=True, text=True, check=True)
assert json.loads(template.stdout) == json.loads((root / 'models.json').read_text())
print(json.dumps({'unchanged_inputs_and_cli': checks, 'app_matches_review_snapshot': True, 'config_matches_unmodified_medium_template': True, 'template_command': template.args, 'template_exit_code': template.returncode, 'template_stdout': template.stdout, 'template_stderr': template.stderr}, indent=2))
