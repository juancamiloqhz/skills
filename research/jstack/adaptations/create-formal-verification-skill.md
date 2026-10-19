# Formal verification generator adaptation

Source: `pstack/skills/create-formal-verification-skill/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. Local: [jstack-create-formal-verification-skill](../../../skills/jstack/jstack-create-formal-verification-skill/SKILL.md).

Preserve every source heading, target/tool selection, all seven quality requirements, generated-skill frontmatter, real-code mutation proof, restoration and scoped handoff. A current-code failure remains a finding; a passing bound does not prove the whole system. Keep the exact upstream license and explicit-invocation flag. Codex metadata adds a default prompt and disables implicit invocation.

| Location | Difference | Requirement and verification |
| --- | --- | --- |
| Identity | Prefix the package name and invocation with `jstack-`. | Portable naming decision; no automatic Juan-mode trigger or new model role. |
| Introduction | Discover actual installed tools/versions, honor authorized proof scope and keep missing prerequisites explicit. Use owned mutation scratch and preserve unrelated work. | Manual installation and product-change authority remain separate. A proposed command is not an executed proof. |
| Generate the verify skill | Respect explicit/existing destinations; default to `.agents/skills/verify-<area>-formal/`. Reuse suitable skills and resolve actual repository/package paths. | Supported portable project discovery, without colliding with an ordinary app-verification package or retaining a temporary checkout path. |
| Generate the verify skill | Automatically link each generated formal verification package under `.claude/skills/`, using a confined relative link; preserve conflicts and verify all supporting files resolve. | The user's [automatic linking decision](../decisions.md#automatic-claude-linking-2026-10-14) applies to every generated verification skill. This is the same intentional jstack addition as the existing app-verification generator, not an upstream requirement. |
| Prove and hand off | Report missing tools, unexercised mutations and unresolved links as incomplete. A stale-source warning alone is not a detected invariant violation. Distinguish a valid finding from broken tooling; report paths and restoration. | Honest evidence and required project linking. A baseline failure must survive restoration; mutation evidence must exercise the property, not only a change detector. |

See the [evaluation](../evaluations/formal-verification/README.md) for live generation, finite-state scope, mutation/restoration and supplied-evidence limits. No particular verifier, language or verification approach is mandated. This package has no named operational skill dependency. Existing skills, model configuration and reviewed upstream checkpoints remain unchanged; live installed-provider discovery is unverified.
