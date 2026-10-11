"""Prepare disposable Pocket worktrees from an existing generated verification skill."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--verification-skill', type=Path, required=True,
                    help='Existing generated verify-pocket directory from the generator evaluation')
args = parser.parse_args()
if not (args.verification_skill / 'SKILL.md').is_file():
    parser.error('--verification-skill must contain SKILL.md')
root = Path(tempfile.mkdtemp(prefix='jstack-maintenance-eval-'))
seed = root / 'seed'
seed.mkdir()
fixture = Path(__file__).resolve().parents[1] / 'create-verification-skill/fixture'
for name in ('README.md', 'pocket.py'):
    shutil.copy2(fixture / name, seed / name)
readme = seed / 'README.md'
readme.write_text(readme.read_text().replace('There is no UI or existing verification harness.', 'There is no UI. The project-local verification skill is at `.agents/skills/verify-pocket/`.') + '\nA successful `show` returns the complete persisted note, including its original body.\n')
skill = Path('.agents/skills/verify-pocket')
shutil.copytree(args.verification_skill, seed / skill)
def git(at, *args):
    return subprocess.run(['git', '-C', str(at), *args], check=True, capture_output=True, text=True).stdout.strip()
git(seed, 'init', '-b', 'main')
git(seed, 'add', '.')
git(seed, '-c', 'user.name=Jstack evaluation', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Pocket 1.0 with generated verification skill')
for case in ('drift', 'regression', 'clean', 'missing'):
    git(seed, 'worktree', 'add', '-b', case, str(root / case), 'main')
drift = root / 'drift'
app = drift / 'pocket.py'
s = app.read_text().replace('Pocket 1.0', 'Pocket 1.1').replace("add_parser('show')", "add_parser('get')").replace("args.command == 'show'", "args.command == 'get'")
s = s.replace("    args = parser.parse_args()", "    search = commands.add_parser('search')\n    search.add_argument('query')\n    args = parser.parse_args()")
s = s.replace("    else:\n        result = notes", "    elif args.command == 'search':\n        result = [n for n in notes if args.query.casefold() in n['title'].casefold()]\n    else:\n        result = notes")
app.write_text(s)
r = drift / 'README.md'
r.write_text(r.read_text().replace(' show ', ' get ').replace('`show`', '`get`') + '\n## Pocket 1.1 changes\n\nThe read-by-ID command is intentionally renamed from `show` to `get`, without a compatibility alias. Its returned JSON and error behavior are unchanged. The version is now `Pocket 1.1`.\n\n`search QUERY` is a new read-only command that returns notes whose titles contain QUERY, ignoring case. It returns an empty JSON array on no match and does not create data storage. Existing creation, list and validation behavior is unchanged.\n')
git(drift, 'add', 'pocket.py', 'README.md')
git(drift, '-c', 'user.name=Jstack evaluation', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Release Pocket 1.1 with get and title search')
(root / 'intentional-changes.patch').write_text(git(drift, 'diff', 'main..HEAD', '--', 'README.md', 'pocket.py') + '\n')
idx = drift / skill / 'features/README.md'
s = idx.read_text()
line = next(l for l in s.splitlines() if '| [Read notes]' in l)
s = s.replace(line + '\n', '')
line = next(l for l in s.splitlines() if '| [Create notes]' in l)
s = s.replace(line, line + '\n' + line + '\n| [Deleted legacy feature](legacy.md) | legacy | Untested |')
idx.write_text(s)
git(drift, 'add', str(skill))
git(drift, '-c', 'user.name=Jstack evaluation', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Fixture with stale verification index')
reg = root / 'regression' / 'pocket.py'
reg.write_text(reg.read_text().replace('    print(json.dumps(result))', "    if args.command == 'show':\n        result = dict(result, body='INJECTED REGRESSION')\n    print(json.dumps(result))"))
git(root / 'regression', 'add', 'pocket.py')
git(root / 'regression', '-c', 'user.name=Jstack evaluation', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Refactor note serialization')
git(root / 'missing', 'rm', '-r', str(skill))
git(root / 'missing', '-c', 'user.name=Jstack evaluation', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Fixture without verification skill')
def hashes(at):
    return {str(p.relative_to(at)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(at.rglob('*')) if p.is_file() and '.git' not in p.parts}
manifest = {'root': str(root), 'cases': {c: {'revision': git(root/c, 'rev-parse', 'HEAD'), 'before': hashes(root/c)} for c in ('drift','regression','clean','missing')}}
(root/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print(root)
