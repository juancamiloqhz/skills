# Orchestrate runtime evaluation

Historical PR #70 assessment. The subsequent [GitHub frontier adaptation](../orch-frontier/README.md) replaces the Graphite reader described here. Other state-helper and recovery limits remain.

The bundled `orch` helper now records work units, completion pointers, verification verdicts, standing orders and human gates in readable files. This foundation does not enable the Orchestrate playbook. Its Graphite-only frontier and coordinator recovery still need adaptation and validation.

Source is `11713c683fe4add4fd403ea880580abbc9e0875f`; local base is merged PR #69, `e830ea86dec6cce3e6bfb16625526ee47355a3ea`. The [adaptation record](../../adaptations/orch-runtime.md) explains every difference. [Source comparisons](source-comparison.json) record exact file and diff hashes. Store implementation and the 14 upstream tests are unchanged.

## Results

On 2026-10-17, Ubuntu Linux, Bun 1.4.2, Python 3.14.4:

- All 14 upstream orchestration tests and 48 existing watcher tests passed, 62 total. These exercise store operations, locks, invalid input, CLI parsing and exit codes, plus the existing watcher behavior. Graphite responses are test doubles; the branch histories used by its frontier tests are real local Git.
- The [six-part executable exercise](exercise.py) passed through fresh CLI processes. It preserved three units and standing orders through repeated initialization, rejected an unrecorded SHA with exit 2, and exposed `verifier-blocked` in JSON despite exit zero. Duplicate completion pointers stayed distinct; draining did not silently complete a unit. Status left a human gate open. A live owned process blocked another writer; after that process was killed, a fresh process recovered the stale lock and preserved existing records.
- Missing and mismatched Commander versions failed before any store creation or dependency-tree change. The first direct CLI probe showed this expected prerequisite error. An initial suite command accidentally ran from the source checkout without dependencies and failed CLI imports and assertions. Running the unchanged suite in the prepared isolated copy passed all 62 tests.
- Strict type checks passed for both tool directories with the available TypeScript 5.9.3 and bun-types 1.4.2. The full locked development environment, including TypeScript 7.0.2 and bun-types 1.3.14, was not installed or tested.
- Tests used an exact source copy in task scratch, linked to the already cached Commander 14.0.0 previously integrity-checked for Babysit. No package-manager install, package lifecycle script, real Graphite call or remote PR action ran as part of the runtime tests.

These are executable tool checks, not paired prompt evaluations. No agent workflow instruction was activated. The helper itself never spawns or monitors agents.

## Reproduce

With Bun and the declared dependencies already available, run from the repository root:

```bash
bun test skills/jstack/jstack-juan-mode/scripts/orch skills/jstack/jstack-juan-mode/scripts/watch-pr
python3 -B research/jstack/evaluations/orch-runtime/exercise.py
```

Run `bun run typecheck` from `skills/jstack/jstack-juan-mode/scripts` with the development dependencies present. The executable reports the manual prerequisite when dependencies are missing. Installing them is a separate user action, `bun install --frozen-lockfile` from that scripts directory. The exercise accepts an optional absolute `orch.ts` path for an isolated exact copy and cleans only its own temporary stores.

The source comparison can be reproduced with the recorded pin and `git show <pin>:<source>`, then a unified diff to each local path. The JSON records both SHA-256 hashes. The copied TypeScript tests are executable upstream source, not logs. Only this report, the exercise and source comparison are retained here. Raw output and temporary dependencies remain outside Git.

## Normal use

For a pagination task split into API, UI and tests, you can ask:

> Keep a local task board with jstack's orch helper. Record the three tasks, their actual verification evidence and anything waiting on my decision. Show me the status before I pause. Leave PRs open.

This requests bookkeeping within the active task. It does not start the still-unavailable Orchestrate workflow. With dependencies present, a local example is:

```bash
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board init
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board unit add api --track pagination
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board unit add ui --track pagination
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board unit add tests --track pagination
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board status
```

Choose an owned durable directory instead of `/tmp` for a real resumable task. The result is three pending units and a derived `status.md`; no implementation, verification or PR creation is implied. Record verdicts only after running their stated checks. `--help` describes the remaining commands.

## Remaining boundaries

The frontier command still depends on Graphite metadata and local branch tips. It has not been validated against a real Graphite installation. The planned Git/forge adapter must avoid trusting stale local or mid-restack base refs. Orchestrate also needs T3 child reconciliation, current-head acceptance, single-writer ownership, an acknowledged drain/recovery procedure and a live restart trial.

The current store does not deduplicate notifications, enforce verifier precedence or provide a multi-command transaction. Drain removes pointers before it returns them, so its success is not durable proof of subsequent classification. Historical ledger rows remain in status totals. A PID lock does not protect a shared store across hosts; `--force` bypasses a live holder. Keep these limits visible when designing the coordinator rather than changing the upstream format silently. Gate defaults record a proposal and do not grant approval.

All four packaging tests, changed-document Markdown lint and relative-link checks, final source hashes and `git diff --check` passed. The playbook count stays at 22, and source pins, licenses, the lockfile and saved model configuration remain unchanged.
