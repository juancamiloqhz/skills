# Shared investigation evaluation

This evaluation covers the bundled how/why procedures and shared evidence contract. It uses isolated local Git fixtures, inherited Codex selections and the installed setup-jstack resolver. The procedures are internal references inside juan-mode. They do not implement the planned Investigation playbook or complete the shared-procedure group.

## Cases and acceptance criteria

| Case | Required behavior |
| --- | --- |
| Narrow how | Resolve `how explainer`, dispatch one explainer and return a cited source explanation. Correctly trace batches, three total attempts, terminal timeouts and the absence of exactly-once guarantees. |
| Multi-component how | Resolve explorer and explainer roles, use two distinct exploration angles, then synthesize after both finish. Explain API validation, gateway ownership and the meaning of the returned count. |
| Historical why | Resolve investigator and synthesizer roles. Search local history and documents separately, trace the file rename, retain conflicting rationale, reject an unsupported throughput assumption and leave the unexplained attempt count unknown. |
| Unavailable model | Stop at failed role preflight. Do not dispatch a child, substitute a model, repair settings or produce an unconfigured explanation. |

The evaluators receive the actual user questions, fixture paths, helper references and read-only scope. Expected answers are not included in their briefs. The multi-component case explicitly selects the complex branch and two angles to exercise its coordination contract. Fixture code and tests are not executed; these are workflow executions that produce source-based explanations.

## Fixtures

The first fixture contains a sender callback, contiguous batches of two and a three-attempt timeout loop. Its three commits introduce the module, change batch size from three to two, then rename the module. The change commit cites a hard partner limit and disclaims a throughput benchmark. A document contradicts that explanation and supplies no measurements. No record explains the attempt count. An untracked sentinel represents existing user work.

The second fixture adds an API function and a validation module around the same gateway behavior. A successful API result returns the input count; the fixture has no receipt store, network implementation or deduplication mechanism. Both fixtures and their history are synthetic, not evidence about a real partner gateway.

The unavailable-provider configuration is a separate temporary copy with only the `how explainer` provider replaced by a nonexistent fixture provider. The user's global configuration remains unchanged.

## Evidence and limits

All four cases passed their acceptance criteria. Narrow how traced retries without claiming delivery guarantees. Multi-component how separated validation, gateway and sender ownership; host run timestamps confirm both explorers finished before synthesis. Historical why retained the conflicting document and commit, followed the rename and left the attempt-count rationale unknown. The unavailable-model case stopped at preflight with no child, fallback answer or configuration repair.

The parent verified four completed coordinator tasks and seven completed nested tasks with no pending runs. Both fixture histories, file contents and Git status remained unchanged, as did the evaluated skill sources and global model configuration. The complex explorers ran serially, so this case verifies phase ordering without establishing concurrent execution.

[Results](results.json) retain evaluated source hashes, fixture contents and history, coordinator and nested task identities, final answers, preflight observations and parent verification. Local raw artifacts under `/tmp/juan-investigation.anXUVCv7` may expire. The parent checks the final answers against source and commit bodies, verifies terminal lifecycle records and compares fixture/config hashes. A child's completion summary alone does not establish the result.

These cases use Codex and inherited selections. They do not establish other-provider behavior, live external connector searches, browser execution, actual compaction/restart, adversarial retrieved instructions or full playbook support. The how complex branch is tested with two explorers, not every permitted task count. Why's seven-category coverage includes explicit external-source exclusions; it does not claim those services were searched.

The shared-procedure group still needs architect, arena, swarm, interrogate, reflect, custom planning, principle mappings and their acceptance evidence. The existing foundation persistence requirements remain open.
