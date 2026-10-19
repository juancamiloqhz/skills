"""Create an owned two-commit Python/JavaScript fixture; never modify an existing path."""

import argparse
import json
from pathlib import Path
import subprocess


def git(root, *args):
    return subprocess.check_output(
        ["git", "-c", "core.hooksPath=/dev/null", "-C", str(root), *args],
        text=True, stderr=subprocess.PIPE,
    ).strip()


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Fixture author")
    git(root, "config", "user.email", "fixture@example.invalid")
    git(root, "config", "commit.gpgsign", "false")
    files = {
        "producer.py": '''import json


def export_records(records):
    return json.dumps([{"id": str(row["id"]), "label": row["label"]} for row in records])
''',
        "web/cache.cjs": '''function indexRecords(payload) {
  const rows = JSON.parse(payload);
  return Object.fromEntries(rows.map(row => [String(row.id), row.label]));
}
module.exports = { indexRecords };
''',
        "tests/test_producer.py": '''import json
import unittest
from producer import export_records


class ExportTest(unittest.TestCase):
    def test_labels_and_row_count(self):
        rows = json.loads(export_records([{"id": 7, "label": "first"}, {"id": 8, "label": "second"}]))
        self.assertEqual([row["label"] for row in rows], ["first", "second"])
''',
        "samples.json": json.dumps([
            {"id": 7, "label": "sample"},
            {"id": 9007199254740992, "label": "invoice A"},
            {"id": 9007199254740993, "label": "invoice B"},
        ], indent=2) + "\n",
        "README.md": '''# Ledger export fixture

`producer.export_records` emits records for `web/cache.cjs:indexRecords`.
The cache must preserve each record's exact ID and label. IDs are nonnegative
64-bit database keys. `samples.json` contains representative records.

Run producer tests with `python3 -B -m unittest discover -s tests`.
The consumer uses the Node.js built-in JSON implementation, with no package
install or local dependency patch. This is a small owned fixture, not a deployed
application. No remote PR or conversation history exists.
''',
    }
    for name, content in files.items():
        p = root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    git(root, "add", ".")
    git(root, "commit", "-m", "fixture: export identifiers to the web cache")
    base = git(root, "rev-parse", "HEAD")
    p = root / "producer.py"
    p.write_text(p.read_text().replace('str(row["id"])', 'row["id"]'))
    git(root, "commit", "-am", "fixture: keep database identifier type in JSON")
    return {"root": str(root), "base": base, "head": git(root, "rev-parse", "HEAD")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="New task-owned directory outside the skills checkout")
    print(json.dumps(create(parser.parse_args().path.resolve()), indent=2))
