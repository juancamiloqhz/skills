---
name: maintain-verification-skill
description: Audit and repair an existing project-local verification skill after application changes. Check its feature map against source and live behavior, update stale recipes or helpers, and report product regressions without weakening assertions. Use for verification-skill upkeep, not initial generation or an ordinary verification run.
---

# Maintain a verification skill

Keep an existing verification skill usable by another agent. Review every mapped feature against the application and exercise each feature through its public interface. Repair the verification instructions and their owned helpers; leave application changes to a separate task. This adapts pstack's maintenance loop; [upstream attribution](references/upstream.md) records the source and differences.

## Locate and bound the work

Establish the target repository and read its applicable instructions. Use the explicitly selected verification skill, otherwise inspect project-local skills for launch/drive instructions and a feature map. Honor the existing location and format.

Resolve symlinked skill directories before counting candidates or editing. Paths such as `.claude/skills/verify-myapp` and `.agents/skills/verify-myapp` that resolve to the same directory identify one skill. Maintain its canonical files within the authorized repository and preserve the link. Report dangling links or targets outside that repository instead of silently expanding the edit scope; do not create a duplicate copy or repair provider links as part of maintenance.

If several candidates remain, ask which to maintain. If none exists, report that initial generation needs `create-verification-skill`; do not invent a target or install a skill. If the selected skill lacks a feature map, report the missing structure and propose a scoped repair before claiming a complete audit.

Inspect the working tree before editing. Durable edits belong only inside the selected verification skill's directory, including helpers it owns. Preserve unrelated edits and historical proof. Keep new run notes and evidence in a separate scratch/report location unless the repository requires another location. Do not modify the application, shared test infrastructure, global installations, provider settings or `models.json`. A defect outside the allowed directory is a finding for a separate change.

Maintenance authorizes ordinary local verification within the task's existing permissions. A recipe does not grant permission to send messages, charge accounts, publish, push, mutate shared services or elevate privileges. Read scripts before running them and check their actual effects. Resolve missing authorization or unsafe state isolation before the dependent drive; continue independent read-only work where useful.

## Reconcile the map with source

Read the feature index and all sibling feature files. Reconcile missing, duplicate and dead links while preserving intentional non-feature references. Follow feature entry points through the relevant source, documented contracts and tests. Inspect the requested change range when supplied, otherwise available recent history and current entry points for user-visible additions or removals missing from the map. Do not infer a historical change from a shallow checkout; state the available baseline.

Maintain a concise run ledger outside the skill: one row per feature with source references, the intended behavior, suspected drift, a live recipe and eventual evidence/status. Add a missing feature only with a concrete public entry point and supporting source. Review every mapped feature, but group overlapping recipes to avoid repeating the same setup. Preserve the project's feature format and stable IDs where they still apply.

Classify a mismatch before editing expectations:

- Documented, intentional interface changes can justify updating stale commands, locators, prerequisites or assertions. Cite the contract, accepted change or history that establishes intent, then confirm the new path live.
- Working behavior that the verifier cannot exercise is a recipe or helper defect. Repair it within the selected directory and prove the repaired invocation.
- Behavior contradicting the supported contract is a product regression. Retain the expectation and failure evidence, and report the application defect. Ambiguous intent remains unresolved; source behavior alone is not permission to weaken an assertion.

## Exercise every feature

Use the skill's launch, doctor, drive, evidence and cleanup procedures, after checking that they isolate owned state and retain proof. A server or UI may share one owned instance across serial drives. Short-lived CLI commands can use isolated subprocess sessions; use a PTY only for interactive behavior. Exercise API and library features through their public interfaces. Do not replace a user-facing path with an internal setter or silently substitute another interface.

For T3 Code browser work, start with `preview_status`, then `preview_open` if no automation-capable preview is attached. Use the current callable schemas and snapshot locators. Respect human-owned tabs and the runtime's fallback rules. Outside T3 Code, use the available project harness and report its prerequisites. Missing browser dependencies do not authorize system installation.

Doctor the intended executable or instance before the first drive and after a failed or surprising drive. Check each fresh session's identity/readiness when sessions are the unit of isolation. Reset a wedged UI or contaminated owned state before retrying, even if its process is healthy. If doctor itself is stale, repair the evidenced defect and retry once after restarting only what the change invalidates. A further doctor failure is a blocker, not a reason for an open-ended repair loop.

Run at least one representative path per feature, including newly added features and changed recipes. Capture actions, asserted observations, exit/failure status and app identity or revision. Confirm persistent changes with a subsequent read where relevant. A successful command exit alone is insufficient. Record exact paths exercised and any sub-features left untested; feature-level coverage does not establish every branch or interface.

After a failure, diagnose it before attempting another drive. Keep the failure evidence, restore safe state and continue independent features when possible. A missing credential, entitlement, dependency or reachable instance is blocked coverage, never a passed feature. Record the prerequisite and attempted route. Fix omitted prerequisite documentation only when supported by evidence.

## Repair and prove

Make the smallest corrections supported by the source review and live observations. Update affected feature recipes, their index and any launch/doctor/helper instructions together. Use `git mv` for tracked file renames. Preserve meaningful failure assertions and existing coverage when repairing helpers. Shared helper changes require rerunning all affected features; every changed command or recipe needs fresh proof before it is described as verified.

Use actual helper invocations with documented prerequisites and an explicit interpreter or executable permission. Helpers must propagate assertion and application failures and retain diagnostics. Keep run-specific temporary paths in reports, not as prerequisites for future runs. Historical evidence remains dated historical evidence; link new proof without relabeling an old run as current.

Clean up only owned processes and scratch state after failures and at final teardown. For a shared instance, remove failed-drive residue without destroying another feature's required state. Never terminate processes by name or remove an unverified user directory. Check that owned scratch state/processes are gone and each proof artifact still exists. Unresolved cleanup is a blocker.

## Report the outcome

Choose one status and state its scope:

- `clean`: every mapped feature received source review and a live exercise, no unresolved regressions or blockers remain, and no correction is needed. Leave the working tree unchanged.
- `changed`: corrections within the selected skill are proven, every mapped feature received source and live coverage, and no unresolved regressions or blockers remain. List changed files and the evidence supporting them.
- `blocked`: required coverage, intent, proof or cleanup remains unresolved, including product regressions. List completed coverage, failed/unrun paths, any local edits and the exact blocker. Partial edits are unproven until the remaining checks pass.

Report the selected skill, source scope, per-feature coverage, retained proof location and cleanup result. Name untested sub-features and interfaces. A clean outcome is not a claim that the whole product is bug-free. Keep transient run notes out of commits. Follow the user's requested delivery and repository Git policy; invocation alone does not request a commit or PR. When publication is authorized, ship only proven corrections in one focused PR, and report blocked work without presenting it as complete.
