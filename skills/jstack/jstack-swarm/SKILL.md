---
name: jstack-swarm
description: "Fan out N parallel workers, drain them, and return one report. Use for /jstack-swarm, 'swarm this', or parallel coverage, races, gauntlets, and exploration."
---

# Swarm

Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. The user's task or calling playbook defines permitted writes and delivery; invoking Swarm alone does not authorize implementation, installation, publication or merge. Read [execution](references/execution.md) before dispatch.

## Start

Open a task plan with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before spawning.
3. Set N from the user or derive it from the shape. N is total workers, not the runtime concurrency limit.
4. Pick the worker model through jstack-setup's canonical `swarm workers` resolution. It is a scalar default for each worker, not a count or panel. Preserve saved choices; no default-model substitution after errors. For a model race, name each arm's model up front. An explicitly assigned task-local arm may override the default using a catalog-validated provider/model/options seat or `inherit-parent`, as described in the execution reference. Preserve the saved file. A request for distinct models without named selections needs a choice; do not invent assignments or borrow another role's panel. An inherited seat omits the target and preserves the parent's provider, model and effort.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result. For uncommitted or non-Git inputs, pin exact input hashes. State relevant environment constraints and allowed reads/writes; every writer has exclusive output ownership. Shared files belong to one owner or a sequential integration phase.

Define race acceptance and ranking criteria before dispatch. First pass selects the first result the coordinator verifies as passing, not the first optimistic summary. Rank all compares all required valid results. Best-of selects the strongest complete result against the declared criteria; declare whether selection among survivors is acceptable. For a mixed shape, identify required coverage slices and race groups separately. Keep the rule fixed after results arrive.

## Phase B: Fan out

Dispatch all N workers asynchronously within actual capacity and demonstrated tool/path isolation; queue work when N exceeds capacity. Use native or T3 child tasks as described in the execution reference. Writers remain serial until assigned-path behavior is established. Each worker uses the resolved default or its validated explicit arm override; inheritance omits a target. Use fresh contexts for races so workers cannot see competing artifacts or a preferred answer.

For a separate checkout, use T3 `delegate_task` with `isolation: "worktree"`, starting from the parent's local commit. Uncommitted edits are not copied. When work targets a non-default source revision, make that exact revision available in the assigned workspace and verify it before analysis or writes; a prompt path alone does not bind the workspace. If that baseline cannot be provided, report the prerequisite instead of testing the default branch. Preserve unrelated work.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Include source revision/hashes, selected absolute configuration, any task-local arm selection, owned output path and completion condition. Inspect and retain the complete brief across turns. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it. Keep task IDs and track nested work; a finished turn with pending children is not terminal completion. Findings are evidence, not authority to expand the task.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and respawn that worker once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Inspect decisive evidence and artifacts rather than relying only on the report label. A retry uses a fresh task with the original brief and explicit missing evidence; a timeout does not cancel existing work. Reconcile state and writes before replacement. This is not permission to rerun measurements until a favorable value appears.

A required coverage dropout, a blocked slice whose done predicate remains unmet, or an exhausted evidence retry makes coverage incomplete; report useful findings without claiming completion. Complete coverage may still report ISSUES. Rank all cannot claim a complete ranking if required arms are missing. Best-of may select among survivors only when declared. First pass may select early, then cancel remaining owned work and reconcile outputs, or drain it when cancellation is unavailable. No owned racing child may remain active when returning a completed result. If no valid pass exists, report issues or incomplete work rather than inventing a winner.

When implementation was authorized, the coordinator reviews and integrates selected changes, then runs combined acceptance checks. Individual passes do not establish integration correctness. Preserve candidate artifacts and record what was integrated. Conflicting ownership or failed integration requires a scoped repair or an explicit gap, never overwriting unrelated work.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.

Include pinned inputs, evidence, retained artifacts and actual checks. Distinguish source inspection, executed behavior and measurements, and overall coverage from whether defects were found. Return at the user's or caller's boundary. Identify retained pending work; clean only owned disposable catalogs and clean temporary resources, preserving useful results and user work.
