# Coordination principles

Read only the sections selected by the [index](index.md). These rules operate within the task’s authorization and repository constraints.

## separate-before-serializing-shared-state

Inventory shared files, branches, keys and external state. Give independent actors separate owned artifacts and combine at a controlled boundary. If a single shared object is necessary, enforce serialization with one writer or real synchronization. Different fields in the same JSON file are still shared mutation. Prompt ownership alone is not a sandbox or lock.

## make-operations-idempotent

Check repeated execution and crashes at meaningful transition points. Reconcile owned partial state, reuse durable identities and inspect uncertain outcomes before retrying external effects. Respect idempotency-key scope and retention. Establish ownership and liveness before clearing stale artifacts; a PID alone may be reused. No blind cleanup, repeated messages or schedule creation just because an earlier call timed out.

## guard-the-context-window

Store bulk output in owned artifacts and read focused sections with source pointers. Preserve decisive evidence, task IDs, configuration path, scope and outstanding work in handoffs. Use bounded delegated analysis when authorized and useful; do not spawn agents solely to hide unread evidence. Compaction and resume require state recovery, not a claim that context is permanently lost or automatically retained.
