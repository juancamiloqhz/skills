# Jstack decisions

Initially recorded on 2026-10-10 from the project discussion and shipped setup implementation. Updated on 2026-10-11 with the complete juan-mode playbook target and activation preference. The specification records design choices that still require implementation evidence.

## Names and scope

The bundle is named `jstack`. Its first skill is `setup-jstack`. The planned workflow entrypoint is `juan-mode`, corresponding to pstack's `poteto-mode` concept. Jstack will select useful ideas from pstack; no commitment has been made to implement all upstream skills.

On 2026-10-11, the user confirmed the direction of adapting poteto-mode's broader working approach, including task routing, delegation, review and verification. After discussing staged delivery, the user accepted assessing and designing for all 23 upstream playbooks, then implementing and verifying them in manageable groups. This supersedes the earlier three-playbook first-release plan. The [roadmap](roadmap.md) owns the scope and sequence; the [specification](juan-mode-spec.md) records the complete adaptation design.

Explicit invocation activates juan-mode for later tasks in the same conversation until the user turns it off. Task completion does not deactivate it. This is the intended behavior; provider persistence across compaction and resume must be demonstrated before claiming support. Activation does not itself authorize new external actions, merging or installation.

## Delivery

Develop in small, focused pull requests. Merge a completed skill before installation from `juancamiloqhz/skills` with the Skills CLI. The user performs all skill installations and updates manually; agents provide commands but do not run them. The selected installation providers are Codex, Claude Code, Cursor, and OpenCode. This selection is not a claim that every future workflow has been tested on all four providers.

Portable skills are the current distribution format. Their source directories are grouped under `skills/jstack/`, with each skill retaining its own `SKILL.md`, supporting files and existing name. The `jstack/` container has no `SKILL.md` and introduces no plugin namespace. A broader plugin or generated adapter system has not been committed to.

## Shipped configuration

`setup-jstack` uses T3 Code's live capability catalog and saves validated model assignments as global defaults or optional project settings. The [configuration contract](../../skills/jstack/setup-jstack/references/configuration.md) defines the schema, 17 roles, inheritance, reasoning budgets, and consumer requirements.

On 2026-10-11, the user approved optional `<project_root>/.jstack/models.json` configuration. Explicit file selection takes precedence over `JSTACK_CONFIG`, then the project file, then the existing XDG global path. Each file supplies the complete 17-role map; files are not merged. Setup offers global or project scope and seeds a new project draft from global settings when available. Consumers share setup's lookup and pass the selected absolute path to children. `inherit-parent` keeps its existing conversation-model meaning.

Retain pstack's reasoning-budget labels with their target effort shown: unlimited/max, large/xhigh, medium/high, small/medium. This gives setup a bulk effort choice without implying a spending cap. Keep schema version 1 and the `preset` field; effective per-seat options remain authoritative at resolution time. See the [upstream rationale](adaptations/setup-jstack.md).

Setup configures routing only. A configured role does not enable a workflow or grant execution permissions. Future consumers must load and revalidate the configuration when invoked.

## Research organization

Keep active research in `research/jstack/`. Record sources and dates, distinguish observed behavior from proposals, and investigate each workflow when it becomes the next authorized task. Preserve attribution when adapting source material.

The old review prototype and raw evaluations are removed from the proposed merge. Their earlier commit remains available for retrieval. Do not carry forward the old implementation plan as an approved architecture.

Use one source line per prose paragraph, with separate paragraph, list, and code-block boundaries.

## Standalone investigation skills, 2026-10-12

Package how and why as separate skills, as pstack does, with direct invocation and catalog-discovered use by juan-mode playbooks. This supersedes the initial plan to bundle these two procedures as references inside juan-mode. Their configured roles and investigation algorithms remain. Setup-jstack owns their shared configuration and evidence contract; they do not require a juan-mode installation or activate its persistent mode. Other planned helpers retain their existing packaging until assessed. Installation and updates remain manual.

## Automatic Claude linking, 2026-10-14

The user explicitly reaffirmed PR #9's automatic project-local linking: "Keep automatic Claude linking (preserve existing behavior)". Every generated verification skill gets a relative `.claude/skills/verify-<app>` link to its canonical directory, regardless of the executing provider. This is an intentional jstack addition to pstack. Preserve conflicting paths, keep canonical files inside the authorized repository and verify the link resolves the complete package. This decision does not authorize global installation or establish live provider discovery. Future fidelity reviews should preserve this choice unless the user changes it. See the [generator adaptation record](adaptations/create-verification-skill.md).
