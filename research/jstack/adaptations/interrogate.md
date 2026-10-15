# Interrogate adaptation

The [2026-10-15 naming decision](../skill-names.md) additionally changes this package's local identity and callers. Its upstream identity, procedure and revision pin remain as recorded below.

Source: [pstack interrogate](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate), revision `11713c683fe4add4fd403ea880580abbc9e0875f`. Local package: [interrogate](../../../skills/jstack/jstack-interrogate/SKILL.md). Its [MIT license](../../../skills/jstack/jstack-interrogate/LICENSE) matches the pinned plugin notice.

This correction restores the source's five-step entrypoint and four reference files. It removes the jstack-only `references/review-criteria.md` summary in favor of the original reviewer prompt, rubric and code-quality lens. The full lead framework returns, including hypothetical-versus-actual checking, singleton security scrutiny and verdict calibration. See the [comparison and evaluation](../evaluations/design-review-restoration/README.md).

The earlier record at `34cbcca75dabd8d58e1d2b0945f6d550cfa572c7` incorrectly described upstream as requiring blanket compatibility deletion and a five-blocker cap. The source already conditions deletion on external consumers and describes five items as a calibration warning. Its file-size rule already allows a compelling structural exception. This restoration preserves those distinctions and the source's strict maintainability bar.

## Remaining differences

| Local file | Difference from the same upstream relative path | Requirement and verification |
| --- | --- | --- |
| `SKILL.md` frontmatter | Omit `disable-model-invocation: true`; retain source name/description. | The [catalog-call compatibility exception](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) applies to this helper too. Automatic selection remains possible; full provider invocation is unverified. |
| `SKILL.md` introduction, Scope and Spawn | Preserve configured seats including a single inherited seat; disclose actual diversity. Add task scope, source-only reads, actual base/merge-base and input hashes, design-artifact review, complete child briefs and execution-reference lookup. | Existing Jstack callers include design reviews. Configured models, source identity and host capacity control the review; review permission does not authorize fixes. |
| `SKILL.md` Spawn | Replace Cursor Task options, `.mdc` model lines, fixed defaults, rejected-slug substitutions and automatic default-table PR with the canonical resolver and T3/native dispatch contract. | User-owned model settings and actual tool capabilities take precedence. Unsupported selections stop incomplete without changing settings. |
| `SKILL.md` Synthesize and output | Check all terminal reports, retain failed-seat coverage gaps, verify decisive claims, distinguish silence from agreement and repeated models from diversity; report hashes and real checks. | Async completion and shared evidence must be checked. The bounded synthetic packet exercises lead judgment, not reviewer fan-out. |
| `references/reviewer-prompt.md` | Add design/static distinction, assigned-report-only writes and no further delegation or peer findings. Add a code-fence language. | Report-only authority and separate reviewer contexts; formatting has no procedure effect. |
| `references/rubric.md` | Replace named Cursor read/search tools with available file reads and search. | Tool names vary by host. All substantive source criteria remain. |
| `references/code-quality-review.md` | Clarify that structural improvements are proposals during review. | The source's quoted audit prompt includes action language; the entrypoint's report-only boundary governs it. The strict criteria are otherwise unchanged. |
| `references/lead-judgment.md` | Retain the five-item warning and explicitly state it is not a cap on verified blockers. Add a list-spacing fix. | Avoid hiding correctness or security findings to satisfy a count. The fixture retains more than five blocker groups after rejecting unsupported claims. |

The existing jstack-only [execution contract](../../../skills/jstack/jstack-interrogate/references/execution.md) is unchanged. It supplies canonical setup lookup, inherited/concrete dispatch, capabilities, owned outputs and terminal checks. Markdown spacing changes preserve source organization. Pins, checkpoint, historical evidence and setup contracts remain unchanged.
