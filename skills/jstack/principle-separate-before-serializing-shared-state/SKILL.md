---
name: principle-separate-before-serializing-shared-state
description: "Apply separate before serializing shared state guidance. Use when multiple actors might mutate the same object."
---

# Separate before serializing shared state

Inventory shared files, branches, keys and external state. Give independent actors separate owned artifacts and combine at a controlled boundary. If a single shared object is necessary, enforce serialization with one writer or real synchronization. Different fields in the same JSON file are still shared mutation. Prompt ownership alone is not a sandbox or lock.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
