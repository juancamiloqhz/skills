---
name: jstack-architect
description: "Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /jstack-architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
---

# Architect

Before writing code, trace every system the change touches, then sketch two different shapes for it (types, signatures, module boundaries) and pick the one where each piece of state has one owner, each task has one way to do it, and callers need to know least. Redesign instead of patching if workarounds repeat.

For a large or contested design, run the **jstack-arena** skill instead of sketching alone. Discover it through the current catalog or an explicitly supplied authoring path and read its entrypoint; if several entries share the name, use source metadata to identify `juancamiloqhz/skills`. If it is unavailable or ambiguous, report the design incomplete and provide `npx skills add juancamiloqhz/skills --skill jstack-arena` for manual installation. Pass Arena an explicit design-only return; Architect owns any later implementation.

Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. A design-only or ambiguous design request returns the design without implementation or executable placeholders in the target project. An explicit checkpoint request, such as "with checkpoint" or "stop and show me before implementing", pauses for sign-off after the design. Already authorized implementation continues without another approval; commits, PRs, merges and installation follow the original task's authority.
