# Swarm restoration

This correction follows merged PR #36 at `36e489aa73c35c8e0bf84f1e0bc9a7f1298a57b5`. Swarm retains pin `11713c683fe4add4fd403ea880580abbc9e0875f`. It restores the source description, Start list, numbered Frame procedure and four Phase headings. Explicit task-local race-arm assignments now override the scalar worker default without editing saved settings.

## Source comparison

[compare.py](compare.py) compares the complete pinned Swarm source, checks the license, inventories the local execution reference and records the three shared setup-support changes against the merged base. [source-comparison.json](source-comparison.json) retains full differences and hashes. Setup's distinct primary pin remains `ccb5507cec1546dc88135c1139c811e6c59115ba`; its step 3(c) also describes per-arm model assignments. The [Swarm](../../adaptations/swarm.md) and [setup](../../adaptations/setup-jstack.md#swarm-task-local-resolution-2026-10-15) records explain every change. The parent inspected the complete source and final differences.

```sh
python3 -B research/jstack/evaluations/swarm-restoration/compare.py > /tmp/swarm-source.json
cmp research/jstack/evaluations/swarm-restoration/source-comparison.json /tmp/swarm-source.json
python3 -B skills/jstack/setup-jstack/scripts/test_models.py
python3 -B skills/jstack/juan-mode/scripts/test_preflight.py
```

The canonical resolver's new `--worker-override` flag is restricted to `swarm workers`. It validates the complete selected configuration before validating the task-local seat with the existing catalog rules. It returns one effective target while retaining the original config source identity. It never writes settings. The tests cover two concrete model identities, options, inherited override of a concrete default, invalid selections, wrong-role rejection, stale unrelated roles and unchanged saved files. Old helpers lacking the flag require manual update.

## Runtime exercise

A fresh-context evaluator received the actual Swarm skill and setup authoring path, a four-line `take()` fixture with a written contract, and an inherited synthetic configuration. The request combines one required coverage worker with a two-arm best-of race for a regression test plan. Survivor selection is explicitly permitted for the race; coverage remains independently required. One arm explicitly selects `inherit-parent` through the new override, while other workers use the saved scalar default.

The evaluator ran the three workers through live T3/native capabilities, with writes restricted to `/tmp/jstack-swarm-restoration-20261015/runtime/output`. Source, contract and config stayed read-only. No expected findings or competing results were supplied. The request forbade implementation, settings changes, installations, PRs, schedules and extra worker nesting.

Required coverage passed 20 executed contract cases. Both race arms returned valid seven-case proposals; B won under the predeclared criteria because its non-palindromic prefix and two different negative limits catch more plausible regressions at the same case count. That ranking was source/test-plan inspection, not an executed mutation experiment. The plan workers accurately disclosed that their proposed tests were unexecuted. The first coverage writer ran alone to establish path handling; the two plan workers then ran concurrently. All three finished before completion, with no dropouts, retries or unresolved coverage.

[runtime-record.json](runtime-record.json) retains exact fixture contents and all output files as named text entries, with their SHA-256 hashes. It includes full dispatch briefs, input pins, resolver commands/results, capability evidence, declared selection criteria, worker reports, test code/stdout, task states, aggregation, cleanup and final result. Full temporary catalogs and the override draft were removed. Source packages were used explicitly; this was not an installation/discovery test.

The parent read the actual reports and selection, checked all immutable inputs, verified three fresh inherited terminal workers and both canonical resolution results, and reran the inspected [coverage checker](coverage-check.py). Its [replay stdout](parent-replay.txt) exactly matches the worker's 20-case log. [Parent checks](parent-checks.json) record these results and the unchanged real model-file hash. The checker retains original temporary paths; recreate `fixtureFiles` from the runtime record under `/tmp/jstack-swarm-restoration-20261015/runtime/` before replay if those fixtures have been removed.

The actual B dispatch contained a mistyped first source hash and an explicit correction later in the same message, before worker analysis. B verified the correct pin. Both versions remain in its archived brief; this was not a missing-evidence retry or a separate correction delivery. The briefs are not claimed to be identical. This evidence establishes the bounded workflow outcome, not flawless prompt assembly or an independent host trace of every read.

## Continuation assessment

A separate fresh-context evaluator assessed nine controlled states: missing evidence and its exhausted retry, unconfirmed first-pass cancellation, best-of survivor selection, rank-all dropout, mixed coverage blocked despite a race winner, unavailable explicit model, unnamed distinct-model choices and inherited override of a concrete default. [Its report](continuation-assessment.md) records the permitted actions and source citations. It did not execute workers, cancellation or catalog validation.

The report found that the prior paragraph did not explicitly classify a BLOCKED coverage result. The final skill now states that a blocked required slice makes coverage incomplete when its done predicate remains unmet. This preserves tasks whose actual goal is to identify readiness/blockers while preventing a race winner from masking unfinished required work. The parent checked this narrow clarification directly; it was made after the tabletop report and does not turn that report into a live recovery test. Unspecified cancellation timeout/escalation and ordinary dropout retry policies remain reported limits, not permission to claim completion or invent replacement models.

## Limits

All 19 resolver tests, 15 preflight tests and 11 upstream-checker tests pass. Skill validation, Markdown lint, unchanged-manifest validation, local-link checks and exact-source comparison pass. The actual global model file retains SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`.

The runtime exercise uses inherited workers. Concrete different-model and cross-provider dispatch, live first-pass cancellation, induced missing-evidence retries/dropouts, source integration and non-default code-worktree execution remain untested here. Catalog validation and preserved target objects do not prove provider execution. Installed-provider discovery remains separate from authoring-source use. No source pins or reviewed checkpoint advance. Broader dependency/provider gates and the 23 Juan-mode playbooks remain open.
