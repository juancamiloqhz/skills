# Helper fidelity audit

Audit date: 2026-10-13. Local baseline: `d57d3407626f741900c9574b9ecd47421a8de96f`. This report covers `how`, `why`, `arena`, `architect`, `interrogate`, `swarm`, `reflect` and `figure-it-out`, including every file under their mapped upstream and local directories. The comparison found material, unnecessary compression and a missing standalone dependency. These helpers are implemented adaptations, but they are not close semantic copies of their pinned sources.

Only this report was written. No source, configuration, schedule, installation, upstream checkpoint or Git history was changed. No child work was delegated.

## Authority, sources and method

Read `AGENTS.md`, `research/jstack/upstream-fidelity.md`, the research skill and the writing guidance before comparison. The user's current instructions authorize this independent research and prohibit further delegation. The fidelity policy requires upstream structure, wording, principle grouping, trigger placement and substantive behavior unless a runtime incompatibility or explicit user requirement justifies a change. Earlier adaptation records describe choices; their existence does not approve those choices.

All eight mappings in `research/jstack/upstream.json` have the same exact `adaptedFrom` pin, **`11713c683fe4add4fd403ea880580abbc9e0875f`**, in `https://github.com/cursor/plugins.git`. In this report, **U** means that exact revision, never the branch tip or the manifest's `reviewedThrough` checkpoint. Paths written as `U:pstack/...` are exact Git object citations. Each component below also links to its pinned source directory. The manifest's initial revision is `ccb5507cec1546dc88135c1139c811e6c59115ba`; `reviewedThrough` is `4bf3e083c6dec126e254f96181b84a105b6e3e70`. Neither replaces the component pins. The setup mapping itself uses the initial revision; setup was inspected here only as a dependency and role-contract context, including its source at U as referenced by these helpers.

Used `git ls-tree -r --name-only U <upstreamPath>` and `git show U:<upstreamPath>/<file>` against `/home/ubuntu/.cache/jstack/upstream/upstream.git`. Read all mapped supporting Markdown files, not just entrypoints. Also inspected all three upstream `show-me-your-work` files, setup's upstream role contract, local configuration and T3 integration contracts, local `scripts/models.py`, and the seven upstream/local principle leaves used by Figure it out. Read existing difference records and evaluation READMEs; spot-checked structured evaluation results for their stated failures and limits. No upstream fetch or weekly change detection was needed.

`git rev-parse HEAD` matched the baseline. `git diff d57d3407626f741900c9574b9ecd47421a8de96f --` over the eight local packages and manifest was empty at inspection. Local citations below name baseline paths and line numbers. Concurrent parent edits to other research files are outside this report's ownership.

Dispositions used below:

| Disposition | Meaning |
| --- | --- |
| Necessary | A demonstrated T3/tool/host substitution, with behavior preserved as far as possible. |
| User-approved | Required by the user's stated preferences or recorded explicit decision. This does not authorize unrelated work. |
| Restore | Unnecessary drift. Restore the pinned structure or rule, retaining narrow runtime and authorization adaptations. |
| Pending implementation | A declared capability or dependency is not implemented. Do not report it as supported. |
| Needs decision | A material behavioral choice conflicts with another requirement or lacks evidence of approval. Do not silently adopt the local redesign. |

## Priority findings

1. **Restore Why's investigation playbooks and prompts.** All twelve supporting upstream files are absent locally. Seven categories and five confidence names survive, but the detailed search methods, source-specific traps, phrasing rules and output checks do not. A live tool schema cannot replace these instructions. See Why below.
2. **Restore standalone `show-me-your-work`, including its script and template.** Figure it out replaces a separately invocable helper with `references/decision-trail.md`. Upstream explicitly says consumers should reference that skill instead of restating its columns. The local package has no logger implementation. This conflicts with the user's standalone-helper requirement. Same-family review must still honor inherited configuration; that conflict needs an explicit adaptation, not a hidden model override.
3. **Restore substantive design and review rules.** Architect compresses three detailed references into short summaries and weakens isolation, invariant and boundary prescriptions. Interrogate replaces its rubric, reviewer prompt and code-quality lens with twelve lines of generic criteria. Review quality rules are not Cursor runtime assumptions.
4. **Resolve invocation-policy drift across all eight helpers.** Every upstream entrypoint has `disable-model-invocation: true`; every local entrypoint drops it and broadens discovery. The difference records call this Cursor-specific and necessary for playbook calls, but no inspected evaluation demonstrates that claim. Direct invocation, catalog visibility, an explicit workflow call and unsolicited model invocation are different questions.
5. **Move provenance to research, retaining licenses.** All eight packages carry `references/upstream.md`, and operational entrypoints direct readers to those records. This contradicts the current provenance policy. All eight package licenses are byte-identical to `U:pstack/LICENSE`, including Lauren Tan's notice, and should remain.

## Complete mapped-path inventory

All paths in the upstream column are relative to `U:pstack/skills/<component>/`; all local paths are relative to `skills/jstack/<component>/`. Every listed file was read. There are no mapped scripts hidden behind these eight upstream directories. The important script dependency is outside them, under `show-me-your-work`.

| Component | Every upstream path | Every local path | Supporting-path disposition |
| --- | --- | --- | --- |
| how | `SKILL.md`; `references/explainer-prompt.md`; `references/explorer-prompt.md` | `SKILL.md`; `LICENSE`; `references/upstream.md` | Restore both prompt files; retain package license; move provenance to research. Shared setup evidence/config contract is an approved dependency, not a substitute for those prompts. |
| why | `SKILL.md`; `references/epistemics.md`; `references/investigator-prompt.md`; `references/source-playbook.md`; `references/synthesizer-prompt.md`; `references/sources/code-archaeology.md`; `references/sources/databricks.md`; `references/sources/datadog.md`; `references/sources/incident-postmortem.md`; `references/sources/linear.md`; `references/sources/notion.md`; `references/sources/sentry.md`; `references/sources/slack.md` | `SKILL.md`; `LICENSE`; `references/upstream.md` | Restore all twelve supporting files, adapting callable tool names and authorization narrowly. Keep shared setup contract, license and research provenance. |
| arena | `SKILL.md` | `SKILL.md`; `LICENSE`; `references/execution.md`; `references/upstream.md` | Execution reference is necessary T3 support; restore upstream phase names/organization and principle pointers; keep license; relocate provenance. |
| architect | `SKILL.md`; `references/design-red-flags.md`; `references/rationale-template.md`; `references/runner-prompt.md` | `SKILL.md`; `LICENSE`; `references/design-red-flags.md`; `references/rationale-template.md`; `references/runner-prompt.md`; `references/upstream.md` | All source paths survive by name, but their contents are substantially compressed. Restore substantive reference instructions; retain license and relocate provenance. |
| interrogate | `SKILL.md`; `references/code-quality-review.md`; `references/lead-judgment.md`; `references/reviewer-prompt.md`; `references/rubric.md` | `SKILL.md`; `LICENSE`; `references/execution.md`; `references/lead-judgment.md`; `references/review-criteria.md`; `references/upstream.md` | Restore three missing references and expanded lead framework. `review-criteria.md` is a replacement abstraction, not upstream packaging. Retain necessary execution support/license; relocate provenance. |
| swarm | `SKILL.md` | `SKILL.md`; `LICENSE`; `references/execution.md`; `references/upstream.md` | Runtime reference is necessary; phase algorithm mostly survives. Model races remain unsupported locally. Restore section/trigger fidelity; retain license; relocate provenance. |
| reflect | `SKILL.md`; `references/divergent-reviewer.md`; `references/judgment-reviewer.md`; `references/synthesizer.md`; `references/tooling-reviewer.md` | `SKILL.md`; `LICENSE`; `references/assessment.md`; `references/execution.md`; `references/upstream.md` | Restore four separate templates. `assessment.md` consolidates their content without runtime necessity. Keep execution support/license; relocate provenance. |
| figure-it-out | `SKILL.md` | `SKILL.md`; `LICENSE`; `references/decision-trail.md`; `references/execution.md`; `references/principles.md`; `references/upstream.md` | Principle discovery is user-approved; execution support is necessary. Restore separate audit-trail phase and standalone trail-helper boundary. Retain license; relocate provenance. |

The added `LICENSE` files are a correct package-level adaptation from the upstream plugin-level license. File counts establish inventory coverage only. They do not establish equivalent behavior.

## Shared dispositions and conflicts

### Model resolution and lifecycle

**Necessary / user-approved.** Replacing `Task`, Cursor model slugs, `.mdc` lookup, `readonly` mode assumptions and cloud flags with actual T3 capabilities is justified. The user's role configuration and inheritance override upstream fixed defaults and rejected-slug fallback. Local `skills/jstack/setup-jstack/scripts/models.py:98` validates concrete catalog choices; `:126` validates the complete map; `:150` returns null for inherited seats. These support the helper instructions to omit inherited targets and pass concrete options unchanged. Keep manual dependency installation, explicit config-path handoff, fresh review tasks, retained task IDs, terminal-state checks and owned workspaces. They preserve actual authorization and T3 ownership semantics.

Evidence locations include `skills/jstack/how/SKILL.md:10`, `why/SKILL.md:10`, `arena/references/execution.md:13`, `interrogate/references/execution.md:13`, `swarm/references/execution.md:13`, `reflect/references/execution.md:13`, `figure-it-out/references/execution.md:5`, all under `skills/jstack/`. Upstream counterparts are the model paragraphs in each `U:pstack/skills/<name>/SKILL.md` and the role table in `U:pstack/skills/setup-pstack/SKILL.md`.

Whole-map validation and one inherited seat per default panel can block Arena/Architect without user configuration changes. This is a consequence of the current configuration design, not permission to invent extra seats. Saved user choices are approved; first-run panel cardinality and whole-map blocking remain separate policy questions in the foundation audit. It should be disclosed during setup or invocation. Upstream's two default runners do not authorize changing saved local settings.

**Necessary, with a verification limit.** Serializing writers until assigned-path behavior is established protects a shared T3 workspace. This replaces upstream same-message parallel dispatch in How, Why, Arena, Interrogate, Swarm and Reflect. The correct long-term behavior is concurrent independent work once isolation and capacity are demonstrated. Evaluations mostly used serial writers; they do not establish that parallelism is impossible. Keep the condition rather than turning it into a permanent serial algorithm.

### Invocation, activation and discovery

**Needs decision.** All eight upstream frontmatters disable model invocation. All eight local `SKILL.md:1` frontmatters omit that key, and their `description` values are rewritten. `how/references/upstream.md:5`, `why/references/upstream.md:5` and the other records justify normal discovery by future playbook calls. That is an assertion about host behavior, not demonstrated necessity. Restore upstream trigger phrases and placement where compatible. Establish whether each supported provider can expose explicit-only skills to an explicitly selected caller; if it cannot, document the smallest adapter or exception. Do not assume removal is required merely because catalog discovery is required.

Verify using an ordinary matching request, explicit `/helper` request, explicit workflow call and mere authoring read on each supported provider. Record which activates a helper, which leaves it discoverable, and whether an already active juan-mode survives. These are future checks, not checks performed here. Installed discovery was not exercised by the inspected evaluations.

**User-approved.** Direct helper use must leave juan-mode activation unchanged. Most entrypoints state this explicitly at line 8; How and Why say they do not activate it. This is compatible with `skills/jstack/juan-mode/SKILL.md:8` keeping an active mode until opt-out. Do not turn task-scoped helper use into a mode reset. Keep standalone helper packages and the standalone principles. Figure it out's selective leaf discovery is expressly approved by `research/jstack/upstream-fidelity.md`, even though its upstream Start reads poteto-mode's full Principles section. It does not justify removing the inline principle groups from juan-mode.

### Provenance and authority

**Restore.** Move each package's `references/upstream.md` to `research/jstack/`, update all eight manifest `differences` fields, and remove operational provenance-only pointers. Affected entrypoints are `how/SKILL.md:12`, `why/SKILL.md:12`, `arena/SKILL.md:8`, `architect/SKILL.md:8`, `interrogate/SKILL.md:8`, `swarm/SKILL.md:8`, `reflect/SKILL.md:8` and `figure-it-out/SKILL.md:42`, all under `skills/jstack/`. Keep every `LICENSE`. Verify all moved mappings resolve and that installed package discovery uses metadata rather than an Attribution paragraph. Do not advance any source pin or checkpoint for this move.

**User-approved.** Preserve manual installs, separate merge authority and no unsolicited external messages. Do not copy upstream Reflect's automatic backlog filing or Interrogate's unsolicited PR to fix model defaults. Already granted task authority can cover reversible edits; no new approval is needed merely because a helper ends a phase. Explicit checkpoints still bind. These requirements do not justify unrelated weakening of source algorithms.

## How

Source: [pstack How at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/how). Material source paths are `U:pstack/skills/how/SKILL.md` and both prompt references in the inventory.

**Preserved.** The simple path uses one explainer, while the complex path uses two to four explorers followed by one explainer. Scope interpretation, evidence gathering, source checking, light presentation edits and the mechanics-versus-history distinction remain in `skills/jstack/how/SKILL.md:16`, `:18`, `:22`, `:26` and `:28`.

**Restore.** The two prompt templates and numbered Assess / Explore / Synthesize / Present structure were replaced by three short sections. Upstream's explicit "when in doubt, take the simple path" is missing. The explainer's Overview, Key Concepts, How It Works, Where Things Live and Gotchas structure, senior-engineer audience, prose-over-pseudocode rule, concrete file/function language and concise-versus-complex explanation guidance are absent. The explorer's ordered entrypoint, flow, abstraction, boundary and non-obvious-behavior investigation is compressed into one paragraph. Its structured Components Found / Flow / Files Read / Boundaries / Non-Obvious Things / Open Questions output is lost. Local `:26` permits a diagram and a file map but does not preserve those contracts.

**Necessary / user-approved.** Catalog-discovered setup, a shared evidence contract, role configuration, scoped findings files and no automatic implementation are appropriate. The 2026-10-12 explicit standalone decision in `research/jstack/decisions.md:39` also approves setup ownership of shared evidence guidance. This does not approve deleting How's prompt templates.

Correction and verification: restore both templates and the original procedure order; substitute actual read tools and configured roles in place. Run an ambiguous narrow question to verify the simple-path default, and a cross-component question to verify two-to-four independent exploration outputs, synthesis ordering, complete file inventory and uncertainty. Inspect generated briefs and explanation sections, not only a correct final answer. Existing serial source-tracing fixtures are useful regression inputs but do not cover the restored presentation or parallel behavior.

## Why

Source: [pstack Why at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why). All thirteen upstream paths are enumerated above.

**Preserved.** Local `skills/jstack/why/SKILL.md:16` retains history through renames, blame, pickaxe, patches and PR/ticket follow-up. `:18` through `:30` retain seven-category coverage and empty/unavailable results. `:34` through `:42` preserve investigators before synthesis, cross-category leads, contradictions, confidence separation and preserve/change/avoid/risk constraints. Setup's `references/investigation.md:29` through `:41` retains the five confidence levels, independent corroboration, no intent inferred from mechanics, hypothesis checking and source verification.

**Restore, high impact.** Deleting every supporting file removes source-specific procedures, not merely obsolete MCP names. `why/references/upstream.md:7` says live schemas replace provider-specific playbooks, but schemas explain tool arguments, not investigative reasoning. Restore these particular losses:

| Missing source at U | Substantive behavior to restore |
| --- | --- |
| `pstack/skills/why/references/epistemics.md` | Tier-specific language and examples; prohibit confidence words for unsupported intent; avoid retrofitting clean motives; audit every final claim for its tier, citation and gaps. |
| `pstack/skills/why/references/investigator-prompt.md` | Wide search before narrowing; full-document/thread reads; follow links only within assigned source; verbatim queries; alternative readings and the counterfactual check on strong evidence; gather evidence without prematurely choosing the final answer. |
| `pstack/skills/why/references/synthesizer-prompt.md` | Explicit final sections, inference chains, evidence for and against competing hypotheses, specific failed searches, per-source scope details, confidence summary and seven-item quality check. Local `SKILL.md:40` preserves concepts but not this procedure. |
| `pstack/skills/why/references/source-playbook.md` | The category-to-playbook routing table and separate cross-cutting incident playbook. Adapt examples to the installed connector rather than removing the methods. |
| `pstack/skills/why/references/sources/code-archaeology.md` | Co-change evidence, related tests, ADRs/TODOs/release notes; full PR comments and reviews; squash-merge fallback, copied-pattern origins and misleading commit-message checks. |
| `pstack/skills/why/references/sources/databricks.md` | Discover schema before SQL; poll existing statement IDs rather than rerun; typed/deduplicated model preference; before/after windows; threshold percentiles; flag exposure; query-history and lineage methods; instrumentation/schema changes, refresh lag and retention versus null results. |
| `pstack/skills/why/references/sources/datadog.md` | Find owner/service, inspect dashboards and monitors before metrics/logs/traces/incidents, retain query/threshold/owner/time metadata; distinguish retention gaps and instrumentation from causal rationale. |
| `pstack/skills/why/references/sources/incident-postmortem.md` | Specific incident queries in each source and full postmortem action-item linkage. Local `SKILL.md:30` retains only general incident terms and correlation caution. |
| `pstack/skills/why/references/sources/linear.md` | Linked ticket first, parent/subissue tree and project documents; labels/milestones; scope changes, stale plans, boilerplate and duplicate chains. |
| `pstack/skills/why/references/sources/notion.md` | Full page, backlinks, child pages and related databases; finalized versus draft documents; shipped-code divergence and access gaps. |
| `pstack/skills/why/references/sources/sentry.md` | Stack relevance, release trajectory, regrouping, sampling, manual resolution versus a fix, and AI-generated root cause as hypothesis rather than authority. |
| `pstack/skills/why/references/sources/slack.md` | Author/date/PR/error/channel searches, complete thread traversal, retention and inaccessible-DM limits, and casual remarks distinguished from actual decisions. Read access does not authorize sending messages. |

**Necessary.** Remove the upstream assumption that Git and `gh` are always available. Use actual connector schemas, authorized project scope and bounded queries. Read-only intent should not use a provider mode that strips required read tools. Authorized short excerpts or accurate paraphrases can satisfy evidence needs without copying every source verbatim.

**Restore / needs decision.** Upstream says a source must be *provably* irrelevant before skipping and requires written justification. Local `:30` says "irrelevant" with a concrete reason, a weaker bar. Restore the high relevance threshold within authorized scope. Upstream also permits a rare inline answer only after all seven searches are shown redundant; local `:34` and `:40` always require configured investigator/synthesis phases for readable sources. Restore that narrow exception unless the user intentionally wants compulsory delegation. The upstream wording has tension between one investigator per category and one tool/MCP per investigator. Local `:34` permits explicit partitioning when multiple sources serve a category. Preserve complete coverage, but document the chosen partition rule rather than claiming exact equivalence.

Correction and verification: restore the complete reference tree and pass the right playbook into each investigator brief. Use fixtures where an answer in the first PR is contradicted by a full review thread, a ticket's parent changes the rationale, telemetry predates retention, error regrouping mimics a fix and analytics instrumentation changes mimic product changes. Verify those traps remain visible in the final confidence-weighted output. Existing local-history tests do not exercise live external sources or these methods.

## Arena

Source: [pstack Arena at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/arena), `U:pstack/skills/arena/SKILL.md`.

**Preserved.** A hidden three-to-six criterion rubric, independent candidates, frozen outputs before one judge, coordinator scoring during judging, disagreement inspection, smaller-interface tie-break, coherent contributions from losing candidates, convergence, reframe-on-divergence and final verification survive in `skills/jstack/arena/SKILL.md:12` through `:42`.

**Necessary / user-approved.** Fixed configured seats, an architect runner override, inheritance, fresh contexts, candidate ownership, no implicit implementation and manual setup dependencies are appropriate. Upstream cross-family judging is a preference, not an absolute requirement. Local `:14` correctly permits same-family judging with disclosure unless the caller requires diversity. Do not flag that as a missing upstream mandate.

**Restore.** Frame / Fan out / Cross-judge / Pick / Graft / Verify was renamed and partly merged. `:24` combines judging and picking; `:30` renames Graft to Synthesize. This has no demonstrated runtime need. Restore the original section organization and references to `principle-separate-before-serializing-shared-state`, `principle-laziness-protocol`, `principle-redesign-from-first-principles` and `principle-prove-it-works`, using catalog discovery. Local summaries preserve much of their immediate behavior but stop directing the agent to the standalone principles.

**Needs decision.** Local `:14` and `:22` impose at least two viable candidates, including after dropout. Upstream says proceed with N-1 and report the dropout, without that lower bound. Keeping the label "comparison incomplete" with one survivor is reasonable, but forbidding the remaining artifact's synthesis is a stricter policy. Record that choice explicitly. Upstream also allows more runners for multiple directions and repeated same-model generation; the local no-added-seats rule follows configured panel ownership. Keep user-approved seat counts rather than copying upstream autonomous expansion.

Correction and verification: preserve the six phases and explicit principle routes. Test two candidates with one dropout and document whether the result is a useful partial artifact or a stopped comparison. Verify rubric creation precedes reading any candidate, and judge dispatch follows all candidate writes. The later Architect runtime evaluation recorded rubric creation after reading a candidate; it is evidence of a procedural failure, not approval to reorder Arena.

## Architect

Source: [pstack Architect at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect). The entrypoint and all three supporting sources matter.

**Preserved.** How grounding, conditional Why grounding, greenfield exception, Arena with `architect runners`, two structurally distinct designs, usage-first output, optional checkpoints and repeated-friction redesign survive in `skills/jstack/architect/SKILL.md:16` through `:36`.

**User-approved.** `SKILL.md:10` distinguishes a design-only task, an explicit checkpoint and already authorized implementation. This narrows upstream's default-to-implementation behavior to the user's actual request and avoids redundant approval when implementation is already authorized. It is appropriate. Protecting unrelated work during reconsideration is also required; "scrap the sketch" does not authorize a destructive reset. Preserve the option of an authorized scaffold commit; separate merge authority still applies.

**Restore.** Same filenames mask substantial reference drift:

| Local location | Exact source at U and lost behavior |
| --- | --- |
| `skills/jstack/architect/references/runner-prompt.md:5` | `pstack/skills/architect/references/runner-prompt.md`: caller usage is the spec; reconcile types to usage rather than the reverse. Dominant access-pattern tracing survives, but the explicit reject-"add a map/index/cache later" test is softened. |
| `skills/jstack/architect/references/runner-prompt.md:7` | Same source: default to per-actor state and merge at the read boundary if concurrent writes have an effect. Local single-owner/compare-actors guidance is a different default. Restore isolate-before-serialize. |
| `skills/jstack/architect/references/runner-prompt.md:7` and `:9` | Same source: keep wire types off the public API, parse them into domain types, validate at boundaries and trust types inside; business logic is pure and shell thin. Local conditions about independent change and reduced caller obligations weaken those prescriptions. |
| `skills/jstack/architect/references/runner-prompt.md:11` | Same source: flatten when tracing flow requires more than three files; explicit principle citations; read Architect in full before producing a candidate; make a whole design rather than hedge toward the other models. The local short-interface summary drops these instructions. |
| `skills/jstack/architect/references/design-red-flags.md:3` and `:5` | `pstack/skills/architect/references/design-red-flags.md`: eight diagnostic sections explain mechanisms and remedies. The table drops much of that reasoning. Hand-synced lists require a build failure when not derivable, not merely a potentially meaningful check. |
| `skills/jstack/architect/references/design-red-flags.md:12` and `:13` | Same source: move callers and delete duplicate routes in the same change; make internal imports fail the build. Scope, real external compatibility and language enforcement limits justify narrow exceptions, not replacing the default with general discretion. |
| `skills/jstack/architect/references/rationale-template.md:5` through `:11` | `pstack/skills/architect/references/rationale-template.md`: restore actual Problem / Usage / Shape / Synthesis decision / Tradeoffs / Alternatives / Questions / Next-step sections. Restore "we accept X in exchange for Y," explicit interface-depth comparison, principle citations and the distinction between alternatives within a candidate and competing runner outputs. |
| `skills/jstack/architect/SKILL.md:36` | `pstack/skills/architect/SKILL.md`, Phase E: two independent same-shape deviations, unrelated special-case branches, data complexity versus design complexity, redesign with new constraints as day-one assumptions and subtract-before-add sequence are compressed. Restore the diagnostic list and ordered Scrap steps. |

**Needs decision.** A fixed three-file flattening heuristic and strict one-route rule can be debated, but T3 does not require their removal. Restore upstream defaults with narrow repository/compatibility exceptions, or get an explicit redesign decision. Likewise, local `SKILL.md:30` limits Interrogate to an explicitly requested review, while upstream Phase C offers it for adversarial pressure without that added condition. Actual delegation authority governs; do not silently rewrite a workflow option into a universal user-request requirement.

Correction and verification: diff every restored reference against U, allowing only recorded substitutions. Evaluate a candidate that hides transport types poorly, one that uses a shared lock where independent state would work, and one whose usage requires changing its own type sketch. Require the original remedies and rationale fields. Exercise the repeated-friction Scrap loop and checkpoint continuation; current runtime evidence covers implementation and checkpoint stop, not those branches.

## Interrogate

Source: [pstack Interrogate at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate). All four references are substantive.

**Preserved.** Pinned review scope, one common intent, configured reviewer seats without personas, independent findings, severity/location/evidence, duplicate merging, four lead categories, agreement map and report-only behavior survive in `skills/jstack/interrogate/SKILL.md:12` through `:30`. A valid single inherited reviewer cannot establish cross-model diversity; local disclosure correctly honors configuration.

**Restore, high impact.** `references/review-criteria.md:5` through `:12` is not equivalent to upstream `references/rubric.md` and `references/code-quality-review.md`. Restore the original files, reviewer prompt and section organization. Specific lost checks include off-by-one/coercion/overflow/encoding, stale closures/dangling references, post-crash reconciliation, structural concurrency controls, a regression test for a bug, full integration-path tests, actual liveness versus cached proxies, dead/vestigial code, completed-migration cleanup, user-experience justification for complexity, and explicit SQL/shell/eval/HTML sinks, authorization gaps, secrets and security TOCTOU. Generic correctness/security bullets are not a substitute for these prompts.

Restore the ambitious structural quality lens, ordered priority of findings, unnecessary serialization check and explicit presumptive blockers. The local file says a large file warrants inspection rather than a rewrite; upstream's actual rule is more nuanced than a blanket limit: crossing 1,000 lines is a strong smell/presumptive blocker that permits a compelling structural justification. `skills/jstack/interrogate/references/upstream.md:9` also describes upstream compatibility deletion as blanket, but `U:pstack/skills/interrogate/references/rubric.md` explicitly conditions deletion on having no external consumers. Those adaptation rationales overstate the source and should be corrected.

**Restore / needs decision.** Local `references/lead-judgment.md:12` removes the five-item calibration warning as though it were a hard blocker cap. Upstream `references/lead-judgment.md` says more than five items *probably* means insufficient filtering; it does not require hiding real blockers. Restore that calibration and detailed false-positive checks while retaining all real defects. Local evidence-based scrutiny of singleton security/correctness reports is consistent with upstream's explicit singleton exception. Removing all consensus weighting, however, is broader than needed; independent convergence can remain a signal without overriding evidence.

**Necessary / user-approved.** Use the actual merge-base rather than assuming `main`. Review design artifacts honestly as designs. Do not create a separate external PR to repair a rejected default model as upstream Step 3 instructs; preserve configured choices and report the prerequisite. No automatic fixes or merges.

Correction and verification: restore the three missing references and complete lead framework, with narrow runtime edits. Test a justified large-file exception, needless complexity with correct behavior, an externally consumed compatibility route, a lone reachable security defect and more than five real blockers. Verify the lead does not suppress defects, mistake source guidance for a blanket ban or label generic preferences as bugs. Existing two-defect and no-findings cases do not cover those dimensions.

## Swarm

Source: [pstack Swarm at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/swarm), `U:pstack/skills/swarm/SKILL.md`.

**Preserved.** Frame / Fan out / Aggregate / Report, partition/race/mix, total worker count separate from capacity, declared first-pass/rank-all/best-of rule, pinned SHAs and measurement method, PASS/ISSUES/BLOCKED, report all supported issues, one retry for missing required evidence and explicit coverage gaps survive in `skills/jstack/swarm/SKILL.md:12` through `:36`. This is the closest procedural adaptation among the eight.

**Necessary.** Actual T3 capacity, explicit source checkouts, child lifecycle, verified first-pass selection, cancellation/draining and integration checks replace Cursor cloud/local flags and `cloud_base_branch`. Do not preserve literal Cursor dispatch fields. Do preserve the ability to give a worker the intended non-default source revision. The coordinator's acceptance check is consistent with upstream aggregation; it is not a reason to trust worker summaries less explicitly upstream.

**Pending implementation / needs decision.** `SKILL.md:16` rejects distinct-model races because local `swarm workers` is scalar. `U:pstack/skills/swarm/SKILL.md`, Frame step 4, says to name each race arm's model; `U:pstack/skills/setup-pstack/SKILL.md`, step 3(c), explicitly makes that scalar a default overridden by an assigned race/comparison arm. A scalar role alone is therefore not source evidence that model races are invalid. Preserve saved settings and never invent models, but distinguish an explicitly authorized per-arm override from an invented one. Decide how a task can supply catalog-validated per-arm selections, or disclose model races as a deliberate unsupported upstream feature.

**Restore.** Restore original Start/phase organization and trigger wording rather than treating a total rewrite as portability. Most added ownership/evidence clarifications can remain as a concise T3 contract without replacing the source algorithm.

Correction and verification: retain the existing two-worker fixtures, add missing-evidence retry/dropout, first-pass cancellation, best-of and mixed coverage/race cases. Add a requested distinct-model race with explicit selections, including an unavailable arm and inheritance. Do not claim this works before the override decision and runtime checks exist. Current evidence exercised serial same-model coverage and rank-all designs only.

## Reflect

Source: [pstack Reflect at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/reflect). All four reviewer/synthesis templates were inspected.

**Preserved.** Three distinct lenses with two scalar roles, one separate synthesizer, current-session evidence, untrusted transcript handling, existing-skill-first routing, missed-trigger versus body edits, structural enforcement and Accepted/Rejected/Backlog remain in `skills/jstack/reflect/SKILL.md:12` through `:38` and `references/assessment.md:3` through `:27`.

**Necessary / user-approved.** T3 current-thread reads or a labeled digest replace Cursor transcript-directory commands. Manual installs and available authoring guidance replace built-in Cursor assumptions. Do not restore upstream automatic backlog filing. Keep explicit checkpoints, but use existing edit authorization instead of requesting it again. This satisfies the user's no-unsolicited-message and autonomy constraints.

**Restore.** The four independently passed templates became one summary reference. Upstream explicitly passes reviewer and synthesizer templates verbatim. Restore their boundaries and substantive scan lists: decisions that worked for the wrong reason, verification skipped or deferred, caller/downstream effects, architectural symptoms, workflow friction, repeated manual actions, package-manager/sandbox surprises and concrete debugging entry points. Local `references/assessment.md:7`, `:11` and `:15` cover categories but lose concrete cues. Restore exact routing forms, rejected reason codes, the compact Accepted table and the six-month durability test from `U:pstack/skills/reflect/references/synthesizer.md`. Keep examples only where applicable; do not turn upstream illustrative convention examples into new repository requirements.

**Needs decision.** Upstream tooling review says flag every manual context handoff the agent could fetch; local `assessment.md:11` makes this merely something to consider. Authorized-source checks are necessary, but do not require weakening that search instruction. Upstream also gives repeated findings higher confidence and singleton findings a higher bar. Local `:27` preserves evidence but omits the higher-bar rule. Restore the source rule, or explicitly choose a different evidence-weighting policy. Local `SKILL.md:28` rejects already effective enforcement, whereas upstream sends already-enforced or cheaply enforceable mechanisms to Backlog. Avoiding duplicate effective machinery is reasonable, but it is a behavioral correction requiring an explicit disposition rather than a claimed literal port.

Correction and verification: restore templates and pass complete bounded evidence to each. Test missed triggers, weakly placed existing guidance, genuinely already-covered rules, manual context handoffs and a strong singleton. Keep a poisoned transcript instruction and unauthorized tracker write as negative cases. The current synthetic run supports assessment behavior and no automatic changes, not application, live transcript retrieval or description tuning.

## Figure it out and the missing trail helper

Source: [pstack Figure it out at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/figure-it-out), `U:pstack/skills/figure-it-out/SKILL.md`; external dependency [Show me your work at U](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work).

**Preserved.** Falsifiable done predicate, quantified scope, risk-based rigor, riskiest-unknown-first planning, before/after evidence, architecture before consequential commitments, per-unit hypothesis/check, VERIFIED/NOT VERIFIED/INCONCLUSIVE, actual artifact checks, append-only trail and final product verification survive in `skills/jstack/figure-it-out/SKILL.md:14` through `:40`.

**User-approved / necessary.** Discover the seven standalone principles instead of requiring juan-mode's body. Keep planning-only return, current-thread evidence boundaries, actual configured review, manual installs and separate delivery/merge authority. Use existing checks when they already provide the necessary verification rather than constructing an unnecessary harness. Recovery must preserve unrelated work; no automatic rebase/reset is justified by a principle reference.

**Restore, high impact.** `skills/jstack/figure-it-out/references/upstream.md:7` openly replaces standalone Show me your work with a bundled reference. This conflicts with `U:pstack/skills/show-me-your-work/SKILL.md`, "Composing this skill," which requires consumers to route to that helper by name and not restate its columns. Its standalone invocation is missing entirely from `skills/jstack/`, and the manifest has only a context path rather than a mapped implementation.

| Every upstream trail-helper path at U | Local accounting and correction |
| --- | --- |
| `pstack/skills/show-me-your-work/SKILL.md` | Partially summarized by `skills/jstack/figure-it-out/references/decision-trail.md:1`. Restore as an independently invocable helper, retain one canonical log and its source boundary, and map it explicitly. |
| `pstack/skills/show-me-your-work/references/decision-log-template.tsv` | Header copied into `decision-trail.md:9`; actual template absent. Restore the distributable template. |
| `pstack/skills/show-me-your-work/scripts/log.sh` | No local corresponding implementation. `decision-trail.md:15` tells the agent to use a serializer instead. Restore the tested reusable helper rather than requiring each execution to implement one. |

The script implements six-argument validation, parent-directory creation, UTC timestamps, header creation with append rather than truncation, tab/newline/carriage-return normalization, spreadsheet-formula prefixing and append-only rows. The local prose preserves some of the contract but does not implement it. The script's append-on-first-use safeguard is absent from the local description. Existing Figure it out evaluation recorded a shell continuing after an assertion failure and false success rows later corrected; that does not prove the upstream logger would fix the failure, but it demonstrates why prose instructions and a passing product test are not proof of trail correctness.

**Restore.** Upstream Phase D is an explicit audit-trail phase woven through Phase C, not a reason to log late. Local `SKILL.md:30` starts the trail at the correct time but removes Phase D as a named phase. Restore the original phase organization and reference the standalone helper. Restore its preference for evidence from committed scripts, bounded audit of only this run's timestamp stretches and the prescribed Attention handoff section. Local `decision-trail.md:17` preserves most handoff logic; `:19` says this run's rows but drops the explicit start-to-next-run interval algorithm. Keep the exact algorithm so a resumed coordinator does not audit or rewrite another run's claims as its own.

**Needs decision.** Upstream Show me your work requires a different model family for trail review and an Attention section on every reply of a run that produced a trail. Local `decision-trail.md:21` instead uses the inherited `judgment and prose` role and permits same-model review. Honoring the saved role is user-approved; silently changing it to enforce diversity is prohibited. Explicitly document reduced independence or agree on a user-authorized review selection. Do not call same-family review equivalent to upstream cross-family review. The Attention format can be restored independently of the model choice.

**Restore / needs decision.** Figure it out's upstream Phase C pairs delegated work with a judge; local `SKILL.md:34` requires a separate reviewer only for consequential delegated work. This is a narrowed review gate, not a T3 necessity. Upstream Frame also says rigor is biased high and gives a multi-hour run one checkpoint; local `:14` and `:16` replace that with consequence-based scope/resource settlement. Avoid redundant permission when the run is already authorized, but retain an explicit framing checkpoint before an unapproved long run. Record the narrowed judge gate and omission of high-rigor bias as decisions if retained.

Correction and verification: restore the standalone helper and all three files, map and license it, then make Figure it out call it. Verify logger argument errors, first and later appends, nested output directories, embedded CR/tab/newlines, all four formula prefixes and preservation of existing rows. Exercise alternating coordinator `start` rows and ensure each audit covers its own stretches. Verify every decision evidence pointer resolves, false rows receive corrections and a configured same-family reviewer is disclosed without a model override. These corrections were not performed in this audit.

## Dependency closure and pending scope

The mapped packages have no local scripts of their own. All eight rely directly or through Arena/Architect on catalog-discovered `setup-jstack` for delegation. Inspected local dependency paths are `skills/jstack/setup-jstack/references/configuration.md`, `references/t3-code.md`, `references/investigation.md` and `scripts/models.py`. The shared investigation contract is used by How and Why. Setup's writer exists but no helper is authorized to call it to repair settings. This was source inspection, not an independent full setup audit.

Architect calls How, conditional Why and Arena, and exposes optional Interrogate. Those packages exist separately. Figure it out calls Architect only for consequential unresolved design and discovers these seven standalone packages: `principle-prove-it-works`, `principle-never-block-on-the-human`, `principle-foundational-thinking`, `principle-laziness-protocol`, `principle-separate-before-serializing-shared-state`, `principle-sequence-verifiable-units`, `principle-encode-lessons-in-structure`. Each upstream directory contains only `SKILL.md`; each local package contains `SKILL.md` and `LICENSE`. Their bodies were read for dependency context, not counted as a complete principle audit. Compression in those leaves can weaken helpers transitively; the separate principle audit owns those corrections.

Upstream Arena additionally routes to redesign-from-first-principles; Architect routes to exhaust-the-design-space, foundational-thinking, outcome-oriented-execution, fix-root-causes, subtract-before-you-add, boundary-discipline, make-operations-idempotent and minimize-reader-load among its principle references. Their local standalone names exist in the manifest, but helper summaries no longer preserve all explicit routes. Restore catalog-discovered principle pointers at the original decision points. Do not require a juan-mode installation merely to read a leaf. Upstream Show me your work also invokes `unslop`; the repository has that writing skill, but the restored helper should discover it rather than assume an installation path.

**Pending implementation.** The 23 juan-mode playbooks remain registered but unavailable at `skills/jstack/juan-mode/SKILL.md:10`. Existing helpers do not implement those routes or demonstrate persistent activation across compaction/restart. Preserve this limit. The missing standalone trail helper and Swarm model-race support are specific gaps identified here, not a request to implement every upstream helper. Do not treat older manifest decisions saying these helpers have no counterpart as current inventory truth; they are historical checkpoint records whose dates and pins must remain intact.

## Evaluation evidence and limits

The following records were used to distinguish observed runtime behavior from adaptation claims. They are evidence of bounded prior tests, not new tests executed for this audit and not proof of upstream equivalence.

| Record under `research/jstack/evaluations/` | What it supports | Limits relevant to correction |
| --- | --- | --- |
| `shared-investigation/README.md`, `remaining-cases.json` | Simple/complex How, history/contradiction Why, explicit project-config handoff and failed prerequisites. | Serial inherited Codex exploration; no live external source methods or provider UI discovery. |
| `arena/README.md`, `results.json` | Two candidates, one judge, useful synthesis; one-seat and mandatory-family failures stop before dispatch. | Design-only, serial inherited seats; no successful cross-family judging, dropout or code-worktree case. |
| `architect/README.md`, `runtime/README.md`, `runtime/implementation.json` | Grounding and recovered design comparison; authorized implementation and explicit checkpoint stop. | First design round had cancellation/incomplete brief; later private rubric was recorded after reading a candidate. Scrap loop and checkpoint continuation remain untested. |
| `interrogate/README.md`, `code-results.json` | Seeded defects, report-only handling and single-reviewer design case. | No input drift, failed reviewer, explicit disagreement, false-positive dismissal or external-provider evidence. |
| `swarm/README.md`, `coverage-results.json` | Same-model serial coverage and rank-all design race. | Scope deviation in discovery; retry only tabletop; cancellation, best-of, mixed shapes, measurement and integration untested. |
| `reflect/README.md`, `results.json` | Three lenses then synthesis, all ten findings accounted for, no unauthorized edits/filing. | Synthetic digest; no live transcript retrieval, authorized application, description tuning or failed-child recovery. |
| `figure-it-out/README.md`, `execution-results.json` | Planning-only boundary and working CSV product with separate trail review. | False preservation/audit success rows after a failed assertion were corrected later. Same-model digest-based review; no full transcript or delegated implementation case. |

The static comparison is complete for every path under the eight mapped component directories and all three paths of the omitted trail dependency. Material procedure, structure, trigger, wording and packaging differences are accounted for above. This is not a claim of full semantic equivalence, an exhaustive audit of every transitive principle or setup implementation, or a complete runtime support matrix. No live connector queries, provider installations, parallel workflow experiments or full archived child transcript audits were performed.

## Correction sequence and unresolved decisions

1. Restore missing reference trees and substantive instructions in How, Why, Architect, Interrogate and Reflect from U. Preserve necessary T3 substitution paragraphs separately and narrowly. Review complete file diffs against U, not just local before/after diffs.
2. Restore standalone Show me your work with script/template/license and map it in the manifest. Update Figure it out to call it and preserve the original phase sequence. Keep the approved standalone-principle discovery.
3. Move provenance-only files to research and repair manifest paths without changing pins, historical records or licenses.
4. Restore original phase names and explicit principle routes in the less-divergent helpers. Retain workspace ownership and lifecycle corrections.
5. Resolve invocation metadata behavior; Arena's one-survivor outcome; Swarm's explicit per-arm model overrides; strict design/review heuristic exceptions; Reflect's convergence/enforcement routing; Figure it out's reduced judge gate; and trail review diversity under inherited configuration. Default to source behavior where it does not conflict with user authority. Record any retained redesign as an explicit decision.
6. Run the focused correction checks described per component. Reuse historical fixtures, but add cases for restored algorithms and inspect the actual briefs, artifacts and phase order. Keep runtime uncertainty visible until demonstrated.

No correction in this list has been applied by this research task. The report is complete and has no pending child work.
