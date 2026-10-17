# Hillclimb evaluation

This evaluates the new [Juan-mode procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/hillclimb.md) on a synthetic event-summary CLI. It does not establish production performance or full provider support. The [adaptation record](../../adaptations/hillclimb.md) accounts for every difference from the pinned source; [source-comparison.json](source-comparison.json) records the comparison and caller changes.

## Request and method

An independent agent received the in-development skills and this task: reduce median end-to-end time for 80,000 events by at least 30%, perform at least three measured implementation attempts, stop at a hard maximum of three attempts, preserve behavior and make local commits only for accepted changes. It did not receive the intended fix or earlier Perf issue results.

The fixture reuses the checked-in [Perf issue baseline](../perf-issue/baseline/), [generator](../perf-issue/generate.py) and [eight public behavior tests](../perf-issue/app/summary.test.cjs). The generator independently computes expected totals for 80,000 events, with 74,171 accepted and 5,829 rejected. Tests cover empty inputs, iteration ordering, invalid rules, independent calls and non-string coercion. An unrelated untracked note tests preservation of other work.

The agent first ran How and a separate CPU profile, checked small-versus-large workload sensitivity, vetted the benchmark and froze it. Every comparison alternates seven fresh Node processes per side. Timing includes startup, file reads, parsing, summarization, serialization and captured stdout. Full output comparison follows timing. The benchmark reports errors and processed work; a performance win requires a green regression gate and nonoverlapping timing ranges. This conservative rule can reject small real gains. No profiler runs during measurements, and the parent avoids competing application work.

The run uses Node v24.19.0 on Linux with four available cores. A private medium setup template assigns inherited roles and two comparison seats. Preflight selects `codex/gpt-6-astra`; native calls omit model and effort overrides. Native child identities are not independently attested, and the run does not establish different-model or different-family review. The user's saved configuration is unchanged.

## Results

The agent completed three measured attempts, kept one change and fully reverted two. The first attempt exceeded the target, but the agent continued until the attempt floor was satisfied. It then stopped at the explicit cap.

| Attempt | Before median | Candidate median | Decision |
| --- | ---: | ---: | --- |
| Parse primitive string rules once, lazily | 2,378.26 ms | 149.42 ms | Kept; ranges separated and tests passed |
| Hoist the string eligibility check | 159.59 ms | 146.64 ms | Reverted; ranges overlapped |
| Check the cache before string eligibility | 137.78 ms | 146.65 ms | Reverted; slower median and overlapping ranges |

Sensitivity separated 80 events at 63.59 ms from 80,000 events at 2,496.64 ms. Final fresh paired medians were 2,384.95 ms versus 144.61 ms, a 93.94% reduction. Every attempt and the final confirmation reported zero errors and 1,120,000 processed events across 14 runs. The retained change avoids repeated parsing of immutable string rules while preserving lazy iteration and non-string coercion.

The parent's independent run measured 2,457.27 ms versus 138.59 ms, a 94.36% reduction with nonoverlapping ranges. All 125 API comparisons matched, all eight tests passed, the CLI caller stayed unchanged and the fast incorrect implementation failed the correctness gate. Parent inspection also verified the 42 attempt samples' input/source hashes, unchanged frozen benchmark, both full rollbacks, exactly one scoped commit and the preserved untracked note.

The packaged replay passed from a fresh scratch directory. It again classified only the first candidate as beyond noise. Identical source ranges overlapped. The deliberately incorrect candidate looked faster but produced seven rejected samples, confirming that a favorable timing flag alone cannot justify acceptance.

See [results.json](results.json) for individual timings, attempt patches, source identifiers and compact verification results. Each patch is necessary to replay the actual measured candidate, including rejected candidates. The original frozen benchmark hash and the portable replay hash are recorded separately.

The independent trail reviewer found no unsupported accepted win, missing rollback or application failure. It reviewed a labeled digest and actual artifacts, not a complete transcript. The workflow result remains qualified: the initial summarized plan was corrected before measurement; early reads and some child operations lacked raw capture; one comment reviewer violated its exact-opening rule. An append-only audit row clarified two differently based percentage comparisons. The reviewer's initial historical-source hash lookup used the current app by mistake, then passed after selecting the retained baseline. These findings did not change acceptance or rollback decisions.

Packaging tests passed 4/4, all three affected packages passed quick validation, the manifest loaded, and Markdown, relative links and whitespace checks passed. Five complete pinned-source comparisons confirmed the new procedure and narrowly scoped caller changes.

## Reproduce

From the repository root, with Python 3, Node and Git available:

```bash
python3 research/jstack/evaluations/hillclimb/reproduce.py /tmp/jstack-hillclimb-replay
```

Choose a new directory outside the repository. The script refuses an existing destination. It generates data, checks sensitivity, applies the three recorded candidate patches to their historical bases, runs each candidate's tests and measurements, then independently checks the retained result with the existing [parent verifier](../perf-issue/parent-verify.py). That verifier compares 125 API cases, the full CLI output and eight tests, and rejects a fast but incorrect implementation. Replay also measures identical sources and sends incorrect output through the frozen benchmark's error gate.

Replay preserves historical acceptance decisions when selecting the next base. New timing arrays and noise classifications may differ across runs. It does not recreate agent judgment, dispatch, local commit history or the original transcript. It tests the actual candidate code and measurement gates. The parent verifier requires the retained result to clear 30% with nonoverlapping ranges on the replay host.

[benchmark.py](benchmark.py) preserves the evaluator's measurement logic. Packaging replaces its fixed scratch path with the script's directory so it can run elsewhere. That path-only edit produces a new hash; it did not change the original frozen run. All replay outputs go to the chosen scratch directory.

## Limits and retention

The exercise covers a serial CPU-bound CLI. It does not cover parallel worktree hypotheses, a correctness-failing implementation attempt, step 6's simplification exception, an exhausted search with an unmet predicate, unattended wakes, PR publication, installed-provider discovery or persistence. The separate incorrect-output control tests the measurement gate, not an agent's response to a broken attempt. Opening a PR and Autonomous run remain unavailable.

This directory retains five artifacts: this report, compact results with patches and timing arrays, the portable benchmark, the replay script and the source comparison. Existing fixture files are reused. Raw command logs, agent reports, catalogs, generated datasets, profiles, source snapshots and the runtime decision trail stay in task-owned scratch. The report preserves relevant findings and limitations without requiring those temporary paths as durable evidence. See the [retention policy](../../upstream-fidelity.md#evaluation-evidence-retention).
