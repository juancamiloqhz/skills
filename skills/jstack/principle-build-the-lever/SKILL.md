---
name: principle-build-the-lever
description: "Apply build the lever guidance. Use when tooling would make nontrivial work repeatable or reviewable."
---

# Build the lever

Reuse an adequate tool or learn one representative unit, then build the smallest repeatable codemod, generator or check that earns its cost. Compare automated output with the known unit and make reruns safe. Prefer deterministic processing over delegates doing identical edits. For delegated work, retain a shared read-only recipe and verification contract. Do not build a framework or require a new script for every small change.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-build-the-lever](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-build-the-lever/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
