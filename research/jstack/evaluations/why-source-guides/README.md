# Why source-guide update

The [coverage audit](../../coverage-audits/2026-10-18/README.md) found four Why source guides that retained prose removed upstream. This update follows those deletions while preserving the existing evidence and read-only contracts.

## Source and scope

Local base is merged PR #89, `c17e0aafb006806282a5f84f63014ff29be262bc`. Compare `pstack/skills/why/` from original adaptation pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/why).

All five changed source paths are accounted for:

| Source path | Local disposition |
| --- | --- |
| `references/sources/code-archaeology.md` | Adopt deletion of the detailed PR-context recipe, evidence examples, pitfalls and return list. The final file matches source exactly. |
| `references/sources/incident-postmortem.md` | Adopt the reduced three-bullet guide, matching source exactly. Its caller still supplies it to investigators of defensive code. |
| `references/sources/sentry.md` | Adopt deletion of background, evidence examples and pitfalls. Preserve the existing read-only Seer substitution, text-fence labels and list spacing. |
| `references/sources/slack.md` | Adopt the shorter search guide and deleted return list, matching source exactly. Upstream still requires full threads in its retained pitfalls. Preserve source numbering. |
| `SKILL.md` | Its only upstream change adds adaptive effort/speed. Keep selected model options unchanged under the existing configuration policy. |

The parent compared all mapped package files with the audited source and checked the license. Other differences remain the [documented adaptations](../../adaptations/why.md): portable identity/invocation, catalog/configuration and lifecycle handling, source authority, citation and quotation rules, read-tool/schema checks, assigned-output writes, unavailable-source reporting and formatting. The local entrypoint, investigator and synthesizer templates, epistemics, source index and shared investigation contract are unchanged. No removed guide prose was moved into those files. Original source pins and the reviewed checkpoint remain unchanged.

## Reproduction

Reuse `limiter.py`, `source-control.md`, `chat.md` and `errors.md` from the existing [Why fixture](../investigation-restoration/fixtures/why). Copy these unchanged to owned scratch. These are synthetic archive exports, not live connector responses.

Question:

> Why is the batch limit 100? I assume we benchmarked it and proved the new limit stopped partner rejections. Use only the supplied Parcel archives and local code snapshot; do not contact anyone or change anything.

Fill the unchanged investigator template with this question, `limiter.py:1-4`, symbols `BATCH_LIMIT` and `allowed`, the supplied 50-to-100 change dated 2026-03-12, PR #41 and PAR-8. Append the updated category guide and incident guide. Run three fresh investigators, each reading only its own archive and the code anchor. Use the existing shared Findings and citations contract. Permit only separate assigned reports; prohibit live queries, source edits, application execution, configuration changes and further delegation.

After all three reports finish, inspect them and give them to a fresh synthesizer with the unchanged template and epistemics. Allow citation checks against these same archives. Mark issue tracker, long-form documents, infrastructure observability and product analytics as outside this bounded test's authorized evidence; do not claim they were searched or actually unavailable on the host.

Separately apply the entrypoint's pre-dispatch decision to a simulated environment with only the limiter snapshot, no Git history, no forge read access and an empty source-connector catalog. The authoring skill path and shared contract are supplied. Ask for the same historical explanation using only that environment record. This checks unavailable-source reporting, not actual host connector discovery. Limit output to one report and forbid external queries or installation.

Acceptance cases selected before dispatch: read the PR review beyond its misleading title; preserve the chat reply that reverses the apparent approval of 200; distinguish manual error resolution and regrouping from proof of a fix; report missing Seer analysis without starting it; cite evidence and qualify unverified partner rationale; retain all seven coverage categories, including gaps; and avoid empty investigator tasks or invented history when all historical sources are unavailable.

## Results

Five fresh native Codex contexts used inherited GPT-6-Astra/high: three source investigators, one synthesizer and one unavailable-source evaluator. Investigators ran concurrently with disjoint assigned reports. The synthesizer started after all three reached terminal completion and the parent inspected their findings. All five outputs were read and assessed against the authorized raw evidence.

| Case | Observed result |
| --- | --- |
| Misleading PR title | The history investigator read the full review, retained the original throughput framing and the author's correction, and distinguished a stated contract rationale from independent access to the contract. |
| Chat context reverses apparent approval | The chat investigator read the complete exported thread and rejected interpreting the casual 200 suggestion as approval after Sol's clarification. ADR-3 and PAR-1 remained unvisited cross-source leads. |
| Ambiguous incident/error correlation | The error investigator retained manual resolution, changed fingerprint, continued ERR-9 observations, unknown sampling and missing deployment mapping. It did not infer that PR #41 eliminated rejections. It also noticed the unverified relationship between the archived `limiter.check` and snapshot `allowed`. |
| Missing Seer analysis | The investigator reported that no existing analysis was supplied and used the primary archive instead. No new analysis was initiated. |
| Final synthesis | Rechecked all four evidence files, cited the recorded contract rationale, challenged the benchmark hypothesis and left rejection-rate effects unknown. All seven source categories were present, with four explicitly excluded by scope. No live search or full workflow completion was claimed. |
| All historical sources unavailable | Returned source mechanics only, an incomplete seven-category map and the pre-dispatch decision to create no investigator or synthesizer tasks. Unavailable sources were distinguished from empty searches and from a complete inline answer. |

All selected bounded acceptance cases passed. The parent checked decisive citations and protected hashes; fixture and operational instructions remained unchanged during evaluation. The unavailable-source test supplied its availability facts and prohibited real dispatch, so it validates the stated decision, not live discovery or enforcement of a dispatch guard. The three archive cases evaluate the updated guides with existing common instructions; they do not isolate the effect of each deletion.

## Checks and limits

Four packaging tests, skill validation, documentation consistency and diff checks pass. Raw prompts, findings, synthesis and hashes remain in task-owned cache. Reuse the existing fixture and retain only this report as new evaluation material.

The tests exercise authoring templates with inherited evaluation agents, not the saved investigator/synthesizer model assignments. They do not test live MCP schemas, authenticated search, full seven-source dispatch, installed discovery or all-provider behavior. Historical runtime evidence remains tied to its original files. No production defect or improved accuracy is claimed from these instruction deletions.

## Normal use

After merge and a manual skill update, ask `jstack-why`: "Why is our batch limit 100? Was it chosen for performance?" It checks the available history and separates recorded reasons from assumptions. A PR title about throughput is not enough when its review says the limit came from a partner contract. Missing sources remain visible gaps.
