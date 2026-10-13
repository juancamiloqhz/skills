# Principle restoration evaluation

On 2026-10-13, restored the bodies of all 24 principles from `11713c683fe4add4fd403ea880580abbc9e0875f`. The [current adaptation record](../../principle-adaptations.md) identifies every shared difference and seven narrow substantive exceptions. Existing automatic invocation metadata remains an unresolved separate provider question. Missing helper dependencies remain visible.

## Source and package checks

[compare.py](compare.py) reads each exact manifest pin from the shared bare Git cache, compares it with the shipped entrypoint, and checks the package license against that pin. [source-comparison.json](source-comparison.json) captures all 24 source/local hashes and unified differences. The parent inspected the remaining differences. Seventeen bodies have only the documented packaging, scope, dependency-discovery and formatting differences; seven also have the listed substantive exceptions. Source descriptions and original section order are restored.

```bash
python3 -B research/jstack/evaluations/principle-restoration/compare.py > /tmp/jstack-principle-source-comparison.json
```

All 24 skill validations and Markdown lint checks passed. Manifest validation passed with explicit context paths for restored dependencies. The reviewed checkpoint and source pins are unchanged. These checks establish recorded source differences and package integrity, not semantic equivalence or runtime reliability.

## Forward exercises

Two separate inherited-model agents applied the restored skills to bounded requests in disposable workspaces. They inherited conversation context, so these are independent execution exercises, not blinded experiments. Neither changed repository files or configuration. The parent inspected their code, reports and output, then reran both fixtures successfully after making only the runners portable and tightening per-fixture diagnostic checking.

| Exercise | Actual observed result | Limits |
| --- | --- | --- |
| Evidence and retry | A fresh heartbeat remained after its process stopped. The agent rejected an unsupported no-causality conclusion from equal counts and an unverified 2x benchmark claim. A deterministic export recovered at four injected crash boundaries, with two successful retries each. | Synthetic count inputs; no real performance benchmark. Required benchmark-checklist was absent, so that procedure stayed incomplete. Single-writer local process crashes only; no PID-identity, power-loss or external-effect proof. |
| Domain, types and shared state | Five public-interface Rust tests passed. Four invalid programs failed compilation with individually checked diagnostics. Covered contradictory lifecycle states, distinct IDs, partial head versus total sum, absent/present search, permission revocation before execution, and two workers publishing separate files concurrently. | Rust was available; TypeScript compiler/helper was unavailable. Threads and final file content only; no distributed authorization, cross-process ownership or durability proof. The exhaustive-match fixture omits an existing variant; it does not simulate an API release. |

Original reports: [evidence](evidence/report.md) and [design](design/report.md). Original output is retained in their directories. [parent-results.json](parent-results.json) records the parent reruns and final source hashes. Local reports name the original temporary workspaces; the committed fixtures below are the portable reproduction paths.

```bash
python3 -B research/jstack/evaluations/principle-restoration/evidence/check.py
bash research/jstack/evaluations/principle-restoration/design/run.sh
```

Both commands use temporary state and clean it after execution. The evidence check prints JSON without rewriting retained results. The design runner requires an existing Rust compiler and `rg`; it installs nothing. Expected outputs and diagnostic classes are checked independently of the subject implementation. These are illustrative test applications, not production libraries.

## Coverage limits

Behavioral exercises applied nine selected principles; they did not execute every restored rule. Source fidelity was checked across all 24. The exercises do not prove installed catalog discovery, automatic invocation, juan-mode persistence, all-provider support, performance reliability, production crash consistency or the missing helper procedures. Other principles' restored heuristics, migration sequencing, context compaction and broad design workflows still lack fresh runtime exercises.

No skill installation, merge, model change, schedule change or external communication occurred in these exercises. The tests justify their bounded results. Broader fidelity corrections remain on the roadmap.
