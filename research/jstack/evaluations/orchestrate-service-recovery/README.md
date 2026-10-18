# T3 service restart recovery

On 2026-10-18, one explicitly approved restart of `t3code.service` exercised the saved coordinator state and a live, bounded worker. The service returned, the coordinator recovered the same pending inbox batch without repeating an applied effect, and the worker's resumed reporting turn accounted for its stopped process. The worker did not complete its wait successfully. This is bounded service-recovery evidence, not machine-reboot durability or permission to enable Orchestrate.

## Setup and observed result

The repository was clean at merged PR #76, `12347fd3fe805b49528942f545b067bf5031c30e`. PR #75 had landed the implementation pilot and PR #76 the current-head check. The parent retained their original verdicts and did not treat them as verification of a new head.

The approved target was the Ubuntu user service, with no reboot, installation, configuration change or schedule change. Immediately before execution, metadata across ten projects showed only the parent and its probe active. The preflight checked 308 other unsettled threads for pending question IDs, with none returned. The one enabled schedule was next due at 15:09 UTC, outside the trial window. These observations were not an atomic lock against new activity.

The probe used the saved `feature, refactoring` selection, Codex `gpt-6.1-sol` with high effort. Its attached waiting process wrote actual process identities and a heartbeat, then waited up to ten minutes for a parent-owned release file. It had no repository write scope or service-control authority. The saved model configuration remained unchanged.

| Observation | Result |
| --- | --- |
| Authorized command | `systemctl --user restart --no-block t3code.service`, once, issued at 02:18:41 UTC; the parent observed exit 0 in the tool response, which is not preserved in the pre-command intent file |
| Actual service transition | Main PID changed from 767946 to 1769327; new start time 02:18:45 UTC; service active/running afterward |
| Machine identity | Boot ID unchanged; this was not a reboot |
| Worker process | PID 1768495, start ticks 514379151, absent after restart; original Codex provider PID also absent |
| Last worker heartbeat | 02:18:44 UTC, about 65 seconds after the wait started, before its ten-minute timeout |
| Worker task accounting | Original run ordinal 1 was cancelled; T3 started a later reporting turn, ordinal 2, which completed with no pending child work or questions |
| Worker result | `incomplete/process-unavailable`; no release or successful completion file; no replacement waiter |
| Repository and saved state | Before recovery writes, Git HEAD, working tree, retained worktrees, model-file hash, trial rows, ledger and pending evidence hashes matched the checkpoint |

The Python and Codex processes occupied a separate systemd agent scope, although their ancestry reached the T3 server. The initial preparation assumption that they belonged directly to the service cgroup was corrected before restart. T3's later reporting turn wrote `outcome.json` into the original worker directory after its own check that the waiting process was absent. The parent had not dispatched that reporting turn, so future recovery must account for runtime-initiated writers too. The observed process loss does not establish its exact termination mechanism. Neither a changed service PID nor a terminal task status proves that worker code succeeded.

## Inbox recovery

The durable trial store held two pointers to the same real, previously completed PR75 verifier result. They were deliberately replayed as evaluation input, not new completions. Before restart, the first pointer's `prior-result` row was already `observed-before-restart`, its partial receipt was saved, and the second pointer remained unclassified. The trial ledger contained only its header.

After restart, the actual `orch inbox claim` returned the same batch ID, `88267073-7ed0-453b-91bb-96d6accebec4`, with both pointers pending. The parent checked pointer hashes, original task/run/result identity, copied report hash and prior applied state. It preserved the first effect and classified the second pointer as a duplicate with no effect. It saved a complete receipt, rendered status, and acknowledged the batch. A second acknowledgement with the same receipt also succeeded. The inbox was empty; unit and ledger bytes were unchanged by recovery. No new verification verdict was written.

This recovery used the shipped CLI from an exact durable copy with an already-present dependency. The parent made the classification decisions. The CLI did not authenticate the review or provide automatic exactly-once processing.

## Reproduction and evidence retention

The local replay and current-head checks remain reproducible without restarting a service:

- [Partial-application replay](../orchestrate-procedure/README.md) and its committed test script.
- [Current-head verification](../orchestrate-current-head/README.md) and its committed test script.

The live trial requires a separate, explicitly approved service window. Prepare a pending batch and partial receipt, save original task/run and process identities, establish that unrelated work is idle, and start a bounded probe. Save the checkpoint before the named restart. After reconnect, verify the actual service transition and each writer's state before recovering the same batch or creating replacements. Inspect the result, not just command exit codes.

This report is the committed evidence summary. Full metadata, catalogs, receipts, process snapshots and the decision trail remain in task-owned cache while review needs them. They are not packaged with skills or required by the local reproducers. Keep unique unresolved evidence until its finding is captured; follow the repository retention policy before cleanup.

## Fidelity and limits

Compared the final unchanged local [Orchestrate draft](../../../../skills/jstack/jstack-juan-mode/playbooks/orchestrate.md) with `pstack/skills/poteto-mode/playbooks/orchestrate.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`, especially Close, Queue and drain, Verification, and Liveness and failure. The existing [adaptation record](../../adaptations/orchestrate.md) explains the T3 status and recoverable-inbox substitutions. This research report has no one-to-one upstream file. No operational skill, source mapping, pin or reviewed checkpoint changes here.

The trial supports recovery of this saved batch after this one service restart. It does not prove uninterrupted workers, an automatic post-restart coordinator, machine reboot or disk loss recovery, nested-writer shutdown, a fresh replacement worker, other provider families, or automatic duplicate/stale-result enforcement. T3's resumed reporting turn was observed; the parent did not request a new implementation round through the old child thread. Orchestrate stays unavailable until the release-readiness assessment accounts for the pilot, current-head evidence, this bounded recovery and remaining limitations.

For example, if two notifications describe the same finished task and T3 restarts after the first was recorded, the coordinator can read its saved record and skip the duplicate. This trial demonstrates that manual recovery path. It does not make a stopped worker's task successful.
