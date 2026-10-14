# Verification maintenance adaptation

Adapted from Lauren Tan's pstack `maintain-verification-skill` at `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`. The 2026-10-14 restoration follows the [fidelity policy](../upstream-fidelity.md). [Comparison and evaluation](../evaluations/verification-restoration/README.md) account for the final files. The pin and reviewed checkpoint remain unchanged.

## Files and restored behavior

`pstack/skills/maintain-verification-skill/SKILL.md` maps to `skills/jstack/maintain-verification-skill/SKILL.md`. Restore Outcomes, Edit scope and the numbered Pass 0–6. Each feature again gets a read-only source child, followed by reconciliation and coordinator-only live driving. The three live-session invariants, doctor repair and one retry, concrete `verified-unreachable` evidence, product-gap triage and rereading every changed file are retained.

The earlier parent-only source pass is removed. Missing prerequisites no longer automatically mean all maintenance is blocked: upstream permits an evidenced unreachable route. A separately reported product regression also does not automatically block an independently proven verification correction. These restore source behavior under the fidelity policy; they do not mark a failed or unreachable product feature as passed. Unfinished coverage, ambiguous intent, unsafe cleanup and unproven corrections remain blocked.

[Package LICENSE](../../../skills/jstack/maintain-verification-skill/LICENSE) matches `pstack/LICENSE` at the pin. The only added operational file is `references/execution.md`, described below. There are no upstream supporting files omitted from this package.

## Remaining differences

| Location | Exact difference and reason | Verification or limit |
| --- | --- | --- |
| Frontmatter | Omit `disable-model-invocation: true` to retain catalog discovery by the generator's maintenance offer and workflow callers. Preserve source name and description. | Shared-package [invocation compatibility exception](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata). Eligible for automatic selection; all-provider invocation remains unverified. |
| Outcomes | `changed` means proven corrections are ready; publishing still needs task authority. Report passed, failed and evidenced unreachable separately. | Source's product-gap triage and unreachable rule are restored without claiming a bug-free app. The bounded maintenance fixture exercises all three feature results. |
| Edit scope | Preserve unrelated work and proof, inspect scripts, establish owned state, and respect external-action authority. | Host/user constraints; edits remain inside the verification package. |
| Locate | Use canonical `.agents` or established repository layout; resolve Claude links before counting candidates and preserve dangling/conflicting/outside targets. Report missing maps. | Required by approved automatic linking. The fixture presents both canonical and linked paths as one target. |
| Source wave and new `references/execution.md` | Resolve the existing `how explorer` role through setup, validate the full selected map against fresh capabilities, propagate its absolute path, preserve inherit/null targets, and use supported native/T3 children. Queue to actual capacity; retain briefs, terminal findings and source identity. No parent-only substitute on failure. | Concrete T3/configuration adaptation. No new role or saved model changes. Fresh per-feature readers and coordinator drives are evaluated on inherited Codex; other providers and concrete targets remain untested here. |
| Reconcile | Disclose unavailable history; require every source reader terminal before live driving; refresh affected source review when reviewed inputs change. | Host task ownership and evidence freshness; the fixture supplies an explicit migration note and lacks Git history. |
| Live pass | Use T3 preview tool/ownership rules, public API/library interfaces or noninteractive subprocesses. Record feature/sub-feature coverage and rerun all affected features after a shared-helper change. | Retains source phase order and all three invariants. CLI evaluation covers failed drives, doctor repair, cleanup and retained proof. UI, library and wedged-session paths remain untested. |
| Triage | Require contract/history evidence before changing expected behavior; observed code alone cannot justify weakening assertions. | Distinguishes source's doc drift from product regressions. Fixture migration establishes intentional rename; unchanged body contract exposes a regression. |
| Ship | Return proven local changes unless publication was requested or already authorized; no implicit commit, push or merge. | Existing user-controlled delivery. Scratch run notes remain outside the target's committed changes. |

The manifest now tracks setup-pstack and the generator as context dependencies. Earlier maintenance evaluations explicitly prohibited delegation; they remain historical evidence, not proof of this restored source wave. This is not an official Cursor, pstack or T3 Code integration.
