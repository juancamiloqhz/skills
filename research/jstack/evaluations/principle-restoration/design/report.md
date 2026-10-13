# Job tracker forward exercise

Read the five requested restored principle skills from the working tree. This is an independent application exercise, not a source-fidelity comparison or a test of automatic juan-mode routing.

## Concrete design

`tracker.rs` is a Rust library with a public interface used by the separately compiled `checks.rs` client. There are no third-party dependencies.

- Replace optional completion fields with `Status::Open | Status::Done { at: Timestamp }`. Completion labels derive from this state. The legacy input adapter rejects contradictory combinations instead of guessing which old field wins.
- `UserId` and `OrderId` are distinct newtypes with private payloads. Their constructors parse external strings once. They cannot be interchanged in `Job::new`.
- Domain ownership stays in `Job` and `Tracker`, rather than phase-named load/validate/save modules. This small demonstration has no completion command; it parses both legacy lifecycle states.
- `sum` accepts an ordinary slice and returns zero for an empty slice. `head` takes the constructed `NonEmpty { first, rest }` type. Callers cannot pass an empty array to it.
- Indexer and metrics workers own separate JSON files. A read-only reporting function combines their contents. Each writer uses its own temporary file and rename, avoiding partial content on the same filesystem. The report is not a transactionally consistent snapshot of both workers; these are independent facts.
- Input parsing does not freeze authorization. `Tracker::execute` consults the current permission set after any revocation, with exclusive access across check and insertion. In a real remote permission service this must be replaced by an atomic authoritative authorization/commit operation or suitable versioned transaction; an earlier remote check followed by an unrelated write is insufficient.

## Actual verification

Command: `bash /tmp/jstack-principle-restoration-design/run.sh`

Tool: `rustc 1.98.0 (88d9e12ae 2026-08-18)`. `tsc` was not found on PATH. Rust was available, so no compiler installation or TypeScript-specific helper was needed. The catalog does not advertise `typescript-best-practices`; no claim is made that it was consulted or that TypeScript-specific coverage is complete.

Five runtime tests passed:

1. Reject contradictory legacy states, invalid timestamp and mismatched ID prefix; expose literal `open` and `done` labels for valid records.
2. Sum empty input as 0 and `[3,4,-2]` as 5; head of `[7,9,11]` as 7.
3. Search an absent title and obtain an empty result, paired with an exact positive search result `['alpha']`. This avoids a vacuous absence-only test.
4. Parse a job, revoke its owner's permission, and receive exactly `permission denied` with no insertion. Regrant and receive a successful insertion with exactly `['alpha']` visible through the public jobs interface.
5. Execute indexer and metrics concurrently for 1,000 and 700 writes; public reporting returns exactly `{"indexer":{"indexed":1000},"metrics":{"processed":700}}`.

Four negative compilation fixtures were rejected with expected diagnostic classes:

- `invalid_ids.rs`: E0308, swapped user/order types.
- `invalid_done.rs`: E0063, completed state lacks timestamp.
- `invalid_head.rs`: E0308, empty ordinary array supplied to non-empty head.
- `invalid_match.rs`: E0004, unhandled completion variant.

Expected results are literal independently chosen inputs/outputs, not calculated by the subject under test. Tests operate through exported functions and types. Compiler failures are checked for the intended diagnostic class, not merely a nonzero exit status.

## Artifacts and limits

All artifacts are under `/tmp/jstack-principle-restoration-design`: `tracker.rs`, `checks.rs`, four `invalid_*.rs` sources and their diagnostic logs, `run.sh`, `results.log`, compiled library/test binary, and `state/indexer.json` plus `state/metrics.json`.

No repository edits, network access, installation, configuration changes, delegation or commits were performed.

This is a bounded demonstration. The filesystem exercise tests independent threads in one process and final visible content, not process crashes, fsync durability, readers during updates, hostile filesystem access or multiple instances of the same worker. The fixture constructs one publisher per role; the public `publishers` factory does not enforce system-wide singleton ownership. Production supervision must ensure one writer per role, or assign per-instance artifacts. The sample integer sum does not specify overflow handling; the demonstrated values are bounded. Timestamp validation is an unsigned epoch count, not calendar/time-zone validation. This does not validate installed skill discovery, routing, persistence, model delegation, TypeScript compilation, broader migrations, or every possible application of the five principles.
