---
name: principle-boundary-discipline
description: "Apply boundary discipline guidance. Use when wiring validation, adapters or error handling."
---

# Boundary discipline

Validate and narrow external data at CLI, config, network and storage boundaries. Keep domain logic testable without framework wiring and expose domain concepts rather than transport types. Avoid redundant checks only when invariants are established and maintained; internal mutation, concurrency and authorization can still require checks.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-boundary-discipline](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-boundary-discipline/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
