# Swarm evaluation

Authoring-source evaluation against main revision `c86795d2b986f67e03d758fba4a496ecec0a09aa` plus the Swarm working changes. Raw artifacts remain in `/tmp/jstack-swarm-vo52ej_y`. Explicit skill paths were supplied, so installed discovery was not tested. A temporary copy of global settings retained the scalar inherited `swarm workers` selection; two workers were requested per task without changing configuration.

## Executed results

| Case | Outcome | Evidence |
| --- | --- | --- |
| Partitioned source/history coverage | Both required slices recorded the exact SHA and completed. Coverage was complete with ISSUES because documentation contradicted the recorded batching rationale. | [Coverage record](coverage-results.json) |
| Rank-all design race | Both workers returned valid interval-merging designs with the pinned specification hash. The declared correctness, clarity and complexity ranking produced a justified tie. | [Race record](race-results.json) |

The coverage coordinator checked source paths and the fixture's three-commit history, distinguishing current documentation conflicts from historical mismatches already resolved. It did not execute fixture behavior. The race coordinator inspected validation order, input preservation, overlap/adjacency handling and complexity in both designs. No runnable interval implementation or runtime product tests were created. Each original report is retained with its brief, task receipts and actual inherited identity.

All four workers completed without pending nested work. Writers ran serially in separate owned report paths; this does not establish concurrent-write isolation or a wall-clock speedup. The parent checked terminal receipts, report hashes, pinned input and protected fixture/config hashes. Real global settings were unchanged.

## Deviations and limits

The coverage run recorded an overbroad instruction-file search by worker 1, which crossed the evaluation-directory discovery boundary. The coordinator also hashed the parent's newly saved race-results file during its repository integrity scan. Neither result was used as task evidence, but these are scope deviations, so coverage completion is not an unqualified instruction-compliance pass. The parent created the added report file; it was not an unauthorized worker write. Existing source and fixture files remained unchanged.

The missing-SHA retry case was a separate static tabletop assessment: reject the first incomplete report, permit one fresh retry, then record a required-slice gap after the second omission. No retrying worker was actually dispatched. Actual dropout/retry recovery, first-pass cancellation, best-of selection, mixed shapes, measurements, source integration, concurrent writers and cross-provider execution remain untested.

All worker receipts identify Codex `gpt-6-astra`; omitted targets preserve inheritance but do not prove model diversity or independently attest effort. Filesystem integrity checks exclude ignored files and a complete machine-wide audit. The 23 juan-mode playbooks remain planned.
