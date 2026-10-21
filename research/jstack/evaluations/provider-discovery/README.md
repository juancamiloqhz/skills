# Cursor provider discovery probe

On 2026-10-20, a user-approved `cursor / default` child loaded installed jstack skills and completed a configured Codex explainer. The overall workflow assessment is incomplete. The probe shortened its catalog before validation and declined the Unslop writing step. Successful dispatch and a correct source answer do not close those gates.

A separate [complete capture follow-up](#complete-capture-follow-up) passed later that day. Subsequent [explicit Unslop use](#explicit-unslop-follow-up) and a [guided Investigation repeat](#guided-investigation-repeat) establish writing and core execution, with scope, loading-evidence and presentation limits still open.

The later [read-recording check](#read-recording-and-presentation-check) reproduces empty recorded bodies despite text reaching the agent. Bounded reads and citation preservation pass. An integrated follow-up preserves the explainer and verifies a runtime-provided capability file, while its requested native-Write method remains incomplete.

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

The initial probe left two follow-ups: faithful complete capture and a supported Unslop invocation assessment. Capture must not rebuild a model inventory or search internal provider storage. Unslop assessment must preserve the upstream explicit-only flag and distinguish an actual rejected call from a decision not to invoke it. The separate capture test below addresses only the first follow-up.

This single fresh child establishes bounded Cursor execution and actual Cursor-to-Codex delegation. It does not prove top-level activation, later-task persistence, compaction, restart, all 57 entrypoints, standalone Cursor support or OpenCode execution. OpenCode still needs an available live model before its execution check.

## Complete capture follow-up

At source `4b34a8de9bc6adb90cbed0f60bcaa7ac2ce4f8d8`, a fresh user-approved `cursor / default` child tested capture alone. The brief explicitly required every response property, prohibited reconstructed inventories and internal storage access, and left preflight to the parent after independent comparison. This was a guided test of the existing capture contract, not an unassisted Investigation run.

The [capture conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A7c5b7dfd-b026-4108-a4b5-d9278a6d9393%3Adelegate-task%3Ajstack-cursor-complete-catalog-20261020-r1) records one native `orchestrator_capabilities` call at position 8, Cursor `Write` at 16 and JSON parsing at 18. The saved file contained eight providers and 71 models. The parent recovered the complete original tool item through three paginated `t3_thread_read` reads and compared its parsed payload recursively with the saved file. All keys and values matched, including array order, labels, defaults and inherited settings. There were zero differences. Counts and successful parsing alone were not the acceptance test.

The parent then ran the installed canonical preflight against that verified file:

```sh
python3 -B /home/ubuntu/.agents/skills/jstack-juan-mode/scripts/preflight.py \
  --setup-skill /home/ubuntu/.agents/skills/jstack-setup \
  --project-root /home/ubuntu/Dev/skills \
  --catalog /path/to/captured-catalog.json --role 'how explainer'
```

Whole-configuration validation passed and resolved the global `how explainer` to `codex / gpt-6.1-sol / reasoningEffort: high`, with `canDispatch: true`. This capture-only test did not dispatch another explainer. Terminal task status was `completed`, with a result available and no pending child work, question or approval. Independent checks found a clean repository before reporting and unchanged hashes for the saved models, installed capture contract and installed preflight script.

Cursor's file-writing tool can preserve this complete live response without a shell fallback, reconstructed schema or internal runtime-store read. No skill correction is needed for that demonstrated route. One guided capture does not establish unattended reliability, a larger catalog's behavior, native skill registration or full workflow completion. The follow-ups below assess explicit Unslop use and a fresh Investigation. The task-owned catalog was removed after assessment.

## Explicit Unslop follow-up

At source `c663acc93424d6a005dfc180928505c91b29e149`, a fresh user-approved `cursor / default` child received an explicit request to apply installed Unslop to a supplied paragraph. The [writing conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A43e44741-8770-4b39-baaa-3c5c3e38701e%3Adelegate-task%3Ajstack-cursor-unslop-invocation-20261020-r1) records the full skill read at position 7 and the rewrite at 9. The parent recovered that read and verified that its body equals the installed file. The rewrite preserves manifest selection, missing/changed-file detection and ignored installed extras while replacing filler and vocabulary under rules 7, 9, 23 and 31. For example, "leverages" became "uses".

The agent reported no exposed native skill-invocation mechanism. The transcript contains no native invocation call or rejection, so this result establishes explicit filesystem loading and application only. [Cursor's documentation](https://cursor.com/docs/skills) describes explicit slash invocation for flagged skills; it does not establish that path inside this T3 child. The test preserves `disable-model-invocation: true`, matching the pinned dependency. Terminal status was completed with no pending work. Repository status and protected model/Unslop hashes were unchanged. No scratch output was requested or retained.

## Guided Investigation repeat

A fresh `cursor / default` child at the same revision received the original checker question, installed authoring paths, the two prior failure findings and an explicit Unslop request. Temporary catalog/findings writes were permitted in one assigned cache directory. This guidance differs from an ordinary unassisted request. The [repeat conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A43e44741-8770-4b39-baaa-3c5c3e38701e%3Adelegate-task%3Ajstack-cursor-investigation-repeat-20261020-r1) establishes these results:

| Check | Independently assessed evidence |
| --- | --- |
| Catalog | The saved file equals the complete native response at position 26, with zero parsed key/value differences across all eight providers and 71 models. This verifies content independently of the helper's claimed save method. |
| Configuration and dispatch | Canonical preflight at 44 selected the global `how explainer` as `codex / gpt-6.1-sol / reasoningEffort: high`. The actual T3 dispatch at 47 returned that exact target. |
| Explainer and answer | The configured child completed, wrote its explanation/citation index and had no pending work at 57. Both agents inspected the pinned source. The checked answer correctly describes expected-path selection, byte comparison, status priority and ignored extras. This was static inspection, not checker/test execution. |
| Writing and steps | The coordinator read the full installed Unslop body at 62, then produced the final answer. Item 72 records all four Investigation steps completed before the answer at 74. |

The configured explainer task is `node:delegated-task:command%3Amcp%3A142dddca-2b4d-48b6-b66b-db5794b76db6%3Adelegate-task%3Ajstack-cursor-investigation-repeat-20261020-explainer-r1`. Its backing conversation independently confirms the source reads, assigned artifact writes and terminal result. The coordinator's original task also completed with no pending work. A later queued coordinator turn was cancelled before starting, leaving the backing thread labelled cancelled; this does not change the original task's completed result.

This repeat is not a clean full-workflow pass. At 29 and 34, the coordinator made unnecessary host-path and environment searches while trying to save a catalog despite working native MCP. The native helper at 42 returned a narrative summary of repeated save attempts, without separate tool receipts in this view. Exact saved content is proven; the claimed helper Write sequence and selection are not independently verified. Do not copy private runtime metadata or promote those searches into a capture method.

The durable Read outputs for Help, Juan-mode and setup entrypoints at 3–5, and the explainer report at 60, contain empty body strings despite file metadata. The full entrypoint/report loads therefore remain unverified in this record. No Help recipe read is recorded. The coordinator did receive nonempty Investigation, How, shared-contract and Unslop bodies. Its final answer also rewrote the linked explainer text and dropped clickable citations, exceeding the pinned How instruction's light-edit presentation boundary even though the checked claims remain correct.

The explicit writing route and core configured execution work in these bounded tests. A further clean workflow check must verify body retrieval and Help routing, use the demonstrated direct capture route within scope, and preserve the explainer output with light edits. Native slash registration, automatic dependency selection and top-level persistence remain unverified. These results alone did not justify an operational skill change. Repository status and protected model/Unslop hashes stayed unchanged. Task-owned catalogs and redundant findings were removed after assessment; keep this report and durable task references.

## Read recording and presentation check

At source `12dda55366151d02903cb65a21ee9e08873d1828`, a fresh `cursor / default` child received a controlled retrieval test. The parent generated 320 inert lines containing three fresh random markers, whose values were absent from the brief. The [read-check conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A43e44741-8770-4b39-baaa-3c5c3e38701e%3Adelegate-task%3Ajstack-cursor-read-recording-20261020-r1) records one whole-file Read at position 6, followed by the correct three marker values at 8 before any reread. That tool item's durable `content` is empty, with nonzero file metadata and `textTruncated: false`. No intervening reader or alternate source for the values is recorded. The agent obtained the text even though this durable Read record omitted it. The component responsible for that omission was not diagnosed.

Eight bounded Read bodies at 9–16 reconstruct all 320 lines. Bounded bodies also reconstruct the complete installed Help, Juan-mode, setup, Unslop and Help recipe files. Comparisons restore only line separators omitted at range boundaries and the fixture's final newline. The actual Investigation prompt was read from Help's linked `references/recipes.md`. The final supplied explanation matches its source, ignoring only a terminal newline; both local citation links remain intact. All protected files, source and fixtures were unchanged after the task, which completed without pending work. This proves the bounded retrieval and supplied-text presentation routes, not a full Investigation or improved unassisted behavior. It does not retroactively prove the earlier entrypoint loads.

To reproduce the recording distinction, generate fresh marker values outside the agent brief, require an immediate report after one whole-file Read, and compare that report with the fixture before permitting bounded rereads. Then concatenate the bounded bodies and compare them with the complete file. Reusing marker values already visible in the prompt would not establish receipt. Keep the small protocol and result; remove generated fixtures after assessment.

### Integrated follow-up and response files

A fresh [integrated conversation](t3-thread://v1/thread:delegated-task:command%3Amcp%3A43e44741-8770-4b39-baaa-3c5c3e38701e%3Adelegate-task%3Ajstack-cursor-investigation-clean-20261020-r1) used the same revision, explicit authoring paths, bounded reads, one configured explainer and an explicit Unslop request. The native capability call at 25 now had a much larger response. The agent identified a current tool-output file containing the unwrapped catalog. [Cursor documents saving long tool responses as files](https://cursor.com/blog/dynamic-context-discovery). The durable MCP record here has an empty text body, so the original inline payload cannot be independently recovered from that record.

The parent checked the exact identified response file against `catalog.json`: both have identical bytes, parse as the same complete object and identify this caller. This snapshot contains eight providers and 528 models. Older eight-provider/71-model counts were not used as an expected inventory. The runtime-owned response file was preserved. This establishes faithful copying of that file, rather than a second independent copy of the original MCP payload.

Canonical resolution and preflight at 72 and 79 selected the global config, then carried its absolute path explicitly. T3 dispatch at 91 returned `codex / gpt-6.1-sol / reasoningEffort: high` and a completed explainer with no pending work. Its task ID is `node:delegated-task:command%3Amcp%3A1bfa3a5e-08bf-472b-a1a7-36e497ff3d3d%3Adelegate-task%3Ajstack-cursor-investigation-clean-20261020-explainer-r1`. The parent independently read that child's source inspection and artifact write. The coordinator checked the pinned source and copied the explanation exactly, ignoring only its final newline; all 11 citation link strings survived. Item 103 records all four steps completed before the final answer. This verifies source content and preserved link strings, not the application's handling of local `#L` links. Neither checker nor tests ran.

The protocol is still qualified. It specifically requested native Write capture and stopping if that route could not preserve the response. The agent instead made several staging/chunk attempts, then copied the response file programmatically and disclosed the deviation. The native-Write-only variant is incomplete. Search tools labelled as scoped to Help also returned checkout paths, including `.git`; the agent later used explicit absolute paths. These are retained scope/method findings, not a clean protocol pass. The earlier controlled full-body check remains separate from this run's partial instruction reads. No additional native capture helper or model substitution was used.

The verified file-copy mechanism motivates one narrow addition to setup's existing T3 reference: use an exact response file supplied by the current tool/runtime, parse and preserve its full unwrapped payload, verify equality and keep the runtime-owned file intact. Do not search runtime stores for an alternative. The mechanism worked before the new paragraph was written; no reliability improvement from the wording is claimed. This follow-up resolves the recording inference and verifies presentation preservation, while native invocation, automatic dependency selection, top-level persistence and a clean unrestricted workflow remain open. Generated fixtures, copied catalogs and redundant findings are removed after assessment.

## Fidelity and retention

The only operational change is the runtime-provided response-file paragraph in setup's existing T3 reference. The [setup comparison](../../adaptations/setup-jstack.md#runtime-provided-capability-files-2026-10-20) records its necessity against setup's own pin. The four Investigation steps and How's one-explainer/light-edit rules remain unchanged from their existing adaptations of `11713c683fe4add4fd403ea880580abbc9e0875f`. The pinned Unslop source retains its explicit-only flag. Current comparisons and invocation limits remain in the [Investigation](../../adaptations/investigation.md), [How](../../adaptations/how.md) and [Unslop dependency](../../adaptations/technical-writing.md#unslop-dependency-assessment) records. Model settings, source pins and the reviewed checkpoint remain unchanged.

Keep this concise assessment and durable task references. No transcript, catalog, internal database, private metadata, generated fixture or new runner is committed. Documentation checking and `git diff --check` validate this report's consistency, not the incomplete workflow.
