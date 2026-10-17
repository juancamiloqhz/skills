# Orchestrate GitHub frontier

Source: `pstack/skills/poteto-mode/scripts/orch/` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [scripts/orch](../../../skills/jstack/jstack-juan-mode/scripts/orch). This replaces the Graphite-only reader identified in the [autonomy inventory](../juan-mode/autonomy-inventory.md#orchestrate). It does not activate Orchestrate or change the 22-playbook count.

## Contract and necessary differences

Upstream discovers the current stack through `gt log` and `gt info`, optionally compares a caller's PR list, and records local branch tips. T3 does not supply that Graphite stack metadata. GitHub alone does not identify which of several stacks a caller owns. The supported adapter therefore requires an explicit, nonempty `--prs` list in bottom-to-top order. It validates that scope rather than guessing it. Callers must account separately for omitted PRs; this check cannot prove the list is exhaustive.

| File | Difference from pin | Requirement and verification |
| --- | --- | --- |
| `orch/store.ts` | Replace Graphite text parsers and local `rev-parse` with exact GitHub PR reads, published Git heads and commit ancestry. Require `prs`. | Prevent stale local tips and intermediate restacks from becoming current evidence. Real Git fixtures cover branch drift, topology, malformed responses and second-read changes. |
| `orch/orch.ts` | Rename frontier help to GitHub and describe `--prs` as required. | Keep the command names and argument spelling; omission fails with an actionable error. The earlier read-only dependency check remains the sole other CLI difference. |
| `orch/orch.test.ts` | Remove two Graphite-specific cases and their fixtures. Retain the other 12 upstream tests. | The retired dependency is no longer a supported frontier source. Its replacement has executable coverage in the added file. |
| `orch/frontier.test.ts` | Add 23 adapter tests using actual Git branches and a local bare origin, modeled GitHub responses, plus actual CLI subprocesses. | Verify the adapter and byte-for-byte retention of the previous record on failure. Fixture scripts and repositories are generated in temporary directories and removed after tests. |

The prior [runtime adaptation](orch-runtime.md) still accounts for the manual dependency check, package name and strict compiler setup. The [source comparison](../evaluations/orch-frontier/source-comparison.json) compares final files directly with the pinned source. No store schema, unit/ledger/inbox/gate operation, lock algorithm, verdict rule or status derivation changes.

## Evidence read before writing

1. Resolve `origin` to a standard github.com HTTPS or SSH repository. Read its identity and default branch using `gh api` with an explicit hostname and GET method.
2. Read each exact PR number. Require matching repository identity, valid branches and commit IDs, and coherent open/closed/merged state. Fork PRs and deleted head repositories are unsupported. Branch names must be distinct and different from trunk.
3. Allow a merged prefix followed by an open chain, or an all-merged scope. Reject a closed-unmerged PR or a merged PR above an open one. Deleted branches in the merged prefix do not block the read. The prefix records merge state; it does not reconstruct historical topology.
4. Use `git ls-remote --refs origin` for the default branch and each open head. Require API head/base SHAs to match those published refs. Each open PR must target trunk or the preceding open branch.
5. Compare immutable parent/head SHAs through GitHub. Require the reported base and merge base to equal the current parent, with ahead or identical status. Retargeting a PR before its commits have been restacked is insufficient.
6. Re-read PR evidence, published refs, repository identity and default branch. Any observed change fails before writing. Otherwise preserve upstream's atomic replacement of `frontier.json`, increment generation and select the first open PR as `lowestUnmerged`.

GitHub documents the [PR response](https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request) and [commit comparison](https://docs.github.com/en/rest/commits/commits#compare-two-commits). The [gh API command](https://cli.github.com/manual/gh_api) supplies the authenticated reads. Commands have a 20-second timeout and 4 MiB output limit each. Errors, missing tools, unavailable authentication, oversized responses and unsupported topology leave the previous frontier intact. This bound applies per command, not to the whole stack.

Repeated reads reduce race exposure; they are not a distributed atomic snapshot. Another actor can change the repository after inspection. A frontier is topology evidence, not proof of checks, reviews, verifier acceptance or merge authority. Revalidate before any subsequent action that depends on current state.

No fetch, checkout, rebase, push, merge, installation or watch runs inside the adapter. The existing single-host store lock and coordinator recovery limits remain. See the [evaluation and usage example](../evaluations/orch-frontier/README.md). Completion reconciliation and restart validation remain prerequisites for the full Orchestrate procedure.
