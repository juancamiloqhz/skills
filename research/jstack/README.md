# Jstack research

Jstack is a skills bundle being developed for T3 Code, informed by pstack. This directory holds the current decisions, roadmap, and source references. It does not prescribe a full pstack port.

## Current status

As of 2026-10-11, [`setup-jstack`](../../skills/jstack/setup-jstack/SKILL.md) provides model configuration and validation, and [`create-verification-skill`](../../skills/jstack/create-verification-skill/SKILL.md) is released with a CLI evaluation. Setup's optional verification offer and [`maintain-verification-skill`](../../skills/jstack/maintain-verification-skill/SKILL.md) are released; maintenance has a separate [evaluation](evaluations/maintain-verification-skill/README.md). Upstream maintenance is released and its weekly review delivers to the skills project conversation.

The next work is specifying `juan-mode` as an adaptation of poteto-mode's working approach and task router. The [roadmap](roadmap.md) records the first-release playbooks, implementation sequence and release checks. The skill is not implemented.

## Read by purpose

- [Decisions](decisions.md): agreed names, delivery approach, and existing configuration boundaries.
- [Roadmap](roadmap.md): completed work and proposed next steps, with completion checks.
- [Sources](sources.md): pinned references and attribution carried forward from existing work.
- [Juan-mode adaptation](juan-mode-adaptation.md): source assessment, T3 Code integration constraints and design proposals.
- [Upstream maintenance](upstream-maintenance.md): run a pstack change check, review its impact, or implement an approved recommendation. The [first review](upstream-reviews/2026-10-11.md) records the live trial; the roadmap records the completed scheduling handoff.

## Open questions

The adaptation specification must settle activation behavior, helper-skill packaging, shared configuration access, publication defaults and provider coverage. The roadmap distinguishes the agreed first-release scope from later workflow candidates.

## Earlier experiment

The old pstack review prototype, evaluation receipts, and broad portability audit are excluded from the current tree. They remain recoverable in [the earlier PR #4 commit](https://github.com/juancamiloqhz/skills/commit/28be989). They are historical material, not the active jstack plan or evidence that a jstack workflow works.
