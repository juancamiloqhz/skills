# Exact current-head verification

A passing review of head A cannot approve head B after changes. This small subprocess exercise uses the actual `orch` ledger CLI to check exact PR/head binding. It adds no production coordinator or API.

Run from the repository root with Bun and the helper dependencies already installed:

```sh
python3 research/jstack/evaluations/orchestrate-current-head/test_current_head.py \
  --cli /absolute/path/to/orch.ts --scratch /tmp/orch-current-head-tests
python3 -O research/jstack/evaluations/orchestrate-current-head/test_current_head.py \
  --cli /absolute/path/to/orch.ts --scratch /tmp/orch-current-head-tests
```

`--cli` is required. The script compares its sibling `orch.ts` and `store.ts` bytes with this checkout before testing. `--scratch` is optional; each invocation retains a fresh task-owned directory there, or in the system temporary directory when omitted. It contains synthetic evidence, command results and ledger byte snapshots. Nothing is installed. Generated artifacts stay outside Git.

The exercise records a synthetic pass for PR 1/head A, then requires PR 1/head B and PR 2/head A lookups to return exit 2 with `NOT-VERIFIED`, leaving the ledger unchanged. It records a negative B verdict and requires its JSON lookup to return exit 0 with `verifier-failed`. A simulated late A success receives a caller-owned stale classification and no ledger write. Ledger bytes, A's evidence and B's negative row must remain unchanged. A separately labelled fresh B pass replaces B's negative row while retaining A and the negative evidence file.

## Executed results

On 2026-10-17, a fresh implementation worker ran both commands against an exact runtime copy with its existing dependencies. Both exited 0 and reported `PASS` with Bun 1.4.2 and Python 3.14.4. Both source byte comparisons passed before testing. This new test uses explicit exceptions that remain active under `python -O`; PR75's separate assertion-based replay script is unchanged.

The fresh worker used a separate T3 worktree at base `6d7bc41bdf23fb3878c358444e47448c3bb79ccb`. An unexplained commit in the first checkout caused this fresh round; that checkout and staged work remain preserved. The second checkout had a branch-only rename, with no commit or index change. After that child finished, the coordinator checked its reported file hashes and imported those exact bytes into the parent branch. The coordinator does not claim to have identified the first mutation's actor.

The coordinator reran the normal test and published PR #76 at candidate A, `27ecb31004211e53380035952ca0aae86eae3b7a`, then recorded a passing parent check under that exact PR/head. This report update creates a later candidate. Its live head, the old-record rejection and the subsequent fresh check belong in the PR body and local ledger after observation. The original child result remains bound to its original task/run and tested file hashes; it did not report candidate A as its own commit. These parent checks are not an independent model review.

## Synthetic boundary and fidelity

PR numbers, the distinct 40-character SHA-shaped values, reports and evidence fixtures are explicitly synthetic. CLI ledger operations and exit codes are real. The script does not query or authenticate live T3 tasks, GitHub heads or review identities. Stale classification and the fresh B write are simulated caller decisions. The CLI neither authenticates evidence nor enforces verifier precedence or writer ownership. A successful lookup alone is not approval. This exercise proves no host recovery and does not activate Orchestrate.

The exact pinned source is [`pstack/skills/poteto-mode/playbooks/orchestrate.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/orchestrate.md). This worker read that source from the local upstream Git cache and compared its Verification and Liveness requirements with this exercise. Exact PR/head lookup and fresh verification preserve those requirements. Retaining A under its original key follows the local [execution contract](../../../../skills/jstack/jstack-juan-mode/references/execution.md); it cannot certify B.

This research test has no one-to-one upstream file. Its necessary adaptation is the requested bounded synthetic CLI exercise. Operational skills, runtime sources, manifest pins, reviewed checkpoint, lockfiles and licenses are unchanged. The existing [operational source mapping and comparison](../orchestrate-procedure/source-comparison.json) and [adaptation assessment](../../adaptations/orchestrate.md) remain unchanged. Publication, live PR/head checks and durable coordinator records belong to the parent. Restart recovery requires separate approval for a named restart.
