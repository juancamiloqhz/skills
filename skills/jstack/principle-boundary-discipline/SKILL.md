---
name: principle-boundary-discipline
description: "Apply boundary discipline guidance. Use when wiring validation, adapters or error handling."
---

# Boundary discipline

Validate and narrow external data at CLI, config, network and storage boundaries. Keep domain logic testable without framework wiring and expose domain concepts rather than transport types. Avoid redundant checks only when invariants are established and maintained; internal mutation, concurrency and authorization can still require checks.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
