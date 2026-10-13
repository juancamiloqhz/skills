# Engineering principle evaluation

On 2026-10-13 an independent T3-owned evaluator read the new conditional index and answered eight planning scenarios before comparing all 24 mapped principles with pinned upstream revision `11713c683fe4add4fd403ea880580abbc9e0875f`. It found all 24 unique anchors reachable and no concrete scope-expansion defect or unresolved local conflict. The parent verified the recorded source hashes before applying the correction below.

## Findings and correction

The evaluator found one low-severity omission: the structural-learning rule listed possible mechanisms without preserving upstream's preference for the strongest suitable enforcement. The parent restored that preference, scoped to applicable mechanisms, and explicitly retained runtime validation where static guarantees cannot apply. This was a source-level correction after evaluation, checked by the parent against upstream; no second independent scenario run was performed.

[Saved results](results.json) preserve the original finding, eight scenario answers, all 24 source assessments, hashes and limitations. The original audit finding is retained rather than relabeled as an independently tested pass. The raw report and inputs remain at `/tmp/jstack-principles-cf2up7hq`.

## Scenario coverage

The decisions preserved an independently deployed API consumer, reconciled an uncertain billing outcome before retry, recognized different JSON fields as shared mutation, and retained a valid empty-result test. They treated even actor counts as limited evidence, qualified a one-trial speedup, confined temporary migration failure to an isolated unit, and reused an adequate codemod for a small rename.

These are tabletop decisions and source comparisons, not executed migrations, concurrency tests, billing operations or performance measurements. Eight scenarios do not prove all 24 rules in practice. No baseline comparison, repeated trials, provider comparison or full playbook evaluation occurred. No repository or configuration writes were delegated and no child work remains pending.

Static validation checks the complete pinned name set, unique local anchors, local links, Markdown, skill format and upstream manifest. These checks establish packaging integrity, not runtime readiness. The 23 playbooks remain pending.

## Standalone packaging revision

The user requested standalone skills after the initial reference evaluation. The 24 bodies now live in independent `principle-*` entrypoints with descriptions, pinned attribution and licenses. Juan-mode retains discovery metadata only, and Figure-it-out discovers its relevant principles instead of keeping a second guidance table. The original results above describe the earlier internal-reference layout; their source paths and hashes are historical. The [fresh standalone evaluation](standalone-results.json) found no concrete defects across all 24 packages and four tabletop discovery cases. It checked direct use, juan-mode selection, Figure-it-out selection and a missing selected skill. All corrected bodies match commit `19222e0`, and the parent rechecked tested hashes. This used authoring paths as a catalog; installed discovery, automatic triggering and runtime execution remain untested. The missing-catalog case was simulated after the evaluator had read all skills.

## Inline upstream organization

A subsequent user decision requires upstream fidelity as the default for future work. Juan-mode now preserves the pinned upstream Principles section inline, including all five group names, the 24 trigger summaries and their order. Catalog discovery and scoped-authority notes are the documented additions. The separate discovery index was removed. The earlier standalone evaluation describes its then-current index path; its evidence remains historical, and no new runtime or model-based discovery run is claimed for this relocation.

The parent compared the relocated section against pinned upstream and checked all 24 skill names, local links, frontmatter and Markdown. Root AGENTS.md routes all jstack work to the new fidelity policy; CLAUDE.md imports that same instruction. Inventory checks model the root and jstack-subdirectory loading chains under default harness semantics; live provider reload was not tested. A broader fidelity audit is required before adding more playbooks and remains pending.

## Research-owned provenance

At the user's request, all 24 Attribution sections moved out of operational entrypoints into [principle adaptation records](../../principle-adaptations.md), mapped by upstream.json. Licenses remain byte-identical. Caller discovery now uses available catalog package/source metadata and reports ambiguous identity; it does not require attribution prose. Parent checks confirmed that this edit removed only attribution sections from the principle bodies. Earlier discovery reports describe the previous marker requirement and are historical evidence, not a fresh behavioral run of this metadata-based discovery wording.
