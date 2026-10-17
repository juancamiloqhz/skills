# Recoverable inbox evaluation

A coordinator can now read completion notices without deleting them first. It explicitly acknowledges a batch only after saving its decisions. A resumed session can recover a pending batch, and a failed deletion can finish after the acknowledgement has been recorded.

Source pin is `11713c683fe4add4fd403ea880580abbc9e0875f`; local base is merged PR #71, `236a075e5253748cdd61ff9a91c7ef8ddc2b31e7`. The [adaptation](../../adaptations/orch-inbox-recovery.md) explains the additive commands and the [source comparison](source-comparison.json) identifies final files and inherited differences. Orchestrate remains unavailable, with 22 playbooks shipped.

## Results

On 2026-10-17, Ubuntu Linux as a non-root user, Bun 1.4.2 and Python 3.14.4:

- All 97 executable tests passed: 14 new inbox tests, 12 retained upstream store/CLI cases, 23 frontier cases and 48 watcher cases. The new tests exercise reopened stores, idempotent initialization, stable replay, later arrivals, acknowledgement retries, wrong batch IDs, duplicate notifications, missing/empty receipts, modified or missing claimed files, malformed manifests and actual CLI processes.
- A real child process claimed a batch and held the store lock. Another writer failed while it lived. The test killed the holder with SIGKILL and waited for its exit; a new store handle recovered the stale lock and returned the identical batch. The unit remained pending until explicitly changed; reading or acknowledging notices did not complete it.
- A real directory-permission refusal stopped deletion after the acknowledged state was saved. Restoring permissions and reopening the store completed cleanup. A second case combined this real refusal with a manually removed first pointer to model a partial cleanup, then proved recovery preserved a later arrival. This models the partial-deletion state; it is not a precisely timed kill during the unlink loop.
- Both strict TypeScript projects passed with available TypeScript 5.9.3 and bun-types 1.4.2. The locked development environment with TypeScript 7.0.2 and bun-types 1.3.14 was not installed or tested. Tests ran from an exact isolated source copy with existing cached Commander 14.0.0.
- The previous [six-part CLI exercise](../orch-runtime/exercise.py) and all four packaging tests passed. Units, verdicts, legacy drain, gates and dependency refusal retain their existing behavior. The focused and complete test runs had no unexpected failures; permission failures are intentional assertions.

Changed-document Markdown lint, relative-link checks, final source hashes and `git diff --check` passed. The TypeScript source matched the tested copy, and the saved model configuration hash remained unchanged.

These are executable tool checks, not prompt evaluations. No workflow activation, model changes, installation or T3 subagent dispatch occurred. The killed process was a disposable local store client, not a provider session. Full T3 task reconciliation, stale-result acceptance and unattended coordinator restart remain unverified.

## Reproduce

With Bun and declared dependencies already available, run from the repository root:

```bash
bun test skills/jstack/jstack-juan-mode/scripts/orch skills/jstack/jstack-juan-mode/scripts/watch-pr
python3 -B research/jstack/evaluations/orch-runtime/exercise.py
```

The permission-refusal tests require a non-root account on a filesystem that enforces Unix directory permissions. The process-interruption test requires SIGKILL. Run `bun run typecheck` from the bundled scripts directory. Dependency installation remains a separate manual action. Tests generate and remove only their own stores and process fixtures.

## Normal use

Suppose a subagent finishes the backend work while the coordinator is busy. The coordinator records its completion notice and later starts processing the notices. If the session stops before it saves the decision that the backend needs verification, the new commands retain that notice for the next session.

You can ask:

> Process the saved completion notices using recoverable inbox batches. Record what each result needs next before acknowledging it. Leave PRs open.

After an interruption:

> Recover the pending batch, compare it with the decisions already saved, and continue the unfinished processing.

This is a bookkeeping helper for the future Orchestrate workflow. It does not automatically capture T3 events, review a result, dispatch another agent or prevent a caller from repeating its own side effects. The caller must check the real task and current artifact before accepting a result.

With an initialized owned store, the command sequence is:

```bash
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /path/to/store --json inbox claim
```

The output contains the batch ID and its full pointer list. Inspect and classify every pointer, save the resulting unit/ledger changes and a durable receipt, then use that returned ID:

```bash
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /path/to/store --json inbox ack <batch-id> --receipt /path/to/classification.md
```

The receipt should identify the batch and each pointer, its classification and evidence, the saved state changes and anything still unresolved. Ack checks that the receipt exists and is nonempty and records its hash. It does not validate the report's truth or completeness. If claim replays a batch, first reconcile what the previous session already recorded; do not blindly repeat changes.

## Limits and retained evidence

The single manifest holds the pending or latest acknowledged batch. Existing pointer, unit and ledger formats remain unchanged. Legacy drain still consumes notices immediately when no pending batch exists. Pending batches block that destructive command. Power loss, multiple hosts and writers that bypass the store lock remain outside the tested contract. This is not exactly-once processing or permanent notification deduplication.

The next step is coordinator reconciliation of task IDs, duplicate and stale reports, and verifier precedence before enabling the full playbook. Source pins, reviewed checkpoint, licenses, lockfile, saved model configuration and schedules remain unchanged. Keep this concise report, source comparison and executable tests in Git; generated fixtures, full test output and temporary stores stay in scratch.
