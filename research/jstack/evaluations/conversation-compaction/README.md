# Codex and Claude conversation compaction

On 2026-10-20, Juan-mode's inactive and active states each survived a real manual compaction in [Start an Investigation with Juan Help](t3-thread://v1/0fdfffb0-c122-496f-a9df-cd8a37238812). This extends the [fresh-conversation evaluation](../catalog-discovery/README.md#fresh-codex-conversation). It establishes two bounded Codex/T3 observations, not general persistence support.

The [Claude follow-up](#claude-export-follow-up) records the same state choices across two user-triggered compactions in another T3 environment. Its inactive answer has no fresh source-read evidence. The state-retention observations do not certify complete task execution.

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

The active Codex run demonstrates resumed routing, preflight and completed delegation. Its final answer claimed Unslop use without a fresh identity/load check in the observed turn, and the plan had no final completion update. Do not treat this as complete writing-phase or whole-playbook verification. Automatic compaction at a context limit, compaction with live children, provider-process restart, machine reboot, other models, Cursor/OpenCode coordinators and standalone hosts remain unverified by these tests. The Claude follow-up below adds its own bounded manual-compaction evidence.

## Claude export follow-up

The user supplied the same Claude conversation at two later snapshots, `2026-10-20T19:38:26.370Z` and `2026-10-20T19:44:38.647Z`. Both identify thread `3035e001-85df-4036-bb91-83194012ba5e`, title *Check How Skill Changes Are Detected*, in environment `13918500-09c0-412e-83d0-416667c3d684`. These exports are evidence from the `/home/juancamiloqhz` host, not live access from Orbit. The source remained clean at `b3b8fbab33aa233b8a2b8649ccd330cf7a82f49b`. The post-compaction capability payload identifies the coordinator as `claudeAgent / claude-opus-5-5`, effort `medium`, fast mode `false`.

| Run and export positions | Observation |
| --- | --- |
| 5, 52–54 | User sent `/compact` while the earlier activation remained in effect. Provider event `d3c72333-e480-4b92-a55f-e2852553e444` completed at `19:33:58.004Z`; T3 reported token counts of 109,604 before and 4,415 after. |
| 6–7, 55–86 | A source question without reinvocation led to a fresh Juan-mode read at 57, Investigation/How reads, complete-catalog preflight at 71 and one configured Codex explainer at 72. The parent checked an extra-files fixture while the child ran. The first turn returned an interim waiting update; child completion at 73 and notification at 80 preceded the later final answer at 85, which reported active state. |
| 8, 87–89 | User explicitly turned Juan-mode off. Claude acknowledged an inactive record and started no work. |
| 9, 90–92 | User sent `/compact`. Provider event `4d5b172e-3fdf-4caa-ac16-df92c9bf3764` completed at `19:43:56.038Z`; T3 reported token counts of 85,821 before and 5,216 after. |
| 10, 93–96 | A new question about missing/different packages received an inactive-state answer. This entire turn contains no source-read, preflight, file-change or delegation tool event. The latest opt-out survived, but the answer's claim that it read the script is not supported by a fresh read in this turn. |

The active follow-up used the same source question and write boundary as the Codex active test: explain which installed files the checker compares and whether extras affect the result, preserve source/install/configuration, and allow workflow temporary files. The off-state follow-up requested examples of missing and different packages under that same boundary. Both requested state/workflow reporting without prescribing the state. There was no activation between either compaction and its following task.

Parsing the fresh capability payload at 68 and the temporary catalog creation at 70 confirmed exact JSON equality. Preflight selected `/home/juancamiloqhz/.config/jstack/models.json` and resolved `how explainer` to `codex / gpt-6.1-sol`, high reasoning effort. The requested target and returned dispatch identity/options match. Its task ID is `node:delegated-task:command%3Amcp%3Ab2386b9e-2803-4be9-8cc1-840b408ac2eb%3Adelegate-task%3Ajstack-inv2-compared-files-explainer-r1`. The export contains its completed task record and returned explanation; it does not include the child's full underlying tool trace or a live status query from Orbit.

An early read command failed only because an old `/tmp/jstack-inv/parent` directory was absent. The agent continued in `/tmp/jstack-inv2/`, passed preflight and completed the task. Visible parent writes were confined to the allowed catalog and scratch fixtures, including a copy of the installed root. Its checker comparison stayed at 57 matching after added extras; repository status remained clean. The child reported scratch checks and six passing existing tests. The parent removed the catalog and freshly read Unslop plus two cited principle leaves at 83. That read does not independently establish the external Unslop package's identity. No source, installation or model-configuration mutation appears in the parent activity; this is not a remote filesystem-wide audit.

The inactive response correctly retained opt-out and started no workflow. Its answer is consistent with the source already present in the history, but its claim of reading the script has no fresh tool evidence. Treat fresh-source verification as incomplete. Its wording about dropping delegation refers to Juan-mode's routing; opt-out does not prohibit an independently requested or applicable standalone skill. Both state cases pass within this snapshot, with one manual compaction per state and explicit state-reporting prompts. Token counts are T3's reported fields, not an independent context measurement or proof of exact summary contents. Restart/resume, automatic compaction and broader provider support remain open. The exported conversation ends inactive.

## Fidelity and retention

No operational skill, resolver, model assignment, source pin or reviewed checkpoint changes. Direct inspection of `pstack/skills/poteto-mode/SKILL.md` at original pin `11713c683fe4add4fd403ea880580abbc9e0875f` confirms its Cursor mode/reminder metadata; How at the same pin requires one explainer on the simple path. The audit revision `0148b78c56c72a1b8412055913c79f767095b217` retains that child requirement. The existing [Juan-mode adaptation](../../adaptations/juan-mode.md) owns the user-approved T3 conversation-state and configuration differences. This report measures that adaptation without revising it or claiming Cursor equivalence.

Retain this concise assessment and its durable thread/event references. Served client bundles and selected-file hash evidence stay in task-owned cache; no transcript, catalog, generated page or app database is committed. Documentation checking and `git diff --check` validate this evidence-only change, not runtime behavior.
