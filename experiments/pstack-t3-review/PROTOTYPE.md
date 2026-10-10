---
name: pstack-t3-review
description: "Run a pstack-inspired review panel in T3 Code when the user requests independent model analyses followed by a fresh cross-judge. Supports read-only text artifacts; requires T3-owned delegation."
---

# Pstack T3 review

Produce independent text candidates, judge them in a fresh context, and synthesize a verified recommendation. This experimental subset adapts Arena; it does not enable full pstack or poteto-mode.

## Frame

Read [t3-orchestration.md](references/t3-orchestration.md) before dispatch. Consult [upstream.md](references/upstream.md) when checking provenance or updating the adaptation.

Establish the question, supplied evidence, constraints, candidate artifact, and a concrete grading rubric. Candidates receive the same task and grounding, without other candidates' answers. Keep the comparative grading rubric in the parent and judge briefs; candidate briefs contain the task requirements. Preserve user-selected providers, models, and reasoning options.

Check the live capability catalog. Choose at least two candidate seats and a fresh judge, preferably from a different model family than the parent. If required models, grounding, or delegation are unavailable, report the missing capability and stop the panel. A parent answering repeatedly is not an independent panel.

## Candidates

Delegate each seat using the same brief and a unique request ID. Include absolute paths to this skill and its orchestration reference, the role `candidate`, the original task, and all required grounding. Each child must read those files before answering and acknowledge the paths it read.

Candidates return their full text artifact, rationale, rejected alternatives, and uncertainties in the task result. Keep all participants read-only: no file edits, installation, external writes, new top-level threads, or workspace changes. Only the coordinating parent delegates panel seats; candidates and judges create no further agents. Child instructions define this boundary; a review role alone does not enforce filesystem permissions.

Collect every terminal result by task ID. A dropout reduces coverage; fewer than two usable candidates stops the panel. Report unavailable seats without silently substituting models.

## Judge and synthesis

After candidates finish, delegate a fresh judge with the original task, complete candidate results labelled A/B/etc., rubric, and grounding. Omit candidate model names from the labelled answers where practical. The judge scores each criterion, identifies unsupported assumptions, recommends a base, and names useful contributions from the others. A failed judge leaves the panel incomplete.

Read every candidate yourself and compare the judge's reasoning against your own assessment. Resolve substantive disagreements with evidence. Return one coherent recommendation, noting the selected base, incorporated contributions, rejected suggestions, and remaining uncertainty.

Verify the synthesis against each supplied requirement and at least one relevant failure scenario. Record provider/model/options, task IDs, dropouts, grounding acknowledgements, and verification results alongside the evaluation when the user authorized saving artifacts. Keep the final answer focused on the recommendation and material limitations.

## Child roles

If dispatched as `candidate`, read the orchestration reference, acknowledge grounding, and produce only the assigned candidate artifact. If dispatched as `judge`, read the reference and return only the assigned comparison. These roles do not run the parent workflow or create more agents.
