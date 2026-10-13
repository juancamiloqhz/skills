# Foundation fidelity audit

Date: 2026-10-13. Local baseline: `d57d3407626f741900c9574b9ecd47421a8de96f`.

The shipped foundation is not semantically equivalent to pstack. Its model-resolution adaptation preserves important role and inheritance semantics, and its inline principle groups now match the pinned source. The largest shipped drift is the maintenance skill's removal of parallel source readers. Juan-mode also omits upstream's mandatory helper triggers and narrows Figure-it-out routing. Its 23 absent playbooks and their tools are pending implementation, not evidence that the foundation supplies those workflows.

Only this report was written. No source, configuration, installed skill, schedule, upstream checkpoint, commit or PR was changed. No agent was delegated. Research was read-only except for this report.

## Sources and comparison method

Read `AGENTS.md` and `research/jstack/upstream-fidelity.md` first. The latter supersedes earlier packaging preferences. The user's current requirements establish standalone helpers and principles, inline principle groups, research-only provenance with distributed licenses, inherited routing, activation until opt-out, manual installation, separate merge authority and no unsolicited external messages. Earlier adaptation notes establish what changed, not permission for that change.

The exact source revisions below come from `research/jstack/upstream.json`. In subsequent citations, `U1:path` means that exact path at the full U1 revision, and `U0:path` means that exact path at the full U0 revision. All local path-and-line citations refer to the local baseline above. The four mapped working-tree directories had no diff against that baseline when inspected.

| Component | Local root | Exact upstream root and revision |
| --- | --- | --- |
| Juan-mode | `skills/jstack/juan-mode` | `pstack/skills/poteto-mode` at U1 = `11713c683fe4add4fd403ea880580abbc9e0875f` |
| Setup | `skills/jstack/setup-jstack` | `pstack/skills/setup-pstack` at U0 = `ccb5507cec1546dc88135c1139c811e6c59115ba` |
| Generator | `skills/jstack/create-verification-skill` | `pstack/skills/create-verification-skill` at U0 |
| Maintenance | `skills/jstack/maintain-verification-skill` | `pstack/skills/maintain-verification-skill` at U0 |

Primary evidence was retrieved using `git --git-dir=/home/ubuntu/.cache/jstack/upstream/upstream.git ls-tree -r --name-only PIN PATH` and `git ... show PIN:PATH`. Local tracked paths were enumerated with `git ls-tree` at the baseline. No upstream fetch occurred. The manifest's `reviewedThrough` value, `4bf3e083c6dec126e254f96181b84a105b6e3e70`, is not the adaptation pin and was not used as a replacement source.

Read all local operational files, references, Python scripts, test scripts and provider metadata in the four mapped directories. Read the four upstream entrypoints, the generator's three examples, the mode guide, agent wrapper, relevant helper entrypoints, Bugbot reference, bootstrap, package metadata, lockfile, plan checker and worktree audit. Inspected all upstream tool paths, imports, exported interfaces, commands and test-case inventories, with focused implementation reads of watcher classification and Graphite frontier resolution. Playbook inspection established the missing procedure set and its material algorithms. It was not a line-by-line implementation review of the thousands of lines in tools that have no local counterpart.

Context included U1 `pstack/docs/guide/02-poteto-mode.md`, U1 setup, and U0 poteto-mode/how/why role-consumer instructions. How and Why's own supporting-file semantic audits are outside this report. The setup investigation reference explicitly adds a U1 Why source despite setup's U0 primary pin; preserve that distinction when moving provenance.

Disposition terms used below:

- **Necessary** means a demonstrated runtime substitution or preservation of task authority.
- **User-approved** means supported by the current instructions or a specifically recorded user decision, not merely a merged change.
- **Restore** means unnecessary drift under the current fidelity policy.
- **Pending implementation** means an acknowledged missing procedure, tool or acceptance gate.
- **Needs decision** means the inspected evidence does not establish approval, or upstream itself leaves conflicting choices.

## Actionable findings

### F1. Restore the maintenance source wave and its reconciliation order

**Restore. High impact.** U0 `pstack/skills/maintain-verification-skill/SKILL.md:25-37` specifies locate, index hygiene, one concurrent read-only subagent per feature, reconcile every returned summary, coordinator-only serial live driving, triage, and ship or stop. Each reader returns a feature summary, source entry points, likely drift and one live recipe. Children neither edit nor drive. The coordinator spot-checks drift rather than re-proving every clean claim.

Local `skills/jstack/maintain-verification-skill/SKILL.md:22-32` assigns source review to the executing agent and replaces that protocol with a per-feature ledger. `references/upstream.md:7` explicitly acknowledges the removal, but supplies no runtime incompatibility or user decision. T3 supports read-only children. Standalone installation does not imply single-agent execution. The historical evaluation prompt prohibited further delegation, so its successful CLI results cannot validate the upstream source wave or justify deleting it.

Correction scope: preserve the upstream numbered pass and return shape, substitute supported T3 child tools, keep children read-only, and let the coordinator own all live driving and edits. Honor inherited/configured role selection without inventing a new paid model. If no role is already prescribed for this standalone skill, state the choice of inherited parent or existing role explicitly rather than silently changing the 17-role registry. A caller's no-delegation instruction can be a disclosed execution exception; it should not redefine the default skill.

Verification: use a map with three independent features and one missing surface. Inspect actual child task records for one reader per feature, bounded source ownership, returned citations and recipes, all terminal before reconciliation, and no child app interactions. Verify coordinator-only live coverage, shared-state reset, regression preservation and cleanup. Repeat with an explicit no-delegation constraint and require a labeled limitation or authorized serial fallback. Do not grade this from the coordinator's claim alone.

### F2. Restore Juan-mode's mandatory triggers and broad Figure-it-out route

**Restore, with pending dependencies. High impact.** U1 `pstack/skills/poteto-mode/SKILL.md:13-36` contains a Non-negotiables section that binds concrete triggers to How, Architect, Swarm, Interrogate, Unslop, Technical-writing, Deslop, No-comments, control skills, Benchmark-checklist and Show-me-your-work. It also classifies empirical questions before asking the user and requires a throughput checkpoint for nontrivial multi-step work. Local `skills/jstack/juan-mode/SKILL.md:76-78` instead describes optional helper selection and discovery. Naming available helpers does not preserve when they must run.

U1 `pstack/skills/poteto-mode/SKILL.md:123` sends large or cross-cutting work and work the user steps away from to Figure-it-out even when a narrower playbook fits. Local `skills/jstack/juan-mode/SKILL.md:78` limits that helper to a custom workflow when no narrower available procedure fits. This changes priority, not just wording. The local rule against using Figure-it-out to disguise an unavailable named playbook remains useful, but must not eliminate the separate large-work trigger.

U1 `pstack/skills/poteto-mode/SKILL.md:121` also requires copying the matched playbook's steps verbatim into the todo list before task-specific items and retaining skipped steps with reasons. Local `SKILL.md:16` says to read an implemented playbook but omits that contract. The route list moved from the entrypoint into `references/routes.md:1-29`, reordered several entries and compressed their trigger examples. Nothing about T3 requires that structural move. The current fidelity policy specifically protects trigger placement and section organization.

Correction scope: restore Non-negotiables and inline Playbooks placement with their pinned triggers. Add narrow T3 substitutions and explicit unavailable-dependency disclosures. Keep missing playbooks unavailable. Restore step copying when a procedure exists. Preserve principle groups already restored at local `SKILL.md:19-64`; do not create another principle index.

Verification: inspect actual routing for a small feature, a cross-cutting migration, unattended work, a read-only empirical question, a benchmark claim, an adversarial design, a PR status request and skill authoring. Require the right trigger, preserved order, and explicit absence rather than unrelated same-name fallback. For an implemented procedure, compare todo items to its source steps and confirm a skipped step remains visible.

### F3. Restore the general child freshness and agent-style contract

**Restore plus necessary T3 substitution.** U1 `pstack/skills/poteto-mode/SKILL.md:93-99` requires the Poteto agent wrapper for ordinary playbook children, preserves specialized workflow wrappers, and makes every new task, follow-up, retry or fix round fresh by default. Reuse is restricted to expensive process or checkout state that cannot reasonably move. U1 `pstack/agents/poteto-agent.md:3-10` makes the child read the full mode and relevant principle leaves.

Local `skills/jstack/juan-mode/references/execution.md:7-21` carries a consolidated brief and requires fresh delegated review rounds, but does not preserve freshness for other new work or require ordinary children to load the full working style. `references/activation.md:3` says a child receives only task-relevant instructions. That is compatible with bounded authority, but is not an equivalent replacement for the wrapper's mandatory style read.

Correction scope: replace the Cursor wrapper mechanism with explicit child instructions to read the discovered mode and applicable leaves without activating the parent's persistent conversation state in an unrelated thread. Preserve specialized helper instructions. Extend fresh-task rules to non-review work while respecting T3's stronger requirement that each delegated review round is a new `delegate_task`.

Verification: a feature delegate and a later fix delegate should have distinct IDs and consolidated briefs; observed file reads should include the working-style instructions. A genuinely stateful exception must name the retained state. No task should gain external-action authority just by reading the mode.

### F4. Restore generator examples and inline generation requirements

**Restore.** U0 `pstack/skills/create-verification-skill/SKILL.md:23-36` includes the six output sections inline and points to three shipped example files. Local `skills/jstack/create-verification-skill/SKILL.md:28-30` moves those requirements to `references/output-contract.md` and omits all three examples. `references/upstream.md:12` calls this an alternative to shipping fictional app commands. That is a design preference, not a T3 constraint. The examples are expressly examples of the output shape, not instructions to run Notes against an unrelated app.

Much substantive content survives in the output contract, including the four feature headings, separate evidence, observable assertions and public entry points. However, the replacement loses the worked pairing of each action with a command and expected state across toolbar, keyboard and CLI entry points. The upstream example index requires the driving section to start with `Preconditions:` and use labeled action bullets; the local contract at `references/output-contract.md:39-48` keeps headings and concepts but not that exact recipe format. Its weaker phrasing about known entry points also loses the example's explicit instruction to list every user entry point.

Correction scope: restore the upstream five numbered stages, inline output-section requirements and `references/feature-map-example/{README.md,create-note.md,search.md}`. Apply only required path, tool and authority substitutions. Fold useful local assertion/cleanup clarifications into the corresponding upstream sections instead of a new parallel contract.

Verification: generate a skill for a fixture with two UI entry points and a CLI entry point. Check the four headings in order, preconditions, concrete action/command/result pairs, all identified entry points and honest untested labels. Execute one feature, then let a fresh consumer use the generated instructions in another checkout. Inject an incorrect result with exit zero and require a failing assertion with retained proof.

### F5. Move provenance out of operational packages without losing licenses or pins

**User-approved correction.** The fidelity policy requires provenance in research. All four packages still ship `references/upstream.md`. Operational pointers remain at `skills/jstack/juan-mode/SKILL.md:84`, `skills/jstack/setup-jstack/SKILL.md:56-60`, `skills/jstack/create-verification-skill/SKILL.md:8`, and `skills/jstack/maintain-verification-skill/SKILL.md:8`. The manifest's four `differences` fields still target these packaged records.

Correction scope: move source pins, comparison rationale and historical evaluation references under `research/jstack/`; update manifest mappings and research links. Remove provenance-only entrypoint text and package references. Keep operational scope instructions, particularly setup's no-implicit-workflow and authorization boundaries. Preserve all four package LICENSE files. Each is byte-identical to `pstack/LICENSE` at its component's exact pin, including Copyright 2026 Lauren Tan.

Verification: independently install or stage each package and verify its MIT notice remains. Check every manifest difference target and research link resolves. Search operational files for provenance-only sections and ensure discovery never depends on attribution prose. Do not change `adaptedFrom` or `reviewedThrough` for a packaging correction.

### F6. Resolve invocation, coverage-result and provider-link choices explicitly

**Needs decision.** Both U0 verification entrypoints have `disable-model-invocation: true` at line 4. The local frontmatter omits it and advertises ordinary discovery at each local `SKILL.md:3`. Local generator `references/upstream.md:12` and maintenance `references/upstream.md:7` acknowledge this choice. Calling the generator after setup's accepted offer does not require unsolicited model invocation. Preserve caller-authorized use while deciding whether direct automatic triggering is desired. Restore manual-invocation policy where the host supports it unless an explicit contrary decision is established. Codex display metadata alone does not prove that invocation policy is enforced across all selected providers.

Juan-mode's removal of Cursor-specific `mode`, `icon`, `color` and `reminder` metadata is necessary; its until-opt-out behavior is explicitly user-approved. Whether to retain supported manual-invocation metadata without preventing active-mode continuation requires provider-specific checking, not blindly copying Cursor frontmatter.

Maintenance changes U0 `SKILL.md:33`'s `verified-unreachable` classification into blocked coverage at local `skills/jstack/maintain-verification-skill/SKILL.md:44,60`. The stricter outcome is honest, but it is a behavioral choice rather than a tool substitution. Decide whether unreachable with a verified prerequisite remains a separately reportable feature result, and how it affects overall clean/changed/blocked status. Neither label may count as a successful feature drive.

Generator `skills/jstack/create-verification-skill/SKILL.md:34-40` automatically adds a Claude Code symlink for every generated skill, regardless of provider. Upstream has no such step. This is project-local generation, not necessarily a prohibited global installation, so manual-install policy alone does not prove it must be removed. The inspected decision record does not establish the specific all-provider symlink requirement. Retain any prior explicit user authorization if the parent has it; otherwise request a decision before treating it as required. Test default/custom paths, existing identical links, conflicts, dangling links, targets outside the repository and actual client discovery. Maintenance's symlink deduplication at local `SKILL.md:14` can remain as correct handling of an existing target regardless of whether automatic generation is retained.

### F7. Preserve pending tool algorithms and resolve upstream contradictions before porting

**Pending implementation, with necessary substitutions and unresolved choices.** Local `skills/jstack/juan-mode/SKILL.md:10` and `references/routes.md:3` accurately disclose that all 23 playbooks are unavailable. Missing tools are therefore not a runtime regression in an otherwise enabled route. They are mandatory scope to account for before declaring any route implemented.

The preflight is not a substitute for the upstream plan checker, orchestration store, PR watcher or worktree auditor. Important behavior must survive adaptation:

- U1 `pstack/skills/poteto-mode/scripts/check-plan.mjs:5-31,121-169` checks the ordered plan blocks, evidence rules, ten numbered live lanes with proof predicates, dual-sided perf fields and operator review gates. T3 substitutions for `/loop` and model names must not silently reduce these checks.
- U1 `pstack/skills/poteto-mode/scripts/watch-pr/policy.ts:55-265` checks actual merge state, review threads and hidden GitHub CI refusal; conflict, thread and CI blockers have explicit priority. The other watcher files supply query fallback, pagination, queue state, typed verdicts, rendering and executable tests. T3's parent-owned watch replaces polling and wake mechanics where available. It does not by itself prove equivalent readiness classification or verified stack ordering.
- U1 `pstack/skills/poteto-mode/playbooks/shipping.md:7-15` requires independent per-PR proof, contiguous verified landing, patch-id checks after rebases, fresh CI/mergeability, and recomputation after each merge. Its three-build comparison for test/doc/lint-only changes distinguishes real artifact differences from build noise; do not reduce it to "same patch means safe" or "CI green". Separate user merge authority remains mandatory.
- U1 `pstack/skills/poteto-mode/scripts/orch/store.ts:183-220,336-443,1005-1197` exposes units, ledger, inbox, gates, standing orders and frontier operations, with atomic writes and a PID lock. Its Graphite frontier actually executes `gt info` and `gt log`, so Graphite dependence is real. U1 `playbooks/orchestrate.md` requires it while U1 `playbooks/opening-a-pr.md`, `autopilot-full.md` and `autopilot-stack.md` say not to require Graphite. This is an upstream inconsistency needing a recorded forge/frontier decision, not permission to omit the store.
- U1 `pstack/skills/poteto-mode/scripts/bootstrap.ts:26-61` runs `bun install --frozen-lockfile` and restarts the command. `scripts/watch-pr/watch-pr:2-5` invokes it; `scripts/orch/orch.ts` imports it too. Automatic installation conflicts with the user's manual-install requirement. Preserve the dependency declaration and lockfile if those tools are ported, but replace auto-install with a precise prerequisite and manual command.
- U1 `pstack/skills/poteto-mode/scripts/worktree-audit.sh:18-26,62-79` fetches Git refs, scans Cursor transcript paths with macOS stat/date syntax, and may call a worktree safe when it merely has a PR record. The playbook warns that its buckets are advice. Replace host paths/tools and verify in-use state, untracked files and actual merge state before removal. Do not advertise its current implementation as a purely non-mutating local read or copy unsafe deletion assumptions.

Verification: port tools alongside the first consuming procedure, retain their test intent, and add fixtures for the actual T3 substitution. Compare watcher truth tables, stale-head verdict invalidation, queue wake/rearm, explicit parent ownership, store crash recovery and a worktree containing valuable untracked data. Run no installs automatically. Test the plan checker with one missing ordered block, one missing lane and a valid full plan. Source inventory counts cannot establish these behaviors.

## Complete component dispositions

These dispositions cover each mapped file and the material instruction differences identified in the shipped components. They do not certify runtime equivalence.

### Juan-mode

| Difference or retained behavior | Disposition | Reason and correction or verification |
| --- | --- | --- |
| Rename, T3 dispatch/catalog, explicit child briefs, task IDs and parent-owned PR watches | Necessary | Cursor `Task` wrappers and cloud placement cannot be copied as T3 APIs. Preserve upstream role intent and inspect actual chosen model/options and child ownership. Local `SKILL.md:68-74`, `references/execution.md:3-41`; U1 mode `SKILL.md:91-99`. |
| Until-opt-out activation, task completion does not deactivate, no activation during authoring | User-approved | Current user requirement and `research/jstack/decisions.md:9-11`. Local `references/activation.md:3-23` correctly labels compaction/restart unverified. Real host-boundary evidence remains pending. |
| Standalone 24 principle leaves with inline groups | User-approved; retained alignment | Local `SKILL.md:19-64` preserves the U1 mode `SKILL.md:38-79` groups and summaries. Catalog identity/manual-install guidance is necessary for independent packages. Leaf-body fidelity belongs to the principles audit. |
| Configured inheritance, ordered duplicate seats, panel versus pool distinctions, same selected absolute config in children | Necessary and user-approved | U1 mode `SKILL.md:95` and U0 setup step 3 distinguish these roles. Local `references/configuration.md:17-35` and `scripts/preflight.py:12-66` preserve them without substituting concrete targets for inherited seats. Keep saved choices intact. |
| Missing Non-negotiables, reduced Figure-it-out trigger, moved route registry and missing verbatim todo rule | Restore | F2. Availability disclosure does not justify changing routing semantics. |
| Missing full Writing the reply and Comments sections | Restore, subject to scoped authority | U1 mode `SKILL.md:101-117` requires evidence labels alongside claims, consumer/maintainer impact, no fabricated links, all playbook reply content and comments only for non-obvious reasons. Local `SKILL.md:80-84` is a compressed completion summary. Global agent style is not a packaged replacement. Restore applicable wording and concrete reply checks. |
| General child freshness and style wrapper reduced to review-round handling | Restore | F3. Read task records and child instruction reads, not only output quality. |
| Broad upstream external-action autonomy removed; merge/installation/scheduling authority remains separate | User-approved and necessary | U1 mode `SKILL.md:81-89` allows team chat and ticket updates without asking. Current user explicitly excludes unsolicited external messages. Local `references/execution.md:39-41` is the required exception. Keep reversible in-scope autonomy and candor; do not restore blanket external permission. |
| All playbook procedures, Bugbot triage, plan/store/watch/cleanup tools absent | Pending implementation | F7 and full upstream inventory below. Do not mark routes supported until procedure and dependencies have evidence. |
| Separately discoverable How, Why, Arena, Architect, Interrogate, Swarm, Reflect and Figure-it-out | User-approved boundary | Local `SKILL.md:78` supports standalone packages and manual installation; U1 mode refers to standalone helper skills. Do not combine them into the mode. Their algorithms are outside this audit. |
| Replacing deletion-first No-comments with unspecified scoped evidence review | Needs decision | Local `references/upstream.md:11` states this redesign, but upstream `no-comments` has a substantial independent procedure. Useful safety/authority exceptions can be necessary; silently removing its entire workflow is not. See dependency inventory. |
| Provenance record in installed package | User-approved correction | F5. Move it to research; retain LICENSE. |

### Setup-jstack

The basic sequence remains discover, load, budget/map, validate, save, confirm, optional verification offer. It has been reorganized from U0's seven numbered steps into four broad sections. Restore the original step headings/order while placing T3-specific details at their corresponding steps. Do not move the role table solely to save words: U0 step 5 exposes all 17 roles in the entrypoint; local `SKILL.md:26,32` mentions all roles/panels, while the full registry lives in `scripts/models.py:12-20`. The new JSON representation justifies a generated example, not omission of a reviewable role list.

| Difference | Disposition | Reason and concrete verification |
| --- | --- | --- |
| `.mdc` always-applied rule becomes JSON plus runtime resolution | Necessary | T3 does not automatically load a Cursor rule. Local `SKILL.md:14-20,36-40`; U0 setup steps 1, 4-6. Verify fresh catalog validation and invocation-time rereads; never claim saving changes the current model. |
| Global/project choice and explicit/environment/project/global precedence; complete map replaces rather than merges | User-approved | `research/jstack/decisions.md:23`. `references/configuration.md:16-40`, `scripts/models.py:59-83`. Verify scope selection and child-path pinning without modifying saved files in another scope. |
| Provider/model/options instead of effort-encoded slugs | Necessary | Preserve effort separately using advertised values. U0 step 3(b)'s highest supported effort at or below target survives local `SKILL.md:28`; if none qualifies, require a choice. Verify two option schemas, unsupported effort, custom models and ambiguous option meanings. |
| Four budget labels and all 17 role names retained | Retained alignment | `scripts/models.py:12-25` matches U0 setup step 5's labels. `preset` records setup preference; effective options control execution. Verify inherited seats do not acquire a target or changed effort. |
| Preserve explicit role/list/effort choices on rerun rather than rebuilding defaults | User-approved for saved choices | Current inherited-routing requirement and recorded setup contract. Local `SKILL.md:26,40` protects stored selections. Verify bulk budget edits include every requested concrete list seat without changing identities, order, count or inherited seats. |
| New configs use all inherited seats, one seat per panel and `medium` template budget rather than Grok/Opus defaults and two-seat panels | Needs decision for future defaults; retain existing user choices | Local `scripts/models.py:86-95,188-189` and `SKILL.md:26,32`; U0 setup step 5. The user's selected inherited routing must never be overwritten. But inherited identity alone does not dictate one-seat cardinality or the default budget. Document the intentional first-run experience: one-seat templates require setup changes before comparison skills can run. Test the selected count and explicit insufficiency rather than silently adding seats. |
| `auto` alias rejected; provider Auto is concrete | Necessary T3 disambiguation | U0 treats `auto` and inheritance alike. Local `SKILL.md:30` and `scripts/models.py:104-106` prevent an ambiguous generic Auto from switching providers/models. Verify omitted target inherits actual parent options, while advertised Auto remains a concrete selection. |
| Unknown/missing roles error instead of dropping retired roles or falling back to defaults; every invocation validates unrelated roles too | Needs decision where stricter than saved-choice protection | U0 setup step 2 drops retired role lines, and U1 mode `SKILL.md:95` permits absent-role defaults. Local `scripts/models.py:137-149` requires the full exact map; `references/configuration.md:74` blocks unrelated work for stale seats. No silent repair/substitution is necessary, but whole-map blocking is an additional product choice. Keep it pending a decision rather than weaken current validation during this audit. Verify a stale unrelated role and a missing selected role separately. |
| Catalog unavailable stops setup instead of asking for pasted slugs | Necessary for validated T3 target/options | U0 step 1 allows pasted model slugs. A slug alone lacks provider identity and option schema. Local `SKILL.md:14` preserves the saved file and reports the limitation. Confirm the direct attempt and documented ACP fallback occur before declaring unavailable. |
| Optional generator offer occurs once after save; manual discovery/install; no workflow execution during setup | User-approved and retained alignment | U0 step 7; local `SKILL.md:42-54`. Verify decline, missing generator and failed generation do not undo model setup. Existing public-path harness skips the offer; unit tests alone need not. |
| Operational configuration/T3 references, resolver and tests | Necessary implementation support | These have no upstream standalone files because upstream uses a text rule. Keep the single canonical resolver rather than duplicating lookup in consumers. Inspect tests as bounded evidence, not proof of all provider behavior. |
| Shared investigation evidence reference housed in setup | User-approved ownership, preserve semantics | `references/investigation.md:1-51` is shared by standalone consumers and has no U0 setup equivalent. The 2026-10-12 standalone investigation decision explicitly assigns shared configuration and evidence guidance to setup. This resolves the ownership question; it does not approve deleting How/Why prompt templates. Do not move it blindly and break independent installations. Its added U1 Why provenance must be mapped. |
| Section consolidation, nonoperational explanation and provenance | Restore structure; move provenance | Restore seven-step setup organization around necessary substitutions. Remove provenance-only text under F5. Preserve legitimate scope/authority instructions. |

### Create-verification-skill

| Difference or retained behavior | Disposition | Reason and concrete verification |
| --- | --- | --- |
| Repo interview, generation, feature map, one-feature end-to-end proof and maintenance handoff | Retained core sequence, restore original section layout | U0 `SKILL.md:11-44`; local `SKILL.md:10-48`. Tool/output selection and link steps interrupt the original grouping. Place necessary substitutions within the five stages. |
| Existing harness preferred, real public paths, observed dry-run effects, evidence survives cleanup | Retained alignment | Local `SKILL.md:14,32,44` and output contract retain these substantive U0 requirements. Test action plus resulting state and failure cleanup. |
| Default `.agents/skills`, explicit repo conventions and T3 browser operations | Necessary portability/runtime substitution | Local `SKILL.md:20-24`; U0 `SKILL.md:17,25`. Preserve repository harnesses and runtime fallback conditions. Verify app identity and actual browser entry point; API proof cannot stand for UI proof. |
| Ordinary noninteractive CLI subprocesses instead of always PTY/tmux | Necessary interface-specific adaptation | Local `SKILL.md:14`; U0 `SKILL.md:27`. PTY remains required for interactive behavior. Verify stdin/exit/status semantics for each interface. |
| Refuse invented app for docs-only repo; preserve existing suitable verification skill | Necessary task grounding | Local `SKILL.md:16`; consistent with U0's repo-first interview. Existing skill repair still needs requested scope. Historical docs-only evidence is narrow but relevant. |
| Report broader startup defects rather than silently widen application edit/install scope | Necessary authority exception | Local `SKILL.md:18` qualifies U0 `SKILL.md:21`'s fix-or-report baseline rule. Preserve the report path; do not generate against a broken baseline and call it proven. |
| Six inline output requirements and worked examples replaced by separate output contract | Restore | F4. Keep useful assertion/isolation clarifications while restoring source structure and examples. |
| Generated helper may use an explicit interpreter instead of executable mode | Needs decision for strict fidelity | Local `references/output-contract.md:33-35`; U0 `SKILL.md:32` requires executable scripts and documented invocation. An explicit interpreter works, but this relaxation is not demanded by T3. Preserve executable mode where possible and test the documented invocation. |
| Automatic Claude link | Needs decision unless earlier explicit authorization is supplied | F6. Do not infer either permission or prohibition solely from manual global installs. |
| No explicit cadence-only-if-asked sentence | Restore | U0 `SKILL.md:44` has it; local `SKILL.md:48` omits it. Restore the small guard so offering maintenance does not become unsolicited schedule advice or scheduling. |
| Normal model invocation and packaged provenance | Needs decision; provenance correction user-approved | F5-F6. Display metadata can remain as provider support; test actual registration separately. |

### Maintain-verification-skill

| Difference or retained behavior | Disposition | Reason and concrete verification |
| --- | --- | --- |
| Outcomes/Edit scope/numbered Pass reorganized into prose headings, outcomes moved last | Restore | U0 `SKILL.md:11-37`; local `SKILL.md:10-62`. Restore upstream sequence and put local clarifications at their corresponding steps. |
| One source reader per feature removed, generated per-feature ledger added | Restore source wave; keep scratch notes lightweight | F1. U0 step 1 explicitly says no generated inventory, and its final line already allows concise scratch notes. Do not introduce mandatory bookkeeping beyond what proves coverage. |
| Every feature source-reviewed and live-driven, one representative path per feature | Retained alignment | U0 introduction and step 4; local `SKILL.md:24,42`. Sub-feature disclosure correctly prevents overclaiming exhaustive path coverage. |
| Coordinator owns serial server/UI instance or per-drive CLI sessions; doctor/reset after surprise | Retained alignment with necessary browser substitution | U0 step 4; local `SKILL.md:36-44`. Preserve one retry for stale doctor and restart only what its fix invalidates. |
| Stronger intentional-change evidence and regression classification | Necessary preservation of contract, compatible elaboration | Local `SKILL.md:28-32` operationalizes U0 edit scope and triage. Source behavior alone cannot authorize weakening an assertion. Test intentional rename versus wrong output with zero exit. |
| Blocked instead of `verified-unreachable` | Needs decision | F6. Report prerequisite and attempted route either way. |
| Clean/changed require no unresolved regressions; blocked suppresses completion claims | Needs decision where stricter than upstream | U0 step 5 records product gaps outside the correction PR; local `SKILL.md:58-60` makes every unresolved regression a blocked run. Decide whether an independently proven verifier repair can ship while separately reporting a product defect. Do not weaken failure assertions. |
| No automatic PR on every changed run | Necessary/user-approved delivery boundary | U0 step 6 says one PR; local `SKILL.md:62` follows requested publication. Current user forbids unrequested external actions. When publication is authorized, preserve one focused PR and restore upstream's explicit reread of every changed file before shipping. |
| Owned-directory edits, preserved historical evidence, symlink deduplication, no installs | Necessary user/repository scope handling | Local `SKILL.md:14-20,48-52`. These preserve source boundaries rather than grant broad repair authority. Verify canonical target and no outside-repo writes. |
| Interpreter alternative for helper executability | Needs decision for strict fidelity | Local `SKILL.md:50`; U0 step 5 imports generator's executable-helper rule. Same correction/test as generator. |
| Automatic invocation and provenance | Needs decision; provenance correction user-approved | F5-F6. |

## Path inventory

Every tracked path under each mapped root is listed below. Paths in a table are relative to its named root. This is a completeness check for packaging and disposition, not a semantic-equivalence metric. Upstream paths carry the pin from the component table. Local references and scripts were read; absent upstream tools received structural/dependency inspection and targeted algorithm inspection as described above.

### juan-mode local paths

Root: `skills/jstack/juan-mode` at the local baseline.

| Path | Disposition |
| --- | --- |
| `LICENSE` | User-approved retention; exact upstream MIT bytes. |
| `SKILL.md` | Mixed; all material differences classified in component dispositions and F1-F6. |
| `references/activation.md` | User-approved persistent activation; real compaction/restart proof pending. |
| `references/configuration.md` | Necessary configuration contract with approved project lookup; stricter/default policies separately classified. |
| `references/execution.md` | Necessary T3 transport/ownership contract; restore general freshness/style behavior under F3. |
| `references/routes.md` | Restore inline trigger placement; all 23 procedures remain pending implementation. |
| `references/upstream.md` | Move to research under F5; preserve its pins and historical claims as historical evidence. |
| `scripts/preflight.py` | Necessary local model validation/resolution or capability preflight; no equivalent upstream tool file. |
| `scripts/test_preflight.py` | Local validation support; fixture tests are not live provider or workflow equivalence. |

### juan-mode upstream paths

Root: `pstack/skills/poteto-mode` at `11713c683fe4add4fd403ea880580abbc9e0875f`.

| Path | Local counterpart or disposition |
| --- | --- |
| `SKILL.md` | Local SKILL.md; compare dispositions above, not word/file counts. |
| `playbooks/authoring-a-skill.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/autonomous-run.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/autopilot-full.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/autopilot-stack.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/babysit.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/bug-fix.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/eval.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/feature.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/hillclimb.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/investigation.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/multi-phase-plan.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/opening-a-pr.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/orchestrate.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/pause-safely.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/perf-issue.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/prototype.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/refactoring.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/runtime-forensics.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/session-pickup.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/shipping.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/trace-forensics.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/visual-parity.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `playbooks/worktree-cleanup.md` | Absent. Pending implementation as this named procedure inside juan-mode; preserve its algorithm and ordered steps. |
| `references/bugbot-triage.md` | Absent. Pending with Babysit/review consumers; preserve fix/dismiss/ask rubric and risk exceptions, subject to messaging authority. |
| `scripts/bootstrap.ts` | Absent. Pending tool support; automatic dependency install must be replaced by manual prerequisites. |
| `scripts/bun.lock` | Absent. Pending Bun/Commander dependency packaging; retain reproducible dependency information if tools are ported. |
| `scripts/check-plan.mjs` | Absent. Pending Multi-phase plan validator; preserve ordered blocks and verification checks. |
| `scripts/orch/orch.test.ts` | Absent. Pending orchestration test coverage; preserve store, lock, frontier and CLI cases. |
| `scripts/orch/orch.ts` | Absent. Pending orchestration CLI/store; preserve durable records and locking, resolve Graphite dependence explicitly. |
| `scripts/orch/store.ts` | Absent. Pending orchestration CLI/store; preserve durable records and locking, resolve Graphite dependence explicitly. |
| `scripts/package.json` | Absent. Pending Bun/Commander dependency packaging; retain reproducible dependency information if tools are ported. |
| `scripts/watch-pr/cli.test.ts` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/cli.ts` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/watch-pr/fakes.test-helper.ts` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/github.test.ts` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/github.ts` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/watch-pr/policy.test.ts` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/policy.ts` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/watch-pr/render.ts` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/watch-pr/tsconfig.json` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/types.compile.ts` | Absent. Pending PR-readiness test/typecheck support; retain its behavioral cases when substituting T3 wake mechanics. |
| `scripts/watch-pr/types.ts` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/watch-pr/watch-pr` | Absent. Pending PR-readiness implementation/support; T3 watches replace wake ownership, not automatically verdict semantics. |
| `scripts/worktree-audit.sh` | Absent. Pending cleanup audit; adapt host paths and reassess state/deletion assumptions. |

### setup-jstack local paths

Root: `skills/jstack/setup-jstack` at the local baseline.

| Path | Disposition |
| --- | --- |
| `LICENSE` | User-approved retention; exact upstream MIT bytes. |
| `SKILL.md` | Mixed; all material differences classified in component dispositions and F1-F6. |
| `agents/openai.yaml` | Provider display metadata; no upstream counterpart; do not mistake it for invocation-policy proof. |
| `references/configuration.md` | Necessary configuration contract with approved project lookup; stricter/default policies separately classified. |
| `references/investigation.md` | User-approved shared standalone-helper support; retain added U1 Why source mapping. |
| `references/t3-code.md` | Necessary runtime contract and bounded discovery fallback. |
| `references/upstream.md` | Move to research under F5; preserve its pins and historical claims as historical evidence. |
| `scripts/models.py` | Necessary local model validation/resolution or capability preflight; no equivalent upstream tool file. |
| `scripts/test_models.py` | Local validation support; fixture tests are not live provider or workflow equivalence. |

### setup-jstack upstream paths

Root: `pstack/skills/setup-pstack` at `ccb5507cec1546dc88135c1139c811e6c59115ba`.

| Path | Local counterpart or disposition |
| --- | --- |
| `SKILL.md` | Local SKILL.md; compare dispositions above, not word/file counts. |

### create-verification-skill local paths

Root: `skills/jstack/create-verification-skill` at the local baseline.

| Path | Disposition |
| --- | --- |
| `LICENSE` | User-approved retention; exact upstream MIT bytes. |
| `SKILL.md` | Mixed; all material differences classified in component dispositions and F1-F6. |
| `agents/openai.yaml` | Provider display metadata; no upstream counterpart; do not mistake it for invocation-policy proof. |
| `references/output-contract.md` | Restore inline source requirements and examples under F4; retain necessary runtime clarifications. |
| `references/upstream.md` | Move to research under F5; preserve its pins and historical claims as historical evidence. |

### create-verification-skill upstream paths

Root: `pstack/skills/create-verification-skill` at `ccb5507cec1546dc88135c1139c811e6c59115ba`.

| Path | Local counterpart or disposition |
| --- | --- |
| `SKILL.md` | Local SKILL.md; compare dispositions above, not word/file counts. |
| `references/feature-map-example/README.md` | Absent. Restore this worked example under F4; output-contract.md is not a path-equivalent replacement. |
| `references/feature-map-example/create-note.md` | Absent. Restore this worked example under F4; output-contract.md is not a path-equivalent replacement. |
| `references/feature-map-example/search.md` | Absent. Restore this worked example under F4; output-contract.md is not a path-equivalent replacement. |

### maintain-verification-skill local paths

Root: `skills/jstack/maintain-verification-skill` at the local baseline.

| Path | Disposition |
| --- | --- |
| `LICENSE` | User-approved retention; exact upstream MIT bytes. |
| `SKILL.md` | Mixed; all material differences classified in component dispositions and F1-F6. |
| `agents/openai.yaml` | Provider display metadata; no upstream counterpart; do not mistake it for invocation-policy proof. |
| `references/upstream.md` | Move to research under F5; preserve its pins and historical claims as historical evidence. |

### maintain-verification-skill upstream paths

Root: `pstack/skills/maintain-verification-skill` at `ccb5507cec1546dc88135c1139c811e6c59115ba`.

| Path | Local counterpart or disposition |
| --- | --- |
| `SKILL.md` | Local SKILL.md; compare dispositions above, not word/file counts. |

## Dependencies outside the mapped directories

The following dependencies are not made available merely by installing one of these four packages. Existing global skills with similar names are not proof of pinned pstack behavior. Each missing helper should remain standalone under the user's requirement, with a mapped pin, package license, manual-install instructions and an operational caller that reports absence. No helper below was installed or executed in this audit.

| Exact source path at U1 | Dependency and local disposition |
| --- | --- |
| `pstack/agents/poteto-agent.md` | Required by mode `SKILL.md:93`. No local wrapper counterpart. Necessary T3 replacement must preserve its full-mode/leaf-read behavior under F3, not only its name. |
| `pstack/skills/technical-writing/SKILL.md` | Required by mode `SKILL.md:27` and plan/PR procedures. No packaged local counterpart found. Pending standalone helper. Preserve its four layers and differentiated document modes; generic plain-language instructions are not equivalent. |
| `pstack/skills/benchmark-checklist/SKILL.md` | Required by mode `SKILL.md:31`, Perf issue and Hillclimb. No packaged local counterpart found. Pending standalone helper. Retain limiter profiling outside reported runs, tuning parity, physical-limit arithmetic, error/work counts, at least five alternating runs for comparisons, median/range, and user-path relevance. A quick user-requested ballpark has its own narrower exception; do not use it for choosing between options. |
| `pstack/skills/show-me-your-work/SKILL.md` | Required by mode `SKILL.md:36` and autonomous/program procedures. No packaged local counterpart found. Pending standalone helper. Preserve append-only decisions, start rows separating conversations, transcript audit, superseding incorrect rows and distinct-model trail review. Adapt transcript access to the authorized T3 thread rather than scanning unrelated chats. |
| `pstack/skills/show-me-your-work/references/decision-log-template.tsv` | Missing supporting dependency outside the mode root. Preserve the exact six-column header when porting the helper. A generic decision-log mention omits this contract. |
| `pstack/skills/show-me-your-work/scripts/log.sh` | Missing supporting dependency. The source stamps UTC, writes the header on first use, strips tabs/newlines/CR and prefixes formula-leading cells. Preserve these details or demonstrate an equivalent implementation with malformed-cell fixtures. |
| `pstack/skills/no-comments/SKILL.md` | Required by mode `SKILL.md:29` and PR procedures. Missing local counterpart. The existing note's proposed replacement needs decision. Preserve report review, rejection/rerun limits and scoped fixes where compatible; evaluate destructive comment-removal rules individually against repository constraints. |
| `pstack/agents/comment-sicko.md` | Required by No-comments step 1, outside both mapped roots and its skill directory. Missing transitive agent dependency. It must be read and assessed with the eventual No-comments port; this audit establishes the reference and missing path, not approval of all its rules. |
| `pstack/skills/unslop/SKILL.md` | Required by mode `SKILL.md:26` and writing helpers. The current session exposes an independently installed Unslop skill, but the audited package has no explicit pinned dependency/identity mapping. Needs decision on reusing a separately verified helper versus a standalone jstack adaptation; do not claim equivalence by name. |
| `pstack/skills/tdd/SKILL.md` | Bug-fix step 5 references it for cheap local failing-test-first cadence, with an explicit expensive/integration-heavy exception. Existing global TDD discovery is not a pinned packaging contract. Pending dependency decision; preserve the exception and commit-order algorithm in the playbook. |
| `cursor-team-kit/skills/deslop/SKILL.md` | External plugin dependency named in mode `SKILL.md:28` and PR/queue procedures. Same repository and U1 source tree, different plugin. No local package mapping. Pending decision on standalone adaptation or an explicitly supported external dependency; never silently use an unrelated formatter. |
| `cursor-team-kit/skills/control-cli/SKILL.md` | External control dependency named in mode `SKILL.md:30` and verification lanes. No packaged equivalent established. T3/browser tooling cannot stand for terminal interaction. Identify actual CLI/TUI driver and preserve real-surface proof. |
| `cursor-team-kit/skills/control-ui/SKILL.md` | External control dependency named in mode `SKILL.md:30`. T3 preview is a necessary host substitution where available, but it does not prove every Electron/native UI control capability. Record supported surface and gaps. |
| Cursor built-in `create-skill`, no repository skill path | Mode `SKILL.md:26` and `playbooks/authoring-a-skill.md:5` require it. Necessary host substitution must explicitly identify a supported authoring procedure; a global similarly named skill is not automatically the same dependency. |
| Cursor built-in `/loop`, no repository skill path | Autonomous run and queue/program procedures require wakes. Necessary T3 substitution must distinguish one task's event continuation from a persistent schedule, which needs its own user authorization. Never install a recurring schedule solely because upstream says `/loop`. |

Already mapped standalone jstack How, Why, Arena, Architect, Interrogate, Swarm, Reflect, Figure-it-out and 24 principle packages are outside this report's owned component set. Their presence does not make the mode's missing playbooks complete. The manifest currently omits the missing dependency mappings above. Its context paths are useful discovery hints, not a complete transitive dependency inventory.

## Existing evidence and what it proves

Read the README and result records under `research/jstack/evaluations/juan-mode-foundation/`, `juan-mode-runtime/`, `project-model-config/`, `create-verification-skill/` and `maintain-verification-skill/`. These historical records are useful, but their evaluated source hashes and explicit limitations must travel with any claim. They do not approve the architecture they evaluated.

| Evidence | Supported conclusion | Limit relevant to corrections |
| --- | --- | --- |
| Foundation and runtime records | Historical Codex inherited dispatch, explicit-path fixture edits, activation/opt-out decisions and some same-conversation continuity. | No real compaction or restart proof, no four-provider certification, no full playbook behavior. Synthetic histories are not host persistence. |
| Project configuration record and inspected resolver tests | Historical 14 resolver and 15 preflight tests exercise lookup, whole-map validation, list semantics and selected-path handoff. | Tests do not measure the setup conversation or live concrete/cross-provider execution. They also intentionally encode stricter whole-map policy, so a pass does not approve that policy. |
| Generator record | Historical CLI generation, fresh-checkout reuse, wrong output despite exit zero, retained evidence and docs-only no-op. | No browser/API/library/interactive-terminal proof; no auto-discovery or broken-baseline generation proof; this record does not validate the later universal Claude symlink behavior. |
| Maintenance record | Historical intentional CLI drift repaired, product regression preserved, unchanged map left clean. | Its supplied prompts explicitly prohibited delegation. It did not exercise the upstream parallel source wave, live publication, missing credentials, ambiguous intent or failed cleanup. |

No new runtime tests or model calls were run. The audit inspected Python test code rather than executing suites whose disposable Git fixtures create commits, because the assigned task forbids committing. Read-only comparison checks performed during this audit confirmed exact inline principle group/summary text, all 17 upstream setup role labels, byte-identical per-package MIT notices and no source diff against the fixed baseline. These checks establish those narrow facts only.

## Correction order and acceptance boundaries

1. Correct provenance placement and mapping while preserving every pin, history record and package license. This is explicitly required and does not need another design decision.
2. Restore shipped procedure structure and lost details in maintenance and generator. Preserve required T3 paths/tools and authority limits. Record unresolved invocation, unreachable-result and provider-link policies separately rather than using them to delay unrelated fidelity corrections.
3. Restore Juan-mode's sections, mandatory triggers, broad Figure-it-out priority, child freshness and reply contract. Retain its foundation-only disclosure and standalone helper boundaries.
4. Resolve dependency packaging and implement each pending procedure with its supporting tools. Keep playbooks inside Juan-mode. Bring over the pinned algorithm, not a summary of a summary, and record only the minimum tool/runtime substitutions.
5. Execute focused acceptance cases against the correction, then compare the final files again to U0/U1. Preserve historical evaluation records; add new dated evidence instead of relabeling old hashes.

A correction is reviewable when it names the upstream path/pin, exact local location, preserved algorithm, necessary substitution, actual permission basis and proof. A restored file count or a linter pass is insufficient. None of the steps above authorizes a merge, installation, new recurring schedule or unsolicited external message.

## Unresolved questions

- Is there prior explicit authorization for unconditional project-local Claude symlinks? The inspected decisions do not answer this. Do not erase such authorization if the parent can supply it.
- Should verification helpers remain manually invoked, as upstream marks them, with explicit callers such as setup allowed? Or is automatic model invocation an intentional user choice? Validate supported metadata per coordinating provider.
- Should maintenance keep upstream's separately evidenced unreachable-feature result, and may proven verifier corrections ship while a separate product regression remains open? Either policy must report actual unrun/failed coverage.
- For new setup files only, what panel cardinality and initial budget should be proposed? Existing inherited selections and list sizes are not open to unsolicited replacement.
- Is blocking an otherwise usable role because another role is stale a desired setup policy, and is rejecting all missing/retired roles preferred to upstream's defaults/migration? Preserve current files until decided.
- Resolved during parent consolidation: the 2026-10-12 standalone investigation decision explicitly assigns shared configuration and evidence guidance to setup. Preserve that ownership and the added U1 source mapping.
- How should Orchestrate resolve the pinned source's Graphite requirement versus other playbooks' explicit no-Graphite rules? A T3 transport substitution alone does not resolve forge/topology semantics.
- Which missing external helpers will be adapted as standalone packages, and which will be declared optional dependencies with verified contracts? A global catalog match alone does not answer this.

## Coverage and completion

The four-component foundation audit is complete at the mapped-file disposition level: every local and upstream path has an entry, every shipped operational file was read, the main procedure/trigger/packaging divergences are classified, and concrete correction checks are supplied. The comparison is not a full semantic-equivalence certification. It is also not a full code audit of absent orchestration/watcher implementations, a complete transitive helper audit, or a runtime support certification. Those limits are explicit so the parent can schedule the remaining work without calling absent behavior implemented.

No child work is pending. Source files remain unchanged. The only owned output is `research/jstack/fidelity-audits/2026-10-13/foundation.md`.
