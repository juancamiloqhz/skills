# Verification maintenance evaluation

Executed on 2026-10-11 against [maintain-verification-skill](../../../../skills/maintain-verification-skill/SKILL.md). Three fresh Codex subagents independently applied the skill to separate Pocket worktrees. Each received the maintenance skill, the target repository, a realistic upkeep request and execution boundaries. They did not receive the expected outcome or inspect sibling cases. The [results record](results.json) contains hashes, observed outcomes and inspected proof locations.

## Cases and observations

| Case | Fixture change | Observed result |
| --- | --- | --- |
| Intentional drift | Release contract changes Pocket 1.0 to 1.1, renames `show` to `get`, adds title search; the verification index has a duplicate, a dead link and an omitted feature | `changed`; agent repaired six verification files, added search coverage, and passed 15 real CLI calls across four features |
| Product regression | `show` returns an incorrect body while exiting zero; the documented contract still requires the persisted body | `blocked`; verifier failed with `Show mismatch across processes`; agent preserved assertions and application files, then exercised independent remaining paths |
| Unchanged baseline | Pocket 1.0 and its existing generated verification skill | `clean`; doctor and all three mapped features passed, with 11 calls in the full verification run; working tree unchanged |
| Missing target | Pocket checkout with the verification directory removed | Parent locator smoke check found no target, launched nothing and generated no files; this was not an independent agent evaluation |

The parent inspected actual diffs and JSON proof, rather than relying on agent summaries. Checks confirmed unchanged application and README hashes, edits confined to the verification directory, preserved historical evidence, removed scratch directories, retained proof, resolved local Markdown links and clean whitespace. All owned processes were synchronous CLI subprocesses; no service was started. No skills or dependencies were installed, provider settings changed, or external services accessed.

## What the repair proved

The drift run first recorded a failing doctor with the old version expectation. It repaired the documented identity and command changes, passed doctor on its one retry, and ran the full updated helper. Creation, reads and validation errors retained their assertions. Search added absent-storage behavior, a case-insensitive title substring match, no-match and body-only-query exclusions, plus state-preservation checks. The repaired index contains one entry per current feature, and the generation-time evidence remains explicitly historical.

The regression run's helper failed after eight CLI calls. The agent doctored the application again, then used a temporary public-CLI script to finish independent list and error coverage. It reported the product failure and left the entire repository unchanged. The helper's first-failure behavior required this supplemental script; the agent completed that work without changing the maintenance instructions.

No change to the maintenance skill was needed after these runs. The evaluation does not compare performance with and without the skill.

## Reproduce

Prerequisites are Python 3, Git and an existing generated Pocket verification skill from the [generator evaluation](../create-verification-skill/README.md). The preparation script expects that fixture's `verify-pocket` layout, including the `features/README.md` rows for Create notes and Read notes. A fresh generator may choose another layout; reconcile those fixture selectors before using it. The original generated files are not part of the installable skill or this repository's retained evidence.

From the skills repository root, run:

```sh
python3 research/jstack/evaluations/maintain-verification-skill/prepare.py --verification-skill /path/to/verify-pocket
```

The script creates a new temporary Git repository with `drift`, `regression`, `clean` and `missing` worktrees. It copies the generated verification skill, applies the controlled application changes, commits the local fixture history and records input hashes in `manifest.json`. It does not modify the supplied skill or the source fixture. The published script was executed separately and produced identical input file hashes for all four evaluated cases.

Give a fresh agent each of the first three worktrees and this prompt, replacing the paths:

```text
Use MAINTENANCE/SKILL.md to audit and maintain Pocket's existing verification skill against the current application in TARGET. Report what you changed and exercised. Work only in this worktree and your own temporary evidence. Do not inspect sibling cases, modify the application, install anything, contact external services, change provider settings, commit, push or delegate. Save a report outside the repository with outcome, changed files, per-feature coverage, evidence, cleanup and limitations.
```

For the drift case, add that Pocket has changed. Inspect each result against the case table, then check file hashes and actual proof. The successful invocation should be the documented helper command, not an improvised substitute for a broken verifier. In the regression case, require a failing content assertion despite the application's zero exit status. Verify that evidence survives cleanup and the clean case has no changed files. Keep each worktree isolated until inspection is complete.

## Limits

These are focused CLI functional evaluations. They do not establish browser, API, library, interactive-terminal, cross-provider or automatic-discovery behavior. There was no without-skill baseline, live PR publication, installation or model-routing trial. The missing-target case is only a parent smoke check. Multiple candidate selection, missing feature maps, absent credentials, ambiguous contract changes, partial edits and failed cleanup were not behaviorally evaluated.

The Pocket recipes do not cover Unicode/empty search queries, multiple matches, corrupt storage, manually gapped IDs, concurrent writers, the complete argument-error matrix, filesystem faults or forced process termination. Raw reports were inspected locally and remain in temporary storage, whose paths may expire. The retained hashes identify this run; generated output may differ on a later run.
