# Show a note

Read a persisted note by ID and distinguish a missing note from a successful read.

## Sub-features

- `show-existing` retrieves the first saved note.
- `show-second` retrieves the second saved note.
- `show-missing` rejects an absent ID without changing data.

## How to get to it (user POV)

Run `python3 pocket.py --data-dir "$POCKET_DATA" show 1` in a terminal; replace `1` with the desired note ID.

## Driving it with Python subprocesses

Preconditions:

- The version doctor reports `Pocket 1.0`.
- The helper owns a fresh data directory and runs the map in order: empty list, first add, reads and error cases, second add, final reads.

Run `.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/generation-evidence` from the repository root to execute this recipe with assertions and evidence.

- After adding Packing list, run `python3 pocket.py --data-dir "$POCKET_DATA" show 1`. Require the title `Packing list` and body `Passport and charger` with ID 1.
- Run `python3 pocket.py --data-dir "$POCKET_DATA" show 999`. Require exit code 2 and `note not found` in stderr.
- After adding Groceries, run `python3 pocket.py --data-dir "$POCKET_DATA" show 2`. Require title `Groceries`, ID 2, and an empty body.
- Compare `notes.json` bytes before and after the first successful and missing-note reads. They must match.

## Gotchas

A missing note is an error, not a null JSON result. The data directory must identify the same isolated run as the add commands.
