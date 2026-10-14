---
name: figure-it-out
description: "Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions. Use for /figure-it-out or 'figure it out'."
---

# Figure it out

When the task matches no playbook, design one. The deliverable before any code is the workflow itself: a sequence of phases that scales rigor to the task, runs the scientific method, and leaves a decision trail a human can audit after stepping away.

Direct invocation is task-scoped and leaves juan-mode activation unchanged. Establish source scope, owned artifacts and the requested return boundary; preserve unrelated work. Planning-only requests stop after Phase B. Implementation, commits, PRs, merges and installation follow the original task's authority. This helper does not make an unavailable named playbook executable.

Discover required helpers through the skill catalog or explicit authoring paths and read their actual entrypoints; do not assume sibling installations. If a required jstack helper is unavailable, mark that phase incomplete and provide `npx skills add juancamiloqhz/skills --skill NAME` for manual installation. Pass the selected absolute configuration through helpers once resolved.

## Start

Open a task plan whose first item is to read the relevant standalone principles through [principle discovery](references/principles.md). Then add the phases below as tasks.

## Phase A: Frame

Ground first, then commit. Don't start the run until you can state:

- The definition of done as a falsifiable predicate (the **principle-prove-it-works** principle skill).
- Scope, quantified: rough units and effort, plus the blockers grounding surfaced.
- The rigor level, biased high. One-way doors and high blast radius get more. Reversible low-stakes steps get less. Rigor is gates and artifacts, not "try harder".

Present the framing and tradeoffs before committing to a long run. Reversible work proceeds (the **principle-never-block-on-the-human** principle skill), but a multi-hour run earns one framing checkpoint before execution unless its scope and resource commitment are already authorized. Honor any explicit stop-for-approval request; elapsed time is not approval.

## Phase B: Design the workflow

Decompose into atomic, independently-landable units. Sequence riskiest-unknown-first. Scaffold and verification come before features (the **principle-foundational-thinking** principle skill).

- Build the verification harness before the work, with the baseline captured from the pre-change state, so the check reads as "old value vs new value". Reuse an adequate existing harness; record an unavailable baseline rather than inventing one.
- For one-way-door design decisions, run the **architect** skill with a design-only return (it runs **arena**). Skip it for mechanical work whose shape is already concrete. A second arena over a settled design is over-engineering (the **principle-laziness-protocol** principle skill).
- Read [configured delegation](references/execution.md) before dispatch. Decide what fans out. Parallelize only across seams, and give each worker its own worktree or branch (the **principle-separate-before-serializing-shared-state** principle skill). Don't over-fan.
- Write the designed phase list down. That list is what the human reviews.

For a planning-only request, return the phase list, rigor, verification design, assumptions and open decisions here without execution workers or product edits. Otherwise execute the design within existing authority. Add its steps to the task plan as concrete items between the Phase C and Phase D entries. Run each under the Phase C loop discipline, and weave the Phase D log through them, a row as each step lands, rather than saving the whole trail for the end.

## Phase C: Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert only the unit's owned changes if it didn't, preserving unrelated work. Apply the **principle-sequence-verifiable-units** principle skill, verifying each unit before starting the next instead of batching checks at the end.

- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Pair every delegated work unit with a separate judge using the configured `judgment and prose` role. Inspect its report and decisive artifact evidence; inherited or same-model judging does not establish model diversity. Missing review remains incomplete. If a worker games the gate, discard that unit's result while preserving other work and harden the contract. If the gate itself is wrong, fix the gate in its own change rather than routing around it.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Don't hide a negative.

## Phase D: Keep the audit trail

Log the run via the **show-me-your-work** skill, starting before the first execution unit and adding rows as work lands. figure-it-out's work is usually ambitious enough to commit the trail so the reviewer can read it in the PR, when publication is authorized. The trail plus the diff is what lets the human come back and trust the work.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Encode any recurring correction as a gate, a lint rule, a check, or a script (the **principle-encode-lessons-in-structure** principle skill).

Complete the trail skill's run-bounded audit and configured review before handoff. A missing check or review stays unverified; bound retries by new evidence and report blockers instead of cycling.

**Reply:** the playbook you designed, the rigor level and why, the decision-trail path, what's verified against the predicate, and what's still open. Include the trail skill's Attention section with its actual reviewer and flags or missing review.
