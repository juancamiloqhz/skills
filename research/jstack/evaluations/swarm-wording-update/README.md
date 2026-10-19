# Swarm upstream wording update

The [coverage audit](../../coverage-audits/2026-10-18/README.md) identified shorter upstream Swarm wording and an omitted worker-count step. This update removes two redundant paragraphs while preserving the count needed by later phases.

## Complete source assessment

Local base is merged PR #90, `d9b50794fa6cc2c79dd88a410ed7f7824fad81da`. Upstream's only package file, `pstack/skills/swarm/SKILL.md`, was compared from original pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/swarm/SKILL.md).

All changes in that range are accounted for:

- Adopt deletion of the introductory summary. Partition/race/mixed shapes, aggregation and the report are still specified by the phases.
- Adopt deletion of the repeated result-table sentence in Aggregate. Report still explicitly requires the table, evidenced issue summaries and gaps/dropouts.
- Keep the existing N-selection step as a necessary clarification. Upstream still dispatches all N workers and discusses N-1 dropouts, without its former step defining N. Jstack declares the total from the user or chosen shape and keeps it distinct from actual simultaneous capacity. This preserves the existing algorithm and makes required coverage reviewable.
- Keep selected model options unchanged. Upstream's new adaptive effort/speed instruction remains deferred under the existing model policy.

The full final comparison leaves only the [documented runtime/authority adaptations](../../adaptations/swarm.md), plus that now-explicit count difference. Naming, invocation metadata, task planning, canonical model resolution, isolated ownership, pinned inputs, lifecycle checks, race acceptance and reporting remain intact. The local execution reference has no source counterpart and is unchanged. Package license bytes match upstream. Original pins and the reviewed checkpoint remain unchanged.

## Verification and limits

The parent read the full upstream/local diff and checked that reversing exactly the two paragraph deletions reproduces the prior local entrypoint byte for byte. The execution reference, canonical resolver and manifest are unchanged. Four packaging tests, skill validation, documentation consistency and diff checks pass.

The retained instructions still define N before dispatch, omit targets for inherited workers, require a declared race rule, allow one retry for missing required evidence and report incomplete required coverage after a dropout or exhausted retry. The [historical runtime exercise and continuation assessment](../swarm-restoration/README.md) remain evidence for their original files. They are not relabeled as new runs.

No new subagents or live Swarm execution were used for this wording-only update. Source comparison and static checks do not establish installed-provider behavior, live cancellation, concrete-model dispatch or dropout recovery. There is no new runtime-success claim and no new fixture, log or generated output to retain.

## Normal use

After merge and a manual skill update, ask `jstack-swarm`: "Use three workers to review authentication, billing and exports; report findings only." It declares three required slices, runs within available capacity and returns one report. If the billing worker cannot finish, its gap stays visible and the review is incomplete. This usage is unchanged by the wording cleanup.
