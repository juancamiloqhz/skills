# Skills

[![skills.sh](https://skills.sh/b/juancamiloqhz/skills)](https://skills.sh/juancamiloqhz/skills)

Reusable agent skills for Codex and other tools that support the open Agent Skills format.

This repository is the canonical source for skills I have developed and validated through real project work. Each skill is self-contained under [`skills/`](./skills) and includes a `SKILL.md` entrypoint plus only the resources its workflow needs.

## Catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [`agent-instructions`](./skills/agent-instructions) | Audits, proposes, creates, and repairs repository `AGENTS.md` and `CLAUDE.md` files using repository evidence and harness-aware loading rules. | Experimental |
| [`agent-workflow-readiness`](./skills/agent-workflow-readiness) | Audits a repository's architecture, domain documentation, ADR candidates, agent instructions, and issue tracker before agent-workflow setup. | Experimental |
| [`deep-understanding`](./skills/deep-understanding) | Makes the human's understanding a first-class deliverable through incremental explanation, active recall, and lightweight knowledge checks. | Experimental |
| [`setup-jstack`](./skills/jstack/setup-jstack) | Configures jstack workflow roles using T3 Code's live provider/model catalog, reasoning budgets, global defaults and optional project settings. | Experimental; configuration helper tested |
| [`juan-mode`](./skills/jstack/juan-mode) | Provides conversation activation, a 23-route registry and configured delegation preflight. | Foundation only; playbooks pending; see [evaluation](./research/jstack/evaluations/juan-mode-foundation/README.md) |
| [`how`](./skills/jstack/how) | Explains runtime flow, component ownership and failure behavior using configured investigation roles. | Experimental; see [evaluation](./research/jstack/evaluations/shared-investigation/README.md) |
| [`why`](./skills/jstack/why) | Investigates historical rationale, contradictions and unknowns using relevant evidence sources. | Experimental; see [evaluation](./research/jstack/evaluations/shared-investigation/README.md) |
| [`arena`](./skills/jstack/arena) | Compares configured candidates, selects one cross-judge and synthesizes a verified artifact. | Experimental; see [evaluation](./research/jstack/evaluations/arena/README.md) |
| [`architect`](./skills/jstack/architect) | Grounds competing design sketches and returns a design or continues with authorized implementation. | Experimental; see [evaluation](./research/jstack/evaluations/architect/README.md) |
| [`interrogate`](./skills/jstack/interrogate) | Challenges code or designs with configured reviewers and a checked, report-only verdict. | Experimental; see [evaluation](./research/jstack/evaluations/interrogate/README.md) |
| [`swarm`](./skills/jstack/swarm) | Coordinates configured workers for coverage or races and verifies one consolidated result. | Experimental; see [evaluation](./research/jstack/evaluations/swarm/README.md) |
| [`reflect`](./skills/jstack/reflect) | Reviews bounded session evidence through three lenses and proposes verified guidance changes or structural fixes. | Experimental; see [evaluation](./research/jstack/evaluations/reflect/README.md) |
| [`figure-it-out`](./skills/jstack/figure-it-out) | Designs a custom workflow with measured units, scoped execution and a reviewed decision trail. | Experimental; see [evaluation](./research/jstack/evaluations/figure-it-out/README.md) |
| [`create-verification-skill`](./skills/jstack/create-verification-skill) | Generates project-local verification instructions and exercises a real feature with evidence and cleanup. | Experimental; see [evaluation](./research/jstack/evaluations/create-verification-skill/README.md) |
| [`maintain-verification-skill`](./skills/jstack/maintain-verification-skill) | Audits existing verification instructions against source and live behavior, repairs drift, and reports product regressions. | Experimental; see [evaluation](./research/jstack/evaluations/maintain-verification-skill/README.md) |

## Engineering principles

These 24 jstack skills are independently installable and discoverable. Juan-mode and Figure-it-out load relevant principles through the skill catalog.

| Skill | When to use |
| --- | --- |
| [`principle-attack-the-premise`](./skills/jstack/principle-attack-the-premise) | After multiple fixes sharing an assumption fail the same gate. |
| [`principle-boundary-discipline`](./skills/jstack/principle-boundary-discipline) | When wiring validation, adapters or error handling. |
| [`principle-build-the-lever`](./skills/jstack/principle-build-the-lever) | When tooling would make nontrivial work repeatable or reviewable. |
| [`principle-encode-lessons-in-structure`](./skills/jstack/principle-encode-lessons-in-structure) | When a mechanical correction recurs. |
| [`principle-exhaust-the-design-space`](./skills/jstack/principle-exhaust-the-design-space) | When a consequential novel decision has multiple viable shapes. |
| [`principle-experience-first`](./skills/jstack/principle-experience-first) | When user experience and implementation convenience conflict. |
| [`principle-explain-the-number`](./skills/jstack/principle-explain-the-number) | Before reporting or acting on a measured performance or evaluation result. |
| [`principle-fix-root-causes`](./skills/jstack/principle-fix-root-causes) | When diagnosing a failure. |
| [`principle-foundational-thinking`](./skills/jstack/principle-foundational-thinking) | Before choosing structures or sequencing features. |
| [`principle-guard-the-context-window`](./skills/jstack/principle-guard-the-context-window) | When large evidence or a long run strains context. |
| [`principle-laziness-protocol`](./skills/jstack/principle-laziness-protocol) | When tempted to add layers or widen a refactor. |
| [`principle-make-operations-idempotent`](./skills/jstack/principle-make-operations-idempotent) | For commands or loops subject to retries and partial failure. |
| [`principle-migrate-callers-then-delete-legacy-apis`](./skills/jstack/principle-migrate-callers-then-delete-legacy-apis) | When replacing an internal API. |
| [`principle-minimize-reader-load`](./skills/jstack/principle-minimize-reader-load) | When code is hard to trace. |
| [`principle-model-the-domain`](./skills/jstack/principle-model-the-domain) | When state or domain rules spread across branches. |
| [`principle-never-block-on-the-human`](./skills/jstack/principle-never-block-on-the-human) | When a reversible scoped action is already authorized. |
| [`principle-outcome-oriented-execution`](./skills/jstack/principle-outcome-oriented-execution) | During an explicitly planned rewrite or migration. |
| [`principle-prove-it-works`](./skills/jstack/principle-prove-it-works) | Before declaring an outcome complete. |
| [`principle-redesign-from-first-principles`](./skills/jstack/principle-redesign-from-first-principles) | When a new requirement challenges the existing design. |
| [`principle-separate-before-serializing-shared-state`](./skills/jstack/principle-separate-before-serializing-shared-state) | When multiple actors might mutate the same object. |
| [`principle-sequence-verifiable-units`](./skills/jstack/principle-sequence-verifiable-units) | For multi-step edits or dependent delivery. |
| [`principle-subtract-before-you-add`](./skills/jstack/principle-subtract-before-you-add) | When sequencing a refactor or addition. |
| [`principle-test-behavior-not-implementation`](./skills/jstack/principle-test-behavior-not-implementation) | When adding or reviewing tests. |
| [`principle-type-system-discipline`](./skills/jstack/principle-type-system-discipline) | When designing types or handling untyped inputs. |

## Install

Run the Skills CLI yourself to discover the available skills and choose where to install them. Agents should provide installation and update commands without executing them:

```sh
npx skills add juancamiloqhz/skills
```

Install a specific skill directly:

```sh
npx skills add juancamiloqhz/skills --skill agent-instructions
```

For local authoring with Codex, clone this repository and symlink the skill directory into `~/.agents/skills`:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "/path/to/skills/skills/deep-understanding" "$HOME/.agents/skills/deep-understanding"
```

Codex discovers user-level skills from `~/.agents/skills`. Repository-specific skills should instead live in that repository's `.agents/skills` directory.

## Repository Structure

```text
skills/
  agent-instructions/
    SKILL.md
    agents/
      openai.yaml
    references/
      audit-rubric.md
      change-workflow.md
      harness-loading.md
    scripts/
      inventory_agent_instructions.py
      test_inventory_agent_instructions.py
  agent-workflow-readiness/
    SKILL.md
    agents/
      openai.yaml
    references/
      readiness-report.md
      repository-audit.md
      tracker-audit.md
  deep-understanding/
    SKILL.md
    agents/
      openai.yaml
  jstack/
    setup-jstack/
      SKILL.md
    juan-mode/
      SKILL.md
    how/
      SKILL.md
    why/
      SKILL.md
    arena/
    architect/
    interrogate/
    swarm/
      SKILL.md
    reflect/
      SKILL.md
    figure-it-out/
      SKILL.md
    create-verification-skill/
      SKILL.md
    maintain-verification-skill/
      SKILL.md
```

Skills may also contain `references/`, `scripts/`, or `assets/` when those resources directly support the workflow. Empty scaffolding is intentionally avoided.

## Design Principles

- Build skills from workflows proven in real projects.
- Keep each skill focused on one job with clear activation boundaries.
- Prefer concise instructions over speculative rules or unnecessary scripts.
- Keep repository-specific knowledge in the repository that owns it.
- Preserve approval boundaries for external or destructive actions.
- Validate skills before publishing releases.

## Attribution

`agent-instructions` is an independently written synthesis inspired by Matt Pocock's [AGENTS.md guide](https://www.aihero.dev/a-complete-guide-to-agents-md) and [`writing-for-agents`](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents), with harness semantics grounded in the official [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Claude Code](https://code.claude.com/docs/en/memory) documentation. The [research landscape](./research/agents-md-audit-skill-landscape.md) records comparable skills, differentiators, evidence, and licensing cautions.

`agent-workflow-readiness` is an independent readiness audit designed for compatibility with [Matt Pocock's engineering skills](https://github.com/mattpocock/skills) and their setup workflow. It is not an official Matt Pocock skill.

`deep-understanding` was inspired by Suzanne's original “Learn Quiz” teaching concept, shared publicly by [Thariq Shambaugh](https://x.com/trq212/status/2061545633560010826). It generalizes the teaching loop into a reusable skill for understanding codebases, systems, decisions, documents, research, workflows, and other complex topics.

## jstack

jstack is the bundle name. Its configuration skill, [`setup-jstack`](./skills/jstack/setup-jstack/SKILL.md), adapts pstack's model setup concept for T3 Code. [`juan-mode`](./skills/jstack/juan-mode/SKILL.md), corresponding to pstack's `poteto-mode`, now provides the execution foundation: activation instructions, the complete route registry, dependency discovery and model preflight. Its 23 playbook procedures remain planned. The [upstream reference](research/jstack/adaptations/juan-mode.md) records the inspected revision and MIT attribution. Source availability does not establish automatic rule loading or persistence after restart.

The standalone [`how`](./skills/jstack/how/SKILL.md) and [`why`](./skills/jstack/why/SKILL.md) skills explain runtime behavior and investigate historical rationale. Invoke either directly without activating juan-mode. Each requires an available, current setup-jstack installation for model resolution and the shared investigation contract; neither requires the other or juan-mode. Future playbooks will discover these skills through the provider's catalog. Install or update the dependencies manually, for example:

```sh
npx skills add juancamiloqhz/skills --skill setup-jstack --skill how --skill why
```

Model configuration can use global defaults or an optional `<project_root>/.jstack/models.json`. Lookup selects an explicit file first, then `JSTACK_CONFIG`, the project file, and finally `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`. Each selected file supplies all 17 roles. Setup offers global or project scope; the [configuration contract](./skills/jstack/setup-jstack/references/configuration.md) defines initialization, validation and worktree handoffs.

The bundle's source skills live under [`skills/jstack/`](./skills/jstack/). This directory groups independent skills and has no `SKILL.md` of its own. Keep each skill's existing name for installation and invocation. The Skills CLI supports this category layout; moving the source does not add a plugin namespace.

Install just the setup skill and select providers interactively:

```sh
npx skills add juancamiloqhz/skills --skill setup-jstack
```

## Jstack research

[Research and planning](./research/jstack/README.md) records the current status, agreed decisions, proposed roadmap, and source references. `setup-jstack` is released; `juan-mode` has a foundation implementation with [bounded evaluation evidence](./research/jstack/evaluations/juan-mode-foundation/README.md). The complete playbook release remains in development.

For pstack updates, use the [upstream maintenance procedure](./research/jstack/upstream-maintenance.md). Its checker detects changes and preserves evidence; a review decides which changes belong in jstack. The [roadmap](./research/jstack/roadmap.md) records the enabled weekly review and verified delivery.

## Maturity

The repository is currently experimental. Skill behavior and packaging may evolve as the skills are tested across different projects.

## License

Released under the [MIT License](./LICENSE).
