# Six shorter principle updates

Adopt the six shorter principle bodies identified by the [coverage audit](../../coverage-audits/2026-10-18/README.md). Preserve the source descriptions, which carry triggers and instructions that no longer repeat in the bodies. These remain standalone skills.

## Source comparison

Local base is merged PR #91, `8cdf9af60b2c16d0713b59f07cac836fce05f090`. Source is `cursor/plugins` at `0148b78c56c72a1b8412055913c79f767095b217`, compared with original adaptation revision `11713c683fe4add4fd403ea880580abbc9e0875f`. Each source path is `pstack/skills/principle-<suffix>/SKILL.md`; its local path is `skills/jstack/jstack-principle-<suffix>/SKILL.md`. The [adaptation record](../../principle-adaptations.md) links the exact source files.

| Suffix | Complete disposition of the source change |
| --- | --- |
| `encode-lessons-in-structure` | Adopt removal of introductory framing, the numbered pattern, mechanism ranking, routing and anti-patterns. Keep the judgment-only fallback and structural-fix corollary. The description still directs recurring corrections into mechanisms. |
| `exhaust-the-design-space` | Adopt removal of the detailed rule and applicability lists. Keep the product-feel sentence. The description still requires two or three competing prototypes for novel decisions. |
| `guard-the-context-window` | Adopt removal of the context assertion and large-payload/inline-content bullets. Keep the reason and phase/scope budget. The description still routes bulk to helpers and summaries to the main conversation. |
| `laziness-protocol` | Adopt removal of introductory framing, deletion/three-layer/threading/leak bullets and the maintenance test. Keep decision consolidation and the smallest effective diff. The description still favors deletion over added complexity. |
| `migrate-callers-then-delete-legacy-apis` | Adopt removal of the opening rule, explicit inventory/deletion/adapters list and closing rationale. Keep contract-test guidance and applicability boundaries. The description still requires migration and deletion in one wave. |
| `type-system-discipline` | Adopt removal of the illegal-state and construction examples, casts paragraph, exhaustive-matching paragraph and partiality paragraph. Remove the same compiler-honesty clause from the description as upstream. Keep semantic brands, boundary parsing and authoritative schemas, plus the retained description's illegal-state and exhaustiveness instructions. |

All six final files match their source Git objects exactly after applying only the existing adaptations: `jstack-` names, the TypeScript helper's catalog name, omission of `disable-model-invocation: true`, list-spacing normalization, the standalone authority paragraph and Type System Discipline's helper-discovery paragraph. No deleted source prose moves into another operational file. The invocation-metadata omission remains an explicit provider-verification gap, not a newly justified difference.

The context-compaction correction is retired because upstream removed the entire assertion. The leaf's corrected time-range example is likewise removed with its upstream example. The independently corrected TypeScript helper remains byte-identical to the local base, including its nonnegative-duration guidance. All six licenses match upstream. Juan-mode is byte-identical to the base and its six corresponding summary lines match the audited source exactly. The other 18 principles, setup package, upstream manifest and reviewed checkpoint remain unchanged.

## Evaluation procedure

[Cases and expectations](cases.json) retain six design requests. For a direct-use run, provide each request and its named local skill. For a selection run, provide the requests without the `directSkill` and `expectations` fields, the exact `## Principles` section from Juan-mode and an authoring catalog mapping skill names to absolute paths. Let that agent select and read the relevant leaves. Both runs can resolve the TypeScript helper through the catalog.

Use fresh agents without parent history. Withhold the expectations, other run's answers, diffs and earlier evaluations. Allow reads of the selected skills and required helpers, but no network, implementation, installation, configuration writes or nested delegation. Each agent writes only its own scratch report. Inspect actual answers and skill reads against the retained expectations. This procedure tests principle use and selection, not full Juan-mode activation or playbook execution.

## Observed results

Ran both conditions on 2026-10-19 with two fresh native Codex agents using inherited gpt-6-astra/high. Each handled all six requests in one context. The parent inspected both reports. Both met the two recorded expectations for every request; the selection run chose the intended updated leaf in all six cases and also used relevant companion principles.

| Case | Direct-use result | Selection result |
| --- | --- | --- |
| Recurring corrections | Proposed an enforced payment import boundary and a prominent tone instruction with a failure example. | Selected Encode Lessons in Structure and made the same enforceable-rule versus judgment distinction. |
| Novel UI | Compared three distinct sketches, then provisionally chose a shared form with exceptions. | Selected Exhaust the Design Space, compared three sketches and deferred interaction claims until prototype testing. |
| Context budget | Proposed bounded helper slices, short summaries, evidence locations and explicit phase/file limits. | Selected Guard the Context Window and proposed bounded slices with a compact evidence ledger. No helpers were launched. |
| Duplicated decision | Centralized permission calculation and passed a boolean instead of introducing a framework. | Selected Laziness Protocol and proposed the same small change with visible-behavior checks. |
| API migration | Proposed migrating callers and removing the old internal path while retaining the required public v1 boundary. | Selected Migrate Callers Then Delete Legacy APIs and respected its external-compatibility exception. |
| Types and ranges | Read the TypeScript helper and its patterns; proposed distinct IDs, parsed boundaries, schema-derived types, exhaustive variants and negative-duration rejection. | Selected Type System Discipline, read the same helper and preserved the nonnegative-duration invariant. |

The results demonstrate these design decisions under supplied prompts. They do not establish executable application correctness, full dependency execution, automatic skill discovery, context compaction or provider-wide behavior. The selection run proposed tools under Build the Lever but correctly left their construction unexecuted within the design-only task. Both UI answers supplied word sketches, not tested interactive prototypes. Neither ran a compiler or application tests. There is no baseline condition, statistical success-rate claim or attribution of the answers solely to these six leaves. Cases share context within each run.

Protected-file hashes remained unchanged during the exercises. Raw reports, prompt-only copies and the temporary catalog stay in task-owned cache. Only this report and the compact prompts/expectations are retained in the repository. No installed copies, model configuration or schedule changed.

## Package checks

Four packaging tests, six skill validations, the documentation consistency check and whitespace checks pass. Complete normalized source comparisons, license identity and unchanged-file checks also pass. The documentation checker reports 45 skills and 23 playbooks with zero problems; guide coverage remains pending. All relative links in this report and the updated adaptation record resolve.

Run the existing checks from the repository root:

```sh
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
git diff --check
```

Also run the host skill creator's `scripts/quick_validate.py` on each of the six packages. Compare entire files against the source Git objects using only the documented adaptations above; a passing package check alone does not establish fidelity.

## Normal use

After merge and a manual skill update, ask `jstack-principle-exhaust-the-design-space`: "Compare approaches for bulk-editing inventory, including per-item exceptions." It still calls for two or three alternatives before choosing. With Juan-mode active, its existing principle list can select the same skill for a novel interaction. Direct invocation does not activate Juan-mode.
