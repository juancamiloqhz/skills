# Upstream attribution

Relocated from the skill package on 2026-10-13. This record describes the existing adaptation; it does not approve every difference. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) classifies remaining corrections.

Adapted from [pstack how](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/how) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`, inspected on 2026-10-11. The bundled [MIT license](../../../skills/jstack/how/LICENSE) retains Lauren Tan's attribution. Like upstream, this is a separately invocable skill.

Configured jstack roles replace fixed model defaults and fallback selections. The separately discovered setup-jstack installation owns the resolver and shared investigation contract. Invalid settings or unavailable execution capability stop the affected phase without substitutions. Direct invocation does not activate juan-mode. Normal skill discovery remains enabled so a playbook can call this skill; upstream's Cursor-specific explicit-only frontmatter is not copied.

The simple path uses one explainer; the complex path uses two to four distinct explorers followed by one explainer. Source explanations distinguish traced behavior from execution. Concurrent exploration is allowed when scoped safely, but the initial complex-case evaluation ran explorers serially.
