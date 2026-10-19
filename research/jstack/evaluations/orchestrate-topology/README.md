# Orchestrate stack ownership

Make the worker brief explicit about PR retargets and merges, and name the operations reserved for the single stack owner. This follows the [coverage audit](../../coverage-audits/2026-10-18/README.md). It changes instructions, not the orchestration runtime or its enforcement capabilities.

## Complete source assessment

Local base is merged PR #93, `c95bd00a7698553eaaa0f1c24c0f6b049122aed6`. Compared `pstack/skills/poteto-mode/playbooks/orchestrate.md` from original pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/poteto-mode/playbooks/orchestrate.md). Every change in that source range is accounted for below.

| Source change | Disposition |
| --- | --- |
| Replace restack wording with chain rebases in the coordinator role and rebase mechanics in escalation | Adopt both wording changes. Keep delegated conflicted merges/code edits and the coordinator's cheap clean-landing path. |
| Replace the brief's `no gt` restriction with explicit `no PR retargets or merges`; retain rebase, force-push and scope restrictions | Adopt the complete two-line `FORBIDDEN` field exactly. This names the prohibited operations independently of the Git tool used. |
| Enumerate the stacker's exclusive operations and forbid worker PR retargets/merges; have Babysit report conflicts rather than rebase | Adopt the operation list and worker/conflict sentences. Preserve jstack's T3 worktree placement, writer quiescence, old-parent/base/head capture and expected-ref leases. Mandatory Cursor cloud placement remains inapplicable. |
| Replace Graphite frontier discovery with automatic gh/Origin discovery and local branch heads; add `--forge origin` at initialization | Keep the existing explicit GitHub PR scope and remote-verified reader. Origin and automatic discovery are not implemented. A failed refresh preserves the prior file without making it current. See the [frontier adaptation](../../adaptations/orch-frontier.md). |
| Add adaptive model effort/speed selection | Keep exact saved options under the existing model-policy boundary. No configuration change or new fallback is authorized by this update. |

The parent inspected the entire final upstream/local diff. All remaining differences retain the [documented T3 and authority adaptations](../../adaptations/orchestrate.md), including supported child tools, logical role durability, bounded nesting, explicit stores, recoverable inbox claim/ack, current-head verification and writer-aware recovery. The seven procedure steps and ten section headings remain in source order. Six exact text replacements account for the entire local operational diff; reversing them reproduces the base procedure byte for byte.

Every other shipped file remains unchanged, including the runtime, Autopilot-stack mechanics, model resolver and invocation instructions. License bytes match upstream. Original pins, the upstream manifest and reviewed checkpoint remain unchanged. This is not a claim that the newer upstream runtime or every workflow has been adopted.

## Bounded evaluation

[Four cases and expectations](cases.json) cover a worker shortcut, competing stack owners, a failed frontier refresh and coordinator-owned mechanical landing. Give a fresh agent the requests without expectations, the complete authoring procedure and its needed local references. Require proposed actions and evidence requirements only. Prohibit actual Git/forge mutations, program execution, nested dispatch and configuration changes. Inspect the decisions against the retained expectations.

One fresh native Codex agent using inherited gpt-6-astra/high answered all four cases on 2026-10-19. It read Orchestrate, the imported Autopilot-stack mechanics, execution and Shipping references. The parent inspected its report against all eight expectations; each was met.

| Case | Observed decision |
| --- | --- |
| Worker shortcut | Refused the worker's retarget/merge, retained the parent dependency and returned scoped evidence for coordinator/stacker action. |
| Competing stackers | Held Bob's mutations until Alice and the affected worker were reconciled, one holder was recorded and current refs supported expected-ref leases. An isolated checkout alone did not authorize rewriting contested published branches. |
| Failed frontier | Treated the preserved record as stale, retained explicit PR scope and rejected undocumented Origin/automatic-discovery recovery. |
| Coordinator landing | Allowed the authorized sole-holder coordinator's cheap clean landing. Required a scoped task for conflict code edits and current-head verification afterward. |

All cases shared one agent context. The evaluator saw neither expectations nor prior results/diffs. It proposed actions without performing a rebase, retarget, push or merge. These are instruction-conformance results, not four independent runtime trials or a measured improvement over the previous wording. Protected skill and manifest hashes remained unchanged during the exercise.

The evaluator also flagged an existing cross-reference question: Orchestrate requires a verdict for every new head, while imported Autopilot-stack/Shipping rules may preserve some lane evidence for an unchanged patch. It treated preserved evidence as input to a new current-head assessment, never permission to relabel an old verdict. No case accepted stale-head evidence. The exact lane-rerun requirement remains for the already-planned coordinated Shipping/Autopilot update. Its acceptance case should distinguish an unchanged patch after rebase from changed implementation, requiring a current-head decision in both. This wording update does not settle that broader verification policy.

## Checks and limits

Four packaging tests, containing-skill validation, documentation consistency and whitespace checks pass. The documentation checker reports 45 skills and 23 playbooks with zero problems; guide coverage remains pending. Exact source replacements, base reversal, heading/step order, license identity, unchanged shipped files/manifest and updated relative links also pass.

Run existing package and documentation checks from the repository root:

```sh
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
git diff --check
```

Also validate the containing Juan-mode skill with the host skill creator's `scripts/quick_validate.py`. The source comparison and ownership cases assess instructions; they do not prove live concurrent-writer isolation or successful PR retargeting. Historical runtime evaluations retain their original scope and are not new runs for this update.

Keep raw source diffs and agent output in task-owned cache. Retain only this report and four case prompts/expectations. Installation, saved models and schedules remain unchanged.

## Normal use

With Juan-mode active, ask it to coordinate a multi-day migration with several dependent PRs. Workers implement their assigned changes. If an upper PR needs a new base, its worker reports that need; the designated stack owner handles the retarget or rebase after checking affected writers and current branch state. The same ownership rule covers merges. Existing user authorization and verification gates still apply.
