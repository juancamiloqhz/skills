# Fresh-parent evaluation

Date: 2026-10-06. Status: completed. Operational workflow passed; candidate rubric disclosure deviated from upstream Arena and was clarified afterward.

A fresh T3-owned coordinating agent receives only the skill path, selected candidate models, read-only scope, and a new self-contained webhook-processing design problem. It receives no previous candidates, judge answer, or expected design. Its own provider/model inherits from this thread. It may delegate the candidate and judge seats required by the skill, but may not edit files, install, publish, or create top-level threads.

Before dispatch, clarified the skill's read-only paragraph: only candidates and judges are forbidden from further delegation. The coordinating parent must be allowed to dispatch its seats even when it is itself a delegated evaluator.

Inspect the parent's actual activity and child task/thread receipts for live capability discovery, independent same-brief candidates, correct selected models/options, explicit grounding, terminal collection, a fresh post-candidate judge, synthesis and failure-scenario verification. Distinguish observed tool activity from self-report. Automatic skill discovery and provider installation remain outside this experiment.

## Observed workflow

The fresh parent was `codex/gpt-6.1-sol`. Its activity shows reads of the skill and orchestration reference, a capability-catalog call, two asynchronous candidate dispatches, result collection after completion notifications, and a new judge dispatch after both candidates finished. It resumed over four turns without intervention from the outer evaluator.

| Check | Evidence |
| --- | --- |
| Independent candidates | Two distinct child task/thread IDs; candidate briefs are byte-identical |
| Selected models | Dispatch targets and receipts confirm `codex/gpt-6-astra` and `claudeAgent/claude-opus-5-5`; requested reasoning options are medium |
| Fresh judge | Third distinct thread using `claudeAgent/claude-sonnet-5-5`, different family from the coordinating parent |
| Complete comparison | Judge input contains both complete published candidate summaries verbatim, labelled A/B, with no candidate model IDs |
| Terminal collection | All three collected task outputs are completed, result available, and have no pending child runs |
| Grounding | All three results acknowledge both required paths; the coordinating parent's filesystem read activity is visible |
| Synthesis | Parent selects A, incorporates B's recovery details, corrects claims from the judge/candidates, and checks explicit failure scenarios |
| Read-only boundary | Visible parent commands read the skill files; participant results report no writes. This does not prove operating-system isolation |

[Audited tool inputs and outputs](./pstack-t3-review-parent-audit.json) retain the candidate dispatches, terminal results, and judge brief. [Complete parent result](./pstack-t3-review-parent-result.md) retains the synthesis, selected base, contributions, rejections, uncertainties, and failure checks. The original [launch receipt](./pstack-t3-review-parent-receipts.json) remains available.

## Deviation and correction

The coordinating parent included the rubric in both candidate briefs. Upstream Arena separates the candidate task from the comparative grading rubric. Our previous wording said the judge receives the rubric but did not explicitly exclude it from candidate briefs. Clarified that boundary in the skill after this run. The corrected wording has passed structural validation but has not received another behavioral run. Candidate independence, model selection, and lifecycle handling still passed.

No other workflow edits were needed. The result identifies the snapshot/delta distinction and notification-provider assumptions rather than claiming unconditional ordering or delivery guarantees. These are conceptual design checks, not executed database or provider tests.

## Completion and limits

The fresh parent ran the read-only panel from the skill without step-by-step outer coordination. This adds evidence beyond the first manually coordinated run. It does not establish automatic discovery, installation, full pstack compatibility, worktree writers, cancellation, or behavior on model failure. Reasoning options are submitted values; provider-effective settings were not independently measured. The skill remains experimental and uninstalled.
