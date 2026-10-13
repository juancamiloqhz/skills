# Evidence principles

Read only the sections selected by the [index](index.md). These rules operate within the task’s authorization and repository constraints.

## prove-it-works

Observe the requested artifact through its real interface and inspect decisive evidence. Compilation, timestamps or worker summaries alone do not establish product behavior. Investigate the observation method when a result is suspicious. Keep rerunnable checks where useful and distinguish verified, failed and inconclusive results.

## test-behavior-not-implementation

Exercise the subject as a consumer does and assert concrete observable results. Avoid tautologies, expected values computed by the subject, or tests that pass when behavior is broken. Use positive controls for absence checks where appropriate. Empty results, no-call assertions, schema relationships and type-level tests are valid when they prove an actual contract; do not delete them by syntax alone.

## explain-the-number

Keep workload, method, run count and spread with the result. Investigate limiting resources with profiles or counters and map evidence to source; a code-reading guess is not a measured bottleneck. Check for skipped, cached, failed or untuned work and end-to-end relevance. For evaluations, distinguish one case from reliability across trials and models. Unknown limiters or inadequate samples must qualify claims rather than become fabricated explanations.

## fix-root-causes

Reproduce and trace evidence through the causal chain; instrument unknowns rather than guessing. Investigate persistent state for restart-only failures using safe copies or reversible experiments. Inspect related instances within scope. A containment guard can be justified while the cause remains unresolved; label that limitation and preserve useful rationale rather than treating every guard or long comment as wrong.

## attack-the-premise

Write the shared premise before trying another similar fix. For an actor imbalance, capture a rerunnable per-actor census and inspect persistent skew and role assignment. Test whether changing the assignment removes the asymmetry instead of adding compensating work. Even counts weaken that particular hypothesis but do not prove the premise irrelevant. For other failure classes, choose an analogous discriminating experiment rather than forcing an actor census.

## build-the-lever

Reuse an adequate tool or learn one representative unit, then build the smallest repeatable codemod, generator or check that earns its cost. Compare automated output with the known unit and make reruns safe. Prefer deterministic processing over delegates doing identical edits. For delegated work, retain a shared read-only recipe and verification contract. Do not build a framework or require a new script for every small change.

## encode-lessons-in-structure

When several mechanisms can prevent the failure, prefer the strongest suitable enforcement within scope: an unrepresentable state, then CI lint or a banned API, then a canonical helper, then a runtime check. External data still requires runtime validation where static guarantees cannot apply. Verify the mechanism catches the failure, then remove redundant reminders while keeping useful explanations. Judgment-dependent guidance can remain prose with a concrete example. Apply within scope or record a concrete follow-up; no automatic issue filing or private-memory write.
