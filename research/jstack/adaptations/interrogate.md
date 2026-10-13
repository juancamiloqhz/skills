# Upstream attribution

Relocated from the skill package on 2026-10-13. This record describes the existing adaptation; it does not approve every difference. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) classifies remaining corrections.

Adapted from [pstack interrogate](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/SKILL.md) and its reviewer prompt, rubric, code-quality and lead-judgment references at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The bundled [MIT license](../../../skills/jstack/interrogate/LICENSE) retains Lauren Tan's attribution.

Jstack preserves common reviewer briefs, adversarial evidence, duplicate merging, agreement/disagreement reporting and lead judgment in four categories. It supports design artifacts for Architect callers as well as code diffs and remains independently invocable through normal skill discovery.

Canonical setup configuration replaces fixed model tables and rejected-model substitutions. Configured seats are preserved, including a valid single seat; same-model review does not claim model diversity. Explicit diversity requirements are checked before spending reviewer work. T3 lifecycle and demonstrated path handling replace assumptions about a read-only tool flag or simultaneous writers.

The lead verifies findings rather than ranking truth by consensus. File-size thresholds, blanket compatibility deletion and a five-blocker cap become evidence-based judgments. Review remains report-only, missing reviewers remain incomplete coverage, and design inspection is distinguished from runtime verification.
