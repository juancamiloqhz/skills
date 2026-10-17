# Completion reconciliation evaluation

The coordinator instructions now spell out how to reject stale or mismatched results, recognize duplicate notices, and preserve verifier precedence while processing recoverable inbox batches. This is an instruction change, not automatic enforcement by `orch`.

The [adaptation](../../adaptations/completion-reconciliation.md) maps the rules to pstack's agentic queue, verification and liveness sections at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local base is merged PR #72, `6bb80ef6d753bb1d28fa63004619682123f04dcf`. The local execution reference has no one-to-one upstream file; [source comparison evidence](source-comparison.json) records the governing source, baseline/local hashes and exact local diff hash rather than presenting it as a verbatim port.

## Results

On 2026-10-17, two native evaluation agents inherited Codex gpt-6-astra at high effort. One read the updated execution contract and the other read the previous version. Each handled the fresh and resume cases sequentially in separate fixtures. Neither activated juan-mode or resolved configured workflow roles. The parent used writing-for-agents and skill-creator guidance to author and evaluate the contract.

| Case | Updated contract | Previous contract | Artifact evidence |
| --- | --- | --- | --- |
| Fresh notices | 6/6 | 6/6 | Five pointers accounted for; independent API failure preserved; superseded UI and mismatched run rejected; current modeled tests verdict recorded once despite a duplicate notice. |
| Resume pending batch | 6/6 | 6/6 | Original batch recovered; live nested work stays unresolved; old-head original result remains distinct from a later summary; earlier verified row is not rewritten. |

Both conditions passed all 12 assertions. This establishes bounded compatibility, not a measured improvement. There was one run per case and condition, with the two cases sharing one agent per condition. The task itself supplies important inspection and authority constraints. No statistical, speed or token-efficiency claim is made; unavailable measurements are omitted.

The parent checked every decision against the actual saved unit and ledger rows, pointer filenames, receipt hashes and command traces. PR 201 retained `verifier-failed` from `independent-api`; PR 202 gained no verdict; PR 203 had one current-head modeled verification row. In the resume case neither condition issued a unit or ledger mutation. All acknowledged manifests matched their saved receipts. Immutable fixture hashes, actual Git heads and clean worktrees matched their initial evidence. Every unresolved result had a recorded follow-up and no replacement was dispatched.

The updated run left the blocked API unit as `needs-verify`; the baseline marked it `needs-fix`. Both preserved its failed independent verdict and described the required fix, so neither counted it verified. The baseline's resume lookup returned expected exit 2 with `NOT-VERIFIED`. No mutation or local artifact-check command failed.

## What was real and what was modeled

Git repositories, commit comparisons, local process execution, `orch` commands, table writes, batch claims and acknowledgements were real. Task statuses, PR states and independent verifier receipts were fixture inputs. The local check deliberately only prints success; both agents identified that it proves no pagination behavior. The accepted PR 203 verdict is a modeled verifier receipt, not newly established application coverage.

The stored frontier stayed at generation zero. Neither run called the network-backed frontier reader because live forge access was outside the exercise. They checked the modeled current PR observations against actual Git heads and disclosed that live frontier verification remained unavailable. The earlier [frontier evaluation](../orch-frontier/README.md) covers that separate tool; it does not fill this exercise's missing live integration.

No T3 task restart, actual cancellation, writer replacement, independent live verifier, merge, watch or schedule ran. Full Orchestrate remains unavailable. The next work is to connect the final coordinator procedure to these contracts and validate its pilot and recovery against real task lifecycle evidence.

## Reproduce

With Bun and the tool dependencies already available, generate fresh fixtures from the repository root:

```bash
python3 -B research/jstack/evaluations/completion-reconciliation/fixture.py /tmp/reconciliation-fresh --case fresh
python3 -B research/jstack/evaluations/completion-reconciliation/fixture.py /tmp/reconciliation-resume --case resume
```

Use `--cli /absolute/path/to/orch.ts` for an isolated exact copy with declared dependencies already present. The generator refuses existing destination roots. It creates local Git history and initialized stores, without remote access or installation. For paired runs generate a separate pair of roots for each condition. Save the old contract with `git show 6bb80ef6d753bb1d28fa63004619682123f04dcf:skills/jstack/jstack-juan-mode/references/execution.md`.

Give the agents [the case prompts](cases.json) with their own `FIXTURE` path and the chosen contract. Withhold the assertions and generator. Restrict writes to their store and output files; fixture inputs and repositories are immutable. Use the modeled task-status endpoint and actual declared CLI. Require one decision per pointer, original task/run identity, classification, reason, applied changes, a report and an actual command trace. Inspect records and command outcomes before grading; a plausible report alone is insufficient.

The 4 packaging and 16 preflight tests passed. Changed-document Markdown lint, relative links, source hashes and `git diff --check` passed. No runtime code changed, so the prior 97-test runtime result is retained as prior evidence rather than claimed as a new run. Source pins, reviewed checkpoint, licenses, lockfile and saved models are unchanged.

Only this report, the fixture generator, cases and source comparisons are retained in Git. Raw receipts, command traces, grading data, static review viewer and generated stores remain in task scratch while the PR is reviewed. The viewer was generated with skill-creator's renderer; its static feedback fallback and fixed frame were adapted for T3 embedding. No unavailable timing or token measurements are represented as zero.

## Normal use

Suppose a worker reports success for an old version after you have already replaced it. You can ask:

> Process the saved completion notices. Check that each result belongs to the current task and code before updating our progress.

The coordinator checks the recorded assignment and current commit, records the late result as stale, and keeps it from marking the new version verified. If the same accepted result arrives twice, it accounts for the duplicate without repeating its state changes. These instructions support the future full Orchestrate workflow; the bookkeeping helper does not enforce them on its own.
