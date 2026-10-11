# Jstack sources

References carried forward on 2026-10-10 from existing work. No new upstream research was performed for this reorganization. A pinned source identifies what was previously inspected; it does not establish compatibility with a current runtime.

## Shipped setup

The setup adaptation uses `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`.

- [setup-pstack](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/setup-pstack/SKILL.md): source for the setup concept and role registry.
- [poteto-mode](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/poteto-mode/SKILL.md): previously inspected consumer context, not an implemented jstack workflow.
- [Local attribution](../../skills/setup-jstack/references/upstream.md) and [retained MIT notice](../../skills/setup-jstack/LICENSE): adaptation scope and Lauren Tan's upstream copyright notice.

## Local implementation references

- [Setup skill](../../skills/setup-jstack/SKILL.md): setup behavior and limits.
- [Configuration contract](../../skills/setup-jstack/references/configuration.md): schema and consumer requirements.
- [T3 integration reference](../../skills/setup-jstack/references/t3.md): integration guidance shipped with setup. Recheck callable tools and injected runtime instructions before execution.

## Historical material

[Commit 28be989](https://github.com/juancamiloqhz/skills/commit/28be989) preserves the previous experiment and audit if a future question warrants consulting them. The Arena prototype used `e5a8186d7b43be8d6ac4452440fbead5f1a51c70`; the broader dependency audit used `df581122cde17e6e27686b5a448bde23e4ad4318`. These are separate baselines from the shipped setup.

The panel experiments tested selected delegation mechanics. They did not validate `juan-mode`, and the post-evaluation rubric correction was not behaviorally rerun. Historical capability snapshots must not serve as current model allowlists.

## Verification generator

The generator adaptation uses the same `ccb5507cec1546dc88135c1139c811e6c59115ba` pin. Its [upstream reference](../../skills/create-verification-skill/references/upstream.md) identifies the generator and feature-map sources, retained license, and T3-specific changes. Its [evaluation](evaluations/create-verification-skill/README.md) records what was actually executed. The optional offer is implemented in `setup-jstack`; the upstream maintenance skill remains future work.
