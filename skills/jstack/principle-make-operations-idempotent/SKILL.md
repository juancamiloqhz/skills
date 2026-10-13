---
name: principle-make-operations-idempotent
description: "Apply make operations idempotent guidance. Use for commands or loops subject to retries and partial failure."
---

# Make operations idempotent

Check repeated execution and crashes at meaningful transition points. Reconcile owned partial state, reuse durable identities and inspect uncertain outcomes before retrying external effects. Respect idempotency-key scope and retention. Establish ownership and liveness before clearing stale artifacts; a PID alone may be reused. No blind cleanup, repeated messages or schedule creation just because an earlier call timed out.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
