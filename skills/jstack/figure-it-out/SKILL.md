---
name: figure-it-out
description: Design and follow an auditable workflow for a multi-part task when no narrower procedure fits. Use for an explicit figure-it-out request, a large migration needing a custom plan, or a workflow caller requesting task-specific phases.
---

# Figure it out

Design the workflow before changing the product. Scale its gates to the consequences, then verify each unit against the requested outcome. Direct invocation is task-scoped and leaves juan-mode activation unchanged. This helper does not make an unavailable named playbook executable. Read [principle adaptations](references/principles.md) when framing the workflow.

## Frame the task

Inspect the relevant source, current status and existing verification. Preserve unrelated changes. Identify the requested deliverable and delivery authority, including planning-only requests and explicit checkpoints. Reuse a narrower available procedure when it covers the task instead of composing another workflow.

State a falsifiable completion predicate, the approximate units of work, dependencies and unresolved assumptions. Give estimates as ranges with their basis, not guarantees. Choose rigor through concrete gates and artifacts: a reversible internal change can use focused checks; a data migration or difficult-to-reverse decision needs recovery evidence and stronger review. Record an observation limit as unknown rather than inventing a baseline.

Present framing and tradeoffs before a long run. Honor a requested checkpoint and clarify material unknowns that affect scope. Continue authorized independent work while awaiting answers. Existing authorization covers routine reversible steps; elapsed time supplies no approval. A multi-hour or materially expanded run needs its scope and resource commitment settled before execution.

## Design the workflow

Write a phase list with each unit's hypothesis, owned files or artifacts, prerequisites, observable check and recovery action. Sequence the riskiest unknown early, establish the data contracts and needed verification before dependent features, and keep units independently reviewable. Capture pre-change behavior with the same measurement that will evaluate the result. Reuse existing checks when adequate; add a harness only for a real verification gap.

For a consequential unresolved architecture choice, discover jstack `architect` through the skill catalog and request its design-only return. Verify its jstack setup contract and pass the selected absolute config when one has been chosen. A missing required helper makes that phase incomplete; provide `npx skills add juancamiloqhz/skills --skill architect` for manual installation. Concrete mechanical work needs no design tournament.

Decide whether any work can run independently. Read [execution](references/execution.md) before delegation. A custom plan does not imply a particular worker count or authorize new model assignments. Name ownership and integration checks; keep shared plans and decision records parent-owned.

For a planning-only request, return the phase list, rigor, verification design, assumptions and open decisions here. Do not implement a unit or launch implementation workers. Otherwise place the designed units in the working plan and execute within the existing task authority.

## Execute and measure

Before the first execution unit, start the [decision trail](references/decision-trail.md). Each unit states its hypothesis, makes the smallest useful change, and measures the actual artifact. Record VERIFIED, NOT VERIFIED or INCONCLUSIVE with the check and evidence. A successful build or worker summary alone cannot prove the product predicate.

Keep a change when evidence supports it. If it fails, diagnose the observation method as well as the change; recover only the unit's owned changes and preserve other work. Record a justified pivot or corrected gate separately. Do not weaken the expected behavior to turn a failure green. Dependent units wait for a verified prerequisite; independent authorized units may continue with the gap explicit. Bound retries by new evidence and surface an unresolved blocker instead of looping indefinitely.

Check delegated artifacts before accepting them. A worker's self-report is not its judge. Use a separate reviewer for consequential delegated work, with the configured judgment role, and independently inspect decisive evidence in the parent. Recurring mechanically preventable mistakes warrant a scoped test, validator or other concrete follow-up, not an automatic expansion of the task.

## Verify and hand back

Check the combined product against the original predicate through its real interface, including integration behavior and recovery where required. Audit the decision trail against the bounded run evidence and follow its review procedure. A missing check, unavailable reviewer or inconclusive result stays visible; do not report full verification.

Return the designed workflow, rigor and reason, decision-trail path, verified outcomes, failed or unverified checks, and remaining work. Report review limitations and flags. PRs, merges, installation, external messages and recurring schedules follow their own applicable task authorization. This skill supplies no automatic authority for them.

The [upstream record](references/upstream.md) identifies the source and intentional differences.
