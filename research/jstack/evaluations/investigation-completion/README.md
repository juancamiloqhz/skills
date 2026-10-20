# Investigation completion evidence

The 2026-10-20 follow-up verified a full parent-side Unslop read and corrected an earlier assessment of unfinished task lists. T3 updates a task-list item in place. Reading only later activity positions missed its completed steps. No operational skill change is retained.

## Trial and observations

The existing [Start an Investigation with Juan Help](t3-thread://v1/0fdfffb0-c122-496f-a9df-cd8a37238812) conversation used `codex / gpt-6.1-sol`, low effort and standard service tier on Orbit. The source baseline was `49eaf11b8b05e48944de4bfb95adab65083a4acd`, the PR #123 merge. Its installed setup investigation reference still predated PR #120; temporary preflight files were allowed, so that reference's strict-write branch was not exercised.

Both source questions asked how `scripts/jstack/check_installation.py` selects files and whether it detects installed extras. Repository, installed-skill, configuration and service changes were forbidden. Both turns completed fresh preflight and one configured `codex / gpt-6.1-sol` explainer at high effort and standard service tier. The parent and children read current source, and the final answers correctly identified manifest packages, Git-tracked paths, byte comparisons, ignored extras and the working-file baseline. This was static reading, not a checker execution.

| Run and positions | Observation |
| --- | --- |
| 15, 124–141 | Installed baseline, explicitly asked to reread the mode entrypoint. The source answer completed at 140. No fresh parent Unslop read appears in this turn. A terminal reread of task-list item 132 shows all four steps completed, updated before the final reply. |
| 16, 142–158 | Authoring experiment loaded the repository playbook at 144 with a temporary completion paragraph. The parent read the entire installed Unslop file at 145. Task-list item 147 recorded that path and all four steps complete before final answer 157. |
| 17, 159–161 | Explicit opt-out restored the original inactive state. No new task ran. |

The authoring paragraph asked the agent to reconcile its task list before the final reply and record the Unslop path before completing the writing step. The experiment explicitly supplied that playbook path. It was removed after terminal rereads disproved the unfinished-plan premise. The final repository and installed playbooks are unchanged. This experiment demonstrates the read and task-list operations; it is not an unchanged-instructions reliability test or a shipped correction.

The baseline explainer task ends in `selection-extras-explainer-20261020-2`; the authoring explainer ends in `author-selection-explainer-20261020-1`. Both share task-ID prefix `node:delegated-task:command%3Amcp%3A9fa8734e-1ccf-46bd-8c4b-66f7e3ddb921%3Adelegate-task%3A`. Their dispatch records at 134 and 151 match the resolved models and options. Each temporary catalog exactly matched its fresh capability payload. Both backing conversations were independently observed completed, with no active run or pending request.

The full command output at 145 contains every Unslop rule through rule 33. Its file hash matches the [existing version-specific assessment](../../adaptations/technical-writing.md#unslop-dependency-assessment), and the installation record identifies `cursor/plugins`, `pstack/skills/unslop/SKILL.md`. The final response preserves the source findings and follows the loaded writing rules. This supports the explicit Codex authoring case, not invocation permission on another provider. No rejected host invocation was bypassed.

The protected installed entrypoint, installed playbook, Unslop file and saved model configuration matched their pre-test hashes. Both temporary catalogs were removed, and both child conversations were quiescent. These checks cover selected files and visible actions, not all filesystem writes.

## Corrected earlier findings

Terminal rereads also found all four steps completed in the earlier compaction run 10 at item 83 and manual-recovery run 13 at item 113. Their previous reports incorrectly said there was no final completion update. The item-level `status` field still says `running`; the current step text contains four `[completed]` entries. The final step updates preceded their final answers.

The [compaction](../conversation-compaction/README.md) and [manual-recovery](../conversation-recovery/README.md) reports now correct that claim. Their separate limits remain: no fresh parent-side Unslop identity/load evidence in those turns, and failed automatic backend recovery. A missing fresh read does not prove previously loaded instructions were unavailable or unused. The new trial does not retroactively establish the older writing checks.

## Review procedure and limits

After a run becomes terminal, reread its known task-list item IDs or its complete activity range. An `afterPosition` cursor retrieves later positions, not updates to an earlier item. Inspect the current step states and update time; neither an earlier snapshot nor the outer item status establishes unfinished work. Recover truncated evidence with `itemId` and `textOffset` until `nextTextOffset` is null before claiming a full file read.

This was one baseline and one explicitly guided authoring experiment in the same existing native conversation. Prior context, explicit file loading and different playbook text prevent attributing the result to a general reliability improvement. Missing or blocked Unslop, fresh-conversation discovery and other providers were not tested here. No additional restart, installation or model change ran.

## Fidelity and retention

The final diff changes only research records and review guidance. Inspection of `pstack/skills/poteto-mode/playbooks/investigation.md` at pin `11713c683fe4add4fd403ea880580abbc9e0875f` confirms its four steps, ownership line and reply boundary. The temporary experiment changed none of those steps, and its extra paragraph is absent from the delivered package. Existing runtime differences remain in the [Investigation adaptation](../../adaptations/investigation.md). No source pin or reviewed checkpoint advances.

Keep this concise assessment and durable conversation references. No transcript, catalog, application database, temporary playbook or additional runner is committed. `node scripts/jstack/check_docs.mjs` and `git diff --check` validate documentation consistency, not agent reliability.
