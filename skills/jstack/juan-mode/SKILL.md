---
name: juan-mode
description: Apply jstack's task routing and configured delegation when the user invokes juan-mode, or continue an already active juan-mode conversation. Activation lasts until explicit opt-out.
---

# Juan-mode

Use the user's requested outcome to select a playbook, resolve the current jstack model assignments and coordinate verified work in T3 Code. Explicit invocation activates the mode in this conversation until the user turns it off. Reading this file for authoring or review does not activate it.

This package currently implements the execution foundation. The separately installed how and why skills provide shared investigation procedures. All 23 playbooks are registered but awaiting implementation. Report a selected route as unavailable rather than improvising its missing procedure or claiming its workflow passed. Full release requires executed acceptance evidence for every route and the supported providers.

## Activation and task selection

On activation, opt-out, handoff or resume, follow [conversation state](references/activation.md). Apply the latest user instruction before loading models or dispatching work. An opt-out works even when configuration or T3 Code is unavailable. Mode activation does not expand the task's permissions.

For each new task while active, read the [route registry](references/routes.md), select by deliverable and report any unavailable procedure. Casual conversation does not start a playbook. Preserve ongoing work when a later message clarifies it; a new task needs a fresh route. Read an implemented playbook before using its steps. Use the user's existing authorization for concrete actions within its scope.

<!-- markdownlint-disable MD033 MD036 -->
## Principles

Read the leaf skill in full for any principle you apply. Each entry names when it applies. Each leaf is the **principle-<title>** skill, with the title in kebab case, hyphens kept and other punctuation dropped, unless the entry gives its name.

Discover each selected standalone jstack skill through the current catalog and read its advertised path; do not assume sibling installation. Verify jstack attribution. If missing, identify the dependency, provide `npx skills add juancamiloqhz/skills --skill principle-NAME` with its actual name for manual installation, and keep the affected guidance unavailable while continuing independent authorized work. Principle summaries below follow upstream; the scoped leaf instructions, task authority and repository constraints govern their application. A principle cannot make an unavailable playbook executable.

In your reply, name principles that shaped a consequential decision and the choice each changed. Cite only leaves read this session.

**Core**

- **Laziness Protocol.** Refactoring, sizing a diff, or tempted to add abstractions, layers, or signal threading. Bias to deletion and the smallest change that solves the problem.
- **Foundational Thinking.** Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.
- **Redesign from First Principles.** Integrating a new requirement into an existing design. Redesign as if it had been foundational from day one.
- **Attack the Premise.** Two or more fixes that share one premise have failed the same gate. Take a census of which actors hold the imbalance before the next fix, then question the premise instead of writing another fix that assumes it.
- **Subtract Before You Add.** Sequencing an addition, refactor, or rewrite. Remove dead weight first, then build on the simpler base.
- **Minimize Reader Load.** Reviewing or shaping code that's hard to trace. Count layers and hidden state, collapse one-caller wrappers, shrink mutable scope.
- **Outcome-Oriented Execution.** Planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture, don't preserve throwaway compatibility states.
- **Experience First.** Product, UX, or feature-scope tradeoffs. Choose user delight over implementation convenience.
- **Exhaust the Design Space.** A novel interaction or architectural decision with no precedent. Build 2-3 competing prototypes and compare before committing.
- **Build the Lever.** Any non-trivial work. Build the tool that does or proves it (codemod, script, generator), not by hand. The tool is the artifact a reviewer reruns.

**Architecture**

- **Model the Domain.** Writing stateful logic, or code that branches a lot or repeats a shape assumption across files. Encode the domain in a structure (state machine, typed model, table or registry, reducer, boundary, the right collection) instead of scattered conditionals.
- **Boundary Discipline.** Wiring validation, error handling, or framework adapters. Guards at system boundaries, trust internal types, keep business logic pure.
- **Type System Discipline.** Designing types or a signature in any typed language. Make illegal states unrepresentable, brand primitives, parse external data at boundaries.
- **Make Operations Idempotent.** Designing commands, lifecycle steps, or loops that run amid crashes and retries. Converge to the same end state.
- **Migrate Callers Then Delete Legacy APIs.** Introducing a new internal API while old callers exist. Migrate and delete in one wave.
- **Separate Before Serializing Shared State.** Concurrent actors might write the same file, branch, key, or object. Eliminate the sharing first.

**Verification**

- **Prove It Works.** After a task, before declaring done. Verify against the real artifact, not a proxy or "it compiles".
- **Fix Root Causes.** Debugging. Trace each symptom to its root cause, reproduce first, ask why until you reach it.
- **Sequence Work into Verifiable Units** (**principle-sequence-verifiable-units**). Multi-step work (sweeps, migrations, runs of similar edits) and how you stack commits and PRs. Break work into small units that each end in a check, verify each before the next, and order delivery so the sequence proves itself.
- **Test Behavior, Not Implementation.** Writing, changing, or keeping a test. Call the code the way its users do and assert the result against a literal expected value. If the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test.
- **Explain the Number.** Before you trust, report, or act on a number you measured (a speedup, a regression, a throughput, a latency, or an eval result). Find what limits it, and rule out that it measured something other than the work you think.

**Delegation**

- **Guard the Context Window.** Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.
- **Never Block on the Human.** Tempted to ask "should I do X?" on reversible work. Proceed, present the result, let the human course-correct.

**Meta**

- **Encode Lessons in Structure.** You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.

<!-- markdownlint-enable MD033 MD036 -->

## Prepare execution

Before a routed task dispatches any child, read [configuration discovery](references/configuration.md). Discover the installed `setup-jstack` entrypoint from the current skill catalog, then use this package's [preflight helper](scripts/preflight.py) with a fresh T3 Code catalog. It calls the canonical resolver, validates the entire saved map, preserves ordered seats and options, and checks effective child capability. It reads configuration without changing it or launching agents.

Retain the selected absolute configuration path for the task and pass it explicitly to children, including writers in other worktrees. Resolve each needed role from that file. Configuration validity does not satisfy a workflow's required panel size or judge diversity. Read the role semantics in the configuration reference before fan-out. A missing dependency, stale selection or unavailable provider produces a precise limitation; preserve the user's saved settings.

Before delegation, read the [execution contract](references/execution.md). Give each child an explicit brief and bounded ownership, retain its task ID, and verify its artifacts. The parent owns shared plan state, PR watches and final synthesis. Use serial writes until the selected provider and tools have demonstrated assigned-checkout behavior.

## Shared investigation procedures

When a caller or implemented playbook selects investigation, discover `how` for runtime flow and ownership or `why` for historical rationale in the current skill catalog. Read that skill's advertised `SKILL.md`, pass the original question, source scope and selected absolute configuration path, and follow its procedure. Do not assume a sibling installation or substitute an unrelated skill with the same name; verify that it uses the jstack setup contract. If missing, report the dependency and provide `npx skills add juancamiloqhz/skills --skill how` or `--skill why` for manual installation. These standalone skills return checked findings without activating juan-mode themselves. Their availability does not make the planned Investigation playbook executable. For candidate comparison, discover the standalone `arena` skill through the current catalog and pass the artifact requirements, source scope, selected configuration and return boundary. Verify its jstack setup contract. If missing, provide `npx skills add juancamiloqhz/skills --skill arena` for manual installation. A design-only caller must receive a design artifact without implementation. For grounded architecture design, discover the standalone `architect` skill with the same catalog and jstack-contract checks. Pass the source scope, selected configuration and whether the caller requests design only, an explicit checkpoint or already authorized implementation. If missing, provide `npx skills add juancamiloqhz/skills --skill architect` for manual installation. For adversarial code or design review, discover standalone `interrogate` with the same jstack-contract checks, pass pinned review scope and selected config, and return its report without applying fixes. If missing, provide `npx skills add juancamiloqhz/skills --skill interrogate` for manual installation. For partitioned coverage or a declared race, discover standalone `swarm` with the same jstack-contract checks and pass the task, selected config, worker count or decomposition scope and return boundary. If missing, provide `npx skills add juancamiloqhz/skills --skill swarm` for manual installation. For a requested retrospective or explicit playbook reflection, discover standalone `reflect` with the same jstack-contract checks and pass bounded current-conversation evidence or a labeled digest, selected config and the authorized return boundary. If missing, provide `npx skills add juancamiloqhz/skills --skill reflect` for manual installation. Its assessment returns proposals; it applies edits or files external items only within actual user authorization. For a custom workflow when no narrower available procedure fits, discover standalone `figure-it-out` with the same jstack-contract checks. Pass the task, selected config if already resolved, source scope and planning-only or execution boundary. If missing, provide `npx skills add juancamiloqhz/skills --skill figure-it-out` for manual installation. It does not substitute for an unavailable named playbook. Other shared helpers remain planned.

## Completion

Report the requested outcome, actual verification and any remaining limitation. Distinguish completed, incomplete, blocked, paused and cancelled work. Task completion leaves mode activation intact. PR publication follows the requested delivery; merging, recurring scheduling and installation require their own applicable authorization. Skill installation remains manual.

The [upstream record](references/upstream.md) identifies the source revision and intentional differences. Remaining helper workflows and playbooks arrive in later implementation groups; their upstream names are not dependencies on unrelated global skills.
