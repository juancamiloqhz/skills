# Export

## Sub-features

Export the current note as JSON.

This requires the licensed-export entitlement. This fixture has no entitlement and cannot obtain one, so successful export is unreachable here.

## How to get to it (user POV)

Use the documented Ledger CLI from the repository root.

## Driving it with subprocess

`python3 .agents/skills/verify-ledger/scripts/drive.py export /absolute/evidence/export.json`

## Gotchas

Use only fresh owned data. Attempt export against a nonexistent child of an owned temporary directory. Expect exit 3 and JSON `{"error":"export entitlement unavailable"}` with no data created. Record `verified-unreachable` and the missing entitlement, not a successful export. Do not bypass the requirement.
