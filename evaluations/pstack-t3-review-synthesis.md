# Synthesized queue design

This text artifact evaluates the review workflow. It is not an implementation or deployment recommendation validated against a database or a specific external API.

Store one row per logical job with a unique non-null key, immutable payload and external idempotency key, status, availability time, lease deadline, increasing claim epoch, attempt count, result, and error. Retain completed rows or tombstones throughout the required enqueue-deduplication window. If enforcing an attempt limit, define terminal handling explicitly.

Enqueue using the logical-key uniqueness constraint. A conflicting request returns the existing job after reading the committed winning row, retrying that read if needed. Reject a reused key with a different payload. Never reset completed state or replace the stored external key on duplicate enqueue.

Claim in a short transaction. Select eligible queued or expired running rows with `FOR UPDATE SKIP LOCKED`; after locking, recheck eligibility using current database time. Set running state, increment the epoch and attempts, and establish the lease. Return the immutable request and epoch; commit before contacting the API. A heartbeat renews only a matching running epoch with a still-live lease, using time evaluated after locking.

Serialize completion and retry transitions on the same row. Require running state and the matching epoch. A completion after expiry can be accepted if no newer claim exists. If completion wins the lock first, its success transition makes the job ineligible for reclaim. If reclaim wins first, the increased epoch rejects the old completion. Expired workers cannot overwrite newer ownership. Heartbeat renewal remains stricter than result acceptance.

Retryable failures schedule backoff and clear lease fields. When the attempt budget is exhausted, transition to dead instead of queued. Recovery must also handle exhausted queued rows and expired running rows. A dead job with an ambiguous external outcome requires reconciliation rather than assuming no effect occurred.

For every attempt, send the same external idempotency key and semantically identical request. If a worker crashes after the effect but before completion, a later owner repeats that request and records the provider's replayed result. If the old worker resumes after reclaim, its epoch cannot publish completion.

The queue permits repeated execution attempts. Preventing duplicate external effects depends on the API's concurrent deduplication, key retention, and replay behavior. A live lease guarantees one database owner, not one executing process. If retention might have expired, reconcile the ambiguous outcome before retrying. Finite lease durations or pre-call ownership checks cannot eliminate in-flight requests from paused workers.

Base: candidate B, with candidate A's retention, conflict-read, time, and uncertainty handling. B's exhausted-retry gap is corrected. Row-ordering and crash scenarios were checked conceptually; no SQL or network calls were executed.
