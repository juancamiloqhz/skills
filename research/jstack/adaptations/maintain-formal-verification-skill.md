# Formal verification maintenance adaptation

Source: `pstack/skills/maintain-formal-verification-skill/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`. Local package: [jstack-maintain-formal-verification-skill](../../../skills/jstack/jstack-maintain-formal-verification-skill/SKILL.md). The package preserves the exact `pstack/LICENSE` notice at that revision.

Preserve every source heading, the four per-check outcomes and combined updated/bug outcome, verification-only edit scope, all six Pass steps, and the complete report requirements. Preserve the dangerous stale-pass case, coverage beyond old filenames, intentional-promise evidence, real-code negative controls and counterexample replay, fallback to verification history when no sync commit is recorded, and unchanged checkpoints for blocked checks. Keep the source explicit-invocation flag and supply matching Codex metadata.

| Difference | Requirement and verification |
| --- | --- |
| Prefix the skill and generator command names with `jstack-`. | Portable naming policy. Discover the generator from the current catalog or explicit source path instead of assuming a sibling installation. |
| Add a short runtime/authority preface. | Respect the requested repository, actual tools and unrelated work; missing tools/history block the affected check. Installation, model changes and publication need their own authority. Direct invocation does not activate Juan-mode. |
| State scratch restoration and generated-input limits. | Real-code negative controls use owned copies and return to the original baseline, including existing findings. A generated-input fallback does not become formal proof through maintenance. |
| Qualify a committed sync record when covered product edits are uncommitted. | A commit must identify the code actually checked. Report uncommitted covered-code changes separately and preserve the old checkpoint until correspondence to the recorded revision is established. |
| Add `agents/openai.yaml` and distributed `LICENSE`. | Explicit-only Codex invocation and required notice, with no new model role or helper script. |

The generator handoff, Help table/recipes and guide now point to this available standalone procedure. The new manifest mapping is pinned to the adopted source; the existing generator mapping watches maintenance as context and retains its own historical adoption pin. Statechart and video catch-up remain deferred. No automatic installation, new model role, playbook, schedule or live provider discovery is introduced.

See the [history fixtures and evaluation](../evaluations/formal-maintenance/README.md) for source comparison, executed behavior and remaining limits. The original defer rationale remains in the 2026-10-25 upstream report; the user selected this adoption after PR #145.
