# Prototype playbook evaluation

Prototype is the second internal Juan-mode playbook. It makes a design or behavioral decision through an isolated throwaway experiment, then returns observations, tradeoffs, a recommendation and the scratch path. Investigation remains read-only, and the other 21 procedures remain pending.

## Source and scope

[Complete source comparison](source-comparison.json) compares the entire new playbook and enclosing mode entrypoint with `11713c683fe4add4fd403ea880580abbc9e0875f`. Setup's full entrypoint is compared with its own `ccb5507cec1546dc88135c1139c811e6c59115ba` pin. All existing mode/setup files other than the three availability-bearing files match base `c32dcc728e03ec48ed803ee19962dbdf771f3f8f`; the existing Investigation procedure is unchanged. Licenses match their pins.

The [adaptation record](../../adaptations/prototype.md) accounts for the complete set of new differences. The six steps, no-production-planning rule, user direction choice when needed, isolated build, labeled switcher, observation requirement and handoff remain intact. The original H3 heading is preserved. Existing full-entrypoint differences retain their previous adaptation records.

The manifest still has 41 mappings. It adds three context paths and the exact external Control UI watch subtree; all source pins, decisions and the reviewed checkpoint stay unchanged. The pinned external Control UI source was inspected, but no external package equivalence or visual execution is claimed.

## Live behavioral experiment

The realistic request asks an agent to compare rejecting an entire customer upload with accepting valid unique rows and reporting rejected rows. [Raw inputs](inputs.json) contain four uploads, a design brief, required-field rules and a caller-owned draft. There is no production importer. The nonvisual direction is already set, so no moodboard or direction-selection question is needed.

[Live evidence](live-evaluation.json) preserves the exact copied steps, step states, preflight, child findings, execution records, writing records and integrity snapshots. One native How explainer completed using the configured inherited Codex selection. [Parent verification](parent-verification.json) confirms its terminal result and the 143 captured input, skill and configuration hashes. The evaluator removed the full temporary model catalog after use; its capture hash/time and actual preflight output remain, but that catalog cannot be replayed from this record.

The evaluator builds a small [Python script](artifacts/prototype.py) in owned scratch space. A single `--variant` switch selects whole-upload rejection, first-valid-row acceptance, or rejection of every conflicting duplicate group. The third variant explores a different treatment of ambiguous IDs. It executes all three variants against all four uploads and prints row-level decisions. The [raw output](artifacts/raw-stdout.jsonl) and [original final response](artifacts/final-response.md) remain byte-identical. This is an experiment, not a production importer or a benchmark. The archived script retains its original absolute fixture path; recreate the owned inputs from `inputs.json` or adjust that path in a scratch copy before replay on another machine.

[Independent parent replay](parent-replay.json) executes the actual artifact after inspecting it. Twelve literal accepted-row expectations match. Every input row appears exactly once as accepted or rejected, original payloads remain intact, and each rejection has a reason. Running one selected variant returns only its four cases. The replay matches the initial raw output exactly. These checks are external evaluation of the observed artifact; no assertion suite is added to the prototype.

| Input | Whole upload | First valid row | Reject duplicate groups |
| --- | --- | --- | --- |
| Clean | Accept rows 1, 2 | Accept rows 1, 2 | Accept rows 1, 2 |
| Duplicate ID | Accept none | Accept rows 1, 3 | Accept row 3 |
| Invalid email field | Accept none | Accept rows 1, 3 | Accept rows 1, 3 |
| Mixed conflicts | Accept none | Accept rows 1, 4 | Accept row 4 |

All fixture files, including the caller-owned draft, and the selected model file remain unchanged. Their hashes are retained in the evidence. No installation, source edit, publication or schedule change occurs inside the evaluation.

## Observed limits and misses

The initial writing check covered concrete wording, evidence and a limited string scan. A parent follow-up established that the complete Unslop scan/rewrite/self-audit had not run before delivery. The evaluator performed a late check and recorded two proposed wording improvements while preserving the original answer. The writing records remain intact; this is not an unqualified initial writing pass.

The evaluator also reports the unavailable Feature throughput checkpoint and an unperformed manual-first-unit comparison from Build the Lever. It does not claim those gates passed. No Architect phase was run because the prototype avoids production design planning and function interfaces. Two exploratory reads failed before succeeding; a displayed capabilities response was truncated, but preflight used the complete structured payload. These limits qualify broader mode compliance without changing the observed experiment results.

## Staged boundaries

[Boundary evaluation](boundary-evaluation.json) records concrete responses, step states and exact input hashes for three staged cases:

- An explanation-only request stays in Investigation without authorizing an experiment.
- Supplied screenshots do not establish visual interaction or use of the intended control skill. Missing Control UI leaves visual verification incomplete. A read-only request to compare existing images may itself belong in Investigation; the evaluator preserves that distinction.
- A build request with fixed requirements and no unresolved decision routes to Feature. Existing implementation authority persists, but the absent Feature procedure is not invented and no prototype substitutes for production work.

These cases are routing assessments, not live browser failures or Feature runs. The evaluator also checks the tension between no planning and the copied task list, and between a lower prototype quality bar and the explicit visual evidence requirement.

## Repository checks

[Validation](validation.json) records all four packaging tests, both changed entrypoint checks, actual manifest validation, Markdown lint, relative links and whitespace checks. The upstream H3 fragment uses a byte-identical temporary lint copy with MD041 disabled. The verbatim final response additionally disables MD034 because its raw fixture email values trigger the bare-URL rule; the original output is preserved. No runtime script changed; unrelated resolver suites were not repeated. No installed skills or schedules changed.

## Limits

This is an explicit-authoring-path Codex experiment, not installed discovery, cross-provider execution or persistence verification. No visual prototype, screenshots, browser interaction, open-direction research, timing/performance experiment, production implementation or Architect handoff is exercised. Prototype output does not prove durable import semantics, email deliverability, retries, storage failures or concurrent operation. External dependencies and later routes retain their existing gates.
