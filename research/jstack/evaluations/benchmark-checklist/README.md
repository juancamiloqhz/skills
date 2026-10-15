# Benchmark checklist evaluation

The standalone package preserves `pstack/skills/benchmark-checklist/SKILL.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. It follows merged PR #38 at `8ad4c48e1351ee2a3c6f857d56f530476e02569d`. This record separates source fidelity, actual fixture measurements and assessment of supplied evidence.

## Source and caller comparison

[compare.py](compare.py) checks the complete one-file source directory, exact package license and full final diff. It also compares Juan-mode's complete entrypoint to its pin and verifies that only two availability sentences changed since the merged base. [source-comparison.json](source-comparison.json) retains the differences and hashes. The parent inspected the complete benchmark source and remaining changes. The [adaptation record](../../adaptations/benchmark-checklist.md) accounts for invocation metadata, task scope, manual prerequisites and unavailable playbooks.

All seven questions and the one-run ballpark exception retain their upstream wording and order. No model role, saved configuration or source procedure changes. The existing Explain the Number caller already discovers the checklist by name. The manifest adds its mapping, the mode's direct dependency and the checklist's three playbook context paths; existing pins, decisions and reviewed checkpoint remain unchanged.

```sh
python3 -B research/jstack/evaluations/benchmark-checklist/compare.py > /tmp/benchmark-source.json
cmp research/jstack/evaluations/benchmark-checklist/source-comparison.json /tmp/benchmark-source.json
python3 -B research/jstack/evaluations/benchmark-checklist/check_evidence.py
```

## Independent execution

Two fresh native Codex contexts inherited gpt-6-astra and effort without overrides. Live T3 capabilities confirmed that the executing provider could run child tasks. Delegation was for skill-creator forward testing, not a new requirement of the benchmark skill. The skill itself runs in its caller and does not require setup or configured workers. [Task records](tasks.json) summarize the scoped briefs and terminal outcomes. Neither evaluator received expected verdicts or the other's results.

The runtime evaluator received [fixture.py](fixture.py), its request and the actual skill path. The fixture exports deterministic NDJSON records in memory. A constructs an encoder through `json.dumps` for each row; B reuses an encoder and calls it directly. Both use identical explicit encoding options. The request authorizes bounded local measurements and profiles with already available tools, while keeping source and settings unchanged.

The evaluator produced nine alternating samples per side for both the complete 20,000-record export and serialization alone. Four excluded warmups and two separate profile runs brought the completed correctness checks to 42. Every result matched the expected fields and bytes, with zero export or content errors. Raw wall/CPU times, profiler tables, environment observations, checks and the report are preserved in [runtime-record.json](runtime-record.json).

The observed export medians were 152.072 ms for A and 119.945 ms for B, with ranges of 146.123 to 161.819 ms and 115.440 to 134.269 ms. Profiles and process CPU time supported a single-worker encoding bottleneck. The evaluator limited the finding to the complete candidate path: constructor reuse alone did not explain the difference because B also bypasses the `json.dumps` wrapper. It compared the serialization result with the whole job and did not claim disk, network or production-service gains.

An initial evaluator script incorrectly expected literal backslash-n delimiters and failed on its first warmup. The evaluator inspected actual bytes, corrected its own expectation/parser and retained both script versions. The failed attempt contributed no comparative samples. The completed exercise took about 12.4 seconds including validation and profiles; the retained report discloses the extra failed attempt and small diagnostic calls. Source stayed unchanged. This is a recovered evaluator error, not evidence of a broken exporter or skill change.

The parent inspected both script versions, raw data, profiles and the report. [check_evidence.py](check_evidence.py) verifies archive hashes, A/B ordering, all median/range summaries and recorded error/work counts. It executes both fixture variants without timing at 2,000 and 20,000 rows, checks every field, and compares output hashes with the retained observations. [Parent checks](parent-checks.json) record the result. This replay checks output and evidence consistency; it does not reproduce the historical speed ratio or provide an independent host trace of every agent action.

## Evidence and scope cases

The second evaluator applied the skill to seven independent requests. Six supplied synthetic observations for review only. The fifth allowed exactly one real export for a user-requested ballpark. [cases-record.json](cases-record.json) retains the raw requests, full report, structured verdicts, run script/stdout and hashes. The parent wrote [expected criteria](expected.json) before dispatch and assessed the actual outputs in [assessment.json](assessment.json).

| Case | Observed decision |
| --- | --- |
| C1, lazy generator timed without consumption | Reject the speedup claim; no export work occurred inside timing. |
| C2, fast rejections and invalid successful bodies | Reject comparison despite repeated samples; it measures failures and incorrect work. |
| C3, debug/per-row commits versus release/batching | No adoption winner from an untuned side; keep the no-rerun boundary. |
| C4, repeated full-job timings without limiter evidence | Report inconclusive rather than inventing a profile-based cause. |
| C5, requested one-run rough duration | Execute one 2,000-row export, validate every field and report a ballpark with no comparison or variability claim. |
| C6, one sample per side for choosing an option | Refuse the ballpark shortcut for an adoption comparison. |
| C7, claimed savings exceed the removed step | Reject attribution of a 50 ms saving to removal of a 10 ms step. |

All seven met these bounded criteria. C5 produced 253,113 bytes with zero errors and disclosed its single-run scope. An initial `python` preparation command was unavailable; the evaluator used `python3` before the sole timed export. No source change or extra timed run was needed. These outcomes are not a statistical measure of skill reliability, and the six supplied-evidence cases did not execute actual failing workloads.

## Retained evidence and limits

Each record stores original UTF-8 file text and SHA-256 hashes under its original relative name. The runtime record includes the source/request, measurement scripts, failed attempt, raw timing arrays, separate text profiles, correctness records and report. Generated binary profiler files and C5's deterministic export are represented by hashes and sizes instead of duplicate output data. The text profiles retain the findings used in assessment; `check_evidence.py` regenerates and verifies the export. Original temporary files remain under `/tmp/jstack-benchmark-eval-20261015/`.

To replay an agent's measurement unchanged after temporary files disappear, recreate its record's `files` under `originalRoot`, inspect the stored scripts, then run the recorded command. Measurements will vary; they are never golden timing assertions. The portable parent checker needs only this evaluation directory and Python's standard library.

Package validation for benchmark-checklist and Juan-mode, Markdown lint, local-link checks, manifest validation, all 11 upstream-checker tests and source comparison pass. The global model file retains SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`. No installation, schedule or saved-model change occurred.

The evaluations used explicit authoring paths, not installed-provider discovery or automatic triggering. They do not test other coordinating providers, unavailable profilers, real storage/network services, live load-generator saturation, close-call statistics, sustained contention or all production workloads. All 23 playbooks remain pending. The invocation exception remains a documented compatibility tradeoff, not proof of explicit-only behavior.
