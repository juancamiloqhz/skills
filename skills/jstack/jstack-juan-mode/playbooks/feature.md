### Feature

**You own the design. Plan, review, verify.** Delegate implementation. Stay in the lead.

1. `jstack-how` over the affected subsystem. Discover the helper and pass its configured roles, source scope and selected absolute configuration through the mode's preflight.
2. `jstack-architect` for parallel design exploration, returning a design before step 4. Preserve its configured panel, two structurally distinct candidate requirement and Arena judging. An undersized panel or unavailable helper leaves this step incomplete; do not add seats or proceed as if design exploration passed.
3. Write the throughput checkpoint as four todo items. A dimension that genuinely does not apply (single file, no fan-out) keeps its item with `n/a: <reason>` rather than being dropped:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target (the **jstack-principle-separate-before-serializing-shared-state** principle skill). Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
4. Delegate code-writing to a subagent using the configured `feature, refactoring` role, or `hardest tasks` when warranted by the mode's difficulty rule, with a specific scope (file paths, named data shape and its organizing structure per **jstack-principle-model-the-domain**, a state machine over scattered booleans, a table/registry over branching, a typed model over repeated shape assumptions, chosen before the delegate writes logic, and success criteria). When the implementation admits multiple valid shapes (error handling, abstraction layer, test structure), delegate via the **jstack-arena** skill instead so the runners surface the alternatives and the cross-judge guards the pick. Mandatory: no skip-with-reason escape, and Laziness Protocol does not override it (the gain is review separation, not lines saved). A subagent forbidden to spawn satisfies this by owning the diff directly with the same review separation. No "standing by" reply that waits on a nested agent. Comments per **Comments**. Surgical edits, re-ground against the source for upstream-derived files. Port shared-primitive improvements to all consumers and verify each. Resolve every dispatch through the mode's preflight and preserve the selected absolute configuration, with no fixed-model fallback. Commit liberally within existing authority.
5. Verify on the matching surface. "Inconclusive" or wrong-surface is not a pass. Flag it. Discover the matching control helper, including `jstack-control-cli` for terminal apps. Inspect the delegated diff and run the public acceptance checks yourself; retain actual output and unmet prerequisites.
6. Rebase into small, ordered commits. Stack follow-ups.
   Use the **jstack-principle-sequence-verifiable-units** principle skill, building, verifying, and committing each small unit before the next. Commit, rebase and publish stacks only within the task's authority and preserve unrelated work. For uncommitted local delivery, retain verified artifacts and the proposed order.
7. If the design is contested, `jstack-interrogate` before shipping.
8. Run **Opening a PR** when publication is authorized. Read and follow [Opening a PR](opening-a-pr.md). Preserve local-only delivery and existing publication authority. This playbook does not authorize merging or installation.

Code-coupled work (one feature, one migration) goes to a single owner with the checkpoint inline. That owner fans out internally after the blocking phase. Parent-level fan-out is for slices that produce independent artifacts (audits, cross-subsystem investigations, competing experiments). Rewrite the checkpoint at phase boundaries. Spawn a fresh owner rather than chaining interrupts.

**Reply:** what you built, what you chose and why, the throughput checkpoint, open decisions. Tables for design alternatives.
