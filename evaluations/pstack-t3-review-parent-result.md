# Complete fresh-parent result

<!-- markdownlint-disable MD036 MD060 -->
<!-- Preserve the historical response formatting below. -->

The panel recommends **one PostgreSQL database containing an inbox, account state, and a notification outbox**. Use Astra’s candidate A as the base, incorporating Opus’s more explicit retry and recovery policies.

This prevents repeated database mutations and stale snapshot overwrites. Notification duplicate prevention depends on the API’s idempotency contract, especially its retention window.

**Recommended design**

| Record | Purpose and essential data |
|---|---|
| Inbox | Durable queue and accepted-event ledger: unique source/tenant/event ID, account ID, revision, validated payload/hash, processing outcome, retry metadata |
| Account | Current projection and last applied authoritative revision; preserve deletion/generation metadata |
| Notification outbox | Unique intent per event and notification kind, frozen destination/payload, stable idempotency key, delivery status, retry metadata, lease token/expiry, first possible submission time |

No separate broker is necessary for this small service.

1. **Accept durably.** Verify the signature over the original bytes and validate the envelope. Insert a pending inbox record under a database unique constraint. Return success only after commit, or after confirming an existing matching committed record. Concurrent duplicates converge on that constraint. A database failure or uncertain commit returns a retryable error; a subsequent delivery safely discovers any committed insert.

   Reuse of an event ID with contradictory content is an integrity failure: preserve the original record, reject or quarantine the conflicting delivery, and alert.

2. **Apply atomically.** In one short PostgreSQL transaction, lock a pending inbox row, safely create and lock its account row, check the source revision, update account state when appropriate, insert the notification intent, and mark the event processed. Commit all of these together. Make no external API call inside this transaction.

   For complete snapshots, apply only revisions greater than the account’s last applied revision. Mark older revisions superseded. Equal revisions must represent identical state under the source contract; contradictory equal revisions require investigation. All writers of the affected account fields must obey the same locking and revision rules.

3. **Recover processing.** Workers poll due inbox records; an optional wake-up signal only reduces latency. Row locks and rollback recover a worker crash during the short processing transaction. Configure database timeouts so hung connections eventually release locks.

   Retry transient failures with capped backoff and jitter. Update failure metadata conditionally so a failed worker cannot overwrite another worker’s completed outcome. Retain poison events, alert, and provide controlled replay. For recurring hard crashes that bypass exception handling, use durable attempt-start accounting or crash monitoring. Exhausting a retry budget must retain the accepted work for recovery.

4. **Dispatch separately.** Claim an outbox row in a short committed transaction with an expiring lease and fresh claim token. Call the notification API outside PostgreSQL using the stored idempotency key and exact frozen payload. Record success or retry metadata only while the claim token still matches.

   Expired leases permit recovery. They can also permit overlapping external requests; duplicate prevention therefore requires the provider to handle concurrent requests with the same key atomically. Interpret response codes using that provider’s documented contract.

5. **Handle delivery ambiguity.** If the API delivers and the worker crashes before recording success, a replacement worker resends the same key and payload. Within the provider’s guaranteed deduplication window, this recovers the prior operation without producing another notification.

   Record the earliest possible submission time durably before calling the API. Never change the key between attempts or rebuild content from current state. Stop ambiguous retries before the provider’s retention window expires, with allowance for request delays and clock uncertainty.

   After that window, use a reliable provider lookup if available. Otherwise retain an unknown-outcome record and make an explicit duplicate-versus-missed-notification decision. A local “sent” flag cannot eliminate this uncertainty.

**Necessary assumptions and boundaries**

- PostgreSQL preserves acknowledged commits across the failures being covered. Local synchronous commit alone does not guarantee survival of failover to a lagging replica.
- Event IDs are immutable and appropriately scoped. Account identity and source revision are trustworthy.
- The minimal ordering design assumes **complete snapshots with authoritative, comparable per-account revisions**. Receipt time is not an ordering key.
- Only snapshots that advance state require notification by default. Requiring every historical event to produce an action changes the design.
- The notification provider documents key scope, concurrent-request behavior, retention duration, payload consistency requirements, and what “success” means. API acceptance may differ from end-user delivery.
- Recovery assumes workers eventually resume and dependencies become available. Permanent failures require reconciliation.
- Notification delivery order is unspecified by this minimal design. If it matters, add a per-account delivery policy; unresolved earlier intents may block later ones.

For **delta events**, accepting any greater revision is unsafe: it can lose intermediate mutations. Apply only the expected successor, park later deltas in the existing inbox, and release them when predecessors commit. Missing predecessors require recovery from the source or an authoritative snapshot with a trustworthy version. If every intermediate delta has business effects, replacing them with a snapshot requires additional reconciliation.

Without a trustworthy ordering key, fetching “current state” is not automatically sufficient: concurrent fetches can complete in reverse order. Such a fallback needs a versioned authoritative response or a documented serialization and consistency contract. The supplied problem does not establish either.

Use the sender’s documented signature freshness/redelivery behavior. Do not automatically relax signature verification simply because events may be redelivered days later.

**Ownership and retention**

The upstream source owns event identity, revision semantics, and source account truth. The service owns its accepted-event ledger, account projection, processing outcomes, and notification intents. The notification provider owns its external execution and deduplication ledger. Keep source-owned account fields separate from locally owned fields.

- Retain event identity tombstones and outcomes for the entire allowed redelivery **and internal replay** horizon. If that horizon is unbounded, retain them indefinitely.
- Payloads may be removed after their processing, recovery, audit, and privacy needs end; preserve the metadata needed for deduplication and integrity checks.
- Preserve account revisions and deletion/generation tombstones so late events cannot recreate obsolete accounts.
- Never automatically purge pending, failed, parked, or ambiguous work needed for recovery.
- Compact completed outbox records only when retained metadata prevents unintended recreation of the same intent. Retention is not determined solely by the provider’s key TTL.
- Back up related state consistently. Even a consistent restore to an earlier point can erase local evidence of an already delivered notification; reconcile before replaying external effects.

**Failure verification**

| Scenario | Expected outcome |
|---|---|
| Concurrent deliveries of the same ID | One durable inbox record |
| Inbox commit succeeds; HTTP response is lost | Redelivery discovers the existing record |
| Worker crashes before processing commit | Mutation, marker, and intent roll back together |
| Worker crashes after processing commit | Mutation remains recorded; outbox remains deliverable |
| Newer snapshot is processed before an older one | Older snapshot cannot overwrite newer state |
| Two workers process one account | Account lock serializes revision decisions |
| Delta arrives before its predecessor | Park it; do not skip the missing mutation |
| Notification worker dies before calling API | Lease expires; another worker recovers |
| API delivers; success recording is lost | Retry the same key/payload within provider guarantees |
| Lease expires during an API call | Provider deduplicates overlapping same-key requests |
| Ambiguity outlasts provider key retention | Reconcile or explicitly accept duplicate/loss risk |
| Account is deleted; old event returns | Tombstone/generation policy prevents resurrection |
| Restore loses local delivery evidence | Reconcile; ordinary retries alone are insufficient |

These are design-level checks, not executed tests. No implementation was requested.

**Panel assessment and parent corrections**

The fresh judge scored the candidates as follows:

| Criterion, out of 5 | A: Astra | B: Opus |
|---|---:|---:|
| Durable acceptance and deduplication | 4 | 4.5 |
| Atomic mutation, marker, and intent | 4.5 | 4.5 |
| Ordering and snapshot/delta assumptions | 4 | 4.5 |
| Crash recovery and retries | 4 | 4 |
| Notification ambiguity and provider limits | 4.5 | 4.5 |
| Ownership and retention | 4 | 4.5 |
| Minimality and failure scenarios | 4.5 | 3.5 |
| **Total** | **29.5/35** | **30/35** |

The judge selected A despite the near-tied scores because it better fits the smallest-design requirement. I agree. Incorporated contributions from B include explicit parked-delta recovery, provider-specific retry handling, durable first-attempt timing, and failover considerations.

My review makes four corrections to the judge/candidates:

- **Delivery is not unconditionally at least once.** Stopping ambiguous retries or retaining permanent failures can leave a notification undelivered.
- **Fetching current state without ordering guarantees is insufficient.** It can introduce its own stale-write race.
- **Hard-crash attempt accounting improves operations; it is not required for atomic mutation correctness.** Pre-incremented counters can also consume attempts during benign crashes.
- **Tombstone retention and signature policy need stronger contracts.** Revision checks do not replace the complete accepted-event ledger, and relaxing signature freshness is not a general solution.

Rejected approaches include in-memory/TTL deduplication, check-then-insert without database uniqueness, separate mutation/processed commits, sending or marking sent before the database work commits, and treating an external call inside a database transaction as atomic.

Remaining uncertainty concerns snapshot versus delta semantics, revision guarantees, replay horizons, notification ordering, provider idempotency behavior, database durability, and the policy for expired ambiguity.

**Execution settings and receipts**

All three delegated tasks completed successfully with usable results and no pending child runs. There were no dropouts or substitutions. Both candidates independently received the same brief and rubric; the fresh judge received both complete answers labelled A/B without candidate model names.

| Seat | Provider | Model | Explicit options | Request ID |
|---|---|---|---|---|
| Candidate A | `codex` | `gpt-6-astra` | `reasoningEffort=medium`, `serviceTier=default` | `pstack-webhook-20261006-A-1` |
| Candidate B | `claudeAgent` | `claude-opus-5-5` | `effort=medium`, `fastMode=false`, `contextWindow=1m` | `pstack-webhook-20261006-B-1` |
| Fresh judge | `claudeAgent` | `claude-sonnet-5-5` | `effort=medium`, `contextWindow=200k` | `pstack-webhook-20261006-J-1` |

Options above are the submitted settings; receipts confirmed provider/model selection.

```text
Candidate A task:
node:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-A-1
Candidate A thread:
thread:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-A-1

Candidate B task:
node:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-B-1
Candidate B thread:
thread:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-B-1

Judge task:
node:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-J-1
Judge thread:
thread:delegated-task:command%3Amcp%3A49f6073f-ae73-4c51-b3e3-b119027dfe4f%3Adelegate-task%3Apstack-webhook-20261006-J-1
```

Every participant acknowledged reading [the skill](/home/ubuntu/Dev/skills/skills/pstack-t3-review/SKILL.md) and [its orchestration reference](/home/ubuntu/Dev/skills/skills/pstack-t3-review/references/t3-orchestration.md). The evaluation used only those files, the supplied problem, and orchestration metadata/results. No repository browsing, previous evaluation inspection, filesystem edits, installation, publication, or external service writes were performed. Read-only restrictions were instructions; provider runtime isolation was not independently verified.
