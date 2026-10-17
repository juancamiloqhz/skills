# Session pickup evaluation

Session pickup is the seventeenth available juan-mode procedure. It recovers the prior stopping point, retains settled decisions, distinguishes matching proof from stale claims, and routes the remaining work. This evaluation supports bounded recovery behavior, not automatic persistence across provider restarts.

Run date: 2026-10-17. Repository base: `af079ddea7615a632b3aa6a04a9851f01de441e0`, merged PR #63. The [adaptation record](../../adaptations/session-pickup.md) accounts for differences from the pinned pstack procedure. The [source comparison](source-comparison.json) records final operational file hashes and pins. The original five-step order and reply contract remain intact; T3 history cursors, child ownership, configuration and current user authority require the recorded substitutions.

## Reproduce the fixture

Run from the repository root with Python 3 and Git. The output directory must not exist.

```bash
python3 -B research/jstack/evaluations/session-pickup/fixture.py /tmp/jstack-pickup-example
git -C /tmp/jstack-pickup-example status --short --branch
git -C /tmp/jstack-pickup-example diff main...HEAD
python3 -B /tmp/jstack-pickup-example/math_cli.py triple 3
```

The generator reuses the [Shipping fixture](../shipping/fixture.py), then adds an earlier passing receipt, a later arithmetic regression, a modified tracked note and an unrelated untracked note. It asserts that the old CLI returns `9`, the current CLI returns `12`, and both HEAD and stable patch identity changed. The sibling `jstack-pickup-example-handoff.json` preserves the original `3*n` goal, integer-only decision, prior receipt and status-only task boundary. The CLI exits successfully despite returning the wrong value; exit status alone is insufficient.

Give a fresh agent the task from [cases.json](cases.json), the generated checkout and handoff paths, and its own report destination. In the with-playbook condition also supply the current Session pickup procedure. Keep the assertions, generator and other agent's report out of both prompts. Compare the responses against all five assertions and compare the checkout's HEAD, visible status and product/user file hashes before and after. The two task/history counterexamples in this pack are explicitly simulated and must not be passed to host tools.

## Observed results

Both fresh native agents used the configured `feature, refactoring` role, Codex `gpt-6.1-sol` at high effort. The parent, Codex `gpt-6-astra` at high effort, assessed the reports and actual commands. One run per condition covered the real CLI fixture plus an independent incomplete-transcript scenario.

| Assertion | With playbook | Without playbook |
| --- | --- | --- |
| Inspect actual Git/CLI evidence and identify stale proof and regression | Pass | Pass |
| Retain settled decisions and completed work without a blanket replay | Pass | Pass |
| Preserve dirty/untracked files and status-only authority | Pass | Pass |
| Treat a simulated terminal task with pending children as unfinished | Pass | Pass |
| Disclose incomplete history and propose focused repair without executing it | Pass | Pass |

Both scored 5/5. This is a bounded compliance check, with no observed score advantage and no reliability or timing estimate. The baseline unnecessarily reran the historical receipt's CLI blob and got `9`; the with-playbook agent retained that historical evidence and checked the changed artifact. The baseline's narrow extra check did not violate the rubric's prohibition on a blanket restart. Both found current `triple 3 = 12`, retained the integer-only decision and existing double implementation, and proposed regression repair followed by verification and documentation review. Neither executed that route or accepted the prior assistant's merge-approval claim as user authority.

The parent compared HEAD, visible Git status and all top-level product/user file hashes before and after both agents. They matched. This does not claim that every Git metadata byte was unchanged. The with-playbook agent's initial report write failed because its owned output directory did not exist; it created that directory and successfully wrote the report. The failure did not modify the fixture.

## Native T3 recovery

Separate parent checks used actual T3 records in this project:

- Read current thread metadata and confirmed this branch's root checkout through scoped worktree lookup. Verified merged PR #63 against the forge.
- Recovered the prior Multi-phase plan comment review by its retained task ID. It was complete with no pending child runs; the review was not rerun.
- Read that known child's first transcript page and recovered truncated text using its returned `itemId` and `nextTextOffset`. Continued the timeline with the returned `nextPosition`, reaching the complete final result that matched task status.

An exploratory root-thread tail lookup derived from `itemCount` returned an empty page despite existing history. It did not establish an empty transcript or complete recovery. The procedure therefore requires returned cursors rather than treating item count as a timeline position. No unrelated chat search was used.

The fixture's unfinished nested task and inaccessible page/text continuations were simulations. Native reads demonstrated recovery of a completed child and available continuations; they did not exercise a live unfinished child or a real inaccessible transcript.

## Review and limits

Comment Sicko ran through T3 using the configured `judgment and prose` role, Claude Opus 5.5 at high effort. It found no comments or docstrings in the generator and returned an empty diff. The parent confirmed the reviewed copy matched the source. Model configuration was unchanged.

Final checks passed: all four `scripts/jstack/test_skill_packaging.py` cases, skill validation for juan-mode and setup, relative Markdown link targets, Markdown lint and `git diff --check`. Markdown lint disabled line-length and first-heading rules for the existing long lines and embedded playbook fragment. Final operational hashes matched the source comparison; the upstream manifest and package license were unchanged. There are 17 local playbook procedures.

Cross-provider restart recovery, automatic mode persistence, long-transcript summarizer dispatch, resuming an active implementation child, and subsequent repair or shipping remain unverified. The agents performed status-only pickups. The fixture contains no live forge or scheduler operations.

Only this report, the small fixture generator, task/assertions and source comparison belong in the repository. Generated checkouts, full answers, grading/viewer output and capability catalogs remain in task-owned scratch. The dirty fixture at `/tmp/jstack-pickup-20261017/fixture` remains available for this pending review; its edits are intentional test data. No evaluation child or process remains active. Scratch can be removed after acceptance when nothing depends on it, following the [retention policy](../../upstream-fidelity.md#evaluation-evidence-retention).
