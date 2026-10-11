# Execution contract

Use the current tool schemas and injected T3 Code instructions. Prefer native same-provider children when they support the resolved model, options and required lifecycle. Use T3 Code `delegate_task` for cross-provider work, selections the native tool cannot express, or explicitly T3 Code-owned children. Catalog presence and preflight success are prerequisites, not proof a provider ran successfully.

## Child brief and lifecycle

Supply the following in every child brief because T3 Code delegation does not copy the parent conversation:

- Original goal, later constraints, relevant findings and selected procedure.
- Absolute checkout path, base revision, owned paths and read-only or write scope.
- The parent's selected absolute model-config path, passed explicitly to preflight in the child.
- Permitted commands or actions where the task needs a narrow boundary.
- Output location, observable acceptance checks and the evidence to return.
- Review findings and unresolved objections when this is a new review round.
- Stop condition and actions reserved for the parent.

For T3 Code dispatch, choose a distinct `clientRequestId` per logical round and reuse it only when retrying that dispatch. Retain the returned `taskId`; `childThreadId` is backing storage, not a target for continuing review. Each new review round uses a fresh `delegate_task` with the consolidated brief. Use completion delivery and `task_status` when needed mid-task. A wait timeout does not cancel work, and a completed turn with pending child runs is not task completion.

Before replacing or abandoning a task, cancel its owned child work and reconcile any writes. Never give the same writable scope to a replacement while the original can still write. Inspect actual artifacts and verification output before accepting a child summary. Record task ID, effective selection, checkout, revision, permitted scope, outcome and evidence in the task's existing handoff when the work needs recovery.

## Workspaces

T3 Code's current `delegate_task` has no workspace-binding parameter. A path in a prompt does not move the child's app binding. Start writers serially until the chosen provider and tool combination has demonstrated that commands and edits affect the assigned checkout. A successful shell `workdir` check does not prove every editor or Git integration follows it.

For an explicit-path writer, have the parent prepare an owned checkout and give the child its absolute path. Before mutation, the child reports its default directory, assigned Git root and branch. Use explicit command working directories and absolute edit paths. Verify the result in the assigned checkout and check that the original checkout is unchanged before accepting it. Keep shared plan files parent-owned. Confine logs, ports and generated artifacts to owned resources as needed.

Parallel read-only work can proceed within its scope. Independent top-level conversations use `t3_thread_launch` only when the user requests them, with an explicit workspace strategy. Creating a top-level conversation is not a workaround for child isolation.

## PRs and verification

The parent links every worked PR with T3 Code. The parent also owns PR watches and wake handling; children return results instead of watching. Read existing comments before watching, dispatch fresh work for new findings, and stop watching when handing responsibility back to the user. Check readiness against the current PR head and forge state before any authorized merge.

Keep task delivery separate from mode activation. An implementation request does not itself authorize merging, publishing unrelated messages, installing skills or recurring schedules. Use already-granted authority without repeated confirmation. Preserve local user work and report incomplete verification accurately.
