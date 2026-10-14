# Add notes

Create a note with a title and optional body, then read it from a fresh process.

## Sub-features

- `add-trim` trims surrounding title whitespace and saves the supplied body.
- `add-blank` rejects a blank title without changing stored notes.
- `add-default-body` assigns the next ID and an empty default body.

## How to get to it (user POV)

Run `python3 pocket.py --data-dir "$POCKET_DATA" add --title '  Packing list  ' --body 'Passport and charger'` in a terminal. The same `add` entry accepts `--title 'Groceries'` without `--body`.

## Driving it with Python subprocesses

Preconditions:

- The version doctor reports `Pocket 1.0`.
- The helper owns a fresh data directory and runs the map in order: empty list, first add, reads and error cases, second add, final reads.

Run `.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/generation-evidence` from the repository root to execute this recipe with assertions and evidence.

- Run the first add command above. Require JSON `{"id": 1, "title": "Packing list", "body": "Passport and charger"}` and the same object in `notes.json`.
- Run `python3 pocket.py --data-dir "$POCKET_DATA" show 1` and require the saved object in a new process.
- Run `python3 pocket.py --data-dir "$POCKET_DATA" add --title '   '`. Require exit code 2, `title must not be blank` in stderr, and unchanged stored bytes.
- Run `python3 pocket.py --data-dir "$POCKET_DATA" add --title 'Groceries'`. Require JSON `{"id": 2, "title": "Groceries", "body": ""}` and both objects persisted.

## Gotchas

Titles are trimmed. IDs increase from the highest existing ID. There is no delete command, so cleanup removes only owned disposable data.
