---
name: principle-make-operations-idempotent
description: "Apply make operations idempotent guidance. Use for commands or loops subject to retries and partial failure."
---

# Make operations idempotent

Check repeated execution and crashes at meaningful transition points. Reconcile owned partial state, reuse durable identities and inspect uncertain outcomes before retrying external effects. Respect idempotency-key scope and retention. Establish ownership and liveness before clearing stale artifacts; a PID alone may be reused. No blind cleanup, repeated messages or schedule creation just because an earlier call timed out.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.

## Attribution

Adapted from [pstack principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/principle-make-operations-idempotent/SKILL.md). The bundled [MIT license](LICENSE) retains Lauren Tan's attribution. Jstack keeps this principle independently discoverable and scopes upstream absolutes to evidence, compatibility and task authority. Normal skill discovery supports direct requests and workflow callers.
