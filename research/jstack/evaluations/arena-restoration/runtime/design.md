# Final design

Propose `deliver(items, send, batch_size=2, *, on_progress=None)`. The optional synchronous callback receives one integer, the current `sent` value. Ignore its return value. Existing two-argument, three-positional-argument and existing keyword calls keep their meaning. Signature introspection will show the new parameter.

Preserve all original operations in order: materialize `items` once; select a batch; call `send(batch)`; add the post-send `len(batch)` to `sent`; advance `pending`; return `sent` when exhausted. Add reporting only after the pending update completes. Test `on_progress is not None`, then invoke it with `sent`. This identity check does not execute a callable object's truthiness method.

Guard only the callback invocation with `BaseException` suppression. A reporting failure is discarded; later completed iterations still attempt reporting. Do not log the failure, call another handler, retry delivery, or wrap any existing delivery operation in the handler. This deliberately suppresses callback-raised `SystemExit`, `KeyboardInterrupt` and `GeneratorExit`, as well as ordinary exceptions and the TypeError from a noncallable reporter. It also suppresses an ambient interrupt delivered while the callback runs; Python cannot reliably distinguish that from a callback-raised interrupt at this boundary. Send-originated exceptions, including base exceptions, retain their original propagation.

Emit no initial, final-only, empty-input or failure event. Five ordinary items with batch size two produce counts 2, 4 and 5 after their corresponding completed iterations, then return 5. Empty input returns 0 with no sends or reports. A failing second send leaves only the first report, propagates the same exception object, and prevents the third send. A bookkeeping failure after send remains visible and produces no report for that incomplete iteration.

The count means exactly what the original return value means. The sender can mutate its batch: clearing every batch makes the original return value zero. Keep post-send counting, including this behavior. Reporting receives no item, batch or pending references, only the integer. It must not reinterpret the count as confirmed remote delivery, original-item consumption, or a percentage. No total or new return object is needed.

Reporting runs synchronously and adds latency. The failure guarantee covers callbacks that return or raise. A callback that blocks forever, directly terminates the process or modifies shared state used by the sender cannot be isolated by an in-process exception handler. Require a prompt observational callback. Async callbacks are unsupported and are not awaited. Preserve existing invalid and unusual batch-size behavior, including possible nontermination; validation and batching changes are outside this proposal.

A generator would change eager execution and the return contract. Built-in printing or a progress library would impose an output destination or dependency. Background reporting would add queues, lifecycle and ordering requirements. A count plus total would require additional semantics where sender mutation already makes accounting unusual. The single callback matches the small existing loop.

For a future implementation, compare these observable cases with the pinned source:

- Existing positional and keyword calls, omitted reporting and explicit None preserve sends, results and exceptions. Verify empty input, one batch, several batches, a final short batch and a single-use iterable.
- Five items at size two produce send/report pairs with counts 2, 4 and 5. Report return values do not affect the integer result.
- A sentinel exception from the second send escapes unchanged, with no second report or third send. Repeat after a first-report failure, and with a send-raised custom BaseException.
- Reporters that raise ordinary exceptions, custom base exceptions, SystemExit or KeyboardInterrupt leave delivery traces and results equal to baseline. Later callback attempts still occur. A noncallable reporter also leaves delivery intact.
- A callable whose truthiness raises still receives reports because the design uses an identity check.
- Senders that clear or append to their batch preserve baseline post-send counts and pending progression.
- Materialization, slicing and bookkeeping failures remain outside the reporting handler. Inspect the unchanged loop for zero or negative batch sizes instead of executing an unbounded test.

Grounding: `/tmp/jstack-arena-restoration-20261015/runtime/source/batch.py`, SHA-256 `b4c7dd642a7bf991634d05dec3981d1971970458559a0cca67a0acc217fcb679`. The only proposed changes against that source are the keyword-only argument and guarded callback after pending advancement. No implementation was made. The supplied synthetic source has no callers or tests, so wider caller compatibility remains unverified.
