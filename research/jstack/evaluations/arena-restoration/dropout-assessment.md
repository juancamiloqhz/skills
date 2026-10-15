# Arena continuation assessment

This is a tabletop assessment of the supplied states. No candidates, judges or workflows were launched. No settings, source files or external systems were changed. Citations refer to the current authoring files. I read the required upstream-fidelity policy, the Arena entrypoint, its execution reference and the Architect entrypoint. I applied the unslop prose guidance. I did not read other research or evaluation conclusions.

The states establish only the facts they give. In particular, a viable artifact is not proof of completed judging or verification. Where terminal state includes no pending nested work, the lifecycle prerequisite is satisfied. Otherwise, a completed candidate turn alone is insufficient under [execution.md, line 19](/home/ubuntu/Dev/skills/skills/jstack/arena/references/execution.md:19).

## A. Ordinary Arena with one viable survivor

Proceed with the survivor and record the dropout. Revalidate the selected configuration and current catalog, then use one eligible judge from the configured pool. Read and score the surviving design against the prewritten rubric, compare the judge's rationale, verify the design against the original acceptance checks, and return the design package if those checks pass. The ordinary one-survivor fallback is explicit in [Arena, line 27](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:27); judge selection and rubric assessment remain required by [lines 31 and 35](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:31).

State explicitly that no multi-candidate comparison was possible. Do not claim that the survivor beat B on design merit, that two candidates converged, that a graft came from B, or that inherited seats establish model diversity. Preserve the original artifact and use a separately owned synthesis destination if producing the final package, following [Arena, line 41](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:41).

The dropout alone does not make ordinary Arena incomplete. Missing judge eligibility, required dependencies or unsuccessful verification would. Design verification means tracing caller usage, ownership and failure paths against grounded source; it does not establish executed behavior. See [Arena, lines 51–59](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:51). No implementation is authorized by this design-only state, per [Arena, line 47](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:47).

## B. Architect with one viable survivor

Preserve the viable design, report the dropout and return the unmet requirement as incomplete. The survivor cannot be accepted as the completed Architect synthesis. Architect requires both at least two viable configured candidates and two structurally distinct designs, under [Architect, lines 34–36](/home/ubuntu/Dev/skills/skills/jstack/architect/SKILL.md:34). Arena explicitly preserves that caller requirement in [lines 27 and 37](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:27).

Do not claim the ordinary one-survivor fallback satisfies Architect, that two dispatched seats equal two viable designs, that inherited models establish model diversity, or that a second structure exists without an artifact. Do not invent replacement seats or silently change models. Judging the survivor, if useful as partial work, cannot satisfy the missing design requirement or authorize synthesis and implementation.

The text does not prescribe a specific dropout-recovery retry. Architect explicitly permits grounded reframing with distinct structural hypotheses when candidates converge, and Arena specifies fresh tasks with a corrected common brief and the same panel for reframing. These rules do not establish that a dropout needs a reframed brief or authorize an automatic replacement seat. The given state supports an incomplete report; further recovery needs an evidenced reason and the same configuration constraints. See [Architect, line 42](/home/ubuntu/Dev/skills/skills/jstack/architect/SKILL.md:42) and [Arena, line 47](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:47).

## C. Ordinary Arena with no viable artifacts

Return incomplete, record both dropouts and reconcile owned writes and terminal child state. There is no artifact to judge, select, graft or verify. This follows directly from [Arena, line 27](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:27) and the completion record requirements in [line 59](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:59).

Do not claim a winner, consensus, synthesized result or successful verification. Do not fabricate a coordinator replacement or introduce new seats or models. The instructions do not specify an automatic retry for this state. A future recovery attempt does not make this round complete.

## D. A draft exists while B is writing

Wait for B and all pending nested work to finish. Inspect actual outputs and freeze them only after the completion condition holds. Do not start the cross-judge while B is writing. The barrier is explicit in [Arena, lines 27 and 31](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:27).

Do not call B a dropout, call A's draft the winner, describe the candidates as frozen, or claim the candidate phase or Arena is complete. This is pending work, not evidence of a failed viability requirement. If a timeout occurs later, it does not cancel B; replacement requires cancellation of owned children and reconciliation of their writes, per [execution.md, line 19](/home/ubuntu/Dev/skills/skills/jstack/arena/references/execution.md:19). No timeout is established in this state.

## E. One inherited runner seat before dispatch

Stop before dispatch and report the start requirement unmet. Arena requires at least two configured candidate seats, preserves configured counts and forbids automatic expansion in [Arena, line 20](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:20). One inherited seat is one seat, because the runner list assigns one candidate per entry under [execution.md, line 15](/home/ubuntu/Dev/skills/skills/jstack/arena/references/execution.md:15).

Do not treat the post-dropout one-survivor fallback as permission to start with one seat. Do not duplicate the seat, append a default model or change saved settings. Inheritance itself is valid and retains the parent selection; the blocker is the configured candidate count. The state remains incomplete until a user-requested configuration change supplies a valid panel. No settings edit is authorized by this tabletop.

## F. Two viable candidates but only an inherited judge, with different-family judging required

Revalidate the selected configuration and current catalog as Phase C requires. If the only available eligible judge remains inherited, stop incomplete and preserve the candidates. Inheritance retains the parent's provider, model and effort; its catalog identity is used to check family requirements. It cannot satisfy a different-family requirement relative to the parent. See [execution.md, line 15](/home/ubuntu/Dev/skills/skills/jstack/arena/references/execution.md:15), [Arena, line 20](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:20) and [Arena, line 31](/home/ubuntu/Dev/skills/skills/jstack/arena/SKILL.md:31).

Do not weaken the caller's requirement to a preference, substitute an unconfigured judge, call inherited judging independent family diversity, or claim that viable candidates alone complete Arena. Disclosing inherited judging is insufficient when diversity is mandatory. No eligible judge should have stopped candidate work before dispatch if these facts were already known, per [execution.md, line 17](/home/ubuntu/Dev/skills/skills/jstack/arena/references/execution.md:17). The supplied state does not establish whether eligibility changed after dispatch, so it does not prove an earlier violation.

The skill's stated family comparison is with the parent. If the caller instead means a different family from every candidate, that requirement needs candidate identities as well. The supplied inherited runner states would still make the inherited judge the same family, but F does not independently specify its candidate identities. Under either interpretation, do not claim the diversity requirement is established without the required identity evidence.

## Instruction limits

The main boundaries are explicit: a two-seat start minimum, a one-survivor fallback for ordinary Arena, stricter caller requirements, a terminal-and-frozen barrier before judging, and mandatory diversity when requested. The text is less explicit about whether to perform partial judging after a stricter caller has already failed and about a same-model retry after a pure dropout. Neither ambiguity permits claiming success, changing the panel or fabricating a second artifact. No live transport capability, configuration validity or verification result was tested in this assessment.
