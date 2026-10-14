# Verification generator adaptation

Adapted from Lauren Tan's pstack `create-verification-skill` at `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`. The 2026-10-14 restoration follows the [fidelity policy](../upstream-fidelity.md). [Comparison and evaluation](../evaluations/verification-restoration/README.md) cover the final files; the pin and reviewed checkpoint are unchanged.

## Files and retained structure

| Upstream file under `pstack/skills/create-verification-skill/` | Local file under `skills/jstack/create-verification-skill/` | Disposition |
| --- | --- | --- |
| `SKILL.md` | `SKILL.md` | Restore all five numbered sections, repository interview, six inline output requirements, executable-helper requirement, one-feature proof and cadence only when asked. Differences below. |
| `references/feature-map-example/README.md` | Same relative path | Restored byte-for-byte. |
| `references/feature-map-example/create-note.md` | Same relative path | Restored byte-for-byte. |
| `references/feature-map-example/search.md` | Same relative path | Restored byte-for-byte. |

The earlier jstack `references/output-contract.md` is removed. The source's inline requirements and worked examples again own the contract. Notes commands illustrate output shape; the generated skill must use its actual application. [Package LICENSE](../../../skills/jstack/create-verification-skill/LICENSE) matches `pstack/LICENSE` at the pin, including Lauren Tan's copyright notice.

## Remaining differences

| Location | Exact difference and reason | Verification or limit |
| --- | --- | --- |
| Frontmatter | Omit `disable-model-invocation: true` so setup's approved optional offer can discover and invoke the generator through the provider catalog. Preserve source name and description. | Same shared-package compatibility exception as the [invocation guard assessment](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata). Automatic model selection remains possible; live discovery on every provider is unverified. |
| Introduction and output paths | Default to `.agents/skills`, honoring an explicit destination or repository convention. Preserve existing suitable skills and other work; documentation-only repositories need no invented executable app. | Existing multi-provider packaging; fresh CLI generation and reuse are evaluated. No installation or settings mutation is implied. |
| Interview | Baseline repair follows task authority. Use T3's preview tools and ownership/fallback rules when applicable; missing prerequisites do not authorize installation. | Concrete host tool substitution and manual-installation decision. Browser execution is not covered by this CLI evaluation. |
| Inline Launch and Doctor | Noninteractive CLIs may use subprocesses; interactive terminal behavior still needs PTY/tmux. Libraries use public API clients. Separate scratch/evidence; doctor checks readiness without seeding state. | Pocket is a noninteractive Python CLI. Library and interactive-terminal behavior remain untested. |
| Inline Evidence, Cleanup and Helpers | Fail on wrong output even with exit zero, preserve diagnostics, verify owned cleanup, use portable paths and keep secrets out of proof. Verification recipes grant no external-action authority. | Enforces the source's real-path proof and evidence-survival contract within the authorized workspace. Independent reuse and maintenance's zero-exit regression exercise these requirements. |
| Generate, after the six inline requirements | Automatically link the whole canonical package at `.claude/skills/verify-<app>` using a relative target, on every provider. Preserve conflicts and verify all files resolve inside the authorized repository. | **Explicit user decision, 2026-10-14:** [keep automatic linking](../decisions.md#automatic-claude-linking-2026-10-14). This is an intentional addition, not a runtime necessity. Filesystem link verification does not prove Claude session discovery. |
| Seed and proof | Explain the illustrative examples, distinguish exercised coverage, report output/link/evidence paths and unresolved failures. | Retains the source's one-feature generation threshold; broader feature coverage belongs to later runs. |
| Maintenance offer | Discover the separate maintenance package; if missing, provide a manual install command. Keep cadence suggestions conditional on the user asking. | Preserves separately installable skills and manual installation. Manifest context now tracks maintenance. |

This is not an official Cursor, pstack or T3 Code integration. Historical generator and linking evaluations remain unchanged; they are not relabeled as tests of this restoration.
