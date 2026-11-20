---
name: jstack-principle-type-system-discipline
description: "Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives, parse external data at boundaries, exhaust variants, derive from authoritative schemas."
---

# Type System Discipline

Make the compiler reject impossible states, mismatched primitives, and unhandled variants.

- **Brand semantic primitives.** If two arguments share a primitive type but mean different things, give each its own type. Validate once at creation.
- **External data is untyped until parsed.** JSON, RPC payloads, CLI args, config, environment variables, and database rows go through a parse function at the boundary that returns the typed model.
- **Derive types from authoritative schemas.** When a schema file owns a shape, derive the type from it instead of hand-rolling a parallel one.

For TypeScript syntax, see the **jstack-typescript-best-practices** skill.

Apply within the requested scope and existing authorization, preserving unrelated work and repository constraints. Direct invocation does not activate jstack-juan-mode or change model configuration.

Discover referenced skills through the current catalog and read their advertised paths; independently installed packages need not be siblings. Verify jstack identity when available and report ambiguity. If a required helper is unavailable, report the missing dependency and incomplete procedure, continue independent authorized work, and leave installation to the user.
