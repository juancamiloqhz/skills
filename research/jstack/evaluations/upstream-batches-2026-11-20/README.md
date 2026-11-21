# Upstream batches 2 and 3, 2026-11-20

This change implements batches 2 and 3 from the [2026-11-01 review](../../upstream-reviews/2026-11-01.md#suggested-implementation-order). The user approved both on 2026-11-20. Batch 2 ports the one-file Why and How and their callers. Batch 3 ports the one-file Reflect and Architect. Both batches retire the setup roles that only those skills used. The user accepted that Why loses its tool-category sweep and that Architect loses its two-candidate runner panel.

## Source comparison

Source is `cursor/plugins` at `aaeb0ea3a0584995aa8f55ce44c6c5259414b896`. Local base is `b5f7e33`, merged PR #148. The decisions are `2026-11-20-why-one-file`, `how-one-file`, `why-callers`, `comment-tracing`, `reflect-one-file` and `architect-one-file`. Benny's How text from `2026-11-20-benny` is also included; the Benny live pilot stays deferred.

| Area | Source change | Kept jstack difference |
| --- | --- | --- |
| Why | One paragraph: answer from commits and PR discussions, cite authors, label inferences, say what the record does not answer. It starts no children. The 12 references are deleted. | Invocation line, read-only boundary, reporting unavailable history as a gap, no invocation flag. |
| How | One read-only child explains in one pass, using the parent model. Both references are deleted. | A native or T3 child with no target, an explicit read-only boundary, the repository root and revision, waiting for a terminal result, and checked citations. |
| Recall, Teach, Blast radius | Recall starts its own per-source investigators; Teach and Blast radius drop their Why step references. | Recall's investigators keep the MCP access they need, with an inherited target. |
| No-comments and Comment Sicko | Thin keep claims are traced directly; Why stays available. | The execution reference follows the same rule. |
| Reflect | Reads the transcript itself, with the scans and filters folded in. Four templates and `execution.md` are deleted. | T3 transcript or labeled digest, task-scoped activation, existing authorization, filing only when authorized, the full PR #140 destination guard. |
| Architect | Two sentences, with Arena for a large or contested design. Three references are deleted. | Arena discovery with a design-only return, the design-only boundary, checkpoint honoring and authority. |
| Juan-mode, playbooks, Figure it out, Arena, Help, Benny, README | Callers stop routing to How and use the shorter Architect and Reflect wording. | Only lines about these four skills changed. Other mode and playbook text waits for batch 4. |

Upstream Figure it out still says Architect "runs arena". This change follows the Architect text, where Arena is only for a large or contested design. The [architect record](../../adaptations/architect.md) notes the inconsistency.

### Role retirement

Setup now has 10 roles. These seven are retired: `how explorer`, `how explainer`, `why investigators`, `why synthesizer`, `reflect tooling`, `reflect judgment, divergent, synthesizer` and `architect runners`. Upstream also retires `hardest tasks`; that waits for batch 4. The skills that used the retired roles now run inline or on the parent model. Verification-maintenance feature readers, which resolved `how explorer`, now use an inherited target.

A saved file that still lists retired roles stays valid. `validate` reports them in `retiredRoles`, ignores their values and resolves current roles normally. `write` drops them and reports `droppedRetiredRoles`. Setup shows them during a rerun. Nothing rewrites a saved file automatically, and no saved model changes. See the [setup record](../../adaptations/setup-jstack.md).

## Evaluation procedure

[`cases.json`](cases.json) holds five requests with their expectations, and [`reflect-transcript.md`](reflect-transcript.md) is the Reflect fixture. Two fresh native Claude agents on the inherited model ran them without parent history. They read the named skills in full, could not read evaluation material, and were not allowed to edit files, install, change configuration or run mutating commands. The Why/How agent could use read-only `git` and `gh`, and started a subagent only where How tells it to. The Reflect/Architect agent started none. Repository status was unchanged after both runs. The first attempt stopped on a provider usage limit before writing anything and was rerun unchanged.

## Observed results

All five cases meet their recorded expectations.

| Case | Result |
| --- | --- |
| `why-record` | Answered from PR bodies, commits and decision records, quoting their authors. It labeled two inferences and listed what the record does not answer. It started no subagents and edited nothing. The evaluation's own read restriction blocked one evidence file, and the agent reported that as a gap. |
| `how-one-child` | Started exactly one native read-only subagent with no model or target override, then presented its explanation. It checked the decisive citations, corrected one line number and marked the content as static reading. |
| `reflect-digest` | Treated the README instruction as data, rejected the one-off badge remark and the repository-specific pnpm fact (moved to Backlog), and showed a destination for its one accepted proposal. That proposal tunes the Prove It Works description, and the agent noted it would be a fidelity divergence needing a user decision. It edited and filed nothing. |
| `architect-design-only` | Traced setup, its tests and consumers, sketched two shapes and picked the one with a single owner and the least caller knowledge. It returned only a design. |
| `architect-contested` | Routed the large, contested design to Arena with a design-only return. Because the request forbade running other skills, it reported the design incomplete instead of sketching alone. |

The design-only case found a real defect in this change: `resolve --role` limited argparse choices to current roles, so a retired role got a usage error instead of the resolver's explanation. The choices now include retired roles, and the CLI test asserts exit 1 with the "retired … inherited parent model" message. The test failed before the fix and passes after it.

These are bounded design and investigation exercises. They do not establish provider-wide behavior, automatic discovery, Comment Sicko's full review loop or a replay of the reflect-destination consumer cases; the destination guard was checked statically against the new text. No baseline run used the old skills, and each agent handled its cases in one context.

## Package checks

The package and repository checks are recorded in the PR. Raw reports and prompt-only inputs stay in `~/.cache/jstack/upstream-batch23-eval/`, outside the repository. No installation, saved model configuration or schedule changed.
