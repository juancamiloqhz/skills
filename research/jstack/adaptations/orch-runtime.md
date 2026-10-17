# Orchestrate runtime foundation

Source: `pstack/skills/poteto-mode/scripts/orch/` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [scripts/orch](../../../skills/jstack/jstack-juan-mode/scripts/orch). This is a dependency port, not activation of Orchestrate. The bundle still provides 22 of 23 playbook procedures.

Preserve the source module boundaries, command names, TSV/JSON formats, exit codes, verdict categories, store locking, status derivation and Graphite discovery. `store.ts` and `orch.test.ts` are byte-identical to the pin. Historical fixture names inside tests remain source examples. No additional skill, configuration role or manifest mapping is needed because the existing juan-mode mapping covers its scripts directory.

| File | Difference from pin | Requirement and verification |
| --- | --- | --- |
| `orch/orch.ts` | Import and call `checkDependencies` instead of `ensureDependenciesInstalled`. | Reuse jstack's existing manual-install boundary. Missing or mismatched Commander fails before store writes. The tool never installs dependencies or restarts itself. |
| `bootstrap.ts` | Retain the read-only exact-version check from the Babysit port; generalize its error label from watch-pr to jstack tools. | Both consumers now share the helper. The [Babysit adaptation](babysit.md) records the original substitution. Actual CLI refusal and all watcher tests passed. |
| `package.json` | Preserve the jstack package name, restore upstream's `bun test orch watch-pr`, and add strict checking of the new directory. | Existing portable identity decision and executable coverage. No dependency version or lockfile change. |
| `orch/tsconfig.json` | Add the same strict compiler settings as the pinned watcher configuration. | Include the new code and copied tests in type validation without changing runtime behavior. |

The unchanged frontier reader still invokes Graphite and resolves local branch SHAs. That is an interim dependency, not the supported Git/forge adapter required by the [autonomy inventory](../juan-mode/autonomy-inventory.md#orchestrate). Do not enable the route on this basis. Its replacement must preserve ordered PR identities and fail on ambiguous or stale topology, with separate evidence for forge reads.

The helper is bookkeeping, not an authority or task-lifecycle engine. It does not dispatch children, enforce dependency order, authenticate verifier identity, prevent an older report from replacing a newer unit, or decide whether a gate answer is authorized. Duplicate inbox pushes remain distinct. A ledger check returns an existing blocked or failed verdict with exit zero; callers must inspect the verdict. New SHA keys require their own records. A status count includes historical ledger keys and is not a count of currently verified units.

Keep one coordinator writer per local store. The PID lock is single-host and is not a distributed lease. `--force` can steal a live lock and is not a normal recovery step. Normal drain removes pointers before printing them and does not acknowledge later classification, so a crash can interrupt that handoff. These preserved source limits require an explicit drain/reconciliation design and tests before unattended Orchestrate delivery. Do not infer multi-day recovery from the dead-process lock test.

See the [evaluation and usage example](../evaluations/orch-runtime/README.md) and [final source comparison](../evaluations/orch-runtime/source-comparison.json). Source pins, reviewed checkpoint, saved models and schedules remain unchanged. No full Orchestrate program or automatic installation ran.
