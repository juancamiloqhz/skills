# Jstack sources

Setup and historical references were carried forward on 2026-10-10. Later entries record the inspection dates for verification tooling. A pinned source identifies what was previously inspected; it does not establish compatibility with a current runtime.

For newer upstream changes, use the [maintenance procedure](upstream-maintenance.md) and [manifest](upstream.json). Review checkpoints do not replace the historical adaptation pins below.

## Shipped setup

The setup adaptation uses `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`.

- [setup-pstack](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/setup-pstack/SKILL.md): source for the setup concept and role registry.
- [poteto-mode](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/poteto-mode/SKILL.md): previously inspected consumer context, not an implemented jstack workflow.
- [Local attribution](adaptations/setup-jstack.md) and [retained MIT notice](../../skills/jstack/jstack-setup/LICENSE): adaptation scope and Lauren Tan's upstream copyright notice.

## Local implementation references

- [Setup skill](../../skills/jstack/jstack-setup/SKILL.md): setup behavior and limits.
- [Configuration contract](../../skills/jstack/jstack-setup/references/configuration.md): schema and consumer requirements.
- [T3 Code integration reference](../../skills/jstack/jstack-setup/references/t3-code.md): integration guidance shipped with setup. Recheck callable tools and injected runtime instructions before execution.

## Historical material

[Commit 28be989](https://github.com/juancamiloqhz/skills/commit/28be989) preserves the previous experiment and audit if a future question warrants consulting them. The Arena prototype used `e5a8186d7b43be8d6ac4452440fbead5f1a51c70`; the broader dependency audit used `df581122cde17e6e27686b5a448bde23e4ad4318`. These are separate baselines from the shipped setup.

The panel experiments tested selected delegation mechanics. They did not validate `juan-mode`, and the post-evaluation rubric correction was not behaviorally rerun. Historical capability snapshots must not serve as current model allowlists.

## Verification generator

The generator adaptation uses the same `ccb5507cec1546dc88135c1139c811e6c59115ba` pin. Its [upstream reference](adaptations/create-verification-skill.md) identifies the generator and feature-map sources, retained license, and changes for T3 Code. Its [evaluation](evaluations/create-verification-skill/README.md) records what was actually executed. The optional offer is implemented in `setup-jstack`.

## Verification maintenance

The maintenance adaptation uses `ccb5507cec1546dc88135c1139c811e6c59115ba`, inspected on 2026-10-11. Its [upstream reference](adaptations/maintain-verification-skill.md) records source and differences, including optional publication, executing-agent source review, and blocked coverage for unmet prerequisites. Its [evaluation](evaluations/maintain-verification-skill/README.md) records the tested cases and limits.
