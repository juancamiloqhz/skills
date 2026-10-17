# Recoverable Orchestrate inbox batches

Source: `pstack/skills/poteto-mode/scripts/orch/` and `playbooks/orchestrate.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local implementation: [store.ts](../../../skills/jstack/jstack-juan-mode/scripts/orch/store.ts) and [orch.ts](../../../skills/jstack/jstack-juan-mode/scripts/orch/orch.ts). This implements the acknowledged handoff required by the [autonomy inventory](../juan-mode/autonomy-inventory.md#orchestrate), without enabling the final playbook.

## Why this differs from upstream

Upstream's queue discipline says to drain pointers, classify them, update units and ledger, then render status. Its `inbox drain` implementation removes the pointers before returning them. If the coordinator stops after that command but before recording its decisions, a new session cannot recover the unprocessed batch from the store. T3 notifications and a surviving task ID do not make that multi-command handoff atomic.

Add `inbox claim` and `inbox ack <batch> --receipt <path>` as the supported resumable handoff. Keep the original push, peek, count and drain command shapes for compatibility. A pending batch blocks destructive legacy drain. The future Orchestrate procedure must use claim/ack instead of assuming legacy drain is recoverable. This addresses a demonstrated interruption gap; it does not redesign upstream's program roles, queue classification, ledger or verification rules.

| File | Difference from pin | Requirement and verification |
| --- | --- | --- |
| `orch/store.ts` | Add batch types, one validated manifest, claim and acknowledgement operations. Reuse pointer parsing with filenames and content digests. Guard legacy drain while a batch is pending. | Preserve the exact batch across session interruption, keep later arrivals separate and resume cleanup after acknowledged deletion fails. Existing pointer TSV files and all other store formats remain unchanged. |
| `orch/orch.ts` | Add `inbox claim` and `inbox ack`, with JSON and compact output. | Actual CLI processes exercise replay, wrong IDs, required receipts and acknowledgement. Existing dependency and frontier changes remain as recorded previously. |
| `orch/inbox.test.ts` | Add 14 tests, including a killed store-holder process and real filesystem deletion refusal. | Check durable handoff and stale-lock recovery without claiming T3 child lifecycle recovery. Test repositories, stores and subprocess output are temporary. |

The [source comparison](../evaluations/orch-inbox-recovery/source-comparison.json) compares final files directly with the pin. The [runtime](orch-runtime.md) and [frontier](orch-frontier.md) records account for the inherited manual dependency check and GitHub adapter. `orch.test.ts`, frontier and watcher tests are unchanged by this work.

## Batch lifecycle

1. Claim holds the existing single-host writer lock and snapshots current pointer filenames, parsed fields and SHA-256 content digests into `inbox-batch.json`. It leaves every pointer in place. An empty inbox returns JSON `null` without creating an empty batch.
2. A repeated claim returns the same pending ID and entries. New pushes stay outside that snapshot. Changed or missing claimed files cause an error, retaining the manifest for reconciliation.
3. The coordinator records the actual classification, current task/PR/head evidence, unit/ledger decisions and any unresolved items. Its receipt should identify the batch and every pointer, including duplicates or rejected results. On replay, inspect those saved decisions before doing work again. The helper does not perform or transact these decisions.
4. Ack requires the current batch ID and an existing nonempty receipt file outside the inbox and batch manifest. It records the absolute receipt path and content digest, then atomically writes the acknowledged state before removing any pointers. A receipt is a caller's evidence reference, not proof that its contents are correct or every classification was applied.
5. Cleanup removes only the snapshot's filenames after checking their current content. If cleanup fails or the process stops partway, the acknowledged state remains. A subsequent ack or claim finishes cleanup, tolerating already removed files and preserving later arrivals. Unexpected changed files block cleanup.
6. Retain only the latest batch manifest. Repeating ack for that ID and receipt path is harmless. Once a new batch replaces it, an old ID fails without touching new work. An empty claim preserves the last acknowledgement. This is bounded retry support, not permanent event deduplication.

`inbox count` and peek still show physical pointers, including a pending batch or unfinished acknowledged cleanup. `status` continues to derive only upstream's existing unit, ledger, frontier and gate fields. Pending-batch inspection goes through claim or the readable manifest. Existing stores need no migration or initialization change; the new file appears on the first nonempty claim.

The manifest holds the active or latest batch, not an ever-growing event history. Keep real classification receipts with the program's required decision trail. A later retention pass may remove accepted task-owned evidence only when no recovery needs it. Do not delete the pending manifest or inbox files manually to get past an error. Finish or reconcile an active batch before downgrading to a version that cannot recognize it.

## Boundaries

The existing lock and atomic-rename helper are unchanged. This supports local process interruption and permission-error retry; it does not promise power-loss durability, cross-host locking or a transaction across units, ledger, receipt and inbox. External writers that ignore the lock remain unsupported. Legacy drain remains destructive when no pending batch guards it.

Claims may replay. Duplicate notifications remain separate entries. Task-ID reconciliation, stale-result rejection, verifier precedence and idempotent classification remain coordinator requirements. A nonempty receipt alone cannot grant verification, merge or dispatch authority. No subagents, schedules, installations or remote mutations run inside these commands. See the [evaluation and normal example](../evaluations/orch-inbox-recovery/README.md).
