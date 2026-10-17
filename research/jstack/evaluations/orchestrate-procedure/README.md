# Orchestrate procedure evaluation

The [draft procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/orchestrate.md) connects the existing state helper, GitHub frontier and completion contract to pstack's full coordinator procedure. It preserves all ten headings and seven ordered steps at pin `11713c683fe4add4fd403ea880580abbc9e0875f`. The [adaptation record](../../adaptations/orchestrate.md) explains each substitution; [source hashes](source-comparison.json) identify the exact comparison.

Orchestrate remains unavailable as a route. Twenty-two playbooks are enabled. This PR supplies a reviewable draft and bounded evidence, not a completed program pilot or proof of restart durability.

## Results

On 2026-10-17, five actual T3-owned Codex children inherited the executing conversation's model and effort without overrides. The parent was gpt-6-astra at high effort. One read-only source-inspection child completed before two paired planning rounds began. Each pair used separate children, one with the draft and one without a jstack procedure. Each child answered both [case prompts](cases.json) sequentially. Assertions were added to the retained cases after execution and were not supplied in the initial prompts.

| Final case | With draft | Without draft | Assessment |
| --- | --- | --- | --- |
| Frame and pilot | 6/6 | 4/6 | The draft response explicitly requires landing before scaling and a rolling worker window. The baseline acknowledges incomplete landing but does not make landing an unambiguous prerequisite to scale, and does not specify a rolling refill. |
| Recover after interruption | 6/6 | 6/6 | Both preserve pause, duplicate handling, stale-head boundaries, unresolved child ownership, stale frontier evidence and durable continuation records. |

The parent graded the actual saved reports against those assertions. These scores measure conformance to the specified coordinator procedure, not general planning quality or demonstrated runtime safety. One final run per condition, shared context across its two cases, and explicit constraints in the prompts limit generalization. No statistical, speed, cost or token-efficiency claim is made. Unavailable timing and token measurements are omitted. Results are delivered briefly in chat, following the user's preference after the prior HTML viewer.

The first draft imported Shipping's stricter per-PR verification into Orchestrate. Its assisted response propagated that addition, contradicting the upstream cheap-unit path. The final draft removes that import and clarifies that only Autopilot-stack's topology mechanics apply. A fresh pair tested the corrected version. The final assisted response retains cheap worker checks with receipt spot-checks and different-family dedicated verification for novel units. An additional wording correction accounts for T3 children being able to ask questions.

## Actual child delivery and local recovery

The parent queried `task_status` for all five children. Each returned its original task/run identity, `completed`, `result_available`, no pending child work or question, and a result reference. Report files were inspected. The source child independently computed the pinned source hash, which the parent compared with `git show` from the cached upstream repository. No configured workflow role was invoked; authoring evaluations do not activate juan-mode.

The [replay exercise](replay.py) used observed identities and real report paths from the first three completed tasks. It initialized an actual CLI store, enqueued their three results plus a duplicate, claimed four pointers and exited before applying decisions. A second process recovered the same batch, recorded three `assessed` units, classified one duplicate, rendered status, saved the receipt and acknowledged it. Repeated acknowledgement returned the same record and receipt hash. The inbox was empty afterward. No ledger verdict or PR completion was invented for these prose tasks.

An initial exercise version used nonexistent `inbox peek`; it failed after acknowledgement. The corrected read is `inbox drain --peek`. Both phases then passed in a fresh store. This was a reproducer error, not a runtime code change. An intermediate authoring replacement assertion also failed before writing the draft and was corrected. No failed run is counted as a pass.

These are live child completions plus local process-boundary recovery. They do not simulate a successful host restart, cancellation, nested child shutdown, replacement writer, implementation PR, independent live verifier, forge landing or frontier refresh. The CLI exercise receives saved observations; it cannot authenticate them or query T3 itself. The parent checked their live source separately. All child tasks ended, and only distinct scratch report paths were writable. No watches, timers, installs or model changes ran.

## Reproduce and retain

For the planning comparison, give fresh inherited-model children the case prompts without assertions. Supply the draft and needed references only to the assisted child. Allow only separate report outputs, prohibit program execution and compare the reports against the assertions afterward. Do not use task IDs or reports from unrelated conversations.

For the local recovery exercise, collect three completed owned tasks through live `task_status`. Save their JSON records as an array, adding a distinct `unit` and actual `reportPath` to each. Inspect each report before marking it assessed. With Bun and the existing declared tool dependencies available:

```bash
python3 -B research/jstack/evaluations/orchestrate-procedure/replay.py /tmp/orch-replay /tmp/observations.json --cli /absolute/path/to/orch.ts --phase claim
python3 -B research/jstack/evaluations/orchestrate-procedure/replay.py /tmp/orch-replay /tmp/observations.json --cli /absolute/path/to/orch.ts --phase resume
```

The first phase refuses an existing destination. The second uses the same observations and store after the first process exits. Runtime commands ran from an exact source copy with already-present Commander dependencies; nothing was installed. The retained script is an exercise, not a generic idempotent coordinator or automatic result classifier.

The four packaging and sixteen preflight tests passed. Changed-document lint with MD013/MD041 disabled and MD040 disabled for the preserved upstream brief fence, relative links, exact source hashes, preserved headings/step labels and diff checks passed. Runtime code is unchanged, so earlier runtime-suite evidence is not represented as a new run. Source pins, reviewed checkpoint, license, lockfile and saved model configuration are unchanged.

Retain only this report, cases, the replay script and source comparison in Git. Raw status observations, reports, receipts and generated stores stay in task scratch while needed for review. Do not commit them or delete shared caches as routine cleanup.

## Intended use and next gate

For a large API migration, the intended request is:

> Plan the migration in three tracks. Prove one endpoint through implementation, verification and approved landing before starting the wider rollout. Keep a record so we can pause and resume.

The draft tells the coordinator how to assign work, verify results, process completions and recover recorded state. It remains an authoring draft; use it for review or a separately scoped validation exercise, not a claim that the route is released.

Next, run an explicitly scoped three-unit implementation dependency graph with a real pilot through authorized landing, current-head invalidation, and a controlled host-restart/continuation trial. Capture every task, writer and result after recovery, including an intentionally stale result. Enable the router only after those gates pass. A generic go does not authorize restarting the user's host, changing model selections, or merging evaluation PRs.
