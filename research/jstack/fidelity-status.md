# Jstack fidelity status

As of 2026-10-15, at merged PR #37, commit `d4cfe22`. The seven correction groups in the [original audit](fidelity-audits/2026-10-13/README.md) now have merged source restorations. Required helper dependencies and runtime checks remain open. All 23 playbook procedures remain unimplemented.

This record reconciles the existing audit with current files and recorded evaluations. It is not a new full semantic audit or a fresh workflow evaluation. The original reports and test artifacts retain their dates, failures and limits. This record and the [fidelity policy](upstream-fidelity.md) supersede the initial specification/inventories wherever those propose bundled standalone helpers, shortened algorithms or optional redesign without a user decision.

## Merged corrections

The original 36 mapped components now total 37 because Show me your work is standalone. Pins remain `ccb5507cec1546dc88135c1139c811e6c59115ba` for setup and the two verification helpers, and `11713c683fe4add4fd403ea880580abbc9e0875f` for the other 34. The reviewed checkpoint remains `4bf3e083c6dec126e254f96181b84a105b6e3e70`.

| Original correction group | Merged result | Evidence and remaining limit |
| --- | --- | --- |
| 1. Provenance | PR #28 moved 12 adaptation records to research. Licenses and operational procedures remain in packages. | [Packaging record](adaptations/README.md). This closed provenance placement, not behavior findings. |
| 2. Principles | PR #29 restored all 24 bodies and dependency calls, with seven narrow exceptions. | [Differences](principle-adaptations.md), [source and bounded exercises](evaluations/principle-restoration/README.md). Benchmark and TypeScript helpers are absent; principle invocation metadata remains unresolved. |
| 3. How and Why | PR #30 restored both How prompts, all 12 Why references, source organization and source-specific investigation rules. | [Final alignment comparison](evaluations/investigation-restoration/alignment-review/README.md). Live connectors and all-provider discovery remain unverified. |
| 4. Architect, Interrogate, Reflect | PR #31 restored all eleven supporting references, review criteria, phase order and synthesis classifications. | [Evaluation](evaluations/design-review-restoration/README.md). Template exercises do not establish full execution of each restored orchestrator. PR #36 later corrected Architect's caller sentence. |
| 5. Trail and Figure it out | PR #32 restored the standalone trail package, exact logger/template, original phases and mandatory per-unit judging. | [Evaluation](evaluations/trail-restoration/README.md). Real logger and bounded audit/review passed; full delegated implementation and model-family diversity remain unproven. |
| 6. Verification helpers | PR #33 restored generator examples, inline requirements, maintenance's source wave, live-pass order and evidenced unreachable classification. | [Evaluation](evaluations/verification-restoration/README.md). CLI cases passed; browser and other-provider use remain untested. Automatic Claude linking is an explicit user decision. |
| 7. Mode, setup, Arena, Swarm | PRs #34–37 restored mode triggers/style, setup steps/map, Arena phases/dropout handling and Swarm phases/task-local arm selection. | [Mode](evaluations/mode-restoration/README.md), [setup](evaluations/setup-restoration/README.md), [Arena](evaluations/arena-restoration/README.md), [Swarm](evaluations/swarm-restoration/README.md). Inherited fixture runs do not prove concrete cross-model races, provider persistence or the missing playbooks. |

The original findings about Reflect's already-enforced Backlog, Figure-it-out's required judge, maintenance's `verified-unreachable` result and Arena's ordinary sole-survivor result were resolved by restoring source behavior. They are not new user preference questions. Architect still requires two structurally distinct designs. Preserve the [recorded setup and linking decisions](decisions.md), inherited model choices, task authority and manual installation.

## Missing or unverified helper dependencies

The source paths below use pin `11713c683fe4add4fd403ea880580abbc9e0875f`. They are dependency targets, not new adaptation pins or implemented mappings. Each port must enumerate all source files, preserve its boundary, add the license and manifest mapping/context dependencies, document necessary differences, and test the affected caller behavior.

| Dependency | Exact source scope | Current disposition and first affected caller |
| --- | --- | --- |
| Benchmark checklist | `pstack/skills/benchmark-checklist/SKILL.md` | No jstack package. Next port. Required by Explain the Number and Juan-mode measurement triggers; later Perf issue and Hillclimb depend on it. |
| TypeScript best practices | `pstack/skills/typescript-best-practices/SKILL.md` and `references/patterns.md` | No jstack package. Conditional dependency of Type System Discipline. Preserve both files; correct the known claim that plain numeric duration excludes negative ranges. |
| Technical writing | `pstack/skills/technical-writing/SKILL.md` | No jstack package. Required by the mode's documentation/PR trigger. Preserve all four layers, document modes and the worked example. Assess its Unslop dependency alongside it. |
| No comments | `pstack/skills/no-comments/SKILL.md` and `pstack/agents/comment-sicko.md` | Neither is packaged. Required before mode-led review. Assess the complete reviewer and skill together, including exceptions, rejection/rerun limits, How/Why calls, scoped fixes and constraint encodings. Record precise authority/repository conflicts; do not replace the whole procedure by preference. |
| Unslop and TDD | `pstack/skills/unslop/SKILL.md`; `pstack/skills/tdd/SKILL.md` | Same-name skills are available in this session, but are not jstack packages with established pinned equivalence. Decide faithful external reuse or a standalone port after comparison. Unslop affects writing/trail calls; TDD affects Bug fix. |
| Deslop | `cursor-team-kit/skills/deslop/SKILL.md` | External pre-commit dependency. No jstack package or verified external-equivalence record. Keep its own boundary; a formatter is not a substitute. |
| Control CLI and UI | `cursor-team-kit/skills/control-cli/SKILL.md`; `cursor-team-kit/skills/control-ui/SKILL.md` | External execution dependencies. Existing preview tools and project verifiers supply bounded capabilities, not equivalence to both skills. Assess CLI/TUI and browser/Electron requirements with the consuming route. |
| Skill authoring and ordinary child style | Cursor built-in `create-skill`; `pstack/agents/poteto-agent.md` | Host authoring guidance and full-mode/leaf reads are documented substitutions. The mode restoration exercises the child-style contract. This does not prove provider installation or every authoring workflow. |

On this date, the advertised `/home/ubuntu/.agents/skills/setup-jstack` lacks both `references/investigation.md` and the `--worker-override` flag. The repository source contains both. This is an installation-version gap, not a request to change settings or copy the resolver elsewhere. Update manually before testing installed consumers that need those features. This inspection covers that advertised path, not every provider's loader or installation.

## Open policy and runtime checks

| Check | Existing evidence | Requirement still open |
| --- | --- | --- |
| Invocation metadata | The [How/Why compatibility assessment](evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) shows a concrete Claude catalog-call conflict. Later helper records cite that exception. | The 24-principle record still marks its metadata disposition pending. Compare actual direct, workflow and automatic invocation for each intended provider before closing it. Do not infer explicit-only behavior or extend a bounded guard probe into an end-to-end claim. |
| Installed discovery and configuration handoff | Earlier installed Codex checks and recent explicit-authoring-path exercises. | Verify the updated installed packages, independent locations, helper calls and selected absolute config propagation. Same-name catalog entries and repository files alone do not pass this check. |
| Activation until opt-out | Written recovery rules and six synthetic histories. | Demonstrate compaction, resume/restart and opt-out persistence on each claimed coordinating provider. No current record proves those transitions. |
| Delegated workspaces | Earlier explicit-path shell/editor tests; current T3 worktree contract documented. | Exercise app-bound `isolation: "worktree"`, committed input identity, config handoff, writes and cleanup. Earlier path tests do not prove this newer binding path. |
| Model/provider dispatch | Inherited Codex fixtures and concrete target validation tests. | Execute concrete selections and cross-provider children, preserving options and reporting unavailable diversity. Fresh inherited agents do not establish different model families. |
| Recovery and continuation | Bounded assessments of retry, dropout and cancellation decisions. | Induce real failures/cancellation and inspect terminal state, owned outputs and safe recovery. Validate program continuation after PR merge/watch completion. |
| Procedure-specific behavior | Each evaluation records its own exercised cases. | Carry remaining checks into the relevant caller: live investigation connectors, full Reflect orchestration, delegated Figure-it-out implementation and real browser verification, among others. Do not treat this list as exhaustive test coverage. |

These checks constrain support and release claims. They do not prohibit independent authoring work. Before marking a route implemented, resolve material drift and missing dependencies that its actual path needs, compare the full source procedure and support files, and run its acceptance case. An unmet prerequisite stays visible; no generic fallback can stand in for the named workflow.

## Next implementation and later tools

Next is a focused standalone benchmark-checklist PR. Preserve the source's introduction, ballpark exception, preparation, seven questions, Report and Other perf material sections. Keep profiling outside reported runs, production tuning on both sides, physical-limit arithmetic, error/output checks, at least five alternating runs per side, median/range, end-to-end relevance and proof that work occurred inside the timed region. Its references to Opening a PR, Perf issue and Hillclimb do not implement those routes.

Verification should include a real bounded workload with recorded errors/work counts and alternating measurements, plus counterexamples for a no-op timer, fast failures, an untuned comparison and an unsupported speedup. Test the one-run user-requested ballpark exception separately from choosing between options. If profiling or other prerequisites are unavailable, report the relevant conclusion as inconclusive. Do not install tools or change model settings to make a case pass.

Then address the remaining standalone dependencies and invocation question in focused work, before enabling their consuming routes. This preserves the accepted all-23 target and grouped implementation. It does not require porting unrelated pstack skills.

The 23 source playbooks still have no local procedure files. The mode comparison also records pending supporting paths. Port tools with their first consuming procedure and retain the [original audit's algorithm requirements](fidelity-audits/2026-10-13/foundation.md#f7-preserve-pending-tool-algorithms-and-resolve-upstream-contradictions-before-porting): ordered plan blocks and ten live proof lanes; watcher blocker priority and stale-head invalidation; contiguous verified stack landing; orchestration ledger/gates/frontier and atomicity; manual dependency prerequisites; and conservative worktree ownership checks. The conflicting upstream Graphite assumptions need a concrete frontier decision. A host PR watch replaces waiting, not independent merge-readiness verification.

## Reconciliation checks

Re-ran all nine existing restoration `compare.py` scripts against the shared pinned upstream cache. Seven outputs match their recorded comparisons exactly, using How/Why's final alignment record. The design/review output differs only in Architect's later caller sentence, covered by the matching Arena comparison. Setup differs only in the three support files changed by Swarm, covered by the matching Swarm comparison. Historical snapshots remain unchanged.

Enumerated the 37 manifest mappings, all nine dependency directories above, the external Comment Sicko source, 23 upstream playbooks and zero local playbooks. Read the original findings, current adaptation/evaluation records and complete benchmark, technical-writing and no-comments sources. Reconciliation does not re-audit every unported transitive tool. No upstream fetch, weekly review, new runtime test, skill edit, installation, model change or schedule change was performed. The global model-file hash remains `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`.

The specification now removes stale instructions to bundle helpers, keep the trail inside Figure-it-out, replace No-comments wholesale or drop source validator obligations. This is a research-plan correction under the fidelity policy; operational behavior and all source pins remain unchanged.
