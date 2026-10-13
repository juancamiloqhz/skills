---
name: principle-build-the-lever
description: "Apply build the lever guidance. Use when tooling would make nontrivial work repeatable or reviewable."
---

# Build the lever

Reuse an adequate tool or learn one representative unit, then build the smallest repeatable codemod, generator or check that earns its cost. Compare automated output with the known unit and make reruns safe. Prefer deterministic processing over delegates doing identical edits. For delegated work, retain a shared read-only recipe and verification contract. Do not build a framework or require a new script for every small change.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
