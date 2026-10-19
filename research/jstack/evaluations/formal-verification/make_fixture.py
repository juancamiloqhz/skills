"""Create an owned, finite lease protocol for formal-verification authoring exercises."""

import argparse
import json
from pathlib import Path
import subprocess


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    (root / "lease.py").write_text('''from dataclasses import dataclass, replace

WORKERS = ("A", "B")


@dataclass(frozen=True)
class State:
    owner: str | None = None
    phases: tuple[str, str] = ("new", "new")


def advance(state, worker):
    """One atomic dispatcher action; each worker attempts acquisition once."""
    index = WORKERS.index(worker)
    phase = state.phases[index]
    phases = list(state.phases)
    owner = state.owner
    if phase == "new":
        phases[index] = "ready" if owner is None else "done"
    elif phase == "ready":
        if owner is None:
            owner = worker
            phases[index] = "holding"
        else:
            phases[index] = "done"
    elif phase == "holding":
        owner = None
        phases[index] = "done"
    return replace(state, owner=owner, phases=tuple(phases))
''')
    (root / "README.md").write_text('''# Lease dispatcher

Two workers, A and B, each attempt one acquisition of a single exclusive lease.
`advance(state, worker)` is the dispatcher's atomic transition. Calls are serialized;
the scheduler may choose either worker between calls. A worker observes availability,
then attempts acquisition on its next call. It may hold the lease until scheduled again.
At most one worker may be in the holding phase, or both could perform the exclusive job.

This is the complete small state machine, not a thread-safe distributed lock service.
There are no crashes, restarts, retries, network, external side effects or timing model.
No fairness or eventual-completion guarantee is promised by arbitrary scheduling.
The presentation label in `display.py` has no role in lease ownership.

Run the existing example with `python3 -B -m unittest discover -s tests`.
''')
    (root / "display.py").write_text('def label(worker):\n    return "Worker " + worker\n')
    (root / "AGENTS.md").write_text('''# Lease project

Preserve product files unless the task explicitly asks for implementation changes.
Project-local verification skills belong under `.agents/skills/`.
Proof tooling may call the actual transition function. State any bounds and assumptions.
''')
    (root / "tests").mkdir()
    (root / "tests/test_lease.py").write_text('''import unittest
from lease import State, advance


class LeaseExample(unittest.TestCase):
    def test_serial_acquisition(self):
        state = State()
        for worker in ("A", "A", "A", "B", "B", "B"):
            state = advance(state, worker)
        self.assertEqual(state, State(owner=None, phases=("done", "done")))
''')
    args = ["git", "-c", "core.hooksPath=/dev/null", "-C", str(root)]
    for command in [
        ["init", "-b", "main"], ["config", "user.name", "Fixture author"],
        ["config", "user.email", "fixture@example.invalid"],
        ["config", "commit.gpgsign", "false"], ["add", "."],
        ["commit", "-m", "Add serialized lease protocol and one scheduling example"],
    ]:
        subprocess.run(args + command, check=True, capture_output=True)
    revision = subprocess.check_output(args + ["rev-parse", "HEAD"], text=True).strip()
    return {"root": str(root), "head": revision}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    print(json.dumps(create(parser.parse_args().path.resolve()), indent=2))
