---
name: how
description: Explain how code works, including runtime flow, component ownership and failure behavior. Use for code walkthroughs and placement or layering questions; use why for historical rationale.
---

# How a subsystem works

Run directly for the user's question or as a procedure called by a juan-mode playbook. Direct invocation is task-scoped and does not activate juan-mode. Return checked findings to the user or calling playbook; investigation does not authorize implementation.

Find `setup-jstack` in the executing provider's skill catalog, or use its explicitly supplied source path during authoring. Resolve all resources relative to that skill's advertised installation; it need not be a sibling of this skill. Read its `references/investigation.md` before executing the procedure. That shared contract defines configuration lookup, capability checks, child lifecycle, evidence and read-only scope. If setup-jstack or that contract is missing, report the dependency and provide `npx skills add juancamiloqhz/skills --skill setup-jstack` for manual installation or update. Keep model configuration unchanged. This skill does not require juan-mode or the companion investigation skill to be installed.

Use `why` for historical motivation when that skill is available; this skill explains runtime mechanics. See [upstream attribution](references/upstream.md) for the source and adaptations.

## Select the exploration scope

State the target and a useful interpretation if the question is ambiguous. For one function, module or narrow ownership question, resolve `how explainer` and dispatch one explainer that both inspects the source and writes the explanation. Prefer this path when extra exploration would duplicate work.

For a subsystem spanning distinct components, choose two to four non-overlapping angles and state that task count. Resolve `how explorer` and `how explainer` from the same selected config. Send one read-only explorer per angle, then one explainer after all findings arrive. Each explorer gets the original question, its angle and the common source scope; it does not expand into the other angles. The scalar explorer role supplies the selection for each task, not a configured panel.

## Explorer brief

Give each explorer the shared evidence contract and ask it to trace its assigned path from entrypoint through calls, data transformations and failure branches. Read implementations and relevant callers, not just symbol names. Identify ownership boundaries, external interfaces, surprising behavior and any edge that cannot be traced. Return file-and-line citations, the inspected revision, files read, the observed flow and open questions. Do not infer historical intent from an architectural pattern.

## Explainer brief and return

Give the explainer the original question, common evidence contract and all explorer findings. On the simple path it gathers this evidence itself. Ask it to reconcile disagreements by reading the source, then explain the trigger, data flow, key decisions, component ownership and relevant failure behavior. Include only the concepts and file map needed to understand the answer. Preserve untraced edges and distinguish static reading from executed checks. Use a diagram only when it makes the explanation easier to follow and the current host supports the format.

The coordinator checks the explanation's decisive source references and returns it with light edits for clarity. If evidence is incomplete, name the missing dependency or path. Do not turn an ownership recommendation into a patch or launch a later playbook from this helper.
