# Juan-mode autonomy, prototyping and evaluation inventory

Assessed on 2026-10-11 at upstream commit `11713c683fe4add4fd403ea880580abbc9e0875f`. This covers seven of the 23 playbooks in the agreed target. The proposed adaptations below require implementation and behavioral checks before release. Reading upstream instructions grants no execution authority.

Source: [upstream router][mode], [local permission boundary][config].

## Common dependencies and constraints

Keep the playbooks and shared helper protocols inside `juan-mode` for a complete package. `figure-it-out` designs a bespoke workflow when a route does not fit. `swarm` covers or races work and reports gaps. `arena` produces competing artifacts, cross-judges, selects and combines them. Their configured roles already exist; each protocol needs one canonical definition. Their upstream standalone invocation contracts make them later extraction candidates, without requiring separate installations now. Discover the shipped `setup-jstack` resolver through the skill catalog as the explicit runtime dependency.

Source: [figure-it-out][figure], [swarm][swarm], [arena][arena], [role registry][roles].

Load and validate the entire saved role map before dispatch. Preserve list lengths, inherited seats and options; an unavailable model is a configuration failure. `swarm workers` is one default seat, not a worker count. `arena cross-judge pool` supplies one selected judge. A valid inherited-only configuration does not guarantee a different-family judge. Report that unmet requirement rather than choosing an unrequested model or describing self-review as independent review.

Source: [configuration consumer contract][config], [swarm][swarm], [arena][arena], [decision-trail review][trail].

Use explicit child briefs with goal, allowed paths, output, checks and current context. T3 Code `delegate_task` copies no parent history and exposes no Cursor `environment`, `cloud_base_branch` or worktree-binding argument. Prepare exclusive paths or worktrees when needed and name them in the brief; verify access before writing. Prefer supported native delegation for a matching same-provider model, otherwise use T3 Code delegation. Never launch provider agents through shell commands or create top-level conversations merely to obtain child isolation.

Source: live `delegate_task` schema inspected on 2026-10-11; [T3 Code integration contract][t3], [upstream brief and placement][orchestrate].

Retain each delegated task ID and its artifact location. An asynchronous completion wakes its parent; waiting timeout alone does not cancel the child. `task_status` distinguishes live nested work from a completed turn and reports later pending runs. New review rounds need fresh tasks with consolidated context and a new retry-stable request ID. Cancel obsolete tasks before replacing their writable scope; if stopping cannot be confirmed, isolate the replacement and reject late writes against stale revisions. Reconcile all children before completion or handoff.

Source: live `delegate_task`, `task_status` and `task_cancel` descriptions inspected on 2026-10-11; [upstream lifecycle][orchestrate].

The parent owns PR linking, PR watches and wake handling. T3 Code forbids child-owned `watch_pull_request`; its watch delivers changes without a custom polling process and ends on stop, settlement or closure. Model configuration and a playbook name authorize no merges, communications, installations or recurring work. A requested persistent audit cadence needs an explicit schedule scope and cancellation contract; ordinary routes can use task completions and PR events without creating a schedule. No weekly-review schedule changes belong to this adaptation.

Source: live `watch_pull_request`, `unwatch_pull_request` and `schedule_task` descriptions inspected on 2026-10-11; [configuration permission boundary][config], [local delivery decisions][decisions].

Reuse one append-only decision-trail contract across long runs, including evidence pointers, run ownership and superseding corrections. The small `log.sh` helper handles tabs, newlines and spreadsheet formula prefixes. Upstream also demands transcript auditing and a different-family review. T3 Code's messages and summarized activity views do not establish raw tool-call coverage by themselves. Adapt the audit to the current run's available evidence and label missing trace evidence. `reflect` is a separate reusable retrospective candidate, not permission to edit global skills or file tracker items automatically.

Source: [trail skill][trail], [log helper][log], [reflect][reflect], [reflect synthesis][reflect-synthesis]; live `t3_thread_read` description inspected on 2026-10-11.

`orch` owns bookkeeping, not agent launching. Its plain-file units, ledger and atomic updates are useful, but its frontier resolver requires Graphite output and PID locks assume one host. Its bootstrap installs Bun dependencies automatically. `check-plan.mjs` hardcodes hourly `/loop` and exactly ten screenshot lanes even for plans whose risks differ. Adapt the store and checker contracts deliberately; copying these scripts would import undeclared tool, installation and workload requirements.

Source: [orch CLI][orch], [store frontier and locks][store], [bootstrap][bootstrap], [plan checker][check-plan].

## autonomous-run

Trigger on one sustained task with a checkable exit condition, such as fixing a reproduction and keeping its behavior verified. Output the predicate, iteration results, retained and discarded changes, and evidence for the final state. Dependencies are the relevant task playbook, verifiable-unit discipline and the shared decision trail. Resolve the underlying task's implementation role, using `hardest tasks` only for that difficulty and `judgment and prose` for delegated judgment.

Source: [autonomous run][autonomous], [mode role mapping][mode], [local role registry][roles].

Adapt Cursor `/loop` to task completion and parent-owned PR events. Continued work remains inside the agreed objective; an adjacent bug is not automatic permission for unrelated PRs. An authorized recurring run can use a separately scoped T3 Code schedule with recorded ownership and teardown. A missing wake mechanism is a reported limitation, not a reason to install a hidden heartbeat.

Source: proposed adaptation of [autonomous run][autonomous]; live `schedule_task` and `watch_pull_request` contracts inspected on 2026-10-11.

Accept when a failing sample reproduction becomes passing, one ineffective attempt is discarded without touching pre-existing work, each iteration has evidence, and the run stops at the original predicate. A second case with a blocked external prerequisite must preserve a resumable record and report incomplete. Prerequisites are task dispatch, owned-change tracking, decision logging and event handling; indefinite unattended runtime remains unproven.

Source: proposed acceptance cases derived from [autonomous run][autonomous] and [decision trail][trail].

## orchestrate

Trigger on a standing program that exceeds one agent's session budget. Output durable units, briefs, child states, verification ledger, branch/PR ordering, decision trail and remaining gates. The coordinator owns decomposition and integration decisions; workers and verifiers own scoped code and proof. Dependencies include `figure-it-out` boundaries, `arena` for disputed design, the trail, `orch`, and delivery playbooks. Resolve task-specific workers, `swarm workers` for parallel verification, `arena` seats for design, and `judgment and prose` for delegated coordination.

Source: [orchestrate][orchestrate], [figure-it-out][figure], [role registry][roles].

Replace assumed cloud workers, nesting depth and fixed concurrency with observed T3 Code capabilities and an explicit in-flight budget. Keep one writer per worktree and topology. Use task IDs and event-driven drains rather than Cursor agent IDs and `/loop`. Replace the Graphite-only frontier with an explicit supported Git/forge adapter before enabling this route; retain verdicts keyed to PR and head SHA. A restart must reconcile real child and branch state, without assuming all local children died or all remote children survived.

Source: proposed adaptation of [orchestrate][orchestrate], [store][store] and [T3 Code integration][t3]; live delegation/status descriptions inspected on 2026-10-11.

Accept with a three-unit sample dependency graph whose pilot finishes before broader dispatch, whose late stale result cannot overwrite a newer unit, and whose rewritten head loses its old verdict. Interrupt and resume the coordinator, then prove every child and unit is accounted for with no duplicate writer. Prerequisites are the durable state model, idempotent drain/claim behavior, explicit stack adapter, child reconciliation and an authorized landing policy. Multi-day durability needs a live restart trial.

Source: proposed acceptance cases derived from [orchestrate queue, stack safety and liveness][orchestrate] and [store implementation][store].

## autopilot-full

Trigger on a queue of independent PRs with explicit landing authority. Output owner and head per PR, independent verdicts, landed work, held operator items and decision trails. Dependencies include Feature/Bug fix, PR creation, Babysit, Shipping, `swarm`, the trail and skeptical review triage. Resolve owners through their implementation role and hard-task override; verification uses `swarm workers` and configured judgment roles where needed. Upstream assigns owners the build-through-merge role and the root the final verification decision.

Source: [autopilot-full][full], [swarm][swarm], [mode roles][mode].

Keep an owner as a logical responsibility across fresh delegated rounds. Move watch registration and event routing to the parent, since T3 Code children cannot watch PRs. Record the exact verified head and recheck affected behavior after rebases or changed patches; a green check alone is insufficient. Link every worked PR. Require the user's actual merge grant and respect named holds. Hourly audits and early ready-PR publication become explicit run policy rather than automatic side effects of routing.

Source: proposed adaptation of [autopilot-full][full] and [local authority boundaries][decisions]; live PR-watch and delegation contracts inspected on 2026-10-11.

Accept in an isolated forge exercise with two independent changes and an operator-held item. An injected defect must block its PR while the other advances. A later patch must invalidate the relevant verdict, and an operator stop must cancel active child work and watches, reconcile any in-flight writes, and prevent another dispatch. The held item must remain unmerged. Prerequisites are branch ownership, complete reviewer coverage, parent wake routing, scoped merge authorization and a tested stop/replacement protocol.

Source: proposed acceptance cases derived from [autopilot-full][full] and [swarm coverage semantics][swarm].

## autopilot-stack

Trigger on a queue to build and verify for the operator to land. Output one linear base-branch stack, exact heads, per-link proof and exclusions. It shares owner, trail, swarm and review dependencies with Autopilot-full, but the parent alone changes stack topology. Resolve owners and verifiers through the same existing roles. The upstream contract forbids owners from merging, arming auto-merge or closing PRs.

Source: [autopilot-stack][stack], [autopilot-full][full], [role registry][roles].

Use Git and the selected forge to maintain explicit branch-parent relationships. T3 Code links and watches every layer from the parent. Record topology changes and revalidate CI, mergeability and affected verdicts after a restack. Keep merge authority absent throughout this route, even if the user's broader wording says full autonomy. Replace its automatic hourly `/loop` with the explicit audit policy described above.

Source: proposed adaptation of [autopilot-stack][stack]; live parent-owned PR-watch contract inspected on 2026-10-11.

Accept with three sample PRs targeting trunk, then their preceding branches. Move the base, restack bottom-up with one topology writer, and verify that stale verdicts cannot mark rewritten code ready. Finish with three linked, verified, open PRs and no merge or auto-merge calls. Prerequisites are the same owner/reviewer lifecycle as Autopilot-full plus a tested topology ledger, scoped branch rewrite handling and Shipping's verdict-transfer rules.

Source: proposed acceptance cases derived from [autopilot-stack][stack] and [autopilot-full review rounds][full].

## prototype

Trigger on a throwaway design or empirical question that an observation can settle. Output compared alternatives, observed evidence, tradeoffs, a recommendation and the scratch artifact path. Dependencies are the matching runtime control, design-space exploration and the later Feature or `architect` handoff. No dedicated prototype role exists; use the current agent or the appropriate configured implementation/design seat when delegation is useful.

Source: [prototype][prototype], [mode triggers][mode], [role registry][roles].

Use a task-owned scratch directory and the smallest runnable artifact. Prefer T3 Code preview for browser interaction and screenshots; use `html_preview` then `html_render` for an inline visual comparison. A behavioral question may need only a script and recorded output. Preserve the distinction between observing a prototype and verifying production code. The selected direction enters Feature only when implementation is in scope.

Source: proposed adaptation of [prototype][prototype]; live `preview_status`, `html_preview` and `html_render` descriptions inspected on 2026-10-11.

Accept when two labeled UI alternatives or two behavioral implementations answer one stated question with real observations, while production source remains unchanged. A request for a cited read-only explanation must stay Investigation instead. Prerequisites are a usable scratch location, matching runtime access and evidence capture; unsupported simulator or desktop access must be reported without claiming visual verification.

Source: proposed acceptance cases derived from [prototype][prototype] and [read-only exception in the router][mode].

## eval

Trigger on measuring an agent's response to a skill, prompt or structure change before promotion. Output the hidden rubric, sanitized per-candidate artifacts, blinded judge result, the parent's synthesis and a promotion recommendation. Dependencies include Arena candidate dispatch/cross-judging and actual output/transcript inspection. Resolve `arena runners` and one seat from `arena cross-judge pool`, checking the required model-family distinction before starting.

Source: [eval][eval], [arena][arena], [configuration panel semantics][config].

Create project-shaped candidate directories and organic task prompts with no judge rubric or comparison labels. Use delegation without parent-history inheritance. Give the judge completed outputs under neutral labels, without model identities. T3 Code summarized activity is not proof of every file read; capture permitted run-specific evidence, or mark the chain-following result unverified. Access no unrelated conversation histories. Promotion remains a separate decision supported by results.

Source: proposed adaptation of [eval][eval]; live `delegate_task` and `t3_thread_read` contracts inspected on 2026-10-11.

Accept with one ordinary coding request run against two skill variants in isolated fixtures, one failing a concrete rubric criterion. Verify candidate prompts and files cannot expose the hidden rubric, let one blind judge score both, then inspect the artifacts directly. Missing tool-read evidence must produce an explicit coverage gap. Prerequisites are candidate isolation, a private judge context, evidence collection and configured judge diversity; rubric validity requires a pilot before interpreting results.

Source: proposed acceptance cases derived from [eval][eval] and [arena][arena].

The [Eval procedure](../../../skills/jstack/jstack-juan-mode/playbooks/eval.md) is now bundled. Its [bounded evaluation](../evaluations/eval/README.md) records configuration, blinding and transcript-evidence limits. Repeated inherited seats do not establish distinct models; missing diversity stops the comparison before dispatch.

## authoring-a-skill

The [implemented procedure](../../../skills/jstack/jstack-juan-mode/playbooks/authoring-a-skill.md) triggers on creating or editing a `SKILL.md`. Output the authored package, rationale for its instructions and validation evidence. Upstream depends on Cursor's built-in `create-skill`, relevant principle leaves and Opening a PR. Adapt authoring to available skill-creation and agent-writing guidance; `judgment and prose` is the existing role for a delegated draft, and structural helper code uses the corresponding implementation role.

Source: [authoring-a-skill][authoring], [mode roles][mode], [local role registry][roles].

Validate required frontmatter, referenced files, independently installed helper discovery and applicable behavior cases. Replace Cursor mode metadata and authoring tools with the selected provider's supported contract. Keep publication aligned with the requested delivery; authoring does not require a PR, merge or installation on every invocation. Skill installation remains manual under jstack's established policy.

Source: proposed adaptation of [authoring-a-skill][authoring], [setup discovery conventions][setup] and [local delivery decisions][decisions].

Accept when a small sample router resolves its packaged references after independent installation layout is simulated, while a deliberately broken helper reference fails validation. A behavioral routing change must select the correct playbook on contrasting requests. A wording-only edit needs document validation rather than invented runtime tests. Prerequisites are an explicit authoring dependency and package/link validation. Structural edits require behavior cases; the separate Eval procedure remains pending and is not required by this source playbook. See the [bounded authoring evaluation](../evaluations/authoring-a-skill/README.md).

Source: proposed acceptance cases derived from [authoring-a-skill][authoring], [eval][eval] and [setup dependency handling][setup].

## Evidence inspected

Read the full mode file, all seven playbooks above, full `figure-it-out`, `swarm`, `arena`, `reflect` and `show-me-your-work` skills, Reflect's synthesizer, `log.sh`, `bootstrap.ts`, `check-plan.mjs`, and `orch.ts`. Inspected `store.ts` locking, frontier resolution and writes rather than claiming a full store audit. Read local setup instructions, configuration/T3 Code references and the role registry. Live capabilities confirmed exposed child-task, cancellation, thread-read and scheduling features; this read-only assessment did not test provider execution, persistent scheduling, nested recovery or any workflow implementation.

Source: linked immutable files below; live `orchestrator_capabilities` payload and cited tool descriptions inspected on 2026-10-11.

[mode]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md
[autonomous]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autonomous-run.md
[orchestrate]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/orchestrate.md
[full]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-full.md
[stack]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/autopilot-stack.md
[prototype]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/prototype.md
[eval]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/eval.md
[authoring]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md
[figure]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/figure-it-out/SKILL.md
[swarm]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/swarm/SKILL.md
[arena]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/arena/SKILL.md
[reflect]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/reflect/SKILL.md
[reflect-synthesis]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/reflect/references/synthesizer.md
[trail]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md
[log]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/scripts/log.sh
[orch]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/orch/orch.ts
[store]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/orch/store.ts
[bootstrap]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/bootstrap.ts
[check-plan]: https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/scripts/check-plan.mjs
[config]: ../../../skills/jstack/jstack-setup/references/configuration.md
[t3]: ../../../skills/jstack/jstack-setup/references/t3-code.md
[roles]: ../../../skills/jstack/jstack-setup/scripts/models.py
[setup]: ../../../skills/jstack/jstack-setup/SKILL.md
[decisions]: ../decisions.md
