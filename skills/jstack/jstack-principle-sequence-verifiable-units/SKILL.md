---
name: jstack-principle-sequence-verifiable-units
description: "Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state, check each before the next, and order delivery so the sequence proves itself to a reviewer."
---

# Sequence work into verifiable units

Order work as a sequence of small units, each ending in a state you can check, and don't advance until the current one is green.

**Why:** A break caught at the unit that caused it is cheap to localize. A break caught after a batch is buried, and you have already built further on a broken base. Sequencing those same units into a delivery a reviewer can replay turns "trust me" into "watch it go red, then green."

**Execution.** In a sweep, migration, or any run of similar edits, verify each change before starting the next. Each unit is a before/after bracket: known-good state, one change, run the check, then proceed. Establish a known baseline first so every check measures against it. Preserve existing work; use an isolated checkout when needed rather than automatically rebasing a dirty or shared branch. When a lever does the edits, the per-unit check is nearly free. Run it anyway.

**Delivery.** Stack commits and PRs in the order that proves the work. The canonical shape is the failing test first, then the fix on top. Other story orders are a subtraction before the reshape, a baseline capture before the treatment, the scaffold before the feature. Each delivery unit must pass its required checks before landing, and the sequence reads as an argument. Preserve failing-test evidence without presenting a red commit as independently merge-ready. Merging remains separately authorized.

The sequencing complement to the **prove-it-works** principle skill, which keeps each check real, and the **build-the-lever** principle skill, which makes the per-unit check cheap.

Apply within the requested scope and existing authorization, preserving unrelated work and repository constraints. Direct invocation does not activate jstack-juan-mode or change model configuration.

Discover referenced skills through the current catalog and read their advertised paths; independently installed packages need not be siblings. Verify jstack identity when available and report ambiguity. If a required helper is unavailable, report the missing dependency and incomplete procedure, continue independent authorized work, and leave installation to the user.
