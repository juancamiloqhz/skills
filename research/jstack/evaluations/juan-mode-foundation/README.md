# Juan-mode foundation evaluation

Run on 2026-10-11 from the foundation branch based on `06e73c9982da136d066f8f3a8a0081946bdfecb9`. This is a focused functional evaluation, not a comparative benchmark or a full playbook release. [Results](results.json) record source hashes, task IDs, observed outcomes and limits.

## Executed checks

| Check | Observed result |
| --- | --- |
| Consumer CLI | Twelve tests pass with a copied setup dependency in a separate directory, including a path with spaces. |
| Canonical resolver | All six existing setup-jstack tests pass. Its model validation and resolution implementation is unchanged. |
| Installed dependency and live catalog | The preflight uses the catalog-advertised `/home/ubuntu/.agents/skills/setup-jstack` installation and the real saved configuration. `how explorer` resolves to `[null]` with effective `codex` / `gpt-6-astra`. |
| T3 Code inherited dispatch | An omitted target creates a Codex child with `gpt-6-astra`, `reasoningEffort: xhigh` and `serviceTier: default`, matching the parent's observed selection. |
| Assigned-checkout shell write | The child's default directory is `/home/ubuntu/Dev/skills`. Explicit command working directories and an absolute output path confine its write to the assigned fixture worktree. |
| Native Codex activation exercise | A fresh evaluator activates the skill, retains activation for a later planning task, and records opt-out. It discloses that selected playbooks are unavailable. This tests the native agent's retained context, not a distinct T3 Code conversation. |
| T3 Code conversation continuity | A separate T3 Code child returns activation states `true`, `true`, `false`, `false` across four turns in the same child conversation. |
| Review regression | The first review finds an overstrict cross-judge pool check. Two new regression cases fail before the fix and pass afterward. |

The CLI tests preserve the config file byte-for-byte, verify no installation writes, retain seat order and options, distinguish panels from judge alternatives, reload configuration between calls, reject stale settings in unrelated roles, and check inherited and cross-provider execution capability. Concrete and mixed-provider selections use fixtures; they are not live cross-provider execution evidence.

The workspace fixture contains a committed `value.txt` and a protected untracked sentinel in its base checkout. The child changes only the assigned worktree's `value.txt`. The parent verifies exact bytes, the assigned Git diff, unchanged base files, unchanged project Git status and unchanged saved configuration hash. After retaining the diff and task result, the parent restores its disposable fixture edit and removes the clean temporary worktree. The base fixture and raw local evidence remain under `/tmp/juan-foundation-20261011`; those temporary paths may expire.

## Conversation exercise

The first T3 Code dispatch explicitly invokes the source skill and requests activation only. Later turns use `t3_thread_send` because this evaluation requires the same conversation state. These are continuity probes, not independent review rounds. Each returned task ID is retained and its completed result is read with `task_status`.

1. Invoke juan-mode by its source path and ask for a handoff record. Result: active.
2. Ask whether requesting a plan authorizes implementation, without invoking the skill again. Result: a bounded answer and active state.
3. Turn juan-mode off and ask the difference between a JSON array and object. Result: an answer and inactive state.
4. Ask for `7 times 8` and the current handoff record, without mentioning the mode. Result: `56` and inactive state.

Every record names the actual child thread ID. The parent parses the returned JSON and verifies the state sequence and completed child lifecycle. This demonstrates retained activation state across these turns. It does not demonstrate automatic discovery, all routing decisions or persistence through compaction and restart. Requesting a handoff on every turn also makes state retention easier than an ordinary long conversation.

## Repeat the deterministic checks

From the repository root:

```sh
python3 -B -m unittest discover -s skills/jstack/juan-mode/scripts -p 'test_*.py' -v
python3 -B -m unittest discover -s skills/jstack/setup-jstack/scripts -p 'test_*.py' -v
npx --yes markdownlint-cli2 'skills/jstack/juan-mode/**/*.md'
```

For live preflight, obtain a fresh unwrapped `orchestrator_capabilities` payload in an owned temporary file and discover setup-jstack from the current skill catalog. Run the command in the [configuration reference](../../../../skills/jstack/juan-mode/references/configuration.md). A historical catalog snapshot is not a substitute for live capability discovery.

## Remaining evidence

- Genuine context compaction and provider process restart/resume. The exposed T3 Code tools inspected here do not provide a compaction test operation. No host settings or running services were changed to force it.
- Claude Code, Cursor and OpenCode as coordinating providers; live concrete or cross-provider dispatch.
- Editing tools beyond explicit-path shell execution, concurrent writers, cancellation during a write and recovery from provider failure.
- Different-family judge selection and minimum panel-size handling in actual shared procedures.
- All 23 playbook procedures, shared helpers and principles, merge continuation, and the full release support matrix.

The foundation group remains in progress until its persistence and provider requirements have evidence. No skill was installed, saved routing changed, schedule modified or PR merged by this evaluation.
