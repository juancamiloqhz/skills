---
name: principle-test-behavior-not-implementation
description: "Apply test behavior not implementation guidance. Use when adding or reviewing tests."
---

# Test behavior not implementation

Exercise the subject as a consumer does and assert concrete observable results. Avoid tautologies, expected values computed by the subject, or tests that pass when behavior is broken. Use positive controls for absence checks where appropriate. Empty results, no-call assertions, schema relationships and type-level tests are valid when they prove an actual contract; do not delete them by syntax alone.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
