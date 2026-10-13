---
name: principle-minimize-reader-load
description: "Apply minimize reader load guidance. Use when code is hard to trace."
---

# Minimize reader load

Assess both indirections to follow and mutable state to remember. Prefer boundaries that hide meaningful decisions, local state and derived values over synchronized copies. Collapse layers that add no useful abstraction while retaining justified adapters. The goal is understanding where a value comes from and what can change it, not a timed reading quota.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-minimize-reader-load](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-minimize-reader-load/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
