# Coordinated Autopilot update

Date: 2026-10-19. Local base: `14dac6ed370190910651ff8f25c644de85888539`, merged PR [#96](https://github.com/juancamiloqhz/skills/pull/96). Source: `cursor/plugins`, `pstack/skills/poteto-mode/playbooks/{autopilot-full,autopilot-stack,multi-phase-plan}.md`, compared from `11713c683fe4add4fd403ea880580abbc9e0875f` to `0148b78c56c72a1b8412055913c79f767095b217`.

## Change and fidelity

Full retains the current seven source steps. A full swarm checks finished code and later major changes; a single independent verifier checks rebases and minor fixes. Every new head still needs its own assessment and green CI. Root-owned recovery records and last-owned-push leases support replacement owners. Trunk-only defects are recorded separately from defects a PR copies or newly exposes. Merge preparation now distinguishes harmless drift, overlapping files, changed callers, dependency resolution and changed CI selection, with a hold before a third additional rebase.

Stack preserves the current four source overrides over Full. Owners start dependent work on the parent branch; only the root changes stack topology. Landing freezes the chain except Shipping's immediate-child operation. Both Autopilots call the full Ketchup/Bro helpers for operator updates.

The plan adopts the source's verification cadence while retaining its complete skeleton, ten full-swarm live lanes, performance and review gates. Necessary caller corrections resolve conflicting owner-rebase instructions, stale-head evidence wording, waiting-question recovery and recap instructions that suppressed older decisions. The plan now names STACK-READY for Stack review handoffs.

The full final files were compared with the frozen source objects. The [Full](../../adaptations/autopilot-full.md), [Stack](../../adaptations/autopilot-stack.md) and [plan](../../adaptations/multi-phase-plan.md) records account for all differences. Existing T3 worktrees, configured model/effort, root-owned links/watches, explicit schedule authority, canonical package discovery and confirmed cancellation replace incompatible Cursor assumptions. Full's private-stack exception, per-head full swarms, fixed 15-minute opening detail and repeated old audit/retro recipes are removed with upstream. Plan's new source-selected effort/speed sentence is not adopted because saved model policy governs jstack.

The manifest adds Ketchup/Bro context paths and records PR #96's verified merge for its existing decision. It preserves that decision's ID/range, mode's original adaptation pin and the shared reviewed checkpoint. This is a bounded implementation of the earlier coverage audit, not a new complete upstream review.

## Executed behavior checks

Run from the repository root with Python 3, Git supporting `merge-tree --write-tree`, and Node:

```sh
python3 -B research/jstack/evaluations/autopilot-update/check_merge_result.py
python3 -B research/jstack/evaluations/shipping-sequence/check_git.py
python3 -B research/jstack/evaluations/multi-phase-plan/exercise.py
python3 -B scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
```

| Check | Observed result |
| --- | --- |
| Actual Git merge results | A feature and a disjoint caller change each pass separately, but their conflict-free merge raises `TypeError`. A compatible caller and unrelated documentation pass. The fixture materializes a CI-file change and rejects a source conflict while preserving the original clean checkout and feature ref. This demonstrates why a clean merge alone cannot establish behavioral compatibility. |
| Existing Shipping fixture | All four groups pass, including three squash layers, own-patch extraction, an incorrect base changing patch identity, rejected empty patches and a stale lease that preserves a competing ref. |
| Current plan template | One- and two-PR plans, a no-review-gate case, 16 rejection cases and usage-error behavior pass. Generic unresolved placeholders still pass the source checker, so semantic review remains required. |
| Packaging and docs | Four packaging tests pass. Current-document check reports 47 skills, 23 playbooks and no problems; guide coverage remains pending. Juan-mode passes the Codex authoring validator. Manifest validation, applied-merge ancestry, changed-document relative links and whitespace checks pass. |

The Git fixture does not execute a forge CI pipeline or prove CI selection correctness. It does not run a frozen package install or verify package resolutions. Those lockfile decisions are tested only as instructions below. All fixture repositories are disposable and removed automatically.

## Independent authoring exercises

Two native Codex `gpt-6-astra`/high evaluators inherited the authoring conversation's model. No configured production role was invoked or changed, and juan-mode was not activated. They read the full Full, Stack, plan and Shipping procedures without source diffs or expected answers. Evaluators could write only their cache reports and were forbidden to execute programs, dispatch owners, publish, merge, schedule or change configuration.

[Cases](cases.json) retain the requests and expectations. For replay, give one evaluator the six decision requests without their expectations and the four procedure paths. Supply repository paths for the complete Ketchup and Bro helpers for the recap. Give another evaluator only the plan case. Keep outputs outside the checkout and inspect actual decisions and prose, not a self-reported pass label.

| Exercise | Observed result |
| --- | --- |
| Verification | Distinguished full and single verification, retained historical receipt identities, required fresh CI, blocked missing live proof and separated trunk-only from newly exposed defects. |
| Drift | Required merge-result checks for changed callers, full frozen-install/resolution proof for the lockfile exception, rebases for normal overlap or changed CI selection, and the third-additional-rebase hold. |
| Recovery | Refused an unexpected remote push as a new lease, preserved waiting questions, reconciled missing records and required stopped writers or isolated replacements. General go did not become schedule authority. |
| Stack | Assigned dependent bases and topology to the root, quiesced writers, froze landing, reconciled an in-flight pass before repair and preserved operator-owned landing. |
| Gates | Required proof and countersign for weaker budgets/allowlists, removed soft-failure bypasses, and preserved forge approval requirements, named holds and queue scope. |
| Actual recap reply | Read full Ketchup/Bro, corrected earlier readiness, linked the fictional merged Search and failing Export PRs, retained the older retention choice and kept the export fix as agent work. No live reads or actions were claimed. |
| Plan excerpts | Produced Program checklist and Merge excerpts for dependent A/B, selected Stack, retained planning-only authority and marked absent commands, performance evidence and runtime proof unproven. It did not produce or validate a complete execution plan. |

The plan evaluator wrote its complete report before a terminal model-capacity error. The parent recovered and inspected that artifact rather than counting the errored turn as a successful runtime. Both reviewers identified ambiguous Stack source-refresh wording; the plan reviewer also identified generic merge-ready wording. The final edits explicitly name the canonical jstack source and route-specific readiness. The focused reread used the corrected source location and STACK-READY handoff, and retained planning-only scope. It is not a fresh blind replay of all cases.

Other observations need no behavioral redesign: the skeleton's dependency placeholders must be filled for the chosen graph; conditional schedule registration does not authorize a timer; Stack overrides the template's Full landing alternative. Autopilot's required clean lanes and Shipping's later PASS+NOTES handling are distinct gates. The parent reviewed these interpretations against the complete procedures.

## Limits and retention

These checks establish local Git behavior, document structure and bounded instruction decisions. They do not establish a live multi-owner Autopilot run, concurrent root/owner writes, cancellation, lost-worktree recovery, hourly wakes, restart persistence, installed-provider helper discovery or cross-provider behavior. Existing release checks remain open. No skill was installed, saved model selection changed or production program started.

Retain this report, replayable cases and the small merge-result reproducer. Reuse existing Shipping and plan fixtures. Raw evaluator replies, copied source files, diffs and command transcripts stay in task cache and can be removed after acceptance when no unresolved work depends on them.

## Normal use

After merge and manual installation, activate `jstack-juan-mode` and ask: "Prepare the import parser and its dependent batch command as a stack for my review." Stack gives each PR an owner, keeps rebases with the coordinator and stops at STACK-READY. Finished code gets the full verification; a small later fix gets an independent verifier and fresh CI. A separate merge request is still needed.
