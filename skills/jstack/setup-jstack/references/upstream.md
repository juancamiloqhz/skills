# Upstream attribution

jstack is a portable adaptation of pstack's model setup concept and 17-role registry for T3 Code, independently implemented here. It is not an official Cursor, pstack or T3 Code release.

- Repository: [cursor/plugins](https://github.com/cursor/plugins).
- Inspected revision: `ccb5507cec1546dc88135c1139c811e6c59115ba`, October 10, 2026.
- Primary source: [setup-pstack](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/setup-pstack/SKILL.md).
- Consumer context: [poteto-mode](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/poteto-mode/SKILL.md).
- License: MIT, Copyright 2026 Lauren Tan. The upstream notice is retained in this skill's `LICENSE`.

Adaptations replace Cursor's always-applied rule, Task model slugs and Auto alias with a JSON contract for global defaults and optional project configuration, T3 Code live model/option discovery, explicit provider identity and parent inheritance. Project files replace the full global role map, and explicit file selections remain highest priority. No upstream playbooks or autonomous shipping rules are enabled. The repository's earlier pstack research and review evaluations retain their own separate source pins.

## Reasoning-budget rationale

[Pstack PR #366](https://github.com/cursor/plugins/pull/366), introduced in [commit 5bf2b1544db739998121a306340631963c2ff3de](https://github.com/cursor/plugins/commit/5bf2b1544db739998121a306340631963c2ff3de), explains that reducing reasoning spend previously required changing each role by hand. The budget choice applies an effort target across the working assignments before per-role confirmation.

Jstack keeps the four labels and target levels for conceptual compatibility. It adapts model slugs to provider-specific options and explicitly resolves the scope of rerun changes and retained overrides. This does not reproduce Cursor's rule-loading mechanism or make the budget a runtime spending limit. The source pin for the shipped setup adaptation above is unchanged.

## Investigation consumer contract

The shared [investigation contract](investigation.md) supports the standalone how/why consumers without activating a workflow during setup. Its evidence categories and confidence guidance derive from [pstack why](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The existing MIT notice covers this attribution. T3 Code capability checks, explicit configuration handoff and artifact ownership adapt that guidance to jstack. This additional source pin does not change the setup implementation's pin above.
