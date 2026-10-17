# Juan-mode adaptation specification

Current jstack skill identities use the `jstack-` prefix. See the [name mapping and manual migration guide](skill-names.md). Earlier assessments and evaluation artifacts retain their original names; current local links point to the renamed packages.

For jstack implementation and maintenance, follow the [upstream-fidelity policy](upstream-fidelity.md). Preserve upstream structure by default and document only necessary or explicitly approved deviations.

Drafted on 2026-10-11 against `cursor/plugins` revision `11713c683fe4add4fd403ea880580abbc9e0875f`, using the source fetched for that assessment. Updated on 2026-10-15 to reconcile merged fidelity corrections through PR #37. The [current fidelity status](fidelity-status.md) supersedes stale packaging and redesign proposals in the initial inventories. This is an implementation specification, not a shipped skill or a report of successful workflow execution. The [initial assessment](juan-mode-adaptation.md) supplies context; the inventories below record the complete playbook review.

## Scope and accepted behavior

The user approved assessing and designing for all 23 poteto-mode playbooks, then implementing and verifying them in manageable groups. This supersedes the earlier three-playbook first-release plan. Implementation order does not reduce the release target. A reduced release or an omitted playbook requires an explicit scope decision.

The user also selected conversation activation. An explicit invocation activates jstack-juan-mode for subsequent tasks in that conversation until the user turns it off. Finishing a task does not deactivate the mode. Turning the mode off removes its routing and working-style instructions; stopping ongoing work is a separate request. New conversations do not inherit activation automatically. A delegated child receives the instructions needed for its assigned work, not permission to start an independent program.

The scope is adapting the complete working approach and playbook set to T3 Code. It does not require reproducing Cursor's UI, copying its tool infrastructure, or making every pstack skill independently installable. Platform-specific capabilities remain explicit prerequisites. A blocked browser, profiler, simulator or review configuration must produce a precise limitation rather than a fabricated completion.

## Complete playbook inventory

Each inventory entry records its trigger, deliverable, dependencies, T3 Code changes and an acceptance scenario. These are source assessments and proposed checks, not test results.

- [Engineering inventory](juan-mode/engineering-inventory.md) covers 9 playbooks: Investigation, Feature, Bug fix, Refactoring, Perf issue, Hillclimb, Runtime forensics, Trace forensics and Visual parity.
- [Delivery inventory](juan-mode/delivery-inventory.md) covers 7 playbooks: Opening a PR, Babysit, Shipping, Multi-phase plan, Session pickup, Pause safely and Worktree cleanup.
- [Autonomy and tooling inventory](juan-mode/autonomy-inventory.md) covers 7 playbooks: Autonomous run, Orchestrate, Autopilot-full, Autopilot-stack, Prototype, Eval and Authoring a skill.

The authoritative upstream set is the [pinned playbook directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks). Before implementation and release, compare its filenames with the supported-route registry. Every source playbook needs an implementation, an acceptance result and documented differences. Extra routes must have their own justification.

## Packaging

Use one installable `jstack-juan-mode` skill containing the entrypoint, all 23 playbook files, shared workflow references, principle discovery, prompt templates and the small scripts that its behavior requires. Playbooks remain internal procedures, not separately installed skills. Keep the entrypoint focused on activation, routing, shared rules and completion requirements; read detailed material only when its route needs it.

Package `jstack-how` and `jstack-why` as standalone jstack skills, matching pstack's independent invocation boundary. This replaces the initial bundled-reference choice by user decision on 2026-10-12. Users can invoke either directly without activating or installing jstack-juan-mode; implemented playbooks discover them through the current skill catalog and pass their task scope and absolute model-config path. Both depend on jstack-setup for the canonical resolver and shared investigation contract. Arena also has an independent invocation boundary and is implemented as a standalone skill discovered by callers; its design-only return supports Architect. Architect also ships as a standalone skill because users can request architecture design independently and playbooks need a design-only return. It discovers how, conditional why and Arena, selecting the configured architect panel. Interrogate ships independently for report-only code and design review, using its configured reviewer panel and lead judgment. Swarm ships independently for partitioned coverage and races, using a scalar configured worker default, validated explicit task-local arm selections, task-derived count and verified aggregation. Reflect ships independently because users can request a retrospective directly and playbooks need bounded learning proposals. It uses three reviewers and a separate synthesizer with two scalar configured roles. Figure-it-out ships independently because a user can request a custom workflow without activating the mode. It calls the standalone `jstack-show-me-your-work` skill for its decision trail and discovers seven relevant standalone principle skills. By user decision, all 24 principles ship as independent `jstack-principle-*` skills, replacing the initial internal-reference packaging. Juan-mode discovers them through its upstream-organized Principles section. Preserve each procedure's roles and algorithms.

Keep `jstack-setup` as an explicit runtime dependency for its canonical configuration validator and resolver. Resolve its actual installation directory through the provider's skill catalog. Do not assume it is a filesystem sibling of `jstack-juan-mode` or copy `models.py` into another independent implementation. If the dependency cannot be found, explain the missing installation and retain the existing model configuration. Installations remain manual. The first implementation group must prove discovery with separately installed skill directories.

Existing project verification is an input to the playbooks. `jstack-create-verification-skill` and `jstack-maintain-verification-skill` stay separate skills, reached only for an appropriate generation or maintenance task. Running an existing verifier does not require generating another one.

Current package layout with planned playbooks shown explicitly. Add upstream supporting paths when their consuming procedure is implemented; do not introduce a replacement workflow-reference layout solely for organization:

```text
skills/jstack/jstack-juan-mode/
  SKILL.md
  playbooks/                 # Nineteen procedures implemented; 4 pending
  references/bugbot-triage.md # restored upstream reference
  references/activation.md   # local conversation-state contract
  references/configuration.md
  references/execution.md    # local T3 execution contract
  scripts/preflight.py
  scripts/test_preflight.py
  LICENSE
```

Source pins and adaptation records live in `research/jstack/adaptations/` and the upstream manifest. Each installed package retains its license.

## Activation and routing

At explicit activation, read the entrypoint and identify the current thread. Record that jstack-juan-mode is active in the conversation's working state and preserve that fact in handoff and compaction summaries. On a new task, select a fresh playbook rather than treating the request as another step of the previous one. Casual conversation need not start a playbook. User opt-out takes effect immediately and must survive the same resume paths as activation.

The [upstream guide](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/docs/guide/02-poteto-mode.md) attributes persistence to Cursor Custom Mode. The inspected T3 Code thread configuration and metadata tools do not expose an equivalent per-thread skill-injection setting. A local state file or `mode: true` frontmatter alone cannot make the host load a skill. The implementation must verify how each supported provider retains or reloads the activation instruction across later turns, compaction and session resume. If that cannot be demonstrated, persistent activation remains an unresolved release requirement for that provider. Do not replace the requested behavior with task-only activation without agreement.

Routing respects the requested outcome. Diagnosis-only Runtime and Trace forensics return findings; a fix request adds a separate implementation route. Investigation remains read-only. A routine implementation does not automatically start PR monitoring or authorize merging. Explicit shipping and autopilot requests carry their stated delivery authority. Large tasks can use the adapted `jstack-figure-it-out` procedure to compose a bounded plan; standing programs use Orchestrate. Unsupported prerequisites stop the affected operation with completed evidence and the missing capability identified.

A shared helper needs a clear return boundary. In particular, the upstream `architect` skill includes implementation stages, but Feature calls it for design before delegating implementation. The adapted helper must support a design-only result so implementation occurs once. A coordinator owns final synthesis and checks each child result against source or artifacts.

## Configuration and delegation

Every new routed task loads the current jstack model configuration and validates the whole map against live `orchestrator_capabilities` before dispatch. Follow the [existing contract](../../skills/jstack/jstack-setup/references/configuration.md): preserve the 17 roles, list order, concrete options and inherited selections. Never silently substitute upstream model defaults, rewrite routing preferences or switch the current conversation's model.

The accepted project-configuration extension selects one complete file with precedence explicit path, `JSTACK_CONFIG`, `<project_root>/.jstack/models.json`, then XDG global defaults. Setup owns this lookup. Retain the selected absolute path for children and task phases in other worktrees, while new tasks repeat lookup in their project context. Partial or invalid project files are errors, not requests to merge or fall back to the global role map.

Implementation playbooks use their configured roles: `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` and `hardest tasks`. Shared helper procedures use their existing explorer, synthesizer, runner and reviewer roles. Roles for procedures without dedicated assignments must be specified using the existing relevant role or explicit parent inheritance; avoid inventing hidden model defaults. The inventory records route-specific mappings.

Check execution capability separately from configuration validity. A model may be listed while its provider cannot run a child. Likewise, a valid one-seat panel does not satisfy a procedure requiring two independent designs, or a cross-family judge. Resolve effective inherited selections before claiming diversity. Preserve configured fan-out. When a required count or diversity is missing, report the precise role and requirement and request a routing adjustment instead of adding paid runs or models silently.

Use native same-provider children when they support the selected model and required lifecycle. Otherwise use T3 Code `delegate_task`, including for cross-provider work. Each brief includes the original goal, later constraints, selected workflow, owned paths, permitted actions, required evidence, relevant prior findings and exact completion criteria. The tool does not copy the parent conversation. Pass source pointers with enough explicit context to make them useful.

Ordinary playbook children read the full discovered jstack-juan-mode style and applicable principle leaves; specialized workflows keep their own child briefs. That read does not activate persistent mode or enlarge task authority. New work, fixes, follow-ups, retries and queue items use fresh children by default; non-review reuse requires named costly live state.

Retain task IDs. A new review round always creates a fresh task with consolidated context and a new request ID; retries of that dispatch retain the same request ID. Use child status and automatic completion delivery to distinguish active work, nested children and a finished result. A completed turn with live child work is not completion of the whole task. Cancellation includes outstanding child work and any resources the run owns.

## Workspaces and concurrent writes

As of 2026-10-14, T3 Code's callable `delegate_task` provides `isolation: "worktree"`. Use it for a child needing a separate checkout, across providers/models. It starts at the parent's local commit and runs project setup; uncommitted edits are not copied. Required inputs must be committed within task authority or supplied as explicit read-only artifacts. Prompting a child to change directories or create a worktree does not bind its app workspace.

Inspect actual assigned checkout, branch, base revision, edits and proof before accepting results. Keep shared plan state parent-owned and mutable runtime resources separate. Shared checkouts are valid for bounded reads or serial writes; concurrent writes still require disjoint ownership and tested tools. This current contract supersedes the earlier no-workspace-option observation, while its historical evaluation remains unchanged. The new app-bound path still needs runtime verification across intended providers and editors. `t3_thread_launch` remains reserved for user-requested separate top-level conversations.

Autopilot and Orchestrate require tested write isolation or a disclosed serial execution path that preserves their ownership and verification rules. Cloud VMs, simultaneous lane counts and provider-specific process controls are not implicit capabilities of a portable skill.

## Shared dependencies and intentional changes

The following dispositions cover the common entrypoint dependencies as well as the detailed inventory. Record each adaptation's source pin in research and the manifest, and retain its required license in the distributed package. A helper being mentioned here does not mean it is implemented.

| Dependency, using jstack names when shipped | Current implementation direction |
| --- | --- |
| `jstack-how`, `jstack-why` | Separate skills for direct invocation and catalog-discovered playbook use, with configured role resolution and explicit child prompts. |
| `jstack-arena` | Standalone candidate comparison and synthesis, discovered through the catalog. Preserve configured panels and one selected cross-judge; support design-only callers. |
| `jstack-architect` | Standalone grounded design through how, conditional why and Arena with the architect runner panel. Return at the caller's design boundary, pause at an explicit checkpoint or continue with authorized implementation. |
| `jstack-interrogate` | Standalone report-only code or design review with the configured reviewer panel, checked findings and lead judgment. |
| `jstack-swarm` | Standalone partitioned coverage and races with task-derived count, configured workers, pinned evidence and checked aggregation. |
| `jstack-reflect` | Standalone bounded session review with three lenses, existing-guidance checks and separate synthesis. Proposals and application remain distinct. |
| `jstack-figure-it-out`, `jstack-show-me-your-work` | Standalone custom-workflow and decision-trail skills, with planning-only return and checked execution. Use bounded T3 Code evidence and configured judgment review with same-model disclosure. |
| `jstack-benchmark-checklist` | Standalone helper with all seven checks, production tuning, separate profiling and the source ballpark exception. [Bounded evaluation](evaluations/benchmark-checklist/README.md) covers a synthetic export and misleading evidence; installed-provider discovery remains unverified. |
| `jstack-tdd` | Standalone port preserves the six-step failing-first procedure and impractical-test alternative. The installed unprefixed skill has a different workflow. [Bounded evaluation](evaluations/tdd/README.md) covers a cheap CLI regression and an unavailable native integration; Bug fix now consumes the helper; its [evaluation](evaluations/bug-fix/README.md) records the supported path. |
| `jstack-technical-writing` | Standalone writing standard preserving four layers, document modes and the worked example. Uses the separately assessed external Unslop dependency; missing or blocked invocation remains incomplete. |
| `unslop`, `deslop` | Preserve independently discoverable skill boundaries. Unslop remains external with its version-specific assessment. Standalone `jstack-deslop` now preserves the pinned cleanup procedure and supplies the pre-commit dependency, with [bounded cleanup evidence](evaluations/deslop/README.md). |
| `jstack-typescript-best-practices` | Standalone TypeScript syntax and patterns helper called by Type System Discipline; numeric constraints still require boundary validation. See [evaluation](evaluations/typescript-best-practices/README.md). |
| `jstack-no-comments` and bundled Comment Sicko | Standalone parent procedure and complete reviewer prompt, preserving exceptions, rejection/rerun limit, investigation and fix order. Uses configured judgment dispatch and private snapshots; findings-only requests do not edit the project, and encodings require their own approval. See [evaluation](evaluations/no-comments/README.md). |
| All 24 `jstack-principle-*` leaves | Implemented as 24 independently discoverable skills, each with research-owned attribution and a package license; jstack-juan-mode retains the upstream-organized inline Principles section. Scope adaptations preserve compatibility, authority and evidence limits; mapping alone is not runtime verification. |
| `typescript-best-practices` | Pending standalone conditional TypeScript helper, including `references/patterns.md`. Preserve its source structure and record the known negative-duration example correction. |
| Cursor `create-skill` and control skills | Use the advertised host authoring skill for the unavailable Cursor built-in. Standalone `jstack-control-cli` preserves the terminal workflow with [bounded PTY evidence](evaluations/control-cli/README.md). Standalone `jstack-control-ui` preserves browser control with [bounded native-preview evidence](evaluations/control-ui/README.md). T3 preview covers only demonstrated browser behavior; rich TUI, profiling, Electron and simulator execution need their own evidence. |
| Verification generation and maintenance | Reuse the shipped jstack skills when separately requested or accepted; existing verifier execution belongs to the active task. |
| `/loop`, Cursor agent wrappers and cloud task options | Use the supported child lifecycle and bounded task continuation. Do not add a hidden scheduler, launch provider CLIs as substitute agents or claim cloud isolation. |
| `watch-pr` and bootstrap | [Babysit](../../skills/jstack/jstack-juan-mode/playbooks/babysit.md) now consumes the preserved watcher with a single-pass adapter and manual dependency check. T3 owns waiting. See [evaluation and remaining limits](evaluations/babysit/README.md). |
| `check-plan.mjs`, `orch` and worktree audit | [Multi-phase plan](../../skills/jstack/jstack-juan-mode/playbooks/multi-phase-plan.md) now consumes the structural checker with the native hourly-schedule marker. Its [evaluation](evaluations/multi-phase-plan/README.md) records preserved validation and remaining semantic limits. Port the other tools with their first consuming procedure, preserving evidence and state algorithms. Assess all ten live-lane proof obligations instead of deleting them for portability. Resolve the source Graphite/frontier contradiction before choosing a substitute. Replace automatic installation with a manual prerequisite and unsafe cleanup classifications with actual ownership/merge evidence. |

Sources include the [mode's dependency rules](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [principle source directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills), [comment reviewer](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/agents/comment-sicko.md), [deslop](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/cursor-team-kit/skills/deslop/SKILL.md), and the detailed inventory's linked helper and script sources. The 24 principle leaves were read for this assessment; this count is separate from the 23 playbooks.

## PRs, autonomous work and handoff

PR publication follows the user's requested delivery and the repository's workflow. Creating a PR does not authorize merging, and keeping jstack-juan-mode active does not expand task permissions. Explicit merge or full-autopilot instructions can authorize their concrete scope without repeated confirmation. Installation remains manual under the project's established preference.

Register every PR with T3 Code, including each layer of a stack. The parent owns PR watching because T3 Code prohibits child-owned watches. Children can implement and review, then return their artifacts; the parent handles wakeups and dispatches fresh scoped work. Read current comments before watching because an existing comment does not trigger a new wake. Recheck readiness after events and stop watching when handing responsibility back to the user.

Shipping verifies each exact candidate head before advancing through a stack. Branch changes invalidate evidence for the old head. Check current forge merge state, required checks, unresolved review findings and the authorized merge scope. GitHub is the first supported forge; other forge support is an explicit capability rather than assumed parity. Test continuation after a merge because watches end and linked PRs can cause thread settlement.

Use a small task-scoped run record only where work must survive a handoff or coordinate several artifacts. Record the goal, authorization, activation state, phase, branch heads, child task IDs, PRs, evidence paths and next action. T3 Code owns task execution and notifications; the record does not create another task scheduler. The parent owns shared plan state while workers publish separate results. Periodic scheduling requires a user request; an autonomous task by itself does not authorize recurring work.

Worktree cleanup requires independent evidence that a checkout is inactive and its work is disposable. Untracked files are work, not proof of scratch status. A closed PR is not proof of merge. Protect current thread bindings, active children, unsaved files and unique commits. Retain uncertain candidates and explain the missing evidence. Pause and pickup preserve both the local artifacts and the information needed to reconcile their current state.

## Verification contract

Each task reports its actual outcome and evidence. Completion requires the requested deliverable and its observable checks. Incomplete, blocked, paused and cancelled are distinct outcomes. A tool's accepted dispatch, a child summary or passing static checks alone does not prove user-visible behavior.

Investigation and forensic cases must preserve their source-write boundary. Temporary runtime instrumentation, process restarts or controlled fault injection need a scope that permits those actions and cleanup of owned state. Runtime and trace diagnosis must not silently become a production fix. Visual parity and browser tasks must use the real target interface; a CLI check does not establish UI behavior.

Eval isolates candidate context from judge rubrics and model identities. Verify actual candidate actions through available evidence. T3 Code's summarized activity is not automatically equivalent to raw provider transcripts; mark unobservable criteria inconclusive or provide an authorized instrumented fixture. Keep performance measurements tied to their workload, run count, variability and limiting resource.

All-playbook release evidence includes at least one representative executed case per route, cross-route tests of the common contracts, and failure cases for unavailable capabilities. These checks demonstrate bounded support rather than every possible platform or task. Record coordinating provider, child provider, effective model options, source revision and evidence paths. Do not derive a support claim from installation or the catalog alone.

## Current playbook coverage

[Investigation](../../skills/jstack/jstack-juan-mode/playbooks/investigation.md) and [Prototype](../../skills/jstack/jstack-juan-mode/playbooks/prototype.md) are implemented, with bounded [Investigation](evaluations/investigation-playbook/README.md) and [Prototype](evaluations/prototype-playbook/README.md) evaluations. [Trace forensics](../../skills/jstack/jstack-juan-mode/playbooks/trace-forensics.md) adds [fixed-artifact analysis](evaluations/trace-forensics/README.md). [Authoring or modifying a skill](../../skills/jstack/jstack-juan-mode/playbooks/authoring-a-skill.md) adds [local skill-authoring validation](evaluations/authoring-a-skill/README.md). [Runtime forensics](../../skills/jstack/jstack-juan-mode/playbooks/runtime-forensics.md) adds [live-process diagnosis](evaluations/runtime-forensics/README.md). [Bug fix](../../skills/jstack/jstack-juan-mode/playbooks/bug-fix.md) adds [delegated repair and verification](evaluations/bug-fix/README.md). [Feature](../../skills/jstack/jstack-juan-mode/playbooks/feature.md) adds [design exploration, the shared throughput checkpoint and delegated implementation](evaluations/feature/README.md). [Refactoring](../../skills/jstack/jstack-juan-mode/playbooks/refactoring.md) adds [pre-change characterization and delegated behavior-preserving cleanup](evaluations/refactoring/README.md). [Perf issue](../../skills/jstack/jstack-juan-mode/playbooks/perf-issue.md) adds [baseline-first profiling and measured improvement](evaluations/perf-issue/README.md). [Hillclimb](../../skills/jstack/jstack-juan-mode/playbooks/hillclimb.md) adds [frozen measurement, per-attempt decisions and bounded stop evaluation](evaluations/hillclimb/README.md). [Eval](../../skills/jstack/jstack-juan-mode/playbooks/eval.md) adds [blinded comparison and explicit evidence limits](evaluations/eval/README.md). [Visual parity](../../skills/jstack/jstack-juan-mode/playbooks/visual-parity.md) adds [frozen-baseline migration and exact pixel comparisons](evaluations/visual-parity/README.md). [Opening a PR](../../skills/jstack/jstack-juan-mode/playbooks/opening-a-pr.md) adds [scoped local preparation and publication checks](evaluations/opening-a-pr/README.md). [Babysit](../../skills/jstack/jstack-juan-mode/playbooks/babysit.md) adds [single-pass watcher checks](evaluations/babysit/README.md). [Shipping](../../skills/jstack/jstack-juan-mode/playbooks/shipping.md) adds [independent CLI verification and local landing checks](evaluations/shipping/README.md). [Multi-phase plan](../../skills/jstack/jstack-juan-mode/playbooks/multi-phase-plan.md) adds [structural validation and bounded plan drafting](evaluations/multi-phase-plan/README.md). [Session pickup](../../skills/jstack/jstack-juan-mode/playbooks/session-pickup.md) adds [scoped history recovery and artifact reconciliation](evaluations/session-pickup/README.md). The other 4 routes remain pending. This does not close the provider/persistence release gates below or change the accepted all-23 target.

## Implementation groups

These groups organize work into focused PRs. They are not reduced releases. A group may need several PRs; each must have an independently inspectable result and acceptance evidence.

1. **Execution foundation.** Implement the entrypoint, full route registry, installed-dependency discovery, configuration resolution and explicit delegation contract. Prove activation/opt-out and resume behavior, model selection and the workspace execution model. These results determine which providers can support the full release.
2. **Shared procedures.** Complete the standalone helper dependencies, principle mapping, review contracts, evidence rules and required validators, following the [current fidelity status](fidelity-status.md). Prove design-only helper return, configured fan-out, distinct candidate/judge handling and clear unavailable-capability results.
3. **Engineering and experiments.** Implement the 9 engineering routes plus Prototype, Eval and Authoring a skill. Exercise diagnosis versus implementation, behavior-preserving refactoring, performance evidence, visual proof and blinded candidate evaluation.
4. **Delivery and recovery.** Implement the 7 delivery routes with parent-owned monitoring, conservative cleanup, exact-head shipping checks, pause/pickup and a plan validator matched to the actual T3 Code execution model.
5. **Autonomous coordination.** Implement Autonomous run, Orchestrate, Autopilot-full and Autopilot-stack against the already-tested task, workspace and PR contracts. Exercise restart reconciliation, held merge authority, child failure and user stop.
6. **Full release verification.** Audit all 23 route implementations and their dependency closure, run the cross-provider and persistence cases, update attribution and upstream mappings, and publish the tested support matrix. No route may appear supported solely because its Markdown file exists.

## Engineering questions that require execution evidence

The accepted activation preference and all-playbook target are settled. The following are implementation investigations, not questions to return to the user in place of testing:

- Which coordinating providers preserve or reload thread-scoped activation after compaction and restart without changing global instructions?
- Can delegated writers reliably operate in explicitly assigned worktrees with the current tool set, and which operations remain bound to the original checkout?
- Does a multi-PR program resume correctly after merge-triggered watch completion or thread settlement?
- Which activity records support Eval and decision-trail assertions, and which need fixture instrumentation?

The proposed release verification covers the project's four installation providers as coordinators, Codex, Claude Code, Cursor and OpenCode, plus live cross-provider child dispatch. A provider that fails these checks remains unverified; report the precise gap before changing the promised support. Model choices continue to come from the user's configuration.

## Runtime evidence used for this design

On 2026-10-11, the live T3 Code catalog reported app-owned children, cancellation, thread reads and scheduling. The callable schemas for `delegate_task`, `task_status`, `task_cancel`, `t3_thread_launch`, `t3_thread_read`, `watch_pull_request`, `link_pull_request`, `t3_thread_configuration`, `t3_thread_update` and project/environment settings were inspected. They establish exposed interfaces, not successful execution of this proposed workflow. Re-read their live schemas during implementation. The [existing integration contract](../../skills/jstack/jstack-setup/references/t3-code.md) remains the local starting point.
