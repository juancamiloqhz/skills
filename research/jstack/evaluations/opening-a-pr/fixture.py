from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1]).resolve()
root.mkdir(parents=True, exist_ok=False)


def git(*args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True).strip()


git('init', '-b', 'main')
git('config', 'user.name', 'Fixture Author')
git('config', 'user.email', 'fixture@example.invalid')
(root / 'catalog.py').write_text('def items():\n    return ["alpha"]\n')
(root / 'notes.txt').write_text('original unrelated note\n')
git('add', 'catalog.py', 'notes.txt')
git('commit', '-m', 'test: seed catalog fixture')
(root / 'catalog.py').write_text('def items():\n    return ["alpha", "beta"]\n')
(root / 'USAGE.md').write_text('# Catalog\n\n`items()` returns `alpha` and `beta`.\n')
(root / 'notes.txt').write_text('staged unrelated note\n')
git('add', 'notes.txt')
(root / 'notes.txt').write_text('unstaged unrelated note\n')
(root / 'private.txt').write_text('unrelated untracked note\n')
(root / '.git/info/exclude').write_text('ignored.txt\n')
(root / 'ignored.txt').write_text('unrelated ignored note\n')
print(root)
