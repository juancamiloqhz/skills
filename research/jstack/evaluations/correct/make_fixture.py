"""Create owned Git history with two CLI-format regressions and one unrelated typo."""

import argparse
import json
from pathlib import Path
import subprocess


def git(root, *args):
    return subprocess.check_output(
        ["git", "-c", "core.hooksPath=/dev/null", "-C", str(root), *args],
        text=True, stderr=subprocess.PIPE,
    ).strip()


def commit(root, message, tag=None):
    git(root, "add", ".")
    git(root, "commit", "-m", message)
    if tag:
        git(root, "tag", tag)


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Fixture author")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    (root / "exporter.py").write_text('''import json


def to_json(rows):
    return json.dumps(rows)


HANDLERS = {"json": to_json}
''')
    (root / "cli.py").write_text('''import argparse
from exporter import HANDLERS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["json"], required=True)
    args = parser.parse_args()
    print(HANDLERS[args.format]([{"id": 7, "name": "Ada"}]))


if __name__ == "__main__":
    main()
''')
    (root / "AGENTS.md").write_text('''# Export project

Keep CLI format choices and exporter handlers synchronized whenever adding a format.
Preserve the output of existing formats.
''')
    (root / "README.md").write_text("# Export CLI\n\nExports a samlpe row. Use --format to select a format.\n")
    (root / "tests").mkdir()
    (root / "tests/test_cli.py").write_text('''import json
import subprocess
import sys
import unittest


class CliTest(unittest.TestCase):
    def test_json(self):
        result = subprocess.run([sys.executable, "-B", "cli.py", "--format", "json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), [{"id": 7, "name": "Ada"}])
''')
    workflow = root / ".github/workflows/check.yml"
    workflow.parent.mkdir(parents=True)
    workflow.write_text('''name: checks
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.14'
      - run: python3 -B -m unittest discover -s tests
''')
    commit(root, "Add export CLI, basic test and synchronization rule")
    p = root / "exporter.py"
    s = p.read_text().replace('HANDLERS = {"json": to_json}', '''def to_csv(rows):
    return "id,name\\n" + "\\n".join(f"{row['id']},{row['name']}" for row in rows)


HANDLERS = {"json": to_json, "csv": to_csv}''')
    p.write_text(s)
    commit(root, "Add CSV export handler", "mistake-csv")
    cli = root / "cli.py"
    cli.write_text(cli.read_text().replace('choices=["json"]', 'choices=["json", "csv"]'))
    commit(root, "Fix CSV rejected by CLI: format choices missed the new handler")
    readme = root / "README.md"
    readme.write_text(readme.read_text().replace("samlpe", "sample"))
    commit(root, "Fix README typo")
    s = p.read_text().replace('HANDLERS = {"json": to_json, "csv": to_csv}', '''def to_tsv(rows):
    return "id\\tname\\n" + "\\n".join(f"{row['id']}\\t{row['name']}" for row in rows)


HANDLERS = {"json": to_json, "csv": to_csv, "tsv": to_tsv}''')
    p.write_text(s)
    commit(root, "Add TSV export handler", "mistake-tsv")
    cli.write_text(cli.read_text().replace('choices=["json", "csv"]', 'choices=["json", "csv", "tsv"]'))
    commit(root, "Fix TSV rejected by CLI: forgot the second format list again")
    return {"root": str(root), "head": git(root, "rev-parse", "HEAD")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    print(json.dumps(create(parser.parse_args().path.resolve()), indent=2))
