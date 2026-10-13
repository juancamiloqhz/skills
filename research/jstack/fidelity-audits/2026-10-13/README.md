# Jstack fidelity audit, 2026-10-13

The shipped adaptations contain material drift from pstack. Necessary T3 substitutions and explicit user decisions explain model configuration, task ownership and authorization boundaries. They do not explain omitted reference files, shortened algorithms, changed routing priorities or merged helper boundaries. Restore those details before adding the 23 planned playbooks.

This audit is complete at the mapped-component comparison level. Corrections are pending. It does not certify semantic equivalence or runtime support.

## Scope and evidence

Compared all 36 components in `research/jstack/upstream.json` at local commit `d57d3407626f741900c9574b9ecd47421a8de96f` against each component's exact `adaptedFrom` revision. Setup and the two verification helpers use `ccb5507cec1546dc88135c1139c811e6c59115ba`; the other 33 components use `11713c683fe4add4fd403ea880580abbc9e0875f`. The source is [cursor/plugins](https://github.com/cursor/plugins). No upstream fetch or weekly review was performed. The reviewed checkpoint remains `4bf3e083c6dec126e254f96181b84a105b6e3e70`.

| Report | Components | Coverage |
| --- | --- | --- |
| [Foundation](foundation.md) | juan-mode, setup-jstack, create-verification-skill, maintain-verification-skill | 4 mapped components, all mapped paths accounted for; shipped instructions, support code and missing tool requirements assessed. |
| [Helpers](helpers.md) | how, why, arena, architect, interrogate, swarm, reflect, figure-it-out | 8 mapped components and the three source files of the missing trail helper. |
| [Principles](principles.md) | All 24 principle-* mappings | Every leaf and license, plus immediate helper dependencies. |

[Inventory](inventory.json) records hashes and sizes for 112 local files and 108 upstream files. Counts establish coverage, not behavior. [Task records](tasks.json) identify the three completed delegated comparisons and parent spot checks. Detailed reports name exact paths, pins, differences, dispositions and proposed verification. Proposed checks have not run.

The parent independently checked removed maintenance delegation, mode triggers and Figure-it-out priority, missing generator examples, Why's reference inventory, the trail-helper composition rule, compressed Interrogate criteria, and three principle bodies against their pins. These checks support the main findings; they are not an independent reread of every source line.

## What must remain

Preserve the user's saved model selections and inherited effort, project/global configuration precedence, activation until opt-out, standalone helpers and principles, inline principle groups, manual installation and separate merge authority. Preserve task scope and explicit checkpoints without asking again for work already authorized. Do not restore upstream's unsolicited external actions.

Keep supported T3 catalog discovery, explicit configuration handoff, child ownership and terminal-state checks, parent-owned PR watches, actual host tools and protection of unrelated work. Record the precise source behavior each substitution preserves and any remaining gap. A tool schema does not replace an investigation method; a passing fixture does not approve a rewritten algorithm.

The 2026-10-12 [standalone investigation decision](../../decisions.md#standalone-investigation-skills-2026-10-12) already assigns shared configuration and evidence guidance to setup-jstack. Parent consolidation resolved the foundation report's ownership question using that record. It does not approve deleting How and Why's prompt templates. Existing saved panel choices also remain approved; proposed defaults for new configurations are a separate question.

## Correction order

Each row is a focused correction scope, with fresh evidence required before delivery. Start with the first row, then restore the highest-impact shipped instructions. No new playbook should bypass unresolved material drift in its dependencies.

| Order | Scope | Required result and verification |
| --- | --- | --- |
| 1 | Provenance in the 12 foundation/helper packages | Move packaged upstream records to research, remove provenance-only operational pointers, repair manifest differences and research links. Preserve licenses, pins, historical evidence and the reviewed checkpoint. Check package file/link inventories and manifest validation. |
| 2 | The 24 principle bodies | Restore original organization, constructive examples, procedures and helper references. Apply only recorded narrow exceptions. Compare every leaf to its pin; exercise the benchmark, type-modeling, evidence and concurrency cases specified in the principles report. Dependencies still missing must be disclosed. |
| 3 | How and Why | Restore both How prompts and all 12 Why references. Preserve configured roles and the approved shared evidence contract. Test simple-path selection, complex exploration, contradictory sources, source-specific traps and confidence/output contracts. |
| 4 | Architect, Interrogate and Reflect | Restore complete reference templates, design remedies, review rubrics, lead filtering and reviewer/synthesis boundaries. Verify original phase order and briefs, valid exceptions, singleton defects, false positives and the repeated-friction redesign path. |
| 5 | Standalone show-me-your-work and Figure-it-out | Restore the independent helper, logger and template; map/license it; restore the caller's named phases and review gate. Test append behavior, cell sanitization, run boundaries and evidence pointers. Preserve inherited models and disclose reduced review independence. |
| 6 | Generator and maintenance | Restore worked examples, inline output requirements, original stages and parallel read-only source readers with coordinator-only live driving. Test generated instruction reuse and a multi-feature maintenance run, including failed/blocked paths and cleanup. |
| 7 | Juan-mode, setup, Arena and Swarm | Restore mode sections, mandatory triggers, broad Figure-it-out priority, child style/freshness and reply contract; restore setup steps/role table and helper phase organization. Test route priority, unavailable dependencies, inherited dispatch and phase order. Keep model-race and provider gaps explicit. |

These groups may be split further to keep reviews coherent. Shared provenance can move first because it is already explicitly required. Restoring an instruction does not establish that its workflow works; each implementation PR needs pinned-source comparison and relevant execution evidence.

## Decisions to isolate from straightforward restoration

The detailed reports distinguish missing instructions from genuine source conflicts and optional local policies. Do not ask the user to reapprove existing decisions. First check recorded authorization and actual provider capabilities, then present only unresolved choices with concrete alternatives.

- Invocation metadata must distinguish explicit use, workflow calls, catalog discovery and automatic triggering. The audits found no proof that removing upstream's manual-invocation metadata was required. Provider behavior remains unverified.
- Source heuristics and defects need narrow treatment: internal trust, even-census causality, layer/time thresholds, containment/comments, assertion controls and red-test commit interpretation. Fidelity does not justify an unsupported causal claim, bypassing a real trust boundary or suppressing a real defect.
- New setup defaults, whole-map validation, Arena's one-survivor outcome and explicitly selected Swarm race-arm models are product choices. Existing configuration must remain untouched.
- Trail review across model families conflicts with saved inherited roles. Preserve inheritance and disclose the limitation unless the user explicitly selects another reviewer. Reflect's convergence/enforcement routing and Figure-it-out's reduced judge gate also require precise dispositions if retained.
- Verification helper invocation, automatic project-local Claude links, unreachable-feature status and shipping proven verifier repairs alongside separately reported product regressions need evidence of prior authorization or a scoped decision.
- Future orchestration tools have conflicting upstream Graphite assumptions. Automatic dependency installation and unrelated transcript scanning require host/authority substitutions. Preserve actual algorithms when porting supporting tools.

## Pending dependencies and limits

Missing dependencies include benchmark-checklist, typescript-best-practices, show-me-your-work, technical-writing and no-comments. Some callers also reference external control, Deslop, TDD, Unslop or built-in authoring capabilities. The reports distinguish absent packages from separately installed skills whose pinned equivalence has not been established. Plan each dependency with its first consuming correction; a same-name catalog entry is insufficient evidence.

All 23 juan-mode playbooks remain unavailable. Their plan validator, orchestration store, watcher and worktree tools remain pending. The foundation report inventories them but does not claim a full implementation audit of absent tool code. This work does not close compaction/restart persistence, installed discovery, all-provider execution, parallel-workspace or cross-model acceptance gates.

No skills, model configuration, installations, schedules or upstream review checkpoints changed. Historical evaluations retain their original hashes, failures and limitations. This audit adds source comparison and a correction backlog; it does not relabel earlier tests as proof of fidelity.
