---
name: verify-pocket
description: "Verify Pocket's local note CLI after changes to add, show, list, or note persistence. Run public commands, assert JSON and file state, and retain proof."
---

# Verify Pocket

Read [the feature map](features/README.md), then run the helper below. Python 3 is the only prerequisite. Pocket has no server, credentials, installation, browser, or external service.

## Launch

From the repository root, run:

```sh
python3 pocket.py --version
.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/generation-evidence
```

The version must be `Pocket 1.0`. This short-lived CLI needs no build or persistent process. The helper resolves the repository from its own location and runs each command through a Python subprocess with a 15-second timeout. It creates a unique `.pocket-verify-*` scratch directory in the repository. Each invocation receives its own `--data-dir`; concurrent runs must never share a data directory. The helper tears down scratch in `finally`, including failed runs.

The evidence-root argument names a writable, authorized artifact directory, not application data. For other checkouts, choose an authorized location or omit the option to use `.verification-evidence` under that checkout. Every run creates a new evidence subdirectory and prints its path before driving Pocket.

## Doctor

Run `python3 pocket.py --version` from the repository root. Require exit code zero and exactly `Pocket 1.0`. This checks identity without creating, seeding, or repairing a data directory. The helper repeats this check and records the source hash and Python interpreter. If it fails, retain the diagnostics and report the blocker. Do not install dependencies or modify the application to make the check pass.

## Drive

The helper runs the real `add`, `show`, and `list` commands and checks their JSON, exit codes, and persisted `notes.json`. It starts with an empty directory, adds a trimmed title and body, reads that note in fresh processes, checks rejected blank titles and missing IDs, adds a second note with the default body, and lists both notes. Read commands and rejected writes must leave persisted bytes unchanged.

Use [add](features/add.md), [show](features/show.md), and [list](features/list.md) for the exact user entries and expected results. The helper drives all three maps in one isolated run. An assertion mismatch fails the helper even if Pocket exits zero. A failed run is not proof of success.

## Evidence

Each printed evidence directory retains `identity.json`, `commands.jsonl`, `notes.json` on successful runs, and `summary.json`. Failed runs also retain `failure.txt`. The command log records each action, feature ID, argv, stdout, stderr, and exit code. Identity includes the actual application path and source hashes. The final notes snapshot proves the filesystem side effect; `show` and `list` independently prove the user-visible persisted state.

After the helper exits zero, inspect `summary.json` and require `passed: true`. Confirm its scratch path is absent and the artifacts still exist. Use synthetic notes only; artifacts must contain no secrets. Exercise public commands rather than internal setters. There are no mocks or dry-run modes here. Any later test mode must prove which side effects it skips by observation. This skill does not authorize messages, charges, publication, or shared-service changes.

## Cleanup

The helper removes only the scratch directory it created and checks that it is gone. Subprocess calls finish before cleanup; timeouts terminate the child and fail the run. Never kill processes by name. Evidence stays outside scratch and survives teardown. No Pocket delete command exists.

If the helper is forcibly terminated before `finally` can run, use the exact scratch path recorded in that run's `summary.json`, if available, or establish ownership from the recorded command data paths before cleanup. Preserve unidentified directories. Never remove the evidence directory as cleanup.

## Helpers

`scripts/verify.py` is executable. Its invocation appears under Launch. It resolves source paths relative to the installed skill, propagates application/assertion failures, and preserves diagnostics before cleanup. No global installation is needed.

Use `/maintain-verification-skill` when Pocket changes so the recipes and exercised coverage stay accurate.
