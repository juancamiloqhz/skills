# Upstream batch 1, 2026-11-20

This batch implements the first group from the [2026-11-01 review](../../upstream-reviews/2026-11-01.md#suggested-implementation-order): the measurement step, goal-scoped autonomous discoveries, the shorter principle texts, technical writing, Sharpen and the benchmark-checklist pointer. The user approved this batch on 2026-11-20. It removes no shipped capability and changes no model role.

## Source comparison

Source is `cursor/plugins` at `aaeb0ea3a0584995aa8f55ce44c6c5259414b896`. Local base is `357c713`, merged PR #147. The decisions are `2026-11-20-measurement`, `2026-11-20-principles-trim`, `2026-11-20-technical-writing`, `2026-11-20-sharpen`, `2026-11-20-benchmark-pointer` and `2026-11-01-autonomous-goal`.

[`port_batch.py`](port_batch.py) builds the 20 changed files from the source Git objects and applies only the recorded adaptations. Every substitution must match once, so a moved source sentence fails instead of being skipped. Rerun it to check fidelity:

```sh
python3 -B research/jstack/evaluations/upstream-batch-2026-11-20/port_batch.py . --check
```

| Files | Source change | Local adaptation |
| --- | --- | --- |
| 14 principle leaves | Shorter bodies. Some rules and examples are removed, although the upstream commit says each rule and test is kept. Explain the Number adds "write the decision before you run" and the broader "Apply before you measure" description. | `jstack-` names, no invocation flag, the authority paragraph, and the helper paragraph only in Explain the Number and Type System Discipline. The Boundary, Idempotent and Sequence exceptions are reapplied. See the [principle record](../../principle-adaptations.md). |
| Juan-mode `SKILL.md` | Its Explain the Number summary line matches the new description. | None. The rest of Juan-mode is unchanged; the other mode changes belong to later batches. |
| Autonomous run | Step 4 limits owned discoveries to those that support the goal. | Existing authority and separate-PR rules are unchanged. See the [record](../../adaptations/autonomous-run.md). |
| Technical writing | Shorter four-layer standard; the compass, several style rules and the worked example are removed. | Scope paragraph, external Unslop discovery, tab exception. See the [record](../../adaptations/technical-writing.md). |
| Sharpen, its Codex prompt and the root catalog line | The rewritten prompt asks the agent to prototype choices an experiment can settle and recommend from the result. Preference choices stay with the user. | Name and slash command only. See the [record](../../adaptations/sharpen.md). |
| Benchmark checklist | The Opening a PR pointer is removed. | The stale "Opening a PR remains unavailable" sentence is removed too. See the [record](../../adaptations/benchmark-checklist.md). |

The manifest drops 15 `contextPaths` entries for cross-links that the new texts removed: four for Attack the Premise, three for Build the Lever, two each for Sequence and Type System Discipline, and one each for Explain the Number, Minimize Reader Load, Prove It Works and the benchmark checklist. The original `adaptedFrom` pins stay unchanged.

## Evaluation procedure

[`cases.json`](cases.json) holds ten requests with their expectations. The direct run gives each request with its named local skill. The selection run gives the six principle requests without the skill name or expectations, together with Juan-mode's `## Principles` section and a catalog of skill paths, so the agent chooses the leaves itself.

Each run used one fresh native Claude agent on the inherited model, with no parent history. The agents could read skills and write only their own report under task-owned cache. They had no network, implementation, installation, Git or nested delegation, and were told not to read research or evaluation files. The parent compared each answer with the expectations. Repository status was unchanged after both runs.

## Observed results

All ten direct answers and all six selection answers meet both recorded expectations, with the one partial result noted below. In every selection case the agent chose the intended leaf.

| Case | Direct use | Selection |
| --- | --- | --- |
| `measurement-clear` | Wrote the ship decision and an A/A noise floor before any run, then planned the limiter, run count and range through the benchmark checklist. | Same, and asked the user for the ship threshold. |
| `measurement-noisy` | Spread of 14 ms against a 2.5 ms gap, so "no measurable difference" and no announcement. | Same verdict, with the missing limiter and error checks named. |
| `boundary-revocation` | No repeated shape check. Fresh authorization and state checks at execution, with a conditional delete. | Same. Also read Make Operations Idempotent. |
| `idempotent-pid` | Kernel-held lock, or boot ID, PID and start time instead of PID alone. | Same. |
| `sequence-red-test` | Strict expected-failure commit, or a red run kept as PR evidence with squash. The merge is left to the user. | Strict expected-failure marker plus a linked red run. Also read Test Behavior and Never Block on the Human. |
| `premise-two-fixes` | Wrote the stale-cache premise down and tested it by bypass, logging and failure distribution before any third fix. | Same. Also read Fix Root Causes. |
| `sharpen-choices` | Returned only a rewritten prompt. It asks for Redis and in-process LRU prototypes with a recommendation, and leaves 30-second staleness to the user with data. | Not in the selection run. |
| `tw-doc-revision` | Commands with real names, with the filler and banned forms removed. **Partial:** the pnpm rationale became one sentence before the steps, not a separate explanation. | Not in the selection run. |
| `tw-pr-body` | One primary number with run count, range and limiter. Both logs are linked, and missing facts are not invented. | Not in the selection run. |
| `autonomous-goal` | Fixed the billing fixture with an injected clock and repeat runs. Recorded the marketing link without changing it and published nothing. | Not in the selection run. |

The writing agent found two Unslop copies. It compared the installed copy with a pstack copy in a local Cursor plugin cache and used the pstack copy, as the discovery rule requires when copies differ. This shows the rule being followed. It does not show that the installed copy is current.

These results show the exercised design decisions under supplied prompts. They do not establish executed code, provider-wide behavior, automatic skill discovery, statistical reliability or improvement over the previous texts. No baseline run used the old texts. All cases in a run shared one context. The removed principle rules were not tested for regressions, because jstack now follows the source and does not keep them.

## Package checks

The 95 regression tests pass, with 3 skipped. The documentation check reports 0 problems, `git diff --check` passes and the port script reports no difference. The skill creator's `quick_validate.py` passes for 17 of the 18 changed packages. It rejects Sharpen's `disable-model-invocation` key, which is unchanged from main and matches upstream. Manifest validation results are recorded in the PR.

Raw reports and prompt-only inputs stay in `~/.cache/jstack/upstream-batch-eval/`, outside the repository. No installation, model configuration or schedule changed.
