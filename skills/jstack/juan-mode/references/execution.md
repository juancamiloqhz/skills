# Execution contract

Use the current tool schemas and injected T3 Code instructions. Prefer native same-provider children when they support the resolved model, options and required lifecycle. Use T3 Code `delegate_task` for cross-provider work, selections the native tool cannot express, or explicitly T3 Code-owned children. Catalog presence and preflight success are prerequisites, not proof a provider ran successfully.

## Child brief and lifecycle

Supply the following in every child brief because T3 Code delegation does not copy the parent conversation:

- Original goal, later constraints, relevant findings and selected procedure.
- For ordinary playbook children, the discovered absolute mode path with an explicit full-read requirement and applicable principle leaves; specialized workflow children keep their own briefs.
- Absolute checkout path, base revision, owned paths and read-only or write scope.
- The parent's selected absolute model-config path, passed explicitly to preflight in the child.
- Permitted commands or actions where the task needs a narrow boundary.
- Output location, observable acceptance checks and the evidence to return.
- Review findings and unresolved objections when this is a new review round.
- Stop condition and actions reserved for the parent.

For T3 Code dispatch, choose a distinct `clientRequestId` per logical round and reuse it only when retrying that dispatch. Retain the returned `taskId`; `childThreadId` is backing storage, not a target for continuing review. Every new task, follow-up, fix, retry or queue item uses a fresh child and consolidated brief by default. A non-review continuation requires named expensive live state that cannot reasonably move; a running child may receive stop/hold instructions without becoming a new work round. Each T3 review round always uses a fresh `delegate_task` with the consolidated brief. Use completion delivery and `task_status` when needed mid-task. A wait timeout does not cancel work, and a completed turn with pending child runs is not task completion.

Before replacing or abandoning a task, cancel its owned child work and reconcile any writes. Never give the same writable scope to a replacement while the original can still write. Inspect actual artifacts and verification output before accepting a child summary. Record task ID, effective selection, checkout, revision, permitted scope, outcome and evidence in the task's existing handoff when the work needs recovery.

## Workspaces

A child that needs a separate checkout uses T3 Code `delegate_task` with `isolation: "worktree"`, across any provider or model. It starts from the parent's local commit and completes project setup before the child runs; uncommitted edits are not copied. Ensure the intended base and required inputs are committed or provided as explicit read-only artifacts before dispatch. Do not simulate app binding by asking a child to create or change to a worktree in its prompt. Do not create a commit merely to dispatch if committing is outside the task's scope.

Retain the returned task identity and inspect the actual assigned checkout, branch, base revision, edits and verification before accepting the result. Keep shared plan files parent-owned and ports, logs and mutable build outputs separate. Separate checkouts do not by themselves prove every provider/editor's behavior. When a separate checkout is unnecessary, a shared checkout is valid for bounded reads or serial writes; concurrent writers require disjoint ownership and demonstrated tool behavior.

Parallel read-only work can proceed within its scope. Independent top-level conversations use `t3_thread_launch` only when the user requests them, with an explicit workspace strategy. Creating a top-level conversation is not a workaround for child isolation.

## PRs and verification

The parent links every worked PR with T3 Code. The parent also owns PR watches and wake handling; children return results instead of watching. Read existing comments before watching, dispatch fresh work for new findings, and stop watching when handing responsibility back to the user. Check readiness against the current PR head and forge state before any authorized merge.

Keep task delivery separate from mode activation. An implementation request does not itself authorize merging, publishing unrelated messages, installing skills or recurring schedules. Use already-granted authority without repeated confirmation. Preserve local user work and report incomplete verification accurately.
