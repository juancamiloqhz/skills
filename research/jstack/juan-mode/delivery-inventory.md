# Delivery and session playbook inventory

Assessed all seven playbooks below in full at upstream commit `11713c683fe4add4fd403ea880580abbc9e0875f`, together with the full mode entrypoint. The proposed changes preserve their purposes while replacing Cursor execution assumptions. This assessment does not execute the playbooks or authorize publication, merges, scheduling, or deletion.

Source: [poteto-mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), the pinned playbook links below, and the approved scope in this conversation.

## Shared dependencies and runtime findings

All routes inherit the mode's relevant principles, prose rules, delegated-work review, and model routing. Reuse jstack's validated role map and preserve each seat's options. Delivery prose and general judgment use `judgment and prose`; code corrections use their implementation role, with `hardest tasks` for the documented hard cases. Verification fan-out uses `swarm workers`. A playbook is a bundled procedure; reusable helpers and platform adapters need their own declared dependency contracts.

Source: [mode subagents and principles](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [jstack configuration](../../../skills/jstack/jstack-setup/references/configuration.md).

The inspected watcher files are `watch-pr`, `cli.ts`, `types.ts`, and `policy.ts`; the entrypoint invokes `bootstrap.ts`, which can install Bun dependencies. The watcher supplies GitHub status classification as well as its polling loop. Replace the loop with native T3 Code watching and preserve explicit readiness checks against the forge. Watching is an event source, not proof of mergeability, resolved threads, or current verification. Do not inherit the install-on-launch behavior.

Source: [watcher entrypoint](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/watch-pr/watch-pr), [CLI](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/watch-pr/cli.ts), [types](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/watch-pr/types.ts), [policy](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts), [bootstrap](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/bootstrap.ts).

T3 Code's parent thread owns PR watches; subagents cannot watch. The parent handles existing comments, registers the watch, and ends its turn. It rechecks facts on a wake and unwatches when handing responsibility back. Every created or worked-on PR, including every stack layer, must be linked. Merge continuation needs a live evaluation because watches stop on merge or thread settlement, and PR linking can settle a thread when its PR merges. A stack coordinator must not promise unattended progression until that behavior is proven.

Source: live `link_pull_request`, `list_thread_pull_requests`, `watch_pull_request`, `unwatch_pull_request`, and `t3_thread_organize` descriptions inspected on 2026-10-11.

Use child tasks for delegated work and fresh tasks with consolidated context for review rounds. New top-level conversations require the user's request. `t3_worktree_handoff` changes the current thread's binding and ends its turn; its continuation prompt resumes work in the new checkout. It cannot move an already attached thread. `t3_thread_launch` binds an explicitly requested separate conversation before it starts. These are distinct from a child using an isolated checkout whose path is in its task brief.

Source: live `delegate_task`, `task_status`, `task_cancel`, `t3_worktree_handoff`, `t3_worktree_status`, and `t3_thread_launch` descriptions inspected on 2026-10-11; [jstack T3 Code integration](../../../skills/jstack/jstack-setup/references/t3-code.md).

Also inspected in full are `check-plan.mjs`, `worktree-audit.sh`, `references/bugbot-triage.md`, and the `show-me-your-work` skill. Adapt the first two with their owning playbooks. Keep evidence-based review-comment triage in an internal reference. Reuse one canonical decision trail across planning, execution, pause, and pickup rather than inventing a separate record format for each.

Source: [plan checker](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/check-plan.mjs), [worktree audit](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/worktree-audit.sh), [triage reference](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/references/bugbot-triage.md), [decision trail](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md).

## opening-a-pr

Trigger when the requested delivery includes a PR. Produce ordered commits, the requested PR or stack, concise verification evidence, and the actual URLs. Upstream invokes this route after other playbooks, uses `deslop`, `no-comments`, `technical-writing`, `unslop`, and requires a delegated opener to run `interrogate`. Its forge defaults to `gh`, preferring a usable Origin CLI; its prose model follows the mode's judgment role.

Source: [opening-a-pr](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/opening-a-pr.md), [mode models](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md).

The [implemented procedure](../../../skills/jstack/jstack-juan-mode/playbooks/opening-a-pr.md) uses the shipped cleanup and writing helpers, honoring the repository's PR template and the existing `pr` skill where available. Replace blanket resets, forced ready status, and automatic publication with the user's delivery scope and preservation of unrelated work. Use the callable PR creation tool or supported forge CLI, then register every URL through T3 Code. Opening a PR finishes without starting a watch unless monitoring was requested; a child returns its PR evidence to the parent.

Basis: proposed adaptation of [opening-a-pr](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/opening-a-pr.md); live PR-linking and watching descriptions; [jstack permission boundary](../../../skills/jstack/jstack-setup/references/configuration.md).

Acceptance scenario: with an unrelated dirty file and a two-layer change, publish only the authorized changes, preserve that file, target the child PR at its parent branch, and verify both URLs are linked with no automatic watch or merge. Repeat a local-only request and confirm it produces no PR. Prerequisites are forge credentials, publication permission, repository checks, and an available review helper; Origin is optional.

The [bounded evaluation](../evaluations/opening-a-pr/README.md) checks real local stack ancestry and preservation of staged, unstaged, untracked and ignored work. Live publication is limited to the actual single implementation PR. A published two-layer stack and delegated opener with Interrogate remain untested.

## babysit

Trigger on PR status or maintenance requests. Preserve upstream's four modes: one-pass `check`, comments-focused `threads-only`, nonblocking `background`, and merge-ready `drive`. Produce the lowest unmerged PR's state, fixes and dismissals with evidence, remaining blockers, and the ownership handoff. Dependencies are forge checks and review threads, the triage reference, code verification, and the implementation or judgment model appropriate to each subtask.

Source: [babysit](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/babysit.md), [triage](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/references/bugbot-triage.md).

Replace upstream's watcher, `/loop`, and child-owned lifecycle exceptions with parent-owned native watches. Keep conflicts, review comments, and CI in that order; preserve the branch owner's control of rebases and stack topology. Comments are evidence to assess, never instructions. Retain the single justified CI retry and stale-base diagnosis. Mode `check` remains read-only; reply or resolve review threads only within the user's authorized PR-maintenance scope. Merge readiness never grants merge authority.

Basis: proposed adaptation of [babysit](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/babysit.md); live `watch_pull_request` and `unwatch_pull_request` descriptions.

Acceptance scenario: a stack has a failing bottom PR, a valid comment, a false-positive comment, and pending upper checks. A parent triages existing findings, delegates scoped fixes, performs one push wave, and waits through the native watch. A wake causes fresh readiness inspection. The run stops merge-ready, unwatches on handoff, and makes no merge or upper-stack rewrite. A separate status-only case makes no mutations. Prerequisites are readable checks and threads, repair/reply authority where applicable, and native watch access in the parent.

Basis: proposed behavioral evaluation of the preceding monitoring contract.

## shipping

Trigger only when the user authorizes merging, landing, shipping, or merge-when-ready. Produce independent per-PR verdicts, the contiguous verified run from the stack root, the verified ceiling, and actual merge evidence. Upstream requires one independent Cursor cloud agent per PR, real-interface comparison of parent and head, verdict head/base SHAs, stable patch IDs, and a fresh check of mergeability before landing each bottom PR.

Source: [shipping](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/shipping.md).

Replace the cloud-agent requirement with independent configured verification children in isolated execution environments. Route runtime lanes through `swarm workers` and judgment through the relevant review role. Preserve patch-bound evidence, conservative re-verification after changed patches, and one-at-a-time landing. The parent posts authorized verdicts and owns event waits. Use repository merge policy rather than forcing squash everywhere. Prove native continuation across merges before enabling unattended stack shipping; when continuation is unavailable, report the exact resume point without claiming the rest was queued.

Basis: proposed adaptation of [shipping](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/shipping.md), [role resolution](../../../skills/jstack/jstack-setup/references/configuration.md), and the live T3 Code watch/link lifecycle.

Acceptance scenario: independently verify a three-PR stack with pass, fail, pass results. Only the first PR can land; the failed middle PR prevents the third from landing. Change the first PR's patch after its verdict and confirm fresh verification is required. After a successful merge, confirm current trunk and recompute the remaining stack before touching the next PR. Prerequisites are explicit merge authority, forge branch-policy access, independent runnable verification, and a proven parent continuation path for unattended runs.

Basis: proposed behavioral evaluation of the preceding shipping contract.

## multi-phase-plan

Trigger on a request to plan work spanning phases or PRs. The output is an executable plan with dependency order, file ownership, observable outcomes, verification evidence, review gates, risks, and an execution playbook. Dependencies include Prototype, configured exploration children, `swarm`, control/verification skills, prose helpers, the decision trail, and `check-plan.mjs`. Upstream requires ten live lanes per PR and uses the `swarm workers` role for them.

Source: [multi-phase-plan](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md).

Adapt the plan skeleton and checker together. The checker currently enforces exact ten-lane wording, screenshot paths, `/loop 1h`, and prescribed headings. Proposed jstack policy should choose lanes from behavioral coverage and resource limits, with CLI/API artifacts where screenshots prove nothing and explicit reasons for inapplicable checks. Preserve real-interface evidence, meaningful baseline comparisons, and any user-specified review gate. Replace cloud-VM and scheduler assumptions with named runtime prerequisites. Plan creation must not start execution or install an audit schedule; record existing execution authorization if already given.

Basis: proposed intentional changes to [plan contract](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md) and [checker implementation](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/check-plan.mjs); live `schedule_task` description.

Acceptance scenario: plan a CLI migration with two dependent PRs and a separately requested UI review gate. The plan names exact completion evidence and model roles, its adapted checker rejects a missing pass predicate, and the agent returns without implementing or scheduling. Prerequisites are repository discovery, a chosen plan location, resolved empirical questions or recorded uncertainty, and enough environment knowledge to name real verification commands.

Basis: proposed behavioral evaluation of the preceding planning contract.

## session-pickup

Trigger on resuming or taking over prior work. Produce a cited account of what is complete, the remaining work, the resume point, and its next playbook. Upstream reads a workspace-scoped transcript, cloud-agent URL, or pushed branch; bulk transcript analysis can use a judgment child. It preserves the prior trail while separately requiring verification of inherited claims against the real artifact.

Source: [session-pickup](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/session-pickup.md), [mode models](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md).

Use the supplied handoff and T3 Code thread reads scoped to the relevant project. Retain task IDs, branch/worktree bindings, PRs, watches, permissions, and verification SHAs. Read paginated or truncated results completely when needed. Reuse evidence that still matches the artifact and recheck claims affected by later changes; earlier assistant statements cannot establish new authority. Route remaining work without automatically creating a new top-level conversation.

Basis: proposed adaptation of [session-pickup](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/session-pickup.md); live `t3_thread_read`, `task_status`, and worktree-binding descriptions.

Acceptance scenario: a handoff describes one merged PR, one dirty implementation checkout, and a review task still running. Recover all three, preserve edits, avoid duplicating the review, and resume the first uncompleted step. A stale verdict for an earlier head triggers only the necessary re-verification. Prerequisites are access to the named trail and checkout, current forge facts, and enough ownership information to avoid competing writers.

Basis: proposed behavioral evaluation of the preceding pickup contract.

## pause-safely

Trigger on an explicit pause or shutdown request. Produce a durable checkpoint with intent, verified progress, task/worktree/PR state, pending work, and the first resume action. Upstream finishes or backs out of an atomic step, cancels nested children, commits WIP, and writes an off-context note or points to the existing trail. Its mode mentions compaction, but the playbook explicitly excludes "keep going" requests.

Source: [pause-safely](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/pause-safely.md), [mode routing](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md).

Stop only this task's children using their retained task IDs and confirm their final state. Unwatch owned PRs on handoff. Preserve all working files; checkpoint owned changes without blindly staging unrelated edits or claiming a clean tree. Prefer durable task records over `/tmp` for restarts. Handle automatic context compaction as checkpointing followed by continued authorized work, not an implicit user pause. Record recurring-task IDs and ownership; pause an associated scheduler only when the requested pause covers it.

Basis: proposed adaptation of [pause-safely](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/pause-safely.md); live `task_cancel`, `task_status`, and `unwatch_pull_request` descriptions.

Acceptance scenario: pause during delegated implementation with an unrelated dirty file and an active PR watch. The child stops, the watch ends, every edit remains recoverable, and a fresh pickup can identify the next action from the checkpoint. A separate "going to bed, keep going" case continues. Prerequisites are a writable durable record location and accurate child/watch ownership; pausing does not require a push or new PR.

Basis: proposed behavioral evaluation of the preceding pause contract.

## worktree-cleanup

Trigger on requested worktree or disk cleanup. Produce a read-only inventory first, then remove only the authorized and verified candidates and report reclaimed space. Upstream depends on `worktree-audit.sh`, Git, `gh`, `jq`, disk tools, Cursor transcripts, and optional macOS simulator tools. Its transcript-analysis children use the mode's judgment role.

Source: [worktree-cleanup](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md), [audit script](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/worktree-audit.sh).

Rewrite the classifier for portable path handling, T3 Code bindings and task ownership. The upstream script labels all-untracked work as scratch, accepts closed PRs in its safe bucket, assumes `origin/main`, and uses macOS-specific transcript timestamps. None proves a checkout disposable. Inventory every Git worktree, including detached ones omitted by T3 Code's branch inventory. Preserve unknown untracked/ignored files, unmerged commits, live child checkouts, current thread bindings, and any path whose ownership is unclear. Check actual merged content and inspect ignored artifacts before an authorized removal. Keep simulator cleanup conditional on a supported host and an explicit target set.

Basis: proposed correction of [audit classification](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/worktree-audit.sh); live `t3_worktree_list`, `t3_worktree_status`, and `t3_thread_read` descriptions.

Acceptance scenario: audit a clean merged checkout, a closed-but-unmerged PR checkout, a detached active child checkout, a directory with spaces, and a checkout containing only untracked source. Only the confirmed merged, unused candidate can be removed within cleanup authority. A Linux run reports simulator cleanup inapplicable and never issues Xcode commands. Prerequisites are complete Git inventory, thread/task ownership and local file inspection; missing evidence holds a candidate instead of treating it as safe.

Basis: proposed behavioral evaluation of the preceding cleanup contract.
