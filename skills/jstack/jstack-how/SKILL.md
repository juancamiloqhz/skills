---
name: jstack-how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use jstack-why for motivation."
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Run directly for the user's question or as a procedure called by a jstack-juan-mode playbook. Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. Return checked findings; investigation does not authorize implementation.

Discover `jstack-setup` through the executing provider's skill catalog, or use an explicitly supplied authoring path. Read its `references/investigation.md` before executing this procedure. That approved shared contract owns configuration lookup, T3 capability checks, task lifecycle, citation discipline and read-only scope. Resolve resources relative to its advertised installation rather than assuming sibling packages. If it is missing, report the dependency and provide `npx skills add juancamiloqhz/skills --skill jstack-setup` for manual installation. Preserve saved configuration.

Use the configured roles below through the shared contract. Omit targets for inherited selections; never replace a missing or rejected selection with a fixed model. Pass each child the question, source root/revision, selected absolute configuration path, shared contract, assigned template and bounded scope. Supply complete template contents with placeholders filled, or absolute paths the child must read. Resolve reference paths relative to this skill's advertised directory. Independent readers may run concurrently within actual capacity; findings writers use disjoint owned paths and remain serial until assigned-path behavior is demonstrated. Wait for terminal results with no pending children, then check artifacts before synthesis. A failed phase yields an incomplete result with retained findings, not fabricated coverage.

Explorers use `how explorer`; every explainer uses `how explainer`. These scalar roles choose a model for each task, not a worker count.

## 1. Assess complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. Spawn one explainer that explores and explains in one pass, built from `references/explainer-prompt.md` without the explorer-findings section. Go to step 4.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): go to step 2.

When in doubt, take the simple path.

## 2. Explore (complex only)

Decompose the question into 2 to 4 angles, each a distinct slice of the subsystem. Dispatch independent explorers concurrently when the shared contract permits, each with `references/explorer-prompt.md` and its angle filled in.

## 3. Synthesize (complex only)

Once all explorers have returned, spawn one explainer with `references/explainer-prompt.md` and every explorer's findings filled in.

## 4. Present

Check its decisive source citations, preserve untraced edges and distinguish static reading from actual execution. Present the explainer's output. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
