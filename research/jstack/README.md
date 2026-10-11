# Jstack research

Jstack is a skills bundle being developed for T3 Code, informed by pstack. This directory holds the current decisions, roadmap, and source references. It does not prescribe a full pstack port.

## Current status

As of 2026-10-11, [`setup-jstack`](../../skills/jstack/setup-jstack/SKILL.md) provides model configuration and validation, and [`create-verification-skill`](../../skills/jstack/create-verification-skill/SKILL.md) is released with a CLI evaluation. Setup's optional verification offer and [`maintain-verification-skill`](../../skills/jstack/maintain-verification-skill/SKILL.md) are released; maintenance has a separate [evaluation](evaluations/maintain-verification-skill/README.md). Upstream maintenance is released and its weekly review delivers to the skills project conversation.

All 23 poteto-mode playbooks have been assessed for `juan-mode`, the working-style entrypoint and task router. The [specification](juan-mode-spec.md) defines the complete target, shared dependencies and acceptance scenarios. The [foundation implementation](../../skills/jstack/juan-mode/SKILL.md) provides activation instructions, the route registry and configuration preflight, with [bounded evaluation evidence](evaluations/juan-mode-foundation/README.md). The playbook procedures remain planned; the [roadmap](roadmap.md) records the remaining execution proof and implementation groups.

## Read by purpose

- [Decisions](decisions.md): agreed names, delivery approach, and existing configuration boundaries.
- [Roadmap](roadmap.md): completed work and proposed next steps, with completion checks.
- [Sources](sources.md): pinned references and attribution carried forward from existing work.
- [Juan-mode adaptation](juan-mode-adaptation.md): source assessment, T3 Code integration constraints and design proposals.
- [Juan-mode specification](juan-mode-spec.md): accepted scope and activation behavior, complete playbook inventories, proposed packaging, execution contracts and release checks.
- [Upstream maintenance](upstream-maintenance.md): run a pstack change check, review its impact, or implement an approved recommendation. The [first review](upstream-reviews/2026-10-11.md) records the live trial; the roadmap records the completed scheduling handoff.

## Open questions

Conversation activation until explicit opt-out is the accepted behavior. Implementation must prove it across compaction and resume, verify delegated workspace isolation and merge continuation, and establish which runtime evidence supports workflow evaluation. The specification distinguishes proposed implementation choices from measured support.

## Earlier experiment

The old pstack review prototype, evaluation receipts, and broad portability audit are excluded from the current tree. They remain recoverable in [the earlier PR #4 commit](https://github.com/juancamiloqhz/skills/commit/28be989). They are historical material, not the active jstack plan or evidence that a jstack workflow works.
