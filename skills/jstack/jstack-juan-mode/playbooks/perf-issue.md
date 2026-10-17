### Perf issue

**You own the measurement story. Plan, review, verify the numbers.** Tie every fix to a measurement, don't read source instead of measuring.

1. Capture a baseline trace via the matching control skill. Vet the baseline, and each later number, with the **jstack-benchmark-checklist** skill. Discover the matching control helper, including `jstack-control-cli` for terminal apps, and confirm that a runtime profiler can actually capture the workload. Missing access or tools leaves the measurement incomplete and does not authorize installation.
2. `jstack-how` to ground hypotheses. Don't claim a perf ceiling without running it first. Discover the helper and pass its configured roles, source scope and selected absolute configuration through the mode's preflight.
   Try the performance mantras in order, cheapest first:
   1. Don't do it. Stop work whose result nothing uses rather than cheapening it.
   2. Do it, but don't do it again.
   3. Do it less.
   4. Do it later.
   5. Do it when they're not looking.
   6. Do it concurrently.
   7. Do it cheaper.

   When an earlier mantra meets the target, stop.
3. Plan the fix from the trace. If it crosses a function boundary, `jstack-architect` first, returning a design before implementation. Preserve its configured panel and two structurally distinct candidate requirement; an undersized panel or unavailable helper leaves this step incomplete, without adding seats. Delegate implementation to a subagent using the configured `perf-issue` role, or `hardest tasks` when warranted by the mode's difficulty rule. Resolve through the mode's preflight and retain the selected absolute configuration; no fixed-model fallback. Review the diff. Capture a post-fix trace.
   Apply the **jstack-principle-sequence-verifiable-units** principle skill, verifying each attempt before trying the next.
4. Parse and compare the artifacts (JSON to sqlite, diff). "Inconclusive" or wrong-surface is not a pass. Flag it. Inspect the delegated diff and repeat the public workload yourself; retain outputs, error/work counts and comparable measurements. Keep profiling runs separate from reported timings, as the checklist requires.
5. Cite the measurement in the PR when publication is authorized; for local-only delivery, retain it in the local report.
6. Run **Opening a PR** when publication is authorized. That procedure remains unavailable in this package; disclose the gap rather than claiming it ran. Preserve unrelated work and existing publication authority. This playbook does not authorize merging or installation.

For sustained improvement against a metric rather than a one-off fix, use the Hillclimb playbook (`playbooks/hillclimb.md`). That procedure remains unavailable; disclose the missing dependency rather than inventing its steps.

**Reply:** baseline number, post-fix number, delta, artifact path.
