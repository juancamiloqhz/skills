# Pocket verification map

The public CLI is Pocket's only user interface. Read the matching feature file before verification. The executable helper runs all three recipes with fresh isolated state.

## Preconditions and conventions

Use Python 3 and the checkout's `pocket.py`. Run the read-only version doctor first. Every command needs `--data-dir` except `--version`. The helper's owned directory starts empty; no user directory is reused. Writes to a shared directory are unsupported.

In recipes below, `$POCKET_DATA` means the helper's newly created data path, never an existing user directory. Commands show the exact application entry points; the helper supplies their path and performs assertions. Run the helper from SKILL.md to execute the recipes together. Preserve command transcripts, identity, result JSON, storage snapshots, and cleanup outcome. A skipped path remains unverified.

## Features and exercised coverage

- [Add notes](add.md): title trimming, body persistence, blank-title rejection, ID increment, and default body.
- [Show notes](show.md): existing IDs and missing-ID errors.
- [List notes](list.md): empty, single-note, and two-note lists; reads preserve storage.

Coverage status: all listed paths passed on 2026-10-14. The retained proof is `/tmp/jstack-verification-restoration/generation-evidence/pocket-lijm32z3`; its `summary.json` reports `passed: true`. Future runs must produce their own proof. Argument-parser errors outside the listed paths and corrupt user data are not covered.
