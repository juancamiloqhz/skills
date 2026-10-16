# Jstack roadmap

Current jstack skill identities use the `jstack-` prefix. See the [name mapping and manual migration guide](skill-names.md). Earlier assessments and evaluation artifacts retain their original names; current local links point to the renamed packages.

For jstack implementation and maintenance, follow the [upstream-fidelity policy](upstream-fidelity.md). Preserve upstream structure by default and document only necessary or explicitly approved deviations.

Status as of 2026-10-16. Model setup, verification tooling and upstream maintenance are released. All 23 poteto-mode playbooks have been assessed for `jstack-juan-mode`, and the [adaptation specification](juan-mode-spec.md) defines the complete target and staged implementation. The execution foundation now has source and bounded evaluation evidence. Investigation, Prototype, Trace forensics, Authoring or modifying a skill and Runtime forensics are implemented with bounded evaluations; the other 18 procedures remain planned.

## Current priority: restore upstream fidelity

The [2026-10-13 audit](fidelity-audits/2026-10-13/README.md) compared all 36 mapped components with their exact source pins. It found material drift in shipped instructions and missing supporting references. Its seven correction groups have merged source restorations through PR #37. The [current fidelity status](fidelity-status.md) maps them to their evidence and distinguishes unresolved dependencies, invocation policy and runtime checks. It does not certify full behavioral equivalence. Complete the relevant dependency corrections before adding their consuming playbooks. Existing bounded evaluation records remain historical evidence, not proof of upstream equivalence.

The first correction moved the 12 foundation/helper attribution records into [research-owned adaptation records](adaptations/README.md), preserving licenses and operational instructions. That packaging change did not close behavioral findings.

PR #29 restored all 24 principle bodies from their exact pin, with [recorded narrow differences](principle-adaptations.md) and [source comparison plus bounded runtime evidence](evaluations/principle-restoration/README.md). Missing helper dependencies and provider invocation policy remain open.

Merged PR #30 restored How and Why's entrypoint organization, both How prompts and all 12 Why references. [Restoration evidence](evaluations/investigation-restoration/README.md) separates exact-source comparison from inherited-agent fixture exercises. Configured delegation and the approved shared investigation contract remain in place. Merged PR #31 restored Architect, Interrogate and Reflect from the same pin, including all eleven original supporting references. Their [source comparison and bounded template evaluation](evaluations/design-review-restoration/README.md) document remaining runtime and authority differences. Merged PR #32 restored standalone show-me-your-work and Figure it out's original phases and mandatory unit judging, with [source comparison and bounded evaluation](evaluations/trail-restoration/README.md). Merged PR #33 restored the verification generator's worked examples and inline requirements, plus maintenance's parallel source wave and coordinator-owned live pass. Its [comparison and bounded evaluation](evaluations/verification-restoration/README.md) retain automatic Claude linking by explicit user choice. Merged PR #34 restored Juan-mode's original sections, mandatory triggers, inline routes, child style/freshness and reply contract, with [source comparison and bounded evaluation](evaluations/mode-restoration/README.md). Merged PR #35 restored setup's seven steps and inline role map, with two inherited seats for new comparison panels and whole-configuration validation retained by [explicit user decision](decisions.md#setup-defaults-and-validation-2026-10-15). Its [source comparison and isolated setup evaluation](evaluations/setup-restoration/README.md) preserve existing settings. Merged PR #36 restored Arena's six phases, principle routes and N-1 dropout continuation, with [source comparison and bounded evaluation](evaluations/arena-restoration/README.md). Architect still requires two structurally distinct candidates. Merged PR #37 restored Swarm's original phases and explicit task-local race-arm selections, with [source comparison and bounded evaluation](evaluations/swarm-restoration/README.md). Standalone benchmark-checklist now supplies the measurement dependency, with [source comparison and bounded evaluation](evaluations/benchmark-checklist/README.md). Standalone `jstack-technical-writing` now preserves the four writing layers, modes and worked example, with a version-specific external Unslop assessment and [bounded documentation exercises](evaluations/technical-writing/README.md). Standalone `jstack-no-comments` now supplies the complete Comment Sicko reviewer and parent review/fix procedure, with [bounded evaluation](evaluations/no-comments/README.md). Standalone `jstack-typescript-best-practices` now supplies both source files and the Type System Discipline route, with [compiler and caller evaluation](evaluations/typescript-best-practices/README.md). Remaining helper dependencies and provider checks are tracked in the current status; Investigation, Prototype, Trace forensics, Authoring or modifying a skill and Runtime forensics are now available and the other 18 playbooks remain pending. Provider and persistence release checks remain open while bounded source work proceeds. These corrections do not complete the broader fidelity backlog.

## Implemented: Investigation playbook

The [Investigation procedure](../../skills/jstack/jstack-juan-mode/playbooks/investigation.md) is now bundled inside Juan-mode. It routes through How and conditional Why, preserves cited facts and uncertainty, and returns an answer without source edits or publication. Its [evaluation](evaluations/investigation-playbook/README.md) distinguishes live inherited-provider execution from staged failure cases and unverified installed/cross-provider coverage. Missing dependencies still leave the affected run incomplete.

## Implemented: Prototype playbook

The [Prototype procedure](../../skills/jstack/jstack-juan-mode/playbooks/prototype.md) builds isolated throwaway variants, observes their behavior and returns evidence plus a design recommendation. Its [evaluation](evaluations/prototype-playbook/README.md) covers a real nonvisual experiment and staged boundaries. Visual proof still requires the intended external control skill and actual screenshot/interaction evidence. A prototype does not become the production implementation; Feature remains pending.

## Implemented: Trace forensics playbook

The [Trace forensics procedure](../../skills/jstack/jstack-juan-mode/playbooks/trace-forensics.md) analyzes supplied artifacts through a queryable SQLite representation, attributes findings to source symbols and distinguishes paired evidence from unconfirmed hypotheses. Its [evaluation](evaluations/trace-forensics/README.md) exercises synthetic mapped and unmapped CPU profiles. It does not rerun an application or apply a fix. Heap/spindump analysis and real-world capture validation remain untested.

## Implemented: Authoring or modifying a skill

The [authoring procedure](../../skills/jstack/jstack-juan-mode/playbooks/authoring-a-skill.md) uses the host authoring skill, validates package and helper references, tests structural changes and preserves the requested delivery boundary. Its [evaluation](evaluations/authoring-a-skill/README.md) covers a local router change and a wording-only edit. Opening a PR remains a pending procedure; publishing, merging and installation retain their existing authority requirements.

## Implemented: Runtime forensics

The [Runtime forensics procedure](../../skills/jstack/jstack-juan-mode/playbooks/runtime-forensics.md) captures a live signal, tests its mechanism with authorized temporary instrumentation and maps the diagnosis to source. Its [evaluation](evaluations/runtime-forensics/README.md) separates real profiling of an owned fixture from production performance claims. Source files remain unchanged; runtime state is restored and owned processes are cleaned up. Heap leaks, visual glitches and other providers retain separate verification gates.

## Implemented dependency: Control CLI

The standalone [jstack-control-cli helper](../../skills/jstack/jstack-control-cli/SKILL.md) supplies the terminal-control dependency for future engineering playbooks. Its [evaluation](evaluations/control-cli/README.md) covers an actual PTY prompt flow, startup timeout, early exit and owned-process cleanup. The pinned Python example's silent timeout is corrected with retained before/after evidence. Runtime forensics now has its own bounded live CPU-profile evaluation. Other consuming playbooks remain pending; rich TUI input and Control UI still require separate proof.

## Completed: jstack-setup

Model configuration and validation shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with prose formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). Release checks included six helper tests, skill validation, and Markdown linting. Setup was installed for the four selected providers and invoked successfully in a T3 Code session.

Those checks cover setup. They do not establish the behavior of a future workflow consumer.

## Completed: organize research

[PR #4](https://github.com/juancamiloqhz/skills/pull/4) established this research directory and excluded the old experiment archive from the current tree.

## Completed: create-verification-skill

[PR #6](https://github.com/juancamiloqhz/skills/pull/6) added the generator. [Evaluation](evaluations/create-verification-skill/README.md) covered a CLI fixture, independent reuse, failure detection and a documentation-only boundary. Browser and cross-provider execution remain untested. Installation and updates are manual.

## Completed: optional verification offer

[PR #7](https://github.com/juancamiloqhz/skills/pull/7) added the optional offer. After model configuration, `jstack-setup` inspects the target repository for a real application and existing verification support, then offers generation when needed. Acceptance hands off to the separately available generator. A missing generator produces manual installation instructions; declining or a failed generation leaves the saved model configuration intact.

## Completed: maintain-verification-skill

Released in [PR #8](https://github.com/juancamiloqhz/skills/pull/8). Maintain an existing project-local verification skill in place. Review every mapped feature against source, exercise it through the public interface, repair evidenced drift within the skill directory, and report product regressions without weakening expectations. Delivery follows the requested task; invoking maintenance alone does not create a PR. The [evaluation](evaluations/maintain-verification-skill/README.md) records deliberate application changes, a regression, and an unchanged baseline. Installation remains manual.

## Completed: upstream maintenance

Released in [PR #12](https://github.com/juancamiloqhz/skills/pull/12). The [upstream maintenance procedure](upstream-maintenance.md) and manifest support source change detection, complete impact reviews and retained decisions. The [first review](upstream-reviews/2026-10-11.md) covers the manual trial. The weekly review is enabled in the skills project and bound to the [jstack conversation](t3-thread://v1/5f7384b2-cbbe-431f-942d-929f327635a1). Its report delivery and fresh completion receipt were verified on 2026-10-11 before the old lifeOS schedule was deleted. Implementation recommendations require approval, merges remain separate, and installation stays manual.

## Completed: assess the complete playbook set

Adapt poteto-mode's working approach through the `jstack-juan-mode` entrypoint: shared engineering principles, task routing, scoped delegation, review and verification. The [initial source assessment](juan-mode-adaptation.md) led to a broader review of all 23 playbooks. The user accepted the full-set target and grouped implementation, superseding the earlier three-playbook first-release plan.

The [specification](juan-mode-spec.md) links all three inventories, maps shared dependencies, records T3 Code substitutions and defines acceptance scenarios. Playbooks stay inside `jstack-juan-mode`; how and why are standalone skills, while remaining helper packaging is assessed during implementation. Existing configuration and verification contracts remain the starting point.

The user selected explicit activation that stays in effect for subsequent tasks in the same conversation until turned off. That preference is settled. How each supported provider preserves or reloads the instruction across compaction and session resume must be demonstrated; Cursor's mode metadata alone does not establish it in T3 Code.

## In progress: implement and prove the execution foundation

The [entrypoint](../../skills/jstack/jstack-juan-mode/SKILL.md), complete route registry, installed-dependency discovery, model preflight and explicit delegation contract are implemented. The [evaluation record](evaluations/juan-mode-foundation/README.md) distinguishes executed checks from remaining gaps. A registry entry is not a claim that its route already works.

The preflight uses the separately discovered `jstack-setup` resolver and preserves the saved 17-role map. Tests cover inherited and concrete selections, ordered panels, stale settings, capability failures and configuration reloads. Live evaluation checks the current inherited Codex selection and assigned-path shell execution. Full persistence after compaction or provider restart, other coordinating providers and other editing tools still require execution evidence before completing this foundation group.

Optional project configuration extends this foundation. Setup and jstack-juan-mode share one lookup with explicit file, environment, project and global precedence. Project setup seeds a complete map from global settings, and children retain the selected absolute path across worktrees. The [project configuration evaluation](evaluations/project-model-config/README.md) records CLI coverage and compatibility with the older installed helper. It does not change the remaining workflow persistence requirements.

The later [installed runtime evaluation](evaluations/juan-mode-runtime/README.md) verifies both updated installations, inherited Codex model and effort, and absolute-path `apply_patch` edits confined to an assigned worktree. Six synthetic activation histories match the written recovery rules. The available T3 tools expose no compaction or provider-process restart operation, so those runtime gates remain unverified. A live catalog capture exceeded the shell argument limit; the shared integration guidance now covers file-tool, streamed or bounded-chunk capture.

## Then: implement the complete set in groups

Follow the [implementation groups](juan-mode-spec.md#implementation-groups): shared procedures; engineering and experiments; delivery and recovery; autonomous coordination; then full release verification. Each group can span several focused PRs. The target includes advanced autopilot, stacked-PR shipping and multi-day coordination; they are later implementation groups, not automatically deferred product scope.

The shared-procedure group starts with standalone [how](../../skills/jstack/jstack-how/SKILL.md), [why](../../skills/jstack/jstack-why/SKILL.md) and their shared [evidence contract](../../skills/jstack/jstack-setup/references/investigation.md). These skills explain behavior and investigate rationale using configured roles. Their [evaluation](evaluations/shared-investigation/README.md) records read-only fixture coverage. Standalone [Arena](../../skills/jstack/jstack-arena/SKILL.md) now provides candidate comparison and design-only synthesis, with [bounded evaluation](evaluations/arena/README.md). Standalone [Architect](../../skills/jstack/jstack-architect/SKILL.md) builds on this comparison with grounded, structurally distinct sketches and an explicit design-only return. Its [evaluation](evaluations/architect/README.md) records a recovered comparison, initial dispatch failures and the remaining untested branches. A later [runtime evaluation](evaluations/architect/runtime/README.md) verifies authorized implementation and stopping at an explicit checkpoint, while preserving procedural deviations. Standalone [Interrogate](../../skills/jstack/jstack-interrogate/SKILL.md) adds report-only code and design review with configured reviewers and checked lead judgment. Standalone [Swarm](../../skills/jstack/jstack-swarm/SKILL.md) adds partitioned coverage and declared races with checked aggregation. Standalone [Reflect](../../skills/jstack/jstack-reflect/SKILL.md) adds bounded session assessment, three configured review lenses and separate synthesis; its [evaluation](evaluations/reflect/README.md) records bounded synthesis and preserved assessment boundaries. Standalone [Figure it out](../../skills/jstack/jstack-figure-it-out/SKILL.md) adds custom planning and verified execution units; the restored standalone [Show me your work](../../skills/jstack/jstack-show-me-your-work/SKILL.md) owns its decision trail. The earlier [Figure-it-out evaluation](evaluations/figure-it-out/README.md) records planning-only return, real CLI execution and a corrected audit-reporting failure. It discovers its relevant principles from the catalog, while jstack-juan-mode uses the [24-Principles section](../../skills/jstack/jstack-juan-mode/SKILL.md#principles) to reach standalone skills; the [evaluation](evaluations/principles/README.md) records eight tabletop scenarios and a corrected source omission; no playbook is marked implemented by the helper work. The unresolved foundation persistence gates remain release requirements while shared-procedure work proceeds.

Use T3 Code's child-task and parent-owned PR-watch lifecycle. Adapt upstream support scripts to actual requirements rather than copying fixed cloud-lane, Graphite, scheduler or cleanup assumptions. Preserve each playbook's purpose and record intentional behavior differences. Reducing the release scope requires a separate decision.

## Release checks: evaluate observable behavior

Run a representative case for each of the 23 routes, plus common-contract and failure-path evaluations. Demonstrate correct routing, concrete and inherited model assignments, stale configuration rejection, explicit child context, fresh review rounds, unavailable dependencies, protected user work and accurate completion reporting. Each inventory entry supplies a concrete acceptance scenario. Files, static validation and child self-reports alone do not establish support.

Verify the accepted conversation-persistence behavior and publish the coordinating-provider, child-provider and platform coverage actually exercised. The specification identifies resume, delegated-workspace isolation, merge continuation and trace visibility as engineering investigations. Missing capability must remain visible instead of becoming a false pass. Merge completed work before installation; the user installs and updates skills manually.

## Beyond the initial upstream set

Assess newly added upstream playbooks, extra platform support and standalone helper packaging through the existing maintenance process. The full 23-playbook target does not require porting unrelated pstack skills or installing all referenced capabilities on every host.
