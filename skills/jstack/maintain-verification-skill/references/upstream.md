# Upstream attribution

Adapted from Lauren Tan's pstack [maintain-verification-skill](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/maintain-verification-skill/SKILL.md) at `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`, inspected on 2026-10-11. The upstream [MIT license](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/LICENSE) notice is retained in this skill's `LICENSE`.

The adaptation retains feature-map reconciliation, source review, live exercise of each feature, verification-only edits, regression reporting, evidence preservation, cleanup, and clean/changed/blocked outcomes. It accepts the existing project-local skill path rather than requiring Cursor's directory. It is self-contained when installed separately from the generator.

Jstack leaves source review in the executing agent instead of requiring one subagent per feature. No model configuration or delegation is needed. The skill supports normal discovery, but upkeep remains a distinct task from an ordinary verification run. T3 Code browser operations follow the current runtime's tool and ownership rules. Missing prerequisites count as blocked coverage. Commit and PR creation follow the user's requested delivery instead of happening on every changed run. Installations and updates remain manual.

This is not an official Cursor, pstack or T3 Code integration.
