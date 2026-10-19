# Benny event and adapter contract evaluation

2026-10-19, Orbit/Linux, Python 3.14. The inactive pack merged in PR #117. This unit adds repository-only [contract code](../../../../scripts/jstack/benny_contracts.py) and [synthetic tests](../../../../scripts/jstack/test_benny_contracts.py). It creates no receiver, scheduler task, Slack/tracker client, child agent or installation. The operational pack is unchanged.

## What passed

All 30 new contract tests and nine existing pack/discovery tests pass, 39 total. The documentation checker reports zero problems. They exercise real HMAC verification, JSON normalization, SQLite transactions and process boundaries. Slack and tracker effects use explicit in-memory fakes. The triage driver consumes a prepared decision; it does not classify a report, trace code, generate verdict prose or reproduce a bug.

| Boundary | Observed result |
| --- | --- |
| Authentication | Modified bytes, wrong signatures, stale/future timestamps and malformed headers fail before intake. JSON with duplicate keys or malformed shapes is rejected. |
| Fixed report identity | Requires the configured app, workspace and channel. Preserves string timestamps; rejects numeric/bool timestamps, conflicting aliases, replies, edits, deletions and bot markers. Ordinary human messages and human file-share envelopes pass. Unknown fields cannot choose a command, URL or repository and are not retained. Real connector envelopes remain untested. |
| Durable intake | The event and both stage records commit before receive returns. Database failure produces no accepted result. Duplicate event IDs with changed bytes fail; different event IDs for the same root share work. |
| Concurrent claims | Twelve deliveries across four Python processes produce one triage owner and one reproduction owner. Each stage is independently claimable, including reproduction before triage. This does not test T3 dispatch or its scheduling concurrency. |
| Crash and lost results | A subprocess writes one synthetic effect and exits before recording its result. The pending intent and owner survive reopening; retry cannot repeat the effect. Lost create/update/post/cancel responses likewise retain unresolved evidence. A saved receipt survives reopening without another write. |
| Source preflight | Initially missing, inaccessible or mismatched parents, including a reply or operations channel, cause zero Slack/tracker writes. A second preflight occurs before each forward write. If the parent disappears after an issue was created, no verdict is attempted and only that owned issue is compensated. |
| Tracker decisions | A qualified new bug creates once; a confident duplicate only adds recurrence and preserves existing owner/labels/state. Possible duplicates only link. Prior source links or verdicts suppress writes. Other classifications, unresolved fields or unmet creation gates cannot create. Missing compensation capability blocks creation. |
| Handoff failure | A definitive rejected verdict cancels the issue created by that run and verifies cancellation. Direct compensation of a pre-existing or unrelated issue is rejected. Unknown post results/read-back preserve the issue and claim for reconciliation. Unverified compensation never becomes completion. |
| Marker trust | Accepts exactly one configured bug/performance marker from the configured identity in a reply to the exact root. Spoofed authors, wrong coordinates, root messages, missing timestamps, repeated/conflicting markers and `other` do not authorize reproduction. No polling window or UI action is implemented. |

SQLite connections are closed explicitly. Initial development checks exposed unclosed connections and a test-fixture inheritance error; both were corrected before the passing run. No raw transcripts or databases are retained.

## Reproduce

```sh
python3 -B -W error::ResourceWarning -m unittest discover -s scripts/jstack -p test_benny_contracts.py -v
```

Tests generate and delete their own envelopes, SQLite files and crash-effect file. The signing key is public fixture data. No real secret, Slack workspace or tracker is read. Run the existing dormant-pack suite separately for copying/discovery compatibility:

```sh
JSTACK_SKILLS_CLI=/path/to/skills/dist/cli.mjs \
JSTACK_UNSLOP_SOURCE=/path/to/unslop \
python3 -B -m unittest discover -s scripts/jstack -p test_benny_pack.py -v
node scripts/jstack/check_docs.mjs
```

Example: a report is delivered repeatedly while the first triage run is working. The contract grants one triage claim and one independent reproduction claim for that root. If the tracker creates an issue but its response is lost, the run remains incomplete instead of creating another issue. This is the behavior a future live adapter must demonstrate; ordinary jstack users do not invoke these test helpers.

## Source and runtime comparison

Compared against pinned [`pstack/automations/benny`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/automations/benny). The local pack retains its previously recorded [T3 adaptations](../../adaptations/benny.md); this unit changes none of its files, phase order, model choices or the reviewed checkpoint.

The driver exercises triage steps 1 and 6–9, plus reproduction steps 1–2. The full skills still own evidence review, cause tracing, classification, ownership, UI proof, follow-up and fix decisions. The new journal and request verifier have no upstream code counterpart. They are a contract implementation for the approved T3 intake boundary, kept outside the copied pack. Authentication and durable deduplication supply host behavior that the upstream Cursor automation environment otherwise owns.

Slack documents verification over `v0:<timestamp>:<raw body>` with an HMAC comparison and a five-minute replay check. The verifier follows that contract. See [request verification](https://docs.slack.dev/authentication/verifying-requests-from-slack/). Event callbacks expose workspace/app/event identity and can be redelivered; see [Events API delivery](https://docs.slack.dev/apis/events-api/#responding-to-events). The intake permits ordinary messages and the documented file-share subtype; see [message subtypes](https://docs.slack.dev/reference/events/message/). This fixture rejects other subtypes and non-report callbacks, including URL-verification challenges. A real receiver would need its separate challenge and HTTP handling.

The journal records an intent before an external effect and never expires or reassigns an owned claim. `NoWrite` means the adapter has authoritative evidence of no effect; a timeout is never `NoWrite`. Confirmed absent delivery triggers compensation of a known owned issue. Unknown delivery requires reconciliation first. This preserves upstream's compensation requirement without guessing that a failed response means the reply did not land. The upstream instructions are unchanged.

## Remaining gates

These tests establish behavior of the contract code and its fake adapters. They do not establish agent compliance, a working Slack trigger, actual tracker search/update semantics, Slack read-back accuracy, an HTTP acknowledgement deadline, cross-service exactly-once effects, or unattended recovery. Unknown outcomes remain blocked with evidence; this unit provides no automatic reconciliation, lease expiry or dispatcher retry. The generic `finish` method records a caller's assessed outcome and is not a substitute for the workflow's verification gates.

Before a live pilot, select the repository, test workspace/channel, tracker and model contexts. Prove fresh-provider dependency loading, authenticated intake/real envelopes, precise write and read-back semantics, durable dispatch-to-agent completion, and isolation for any child. Independent media review, unreadable attachment behavior, human ownership, marker/rejection time budgets and baseline/patched UI proof need later workflow tests. Keep normal traffic disabled. None of those gates is waived by this passing fixture suite.
