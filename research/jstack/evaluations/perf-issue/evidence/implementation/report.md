The CLI and CommonJS callers keep the same inputs and outputs. The candidate reuses parsed primitive string rules within each summarize call. Parsing starts only after iteration yields an event. Non-string inputs still pass through JSON.parse on every event, preserving observable coercion.

Only app/summary.cjs and app/summary.test.cjs changed. The production edit stays inside summarize. Category lookup, traversal order, arithmetic, counters, return shape and exports remain unchanged. There are no new dependencies, helpers or narrative comments.

Model the Domain kept the existing per-call rules lookup and category totals. Sequence Work into Verifiable Units required the original three tests to pass before the single candidate edit, followed by all eight tests and CLI output verification. Test Behavior, Not Implementation led to public calls with literal results and public error assertions. Added coverage includes empty iterables with nonzero length, nonempty iterables with zero length, iteration errors before parsing, changed rules between calls, and changing or failing non-string coercion.

Verification passed. implementation-baseline-tests.json records 3/3 original tests. implementation-tests.json records 8/8 tests after the change. implementation-cli.json records the supplied 80,000-event CLI execution with exit code 0 and empty stderr. implementation-verify-cli.json verifies every output value against expected.json, the single newline-terminated JSON line, and unchanged CLI source. change.diff contains the exact diff against the saved baseline.

No speedup claim is made here. The parent owns alternating end-to-end measurements, final profiling, code review, comment review and trail review. Test and CLI validation ran concurrently, so their recorded durations are not acceptance measurements. The bounded candidate stops here.

The tests cover the supplied workload and the named public compatibility cases. They do not establish equivalence under arbitrary global JSON.parse replacement or adversarial prototype mutation. No jstack files changed, so this implementation introduces no upstream adaptation or deviation. The upstream-fidelity policy was read. No commit, publication, configuration change or descendant task occurred.

identity.json records the inherited codex gpt-6-astra selection from the parent brief and preflight record. There is no independent model attestation or diversity claim. The initial python launcher failed because only python3 was available; bootstrap-commands.json retains that failure.
