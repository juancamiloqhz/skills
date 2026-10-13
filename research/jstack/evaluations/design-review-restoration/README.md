# Design and review restoration evaluation

Architect, Interrogate and Reflect are restored from `11713c683fe4add4fd403ea880580abbc9e0875f`, the unchanged manifest pin. This continues the fidelity audit after merged PR #30, whose main commit is `34cbcca75dabd8d58e1d2b0945f6d550cfa572c7`. The correction restores fourteen source files, including eleven references, and removes two local summaries that had replaced source procedures.

The [Architect](../../adaptations/architect.md), [Interrogate](../../adaptations/interrogate.md) and [Reflect](../../adaptations/reflect.md) records account for every remaining difference. Configured model roles, actual task authority and supported host tools replace incompatible upstream defaults. Existing jstack execution contracts remain unchanged. The three entrypoints retain the catalog-invocation metadata exception established in PR #30; automatic selection remains possible.

## Source comparison

[compare.py](compare.py) reads each component's exact manifest pin from the shared bare upstream cache. [source-comparison.json](source-comparison.json) stores complete diffs and SHA-256 hashes for all fourteen mapped files, the two unchanged local execution references and both removed summary paths. All three package licenses match the pinned plugin notice. The parent read every diff, including source templates and formatting changes.

```bash
python3 -B research/jstack/evaluations/design-review-restoration/compare.py > /tmp/jstack-design-review-comparison.json
cmp research/jstack/evaluations/design-review-restoration/source-comparison.json /tmp/jstack-design-review-comparison.json
```

The manifest adds context watches for Architect's Interrogate dependency and referenced standalone principles. No source pin or reviewed checkpoint advances. Historical reports remain unchanged. [Parent checks](checks.json) record validation, local link resolution, protected-file checks and skill hashes. Static checks establish package integrity, not behavioral equivalence.

## Bounded forward exercises

Three fresh-context native Codex evaluators received a realistic request, final skill files and synthetic raw artifacts. The parent wrote [expected cases](cases.json) before dispatch and withheld them, prior conclusions and other evaluation directories. No model or effort overrides were supplied. Each evaluator could write only its assigned temporary findings file; source, repository and configuration stayed read-only. All three reached terminal completion and the parent inspected their actual outputs.

[Fixtures](fixtures) preserve the exact supplied inputs with [hashes](fixture-hashes.json). Absolute paths inside them refer to the original `/tmp/jstack-design-review-eval/` workspace; the equivalent files live under the matching fixture subdirectories. Reflect's target skill bodies and transcript are inline fixture data. [outputs.json](outputs.json) retains all three reports as unchanged strings, including caveats. [evaluation.json](evaluation.json) records task identities, configuration resolution, output hashes and the parent's assessment.

| Exercise | Observed result | Scope |
| --- | --- | --- |
| Architect | Used caller-first domain signatures and actor/kind indexes, kept wire types private, merged per-actor state at reads, removed internal duplicate paths and hand-synced lists. Repeated casts in separate modules triggered the ordered Scrap response. Returned design-only and retained checkpoint authority. | Applied runner, red-flag and rationale templates plus the Scrap decision to two supplied candidate sketches and a hypothetical diary. No independent candidates or Arena synthesis claimed. |
| Interrogate | Retained every supplied reachable defect, including singletons, and recommended removing five pass-through wrappers. Grouped the two ownership defects, producing seven blocker groups. Dismissed the unconditional file split, premature compatibility deletion and alleged unchecked-key crash. | Reviewed a small Python source file and reconciled all thirteen claims in a synthetic reviewer packet. Generated-file and external-client facts were supplied context, not separately inspected code. No fixture execution claimed. |
| Reflect | Accepted three supported singleton recommendations: fill a body gap, move buried trace guidance and tune a missed description trigger. Rejected clear existing guidance, drifting specifics, a platitude and injected authority. Recorded existing validation as already-enforced Backlog without new prose or tickets. | One evaluator applied the tooling lens and synthesized three prerecorded reports. It did not run the production three-lens/separate-synthesizer orchestration or mutate target skills. |

These exercises passed their bounded checks. They give evidence that the restored criteria affect decisions; they do not establish full workflow completion or upstream equivalence. Parent conclusions are manual assessments, not a numerical benchmark or a comparison against baseline agent runs.

## Configuration and remaining limits

A fresh full capability response was used with the canonical model resolver. All four relevant roles resolve to `[null]` using the existing global config, preserving inherited provider, model and effort. The config's SHA-256 remains `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`. The first capabilities response was accidentally printed in full and its display truncated; the second response was retained intact for validation. The temporary full catalog is not checked in.

Architect currently has one configured runner. Arena requires at least two viable configured candidates, so a complete Architect/Arena execution was not possible without changing settings or inventing a seat. Neither was done. Restoring these procedures does not resolve Arena's separate fidelity findings.

Full orchestrator dispatch, installed catalog discovery, cross-provider execution, failure/cancellation handling, runtime builds and implementation are unverified for this version. Source references in the fixture are supplied evidence rather than live connector calls. Earlier evaluations remain historical evidence tied to their original files. No configuration, installation, schedule, source pin or external project record changed during testing.

Next in the audit order is standalone show-me-your-work and Figure it out, followed by generator/maintenance and the remaining foundation/orchestration corrections.
