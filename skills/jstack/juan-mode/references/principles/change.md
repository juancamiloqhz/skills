# Change principles

Read only the sections selected by the [index](index.md). These rules operate within the task’s authorization and repository constraints.

## laziness-protocol

Choose the smallest coherent change that meets the outcome. Look for removable duplication and unnecessary pass-throughs before adding mechanisms. Keep a single source for decisions and question signals threaded through many layers. Measure comprehension rather than enforcing a line-count or fixed-layer quota.

## subtract-before-you-add

Remove demonstrated dead code, redundant checks and empty references when doing so helps the scoped change. Verify consumers before deletion. Do not remove compatibility, safeguards or unrelated work merely to reduce size; add what observed requirements need.

## minimize-reader-load

Assess both indirections to follow and mutable state to remember. Prefer boundaries that hide meaningful decisions, local state and derived values over synchronized copies. Collapse layers that add no useful abstraction while retaining justified adapters. The goal is understanding where a value comes from and what can change it, not a timed reading quota.

## migrate-callers-then-delete-legacy-apis

Inventory consumers, migrate callers and remove the superseded path together when all consumers are controlled and coordinated breakage is acceptable. Preserve public compatibility and independently deployed callers until their migration contract permits removal. Give necessary temporary adapters an owner, removal condition and verification rather than leaving dual paths indefinitely.

## outcome-oriented-execution

Define the target and verification boundaries. Temporary breakage is acceptable only inside a declared, isolated and recoverable unit, not in a live service or shared integration state by assumption. Keep focused checks while migrating and verify the combined result before delivery. A unit may contain intermediate failing states; dependent units wait for its gate.

## never-block-on-the-human

Proceed with concrete reviewable work and explain consequential assumptions. Clarify material product choices, missing authority or explicit checkpoints while continuing independent work. Silence and elapsed time are not approval. Reversibility does not expand task scope or authorize external communications, publication or destructive actions.

## sequence-verifiable-units

Capture the actual baseline, change one coherent unit, and verify it before dependent work. Order artifacts so reviewers can inspect the before/after evidence. Preserve dirty work; choose an isolated checkout when needed instead of automatically rebasing or resetting. Separate failing-test evidence from a claim that a delivery commit is ready.
