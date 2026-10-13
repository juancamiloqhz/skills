---
name: principle-minimize-reader-load
description: "Apply minimize reader load guidance. Use when code is hard to trace."
---

# Minimize reader load

Assess both indirections to follow and mutable state to remember. Prefer boundaries that hide meaningful decisions, local state and derived values over synchronized copies. Collapse layers that add no useful abstraction while retaining justified adapters. The goal is understanding where a value comes from and what can change it, not a timed reading quota.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
