---
name: verify-ledger
description: Verify Ledger CLI create, read and export features using isolated local sessions and retained transcripts.
---

# Verify Ledger

## Launch

Python 3 is the only prerequisite. No server or installation. Run from the repository root. Each feature drive owns a fresh temporary data directory and removes it in finally. Evidence lives outside scratch at the explicitly supplied path. Never drive user data.

## Doctor

`python3 .agents/skills/verify-ledger/scripts/drive.py doctor /absolute/evidence/doctor.json` checks version read-only. Expected identity is `ledger 2`. Run before each fresh feature session and after failure.

## Drive

Run `python3 .agents/skills/verify-ledger/scripts/drive.py FEATURE /absolute/evidence/FEATURE.json`, where FEATURE is create, read or export. See features/README.md. Each is a real public CLI invocation. Product output and persisted data must satisfy the documented contract even with exit 0.

Export requires the licensed-export entitlement, which this fixture cannot obtain. Its drive proves the documented rejection and records `verified-unreachable`, not a successful export. The helper exits 0 when that prerequisite check matches the contract. Never bypass entitlement. Read must preserve the body verbatim; a case change remains a failed drive.

## Evidence

The helper records every command, output and exit status, assertion result, owned data path and cleanup result. Supply unique evidence paths; never overwrite old proof. Failed assertions must return nonzero. Evidence survives cleanup.

## Cleanup

Helper finally removes only its own mkdtemp directory and checks it is absent. No shared processes exist. Confirm evidence file still exists after every attempt.

## Helpers

`scripts/drive.py` is executable; invocation shown above. Paths resolve relative to this skill, not a previous checkout.
