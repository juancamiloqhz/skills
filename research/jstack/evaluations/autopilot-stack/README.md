# Autopilot-stack evaluation

On 2026-10-17, one assisted run and one baseline run each passed 8/8 assertions in a local three-PR stack exercise. Both preserved a later owner patch that broke the middle PR, rejected its stale review receipts and withheld a fully verified delivery. This establishes bounded Git and assessment behavior, not a benefit over the baseline or a completed live Autopilot-stack program.

## Scope and source

The [procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/autopilot-stack.md) preserves the eight upstream steps, their order and the choosing-between-autopilots rule. [Adaptation decisions](../../adaptations/autopilot-stack.md) account for T3 delegation, parent-owned watches, explicit recurring-work authority, confirmed writer handoff and permission-scoped publication. The operator retains landing control.

The source pin is `11713c683fe4add4fd403ea880580abbc9e0875f`; setup remains at `ccb5507cec1546dc88135c1139c811e6c59115ba`. [Source comparisons](source-comparison.json) record final file and complete diff hashes for the procedure and five callers. The local base is `04af71fe541c52228eb93f602f1e1f1817dca93b`. Mappings, licenses, saved models and the reviewed checkpoint are unchanged.

Both native evaluation agents inherited Codex `gpt-6-astra` at high effort. Python 3.14.4 and Git 2.53.0 ran on Ubuntu. The assisted agent read the draft and its dependencies; the baseline received no jstack instructions. Each used a separate generated fixture and the same [task and eight assertions](cases.json). The task itself supplies many constraints. There was one run per condition, no timing or token measurement, and no statistical or efficacy claim. Juan-mode was not activated, and the agents did not use configured jstack workflow roles.

## Observed results

| Assertion | Assisted | Baseline | Evidence checked by the parent |
| --- | --- | --- | --- |
| Initial linear stack and patch identities | Pass | Pass | Actual remote base/head chain; all original child patches match; all three CLIs print `9`. |
| One topology writer and protected pushes | Pass | Pass | Six explicit expected-ref leases per run, each after `ls-remote`; retained old parent tips. |
| Bottom-up restack after drift | Pass | Pass | Correct final ancestry, own-file diffs and own-commit counts of 1, 2 and 1; changed owner patch preserved. |
| Current proof and stale-verdict rejection | Pass | Pass | Fresh exact-head proof and local mergeability; middle CLI prints `12`, with `complete=false` despite exit zero. |
| Review-only delivery | Pass | Pass | Every simulated PR remains open with auto-merge off; trunk contains only the authorized fixture documentation change. |
| Truthful evidence and handoff | Pass | Pass | Before/after identities and verdicts retained; owner fix and fresh independent review requested; simulation limits stated. |
| Ownership, stop and statement-then-wait protocol | Pass | Pass | Both explanations assign coordination to the parent, block unconfirmed writer reuse and require an explicit go. Explanation only. |
| Recurring authority and landing boundary | Pass | Pass | Assisted report names missing hourly coverage; baseline limits its audit to one-time work. Both reject implicit recurring or landing authority. Explanation only. |

The parent checked immutable packet/forge hashes, bare-origin branch histories, actual parent diffs, patch IDs, current CLI output and action records. PR 201 and PR 203 kept their own original patch identities. PR 202's net patch changed from `fb618e007e17c7fc332e48b989573d0031d63185` to `740f2b0e8684daf42886be741ff9bca6419495a4`. PR 203's own export check passed, but its inherited invoice behavior failed. Both reports therefore left the complete chain unverified.

There were no failed recorded Git/CLI commands. The intended behavioral failure returned a successful process exit, which both runs correctly distinguished from a passing proof. The assisted report also identified outdated availability text in Opening a PR. That sentence was corrected after the run, alongside the other caller availability updates, without changing the evaluated stack procedure. It is included in the final source comparison.

## Reproduce

From the repository root, choose two fresh paths that do not exist:

```bash
python3 -B research/jstack/evaluations/autopilot-stack/fixture.py /tmp/jstack-stack-with-fresh
python3 -B research/jstack/evaluations/autopilot-stack/fixture.py /tmp/jstack-stack-without-fresh
python3 -B /tmp/jstack-stack-with-fresh/forge.py view
python3 -B /tmp/jstack-stack-with-fresh/forge.py proof 202
```

The proof initially prints `9` and `complete=true`. Give each isolated agent `cases.json`'s task with its fixture path substituted for `FIXTURE`, but withhold the assertions and generator. Give only the assisted agent the procedure and its dependencies. Allow only the named local branch and endpoint mutations. Save initial evidence before the single `drift` call, then restack bottom-up using recorded old parents. Do not fix or revert the injected owner patch. Grade all eight assertions against actual artifacts and commands.

Inspect the final origin with `git -C <fixture>/origin.git`. Its chain must be `main <- pr-201 <- pr-202 <- pr-203`. Relative to each actual parent, the changed files must be `search.py`, `invoice.py` and `export.py`, and the own-commit counts must be 1, 2 and 1. Current proofs must print `9`, `12` and `9`; only the middle proof has `complete=false`. Each parent must be an ancestor with a clean local merge-tree result. Main must equal the recorded drift tip and differ from its initial tip only in `README.md`. Compare `before.json`'s protected hashes and inspect every push's expected-ref lease. Every simulated PR must still be open.

Packaging tests, mode/setup metadata validation, changed-document link checks, Markdown lint and `git diff --check` passed. Fresh fixture generation and its three initial proofs were also checked separately. These structural checks do not prove semantic fidelity or unattended operation.

## Limits and retained evidence

Git rebases, local bare-origin pushes, patch IDs, merge-tree checks and CLI execution were real. PR bases/state and independent review receipts were simulated; the proof endpoint wraps a real CLI in simulated CI metadata. No live independent reviewer, network forge, real stack publication, conflict handoff, lease race, cancellation, watch wake, recurring audit, restart recovery or full owner loop ran. Protocol explanations do not establish those capabilities. A real program must satisfy every required verification lane and current authority check before reporting delivery complete.

Only this report, the fixture generator, cases and source comparisons are retained in Git. Raw reports, traces, snapshots, controller grading and the static review viewer remain in task-owned scratch for the pending review. The grader removed generated zero defaults for unmeasured time, tokens and tool metrics. Scratch can be removed after acceptance when no active task needs it, under the repository retention policy.

## Normal use

> Use jstack-juan-mode's Autopilot-stack to add pagination in three PRs: API support, UI controls, then integration tests. Build and verify the stack, leaving every PR open for me to review and merge. State the plan first and wait for my go.

After your go, the coordinator builds the chain with the API PR based on main, the UI PR based on the API branch, and tests based on the UI branch. If trunk or a lower PR changes, it restacks in order and refreshes affected evidence. You receive the open chain with verdicts and any blockers, then decide when to land it.
