# Perf issue evaluation

The ninth Juan-mode procedure preserves upstream's six steps. The [adaptation record](../../adaptations/perf-issue.md) explains the runtime differences, and [source-comparison.json](source-comparison.json) records complete pinned comparisons. Source pins and the reviewed checkpoint are unchanged.

## Results and limits

The parent replay measured a **94.46% reduction in median end-to-end time** on the synthetic 80,000-event CLI batch. Seven alternating runs per version gave 2,471.07 ms before and 136.83 ms after. Ranges were 2,359.88 to 2,545.31 ms before and 130.84 to 159.68 ms after. All counts and category totals matched, with no errors. A separate workflow run measured 93.87% across five alternating pairs. [results.json](results.json) retains individual timings, environment, correctness outcomes and input hashes without repeated output bodies.

Both timers include fresh Node startup, file reads, parsing, summarization, consumed stdout and process termination. Profiles run separately. The baseline profile attributes 94.65% of sampled self time to `summarize`. A diagnostic probe records 80,000 identical rules parses before the fix and one afterward. The candidate parses a primitive string once per call after iteration yields an event. Non-string coercion stays per event.

Eight tests and 125 additional parent API comparisons pass. A fast candidate with incorrect totals fails the output check. The CLI caller is unchanged. Independent code review found no defects; the decision-log audit supported the ten reviewed decisions. One candidate met the requested 30% target, so optimization stopped.

These results cover one synthetic batch on Node v24.19.0 and one shared host. They do not prove production performance or compatibility with arbitrary built-in replacement and prototype mutation. Browser profiling, missing-profiler recovery, noise-sized differences, cross-function Architect composition, provider persistence and publication remain untested. Hillclimb and Opening a PR remain unavailable.

The independent evaluator received the user-style request and raw inputs without the intended fix. Its five descendants completed. It used an isolated medium setup template with inherited roles; the two comparison seats were unused. Saved settings were unchanged. Separate contexts and containing-thread identity do not establish model diversity or independently attest each child runtime.

Full workflow conformance remains qualified. Early read-only commands lack complete contemporaneous records, and the later host-plan snapshot does not establish initial timing. The audit used a bounded digest. An implementation bootstrap attempted unavailable `python` before `python3`. Required skill-creator guidance arrived after initial briefs. A reviewer read three installed principle files; byte comparisons confirmed repository-equivalent content, but the path deviation remains recorded. Removing verbose logs does not erase these failures or turn this into a full-mode certification.

## Reproduce the checks

From the repository root, copy the fixture to fresh scratch space. Generated data, command output and SQL stay there.

```bash
perf_replay_dir=$(mktemp -d /tmp/jstack-perf-replay.XXXXXX)
cp -R research/jstack/evaluations/perf-issue/. "$perf_replay_dir/"
cd "$perf_replay_dir"
python3 generate.py
python3 parent-verify.py
python3 parent-profiles.py
node parse_probe.cjs "$perf_replay_dir/baseline/summary.cjs" events.json rules.json
node parse_probe.cjs "$perf_replay_dir/app/summary.cjs" events.json rules.json
```

The verifier runs the eight tests, compares 125 API cases, rejects incorrect fast output and repeats seven alternating CLI pairs. The retention cleanup passed this full fresh-copy replay, including the parse probes, Markdown checks and retained-source hash checks. Original recorded timings remain unchanged in results.json. New timings describe the new environment. The profile parser queries the original captures through SQLite; its sampled durations are attribution evidence, not acceptance timings.

## Why these files remain

The 14 retained files follow the [evidence-retention policy](../../upstream-fidelity.md#evaluation-evidence-retention): this report, compact results, the source comparison, five fixture files, four reproduction scripts and two original CPU profiles. The profiles supply primary evidence for the measured hotspot. Generated datasets, SQL dumps, command transcripts, agent reports, duplicate snapshots, capability catalogs and archive indexes are omitted.

The original run's scratch files remain at `/tmp/jstack-perf-issue-20261016` until local cleanup. They are temporary debugging material, not required repository inputs or a permanent evidence link. Retention cleanup does not change the playbook or its measured result.
