---
name: principle-laziness-protocol
description: "Apply laziness protocol guidance. Use when tempted to add layers or widen a refactor."
---

# Laziness protocol

Choose the smallest coherent change that meets the outcome. Look for removable duplication and unnecessary pass-throughs before adding mechanisms. Keep a single source for decisions and question signals threaded through many layers. Measure comprehension rather than enforcing a line-count or fixed-layer quota.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-laziness-protocol](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-laziness-protocol/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
