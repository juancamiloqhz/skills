# Upstream attribution

Relocated from the skill package on 2026-10-13. This record describes the existing adaptation; it does not approve every difference. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) classifies remaining corrections.

Adapted from [pstack arena](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/arena/SKILL.md) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The bundled [MIT license](../../../skills/jstack/arena/LICENSE) retains Lauren Tan's attribution.

Jstack preserves the Frame, Candidates, Cross-judge, Pick, Synthesize and Verify sequence, hidden scoring rubric, one cross-judge, coordinator comparison and coherent synthesis. It keeps Arena independently invocable, with normal skill discovery so future playbooks can call it. Setup-jstack supplies the configured panel and judge pool instead of fixed defaults or rejected-model substitutions. An architect caller can select its own runner panel and require structurally distinct design candidates.

At least two viable candidates are required for a comparison, including after dropouts. Configured seats are not multiplied automatically. A different-family judge is preferred, as upstream recommends; it is mandatory only when the caller requires it, and inheritance alone does not establish diversity. Judge alternatives with unavailable execution capability are distinguished from invalid saved settings.

Candidate writes follow demonstrated T3 path isolation instead of assuming prompt paths create workspaces. Original candidates remain intact for verification. Design-only callers receive a design artifact without source implementation. A successful source inspection or catalog check does not establish runtime behavior or provider UI discovery.
