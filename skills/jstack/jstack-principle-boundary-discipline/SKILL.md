---
name: jstack-principle-boundary-discipline
description: "Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions."
---

# Boundary Discipline

Validate, narrow types, and handle errors where data crosses a system boundary (CLI args, config files, external APIs, network). Inside, trust the types where boundary validation and maintained invariants establish their guarantees: no re-validation and no redundant nil checks. Parse raw data into domain types at the boundary, and keep transport and framework types out of the public surface. Business logic lives in pure functions with no framework dependencies. The shell that calls them is thin.

Two tests. Is this data crossing a boundary right now? If not, avoid repeating an already established check. A new authorization decision, concurrent mutation, or stale external state can require a fresh check even inside the process. Can this be a pure function the shell just calls? If yes, extract it.

Apply within the requested scope and existing authorization, preserving unrelated work and repository constraints. Direct invocation does not activate jstack-juan-mode or change model configuration.
