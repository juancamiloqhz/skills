---
name: architect
description: "Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
---

# Architect

Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. Synthesize across multiple model perspectives, then fill in code against the chosen sketch.

Direct invocation is task-scoped and leaves juan-mode activation unchanged. Establish the source root/revision, owned artifact location, acceptance checks and return boundary from the request. A design-only or ambiguous design request returns a design without implementation or executable placeholders in the target project. An explicit checkpoint pauses for sign-off. Already authorized implementation continues without another approval; commits, PRs, merges and installation follow the original task's authority.

Discover **how**, **why**, **arena**, **setup-jstack** and any needed **interrogate** or **principle-*** skill through the current catalog, or use explicitly supplied authoring paths. Read their actual entrypoints and resolve resources relative to their advertised directories, not assumed sibling installations. If a required dependency is unavailable, return incomplete and provide `npx skills add juancamiloqhz/skills --skill NAME` for manual installation. Preserve saved settings. Pass the selected absolute configuration path through every helper; let the first helper's canonical resolver select it when none was supplied.

## Start

Open a task plan with one entry per phase before starting. Mark phases outside the authorized scope as not applicable.

1. Ground
2. Sketch
3. Agree
4. Implement
5. Scrap

## Phase A: Ground the problem

Build a real mental model of every system the new code touches. Run the **how** skill over the relevant subsystems. Naming a file isn't grounding. Produce the architectural explanation `how` prescribes. If the design redefines ownership or layering, also run the **why** skill on the existing shape so the rationale becomes a constraint, not a guess.

Skip Phase A only when the work is genuinely greenfield with no surrounding system to integrate.

## Phase B: Sketch

Run the **arena** skill with the design-sketch task and the Phase A grounding artifacts. Pass `references/runner-prompt.md` as each runner's prompt.

Use the configured `architect runners` panel in place of `arena runners`, retaining `arena cross-judge pool`. Arena owns canonical resolution, capability checks, independent candidate contexts, owned outputs, judging and terminal child checks. Preserve configured seats, including inheritance and duplicates; never add default seats or substitute models. At least two viable configured candidates are required by the current Arena contract. Inherited or repeated models do not establish model diversity. Pass an explicit design-only return to Arena; Architect owns any later implementation.

Design it twice. Require at least two structurally distinct candidates before synthesis, even when the first looks sufficient. This is the **principle-exhaust-the-design-space** principle skill made concrete. Whole-shape alternatives, not point fixes inside one shape.

Screen every candidate against [`references/design-red-flags.md`](references/design-red-flags.md) before synthesis. Assume the next contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Prefer the design where a change that looks right from one file is right for the whole repo.

Compare viable candidates on interface depth. Prefer the design that hides more complexity behind a smaller, simpler public surface. A rich interface can keep call chains short by concentrating capability instead of scattering it across layers.

If candidates converge on one structure, preserve them and report that the required exploration is incomplete. A grounded reframing can assign distinct structural hypotheses in fresh tasks using the same configured panel; do not fabricate differences or repeat unchanged briefs indefinitely.

Arena returns one synthesized design package. Its synthesis decision fills the rationale's "Synthesis decision" section.

## Phase C: Agree (opt-in)

For an implementation task, proceed directly with the synthesized design within existing authorization. For a design-only request, return the package here. An ambiguous design request grants design scope only.

Opt in to a checkpoint when the invoker explicitly asks: "/architect with checkpoint," "stop and show me before implementing," or similar. Then surface the synthesized design and pause for sign-off.

When commits are authorized, the synthesis can ship as its own commit either way, as the "scaffold first" mode of the **principle-foundational-thinking** principle skill. Planned and scoped breakage during fill-in is fine, per the **principle-outcome-oriented-execution** principle skill. For adversarial pressure on the design before implementing, run the **interrogate** skill on the synthesized sketch when the task and host permit delegated review. Report an unavailable dependency instead of treating Arena as a substitute.

If the human pushes back on the shape (in a checkpoint or after the fact), treat that as Phase A evidence. Re-ground and re-run Phase B before writing more code.

## Phase D: Implement against the sketch

Replace `not implemented` bodies with code, pseudocode with logic. The synthesized sketch is the contract. Deviations from it are signal to surface, not friction to absorb silently. If a function needs a parameter the sketch didn't anticipate, ask whether the sketch was wrong, the requirement was missed, or the implementation is overreaching.

## Phase E: Scrap when the architecture is wrong

If implementation keeps producing friction the sketch can't absorb, throw the sketch out. Don't bolt fixes onto a wrong design, per the **principle-redesign-from-first-principles** and **principle-fix-root-causes** principle skills.

The signal is a *pattern*, not single instances. Tells:

- The same shape of workaround appearing repeatedly across unrelated code.
- Multiple unrelated edge cases that all need special-case branches.
- Types that need escape hatches (`any`, casts, optional fields always set in practice) to compile.
- The "we need a lock" reflex when the sketch said the state wasn't shared.
- Callers having to know the abstraction's internal rules to use it.
- Two or more independent Phase D deviations of the same shape across the implementation.

Use judgment. A few edge cases don't condemn an architecture. Some problems are legitimately complex. Complexity in the data is not complexity in the design.

Preserve unrelated work and useful prior artifacts. Discarding a sketch does not authorize a destructive checkout reset. If progress needs new information or authority, report that blocker instead of cycling.

When you scrap:

1. Re-run the **how** skill over what's been built.
2. Redesign as if the new constraints had been day-one assumptions, per redesign-from-first-principles.
3. Subtract before adding, per the **principle-subtract-before-you-add** principle skill. The new sketch should be smaller than the old one before it grows.
4. Return to Phase B and re-run arena.

## Outputs

The caller's usage is written first and the type sketch derived from it. One file with new types and signatures for small changes. Module map plus type definitions for larger work. The rationale ships alongside, shaped per `references/rationale-template.md`, including the usage sketch and the synthesis decision.

Check decisive source citations and the final design against the task's acceptance criteria. Distinguish static design tracing from executed behavior. A missing prerequisite or failed check remains incomplete.
