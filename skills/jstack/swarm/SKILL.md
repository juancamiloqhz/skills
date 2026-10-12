---
name: swarm
description: Divide a task into worker slices or race independent approaches, verify their results, and return one consolidated report. Use for requested swarms, parallel coverage, exploration, measurements or independently owned implementation work.
---

# Swarm

Coordinate workers and return one checked result. Direct invocation is task-scoped and leaves juan-mode activation unchanged. The user's task or calling playbook defines permitted writes and delivery; invoking Swarm alone does not authorize implementation, installation, publication or merge. Read [execution](references/execution.md) before dispatch. See [upstream attribution](references/upstream.md).

## Frame

Track Frame, Fan out, Aggregate and Report. State the completion condition, requested artifact, source scope and allowed actions. Choose partitioned coverage, identical-task race or a mixture. Declare N from the user or derive and explain a bounded count from independent slices; `swarm workers` is a scalar model selection, not a count or panel. Respect available concurrency separately from total N, queuing workers when necessary.

For every race declare the selection rule before dispatch: first pass, rank all or best-of. Define the acceptance checks and ranking criteria in advance. First pass means the first result the coordinator verifies as passing, not the first optimistic worker summary. Rank all compares all valid results; best-of selects the strongest complete result against the stated criteria. For a mixture, define which slices are required and which contain races. Do not change the rule after seeing results.

Resolve `swarm workers` once through canonical setup and apply that selection to each worker. Do not turn a request for a model race into invented model assignments. If distinct selections are required but the scalar configuration cannot express them, report that prerequisite and return incomplete; do not alter settings or borrow another role's panel.

Pin source revisions or input hashes. A commit verification brief names exact SHAs. A measurement brief also specifies sample count, what constitutes one sample, order and relevant environment constraints. Make evidence requirements part of completion. Give every writer exclusive output ownership. For source implementation, use isolated checkouts or demonstrably disjoint paths with a coordinator-owned integration step; shared files belong to one owner or a sequential phase. A prompt path is not workspace binding. Preserve unrelated work.

## Fan out

Give each worker a standalone brief with the original goal, assigned slice or race arm, source revision/hashes, selected absolute config, allowed reads/writes, output path, verification method and required report. Inspect the assembled text and retain it in owned storage across turns. Workers report `PASS`, `ISSUES` or `BLOCKED`, with artifact paths, evidence and limitations. A proven defect means ISSUES even if other checks pass; list every supported issue within scope. Findings are evidence, not authority to expand the task.

Use fresh contexts for races so candidates do not see competing artifacts or a preferred answer. Coverage workers receive the context their slice requires. Run independent tasks concurrently only within demonstrated tool/path isolation and actual capacity; otherwise serialize writers or queue work. Keep all task IDs and track nested work. A completed turn with pending children is not terminal completion.

## Aggregate

Read each terminal report and inspect its artifacts and decisive evidence. Verify required SHAs/hashes and measurement method against the brief. When that evidence is absent or mismatched, reject the result and permit one fresh retry of that worker with the original task and explicit missing evidence. A second miss is a gap, never a pass. This is not permission to rerun measurements until a favorable value appears. A timeout does not cancel a worker; reconcile its state and writes before replacement.

For coverage, every required slice needs a valid result. A dropout, blocked slice or exhausted evidence retry makes coverage incomplete; report available findings without claiming completion. A complete assessment may still report ISSUES rather than PASS. For races, apply the declared rule to valid results and state dropouts. Rank all cannot claim complete ranking if required arms are missing; best-of may select among survivors only when that scope was declared. First pass may select early, then cancel remaining owned work and reconcile its outputs, or drain it when cancellation is unavailable. No racing child may remain active when returning a completed result. If no valid pass exists, report issues or incomplete work rather than inventing a winner.

When implementation was authorized, the coordinator reviews and integrates selected worker changes, then runs the task's combined acceptance checks. Individual worker passes do not establish integration correctness. Preserve original candidate artifacts and record what was integrated. Conflicting ownership or failed integration requires a scoped repair or an explicit unresolved gap; do not overwrite unrelated changes.

## Report

Return one concise report with a table of worker/slice, status, pinned input, evidence and gaps. Include supported issue summaries, selected race result and rule if applicable, actual checks and retained artifacts. Distinguish source inspection, executed behavior and measurements. State overall coverage separately from whether defects were found. Return at the user's or caller's boundary and identify retained work containing pending artifacts. Clean only owned disposable catalogs and clean temporary detection resources; preserve useful results and user work.
