# Upstream and adaptation

Based on Lauren Tan's pstack Arena at commit `e5a8186d7b43be8d6ac4452440fbead5f1a51c70` of `cursor/plugins`.

- [Pinned Arena](https://github.com/cursor/plugins/blob/e5a8186d7b43be8d6ac4452440fbead5f1a51c70/pstack/skills/arena/SKILL.md)
- [Pinned MIT license](https://github.com/cursor/plugins/blob/e5a8186d7b43be8d6ac4452440fbead5f1a51c70/pstack/LICENSE)
- The upstream license notice is retained in `../LICENSE`.

The adaptation retains independent candidates, task-specific grading, a fresh cross-judge, parent selection, synthesis, and verification. It replaces Cursor Task dispatch and model rules with live T3 capability discovery and T3 task lifecycle operations. Results are text summaries rather than candidate worktrees. Required principles are expressed locally; no upstream agent wrapper or principle registry is installed.

This is an experimental adaptation, not an official T3 or Cursor integration. It does not provide full Arena writing, poteto-mode, automatic synchronization, or provider-wide installation.

To update, compare the pinned Arena and referenced principles with the proposed revision. Review changes to independence, grounding, selection, verification, model routing, and lifecycle assumptions. Amend this subset only where needed, update the pin and license if changed, then rerun a two-provider candidate/judge evaluation. Keep the existing pin if the evaluation fails. Updating these instructions is separate from installing them into a provider.
