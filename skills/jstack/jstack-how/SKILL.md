---
name: jstack-how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use jstack-why for motivation."
---

# How

Explore the codebase to answer "how does X work?" questions.

Run directly for the user's question or as a procedure called by a jstack-juan-mode playbook. Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. Return checked findings; investigation does not authorize implementation.

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

## 1. Explain

Spawn one fresh read-only subagent that explores and explains in one pass. Prefer a native subagent; otherwise use T3 Code `delegate_task`. Omit any model or `target` override so it inherits the parent's provider, model and effort; never substitute a model. It may read the codebase but must not edit files, run mutating commands or change external systems. Give it the user's question, the absolute repository root and revision, and this brief:

> You are writing an architectural explanation for a senior engineer. Explore the codebase and write an explanation that a senior engineer unfamiliar with this area could read and walk away with a solid mental model. They should understand the architecture well enough to start working in it confidently. You have read-only access to the codebase.

Wait for its terminal result. If the subagent cannot run or fails, report the explanation incomplete; do not replace it with your own analysis.

## 2. Present

Check its decisive source citations, preserve untraced edges and distinguish static reading from actual execution. Present the subagent's output. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.
