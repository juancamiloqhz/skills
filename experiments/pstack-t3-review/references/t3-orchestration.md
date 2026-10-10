# T3 orchestration contract

Discover tools by their operation name; MCP prefixes can vary. Use the current callable schemas and injected T3 instructions for arguments.

| Need | T3 operation | Required handling |
| --- | --- | --- |
| Available seats | `orchestrator_capabilities` | Read provider instance IDs, model IDs, selectable options, constraints, and child-task support. Catalog presence is not proof a runtime will succeed. |
| Independent child | `delegate_task` | Supply the full brief. Parent conversation history is not copied. Set explicit target and options when selected by the user. |
| Collect result | `task_status` | Retain the returned `taskId`. Require terminal success, usable summary, and no unfinished nested work before judging. |
| Stop owned task | `task_cancel` | Cancel the tracked task when the user stops the panel or the task must be abandoned. |

Each seat and review round gets a distinct `clientRequestId`, stable across retries of that same request. Preserve `taskId`, returned model/provider, and backing thread ID. A lost response requires inspecting existing tasks before retrying; avoid duplicate paid work.

For asynchronous tasks, use completion notifications. Yield when no independent work remains; read status when a result is needed, rather than running a polling loop. A wait timeout is not task cancellation.

Start each subsequent review with a new `delegate_task`, including the original brief, previous results, responses, and unresolved objections. `childThreadId` is backing storage, not a continuation target. A completed task's original published result stays stable even if that thread later runs another turn.

Read-only here is an instruction boundary unless the provider exposes and applies stronger permissions. All children inherit the parent's workspace; this skill produces text in task results and does not relocate children. Writing candidates, worktree handoff, cloud workers, and top-level thread launches are outside this subset.

Children need only filesystem reads and their assigned reasoning. If a child cannot read a required file, it reports that missing grounding and stops. It does not need orchestration tools for the candidate or judge role.
