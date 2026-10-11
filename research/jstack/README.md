# Jstack research

Jstack is a skills bundle being developed for T3 Code, informed by pstack. This directory holds the current decisions, roadmap, and source references. It does not prescribe a full pstack port.

## Current status

As of 2026-10-11, [`setup-jstack`](../../skills/jstack/setup-jstack/SKILL.md) provides model configuration and validation, and [`create-verification-skill`](../../skills/jstack/create-verification-skill/SKILL.md) is released with a CLI evaluation. Setup's optional verification offer is released. [`maintain-verification-skill`](../../skills/jstack/maintain-verification-skill/SKILL.md) is the current change, with a separate [evaluation](evaluations/maintain-verification-skill/README.md). `juan-mode` is the agreed name for the future workflow entrypoint; it is not implemented.

The roadmap separates verification-tooling work from the proposed `juan-mode` investigation workflow. Research into that first investigation workflow remains deferred until requested.

## Read by purpose

- [Decisions](decisions.md): agreed names, delivery approach, and existing configuration boundaries.
- [Roadmap](roadmap.md): completed work and proposed next steps, with completion checks.
- [Sources](sources.md): pinned references and attribution carried forward from existing work.

## Open questions

The first proposed workflow is a read-only codebase investigation. Its exact scope, prompts, delegation behavior, and evaluation criteria remain to be researched. Packaging beyond the existing portable skills and support for later workflows remain undecided.

## Earlier experiment

The old pstack review prototype, evaluation receipts, and broad portability audit are excluded from the current tree. They remain recoverable in [the earlier PR #4 commit](https://github.com/juancamiloqhz/skills/commit/28be989). They are historical material, not the active jstack plan or evidence that a jstack workflow works.
