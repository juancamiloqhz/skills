# Upstream attribution

jstack is a portable T3-oriented adaptation of pstack's model setup concept and 17-role registry, independently implemented here. It is not an official Cursor, pstack or T3 release.

- Repository: [cursor/plugins](https://github.com/cursor/plugins).
- Inspected revision: `ccb5507cec1546dc88135c1139c811e6c59115ba`, October 10, 2026.
- Primary source: [setup-pstack](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/setup-pstack/SKILL.md).
- Consumer context: [poteto-mode](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/poteto-mode/SKILL.md).
- License: MIT, Copyright 2026 Lauren Tan. The upstream notice is retained in this skill's `LICENSE`.

Adaptations replace Cursor's always-applied rule, Task model slugs and Auto alias with a user-local JSON contract, T3 live model/option discovery, explicit provider identity and parent inheritance. No upstream playbooks or autonomous shipping rules are enabled. The repository's earlier pstack research and review evaluations retain their own separate source pins.

## Reasoning-budget rationale

[Pstack PR #366](https://github.com/cursor/plugins/pull/366), introduced in [commit 5bf2b1544db739998121a306340631963c2ff3de](https://github.com/cursor/plugins/commit/5bf2b1544db739998121a306340631963c2ff3de), explains that reducing reasoning spend previously required changing each role by hand. The budget choice applies an effort target across the working assignments before per-role confirmation.

Jstack keeps the four labels and target levels for conceptual compatibility. It adapts model slugs to provider-specific options and explicitly resolves the scope of rerun changes and retained overrides. This does not reproduce Cursor's rule-loading mechanism or make the budget a runtime spending limit. The source pin for the shipped setup adaptation above is unchanged.
