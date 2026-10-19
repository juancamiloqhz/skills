"""Create a new, owned history fixture for teaching mechanics and uncertain rationale."""

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
    (root / "exporter.py").write_text('''import json

BATCH_LIMIT = 200


def export_records(records):
    return json.dumps([{"id": row["id"], "label": row["label"]} for row in records[:BATCH_LIMIT]])
''')
    (root / "consumer.cjs").write_text('''function indexRecords(payload) {
  return Object.fromEntries(JSON.parse(payload).map(row => [String(row.id), row.label]));
}
module.exports = { indexRecords };
''')
    (root / "README.md").write_text('''# Owned export fixture

Python exports records for a JavaScript cache. Preserve exact database IDs and labels.
No remote, issue tracker, team chat, measurement report or deployed application is provided.
''')
    git(root, "add", ".")
    git(root, "commit", "-m", "Add batch exporter and browser cache")
    p = root / "exporter.py"
    p.write_text(p.read_text().replace('"id": row["id"]', '"id": str(row["id"])'))
    git(root, "commit", "-am", "Preserve distinct database IDs in browser JSON",
        "-m", "Numeric IDs 9007199254740992 and 9007199254740993 become the same JavaScript Number. Export decimal strings so the browser cache preserves both keys.")
    return {"root": str(root), "head": git(root, "rev-parse", "HEAD")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    print(json.dumps(create(parser.parse_args().path.resolve()), indent=2))
