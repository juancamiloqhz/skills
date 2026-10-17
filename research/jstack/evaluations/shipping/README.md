# Shipping evaluation

Shipping now requires independent verification for each PR and lands only the contiguous passing run from the bottom. This evaluation exercises actual CLI revisions and local Git operations. It does not establish live forge landing or unattended continuation after a merge.

Source: `11713c683fe4add4fd403ea880580abbc9e0875f`. Base: merged Babysit, `d5fb19341c40f515da764fad59a1608003f70ca1`. See the [adaptation](../../adaptations/shipping.md) and [source comparison](source-comparison.json).

## Independent verification

On 2026-10-17, Linux x64 and Python 3.14.4, [fixture.py](fixture.py) generated a real three-layer Git repository with a one-shot arithmetic CLI. Labels 101–103 are synthetic PR numbers, not GitHub PRs. Each layer was checked against its direct parent. The middle layer deliberately computes square incorrectly.

Three fresh T3-owned children used the configured `swarm workers` target, Codex `gpt-6.1-sol` at medium effort. Each had a separate T3-bound worktree, read Shipping and `jstack-control-cli`, cloned the immutable fixture into owned scratch and drove its actual CLI. None wrote the fixture. The parent inspected their reports, commands, output expectations and independently recomputed patch identities.

| Layer | Result | Observed evidence |
| --- | --- | --- |
| 101, triple | PASS | All 38 CLI checks passed. Parent rejects triple; head returns `3*n`. Existing double, help and invalid arguments passed. Inputs include zero, negative and large integers. |
| 102, square | FAIL | 39 of 44 checks passed. Five of seven new square cases failed, including `square -3` returning `-6` instead of `9`. Double and triple passed at both revisions. |
| 103, negate | PASS+NOTES | Ten parent/head negate checks passed and all 15 inherited numeric outputs were unchanged. The 48-invocation run also exposed eight inherited square semantic mismatches across parent/head. Those are notes about layer 102, not evidence that square works. |

The landable run is therefore `[101]`, with ceiling 101. Layer 103's passing change cannot bridge layer 102's failure. The parent did not promote the inherited bug to a passing stack verdict.

All reviewers resolved full actual base/head commits and recomputed stable patch IDs. These identities match the generated fixture:

| Layer | Stable patch ID |
| --- | --- |
| 101 | `a239ad2bce1274facde6f2b18ec78233e8c7bf0a` |
| 102 | `b8225cde6751307b8ec1a58f48138c32819217f5` |
| 103 | `47e6daa68d747c32eb66eac7c9912a007312561e` |

Each invocation had a five-second deadline; all children were reaped. The first reviewer used an owned PTY, the other two captured the noninteractive CLI's streams directly. No persistent processes remain. This is checkout isolation on one machine, not a cloud VM or a full UI test.

Two harness errors were corrected and disclosed. The initial fixture generator inserted nested source incorrectly; the parent caught that before dispatch and compiled all final revisions. Reviewer 103's first comparison treated changed argument-usage text as inherited numeric output; its second run compared numeric operations and tested argument errors separately. Both runs reaped their children. Neither correction hides a product failure.

## Patch identity and local landing

The reproducible identity checks passed:

- Rebasing the first change onto advanced trunk changes its head SHA while retaining its base-to-head patch ID.
- Changing product logic with the same commit message changes that ID. Using the wrong base also changes it.
- An empty diff produces no usable identity and is rejected.
- Squashing only layer 101 onto local trunk leaves square and negate absent. The resulting merge commit is on trunk.

From the repository root, choose a new task-owned directory:

```sh
python3 -B research/jstack/evaluations/shipping/fixture.py /tmp/shipping-check --check-identities
```

The command creates a repository and sibling JSON manifest and requires the repository path not to exist. For independent CLI verification, create a second fixture without `--check-identities`, then clone it separately for each reviewer. Resolve `layer-101`, `layer-102` and `layer-103` and their direct parents. At each revision, run `python3 math_cli.py <operation> <integer>`, help and invalid arguments, comparing actual output and exit status. New operations should be rejected at the parent. Check double as `2*n`, triple as `3*n`, square as `n*n` and negate as `-n`; include negative, zero and positive inputs. The square failures are intentional. Recompute each `git diff <base> <head> | git patch-id --stable` in the clone. Raw generated repositories and transcripts are not required in Git.

## Controller decisions

Two fresh native Codex children used the configured `feature, refactoring` target, `gpt-6.1-sol` at high effort. One read Shipping; the baseline did not read any jstack procedure. Both answered the same five independent [cases](cases.json), with no forge calls or workflow mutations. The parent graded the complete answers against the supplied facts and pinned procedure.

| Case | With playbook | Baseline |
| --- | --- | --- |
| Passing prefix with failed middle | Stops after 101; distinguishes shipping from merge-when-ready authority | Correct prefix, but allows arming under shipping authority alone |
| Rebase and stale identity | Requires fresh CI; rejects changed logic, wrong base and empty identity | Same substantive decision |
| Docs/lint build exception | Two old builds and one new build; evaluates each difference; reruns dev-server lane | Requires equivalence and dev-lane rerun, but omits the source's repeated-build noise procedure |
| Pending auto-merge | Native parent watch and yield; no descendant arming; exact checkpoint if unavailable | Correct pending state, but proposes a substitute watcher/scheduler outside the supplied scope |
| Missing independent UI evidence | Incomplete, no publication or merge | Same authority and evidence boundary |

That is five acceptable case decisions with the procedure and two without it in one run per condition. This is a small instruction-following comparison, not a reliability or performance estimate. Shared successes do not demonstrate an advantage. Build-output noise handling, watch registration and merge wakes were hypothetical only. Raw answers, grading and the static review viewer remain in task scratch; timing and token usage were not supplied and are not estimated.

Configured Comment Sicko, Claude Opus 5.5 at high effort, inspected a private snapshot of the new Python fixture and returned an empty diff because it has no comments or suppressions. Parent inspection accepted that result; no code changes followed. Deslop review found no additional scoped cleanup.

Four packaging tests, mode/setup skill validation, changed Markdown lint, relative-link checks and `git diff --check` passed. Markdown fragment headings retain the source level-three structure; lint ran on task-owned copies with the first-line level-one rule disabled. Parent checks confirmed all verifier identities and clean assigned worktrees. The final source comparison preserves all nine Shipping steps and accounts for caller changes.

## Limits and retention

Live stack retargeting/landing, current-head CI transitions, Origin, published verdicts, actual build-noise comparisons and T3 continuation after merge-triggered settlement remain unverified. No fixture PR, auto-merge request or watch was created. Local squash execution and proposed decisions must not be described as live forge proof. The saved model configuration and upstream manifest are unchanged.

Retain only the small fixture, five prompts, this report and source comparison. Full reviewer reports, generated repositories, harnesses, catalog and transcripts remain in `/tmp/jstack-shipping-20261017` while this review is pending. T3-owned read-only worktrees are retained at `/home/ubuntu/.t3/worktrees/skills/t3-087a2dd7`, `/home/ubuntu/.t3/worktrees/skills/t3-861ad16c` and `/home/ubuntu/.t3/worktrees/skills/t3-27a86f21`; their bound branches remain clean at the initial Shipping draft commit. Do not remove app-owned bindings with manual Git cleanup. After acceptance, task scratch can be removed when no active task needs it; shared caches and unrelated work remain outside this cleanup scope.
