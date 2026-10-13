# Design principles

Read only the sections selected by the [index](index.md). These rules operate within the task’s authorization and repository constraints.

## foundational-thinking

Choose data structures around actual access patterns and establish contracts and verification needed by dependent work. Examine shared mutable state before concurrency. Reuse existing foundations; remove evidenced dead code within scope rather than constructing speculative infrastructure.

## model-the-domain

Represent real states and ownership with a suitable state machine, typed model, registry or cohesive module. Prefer a shape that removes invalid combinations or duplicated rules. Keep clear local code when an abstraction would only add indirection.

## type-system-discipline

Parse external values into domain types at boundaries. Use distinct semantic types where interchangeable primitives cause mistakes, exhaustive variant handling and schema-derived types. Validate or narrow rather than hiding uncertainty with casts. Strengthen types where partial operations require it; a total operation such as summing an empty list needs no nonempty-list restriction.

## boundary-discipline

Validate and narrow external data at CLI, config, network and storage boundaries. Keep domain logic testable without framework wiring and expose domain concepts rather than transport types. Avoid redundant checks only when invariants are established and maintained; internal mutation, concurrency and authorization can still require checks.

## exhaust-the-design-space

Compare two or three structurally distinct sketches or prototypes against explicit constraints before committing. Mechanical work with an established target needs no tournament. If delegating to Architect or Arena, use its configured panel contract; this principle does not authorize extra seats or models.

## redesign-from-first-principles

Read affected code and ask what design would include the requirement from the start. Compare that target with the smallest coherent adaptation, then deliver justified changes incrementally. Update affected types, callers, tests and documentation. This reasoning step does not authorize a whole-system rewrite.

## experience-first

Evaluate the experience of end users, API consumers and maintainers. Prefer a polished core flow, clear feedback and useful error states; use focused prototypes for uncertain interactions. Simplify proposed scope openly, without silently dropping user requirements. Foundations determine sequence, while user needs determine the target.
