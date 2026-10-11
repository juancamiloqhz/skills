# Installed juan-mode runtime evaluation

Evaluated on 2026-10-11 after the user installed the skills from `c9c64ce474369db3efa607cf28c9cd80877bf842` and selected global inherited routing. This extends the historical [foundation evaluation](../juan-mode-foundation/README.md) and [project configuration evaluation](../project-model-config/README.md). [Results](results.json) retain source hashes, child task IDs, host observations and checked artifacts.

## Observed support

| Check | Result and scope |
| --- | --- |
| Installed source | All 17 tracked files in setup-jstack and juan-mode match the evaluated commit before this change. |
| Installed preflight | `how explorer`, `feature, refactoring`, `architect runners` and `arena cross-judge pool` resolve the global file and return `[null]`. This exercises scalar, panel and pool selection without dispatching a panel. |
| Inherited T3 child | Omitting the target creates a Codex child using `gpt-6-astra`, medium reasoning effort and standard service tier, matching the parent. The saved medium budget does not override inherited effort to high. |
| Editor isolation | The child's default directory is the skills repository. An absolute `tools.apply_patch` path edits only the assigned fixture worktree. The parent verifies exact bytes, the diff and protected files. |
| Child workspace binding | T3 reports no child worktree binding. Successful explicit-path editing does not establish app-level binding or support for other editors. |
| Activation decision cases | Six independent synthetic histories produce the expected active, inactive or unknown decisions. These are interpretation checks, not persistence tests. |
| Actual compaction and restart | Unverified. The callable T3 tool inventory exposes no operation to compact a conversation or restart its provider process. |
| Other coordinating providers and cross-provider dispatch | Unverified. Both probes inherit the user's current Codex selection. |

Both child tasks completed with no pending child runs. The parent independently reads host configuration and timeline metadata, verifies files and config hashes, restores the disposable fixture edit and removes the clean temporary worktree. No saved model assignments or installed skills were changed by this evaluation.

## Activation cases

Each case is evaluated independently against the installed skill and its activation reference. `CURRENT_THREAD` is replaced with the evaluator's actual T3 thread ID. The evaluator receives the histories, not the expected decisions.

| Case | History and latest request | Observed state |
| --- | --- | --- |
| A | Same-thread active handoff, then a casual arithmetic question. | Active. |
| B | Same-thread active handoff, then explicit opt-out. | Inactive. |
| C | Another thread's active record, in a new conversation without invocation. | Inactive. |
| D | Same-thread inactive handoff, then explicit invocation. | Active. |
| E | Resumed conversation without activation history, then a request to continue. | Unknown; disclose missing history. |
| F | New conversation asks to review and explain juan-mode. | Inactive; authoring is not invocation. |

No case starts a playbook. Active cases reload the installed entrypoint when its instructions are missing from context. The actual evaluation conversation remains inactive. Supplied histories cannot prove that a host preserves those histories across compaction or restart.

## Catalog capture correction

The editor probe initially tried to embed the full capabilities payload in a shell command. Its report records `Argument list too long (os error 7)` before execution. It recovered by writing bounded chunks, parsed the resulting JSON and completed preflight. The parent also captures the full payload through `tools.apply_patch`, checks JSON equality against the original payload and validates the saved configuration with that file.

The shared [T3 Code integration reference](../../../../skills/jstack/setup-jstack/references/t3-code.md) now explains file-tool or streamed capture and bounded chunks when only command strings are available. Setup and juan-mode point to that guidance when capturing capabilities. Model lookup and validation code are unchanged.

## Repeating the checks

Obtain a fresh capabilities payload through T3 Code and save it to an owned temporary file using the shared capture guidance. Read the current thread configuration separately to retain the actual inherited effort and service tier. Use the installed skill paths discovered from the current catalog:

```sh
python3 /installed/juan-mode/scripts/preflight.py \
  --setup-skill /installed/setup-jstack \
  --project-root /path/to/project \
  --catalog /owned/temp/catalog.json \
  --role 'feature, refactoring'
```

For editor isolation, prepare a disposable Git repository containing `value.txt` and `preserve.txt`, plus an untracked sentinel in its base checkout. Add a linked worktree and delegate one absolute-path edit with the returned config path pinned explicitly. Retain the actual task ID, tool event and diff; verify the original checkout, sentinel and saved configuration before removing the clean worktree. Keep writers serial until the relevant provider and editing tool have this evidence.

Raw local evidence remains under `/tmp/juan-runtime.GO18U60v` and may expire. Temporary capability catalogs and the assigned worktree were removed after verification. The committed results retain the relevant evidence without a permanent model catalog.

## Remaining foundation gates

The foundation remains in progress. A real host-compaction test must show activation and a later opt-out surviving the actual boundary. A restart test must resume the same provider session and reconcile the current thread state. Claude Code, Cursor and OpenCode still need coordinating-provider evidence; catalog presence is not execution proof. Concurrent editing, cancellation recovery, other editors and full playbook execution also remain unverified.
