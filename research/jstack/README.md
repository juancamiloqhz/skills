# Jstack research

Jstack is a skills bundle being developed for T3 Code, informed by pstack. This directory holds the current decisions, roadmap, and source references. It does not prescribe a full pstack port.

## Current status

As of 2026-10-10, [`setup-jstack`](../../skills/setup-jstack/SKILL.md) is released and provides model configuration and validation. `juan-mode` is the agreed name for the future workflow entrypoint; it is not implemented.

This reorganization records existing work and decisions only. Research into the first workflow has not started in this directory and is explicitly deferred until requested.

## Read by purpose

- [Decisions](decisions.md): agreed names, delivery approach, and existing configuration boundaries.
- [Roadmap](roadmap.md): completed work and proposed next steps, with completion checks.
- [Sources](sources.md): pinned references and attribution carried forward from existing work.

## Open questions

The first proposed workflow is a read-only codebase investigation. Its exact scope, prompts, delegation behavior, and evaluation criteria remain to be researched. Packaging beyond the existing portable skills and support for later workflows remain undecided.

## Earlier experiment

The old pstack review prototype, evaluation receipts, and broad portability audit are excluded from the current tree. They remain recoverable in [the earlier PR #4 commit](https://github.com/juancamiloqhz/skills/commit/28be989). They are historical material, not the active jstack plan or evidence that a jstack workflow works.
