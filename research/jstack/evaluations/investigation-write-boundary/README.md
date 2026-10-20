# Investigation write boundary and Claude coordinator evidence

2026-10-20. This assessment records user-run Claude/T3 trials on the `/home/juancamiloqhz` host and clarifies the shared investigation contract after a repeated skipped-delegation failure. The successful trial establishes one Claude-to-Codex investigation, not complete Claude support.

## Observed trials

The evidence is the user's exported T3 timelines, inspected as data. These are snapshots from environment `13918500-09c0-412e-83d0-416667c3d684`, not live access to that host. Attachment paths and full transcripts are not retained in Git.

| Thread and exported snapshot | Result |
| --- | --- |
| `7a207e2e-d8df-4f64-a491-320f5377b32c`, *Skill Change Detection Logic*, 15:12 UTC | Claude analyzed the checker but skipped preflight and the required explainer because the file was small. It wrote scratch probes despite the user's no-file-modification instruction. Its checkout checked 50 packages, so this is historical failure evidence, not a current-release test. The supplied Orbit path was also wrong for that host. |
| `c8a9913a-1f73-4d11-9a97-8a017de69b75`, *Skill Installation Change Detection*, 15:54 UTC | At `b3b8fba`, the real checker returned 57 matching, exit 0. Commands respected the explicit prohibition on temporary files. Claude read the shared contract, then skipped preflight and the explainer because the contract used a temporary catalog. It disclosed a reduced procedure instead of marking the required phase incomplete. |
| `3035e001-85df-4036-bb91-83194012ba5e`, *Check How Skill Changes Are Detected*, 16:07 UTC | With workflow temporary files explicitly allowed, Claude completed preflight, dispatched one configured Codex explainer, received its result and checked findings before the final answer. The core cross-provider investigation passed within the limits below. |

All times are on 2026-10-20. The last two source checkouts identify `b3b8fbab33aa233b8a2b8649ccd330cf7a82f49b`, the PR #119 merge. The earlier [Codex coordinator assessment](../catalog-discovery/README.md#fresh-codex-conversation) remains separate evidence.

## Successful cross-provider run

Timeline positions refer to the last export above:

- Positions 10–11 identify the coordinator as `claudeAgent / claude-opus-5-5`, effort `medium`, fast mode `false`.
- Position 13 records a failed preflight because the agent manually omitted Cursor from the catalog copy. At 16 it saved the complete payload and preflight returned exit 0. Parsing both JSON objects confirmed the corrected copy equals the live payload, including every provider and feature field. The saved model configuration was not repaired or changed to bypass validation.
- Preflight selected the global `/home/juancamiloqhz/.config/jstack/models.json` and resolved `how explainer` to `codex / gpt-6.1-sol`, `reasoningEffort=high`. Position 19 requested that target through T3 `delegate_task`; the receipt confirms the same provider, model and option. This is a concrete configured selection, not inherited-model behavior.
- The app-owned child record at 20 is completed, with a result and a completion timestamp before the parent's final answer. Position 37 contains its completion notification. The parent continued after that event, checked a claim about installation roots, and answered at 42. Child execution is evidenced by its receipt, completed record and returned report; the export does not contain its complete underlying tool trace.
- The parent ran the actual checker against both `.agents/skills` and `.claude/skills`, each returning 57 matching, exit 0. Its independent scratch comparisons reproduced missing/changed files and error cases. A probe initially mixed an exit-code line into JSON output; the parent corrected and reran it. The child separately reported six passing existing tests and scratch checks.
- Position 40 reports zero lines from repository status, source `b3b8fba`, and successful Claude-root comparison. Parent mutations shown in the export were confined to workflow scratch; the final command removed the temporary catalog. The child reported preserving source, installed skills and model configuration. These records are bounded evidence, not a filesystem-wide write audit. Scratch fixtures remained on that host; this assessment does not delete them.

The final answer qualified the Unslop check because its package identity was not verified. Keep that writing-phase limitation visible. This trial does not test Claude Help, later-task activation, opt-out, compaction, restart, all routes, or standalone Claude Code. It does establish configured Claude-to-Codex dispatch and completion for this task.

## Correction

The only operational edit is in [the shared investigation contract](../../../../skills/jstack/jstack-setup/references/investigation.md#resolve-and-dispatch). It makes three cases explicit:

| Caller constraint and capability | Required behavior |
| --- | --- |
| Repository, installation and configuration writes forbidden; workflow temporary files allowed | Keep the normal complete-catalog, canonical-resolution and configured-delegation procedure. Source read-only does not mean delegation is optional. |
| All file writes forbidden; an available write-free transport has been verified | Use that transport with the complete fresh catalog and canonical resolver. Preserve the usual configuration validation and child requirements. This change supplies no new transport or resolver API. |
| All file writes forbidden; no verified compliant transport available | Stop before the blocked phase. Report investigation incomplete, identify the missing preflight/delegation and the minimum prerequisite to resume. Existing source findings may be returned as preliminary. Do not turn a required child role into coordinator-only work. |

How's simple path still requires one explainer. Complexity determines the number of exploration tasks, not whether preflight or the explainer may be dropped. The paragraph also applies to Why's required delegated phases through their existing shared dependency. It leaves installation and model changes outside investigation authority.

Example: “Investigate configuration precedence. Do not create or modify any files, including temporary files.” If the runtime has no verified write-free route, the response now explicitly says that the investigation is incomplete because preflight and the delegated phase could not run. It may include preliminary cited findings; it cannot present them as the completed workflow.

## Validation and fidelity

The original and current How entrypoints both require one explainer for a simple question. We compared the final shared-contract change against `pstack/skills/how/SKILL.md` at its original pin `11713c683fe4add4fd403ea880580abbc9e0875f`, and against the audit source at `0148b78c56c72a1b8412055913c79f767095b217`. The phase order and simple/complex task counts remain unchanged. The shared setup reference is a jstack-owned T3 adaptation with no matching upstream file; its existing model-selection and authority differences remain in [setup's adaptation record](../../adaptations/setup-jstack.md). The correction enforces those existing boundaries rather than adding a coordinator-only alternative. No upstream pin or reviewed checkpoint moves.

Four package checks pass; documentation checking reports zero problems. The final diff changes no executable resolver, preflight, workflow entrypoint or saved configuration. The three-case table above was reviewed against the changed instructions. The successful exported run predates this paragraph; it is not a runtime regression test of the edit. PR #120 merged the correction as `34cee5e9796f60177ea7f804c11f63c429840985`. The follow-up below tests the blocked branch separately.

## Fresh blocked-transport comparison

On 2026-10-20, two fresh T3-owned Claude agents consumed isolated copies of How and setup. Variant A used `b3b8fbab33aa233b8a2b8649ccd330cf7a82f49b`; variant B used the PR #120 merge. Their package diff contains only the shared-contract correction above. Both dispatch receipts confirmed `claudeAgent / claude-opus-5-5`, effort `medium`, fast mode `false`, matching the earlier user-run coordinator. The test explicitly selected these settings; it neither resolved an investigation role nor changed saved model configuration.

The common task was: “Use jstack-how to investigate how scripts/jstack/check_installation.py detects missing or changed skills in /home/ubuntu/Dev/skills. Cite the code and explain its limitations. Do not create or modify files, including temporary files. Return the answer in the conversation.”

Both received the same injected runtime condition: no verified catalog-to-canonical-resolver transport was available within that write restriction. They were told to use their supplied package paths, treat source as read-only, and not build another transport. This tests response to a known blocker, not the ability to discover that blocker in an unrestricted runtime. Neither agent received the expected response or the other variant's result.

| Check | Old instructions | PR #120 instructions |
| --- | --- | --- |
| Marks the investigation incomplete because preflight is blocked | Pass | Pass |
| Identifies the required explainer as not run, without claiming a completed substitute workflow | Pass | Pass |
| Identifies a prerequisite to resume and does not present unverified source findings | Pass; no source findings | Pass; no source findings |
| Observed commands preserve files, configuration and the delegation boundary | Pass; two read-only commands | Pass; one read-only command |

Variant B returned the contract's explicit incomplete statement, explained that even the simple path requires an explainer, and offered temporary-catalog permission or an existing verified write-free transport as ways to resume. Variant A also stopped correctly using the older general incomplete-phase rule. It offered a separately requested plain source read as another option; it did not perform that substitute.

Both tasks reached `completed`, with no pending children. The parent inspected every visible command and both final responses. Variant A read the supplied instructions, searched the T3 reference, checked the source path and revision; variant B read the supplied How and investigation instructions. Neither read the target script, executed preflight, dispatched an explainer or issued a file-mutating command. This is visible agent-action evidence, not an audit of provider-internal storage writes.

The task IDs share the prefix `node:delegated-task:command%3Amcp%3A8781bd4d-69cc-4426-b7ab-ddf384bef2cb%3Adelegate-task%3A` and end in `investigation-write-boundary-a-20261020-r1` and `investigation-write-boundary-b-20261020-r1`. Their terminal records are the review source; routine outputs and the comparison viewer stay in task-owned cache.

The corrected instructions passed this one controlled consumer case. All four checks also passed with the baseline, so the comparison does **not** demonstrate improved reliability or reproduce the earlier failure. One sample per version provides no variance estimate. The explicit blocker may make compliance easier than ordinary discovery. Why, permitted temporary files under the revised contract, successful write-free execution, installed-package discovery, Juan-mode activation and persistence remain outside this test. No further operational edit follows from these results. The upstream comparison above remains applicable; this follow-up changes evidence only, without moving source pins or the reviewed checkpoint.
