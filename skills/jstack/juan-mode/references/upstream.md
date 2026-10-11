# Upstream and intentional differences

Adapted from [poteto-mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md) and its [playbook directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`, inspected on 2026-10-11. The bundled [MIT license](../LICENSE) retains Lauren Tan's attribution.

This foundation implements the entrypoint, complete route registry, dependency discovery, model preflight and execution instructions. The 23 playbook procedures and shared helper/principle adaptations remain planned. A registry entry does not imply that its procedure was ported or evaluated.

T3 Code uses the user's saved jstack roles and live provider catalog instead of upstream model defaults and Cursor wrappers. The preflight calls the separately discovered setup-jstack resolver without copying it. That resolver selects a complete global or project configuration, with explicit selections taking precedence. Children receive the selected absolute path so their checkout cannot change routing. Inherited selections preserve the parent. Child briefs contain explicit context, fresh review rounds retain distinct task IDs, and the parent owns PR watches.

Activation until opt-out is a conversation instruction. Cursor mode frontmatter is not used as a portability or persistence mechanism. Resume and compaction remain separate evaluation requirements. T3 Code path-directed children do not acquire an app workspace binding from their prompt.

Publication, merging, installation and recurring work follow the user's authorized scope. Opening a PR is not an automatic ending for every task. Scoped evidence-based review replaces deletion-first comment rules; helper names do not require unrelated global skill installations.
