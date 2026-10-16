# Deslop evaluation

Standalone `jstack-deslop` supplies Juan-mode's pre-commit cleanup dependency. It adds a helper, not another playbook. Five procedures are available and 18 remain pending.

## Source and caller

[Complete comparison](source-comparison.json) covers the entire helper and Juan-mode entrypoint against `11713c683fe4add4fd403ea880580abbc9e0875f`. The source directory has one file. The only skill change is its name, from `deslop` to `jstack-deslop`. Its description, body, focus areas, guardrails and reply length are byte-identical to upstream. The package includes the exact pinned Cursor team-kit MIT license.

The mode's pre-commit trigger selects the new identity, and its dependency paragraph identifies the standalone helper while keeping Control UI external. Existing mode support files and all five playbooks match the base commit. The [adaptation record](../../adaptations/deslop.md) accounts for every difference.

The manifest adds the Deslop mapping, exact source watch subtree and mode caller context. The license was already watched. There are 43 mappings; existing pins, decisions and the reviewed checkpoint remain unchanged.

## Standalone cleanup exercise

The [input archive](inputs.json) retains a small TypeScript repository with a `main` baseline and feature branch. The branch adds a public JSON report formatter. It contains both redundant code and necessary boundary validation. The caller also has a staged note edit and an untracked scratch note.

A fresh evaluator receives the exact skill path and a cleanup-only request. It may edit only `src/report.ts`, must preserve public behavior and other work, and may run the existing check. It receives no proposed cleanup. [Raw evidence](live-evaluation.json) retains the actual before/after source, diffs against main, commands, test output, status, hashes and report.

The evaluator replaces the private formatter's nested logic with an empty-array early return and a typed map/join expression. It removes two comments that narrate code, an unnecessary `any` cast, redundant null checks and a catch that only rethrows. The public parser remains byte-identical, including its malformed-JSON catch, shape and count validation, 100-item limit and the comment explaining that limit.

All 14 existing public checks pass before and after, with identical outputs. They cover empty and populated reports, zero counts, empty names, malformed JSON, invalid containers/items, invalid counts and an oversized batch. The check invokes the existing local TypeScript compiler and then runs the public entrypoint; it is not merely a compile check. Tests and configuration stay unchanged.

[Parent verification](parent-verification.json) reruns the existing check and compares its actual results with both evaluator outputs and the original baseline. It also confirms only `src/report.ts` changed, the public parser is byte-identical, HEAD did not move and the staged diff, caller notes and global model file are unchanged. The final user-style reply stays within the source's one-to-three-sentence requirement.

## Preparation and limits

The first fixture preparation failed with TypeScript TS5011 because its configuration lacked an explicit `rootDir`. The second fixture sets `rootDir` to `src` before the evaluator starts. Both preparation scripts and the failure note are archived; this was a fixture correction, not a skill failure or a concealed evaluator rerun. The existing compiler comes from `/home/ubuntu/Dev/hirejohn/node_modules/typescript/lib/tsc.js`; no installation occurred.

This is one direct standalone cleanup with an explicit authoring path. It does not prove installed discovery, the full Juan-mode pre-commit sequence, other providers, behavior-changing bug fixes, unavailable-main handling or cleanup in other languages. The mode caller change has full source-comparison evidence, not a live full-mode execution. Reading this helper does not activate Juan-mode.

[Validation](validation.json) records four packaging tests, both affected skill validators, manifest validation, Markdown lint, relative links and whitespace checks. No shipped scripts or model roles changed. Scratch evidence remains at `/tmp/jstack-deslop-20261016-v2`; the failed preparation remains at `/tmp/jstack-deslop-20261016`. Archived scripts retain their original absolute paths. No installed skills, model configuration or schedules changed.
