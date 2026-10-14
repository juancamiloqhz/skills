# List notes

Read all notes, including the empty state, from the supplied data directory.

## Sub-features

- `list-empty` shows an empty list without creating files.
- `list-one` shows the first persisted note.
- `list-two` shows both persisted notes.

## How to get to it (user POV)

Run `python3 pocket.py --data-dir "$POCKET_DATA" list` in a terminal.

## Driving it with Python subprocesses

Preconditions:

- The version doctor reports `Pocket 1.0`.
- The helper owns a fresh data directory and runs the map in order: empty list, first add, reads and error cases, second add, final reads.

Run `.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/generation-evidence` from the repository root to execute this recipe with assertions and evidence.

- Before adding notes, run the list command above. Require `[]`, exit code zero, and no created data directory.
- After adding Packing list, run it again. Require exactly the first note object, with ID 1, title `Packing list`, and body `Passport and charger`.
- After adding Groceries, run it again. Require both note objects in insertion order; the second has ID 2 and an empty body.
- Check the persisted JSON independently and retain it in the evidence directory. The single-note list must leave stored bytes unchanged.

## Gotchas

An empty list does not prove creation works. Run add and show as well. Reads do not create directories or files.
