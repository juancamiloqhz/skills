---
name: principle-type-system-discipline
description: "Apply type system discipline guidance. Use when designing types or handling untyped inputs."
---

# Type system discipline

Parse external values into domain types at boundaries. Use distinct semantic types where interchangeable primitives cause mistakes, exhaustive variant handling and schema-derived types. Validate or narrow rather than hiding uncertainty with casts. Strengthen types where partial operations require it; a total operation such as summing an empty list needs no nonempty-list restriction.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
