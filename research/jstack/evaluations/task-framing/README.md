# In your own words and Sharpen adoption

Date: 2026-10-19. Local base: merged PR [#98](https://github.com/juancamiloqhz/skills/pull/98), `8bbe90bc274c686047f6294cdcb079d8f740dc68`. Source: `cursor/plugins` at `0148b78c56c72a1b8412055913c79f767095b217`, `pstack/skills/{in-your-own-words,sharpen}/SKILL.md` and `pstack/LICENSE`.

This is the historical adoption record. Sharpen's later [prompt-only update](../sharpen-prompt/README.md) supersedes its execution behavior and examples below. The original cases and outcomes remain evidence for the earlier version. In your own words is unchanged.

## Scope and source comparison

The user selected this pair after the coverage checkpoint. In your own words restates the user's goal and underlying problem. Sharpen improves the approach and then does the authorized task, retaining an outside check. It is not a mandatory questionnaire or merely a prompt-writing helper.

Both complete bodies remain byte-identical to upstream. Only the name and description's slash command gain the `jstack-` prefix. Each package adds the exact source license and a small Codex invocation policy. The [In your own words](../../adaptations/in-your-own-words.md) and [Sharpen](../../adaptations/sharpen.md) records account for every difference. No extra procedure, reference hierarchy, model role, automatic mode trigger or helper dependency is introduced.

Both source flags preserve explicit-invocation intent; Codex also receives `allow_implicit_invocation: false`. These settings do not prove discovery or behavior in an installed provider. The manifest adds two mappings at the audited pin. Existing mappings, decisions and the shared reviewed checkpoint are unchanged. The current tree contains 49 packages: 46 mapped pstack skills plus three team-kit helpers. Eight top-level pstack skills remain absent and Unslop remains external. The earlier coverage checkpoint retains its dated 47-package baseline.

## Consumer exercise

[Four cases](cases.json) retain requests and expectations. For replay, give a fresh evaluator only each request, the named complete skill and its raw supplied facts. Omit expectations and prior conclusions. Ask it to produce the actual requested answer, draft or calculation. Allow only local calculations and a task-owned report; prohibit external actions, network reads, configuration changes, product edits and nested dispatch. Keep outputs outside the repository.

One native Codex evaluator used the authoring conversation's inherited `gpt-6-astra`/high, without invoking a configured production role. It received both complete authoring packages and four separate fictional scenarios. The parent inspected all four actual outputs against the retained expectations.

| Case | Observed output |
| --- | --- |
| Goal versus solution | Restated reliable uploads, unchanged API and no paid service. Kept the queue as a candidate and stopped at confirming understanding. |
| Open product choice | Identified the hard-to-find next action. Left hidden controls versus navigation redesign undecided and invented no metrics or implementation. |
| Over-specified email | Produced a 59-word draft including its subject/greeting, using fewer than eight sentences. Preserved 14:20 UTC, the 16:00 UTC update regardless of resolution, uncertainty about data loss and no resolution ETA. It did not send the draft. |
| Capacity decision | Completed the recommendation to retain one worker for the stated sustained load. Calculated 66.67% utilization and 105 jobs/hour capacity at the 70% limit, matching the supplied independent replay. Left unknown bursts unproven and made no purchase or deployment. |

The evaluator used Python 3 to check email length/times and capacity arithmetic, and checked the draft against the supplied support policy. Its first command used unavailable `python`; rerunning with `python3` succeeded. This was an exercise-command correction, not a skill change. The numeric answer reported usable capacity at the policy limit rather than raw 100% capacity; its calculation and decision were correct. All four cases met their substantive expectations. No source-body change was needed.

This is a bounded exercise with supplied data, not live incident, capacity or customer evidence, and not a reliability estimate. It does not compare against an unskilled baseline. No installed catalog invocation, later-task activation, cross-provider behavior or unrequested automatic invocation is tested.

## Packaging validation and limits

Four packaging tests pass. Source comparisons reverse only the name and slash-command substitutions and recover the exact frozen source bytes. License bytes and parsed boolean metadata match their intended values. The manifest validates.

The generic Codex `quick_validate.py` rejects both original packages because `disable-model-invocation` is outside its allowlist. Temporary copies omitting only that key pass its remaining checks. This is a qualified validation result, not an unmodified validator pass or a host-loader test. The shipped flag remains intact, as with Bro and Ketchup.

Run existing repository checks:

```sh
python3 -B scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
```

The first document check caught the research index's old 47-package count; the index now reports 49 and the check passes. Changed-link and whitespace checks also pass. The document checker reports 49 skills and 23 playbooks; guide coverage remains pending. No installation, model selection, schedule or existing operational skill is changed. Retain this report and replayable cases; raw consumer output and temporary validation copies stay in task-owned cache or are removed after use. There is no new operational script, generated dataset or transcript archive.

## Normal use after merge and manual installation

Use `$jstack-in-your-own-words` after explaining a task. For example: “I want uploads to stop timing out; a queue might help, but keep the API unchanged.” It restates the goal, the proposed solution and your constraints so you can correct misunderstandings before work.

Use `$jstack-sharpen` with a task: “Check whether our importer needs another worker using these timings.” It chooses an appropriate method, performs the calculation and checks the conclusion against independent evidence. Product choices and unknowns remain visible; the request does not authorize a purchase or deployment.

Neither skill requires Juan-mode activation or a setup rerun. The [manual installation guide](../../skill-names.md#additional-standalone-helpers) includes the exact package names and command. Installations remain user-managed.
