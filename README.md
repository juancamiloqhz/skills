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
| [`jstack-setup`](./skills/jstack/jstack-setup) | Configures jstack workflow roles using T3 Code's live provider/model catalog, reasoning budgets, global defaults and optional project settings. | Experimental; configuration helper tested |
| [`jstack-juan-mode`](./skills/jstack/jstack-juan-mode) | Provides persistent-mode instructions, inline task routing and configured delegation preflight. | Investigation and Prototype available; 21 playbooks pending; see [Prototype evaluation](./research/jstack/evaluations/prototype-playbook/README.md) |
| [`jstack-how`](./skills/jstack/jstack-how) | Explains runtime flow, component ownership and failure behavior using configured investigation roles. | Experimental; see [evaluation](./research/jstack/evaluations/shared-investigation/README.md) |
| [`jstack-why`](./skills/jstack/jstack-why) | Investigates historical rationale, contradictions and unknowns using relevant evidence sources. | Experimental; see [evaluation](./research/jstack/evaluations/shared-investigation/README.md) |
| [`jstack-arena`](./skills/jstack/jstack-arena) | Compares configured candidates, selects one cross-judge and synthesizes a verified artifact. | Experimental; see [evaluation](./research/jstack/evaluations/arena/README.md) |
| [`jstack-architect`](./skills/jstack/jstack-architect) | Grounds competing design sketches and returns a design or continues with authorized implementation. | Experimental; see [evaluation](./research/jstack/evaluations/architect/README.md) |
| [`jstack-interrogate`](./skills/jstack/jstack-interrogate) | Challenges code or designs with configured reviewers and a checked, report-only verdict. | Experimental; see [evaluation](./research/jstack/evaluations/interrogate/README.md) |
| [`jstack-swarm`](./skills/jstack/jstack-swarm) | Coordinates configured workers for coverage or races and verifies one consolidated result. | Experimental; see [evaluation](./research/jstack/evaluations/swarm/README.md) |
| [`jstack-reflect`](./skills/jstack/jstack-reflect) | Reviews bounded session evidence through three lenses and proposes verified guidance changes or structural fixes. | Experimental; see [evaluation](./research/jstack/evaluations/reflect/README.md) |
| [`jstack-figure-it-out`](./skills/jstack/jstack-figure-it-out) | Designs a custom workflow with measured units, scoped execution and a reviewed decision trail. | Experimental; see [evaluation](./research/jstack/evaluations/trail-restoration/README.md) |
| [`jstack-show-me-your-work`](./skills/jstack/jstack-show-me-your-work) | Keeps an append-only decision log and reviews this run's evidence before handoff. | Experimental; see [evaluation](./research/jstack/evaluations/trail-restoration/README.md) |
| [`jstack-typescript-best-practices`](./skills/jstack/jstack-typescript-best-practices) | Applies TypeScript modeling, boundary validation and narrowing patterns through Type System Discipline. | Experimental; see [evaluation](./research/jstack/evaluations/typescript-best-practices/README.md) |
| [`jstack-no-comments`](./skills/jstack/jstack-no-comments) | Runs Comment Sicko, checks comment deletions and code flags, and fixes accepted issues within the requested scope. | Experimental; see [evaluation](./research/jstack/evaluations/no-comments/README.md) |
| [`jstack-technical-writing`](./skills/jstack/jstack-technical-writing) | Applies four writing layers to docs, RFCs, readmes, PR descriptions and commit messages, with an external Unslop dependency. | Experimental; see [evaluation](./research/jstack/evaluations/technical-writing/README.md) |
| [`jstack-benchmark-checklist`](./skills/jstack/jstack-benchmark-checklist) | Checks performance measurements for real work, errors, fair tuning, repeatability and a measured limiter. | Experimental; see [evaluation](./research/jstack/evaluations/benchmark-checklist/README.md) |
| [`jstack-create-verification-skill`](./skills/jstack/jstack-create-verification-skill) | Generates project-local verification instructions and exercises a real feature with evidence and cleanup. | Experimental; see [evaluation](./research/jstack/evaluations/verification-restoration/README.md) |
| [`jstack-maintain-verification-skill`](./skills/jstack/jstack-maintain-verification-skill) | Audits existing verification instructions against source and live behavior, repairs drift, and reports product regressions. | Experimental; see [evaluation](./research/jstack/evaluations/verification-restoration/README.md) |

## Engineering principles

These 24 jstack skills are independently installable and discoverable. Juan-mode and Figure-it-out load relevant principles through the skill catalog.

| Skill | When to use |
| --- | --- |
| [`jstack-principle-attack-the-premise`](./skills/jstack/jstack-principle-attack-the-premise) | After multiple fixes sharing an assumption fail the same gate. |
| [`jstack-principle-boundary-discipline`](./skills/jstack/jstack-principle-boundary-discipline) | When wiring validation, adapters or error handling. |
| [`jstack-principle-build-the-lever`](./skills/jstack/jstack-principle-build-the-lever) | When tooling would make nontrivial work repeatable or reviewable. |
| [`jstack-principle-encode-lessons-in-structure`](./skills/jstack/jstack-principle-encode-lessons-in-structure) | When a mechanical correction recurs. |
| [`jstack-principle-exhaust-the-design-space`](./skills/jstack/jstack-principle-exhaust-the-design-space) | When a consequential novel decision has multiple viable shapes. |
| [`jstack-principle-experience-first`](./skills/jstack/jstack-principle-experience-first) | When user experience and implementation convenience conflict. |
| [`jstack-principle-explain-the-number`](./skills/jstack/jstack-principle-explain-the-number) | Before reporting or acting on a measured performance or evaluation result. |
| [`jstack-principle-fix-root-causes`](./skills/jstack/jstack-principle-fix-root-causes) | When diagnosing a failure. |
| [`jstack-principle-foundational-thinking`](./skills/jstack/jstack-principle-foundational-thinking) | Before choosing structures or sequencing features. |
| [`jstack-principle-guard-the-context-window`](./skills/jstack/jstack-principle-guard-the-context-window) | When large evidence or a long run strains context. |
| [`jstack-principle-laziness-protocol`](./skills/jstack/jstack-principle-laziness-protocol) | When tempted to add layers or widen a refactor. |
| [`jstack-principle-make-operations-idempotent`](./skills/jstack/jstack-principle-make-operations-idempotent) | For commands or loops subject to retries and partial failure. |
| [`jstack-principle-migrate-callers-then-delete-legacy-apis`](./skills/jstack/jstack-principle-migrate-callers-then-delete-legacy-apis) | When replacing an internal API. |
| [`jstack-principle-minimize-reader-load`](./skills/jstack/jstack-principle-minimize-reader-load) | When code is hard to trace. |
| [`jstack-principle-model-the-domain`](./skills/jstack/jstack-principle-model-the-domain) | When state or domain rules spread across branches. |
| [`jstack-principle-never-block-on-the-human`](./skills/jstack/jstack-principle-never-block-on-the-human) | When a reversible scoped action is already authorized. |
| [`jstack-principle-outcome-oriented-execution`](./skills/jstack/jstack-principle-outcome-oriented-execution) | During an explicitly planned rewrite or migration. |
| [`jstack-principle-prove-it-works`](./skills/jstack/jstack-principle-prove-it-works) | Before declaring an outcome complete. |
| [`jstack-principle-redesign-from-first-principles`](./skills/jstack/jstack-principle-redesign-from-first-principles) | When a new requirement challenges the existing design. |
| [`jstack-principle-separate-before-serializing-shared-state`](./skills/jstack/jstack-principle-separate-before-serializing-shared-state) | When multiple actors might mutate the same object. |
| [`jstack-principle-sequence-verifiable-units`](./skills/jstack/jstack-principle-sequence-verifiable-units) | For multi-step edits or dependent delivery. |
| [`jstack-principle-subtract-before-you-add`](./skills/jstack/jstack-principle-subtract-before-you-add) | When sequencing a refactor or addition. |
| [`jstack-principle-test-behavior-not-implementation`](./skills/jstack/jstack-principle-test-behavior-not-implementation) | When adding or reviewing tests. |
| [`jstack-principle-type-system-discipline`](./skills/jstack/jstack-principle-type-system-discipline) | When designing types or handling untyped inputs. |

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
    jstack-setup/
      SKILL.md
    jstack-juan-mode/
      SKILL.md
    jstack-how/
      SKILL.md
    jstack-why/
      SKILL.md
    jstack-arena/
    jstack-architect/
    jstack-interrogate/
    jstack-swarm/
      SKILL.md
    jstack-reflect/
      SKILL.md
    jstack-figure-it-out/
      SKILL.md
    jstack-show-me-your-work/
      SKILL.md
    jstack-typescript-best-practices/
      SKILL.md
    jstack-no-comments/
      SKILL.md
    jstack-technical-writing/
      SKILL.md
    jstack-create-verification-skill/
      SKILL.md
    jstack-maintain-verification-skill/
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

jstack is the bundle name. Its configuration skill, [`jstack-setup`](./skills/jstack/jstack-setup/SKILL.md), adapts pstack's model setup concept for T3 Code. [`jstack-juan-mode`](./skills/jstack/jstack-juan-mode/SKILL.md), corresponding to pstack's `poteto-mode`, now provides the execution foundation: activation instructions, the inline playbook list, mandatory helper triggers, dependency discovery and model preflight. Its 23 playbook procedures remain planned. The [upstream reference](research/jstack/adaptations/juan-mode.md) records the inspected revision and MIT attribution. Source availability does not establish automatic rule loading or persistence after restart.

The standalone [`jstack-how`](./skills/jstack/jstack-how/SKILL.md) and [`jstack-why`](./skills/jstack/jstack-why/SKILL.md) skills explain runtime behavior and investigate historical rationale. Invoke either directly without activating jstack-juan-mode. Each requires an available, current jstack-setup installation for model resolution and the shared investigation contract; neither requires the other or jstack-juan-mode. Future playbooks will discover these skills through the provider's catalog. Install or update the dependencies manually, for example:

```sh
npx skills add juancamiloqhz/skills --skill jstack-setup --skill jstack-how --skill jstack-why
```

Model configuration can use global defaults or an optional `<project_root>/.jstack/models.json`. Lookup selects an explicit file first, then `JSTACK_CONFIG`, the project file, and finally `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`. Each selected file supplies all 17 roles. Setup offers global or project scope; the [configuration contract](./skills/jstack/jstack-setup/references/configuration.md) defines initialization, validation and worktree handoffs.

The bundle's source skills live under [`skills/jstack/`](./skills/jstack/). This directory groups independent skills and has no `SKILL.md` of its own. All shipped jstack skills use portable `jstack-` names for installation and invocation, including `jstack-setup`, `jstack-juan-mode` and `jstack-principle-*`. The directory itself adds no namespace. See the [manual migration guide](research/jstack/skill-names.md) when updating an older installation.

Install just the setup skill and select providers interactively:

```sh
npx skills add juancamiloqhz/skills --skill jstack-setup
```

## Jstack research

[Research and planning](./research/jstack/README.md) records the current status, agreed decisions, proposed roadmap, and source references. `jstack-setup` is released; `jstack-juan-mode` has a foundation implementation with [bounded evaluation evidence](./research/jstack/evaluations/mode-restoration/README.md). The complete playbook release remains in development.

For pstack updates, use the [upstream maintenance procedure](./research/jstack/upstream-maintenance.md). Its checker detects changes and preserves evidence; a review decides which changes belong in jstack. The [roadmap](./research/jstack/roadmap.md) records the enabled weekly review and verified delivery.

## Maturity

The repository is currently experimental. Skill behavior and packaging may evolve as the skills are tested across different projects.

## License

Released under the [MIT License](./LICENSE).
