# Pstack T3 review evaluation

Date: 2026-10-06. Status: completed. The manually coordinated read-only candidate/judge flow succeeded; full pstack compatibility remains untested.

The skill is authored in this repository and read explicitly by absolute path. It is not installed. Upstream Arena is pinned in the skill's provenance reference, with its MIT notice retained.

## Experiment

Two independent candidates receive the same self-contained PostgreSQL background-job queue design problem. Required behavior includes concurrent claims, crash recovery, deduplicated enqueue, stable external idempotency keys, and fencing expired workers. The problem uses no private project data. Children are instructed to read only the skill and orchestration reference and return text, without files, workspace changes, or nested work.

- Candidate A: `codex`, `gpt-6-astra`, `reasoningEffort=medium`.
- Candidate B: `claudeAgent`, `claude-opus-5-5`, `effort=medium`.
- Judge: fresh Opus 5.5 context after both candidate results are available, with anonymized candidate labels and the task-specific rubric.

Check model/provider receipts, distinct child contexts, grounding acknowledgements, terminal task results, judge access to both complete answers, parent selection and synthesis, and requirement/failure-scenario verification.

## Checks completed

- Live T3 catalog advertises both requested models and cross-provider child tasks.
- T3 accepted both delegations and returned distinct task IDs, child threads, and the requested model/provider pairs.
- Both candidate task results are terminal successes with no pending child runs. Both explicitly acknowledge reading the skill and orchestration reference and report no mutations or nested work.
- A fresh Opus judge was dispatched with the complete original task, rubric, and both answers labelled A and B. Candidate model identities were omitted from its brief.
- The judge completed successfully in a third distinct child thread, acknowledged both files, and returned criterion scores and a reasoned selection. No participant reported unfinished nested work.
- [Receipts and complete candidate results](./pstack-t3-review-receipts.json) preserve task IDs, provider/model values, and results. Reasoning options were explicitly requested in dispatch; these receipts do not independently confirm effective provider reasoning settings.
- Skill frontmatter validation passed.
- Local Markdown references resolve and `git diff --check` passed.

## Parent assessment and synthesis

The judge scored A 10/10 and B 9/10 but selected B for its concrete schema and transitions. I agree with the base selection after reading both complete answers. Scores are subjective, not an implementation test. B's retry-limit defect must be corrected; its extra schema and SQL detail does not excuse that gap.

B allows a late completion if its fencing epoch still matches. A requires a live lease. The supplied requirement forbids an expired worker overwriting a newer owner's state, so B's less restrictive rule is acceptable if completion and reclaim serialize on the row and every transition checks the epoch. Either completion commits first and removes eligibility, or reclaim increments the epoch first and rejects the old completion. This is a design argument, not an executed concurrency test.

The judge's heartbeat observation needs qualification. Renewing after expiry is coherent only if renewal is a serialized ownership transition with current-time handling and epoch validation. The synthesis instead uses live-lease-only heartbeat renewal, while accepting fenced late completion. Those rules have different purposes and need not be identical. No finite API latency assumption is used as a correctness guarantee.

Selected base: B. Incorporated from A: durable deduplication retention, post-conflict reading of the winning enqueue, current database time after locking, explicit distinction between a live database owner and an executing process, and reconciliation after API idempotency retention lapses. Added correction: terminal handling for exhausted retries, including already queued exhausted rows. Rejected: unconditional external effectively-once claims and a live-lease requirement for completion where no newer claim exists. See [the synthesized artifact](./pstack-t3-review-synthesis.md).

## Requirement and scenario verification

| Requirement or scenario | Synthesis handling | Verification |
| --- | --- | --- |
| Two simultaneous claims | Row lock, skip locked selection, eligibility recheck, epoch increment | Inspected transition ordering; not run against PostgreSQL |
| Crash before external effect | Lease expiry permits reclaim with a new epoch | Walked recovery timeline |
| Crash after effect | Persisted key and identical request replay; conditional API deduplication | Walked recovery and retention-expiry alternatives |
| Duplicate enqueue | Unique logical key, retained row/tombstone, payload conflict check | Inspected concurrent winner/read path |
| Old completion races new claim | Epoch-conditioned transition serialized on row | Walked both commit orderings |
| Final retry fails | Move to dead; sweep exhausted queued and expired running rows | Corrected B's stranded queued-job defect |
| Provider identities and grounding | Three distinct T3 task/thread receipts and path acknowledgements | Receipts plus participant self-reports |

## Observed limitations and next evaluation

B exceeded the requested answer length. The judge also exceeded its budget. Output length is not reliably enforced by this skill. The synthesis is shorter; the full original responses remain in the receipts. No workflow change is justified by a verbosity miss alone.

The parent supplied the skill paths explicitly and coordinated every dispatch. This demonstrates cross-provider execution of the adapted phases, not autonomous discovery or a different parent correctly orchestrating from the skill alone. The next focused evaluation should give a fresh parent the skill and problem, then inspect whether it independently follows the candidate/judge lifecycle. Installation and writing/worktree experiments remain separate steps.

## Limits

Read-only behavior is prompted, not a demonstrated operating-system permission boundary. This evaluation does not exercise automatic discovery, provider installation, full poteto-mode, writing candidates, worktree isolation, nested delegation, cancellation, or autonomous use of the skill by a different parent agent. A design answer is not a tested queue implementation.
