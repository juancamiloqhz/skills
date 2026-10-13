---
name: principle-fix-root-causes
description: "Apply fix root causes guidance. Use when diagnosing a failure."
---

# Fix root causes

Reproduce and trace evidence through the causal chain; instrument unknowns rather than guessing. Investigate persistent state for restart-only failures using safe copies or reversible experiments. Inspect related instances within scope. A containment guard can be justified while the cause remains unresolved; label that limitation and preserve useful rationale rather than treating every guard or long comment as wrong.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-fix-root-causes](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-fix-root-causes/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
