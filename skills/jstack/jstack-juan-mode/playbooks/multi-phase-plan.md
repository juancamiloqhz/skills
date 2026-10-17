### Multi-phase or multi-PR plan

**You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence.** The plan is the deliverable. Do not implement. Planning does not authorize execution, publication, merge, installation or a recurring schedule. Record existing execution authority separately; a request for a plan alone is not a go.

1. When the change is one or two files with an obvious approach, skip the plan. Say so and stop.
2. Settle open questions by prototype before you write. Run [Prototype](prototype.md) for each within the authorized exploration scope. An unavailable experiment stays unproven in Appendix A and blocks any dependent execution claim. Keep the branch, the SHA, and the screenshots for Appendix A. Ask the operator only about a product or preference call that no run can settle. Give options (the **jstack-principle-never-block-on-the-human** principle skill).
3. Explore in fresh read-only subagents using the configured investigation roles and preflight in the Subagents section. Pass the resolved absolute configuration path, exact checkout/revision, scope and output location. Use native children when they support the selected target, otherwise T3 `delegate_task`. A separate checkout requires `isolation: "worktree"`. Preserve model and effort (the **jstack-principle-guard-the-context-window** principle skill). Each returns file pointers, conventions, test commands, and entry points. No inlined dumps.
4. Copy the skeleton below into the plan file and fill every placeholder. Unless the operator names a path, write the file under `<project-root>/.jstack/docs/`, the project-local plan store. Choose a descriptive filename and preserve existing plans. Keep every heading and every sub-block in the order shown. One section per PR. One PR is one change with its own evidence (the **jstack-principle-sequence-verifiable-units** principle skill). Name the execution playbook in **How to read this**. Choose `playbooks/autopilot-full.md` for independent PRs with landing authority. Choose `playbooks/autopilot-stack.md` when review before landing is required, work is sequenced or coupled, or merge authority is withheld. A standing program takes `playbooks/orchestrate.md`. These three execution procedures are not yet bundled. Name the intended route and mark execution blocked until its procedure and prerequisites are available; do not invent or run its lifecycle. Planning can still finish with that limitation stated.
5. Write under the discovered **jstack-technical-writing** skill in full, then its validated **unslop** dependency. The body is one Diátaxis mode, how-to. Appendices hold explanation and reference. Each heading states the task or the finding. No long dashes. No mid-sentence colons.
6. Run `node <juan-mode-root>/scripts/check-plan.mjs <plan.md>` from the discovered package and fix every line it prints. A zero result checks document structure only; manually inspect unresolved placeholders, dependencies, source paths, meaningful predicates, feasibility and evidence. It proves neither execution readiness nor completed verification (the **jstack-principle-encode-lessons-in-structure** principle skill).
7. Hand back. Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go, under the available execution playbook the plan names. Report missing procedures or capabilities as blocked prerequisites. Do not create a timer while writing the plan.

**Verification.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked (the **jstack-principle-prove-it-works** principle skill). That sentence is the verification rule. Every verification block opens with it. The live block is mandatory. Ten lanes at the PR head drive the real surface through its control skill, per the **jstack-swarm** skill, on the resolved `swarm workers` target. Record the effective provider, model and effort, including inherited selections. Keep all ten lanes; batch dispatch when host concurrency is lower rather than reducing coverage. Each lane still needs isolated state and its own evidence. Each lane is one box with a concrete scenario, the screenshot it saves, and its pass predicate. One lane is the **Regression lane against trunk.** It runs the same load-bearing scenario on trunk and head. If trunk does not have the feature, the lane records that fact and gates the behavior the diff adds plus the end state the user waits for instead of inventing a trunk result. The perf gate is dual-sided. Trunk and head must both produce the named metric. If trunk lacks the feature, also isolate the work the diff adds and set an absolute budget for that work plus the end-to-end state the user waits for. Do not claim a ratio between unlike scenarios. The perf block names the metric, the interleaved probe, the trunk baseline measured first, and the rule with the number that fails. A PR that changes an interaction is review-gated. The operator reviews it in chat with screenshots and a video before merge. A PR that changes no interaction writes `**Review gate.** None. <PR id> is not review-gated.` and no boxes under it.

**Control skill.** Pick it by surface. Browser, Electron, and web UIs use the discovered `jstack-control-ui` skill. CLIs and TUIs use the discovered `jstack-control-cli` skill. Native mobile uses whatever simulator-driving skill the repo has. A PR that touches two surfaces gets lanes on both. A surface with no control skill is a risk in Appendix C, and its live block still names how each lane drives it.

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `<juan-mode-root>/playbooks/<execution playbook>.md`. <State whether this procedure is available. If absent, execution is blocked.> <Who merges, and which PR ids are the operator's items that stop at merge-ready.>

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] Read current sources at program start and every tick. Use `git show origin/main:<path>` for sources tracked in this repository. For independently installed packages, discover their absolute paths, read them from disk and record the version or content identity. An unavailable procedure blocks execution.
  - [ ] `<read command for the execution playbook>`
  - [ ] `<read command for jstack-swarm/SKILL.md>`
  - [ ] `<read command for the control skill>`
  - [ ] `<read command for juan-mode/playbooks/opening-a-pr.md>`
  - [ ] `<read command for each other discovered leaf skill>`
- [ ] Only after execution and recurring audits are authorized and the execution procedure is available, register the hourly audit with T3 `schedule_task` using `schedule={"type":"interval","everyMs":3600000}` and the tick prompt below, bound to this conversation. Record the returned task ID, cadence and next run time. Check for an existing owned timer before creating one. Missing scheduling support blocks unattended audits; do not substitute a shell loop.
- [ ] Use this tick prompt, verbatim. "Re-read the current execution playbook from its recorded source. Audit the operation against it and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then post a short status message to the operator in chat only when the audit found a tracked change that no earlier status message reported, such as a PR opened, a code-ready head, a round launched or closed, a verdict, a merge, a stuck agent and the action taken, a blocker added or cleared, or a decision only the operator can make. Name every such change and nothing else. Do not repeat a table, the merged list, or an unchanged blocker. If the audit found none, end the turn with no reply text. Either way, log this tick's row in your decision trail. The row names the items reported, or none."
- [ ] On the operator's hold or stand-down, stop each owned child through the supported cancellation tool and verify its terminal state. Pause the owned audit schedule when the requested hold covers it. Preserve recoverable work and unrelated tasks.

### Spawn owners

- [ ] Spawn one owner per PR with the full lifecycle the available execution playbook names, in its own T3-bound worktree through `delegate_task` with `isolation: "worktree"`. Retain task IDs and workspace bindings. Uncommitted parent edits are not copied.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Resolve the forge once. Default to `gh`; if `command -v origin` succeeds and Origin can resolve the repository, use `origin pr` for every PR operation. Record any fallback to `gh`. Never require `gt`.
- [ ] Open the PR ready by default per **Opening a PR**, honoring an explicit user-selected draft or local-only boundary. Use the run's built-in PR tool when it has one, else `origin pr create --status open --base <base-branch>` or `gh pr create --base <base-branch>` according to the resolved forge. A stack child targets its parent branch. The T3 parent links every worked PR immediately and owns native watches. On handoff, reconcile links and unwatch scoped PRs.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Run `/jstack-deslop` before each commit and `/jstack-no-comments` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `<juan-mode-root>/references/bugbot-triage.md` within the actual reply and resolution authority.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that merge base in fix rounds. Rebase again only at merge prep, on a `git merge-tree` conflict with trunk, or on a CI failure that comes from a change on trunk.

### Verdict and merge, for every PR

- [ ] At the code-ready head SHA and at each later push that changes the patch, run the swarm per the discovered `jstack-swarm/SKILL.md`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. Two or more audit lanes, each with its own focus, that read the diff and the receipts and distrust the PR body. The root audits the receipts in the merge-ready report before the verdict.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner, including a defect that a lane filed as a note. A new head gets a fresh swarm and a fresh verdict, except for results that stay valid under the patch-id rule in `<juan-mode-root>/playbooks/shipping.md`.
- [ ] <The merge or append rule from the execution playbook, with the patch-id rule from `<juan-mode-root>/playbooks/shipping.md`.>

### Boot recipe, for every live lane

Each live lane runs in its own T3-bound worktree at the PR head, with separate ports, data and owned processes. A worktree is not a cloud VM. If shared host resources prevent the required isolation or comparable performance measurement, record that prerequisite as blocked. Drive through the discovered `jstack-control-ui` or `jstack-control-cli` skill.

- [ ] Inspect status and ownership in the assigned worktree, then `git fetch origin <head-branch> && git checkout <head SHA>`. Confirm the actual revision before starting processes and preserve unrelated work.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report. Keep screenshots and raw logs in owned scratch, preserve evidence needed for review, and stop owned processes after capture.

## <Task as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `<swarm workers model>` at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run <the same load-bearing scenario> at trunk and head. If trunk lacks the feature, record that and gate <the behavior the diff adds plus the end state the user waits for>. Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>

**Review gate.** The operator reviews before merge.

- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change in an isolated lane. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] <The owner squash-merges its own PR, or the root appends it to the base-branch stack and the operator lands it bottom-up.>

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get the discovered `jstack-how/SKILL.md` and `jstack-interrogate/SKILL.md`. The trail per the discovered `jstack-show-me-your-work/SKILL.md`.>
````

**Reply:** the plan path, the PR ids with their dependencies and the review-gated set, what the prototypes proved and what stays unproven, and the check script's output.
