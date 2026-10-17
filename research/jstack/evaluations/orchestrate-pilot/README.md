# Orchestrate implementation pilot

This pilot extends the existing [replay exercise](../orchestrate-procedure/replay.py) to stop after one unit update but before its classification is saved. A new process must reconcile that effect and apply only missing work. This is a research reproducer, not a change to the shipped `orch` runtime or an automatic coordinator.

The [procedure draft](../../../../skills/jstack/jstack-juan-mode/playbooks/orchestrate.md) remains unavailable. The pilot must complete worker implementation, actual verification, a current-head ledger entry and authorized landing before further implementation units start. A process-exit exercise does not establish T3 restart durability.

## Scope and evidence

Base is merged PR #74, `d148e8a0796737f47fc01271be18138766d43747`. The implementation uses the saved `feature, refactoring` role, Codex gpt-6.1-sol at high effort, in an actual T3-bound worktree. The coordinator owns publication and durable records. No new workflow activation, installation, schedule, model-file change or host restart belongs to this pilot.

The implementation and saved `swarm workers` roles both select GPT-6.1-Sol. The coordinator requested a task-local Claude Opus 5.5/high verifier to meet the different-family requirement. That request does not alter the saved configuration and must be answered before the override is dispatched. The PR's current-head verdict and any unresolved gate are recorded in its body and the local ledger; an old verdict does not certify a changed head.

The coordinator store is `/home/ubuntu/.cache/jstack/orchestrate/recovery-pilot-20261017`. It retains standing orders, original task/run bindings, briefs, receipt classifications, the decision trail and the restart checkpoint. It is active recovery state, not a repository artifact. Raw reports and generated test data remain outside Git.

## Executed checks

The worker committed `6535083d19f906912e17de957a086a3abc84ace9` on its assigned branch and returned completed with no pending child work. The coordinator inspected the changed files, applied that commit cleanly, and separately ran the subprocess test against an exact cached runtime copy. Both interrupted and normal paths passed. Six changed-evidence cases were rejected before CLI access; repeated acknowledged replay preserved state and issued no unit updates. Test observations are synthetic; the worker task and its actual Git worktree/commit are live evidence.

The worker corrected an initial test expectation for the CLI count response and its invocation-log offset before the successful run. An initial commit used a command-local hooks-path override despite the brief; the worker replaced it with an ordinary amend using standard hook discovery. The coordinator records that deviation rather than claiming it never occurred. No hook configuration was persisted.

Independent verification and trail-review outcomes are external receipts associated with the actual PR head, so this document does not certify itself. The pilot remains incomplete while either review or landing is pending.

## Reproduction and limits

Run the adjacent `test_replay.py` against the actual helper with Bun and its declared dependencies already available. The evaluation README records the exact command and interruption option. Tests generate their own synthetic task observations, which are labeled as such; the test does not call T3 or authenticate a report. The parent checks live worker identity and actual commit separately.

The important observation is the resulting store and absence of repeated unit updates, not a plausible success message. An injected exit after the first application must leave a pending batch with one applied effect and no saved decision for it. Resumption must finish three assessed units and one duplicate disposition. Repeating an acknowledged run must do no new unit work. Changed original result identity or report content must not be accepted as the original evidence.

The exercise has one writer. It is not a distributed transaction or a production exactly-once guarantee. No application PR, provider cancellation, nested writer shutdown or host restart is implied by a subprocess test.

## Fidelity and remaining gates

The governing source is `pstack/skills/poteto-mode/playbooks/orchestrate.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`, especially Pilot, Queue and drain, Verification, and Liveness and failure. Its coordinator-owned acceptance and pilot-before-scale rules remain intact. The exercise has no one-to-one upstream source. Operational skills, runtime files, upstream manifest, reviewed checkpoint, lockfile and licenses remain unchanged; the existing draft's [source comparison](../orchestrate-procedure/source-comparison.json) still applies.

The dependency graph is recovery-exercise, then current-head evidence, then restart recovery. The latter two units remain blocked on pilot landing. Before any controlled restart, identify the component being restarted, preserve a reviewed checkpoint, isolate test writers and obtain the applicable restart authorization. A client reconnect alone cannot prove provider or server restart recovery.

## Example

Suppose three worker results are waiting. The coordinator records the first result and stops before saving its decision. On resume, it checks that the first result already took effect and processes the remaining two. The first task does not get applied twice.

This PR makes that local scenario reproducible. The pilot remains incomplete until its actual PR is verified and merged; Orchestrate remains disabled until the subsequent live recovery gates also pass.
