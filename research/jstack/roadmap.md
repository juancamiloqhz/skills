# Jstack roadmap

Status as of 2026-10-11. Model setup, verification tooling and upstream maintenance are released. All 23 poteto-mode playbooks have been assessed for `juan-mode`, and the [adaptation specification](juan-mode-spec.md) defines the complete target and staged implementation. The execution foundation now has source and bounded evaluation evidence. The 23 playbook procedures remain planned.

## Completed: setup-jstack

Model configuration and validation shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with prose formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). Release checks included six helper tests, skill validation, and Markdown linting. Setup was installed for the four selected providers and invoked successfully in a T3 Code session.

Those checks cover setup. They do not establish the behavior of a future workflow consumer.

## Completed: organize research

[PR #4](https://github.com/juancamiloqhz/skills/pull/4) established this research directory and excluded the old experiment archive from the current tree.

## Completed: create-verification-skill

[PR #6](https://github.com/juancamiloqhz/skills/pull/6) added the generator. [Evaluation](evaluations/create-verification-skill/README.md) covered a CLI fixture, independent reuse, failure detection and a documentation-only boundary. Browser and cross-provider execution remain untested. Installation and updates are manual.

## Completed: optional verification offer

[PR #7](https://github.com/juancamiloqhz/skills/pull/7) added the optional offer. After model configuration, `setup-jstack` inspects the target repository for a real application and existing verification support, then offers generation when needed. Acceptance hands off to the separately available generator. A missing generator produces manual installation instructions; declining or a failed generation leaves the saved model configuration intact.

## Completed: maintain-verification-skill

Released in [PR #8](https://github.com/juancamiloqhz/skills/pull/8). Maintain an existing project-local verification skill in place. Review every mapped feature against source, exercise it through the public interface, repair evidenced drift within the skill directory, and report product regressions without weakening expectations. Delivery follows the requested task; invoking maintenance alone does not create a PR. The [evaluation](evaluations/maintain-verification-skill/README.md) records deliberate application changes, a regression, and an unchanged baseline. Installation remains manual.

## Completed: upstream maintenance

Released in [PR #12](https://github.com/juancamiloqhz/skills/pull/12). The [upstream maintenance procedure](upstream-maintenance.md) and manifest support source change detection, complete impact reviews and retained decisions. The [first review](upstream-reviews/2026-10-11.md) covers the manual trial. The weekly review is enabled in the skills project and bound to the [jstack conversation](t3-thread://v1/5f7384b2-cbbe-431f-942d-929f327635a1). Its report delivery and fresh completion receipt were verified on 2026-10-11 before the old lifeOS schedule was deleted. Implementation recommendations require approval, merges remain separate, and installation stays manual.

## Completed: assess the complete playbook set

Adapt poteto-mode's working approach through the `juan-mode` entrypoint: shared engineering principles, task routing, scoped delegation, review and verification. The [initial source assessment](juan-mode-adaptation.md) led to a broader review of all 23 playbooks. The user accepted the full-set target and grouped implementation, superseding the earlier three-playbook first-release plan.

The [specification](juan-mode-spec.md) links all three inventories, maps shared dependencies, records T3 Code substitutions and defines acceptance scenarios. Playbooks stay inside `juan-mode`; how and why are standalone skills, while remaining helper packaging is assessed during implementation. Existing configuration and verification contracts remain the starting point.

The user selected explicit activation that stays in effect for subsequent tasks in the same conversation until turned off. That preference is settled. How each supported provider preserves or reloads the instruction across compaction and session resume must be demonstrated; Cursor's mode metadata alone does not establish it in T3 Code.

## In progress: implement and prove the execution foundation

The [entrypoint](../../skills/jstack/juan-mode/SKILL.md), complete route registry, installed-dependency discovery, model preflight and explicit delegation contract are implemented. The [evaluation record](evaluations/juan-mode-foundation/README.md) distinguishes executed checks from remaining gaps. A registry entry is not a claim that its route already works.

The preflight uses the separately discovered `setup-jstack` resolver and preserves the saved 17-role map. Tests cover inherited and concrete selections, ordered panels, stale settings, capability failures and configuration reloads. Live evaluation checks the current inherited Codex selection and assigned-path shell execution. Full persistence after compaction or provider restart, other coordinating providers and other editing tools still require execution evidence before completing this foundation group.

Optional project configuration extends this foundation. Setup and juan-mode share one lookup with explicit file, environment, project and global precedence. Project setup seeds a complete map from global settings, and children retain the selected absolute path across worktrees. The [project configuration evaluation](evaluations/project-model-config/README.md) records CLI coverage and compatibility with the older installed helper. It does not change the remaining workflow persistence requirements.

The later [installed runtime evaluation](evaluations/juan-mode-runtime/README.md) verifies both updated installations, inherited Codex model and effort, and absolute-path `apply_patch` edits confined to an assigned worktree. Six synthetic activation histories match the written recovery rules. The available T3 tools expose no compaction or provider-process restart operation, so those runtime gates remain unverified. A live catalog capture exceeded the shell argument limit; the shared integration guidance now covers file-tool, streamed or bounded-chunk capture.

## Then: implement the complete set in groups

Follow the [implementation groups](juan-mode-spec.md#implementation-groups): shared procedures; engineering and experiments; delivery and recovery; autonomous coordination; then full release verification. Each group can span several focused PRs. The target includes advanced autopilot, stacked-PR shipping and multi-day coordination; they are later implementation groups, not automatically deferred product scope.

The shared-procedure group starts with standalone [how](../../skills/jstack/how/SKILL.md), [why](../../skills/jstack/why/SKILL.md) and their shared [evidence contract](../../skills/jstack/setup-jstack/references/investigation.md). These skills explain behavior and investigate rationale using configured roles. Their [evaluation](evaluations/shared-investigation/README.md) records read-only fixture coverage. Standalone [Arena](../../skills/jstack/arena/SKILL.md) now provides candidate comparison and design-only synthesis, with [bounded evaluation](evaluations/arena/README.md). Standalone [Architect](../../skills/jstack/architect/SKILL.md) builds on this comparison with grounded, structurally distinct sketches and an explicit design-only return. Its [evaluation](evaluations/architect/README.md) records a recovered comparison, initial dispatch failures and the remaining untested branches. A later [runtime evaluation](evaluations/architect/runtime/README.md) verifies authorized implementation and stopping at an explicit checkpoint, while preserving procedural deviations. Standalone [Interrogate](../../skills/jstack/interrogate/SKILL.md) adds report-only code and design review with configured reviewers and checked lead judgment. Standalone [Swarm](../../skills/jstack/swarm/SKILL.md) adds partitioned coverage and declared races with checked aggregation. Reflect, custom planning and principle mapping remain in this group; no playbook is marked implemented by the helper work. The unresolved foundation persistence gates remain release requirements while shared-procedure work proceeds.

Use T3 Code's child-task and parent-owned PR-watch lifecycle. Adapt upstream support scripts to actual requirements rather than copying fixed cloud-lane, Graphite, scheduler or cleanup assumptions. Preserve each playbook's purpose and record intentional behavior differences. Reducing the release scope requires a separate decision.

## Release checks: evaluate observable behavior

Run a representative case for each of the 23 routes, plus common-contract and failure-path evaluations. Demonstrate correct routing, concrete and inherited model assignments, stale configuration rejection, explicit child context, fresh review rounds, unavailable dependencies, protected user work and accurate completion reporting. Each inventory entry supplies a concrete acceptance scenario. Files, static validation and child self-reports alone do not establish support.

Verify the accepted conversation-persistence behavior and publish the coordinating-provider, child-provider and platform coverage actually exercised. The specification identifies resume, delegated-workspace isolation, merge continuation and trace visibility as engineering investigations. Missing capability must remain visible instead of becoming a false pass. Merge completed work before installation; the user installs and updates skills manually.

## Beyond the initial upstream set

Assess newly added upstream playbooks, extra platform support and standalone helper packaging through the existing maintenance process. The full 23-playbook target does not require porting unrelated pstack skills or installing all referenced capabilities on every host.
