# Upstream attribution

The 2026-10-15 correction restores the six original phases, separate Cross-judge and Pick sections, Outputs, source description and four principle routes. It also restores proceeding after a candidate dropout. The [source comparison and evaluation](../evaluations/arena-restoration/README.md) distinguish this correction from the [historical Arena evaluation](../evaluations/arena/README.md). The [original audit](../fidelity-audits/2026-10-13/helpers.md#arena) remains unchanged.

Adapted from [pstack arena](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/arena/SKILL.md) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The bundled [MIT license](../../../skills/jstack/arena/LICENSE) retains Lauren Tan's attribution.

## Complete comparison

The source directory contains only `SKILL.md`; its full diff and the unchanged MIT license are recorded in the comparison.

| Source location | Difference and concrete reason | Verification or limit |
| --- | --- | --- |
| Frontmatter | Retain source description but omit `disable-model-invocation: true` for catalog-based callers, including Architect. The existing [invocation compatibility assessment](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) applies. | Automatic selection remains possible. Full installed-provider discovery remains unverified. |
| Opening | Replace todolist with the host task plan. Add task-scoped invocation, caller return boundary, acceptance checks and execution-reference pointer. | T3 tools and existing task authority govern execution; authoring the skill does not activate Juan-mode. |
| Principle references | Restore separate-before-serializing-shared-state at output allocation, Laziness Protocol at the tie-break, redesign-from-first-principles at grafting and prove-it-works at verification. Use actual standalone `principle-*` names and catalog or explicit-source discovery. | Source comparison preserves all four decision points. Missing required packages are reported for manual installation. The manifest watches these dependencies. |
| Frame, item 3 | Replace Cursor rule/default slugs, automatic added runners and rejected-model fallbacks with canonical setup resolution and fixed configured seats. Architect may select its configured panel. Require at least two configured candidates to start; an insufficient saved panel is not permission to add seats. | Saved selections and the 2026-10-15 whole-map validation decision take precedence. Rejections may refresh discovery but never silently change models. |
| Frame/Cross-judge | Check judge eligibility before candidate work; refresh and select one judge after candidates finish. Preserve different-family preference and disclose inherited/same-family judging. Only an explicit caller requirement makes diversity mandatory. | Avoids spending candidate work when no configured judge can execute. Inheritance does not establish family diversity. |
| Frame, item 4 | Use T3-owned `isolation: "worktree"` for a separate checkout, with committed parent baseline; use owned temporary directories for design/text. Prompt paths do not bind workspaces. | Current host contract, not a claim that a code-worktree run was exercised here. |
| Fan out | Replace Cursor `run_in_background` and same-message dispatch with native/T3 asynchronous dispatch under actual capacity and established path ownership. Preserve the common task, grounding, artifact and rationale; fresh contexts exclude the rubric and other candidates. | Conditional serialization protects shared writes, not a permanent serial redesign. Actual host capacity constrains concurrency. |
| Fan out, dropout | Restore source N-1 continuation. Ordinary Arena may judge and verify its sole survivor, reporting that comparison was unavailable. No survivors is incomplete. Explicit caller requirements still apply. | Removes the previous unapproved blanket two-survivor stop. Architect still requires two structurally distinct designs; its caller sentence now owns that requirement. A one-survivor artifact is not a successful comparison. |
| Cross-judge/Pick | Preserve one read-only judge after frozen outputs, concurrent coordinator reading, per-criterion scoring and disagreement inspection. Keep identity mapping out of the judge brief and forbid judge edits/synthesis. | Labels are a presentation boundary, not guaranteed anonymization. Terminal/nested checks prevent judging while candidates write. |
| Graft | Preserve graft, convergence and reframe rules. Keep originals intact and synthesize separately. Coordinator owns synthesis unless the caller already supplied a role. Replace unqualified "ship" with delivery within existing authority. | No implicit implementation, PR, merge or installation. Fresh retries use the same panel and corrected common brief; unchanged retries stop when they cannot progress. |
| Verify | Keep source rerouting to Frame or Graft after failure. Add concrete acceptance checks and distinguish design traces from executed code behavior. | Missing prerequisites make verification incomplete; source inspection cannot prove runtime behavior. |
| Outputs | Preserve every source synthesis-note item. Add comparison/disagreement evidence, task IDs, artifact retention, temporary-catalog cleanup and terminal write reconciliation. | Makes T3 child work reviewable within the requested scope. |

## Supporting files and caller

`references/execution.md` has no upstream file equivalent. It supplies the necessary T3 catalog, complete-map lookup, explicit selected-path handoff, provider eligibility, inheritance, fresh-task lifecycle, complete-brief checks and owned-write constraints. The correction updates only its separate-checkout instruction to the actual `delegate_task` isolation contract. No configuration code, saved settings or model assignments change.

Architect's one changed sentence identifies two viable candidates as its own requirement rather than Arena's universal post-dropout rule. Its source already requires two structurally distinct designs; that requirement and the rest of Architect remain intact. See the [Architect record](architect.md).

The exact source pin and reviewed checkpoint are unchanged. Historical evaluations remain tied to their original versions. Swarm and the remaining fidelity backlog are separate work.
