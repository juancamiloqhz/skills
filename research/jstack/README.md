# Jstack research

Jstack is a skills bundle being developed for T3 Code, informed by pstack. This directory holds the current decisions, roadmap, and source references. It does not prescribe a full pstack port.

## Current status

As of 2026-10-11, [`setup-jstack`](../../skills/jstack/setup-jstack/SKILL.md) provides model configuration and validation, and [`create-verification-skill`](../../skills/jstack/create-verification-skill/SKILL.md) is released with a CLI evaluation. Setup's optional verification offer and [`maintain-verification-skill`](../../skills/jstack/maintain-verification-skill/SKILL.md) are released; maintenance has a separate [evaluation](evaluations/maintain-verification-skill/README.md). Upstream maintenance is released and its weekly review delivers to the skills project conversation.

All 23 poteto-mode playbooks have been assessed for `juan-mode`, the working-style entrypoint and task router. The [specification](juan-mode-spec.md) defines the complete target, shared dependencies and acceptance scenarios. The [foundation implementation](../../skills/jstack/juan-mode/SKILL.md) provides activation instructions, the route registry and configuration preflight, with [bounded evaluation evidence](evaluations/juan-mode-foundation/README.md). The playbook procedures remain planned; the [roadmap](roadmap.md) records the remaining execution proof and implementation groups.

Setup and juan-mode also share optional project model configuration, with [evaluation evidence](evaluations/project-model-config/README.md). A project file replaces the complete global map for that project, while explicit selections remain highest priority.

The [installed runtime evaluation](evaluations/juan-mode-runtime/README.md) adds inherited Codex dispatch, explicit-path editor isolation and synthetic activation recovery cases. Actual compaction, provider restart and other coordinating providers remain unverified.

The shared-procedure group now includes standalone how/why investigation skills and a shared setup-jstack evidence contract, with [fixture evaluation](evaluations/shared-investigation/README.md). Users can invoke them directly, and juan-mode discovers them through the skill catalog; the 23 playbooks and remaining helper/principle work stay planned.

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

Standalone [Arena](../../skills/jstack/arena/SKILL.md) adds configured candidate comparison, one selected cross-judge and verified synthesis. Its [evaluation](evaluations/arena/README.md) covers a design-only result and insufficient panel/required-diversity failures. Standalone [Architect](../../skills/jstack/architect/SKILL.md) adds grounded design with the architect runner panel and a caller-controlled implementation boundary. Its [evaluation](evaluations/architect/README.md) records the recovered design comparison and initial dispatch failures. The playbook callers remain planned.

Standalone [Interrogate](../../skills/jstack/interrogate/SKILL.md) provides configured code and design review with checked lead judgment and no automatic fixes. Its [evaluation](evaluations/interrogate/README.md) covers seeded defects, a valid design and an unmet model-diversity requirement.

Standalone [Swarm](../../skills/jstack/swarm/SKILL.md) coordinates partitioned coverage and declared races with configured workers. Its [evaluation](evaluations/swarm/README.md) records completed source/history slices, a ranked design tie and scope-discovery limitations.

Standalone [Reflect](../../skills/jstack/reflect/SKILL.md) reviews bounded conversation evidence through judgment, tooling and divergent lenses, then checks recommendations against existing guidance. Its [evaluation](evaluations/reflect/README.md) records three review lenses, separate synthesis, rejected duplicate guidance and preserved assessment boundaries.

Standalone [Figure it out](../../skills/jstack/figure-it-out/SKILL.md) designs custom workflows, returns at planning-only boundaries and verifies authorized execution with a reviewed decision trail. Its [evaluation](evaluations/figure-it-out/README.md) records planning-only return, real CLI checks and a corrected audit-reporting failure.

The [engineering principle index](../../skills/jstack/juan-mode/references/principles/index.md) routes to all 24 standalone principle skills through catalog discovery. The [evaluation](evaluations/principles/README.md) records eight tabletop scenarios and a full source audit; the playbook procedures remain planned.
