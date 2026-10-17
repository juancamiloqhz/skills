# Multi-phase plan evaluation

The planning procedure now supplies pstack's complete template and structural checker, with native T3 scheduling and worktree instructions. Plans preserve ten live lanes per PR and separate unit, live, performance and operator-review evidence. A valid document is not proof that its execution workflow exists or its boxes have been completed.

Source: `11713c683fe4add4fd403ea880580abbc9e0875f`. Base: merged Shipping, `7ae0996d4aa7da6fc3f693b50d8b68feda2f57f9`. See the [adaptation](../../adaptations/multi-phase-plan.md) and [source comparison](source-comparison.json).

## Checker execution

On 2026-10-17, Linux x64, Node v24.19.0 and Python 3.14.4, the [exercise](exercise.py) ran the actual packaged checker on generated temporary documents. It passed one-PR and two-PR structures, a no-interaction review gate with no boxes and the usage-error exit. Sixteen malformed cases were rejected with their expected diagnostics. These cover title/read-guide/program omissions, program order, scheduler and cadence, file block, verification rule, missing model, duplicate lane, missing screenshot, missing pass predicate, performance baseline field, contradictory review gate, missing video and prototype appendix.

```sh
python3 -B research/jstack/evaluations/multi-phase-plan/exercise.py
node --check skills/jstack/jstack-juan-mode/scripts/check-plan.mjs
```

The fixture extracts the packaged template and generates its inputs in a temporary directory. Its filled values are syntax-test data, not a real executable project plan. It removes generated documents on exit. The original checker accepts the source `/loop 1h` form, while the local checker rejects it without the native marker. The native form passes locally. Source comparison confirms that only the scheduling-marker line changes in the checker; its parser and other rules are unchanged.

Generic unresolved placeholders still pass. The checker does not prove valid dependency topology, meaningful predicates, actual screenshots, available models, runtime feasibility or completed evidence. It also does not enforce every semantic requirement in the playbook, such as a genuine trunk regression scenario or numeric failure budget. The port preserves those source limits and explicitly requires content review instead of treating exit zero as execution approval.

## Plan-authoring exercise

The [task and criteria](cases.json) ask for two dependent PRs adding optional JSON checker output and a CI consumer. The operator retains landing authority and requires interaction review. The request is hypothetical; this PR does not implement JSON output or add CI.

The exercise permits local reading and plan validation but excludes prototype work, delegated discovery, implementation, live/performance lanes, publication and scheduling. Those excluded stages remain untested. The source's ten lanes are plan obligations, not ten workers launched during authoring.

Two fresh Codex children used the configured `feature, refactoring` target, `gpt-6.1-sol` at high effort. One read the procedure and writing helpers. The baseline received the same task and checker, without the playbook. The effective future `swarm workers` target is `codex / gpt-6.1-sol / medium`; no role configuration changes are made.

Both final plans passed the actual checker with `2 PR sections, 0 problems`; each retained twenty live boxes and no checked evidence. Parent content review assessed five criteria. The playbook-guided plan satisfied all five, while the clean baseline satisfied two.

| Criterion | With playbook | Baseline |
| --- | --- | --- |
| Two-PR structure and checker | Passed | Passed |
| Ten lanes plus trunk regression per PR | Explicit regression lanes and per-lane proof | Ten lanes, but no explicit trunk regression lane |
| Dual-sided performance proof | Interleaved trunk/head probes, numeric failure budgets, absolute added-work budgets and unmeasured baselines | No concrete failure numbers; P2 lacks the required paired trunk/head probe |
| Dependencies, operator gates, unavailable execution | P2 depends on P1; both gated; absent Autopilot-stack blocks execution | Dependency and gates present, absent execution procedure not identified |
| Planning boundary and small-change stop | No execution claims; omitted discovery/prototype stages disclosed; typo case skips a plan | Same boundary and skip |

These are one plan per condition, not a reliability or performance estimate. The baseline could read the checker, which explains shared structural success. The with-playbook artifact still uses a shortened author-role display label; execution must resolve the actual configured role key. No generated plan was executed or promoted to a ready program.

The first baseline read the combined task/rubric JSON, contrary to its brief. It was stopped and excluded; a fresh baseline read a task-only file. The with-playbook run corrected an unavailable `python` alias by using `python3`, and fixed an internal generation assertion before writing. The first written plan passed validation. No generation error changed repository files. Raw plans, answers, grading and the static viewer remain in scratch. Timing and token usage were unavailable and are not estimated.

Four packaging tests, both skill validators, JavaScript syntax, changed Markdown lint, relative links and `git diff --check` passed. Header order, all seven procedure steps and all ten template lanes match the pinned source structure. Model configuration, source mappings, pins and reviewed checkpoint are unchanged.

## Review and remaining limits

Configured Comment Sicko, Claude Opus 5.5 at high effort, inspected private copies of the copied checker and new Python fixture. It found no comments or suppressions to delete, preserved the checker shebang and returned an empty diff. Parent inspection accepted the result. Deslop found no additional scoped code changes.

Both Autopilots and Orchestrate remain unavailable. Plans must name the intended procedure and block execution until it exists. This evaluation does not prove a full prototype-to-plan workflow, ten-lane execution, terminal screenshots/video, multi-PR execution, timer deduplication or scheduled audit recovery. No schedule, owner task, fixture PR or execution workflow was started.

Retain only this report, the small generator/test, task prompt and required source comparison. Generated plans, raw agent answers, grading, viewer, catalogs and review copies stay in `/tmp/jstack-plan-20261017` while review is pending. After acceptance, remove task-owned scratch only when no task needs it. Do not remove shared caches or unrelated work. The installed skills, saved model configuration and upstream reviewed checkpoint remain unchanged.
