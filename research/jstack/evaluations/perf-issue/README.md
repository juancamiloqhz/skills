# Perf issue evaluation

The ninth Juan-mode procedure preserves the pinned six-step Perf issue workflow. See the [adaptation record](../../adaptations/perf-issue.md) and [complete source comparisons](source-comparison.json). Mode, setup, benchmark-checklist and both forensic handoffs now agree on availability. The manifest, source pins and reviewed checkpoint are unchanged.

## Measured result

On this synthetic 80,000-event batch CLI, the independent parent replay measured a **94.46% reduction in median end-to-end time**. Seven alternating runs per version gave 2,471.07 ms before and 136.83 ms after. Baseline range was 2,359.88–2,545.31 ms. Candidate range was 130.84–159.68 ms. Every run returned the exact expected counts and category totals, with no errors. [Raw parent verification](parent-evidence/verification.json) records the environment, commands, outputs and timings.

The evaluator independently measured five alternating runs per version, with a 93.87% reduction. Its [raw comparison](evidence/benchmark/summary.json) remains separate. Both timers include a fresh Node process, file reads, parsing, summarization, consumed stdout and process termination. Profilers run separately. Node v24.19.0, identical data and flags, and four logical CPUs describe this host. No production tuning or concurrent-service claim follows.

The baseline CPU profile attributes 94.65% of sampled self time to `summarize`. A separate instrumented probe observes 80,000 parses of the same rules document. The fixed version parses a primitive string once per call, after iteration yields an event. Non-string coercion remains per event. The parent independently normalized both profiles into [SQLite rows](parent-evidence/profiles.sql) and retained the [weighted query results](parent-evidence/profiles.json). Those sampled durations support attribution, not the speedup number.

The public CLI caller is unchanged. Eight tests pass, including empty iteration, iteration errors, changing rules between calls and observable non-string coercion. The parent compares 125 additional API cases with the original and rejects a fast negative control that returns incorrect totals. The single candidate meets the requested 30% reduction, so later optimization mantras are not attempted.

## Evaluation boundary

The [evaluator report](evidence/report.md), [structured assessment](evidence/assessment.json), [code review](evidence/code-review/report.md) and [decision-log audit](evidence/trail-review/report.md) retain the completed run and its qualifications. All five descendants are terminal.

An independent agent received a user-style request and raw inputs without the intended fix. It read the in-development mode and delegated grounding, implementation and reviews. The explicit scratch configuration is setup's unchanged medium template with inherited roles and two comparison seats. No comparison panel was needed because the selected edit stays inside one function. The saved global configuration is unchanged. Separate inherited contexts do not establish model-family diversity. The containing thread selection and preflights do not independently attest each native child runtime.

The run retains limitations rather than claiming full-mode certification. The first two read-only discovery calls were not persisted as contemporaneous command files. Later read records also differ in captured metadata. The saved host-plan snapshot does not establish when the initial plan was opened, and the audit uses a bounded digest rather than a complete transcript. An implementation bootstrap attempted unavailable `python` before using `python3`. The parent clarified access to the external host skill-creator after initial agent briefs had been written. Original failures and timing qualifications remain in the evidence. The code reviewer read three installed principle leaves. Both parent and evaluator confirmed they are byte-identical to the repository versions, so this is a recorded path-selection deviation rather than content drift.

The case does not establish compatibility with arbitrary replacement of global `JSON.parse` or adversarial prototype mutation. Browser profiling, missing-profiler recovery, noise-sized gaps, cross-function Architect composition, provider persistence, Hillclimb and publication are untested. Opening a PR and Hillclimb remain unavailable procedures. The evaluator's delivery is local, with no commits, configuration changes or installations.

## Retained evidence

[Archive index](archive-index.json) records source hashes and normalization. Full live provider catalogs and large repeated source-read outputs are indexed rather than duplicated. Raw profiles, benchmark runs, errors, decisions and role resolutions are retained. The generated events file is reproducible with [generate.py](generate.py). Scratch originals remain at `/tmp/jstack-perf-issue-20261016`.

To repeat the parent checks, copy this directory to fresh scratch space, run `python3 generate.py`, then `python3 parent-verify.py` and `python3 parent-profiles.py`. The verification script regenerates its negative control and API cases. New timings describe that run's environment. The [validation record](validation.json) covers package structure, source mappings and authored documentation. Raw evaluator reports are preserved without style rewrites.
