# Juan-mode adaptation specification

Drafted on 2026-10-11 against `cursor/plugins` revision `11713c683fe4add4fd403ea880580abbc9e0875f`, fetched again for this assessment. This is an implementation specification, not a shipped skill or a report of successful workflow execution. The [initial assessment](juan-mode-adaptation.md) supplies context; the inventories below record the complete playbook review.

## Scope and accepted behavior

The user approved assessing and designing for all 23 poteto-mode playbooks, then implementing and verifying them in manageable groups. This supersedes the earlier three-playbook first-release plan. Implementation order does not reduce the release target. A reduced release or an omitted playbook requires an explicit scope decision.

The user also selected conversation activation. An explicit invocation activates juan-mode for subsequent tasks in that conversation until the user turns it off. Finishing a task does not deactivate the mode. Turning the mode off removes its routing and working-style instructions; stopping ongoing work is a separate request. New conversations do not inherit activation automatically. A delegated child receives the instructions needed for its assigned work, not permission to start an independent program.

The scope is adapting the complete working approach and playbook set to T3 Code. It does not require reproducing Cursor's UI, copying its tool infrastructure, or making every pstack skill independently installable. Platform-specific capabilities remain explicit prerequisites. A blocked browser, profiler, simulator or review configuration must produce a precise limitation rather than a fabricated completion.

## Complete playbook inventory

Each inventory entry records its trigger, deliverable, dependencies, T3 Code changes and an acceptance scenario. These are source assessments and proposed checks, not test results.

- [Engineering inventory](juan-mode/engineering-inventory.md) covers 9 playbooks: Investigation, Feature, Bug fix, Refactoring, Perf issue, Hillclimb, Runtime forensics, Trace forensics and Visual parity.
- [Delivery inventory](juan-mode/delivery-inventory.md) covers 7 playbooks: Opening a PR, Babysit, Shipping, Multi-phase plan, Session pickup, Pause safely and Worktree cleanup.
- [Autonomy and tooling inventory](juan-mode/autonomy-inventory.md) covers 7 playbooks: Autonomous run, Orchestrate, Autopilot-full, Autopilot-stack, Prototype, Eval and Authoring a skill.

The authoritative upstream set is the [pinned playbook directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks). Before implementation and release, compare its filenames with the supported-route registry. Every source playbook needs an implementation, an acceptance result and documented differences. Extra routes must have their own justification.

## Packaging

Use one installable `juan-mode` skill containing the entrypoint, all 23 playbook files, shared workflow references, principle references, prompt templates and the small scripts that its behavior requires. Playbooks remain internal procedures, not separately installed skills. Keep the entrypoint focused on activation, routing, shared rules and completion requirements; read detailed material only when its route needs it.

Initially bundle the reusable procedures behind `how`, `why`, `architect`, `arena`, `swarm`, `interrogate`, `reflect` and `figure-it-out` as reference files. Preserve their roles and algorithms without depending on global skills with matching names. They can serve several playbooks inside the package. Standalone wrappers can be considered later when independent invocation earns the additional installation and discovery contract.

Keep `setup-jstack` as an explicit runtime dependency for its canonical configuration validator and resolver. Resolve its actual installation directory through the provider's skill catalog. Do not assume it is a filesystem sibling of `juan-mode` or copy `models.py` into another independent implementation. If the dependency cannot be found, explain the missing installation and retain the existing model configuration. Installations remain manual. The first implementation group must prove discovery with separately installed skill directories.

Existing project verification is an input to the playbooks. `create-verification-skill` and `maintain-verification-skill` stay separate skills, reached only for an appropriate generation or maintenance task. Running an existing verifier does not require generating another one.

Suggested internal layout, to be populated as implementation groups land:

```text
skills/jstack/juan-mode/
  SKILL.md
  playbooks/                 # the 23 supported task procedures
  references/workflows/      # shared investigation, design and review procedures
  references/principles/     # scoped engineering guidance
  references/t3-code.md      # execution and lifecycle requirements
  references/upstream.md     # source pin and intentional differences
  scripts/                   # demonstrated validation or state-management needs
  LICENSE
```

## Activation and routing

At explicit activation, read the entrypoint and identify the current thread. Record that juan-mode is active in the conversation's working state and preserve that fact in handoff and compaction summaries. On a new task, select a fresh playbook rather than treating the request as another step of the previous one. Casual conversation need not start a playbook. User opt-out takes effect immediately and must survive the same resume paths as activation.

The [upstream guide](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/docs/guide/02-poteto-mode.md) attributes persistence to Cursor Custom Mode. The inspected T3 Code thread configuration and metadata tools do not expose an equivalent per-thread skill-injection setting. A local state file or `mode: true` frontmatter alone cannot make the host load a skill. The implementation must verify how each supported provider retains or reloads the activation instruction across later turns, compaction and session resume. If that cannot be demonstrated, persistent activation remains an unresolved release requirement for that provider. Do not replace the requested behavior with task-only activation without agreement.

Routing respects the requested outcome. Diagnosis-only Runtime and Trace forensics return findings; a fix request adds a separate implementation route. Investigation remains read-only. A routine implementation does not automatically start PR monitoring or authorize merging. Explicit shipping and autopilot requests carry their stated delivery authority. Large tasks can use the adapted `figure-it-out` procedure to compose a bounded plan; standing programs use Orchestrate. Unsupported prerequisites stop the affected operation with completed evidence and the missing capability identified.

A shared helper needs a clear return boundary. In particular, the upstream `architect` skill includes implementation stages, but Feature calls it for design before delegating implementation. The adapted helper must support a design-only result so implementation occurs once. A coordinator owns final synthesis and checks each child result against source or artifacts.

## Configuration and delegation

Every new routed task loads the current jstack model configuration and validates the whole map against live `orchestrator_capabilities` before dispatch. Follow the [existing contract](../../skills/jstack/setup-jstack/references/configuration.md): preserve the 17 roles, list order, concrete options and inherited selections. Never silently substitute upstream model defaults, rewrite routing preferences or switch the current conversation's model.

The accepted project-configuration extension selects one complete file with precedence explicit path, `JSTACK_CONFIG`, `<project_root>/.jstack/models.json`, then XDG global defaults. Setup owns this lookup. Retain the selected absolute path for children and task phases in other worktrees, while new tasks repeat lookup in their project context. Partial or invalid project files are errors, not requests to merge or fall back to the global role map.

Implementation playbooks use their configured roles: `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` and `hardest tasks`. Shared helper procedures use their existing explorer, synthesizer, runner and reviewer roles. Roles for procedures without dedicated assignments must be specified using the existing relevant role or explicit parent inheritance; avoid inventing hidden model defaults. The inventory records route-specific mappings.

Check execution capability separately from configuration validity. A model may be listed while its provider cannot run a child. Likewise, a valid one-seat panel does not satisfy a procedure requiring two independent designs, or a cross-family judge. Resolve effective inherited selections before claiming diversity. Preserve configured fan-out. When a required count or diversity is missing, report the precise role and requirement and request a routing adjustment instead of adding paid runs or models silently.

Use native same-provider children when they support the selected model and required lifecycle. Otherwise use T3 Code `delegate_task`, including for cross-provider work. Each brief includes the original goal, later constraints, selected workflow, owned paths, permitted actions, required evidence, relevant prior findings and exact completion criteria. The tool does not copy the parent conversation. Pass source pointers with enough explicit context to make them useful.

Retain task IDs. A new review round creates a fresh task with consolidated context and a new request ID; retries of that dispatch retain the same request ID. Use child status and automatic completion delivery to distinguish active work, nested children and a finished result. A completed turn with live child work is not completion of the whole task. Cancellation includes outstanding child work and any resources the run owns.

## Workspaces and concurrent writes

The inspected `delegate_task` schema has no workspace, cloud-machine or per-child environment field. Prompting a child to use a path does not establish app-level workspace isolation. The implementation must first prove the child tools and Git commands operate on the assigned checkout. Until then, serialize writes in the bound checkout; parallel read-only work is still useful.

Where explicit-path execution is verified, the parent can prepare owned worktrees, assign disjoint paths and validate each child result against its assigned branch. Keep ports, logs and mutable build outputs separate as needed. Never infer isolation from a child's summary. T3 Code's `t3_thread_launch` provides explicit workspace binding for ordinary top-level threads, which remain reserved for user-requested separate conversations. Do not create them just to bypass a child limitation.

Autopilot and Orchestrate require tested write isolation or a disclosed serial execution path that preserves their ownership and verification rules. Cloud VMs, simultaneous lane counts and provider-specific process controls are not implicit capabilities of a portable skill.

## Shared dependencies and intentional changes

The following dispositions cover the common entrypoint dependencies as well as the detailed inventory. Every retained source adaptation must carry its source pin and MIT attribution. A helper being mentioned here does not mean it is implemented.

| Upstream dependency | Proposed juan-mode disposition |
| --- | --- |
| `how`, `why` | Bundle exploration and evidence-based explanation procedures with configured role resolution and explicit child prompts. |
| `architect`, `arena`, `swarm`, `interrogate` | Bundle distinct design, candidate comparison, work partitioning and adversarial review procedures. Preserve their differences, judge independence and configuration prerequisites. |
| `reflect`, `figure-it-out`, `show-me-your-work` | Bundle bounded improvement, custom-plan and decision-record procedures. Use task-scoped T3 Code evidence instead of Cursor transcript paths or a global personal-memory store. |
| `benchmark-checklist`, `tdd` | Bundle the relevant measurement and failing-then-passing proof procedures; preserve real workloads, repeatability and measurement limits. |
| `unslop`, `technical-writing`, `deslop` | Bundle concise writing and code-review references, with repository conventions taking precedence. Do not depend on a user's unrelated global skill installation. |
| `no-comments` and `comment-sicko` | Replace the deletion-first persona with an evidence-based review of the scoped diff. Preserve useful explanations, license text and justified suppressions until a verified replacement exists. |
| All 24 `principle-*` leaves | Map into attributed principle references, loaded by condition. Preserve substantive guidance while adapting absolute upstream rules to the task's scope and repository constraints. |
| `typescript-best-practices` | Carry relevant language-specific guidance as an optional reference reached for TypeScript work; follow the target repository's conventions. |
| Cursor `create-skill` and control skills | Replace with portable skill-authoring requirements and an explicit control-capability contract. T3 Code preview is the preferred browser path; CLI, profiler and simulator access remain separate capabilities. |
| Verification generation and maintenance | Reuse the shipped jstack skills when separately requested or accepted; existing verifier execution belongs to the active task. |
| `/loop`, Cursor agent wrappers and cloud task options | Use the supported child lifecycle and bounded task continuation. Do not add a hidden scheduler, launch provider CLIs as substitute agents or claim cloud isolation. |
| `watch-pr` | Use T3 Code parent-owned PR watches for waiting; retain independent readiness checks against the forge. |
| `check-plan.mjs`, `orch`, bootstrap and worktree audit | Adapt only needed validators and owned run records. Remove hardcoded Graphite, ten-lane/cloud assumptions and automatic dependency installation. Rewrite unsafe cleanup classifications. |

Sources include the [mode's dependency rules](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [principle source directory](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills), [comment reviewer](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/agents/comment-sicko.md), [deslop](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/cursor-team-kit/skills/deslop/SKILL.md), and the detailed inventory's linked helper and script sources. The 24 principle leaves were read for this assessment; this count is separate from the 23 playbooks.

## PRs, autonomous work and handoff

PR publication follows the user's requested delivery and the repository's workflow. Creating a PR does not authorize merging, and keeping juan-mode active does not expand task permissions. Explicit merge or full-autopilot instructions can authorize their concrete scope without repeated confirmation. Installation remains manual under the project's established preference.

Register every PR with T3 Code, including each layer of a stack. The parent owns PR watching because T3 Code prohibits child-owned watches. Children can implement and review, then return their artifacts; the parent handles wakeups and dispatches fresh scoped work. Read current comments before watching because an existing comment does not trigger a new wake. Recheck readiness after events and stop watching when handing responsibility back to the user.

Shipping verifies each exact candidate head before advancing through a stack. Branch changes invalidate evidence for the old head. Check current forge merge state, required checks, unresolved review findings and the authorized merge scope. GitHub is the first supported forge; other forge support is an explicit capability rather than assumed parity. Test continuation after a merge because watches end and linked PRs can cause thread settlement.

Use a small task-scoped run record only where work must survive a handoff or coordinate several artifacts. Record the goal, authorization, activation state, phase, branch heads, child task IDs, PRs, evidence paths and next action. T3 Code owns task execution and notifications; the record does not create another task scheduler. The parent owns shared plan state while workers publish separate results. Periodic scheduling requires a user request; an autonomous task by itself does not authorize recurring work.

Worktree cleanup requires independent evidence that a checkout is inactive and its work is disposable. Untracked files are work, not proof of scratch status. A closed PR is not proof of merge. Protect current thread bindings, active children, unsaved files and unique commits. Retain uncertain candidates and explain the missing evidence. Pause and pickup preserve both the local artifacts and the information needed to reconcile their current state.

## Verification contract

Each task reports its actual outcome and evidence. Completion requires the requested deliverable and its observable checks. Incomplete, blocked, paused and cancelled are distinct outcomes. A tool's accepted dispatch, a child summary or passing static checks alone does not prove user-visible behavior.

Investigation and forensic cases must preserve their source-write boundary. Temporary runtime instrumentation, process restarts or controlled fault injection need a scope that permits those actions and cleanup of owned state. Runtime and trace diagnosis must not silently become a production fix. Visual parity and browser tasks must use the real target interface; a CLI check does not establish UI behavior.

Eval isolates candidate context from judge rubrics and model identities. Verify actual candidate actions through available evidence. T3 Code's summarized activity is not automatically equivalent to raw provider transcripts; mark unobservable criteria inconclusive or provide an authorized instrumented fixture. Keep performance measurements tied to their workload, run count, variability and limiting resource.

All-playbook release evidence includes at least one representative executed case per route, cross-route tests of the common contracts, and failure cases for unavailable capabilities. These checks demonstrate bounded support rather than every possible platform or task. Record coordinating provider, child provider, effective model options, source revision and evidence paths. Do not derive a support claim from installation or the catalog alone.

## Implementation groups

These groups organize work into focused PRs. They are not reduced releases. A group may need several PRs; each must have an independently inspectable result and acceptance evidence.

1. **Execution foundation.** Implement the entrypoint, full route registry, installed-dependency discovery, configuration resolution and explicit delegation contract. Prove activation/opt-out and resume behavior, model selection and the workspace execution model. These results determine which providers can support the full release.
2. **Shared procedures.** Implement the helper references, principle mapping, review contracts, evidence rules and required small validators. Prove design-only helper return, configured fan-out, distinct candidate/judge handling and clear unavailable-capability results.
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

On 2026-10-11, the live T3 Code catalog reported app-owned children, cancellation, thread reads and scheduling. The callable schemas for `delegate_task`, `task_status`, `task_cancel`, `t3_thread_launch`, `t3_thread_read`, `watch_pull_request`, `link_pull_request`, `t3_thread_configuration`, `t3_thread_update` and project/environment settings were inspected. They establish exposed interfaces, not successful execution of this proposed workflow. Re-read their live schemas during implementation. The [existing integration contract](../../skills/jstack/setup-jstack/references/t3-code.md) remains the local starting point.
