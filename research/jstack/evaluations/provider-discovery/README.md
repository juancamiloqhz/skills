# Cursor provider discovery probe

On 2026-10-20, a user-approved `cursor / default` child loaded installed jstack skills and completed a configured Codex explainer. The overall workflow assessment is incomplete. The probe shortened its catalog before validation and declined the Unslop writing step. Successful dispatch and a correct source answer do not close those gates.

## Environment and prerequisites

The source was clean at `83bd97f1ecba86d77dd3e4cd79a496f95f35a240` on Orbit. Cursor CLI was `2026.10.01-e373342`; OpenCode was `2.1.1`. The live T3 catalog offered Cursor child execution and models, but no OpenCode models. OpenCode execution was not attempted.

The installation checker returned a completed comparison with exit 1 both before and after the probe: 56 matching, zero missing and one different package. Only `jstack-setup/references/investigation.md` differed, retaining the version before PR #120. Temporary workflow files were allowed, so the strict no-writes branch was not tested. No installation was updated.

There were 57 installed jstack packages under `~/.agents/skills`. Current [Cursor documentation](https://cursor.com/docs/skills) and [OpenCode V2 documentation](https://dev.opencode.ai/v2/docs/skills/) include that global discovery directory. Filesystem presence and documentation do not establish native catalog registration or successful invocation.

The user selected Cursor default routing for this temporary test. The dispatch receipt confirms provider `cursor`, model `default` and empty options. It does not identify the concrete model behind that routing alias. The saved jstack role map was preserved.

## Observed execution

The [Cursor probe conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A7c5b7dfd-b026-4108-a4b5-d9278a6d9393%3Adelegate-task%3Ajstack-cursor-provider-discovery-20261020-r1) contains one delegated run. Positions below refer to that conversation.

| Check | Evidence and assessment |
| --- | --- |
| Installed entrypoints | Filesystem searches found the packages. `npx skills list -g` at 37 reported the installed Help path. Reads at 11–13, 20–27 and 32 loaded Help, Juan-mode, Investigation, How, setup and their references. This is external-CLI and filesystem discovery, not proof of Cursor's native skill catalog or slash registration. |
| Help routing | The installed recipe at 24 and guide at 45 supplied the Investigation route. Help and the subsequent investigation were explicitly requested in the probe brief. |
| Live catalog | Native T3 MCP capability calls succeeded at 10 and 44. The ACP fallback variable was unset, but MCP tools were already available. |
| Catalog fidelity | At 63 the agent manually built a compact catalog and passed it to preflight. It reconstructed model IDs and option schemas and omitted fields such as model and option labels. The fresh payload had eight providers and 71 model entries. The constructed file was not the complete unwrapped payload required by setup's existing contract. Its passing preflight does not verify that gate. |
| Configured delegation | The installed resolver selected `/home/ubuntu/.config/jstack/models.json` and `how explainer = codex / gpt-6.1-sol / reasoningEffort: high`. Dispatch at 66 returned that exact target. The actual cross-provider task completed, although it followed the invalid catalog-capture step. |
| Checked source answer | The Codex child read the pinned checker and its existing test. Cursor reread the checker at 68 and the relevant test at 71. The final answer at 77 correctly explained manifest packages, tracked paths, byte comparisons, ignored extras and working-file bytes. This was static inspection, not a checker or test execution. |
| Writing | Cursor read the installed Unslop file at 69, then declined to apply it because of `disable-model-invocation: true`. The final response explicitly marked writing incomplete. No native invocation rejection was observed, so this does not establish that Cursor cannot execute an explicitly requested Unslop pass. |
| Final task state | Item 74 lists the first three steps completed. The final response reports the fourth cancelled and writing incomplete. The agent task itself completed; the workflow did not pass every required phase. |

The nested task ID is `node:delegated-task:command%3Amcp%3A108441eb-4c87-44de-b25a-39f1f98b5485%3Adelegate-task%3Ajstack-cursor-provider-discovery-how-explainer-20261020-r1`. Its dispatch and status responses show `completed`, `workState: result_available`, no pending child runs and no pending question. Independent reads found both backing conversations completed with no active run or pending request.

During review, the parent recovered the complete original capability payload from item 44 through `t3_thread_read` and separately ran canonical preflight against that snapshot. Whole-configuration validation passed and selected the same saved Codex explainer and high effort. The assessment-only catalog was then removed. This verifies the saved selection against the actual catalog after the fact; it does not repair the probe's earlier capture failure or establish an unassisted Cursor capture route.

## Capture and scope failures

The catalog builder at 63 explicitly described its input as reconstructed and compact. This violates the existing instruction to preserve the full live payload rather than shorten it. A known output schema and successful role resolution are not substitutes for faithful capture. No failure of a supported complete-capture method was demonstrated, so do not attribute this result to an inherent Cursor limitation.

While seeking a capture method, the agent also searched older task catalogs and inspected its own internal Cursor session database metadata at 53–55. Those reads were unnecessary for the bounded skill probe and are not an accepted capture method. No internal runtime-store contents or values are retained in this report. The investigation should stay within supported catalog tools and task-owned files, and report an incomplete prerequisite when it cannot preserve the required evidence.

## Cleanup and next conditions

The agent removed its owned temporary directory and pointer at 75. Parent checks confirmed both were absent, all selected installed/configuration hashes matched the baseline, and the full installation comparison retained the same single pre-existing difference. Repository status was clean before this report. These checks are not a filesystem-wide audit of CLI caches or provider storage writes.

The next capture check must preserve the complete fresh payload through a supported file, stream or bounded-chunk route and compare the parsed result before accepting preflight. It must not rebuild a model inventory or search internal provider storage. The Unslop follow-up needs a supported invocation assessment that preserves the upstream explicit-only flag and distinguishes an actual rejected call from a decision not to invoke it. Neither correction is implemented or claimed tested by this report.

This single fresh child establishes bounded Cursor execution and actual Cursor-to-Codex delegation. It does not prove top-level activation, later-task persistence, compaction, restart, all 57 entrypoints, standalone Cursor support or OpenCode execution. OpenCode still needs an available live model before its execution check.

## Fidelity and retention

The final change is research-only. The four Investigation steps and How's one-explainer simple path remain unchanged from their existing adaptations of `11713c683fe4add4fd403ea880580abbc9e0875f`. The pinned Unslop source retains its explicit-only flag. Current comparisons and invocation limits remain in the [Investigation](../../adaptations/investigation.md), [How](../../adaptations/how.md) and [Unslop dependency](../../adaptations/technical-writing.md#unslop-dependency-assessment) records. No skill, model setting, source pin or reviewed checkpoint changes.

Keep this concise assessment and durable task references. No transcript, catalog, internal database, private metadata, generated fixture or new runner is committed. Documentation checking and `git diff --check` validate this report's consistency, not the incomplete workflow.
