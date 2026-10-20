# Codex conversation compaction

On 2026-10-20, Juan-mode's inactive and active states each survived a real manual compaction in [Start an Investigation with Juan Help](t3-thread://v1/0fdfffb0-c122-496f-a9df-cd8a37238812). This extends the [fresh-conversation evaluation](../catalog-discovery/README.md#fresh-codex-conversation). It establishes two bounded Codex/T3 observations, not general persistence support.

## Environment and boundary

The existing top-level conversation used `codex / gpt-6.1-sol`, low reasoning effort and standard service tier. The source checkout was `1c4e36103f2cdcf63afd41760249d8ca5b076d52` on Orbit/Linux. All 59 tracked Juan-mode files and all four How files matched their installed copies. Setup's installed investigation reference matched `b3b8fba`, before PR #120; the other seven setup files matched current source. Temporary workflow files were permitted, so the revised strict-write branch was not exercised. No installation or model change was made to prepare the test.

The exposed T3 tools had no named compaction operation. Inspection of the served client confirmed that its Compact context control sends `/compact`. Sending that exact command through `t3_thread_send` produced completed provider compaction events. The two following prompts did not repeat the previous activation or opt-out. The coordinator inspected durable activity and returned findings, rather than accepting a status declaration alone.

## Observed sequence

Positions refer to the linked conversation. Run ordinals belong to that same thread.

| Run and positions | Observation |
| --- | --- |
| 5, 56–60 | After the user's earlier opt-out, a new task asked for the checker's exit codes. One source read, no playbook or child dispatch, correct answer and explicit inactive state. This closes the previously untested ordinary post-opt-out task. |
| 6, 61–63 | `/compact` produced provider event `01a15ab5-5c6a-7f91-98d0-dde0f65491ac`, completed as Context compacted at `19:07:22.495Z`. |
| 7, 64–68 | Asked for the distinction between missing and different packages. The agent read the source directly, answered correctly and remained inactive. No playbook, preflight or delegated task ran. |
| 8, 69–74 | Explicitly invoked `/jstack-juan-mode` for activation only. The agent read the installed entrypoint and activation reference, acknowledged active state and started no task. |
| 9, 75–77 | `/compact` produced provider event `01a15ab7-0f9a-7203-8f1b-e81d917b1051`, completed as Context compacted at `19:09:16.254Z`. |
| 10, 78–99 | Asked which installed files the checker compares and whether extras affect the result. The agent reloaded Juan-mode, read Investigation and How, created the playbook plan, ran fresh preflight and dispatched one configured explainer. The child completed before the final answer, which cited the source and reported active state. |
| 11, 100–102 | Explicit opt-out restored the conversation to its original inactive state. Acknowledgement only, with no new task. |

The active run's preflight selected `/home/ubuntu/.config/jstack/models.json` and resolved `how explainer` to `codex / gpt-6.1-sol`, high effort. The dispatch receipt confirmed that target plus inherited standard service tier. Its task ID is `node:delegated-task:command%3Amcp%3Acdad3ddd-5213-46d6-b301-19fdf2c39ccd%3Adelegate-task%3Ainstalled-files-explainer-20261020-1`. The returned report, completion notification and child thread's terminal state support actual execution; the child had no active run or pending requests when checked. The coordinator reread the decisive source lines before answering.

The inactive follow-up used only a source read. The active follow-up wrote one permitted temporary catalog, invoked the installed preflight and removed the catalog. Git status was clean after the runtime test. Hash checks spanning the follow-up sequence found no changes to the installed entrypoint, activation reference, shared investigation reference or saved model configuration. These are observed commands and selected-file checks, not a filesystem-wide audit. The browser session opened for UI inspection stopped at pairing and was closed; no host service or access setting changed.

## Repeat and interpret

Use an idle top-level conversation with the intended provider and an established activation history. Confirm the installed packages and preserve the user's configuration. Test opt-out followed by `/compact` and an ordinary source task, then explicit activation followed by another `/compact` and another ordinary task. Permit workflow temporary files, preserve source/install/configuration, and ask the agent to report its state and workflow. Require a completed compaction event before each task; a written summary or a new conversation does not establish this boundary. Inspect routing, dependency reads, preflight, actual child completion and cited findings. Restore the starting activation state afterward.

Both post-compaction tasks here also asked whether Juan-mode was active. That question did not set its state, but it made state reporting explicit and may make recall easier than an unprompted task. One compaction per state gives no reliability estimate. The exposed compaction events contained no summary text or token counts, so this assessment does not establish the exact retained JSON representation, how much context was removed or whether every skill instruction survived unchanged.

The active run demonstrates resumed routing, preflight and completed delegation. Its final answer claimed Unslop use without a fresh identity/load check in the observed turn, and the plan had no final completion update. Do not treat this as complete writing-phase or whole-playbook verification. Automatic compaction at a context limit, compaction with live children, provider-process restart, machine reboot, other models, Claude/Cursor/OpenCode coordinators and standalone hosts remain unverified by this test. The separate Claude export does not establish Claude compaction support.

## Fidelity and retention

No operational skill, resolver, model assignment, source pin or reviewed checkpoint changes. Direct inspection of `pstack/skills/poteto-mode/SKILL.md` at original pin `11713c683fe4add4fd403ea880580abbc9e0875f` confirms its Cursor mode/reminder metadata; How at the same pin requires one explainer on the simple path. The audit revision `0148b78c56c72a1b8412055913c79f767095b217` retains that child requirement. The existing [Juan-mode adaptation](../../adaptations/juan-mode.md) owns the user-approved T3 conversation-state and configuration differences. This report measures that adaptation without revising it or claiming Cursor equivalence.

Retain this concise assessment and its durable thread/event references. Served client bundles and selected-file hash evidence stay in task-owned cache; no transcript, catalog, generated page or app database is committed. Documentation checking and `git diff --check` validate this evidence-only change, not runtime behavior.
