# Recover an interrupted PR-status request

Use the service's recorded helper snapshot, journal and fixed scope. Require the journal to exist before calling the helper; a new empty database cannot recover old requests. Keep it private for the service lifetime. Inspect owned task/run status and the matching conversation messages before treating a missing reply as failed delivery.

The normal receiver performs `pending`, then `claim --request-id ID --owner OWNER`, one successful query, `save-result` with exact query JSON on stdin, `result --request-id ID`, publication, and `ack --request-id ID --owner OWNER --evidence REFERENCE`. Each command follows the fixed prefix `python3 HELPER --journal JOURNAL --repository REPOSITORY --pr PR`. Use argument arrays for paths/values; inspect JSON responses, not only exit codes.

| Observed state | Action |
| --- | --- |
| No journal record or payload mismatch | Do no work. Reconcile the original scope and browser request ID; never manufacture a record to justify execution. |
| Unowned pending record | A valid wake may drain it from its one bounded snapshot. An explicitly requested manual recovery may use the same claim/query/save/publish/ack protocol, reported as manual recovery. Never resend the webhook. |
| Lost claim response or an owned record without a result | Inspect the original run and journal. Do not claim again, reset the owner or repeat the query. Report incomplete if whether it ran cannot be established. |
| Lost save response | Read `result --request-id ID`; require the exact expected payload and query observation. Reconcile the original owner's known successful output; do not query GitHub again or replace an observation. |
| Saved result without acknowledgement | Read and validate the saved observation, then publish it with its request ID and `savedAt`. Only the original run/owner may acknowledge. Another run can redisplay the saved result but must leave the claim unacknowledged. |
| Acknowledged result, missing conversation message | Read and validate `result --request-id ID`, then redisplay it as a historical observation with its save time. Preserve the existing acknowledgement. This is not a fresh status check. |
| Legacy `acknowledged_without_result` | Report that no durable observation exists. Do not backfill it from a later query or treat it as pending work. |

A completed CLI operation may be repeated only where the contract explicitly permits identical saves or acknowledgements by the original owner. A repeated claim always fails, including for the same owner. Never interpret that as permission to execute.

Publication must precede acknowledgement. Use a real result link if the host provides one, otherwise `thread:THREAD_ID;request:REQUEST_ID` as a transcript search reference, not an invented URL. If acknowledgement fails, report delivery without confirmed recording. If the conversation rolled back, saved observations allow redisplay; the helper cannot detect rollback or guarantee that a published reply stays visible.

If no wake arrives, the record waits for a later wake or explicit recovery. There is no background poller and a crashed owner can leave a request stuck. Preserve uncertain evidence privately until reconciliation. This protocol does not promise exactly-once effects or enforce every action the receiving agent takes.
