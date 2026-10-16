# TypeScript helper evaluation

Date: 2026-10-16. Base: `39da90d4d922be87e24bbbd0a8346ad81a8a4b84`, the merge of PR #42. Upstream pin: `11713c683fe4add4fd403ea880580abbc9e0875f`.

## Source comparison

The complete upstream package contains `SKILL.md` and `references/patterns.md`. Both retain their rule/heading order and examples. [compare.py](compare.py) records full source diffs and hashes in [source-comparison.json](source-comparison.json), verifies the MIT notice and the exact principle-caller name substitution, and checks existing manifest mappings, pins, decisions and checkpoint. The parent inspected those diffs against the [adaptation record](../../adaptations/typescript-best-practices.md).

Beyond naming, invocation metadata and task/dependency boundaries, the changes correct demonstrated type/example claims. They do not introduce a new domain model or runtime library. Primary references are TypeScript's [unchecked indexed access](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html) and [satisfies documentation](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html).

## Compiler and runtime exercise

Fresh native evaluator `/root/typescript_examples_eval` received the actual helper and full patterns file, with permission to write only its temporary evaluation directory. It used existing TypeScript 6.0.3, Node v24.19.0 and cached Zod 4.6.5. No installation was performed. The skill-creator forward-testing procedure authorized this independent evaluation; fresh live capabilities identified inherited Codex `gpt-6-astra`, with no model/effort overrides.

The initial pass covered all 18 TypeScript code fences in 27 separate snippet files. It supplied explicit minimal definitions for the source's omitted helper/types and split Don't/Do declarations into separate scopes. All recommended snippets compiled with `strict` and `noUncheckedIndexedAccess`. Expected-negative cases exercised brand mixing, empty/non-pair values, missing discriminated payloads, unchecked unknown access, incomplete schemas, unhandled variants, literal inference and argument order. Runtime groups exercised validation and selection, including demonstrations of unsafe examples.

The pass exposed three further qualifications, which were corrected before the final recheck:

- A length-only guard accepted a typed sparse array without a first element. The shipped guard now also requires index 0 to exist and states validation/mutation assumptions.
- `satisfies` retained the theme literal in the example but inferred numeric `cols` as `number`, not literal `3`. The text now describes inferred-type retention rather than universal literal preservation.
- Swapping the shown string and options-object arguments already failed compilation. The misleading comment was replaced while retaining both object-argument examples.

[examples-evidence.json](examples-evidence.json) retains the exact initial/final reports, generated cases, scripts, command results and limitations under original relative paths. It omits dependency links and emitted build files. Failed test-generator attempts remain recorded. The final recheck follows the source corrections; initial limitation demonstrations are not presented as failures of the final guard. After that recheck, only the entrypoint table separator spacing changed to satisfy repository lint. The validation record verifies this exact mechanical difference against the tested snapshot; patterns.md still matches the tested hash.

The parent independently compiled the original random-index body, the corrected fallback, and negative/nonfinite numeric durations. [counterexamples.json](counterexamples.json) records the expected TS2322, successful fallback and acceptance of invalid durations by plain `number`. The parent also extracted the final guard and selector directly from the shipped patterns file. [replay.json](replay.json) records successful strict compilation and seven assertions covering empty/sparse rejection, dense/singleton selection and fallback to a known head.

## Principle-to-helper review exercise

Fresh native evaluator `/root/typescript_review_eval` received a findings-only request through Type System Discipline: review optional-field state, a negative duration, an empty-safe sum, random non-empty selection and an unchecked cast of external JSON. The project context supplied strict indexing, existing Zod and a requirement to preserve `sum([])`. No expected answer was supplied.

The evaluator followed the exact principle pointer to the new helper, read its patterns and relevant principle leaves, and reused the already-read calling principle without recursion. It proposed a discriminated union, actual schema parsing, finite/nonnegative boundary validation and the indexed fallback. It correctly kept the empty-safe sum on `number[]`, avoided a new schema dependency, and returned findings without project edits.

Its original example produced the expected indexing error and demonstrated unchecked-data failure. Proposed examples compiled and passed runtime checks. Four negative compiler cases rejected missing payloads, conflicting object-literal payloads, an empty selection input and an unhandled state variant. [review-evidence.json](review-evidence.json) retains the findings, exact traversal, proof inputs and commands. This exercise preceded the final sparse-guard/comment qualifications; those changes were verified by the example recheck and parent replay, not a second claimed caller run.

The review recorded that the adaptation file did not exist when it was read during concurrent authoring. That observation is retained. The completed adaptation and parent source comparison now supply provenance; the failed read did not block operational helper discovery.

## Reproduction and repository checks

From the repository root:

```sh
python3 -B research/jstack/evaluations/typescript-best-practices/compare.py
python3 -B research/jstack/evaluations/typescript-best-practices/replay.py
python3 -B scripts/jstack/test_skill_packaging.py
python3 -B /home/ubuntu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/jstack/jstack-typescript-best-practices
```

The comparison uses the shared upstream Git cache, overridable with `--cache`. Replay uses an existing compiler path, overridable with `--tsc`, and creates fresh temporary files. Retained delegated scripts use original absolute output/dependency paths; inspect them before replaying in a new owned directory. They are evaluation artifacts, not production package scripts.

[validation.json](validation.json) records the real manifest loader, packaging/frontmatter checks, Markdown lint, relative links and whitespace checks. No model resolver changed, so unrelated model suites were not rerun.

## Limits

These are bounded authoring-path tests with one inherited provider/model, not installed discovery, cross-provider support or full playbook execution. Minimal scaffolding and one cached Zod/compiler version do not prove every project's framework, generated types, compiler options or schema version. No JSX/UI, framework leak/disposable behavior, telemetry, parser-specific unknown-field policy, persisted-JSON migration or allocation benchmark was run. Mutable tuples and Date objects can lose invariants after construction; the skill does not make unchecked mutation safe.

The global model configuration remains unchanged, with SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`. No installed skills or schedules changed. Merging and manual installation remain separate from this port.
