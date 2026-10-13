# Upstream and intentional differences

Relocated from the skill package on 2026-10-13. This record describes the existing adaptation; it does not approve every difference. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) classifies remaining corrections.

Adapted from [poteto-mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md) and its [playbook directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`, inspected on 2026-10-11. The bundled [MIT license](../../../skills/jstack/juan-mode/LICENSE) retains Lauren Tan's attribution.

This foundation implements the entrypoint, complete route registry, dependency discovery, model preflight and execution instructions. The separate how/why skills begin the shared-helper group. The 24 principle leaves are packaged as standalone skills. The 23 playbook procedures and remaining helpers remain planned. A registry entry does not imply that its procedure was ported or evaluated.

T3 Code uses the user's saved jstack roles and live provider catalog instead of upstream model defaults and Cursor wrappers. The preflight calls the separately discovered setup-jstack resolver without copying it. That resolver selects a complete global or project configuration, with explicit selections taking precedence. Children receive the selected absolute path so their checkout cannot change routing. Inherited selections preserve the parent. Child briefs contain explicit context, fresh review rounds retain distinct task IDs, and the parent owns PR watches.

Activation until opt-out is a conversation instruction. Cursor mode frontmatter is not used as a portability or persistence mechanism. Resume and compaction remain separate evaluation requirements. T3 Code path-directed children do not acquire an app workspace binding from their prompt.

Publication, merging, installation and recurring work follow the user's authorized scope. Opening a PR is not an automatic ending for every task. Scoped evidence-based review replaces deletion-first comment rules; helper names do not require unrelated global skill installations.

## Shared investigation skills

Pstack packages how and why as separate skills. Jstack preserves that boundary through catalog-discovered `how` and `why` dependencies. Their own upstream records retain the algorithm adaptations and attribution. They share model resolution and investigation evidence guidance through setup-jstack, without depending on a juan-mode installation. The 23 playbooks remain internal to juan-mode and pending implementation.

## Engineering principles

The [Principles section](../../../skills/jstack/juan-mode/SKILL.md#principles) routes to 24 standalone `principle-*` skills, each with its own entrypoint and MIT license; provenance and adaptation records are maintained in research. This replaces the initial internal-reference packaging by user decision. Juan-mode and Figure-it-out discover relevant skills through the catalog; the principle bodies have one authoritative home and no caller assumes sibling installation.

The scoped adaptations retain compatibility obligations, authorization, evidence limits and useful containment. They avoid unconditional internal trust, syntax-only test deletion, blind external retries and automatic cleanup. Normal discovery permits direct invocation and workflow callers; no principle requires juan-mode activation, setup-jstack or delegation. Missing selected principles produce manual installation guidance and an explicit limitation.

The entrypoint preserves upstream's inline Principles section, its Core, Architecture, Verification, Delegation and Meta groups, and the pinned trigger summaries. Jstack adds catalog discovery and missing-dependency handling around that structure. The temporary separate index was removed to reduce structural drift.
