---
name: jstack-juan-mode
description: Apply jstack's task routing and configured delegation when the user invokes jstack-juan-mode, or continue an already active jstack-juan-mode conversation. Activation lasts until explicit opt-out.
---

# Juan-mode

Explicit invocation activates jstack-juan-mode in this conversation until the user turns it off. Reading it for authoring, review or a bounded child-style brief does not activate persistent mode. On activation, opt-out, handoff or resume, follow [conversation state](references/activation.md). Apply the latest user instruction first; opt-out works without configuration or tools. Casual conversation does not start a playbook, and a clarification preserves the ongoing task.

This package implements the execution foundation, discovers standalone helpers and supplies [Investigation](playbooks/investigation.md), [Prototype](playbooks/prototype.md), [Trace forensics](playbooks/trace-forensics.md), [Authoring or modifying a skill](playbooks/authoring-a-skill.md) and [Runtime forensics](playbooks/runtime-forensics.md). The other 18 playbook procedures remain unavailable. The inline list below preserves all 23 routing triggers; only these five procedures are currently bundled. Their required dependencies and verification gates still apply. Select the route, disclose unavailable procedures or required dependencies, and continue only independent authorized work. Do not invent missing steps or claim an unavailable workflow passed.

## Non-negotiables

The Principles section below grounds every trigger. In your reply, name each principle that shaped a decision and the specific choice it changed. Cite only principles whose leaf SKILL.md you read this session.

Remaining triggers:

- Nontrivial change, architecture decision, or "are we sure?" → the **jstack-how** skill.
- About to ask the user a question on a "which approach", "how should I", or "what should this do" fork → classify it before you ask. If the answer is a fact you could observe by running something (behavior, timing, layout, output, perf, even whether an eval separates), it is not the human's to answer. Sketch it via the Prototype playbook (`playbooks/prototype.md`) and let the result decide. If the task is a read-only Investigation whose deliverable is a cited answer, stay in it and answer from the evidence rather than building a sketch. Reserve the question for a genuine product or preference call no experiment can settle. Under a full-autonomy grant, decide a call the grant covers, act on it, and report it, with no reply word and no offer. Under the grant, for a call only the operator can make, apply a default, report it with a full explanation, and say in plain words what the operator could tell you to do instead. The operator answers in their own words. Never give a shorthand token to type back. Gates the operator named and the Always-pause list in Autonomy still need the operator.
- Any code → name the data shape first, and choose its organizing structure per **jstack-principle-model-the-domain**.
- Code crossing a function boundary → the **jstack-architect** skill, parallel design exploration before implementing.
- Parallel fan-out → the **jstack-swarm** skill for coverage matrices, races, gauntlets, and exploration partitions. Use **jstack-arena** for design or code bakeoffs with base selection and grafting.
- Contested design → the **jstack-interrogate** skill (multi-model adversarial) before shipping.
- Nontrivial multi-step → write the throughput checkpoint (Feature step 3).
- Any prose surface, your reply to the user included → the **unslop** skill. Write the reply per **Writing the reply**. Agent-facing prose also follows the available **skill-creator** authoring skill; read its advertised entrypoint rather than assuming a Cursor built-in tool.
- Docs, RFCs, readmes, PR descriptions, or commit messages → the **jstack-technical-writing** skill (`/jstack-technical-writing`).
- Before commit → the `deslop` skill from the `cursor-team-kit` plugin (`/deslop`).
- Before review → the **jstack-no-comments** skill (`/jstack-no-comments`).
- Shipping UI / IDE / CLI → the matching control skill. Use **jstack-control-cli** for CLIs and TUIs; `cursor-team-kit` publishes the external `control-ui` for browser / Electron / web UIs. For bug fixes, reproduce first on the same surface yourself. Hand to the user only under the narrow Bug fix step 1 exception.
- Running a benchmark, measuring perf yourself, or reporting a speedup or regression you measured → the **jstack-benchmark-checklist** skill before you report or act on the number.
- Any PR-status request ("babysit this", "get it green", "address the bugbot comments", and most often "check on PR X" or "anything outstanding on X") → the **Babysit** playbook (`playbooks/babysit.md`), not an unrelated same-name host skill whose description matches the same words. Never triggered by merely opening a PR. Declare its mode before monitoring. In T3 Code, the parent uses the supported PR watch and completion wake mechanism rather than a polling loop. The playbook's step 1 owns the request-to-mode mapping. A phase child returns its result; the parent owns watches and wake handling.
- Asked to land or ship a green stack → the **Shipping** playbook (`playbooks/shipping.md`). Green is not safe. Nothing gets armed before an independent per-PR verdict, and only the contiguous verified run from the root lands.
- Bugbot or the agentic security review commented → skeptical posture. They catch real bugs and also file non-issues and nitpicks, so assess each on its merits and dismiss noise with a concrete reason instead of churning code. Triage fix / dismiss / ask per [Bugbot triage](references/bugbot-triage.md), within the requested review and communication authority.
- Broken skill mid-task → isolate its repair from the product change; fix it in its own PR when repair and publication are authorized. Continue independent work, report the affected step as incomplete, and do not silently work around it.
- Long, autonomous, or multi-phase work, or any task the user steps away from to review later ("going to bed", "trust it when i'm back", "/loop until X") → a decision trail via the **jstack-show-me-your-work** skill. Commit it when stakes need an auditable record. Keep it local otherwise.

Select the exact `jstack-` catalog name and record its resolved name and absolute SKILL.md path in the task evidence. If multiple entries share that name, use source metadata to identify `juancamiloqhz/skills`; unresolved ambiguity makes the dependency unavailable.

Discover selected helpers through the current catalog or an explicit authoring path, read the full advertised skill and required references, and pass the original task, source scope, selected absolute configuration if resolved, and planning/review/implementation boundary. Verify jstack package identity and its setup contract for configured helpers; do not assume sibling installation or replace them with unrelated same-name skills. Jstack currently ships jstack-how, jstack-why, jstack-arena, jstack-architect, jstack-interrogate, jstack-swarm, jstack-reflect, jstack-figure-it-out, jstack-show-me-your-work, jstack-benchmark-checklist, jstack-technical-writing and jstack-no-comments separately. If a selected package is missing, name it and provide `npx skills add juancamiloqhz/skills --skill NAME` with the actual package name for manual installation. Do not install it yourself.

Deslop and Control UI are external dependencies; jstack-control-cli is a separately discoverable jstack helper. Discover the intended package and verify it before use, or disclose the affected gate as incomplete. An available project verification skill may drive that project's real surface, but does not establish equivalence to an unavailable control skill. The Feature throughput checkpoint, Bug fix exceptions and other named playbook steps remain pending with their procedures. Their absence does not turn an empirical question into a user-preference question. Read-only questions use the Investigation playbook when its required helpers are available; missing dependencies remain explicit gaps.

<!-- markdownlint-disable MD033 MD036 -->
## Principles

Read the leaf skill in full for any principle you apply. Each entry names when it applies. Each leaf is the **jstack-principle-<title>** skill, with the title in kebab case, hyphens kept and other punctuation dropped, unless the entry gives its name.

Discover each selected standalone jstack skill through the current catalog and read its advertised path; do not assume sibling installation. Use package/source metadata exposed by the catalog to distinguish a same-name skill; if identity is ambiguous, report it rather than guessing. If missing, identify the dependency, provide `npx skills add juancamiloqhz/skills --skill jstack-principle-NAME` with its actual name for manual installation, and keep the affected guidance unavailable while continuing independent authorized work. Principle summaries below follow upstream; the scoped leaf instructions, task authority and repository constraints govern their application. A principle cannot make an unavailable playbook executable.

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
- **Sequence Work into Verifiable Units** (**jstack-principle-sequence-verifiable-units**). Multi-step work (sweeps, migrations, runs of similar edits) and how you stack commits and PRs. Break work into small units that each end in a check, verify each before the next, and order delivery so the sequence proves itself.
- **Test Behavior, Not Implementation.** Writing, changing, or keeping a test. Call the code the way its users do and assert the result against a literal expected value. If the test would still pass when every imported function returns `undefined`, rewrite the assertion or delete the test.
- **Explain the Number.** Before you trust, report, or act on a number you measured (a speedup, a regression, a throughput, a latency, or an eval result). Find what limits it, and rule out that it measured something other than the work you think.

**Delegation**

- **Guard the Context Window.** Context fills up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents, keep summaries in the main thread.
- **Never Block on the Human.** Tempted to ask "should I do X?" on reversible work. Proceed, present the result, let the human course-correct.

**Meta**

- **Encode Lessons in Structure.** You catch yourself writing the same instruction a second time. Encode it as a lint, metadata flag, runtime check, or script instead of more text.

<!-- markdownlint-enable MD033 MD036 -->

## Autonomy

**Just do it.** Proceed with reversible work within the requested scope and use existing authorization without asking again. Available tools and mode activation grant no extra authority. External messages, publication, merging, installation and recurring work require applicable user authorization; skill installation remains manual.

**Always pause** at an explicit user checkpoint, and before an irreversible action such as a shared-branch force-push, deployment, data deletion or customer message when the needed authorization is absent. Check existing authorization first; complete concrete reviewable preparation before asking.

**Session overrides:** "Don't stop" / "going to bed" / "run until done" / "be fully autonomous" → keep going.

**No is an acceptable answer.** Asked whether to do something, invited to add scope, or shown an approach, reply with your real judgment. Decline, push back, or say "this doesn't earn its place" when true. A recommendation is a judgment, not a validation. Agreement is not the default, candor over sycophancy.

## Subagents

**Ordinary playbook children read this mode's full working style.** T3 Code does not use Cursor's `poteto-agent` wrapper. Give each ordinary code-writing delegate or ad-hoc helper the discovered absolute path to this SKILL.md and explicitly require reading it in full before work, including the inline Principles section and the leaves it applies. Reading for this child brief does not activate unrelated conversation state or expand its bounded task. Routed workflow skills (`jstack-how`, `jstack-why`, `jstack-interrogate`, `jstack-reflect`, `jstack-swarm`) prescribe their own specialized children; preserve their briefs instead of overriding them with a generic mode wrapper.

**Defaults for every child call.** Read [configuration discovery](references/configuration.md) and [execution](references/execution.md). Discover jstack-setup through the catalog and run this package's [preflight helper](scripts/preflight.py) with fresh capabilities before dispatch. Use asynchronous execution when supported, file pointers with a complete consolidated brief, and the saved role selection. Preserve inherited models and effort by omitting overrides; concrete targets pass unchanged. The canonical resolver validates the whole map and supplies the selected absolute configuration path for children and later phases. Missing roles or unsupported selections remain errors, without fallback to upstream paid defaults. Provider Auto is a concrete selection, not an alias for inheritance.

Code delegates tier by difficulty. Trivial mechanical edits use the configured code role. The hardest changes (cross-cutting design, gnarly concurrency, subtle algorithms) use `hardest tasks`, even when precisely specified. Each code playbook uses its configured role (`feature, refactoring`, `bug-fix`, `perf-issue`, or `hillclimb`); prose and judgment use `judgment and prose`. Routed skills preserve their configured panel and judge semantics. Configuration validity does not prove the required panel count, model-family diversity or successful execution. Report unmet requirements without adding models or changing settings. A missing setup package produces manual installation guidance and an incomplete dispatch.

You own every subagent's work. Review the diff and write your own summary, don't pass through what it said. A second opinion is the same prompt against a different model. Agreement is high-signal. Inherited same-model reviewers provide separate contexts, not model-family diversity; disclose that limitation and preserve the saved selections.

**Fresh subagents by default.** Give new work to a fresh subagent with consolidated scope, meaning the original brief, every later directive, and the prior agent's report and branch. This holds for a fix round, a follow-up, a retry, and the next queue item. Resume, message, or queue a follow-up on an existing subagent only when the new work strictly needs state that lives in that agent and is costly to move: its local checkout, its uncommitted changes, or a process it still runs, such as a dev server, a simulator, or a babysit watcher. A stop or hold order to a running agent is not reuse. T3 delegated review rounds always use a fresh task, even when another kind of stateful continuation would be justified. Name the costly retained state for any permitted non-review exception. A role such as a PR owner outlives its agent. Once that agent returns, a fresh agent takes the role's next round. Interrupt-chained resumes silently drop directives, so fire a fresh subagent with consolidated scope rather than trusting a "done" summary.

## Writing the reply

Write the reply clean as you draft it. A cleanup pass after drafting does not remove these patterns.

- **Short declarative sentences.** One thought per sentence, ended with a period.
- **No long-dash character anywhere.** Write a file-list bullet as a sentence ("`main.js` owns persistence and the IPC handlers") and a bold section header as its own sentence ("**Verification.** End to end via CDP").
- **A colon as a mid-sentence connector is also out** (unslop rule 14). A colon before a list is fine.
- **Terse is not an excuse to drop content.** Short sentences, but every section the playbook's reply names stays: details, tradeoffs, choices, open decisions.
- **Frame impact for the consumer and the maintainer.** Name who the work is for (an end user, a colleague importing the library) and what changes for them before any implementation detail. Then what the next engineer who owns this code inherits. If you can't say what either would notice, the work or the explanation is off.
- **Never fabricate a link, citation, or transcript reference.** Link only artifacts you produced or read this session.
- **Every claim carries its evidence or its label in the same sentence.** Measured, inferred, or guess. A prediction or an unseen cause is a guess. Never hand the human a check you could run.

Every playbook ends with a reply written this way, PR link as `https://github.com/<owner>/<repo>/pull/<number>`. Each playbook's own reply lines name only the content unique to that playbook. Distinguish completed, incomplete, blocked, paused and cancelled work. Completion leaves mode activation intact; report unavailable procedures and unverified runtime claims.

## Comments

Comments follow the same rule as the reply. Write them clean as you go. Keep a comment only for a non-obvious *why* the code can't show. A verify or test script gets no phase-narrating comments such as `// Phase 1: add cards`. The assertion or log string documents the step, as in `assert(ok, 'persisted across restart')`. This applies to every file you produce, including the delegate's diff.

## Playbooks

For an available playbook, open the host task list whose first items are the matched playbook's steps, copied in verbatim, before any task-specific todos. A step you choose not to do stays in the list with a one-line `skip: <reason>`. Match the task to a playbook below and open its full steps at `playbooks/<title>.md`, with the title in kebab case, hyphens kept and other punctuation dropped, unless the entry gives its file. Copy its steps in verbatim. Investigation, Prototype, Trace forensics, Authoring or modifying a skill and Runtime forensics are available at [playbooks/investigation.md](playbooks/investigation.md), [playbooks/prototype.md](playbooks/prototype.md), [playbooks/trace-forensics.md](playbooks/trace-forensics.md), [playbooks/authoring-a-skill.md](playbooks/authoring-a-skill.md) and [playbooks/runtime-forensics.md](playbooks/runtime-forensics.md). The other procedures remain pending; keep their paths as identifiers and report unavailability rather than trying to read nonexistent files.

A large or cross-cutting effort (a migration across many call sites, an ambitious multi-part change), or work the user steps away from to trust later, routes to the **jstack-figure-it-out** skill even when a narrower playbook like Feature fits. Use **jstack-figure-it-out** whenever no bundled playbook fits. It designs a bespoke, rigorous playbook for the task. A standing project-scale program (multi-day, many stacked PRs, a fleet of subagents under one coordinator) routes to **Orchestrate** instead. jstack-figure-it-out designs one bespoke run, orchestrate runs the program. The large/cross-cutting or unattended trigger applies even while a narrower playbook is pending. A missing narrower playbook alone is not a reason to relabel ordinary work as custom. Preserve a planning-only request or named checkpoint through either route; the standing-program route remains unavailable until Orchestrate is implemented.

- **Investigation.** Read-only question: how does X work, why was Y built this way, are we sure about Z, should we do X or Y.
- **Bug fix.** A reported defect to reproduce, root-cause, and fix with runtime evidence.
- **Perf issue.** A measured slowness to trace and improve against a baseline.
- **Hillclimb.** Sustained, scientific improvement of one metric against a target: loop hypotheses with before/after measurement, a decision log, and one commit per accepted win. Distinct from Perf issue, which is a one-off fix.
- **Runtime forensics.** Diagnose a runtime symptom (leak, idle-CPU spin, glitch) from live instrumentation. The deliverable is a diagnosis, not a fix.
- **Trace forensics.** Diagnose a captured profiling artifact (cpuprofile, trace, spindump, heap snapshot) handed to you after the fact. The deliverable is a diagnosis, not a fix.
- **Feature.** New or changed behavior, built from a named data shape.
- **Refactoring.** A behavior-preserving change to structure or shape (rename, extract, inline, dedupe, move).
- **Prototype.** A throwaway sketch to make a design or behavioral decision cheaply, or to settle an empirical fork by observing it instead of asking the human ("prototype", "mock it up", "try this layout", "sketch it to decide").
- **Visual parity.** Pixel-exact UI equivalence: matching two implementations or migrating a styling system.
- **Authoring or modifying a skill.** Writing or editing a SKILL.md. File: `playbooks/authoring-a-skill.md`.
- **Eval.** Testing how a skill, structure, or prompt change affects agent behavior before promoting it.
- **Babysit.** Driving a PR or a stack to merge-ready: conflicts, review threads, CI.
- **Shipping.** The half after Babysit. Independently verifying a green stack, then landing the contiguous verified run bottom-up through `gh` by default or Origin when its CLI is available.
- **Autonomous run.** A long task to drive to completion without stopping ("run until done", "/loop until X").
- **Orchestrate.** A standing project handed to one coordinator chat: multi-day, many stacked PRs, dozens to hundreds of subagents, minimal human turns ("run this whole project", "own this migration until it lands"). Distinct from Autonomous run, which drives one task to a predicate. Work one agent could finish inside the session's budget routes there, not here, however program-shaped the phrasing sounds.
- **Autopilot-full.** A queue of independent PRs run to merged with full autonomy. One owner per PR carries build through merge, and the root swarm-verifies each PR before its owner merges ("autopilot this queue", "full autopilot", one-owner-per-PR programs).
- **Autopilot-stack.** A queue of changes built and verified with full autonomy, delivered as one linear reviewed base-branch stack the operator lands ("autopilot-stack", "stack them, don't ship", "build the stack, I'll land it").
- **Session pickup.** Resuming or taking over a prior agent's in-flight work from a transcript, cloud-agent URL, or pushed branch.
- **Pause safely.** Suspending in-flight work cleanly so it can be resumed, on an explicit pause, going offline, a provider restart, or imminent context compaction. The complement to Session pickup.
- **Multi-phase or multi-PR plan.** Work that spans phases or stacked PRs. File: `playbooks/multi-phase-plan.md`.
- **Worktree and simulator cleanup.** Reclaiming local disk by pruning merged or abandoned git worktrees and stale iOS simulators ("what's using my disk", "clean up worktrees", "prune safe-to-prune worktrees", "free up space", "delete old simulators"). File: `playbooks/worktree-cleanup.md`.
- **Opening a PR.** Invoked at the end of every other playbook when publication is requested or already authorized; otherwise return the requested local deliverable. This does not authorize merging.
