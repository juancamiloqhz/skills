---
name: juan-mode
description: Apply jstack's task routing and configured delegation when the user invokes juan-mode, or continue an already active juan-mode conversation. Activation lasts until explicit opt-out.
---

# Juan-mode

Use the user's requested outcome to select a playbook, resolve the current jstack model assignments and coordinate verified work in T3 Code. Explicit invocation activates the mode in this conversation until the user turns it off. Reading this file for authoring or review does not activate it.

This package currently implements the execution foundation. All 23 playbooks are registered but awaiting implementation. Report a selected route as unavailable rather than improvising its missing procedure or claiming its workflow passed. Full release requires executed acceptance evidence for every route and the supported providers.

## Activation and task selection

On activation, opt-out, handoff or resume, follow [conversation state](references/activation.md). Apply the latest user instruction before loading models or dispatching work. An opt-out works even when configuration or T3 Code is unavailable. Mode activation does not expand the task's permissions.

For each new task while active, read the [route registry](references/routes.md), select by deliverable and report any unavailable procedure. Casual conversation does not start a playbook. Preserve ongoing work when a later message clarifies it; a new task needs a fresh route. Read an implemented playbook before using its steps. Use the user's existing authorization for concrete actions within its scope.

## Prepare execution

Before a routed task dispatches any child, read [configuration discovery](references/configuration.md). Discover the installed `setup-jstack` entrypoint from the current skill catalog, then use this package's [preflight helper](scripts/preflight.py) with a fresh T3 Code catalog. It calls the canonical resolver, validates the entire saved map, preserves ordered seats and options, and checks effective child capability. It reads configuration without changing it or launching agents.

Resolve each needed role. Configuration validity does not satisfy a workflow's required panel size or judge diversity. Read the role semantics in the configuration reference before fan-out. A missing dependency, stale selection or unavailable provider produces a precise limitation; preserve the user's saved settings.

Before delegation, read the [execution contract](references/execution.md). Give each child an explicit brief and bounded ownership, retain its task ID, and verify its artifacts. The parent owns shared plan state, PR watches and final synthesis. Use serial writes until the selected provider and tools have demonstrated assigned-checkout behavior.

## Completion

Report the requested outcome, actual verification and any remaining limitation. Distinguish completed, incomplete, blocked, paused and cancelled work. Task completion leaves mode activation intact. PR publication follows the requested delivery; merging, recurring scheduling and installation require their own applicable authorization. Skill installation remains manual.

The [upstream record](references/upstream.md) identifies the source revision and intentional differences. Detailed helper workflows, principles and playbooks arrive in the later implementation groups; their upstream names are not dependencies on unrelated global skills.
