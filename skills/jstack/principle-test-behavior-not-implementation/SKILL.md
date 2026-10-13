---
name: principle-test-behavior-not-implementation
description: "Apply test behavior not implementation guidance. Use when adding or reviewing tests."
---

# Test behavior not implementation

Exercise the subject as a consumer does and assert concrete observable results. Avoid tautologies, expected values computed by the subject, or tests that pass when behavior is broken. Use positive controls for absence checks where appropriate. Empty results, no-call assertions, schema relationships and type-level tests are valid when they prove an actual contract; do not delete them by syntax alone.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-test-behavior-not-implementation](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-test-behavior-not-implementation/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
