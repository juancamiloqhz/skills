---
name: architect
description: Design types, interfaces and module ownership through grounded, competing sketches. Use for architecture design requests or when a workflow needs a design before implementation; continue into implementation only within the requested scope.
---

# Architect

Return a grounded design with caller examples, types, ownership and a synthesis rationale. Direct invocation is task-scoped and leaves juan-mode activation unchanged. Track Ground, Sketch, Return or agree, Implement and Reconsider in the task plan, marking phases outside the requested scope as not applicable. See [upstream attribution](references/upstream.md).

Establish the source root and revision, owned artifact location, acceptance checks and return boundary from the user's task or calling playbook. A design-only request returns after synthesis without writing implementation or executable placeholders into the target project. An explicit checkpoint pauses there for sign-off. A task authorizing design and implementation proceeds after synthesis without an extra approval. An ambiguous design request grants design scope only. Commits, PRs, merges and installation follow the original task's separate authority.

Discover jstack `arena`, `setup-jstack` and the grounding skills needed below through the current skill catalog, or explicitly supplied authoring paths. Read their advertised entrypoints and verify their jstack configuration contract; installations need not be siblings. If a required dependency is missing, return incomplete and name the manual command `npx skills add juancamiloqhz/skills --skill NAME` with the missing name substituted. Do not install or replace it with an unrelated same-name skill.

## Ground

Use `how` to explain the touched subsystems, their callers, ownership and failure behavior. When redefining existing ownership or layering, also use `why` to recover the reasons for that shape. Check decisive citations and carry uncertain or contradictory evidence into the design constraints. Skip grounding only for genuinely greenfield work with no surrounding integration. Pass the same selected absolute model configuration through every helper; let the first helper's canonical resolver select it when the caller supplied none. Keep real settings unchanged.

## Sketch

Read [candidate instructions](references/runner-prompt.md), [design red flags](references/design-red-flags.md) and [rationale shape](references/rationale-template.md). Run Arena with the design task, checked grounding, acceptance checks, an owned design-output directory and an explicit design-only return. Select `architect runners` instead of `arena runners`; retain Arena's `arena cross-judge pool`. Arena owns canonical resolution, execution checks, isolated candidate contexts, one selected judge and child lifecycle. At least two configured and viable seats are required; no defaults or extra seats are invented.

Require at least two structurally distinct viable designs before accepting synthesis. Different names or parameter choices within one ownership shape do not qualify. Inherited or repeated models are allowed but do not prove diversity. Give each candidate the common requirements and candidate instructions, keeping Arena's private rubric and other candidate artifacts out of its context. Screen every candidate against the red flags before synthesis and pass concrete findings to the comparison. Prefer the design that hides the required complexity behind the smaller usable interface.

If candidates converge on one structure, retain them and explain the unmet exploration requirement. A justified reframing may assign distinct structural hypotheses in fresh tasks while preserving common requirements and the configured panel. Do not invent differences in the report or repeat an unchanged brief indefinitely. Return incomplete if no grounded alternative is viable.

## Return or agree

Inspect Arena's actual synthesis and verification. Return caller usage first, then the type sketch or module map and the rationale with its base, grafts, rejected alternatives, red-flag findings, checks and unresolved risks. Distinguish source-level design checks from executed behavior. A failed prerequisite or unverified acceptance condition remains incomplete.

At the design-only boundary return this package to the caller, which owns any later implementation. At an explicit checkpoint present it and wait. Otherwise continue only when implementation was already authorized. User feedback on the shape becomes new grounding evidence before revising the sketch. An explicitly requested adversarial review requires the actual `interrogate` dependency; report it unavailable if missing rather than claiming that Arena supplied that procedure.

## Implement and reconsider

For authorized implementation, replace the chosen sketch's placeholders with working behavior and run the task's relevant checks. Track deviations against the design. Decide whether each reflects a missing requirement, a wrong sketch or work beyond scope; update the rationale when the design changes.

Reconsider the architecture when friction forms a pattern across independent sites: repeated workarounds, escape-hatch types, unexpected shared-state locking, or callers learning internal rules. A single edge case is not enough. Re-run `how` over what exists, incorporate the new constraints and return to Sketch with fresh Arena tasks. Prefer removing unnecessary structure before adding it. Preserve unrelated user work and useful prior artifacts; discarding a design is not permission to destructively reset the checkout. If progress needs new information or authority, return the concrete blocker instead of cycling.
