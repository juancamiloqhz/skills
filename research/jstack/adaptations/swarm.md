# Upstream attribution

Relocated from the skill package on 2026-10-13. This record describes the existing adaptation; it does not approve every difference. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) classifies remaining corrections.

Adapted from [pstack swarm](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/swarm/SKILL.md) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The bundled [MIT license](../../../skills/jstack/swarm/LICENSE) retains Lauren Tan's attribution.

Jstack preserves Frame, Fan out, Aggregate and Report, partition/race/mixed shapes, declared race rules, exact revision and measurement evidence, and one fresh retry for missing required evidence. Reports keep PASS, ISSUES and BLOCKED worker outcomes distinct from overall coverage.

Canonical scalar `swarm workers` replaces fixed defaults and rejected-model substitutions. Worker count comes from task decomposition. A distinct-model race cannot be represented by the current scalar contract, so it returns an unmet prerequisite instead of inventing selections. T3 capabilities, workspace evidence and lifecycle replace cloud-environment flags and assumed unlimited simultaneous dispatch.

Required coverage gaps remain incomplete. First-pass selection verifies output, then cancels or drains outstanding owned work before returning. Authorized source changes require a coordinator integration check; read-only work stays read-only. These boundaries preserve user work and make partial results distinguishable from completed tasks.
