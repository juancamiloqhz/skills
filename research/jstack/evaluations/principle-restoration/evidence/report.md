# Restored principle forward evaluation

## Verdict

The request does not support a release-ready verdict. The local fixture proves a fresh heartbeat can survive a stopped process. Equal actor counts show absent count skew in the supplied snapshot, not absence of a causal contribution to latency. One cached run does not establish a reliable 2x speedup. A single-writer local export can converge after the tested interrupted stages by rebuilding a complete temporary artifact and publishing it atomically.

## Instructions and dependency discovery

Read the repository upstream-fidelity policy and the current `principle-prove-it-works`, `principle-explain-the-number`, `principle-attack-the-premise`, and `principle-make-operations-idempotent` SKILL.md files under `skills/jstack/`.

The supplied session catalog does not advertise `benchmark-checklist`, `show-me-your-work`, `principle-build-the-lever`, `principle-fix-root-causes`, or `principle-laziness-protocol`. No installation, sibling-path assumption, or model configuration change was made. In particular, the mandatory benchmark-checklist procedure is unavailable and remains incomplete. Independent authorized local checks proceeded. Creating a rerunnable census does not imply that the unavailable Build the Lever helper was executed.

## Actual execution

Command:

```sh
python3 -B /tmp/jstack-principle-restoration-evidence/check.py
```

Exit status: 0. Full output is in `results.json`. Executable source is in `check.py` and `export.py`.

- Started a disposable Python child that writes a heartbeat then sleeps. Direct child-process polling confirmed it was running.
- Terminated and reaped that same child. Its exit status was -15 and its heartbeat was still only 0.0073 seconds old. The heartbeat remained fresh although the actual process was stopped.
- Recomputed the scenario census from 100 A and 100 B synthetic events. Both counts were 100. This is a reproducible encoding of user-provided counts, not a fresh production observation.
- Injected process exit 75 before writing, during a partial write, before publication, and immediately after publication. For each stage, checked that the published file remained a complete old or new JSON export, then ran two successful retries and checked exact final contents and absence of pending temporary output. All four scenarios passed.

## Requested conclusions

The shared premise is: “An uneven distribution of events between actors causes the slowdown.” Two unsuccessful fixes motivate investigating that premise before another patch. The current count snapshot does not show the expected count skew. It cannot rule out different per-event costs, timing skew, queueing, or another unmeasured actor property. No new fix or causal conclusion is justified by this evidence. A subsequent investigation should collect repeated per-actor counts and time/cost measurements during the slowdown and test competing explanations.

The reported benchmark remains inconclusive: the scenario supplies only one cached run and a claimed ratio. There is no observed run spread, verified equivalent workload, measured resource limiter, profile-to-source connection, or evidence excluding skipped work and cache artifacts. I did not run a benchmark or manufacture those missing measurements. Full benchmark-checklist execution is blocked by the missing catalog dependency.

## Safe-retry example and limits

The export example rewrites a pending file from deterministic source data, flushes and syncs it, then atomically replaces the destination on the same filesystem. Before publication a crash preserves the previous complete export; after publication retries reproduce the same complete export. It removes abandoned pending state at startup.

This is a single-writer process-crash demonstration, not a production export implementation. It assumes fixed input, local same-filesystem rename semantics, and no concurrent exporter. It does not prove power-loss durability, directory-entry persistence, permissions/error recovery, network-filesystem behavior, lock handling, external side-effect deduplication, or every possible machine-instruction interruption. Four meaningful interruption boundaries were exercised; claiming exhaustive crash coverage would be incorrect. Production handling needs an explicit input snapshot/idempotency key and concurrency policy where those conditions apply.

The heartbeat test proves process existence only for the disposable child at its observation points. It does not establish service health, request responsiveness, or production state.

No repository files, external services, installations, settings, commits, or PRs were changed. Temporary process and output fixtures were cleaned after checks; rerunnable scripts and recorded evidence remain in this directory.
