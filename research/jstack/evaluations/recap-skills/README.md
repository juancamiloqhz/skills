# Bro and Ketchup adoption

Date: 2026-10-19. Local base: `cffa91930187de6698e493632e26b18f9b66e622`, merged PR #95. Source: `cursor/plugins` at `0148b78c56c72a1b8412055913c79f767095b217`, paths `pstack/skills/{bro,ketchup}/SKILL.md` and `pstack/LICENSE`.

## Scope and source comparison

The user approved both standalone skills before their newer Autopilot callers. Bro restates the last answer; Ketchup gives a read-only catch-up and the complete list of pending user decisions. It does not resume work or merge PRs. No model role or configuration change is needed.

Bro's body and description are unchanged. Ketchup preserves all source sections, their order and every substantive source paragraph. The [Bro](../../adaptations/bro.md) and [Ketchup](../../adaptations/ketchup.md) records account for the portable name, independently located Bro dependency, T3 history/status reads, missing-evidence behavior and host visual tools. Both packages retain exact source license bytes and the source's explicit-invocation flag; Codex also gets its supported YAML policy. Full final files were compared against the frozen Git objects.

The manifest adds two mappings at the audited pin and Bro as Ketchup's dependency. The original `2026-10-11-ketchup` decision keeps its ID and range but changes from defer to adapt after approval, with no `appliedCommit` before merge. PR [#96](https://github.com/juancamiloqhz/skills/pull/96) subsequently merged as `14dac6ed370190910651ff8f25c644de85888539`; the next maintenance PR records that verified merge in the ledger. Its original [review](../../upstream-reviews/2026-10-11.md) remains historical evidence. The shared reviewed checkpoint and all 45 previous mappings are unchanged. Autopilot callers remain for the next coordinated update.

## Consumer exercises

[Cases](cases.json) retain the six fictional conversations, current-read evidence and expected behavior. To replay, copy both packages into different parent directories, provide the evaluator with those exact catalog paths and the cases without their `expectations`, and request actual user-facing replies. Keep the evaluator read-only except for its own report. The example.invalid links are fixture data, not real PRs.

One fresh native Codex `gpt-6-astra`/high evaluator read both complete packages from separate cache directories. It received no expected answers, source diff or earlier conclusions. The parent reviewed the actual six replies. Five met the intended behavioral checks; the missing-history case exposed one unsupported action item.

| Case | Observed result |
| --- | --- |
| Bro | Plainly explained the version check, rejection of stale writes and untouched competing update. Kept the caveat that two live production clients had not been tested. Started no work. |
| Stale status | Used the last real human request despite a synthetic user-role notification. Corrected the old claim that both PRs were ready: Search merged; Export failed. Retained the earlier retention choice with both options, kept the export fix as agent work, advised holding its merge, and disclosed absent screenshots. |
| Nested work | Reported that a completed review turn still had an active child. Kept the known fixture-path answer as parent work, not a user decision. Did not answer or resume the task. |
| Partial history | Disclosed missing history, Bro and live PR status without inventing a link or success. However, it asked the user to restore authentication without evidence that only the user could do so. |
| Ten decisions | Listed all ten PRs with individual links, effects and risks under one merge recommendation. Did not replace the list with a count or generate screenshots. |
| No change | Replied only that nothing changed and nothing was waiting on the user. |

The partial-history failure prompted one sentence in the T3 adaptation: an unavailable read alone does not establish a user-only action. A second fresh evaluator received only the updated skill and that same raw scenario, without the failure or expected response. It reported unknown state and incomplete decision coverage without assigning access repair to the user. This focused retest passed; the other five cases were not repeated after that narrow sentence addition.

Both evaluators used simulated status results. They made no live forge, history, task or visual calls, dispatched no children, and changed no skill files. Byte comparisons confirmed the separately located exercise packages matched source, including the amended Ketchup on retest. This is one six-case exercise and one focused retry, not a reliability estimate or controlled comparison with an unskilled baseline.

## Live read probes

The parent separately exercised T3's current thread reader with `view: activity`. Two pages returned distinct increasing positions; `afterPosition: nextPosition` advanced correctly. A deliberately truncated assistant message was recovered with its returned item ID and UTF-16 offset, and the joined text matched a complete read. No complete conversation-history reconstruction was attempted.

An initial probe passed `runLimit: 0` and was rejected by the tool's minimum-one constraint. Repeating with `runLimit: 1` succeeded; the skill does not prescribe this optional parameter. A fresh GitHub read confirmed the already merged PR #95. These probes establish bounded read mechanics, not a live end-to-end Ketchup run, native/T3 child-state equivalence or persistence recovery.

## Packaging checks and limits

The four repository packaging tests pass. Both frontmatter flags parse as boolean true and both Codex policies as boolean false. The generic Codex authoring `quick_validate.py` rejects the preserved source key `disable-model-invocation` because it is outside that script's allowlist. It is not a loader test. Temporary validation copies with only that extension omitted pass the remaining core-field/body checks. The distributed files retain the flag; this is not an unmodified validator pass or proof that every provider honors explicit invocation.

Manifest validation, current-document checks, final source comparisons, relative links and staged whitespace pass. The current catalog has 47 packages, 23 commands, 24 principles and 23 playbooks. Existing guide coverage remains pending. No installed catalog, automatic invocation, cross-provider discovery, Autopilot caller or visual-rendering pipeline was tested. The manual installation guide names both dependencies and requires no setup rerun.

Retain only this report and the replayable cases. Raw responses, copied packages, tool evidence and intermediate expectations stay in task cache. No operational script, generated screenshot, transcript archive or hash inventory is committed.

## Normal use

After merge and manual installation, invoke `$jstack-bro` when an answer is too technical. It simplifies that answer while keeping its important caveats.

Invoke `$jstack-ketchup` when returning to a long conversation. For example, it can tell you that the search fix merged, the export test failed, and your earlier retention choice is still unanswered. It reports those facts and decisions without fixing, merging or restarting anything.
