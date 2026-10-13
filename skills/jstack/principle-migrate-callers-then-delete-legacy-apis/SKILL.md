---
name: principle-migrate-callers-then-delete-legacy-apis
description: "Apply migrate callers then delete legacy apis guidance. Use when replacing an internal API."
---

# Migrate callers then delete legacy apis

Inventory consumers, migrate callers and remove the superseded path together when all consumers are controlled and coordinated breakage is acceptable. Preserve public compatibility and independently deployed callers until their migration contract permits removal. Give necessary temporary adapters an owner, removal condition and verification rather than leaving dual paths indefinitely.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
