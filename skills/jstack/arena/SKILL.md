---
name: arena
description: Compare independently produced candidates for the same task, cross-judge them and synthesize one verified artifact. Use when the user asks for competing approaches or an arena, or a workflow needs candidate comparison.
---

# Arena

Produce one synthesized artifact from independently generated candidates. Direct invocation is task-scoped and leaves juan-mode activation unchanged. A calling playbook supplies the artifact, source scope, selected configuration and return boundary. Design-only callers receive a design package; this skill does not advance them into implementation. Read [configuration and execution](references/execution.md) before dispatch.

## Frame

Track Frame, Candidates, Cross-judge, Pick, Synthesize and Verify in the task plan. State the requested artifact, source revision, permitted actions, output location and observable acceptance checks. Derive three to six concrete comparison criteria. Keep the scoring rubric and model identities out of candidate briefs; candidates receive the common task requirements and grounding, not hidden expectations required for correctness.

Resolve `arena runners`, or `architect runners` when the caller explicitly selects that panel for a design task. Preserve all configured seats in order, including duplicates and inheritance. Require at least two configured candidates; a single seat is valid model configuration but cannot perform this comparison. Resolve `arena cross-judge pool` and select one executable alternative before spending candidate work. Prefer a demonstrably different model family from the coordinator when available. A same-family or inherited judge is permitted unless the caller requires family diversity; disclose the limitation. Different provider instances alone do not prove different model families. An unverifiable required independence condition or insufficient configuration stops the comparison as incomplete without changing settings or inventing seats.

Give candidates distinct labels and owned output directories. For code changes use isolated worktrees prepared by the coordinator; for design or text use separate temporary directories. Check existing contents and preserve unrelated work. A prompt path alone does not change the child's app workspace binding. Run artifact writers serially until the selected provider/tools have demonstrated explicit-path behavior. Safe independent work may then run concurrently.

## Produce candidates

Dispatch one child per configured panel entry with the same task and grounding, its assigned source and output paths, the selected absolute configuration path, permitted actions and stop condition. Each produces the artifact and a short rationale identifying alternatives considered and rejected. Candidate children do not read each other's outputs, the rubric, judge notes or the coordinator's preferred answer. Use fresh task context when the delegation interface supports it; if it only inherits a context containing those materials, use a supported fresh-context transport or report the isolation gap before dispatch.

Wait for every task and any nested work to finish before judging. Inspect actual outputs and record failures or absent artifacts as dropouts. Continue only if at least two viable candidates remain and any caller-specific requirement still holds. Do not silently replace a failed configured seat, increase fan-out or claim a comparison when only one candidate survived. Retain useful artifacts when returning an incomplete result.

## Cross-judge and pick

Revalidate the selected configuration and judge capability. Dispatch exactly one judge from the pool, with read-only access to frozen candidate artifacts, the task and rubric. Label artifacts by candidate ID, not provider or model; keep the identity mapping in the coordinator's record. This avoids supplying model labels to the judge, but does not guarantee that style or artifact content cannot reveal authorship. The judge scores each criterion, cites concrete artifact evidence and recommends a base. It does not edit candidates or synthesize the result.

While the judge works, the coordinator reads every viable candidate and scores each against the same rubric. Read the judge's actual report after it completes. Investigate disagreements against artifacts and criteria before selecting a base; the judge is evidence, not an automatic vote. Prefer a coherent boundary and smaller public interface when candidates otherwise tie. If a caller requires structurally distinct alternatives, verify that property before accepting synthesis. Convergence is acceptable for ordinary Arena tasks, but does not satisfy a required design-space exploration.

## Synthesize

Keep the original candidates intact. Starting from the chosen base, create the final artifact in its separately owned destination. Inspect each losing candidate for useful contributions, usually a small number rather than most of its content. Integrate selected contributions coherently instead of mechanically concatenating them. Record what was retained, rejected and why. If candidates converge, record that no graft was needed. If they diverge because the requirements were underspecified, reframe and start fresh candidate tasks with the corrected common brief rather than averaging incompatible assumptions.

The coordinator performs synthesis unless the calling workflow supplies an already authorized synthesis role. Candidate selection does not authorize source edits, installation, publication, PR creation or merge outside the original request. For a design-only task, keep sketches and rationale in the assigned artifact directory and leave the target implementation untouched.

## Verify and return

Verify the synthesized artifact against the original acceptance checks, not just the scoring rubric. For code, execute the appropriate authorized checks in the correct checkout; for a design, trace representative caller usage, ownership, failure paths and constraints against the grounded source. Report source inspection separately from executed behavior. An unavailable prerequisite makes verification incomplete, not passing.

If verification fails, identify whether the requirements need reframing or a missed contribution must be integrated, then repeat the affected phase and checks. A new review or candidate round uses fresh child tasks with the original brief, relevant prior findings and unresolved objections. Do not endlessly rerun unchanged work after a failure; return the concrete unmet condition when progress needs new information or authority.

Return the final artifact and a synthesis note naming the base, per-criterion comparison, judge verdict and disagreements, contributions with source labels, rejected alternatives, dropouts or convergence, actual verification and remaining gaps. Retain task IDs and candidate artifacts needed to review the result; remove owned temporary catalogs. The coordinator checks terminal state and reconciles owned writes before declaring completion. Return to the user or caller at its requested boundary.
