# Autonomous run evaluation

The procedure preserves pstack's six-step loop: define a fixed exit condition, select a supported wake, verify each attempt, address related discoveries, checkpoint decisions and stop at the original condition. This evaluation proves a finite local CLI repair and honest handling of an unmet prerequisite. It does not prove a complete unattended workflow.

Base: `f0c660c97b8e9bcdd6a5ac58dd1e23f37edc937e`. Procedure and mode source: `11713c683fe4add4fd403ea880580abbc9e0875f`; setup source: `ccb5507cec1546dc88135c1139c811e6c59115ba`. See the [adaptation](../../adaptations/autonomous-run.md) and [final source comparison](source-comparison.json). Pins, mappings and reviewed checkpoint remain unchanged.

## Reproduce

From the repository root, choose a fresh scratch path:

```sh
python3 -B research/jstack/evaluations/autonomous-run/fixture.py /tmp/jstack-autonomous-example
python3 -B /tmp/jstack-autonomous-example/checker.py /tmp/jstack-autonomous-example/repo/app.py
python3 -B /tmp/jstack-autonomous-example/blocked_checker.py
```

The generator creates a Git repository and immutable-by-task checkers outside it. `baseline.json` records the original multiplier bug (3/5 checks pass). The supplied uncommitted formatter attempt regresses that to 1/5. An unrelated user file is staged and another is untracked. `before.json` records protected hashes and staging. Both checkers exit successfully even when their JSON says `complete=false`.

Give a fresh agent the task in [cases.json](cases.json), the fixture path and a separate output directory. Permit only the specified local changes and commit. For the with-playbook run, supply [Autonomous run](../../../../skills/jstack/jstack-juan-mode/playbooks/autonomous-run.md) and its trail dependency. For the baseline, do not provide jstack instructions. Withhold the generator, assertions and other run's results. Inspect the evidence and actual Git state against all six assertions; do not grade the agent's completion claim alone.

## Observed results

Two fresh native agents ran on Ubuntu with Python 3 and Git, inheriting Codex `gpt-6-astra` at high effort. Skill-creator supplied the paired evaluation; no saved jstack role was selected or changed. Juan-mode remained inactive. One run per condition is a behavioral check, not a reliable estimate of model performance.

| Check | With playbook | Without playbook |
| --- | --- | --- |
| Existing formatter attempt | 1/5, rejected | 1/5, rejected |
| Reverted attempt | 3/5, exact baseline restored | 3/5, exact baseline restored |
| Mode-dependent multiplier fix | 5/5, current artifact verified | 5/5, current artifact verified |
| Unrelated bytes, staging and verifiers | Preserved | Preserved |
| Local advancing commit | One, only `app.py` | One, only `app.py` |
| Separate prerequisite checker | Incomplete; resume note retained | Incomplete; resume note retained |
| Bounded task assertions | 6/6 | 6/6 |

The parent reran both final checkers, compared their artifact hashes with current files, checked all protected hashes and staged blobs, verified exactly one app-only commit per run, and resolved every trail evidence path. Both implementations selected multiplier 3 for triple and 2 for double while preserving integer parsing and formatting. The checks cover positive, negative and zero triple values, double behavior and fractional-input rejection. They are not exhaustive.

The with-playbook agent used the existing trail writer and completed its coordinator audit. It recovered from a missing `python` alias (exit 127) by using `python3`. An initial `rg` no-match exit skipped a chained read; a later explicit read recovered it. The baseline reported no command failure. Both preserved rejected-attempt evidence. Aggregation and a static review viewer were generated in scratch; unmeasured timing, token and tool-call fields were omitted. Both scored equally, so this pair demonstrates no advantage from the playbook.

## Limits and retained evidence

The external-prerequisite case is a local checker returning `complete=false`, not a real service outage. Missing-wake and completed-with-pending-children handling were explanation-only cases. Capability inspection confirmed T3's task, watch and schedule contracts; no live PR wake, recurring schedule, native goal, restart recovery or indefinite continuation was tested. The final procedure's authorized fixed/fallback cadence wording was source-reviewed, not exercised.

Nested agents were prohibited in both fixtures. The required independent trail review therefore remained pending and was disclosed. The with-playbook coordinator audit does not replace it. Code completion and the six bounded assertions pass; full workflow completion remains unverified. No publication, merge, installation, model change or external service action occurred in either fixture.

Packaging tests, mode/setup metadata validation, changed Markdown links and lint, and `git diff --check` passed. The bundle contains 20 playbook procedures; Autopilot-full, Autopilot-stack and Orchestrate remain pending. The final comparison covers Autonomous run, Hillclimb's availability update, mode and setup; prior adaptation records explain unchanged differences in those callers.

Retain only this report, the fixture generator, case specification and source comparison in Git. Generated repositories, raw results, agent reports, trails, capability data, grading and the viewer remain in task-owned scratch while review needs them. They can be removed after acceptance when no active task depends on them. Do not remove shared caches or unrelated work.
