# Jstack decisions

Recorded on 2026-10-10 from the existing project discussion and shipped setup implementation. These decisions do not settle the deferred workflow research.

## Names and scope

The bundle is named `jstack`. Its first skill is `setup-jstack`. The planned workflow entrypoint is `juan-mode`, corresponding to pstack's `poteto-mode` concept. Jstack will select useful ideas from pstack; no commitment has been made to implement all upstream skills.

## Delivery

Develop in small, focused pull requests. Merge a completed skill before installation from `juancamiloqhz/skills` with the Skills CLI. The user performs all skill installations and updates manually; agents provide commands but do not run them. The selected installation providers are Codex, Claude Code, Cursor, and OpenCode. This selection is not a claim that every future workflow has been tested on all four providers.

Portable skills are the current distribution format. A broader plugin or generated adapter system has not been committed to.

## Shipped configuration

`setup-jstack` uses T3's live capability catalog and saves validated model assignments outside the repository. The [configuration contract](../../skills/setup-jstack/references/configuration.md) defines the schema, 17 roles, inheritance, reasoning budgets, and consumer requirements.

Retain pstack's reasoning-budget labels with their target effort shown: unlimited/max, large/xhigh, medium/high, small/medium. This gives setup a bulk effort choice without implying a spending cap. Keep schema version 1 and the `preset` field; effective per-seat options remain authoritative at resolution time. See the [upstream rationale](../../skills/setup-jstack/references/upstream.md).

Setup configures routing only. A configured role does not enable a workflow or grant execution permissions. Future consumers must load and revalidate the configuration when invoked.

## Research organization

Keep active research in `research/jstack/`. Record sources and dates, distinguish observed behavior from proposals, and investigate each workflow when it becomes the next authorized task. Preserve attribution when adapting source material.

The old review prototype and raw evaluations are removed from the proposed merge. Their earlier commit remains available for retrieval. Do not carry forward the old implementation plan as an approved architecture.

Use one source line per prose paragraph, with separate paragraph, list, and code-block boundaries.
