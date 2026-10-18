# Orchestrate release assessment

Orchestrate is the 23rd available Juan-mode procedure. This removes its draft-only routing block after the implementation pilot, current-head checks and bounded T3 service recovery. It does not activate Juan-mode in an authoring conversation or grant permission to run a program.

## Evidence against the original gates

| Gate | Observed evidence | Boundary |
| --- | --- | --- |
| Preserve the source procedure | Ten headings and seven ordered steps retained; [final source comparison](source-comparison.json) uses the exact manifest pins. | Existing T3 substitutions remain in the [adaptation record](../../adaptations/orchestrate.md). |
| Pilot through implementation, verification and landing | [PR #75](https://github.com/juancamiloqhz/skills/pull/75) landed after a real worktree implementation and a separately approved Claude Opus 5.5 verifier. | Research replay implementation, not a production application migration. |
| Verification remains tied to the current head | [PR #76](https://github.com/juancamiloqhz/skills/pull/76) exercised A/B keys and landed the reproducible check. The later continuation below rejected an actual historical A receipt for live B. | Coordinator classification; the CLI does not authenticate reviews. |
| Controlled restart and saved-state recovery | [PR #77](https://github.com/juancamiloqhz/skills/pull/77) records one approved service restart, recovery of the same batch, no repeated effect, and harmless repeated acknowledgement. | Service restart on one host; the probe wait failed and was accounted for. |
| Fresh continuation and late evidence | A new T3 task checked the checkpoint and original process loss, read live PR metadata and preserved both historical ledger keys. | Read-only continuation, not replacement implementation work or a surviving worker. |

The three-unit validation sequence has landed. The earlier reports retain their historical pending statements; the merged PRs and this assessment supply the later outcomes. A new program must still run its own pilot before scaling.

## Fresh continuation on 2026-10-18

The parent first queried the interrupted probe's task. Its later reporting turn was terminal with no pending children or question, and the original waiting process and provider were absent. It then dispatched a fresh `orchestrate-fresh-continuation-20261018-r1` task using the saved Codex `gpt-6.1-sol`/high selection. That task received the standing orders, saved checkpoint, original task/result references and a new exclusive output directory. It did not reuse the probe directory or resume the old task.

The child completed all five checks, with a distinct original run identity and no pending work:

1. Original probe and provider PIDs were absent, without PID reuse at observation.
2. Live GitHub metadata identified PR76's final head as `f7586c19bfeb5affb9f217d9831a6a9033dce4e0`. The intentionally replayed parent receipt for `27ecb31004211e53380035952ca0aae86eae3b7a` was classified stale for that final head.
3. Actual JSON ledger reads returned separate A and B `unit-test-verified` parent-check records. The old A receipt was not promoted into B's evidence; neither record was rewritten.
4. The restart batch remained acknowledged, its receipt hash matched, and its inbox remained empty.
5. Observed ledger, trial, model and repository file hashes were unchanged over the child's check. The parent inspected the result and recorded command outputs.

Both ledger lookups returned exit 0. The child inspected their JSON verdicts and evidence paths; exit 0 alone was not acceptance. The current-head reproduction remains in the [existing test](../orchestrate-current-head/README.md). Repeat the live check against owned PRs and saved receipts using `gh pr view <pr> --json state,headRefOid,mergeCommit` and `orch ledger check <pr> <sha> --json`; compare receipt identity before accepting it and preserve the ledger. Do not invent historical task evidence for a new run.

An initial read-only source search used a nonexistent `runtime/orch/ledger.ts` path and exited 2; the child corrected it to `store.ts`. The final checks passed. The parent changed the branch and prepared operational text while the child was running; the child explicitly reported those pre-existing edits and made none itself.

Raw reports, catalogs, process observations and hash inventories remain in task-owned cache. This report, the source comparison and bounded route cases are the retained release evidence. No cache is shipped, no installation was performed, and saved models and schedules remain unchanged. The previously consumed restart approval grants no further host action.

## Operational change and fidelity

Five operational files change. Juan-mode's availability text, setup's coverage sentence, the planning caller and the completion-contract introduction now recognize Orchestrate. The procedure removes its draft label and adds one Liveness sentence: T3 can start later reporting/recovery turns, so inspect pending runs and actual writers before reassigning a scope. The restart trial demonstrated this behavior. The route trigger, seven steps, pilot, verification bar and permission boundaries remain intact.

The comparison covers final files against each exact manifest source, with baseline deltas and necessary differences recorded. The completion reference is a local T3 contract with no one-to-one upstream file; only its obsolete availability wording changes. Existing history and pin records remain unchanged. This release adds no orchestration daemon, automatic result classifier or new model policy.

## Validation and remaining support limits

Four packaging tests and sixteen model-preflight tests passed. Pinned-source headings and step-label comparisons passed. Runtime code is unchanged; earlier runtime and replay suite results are not represented as new executions. The [route cases](cases.json) cover a standing program, a small single-session task and recovery with unresolved writer ownership. Review results are recorded after assessment.

This supports a coordinator-led, single-host workflow under the observed T3 capabilities. Required dependencies, supported forge topology, current authority and model diversity are checked per task. A missing prerequisite blocks its affected operation. No claim is made for unattended timers without authorization, uninterrupted worker survival, machine reboot or disk loss, replacement implementation writers, nested-writer recovery, arbitrary parallel ownership, or activation/opt-out persistence across all coordinating providers. Earlier unexplained worktree mutations remain unresolved and are not evidence of safe general concurrency.

The next project phase is the specification's full release verification: audit dependency closure and publish the provider/persistence support matrix. All 23 procedure files being available does not complete that phase.

## Example

Invoke `jstack-juan-mode`, then ask: "Own this multi-week API migration. Prove one endpoint through a tested PR first, wait for my approval before merging, then continue the remaining endpoints. Keep a checkpoint so we can pause and resume."

The coordinator uses Orchestrate, runs the pilot through the permitted lifecycle, and tracks the later units. A one-session task takes the smaller Autonomous run path. Reading this example does not start either workflow.
