# Interrogate lead-judgment update

The [coverage audit](../../coverage-audits/2026-10-18/README.md) identified a shorter upstream lead-review reference. This update adopts it without changing reviewer dispatch or model selection.

## Source and scope

Local base is merged PR #87, `f06138c22fb3ea55e071b8c12daf2163233cb4bd`. Compare `pstack/skills/interrogate/` from its original adaptation pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/interrogate).

Two paths changed upstream:

- `references/lead-judgment.md` removes its opening context section and verdict-calibration section. Adopt the full new reference with only the existing blank line before a list. This also removes the now-unnecessary local clarification that the five-item warning was not a cap. Hypothetical-versus-actual checking, contextual filtering and singleton security/correctness scrutiny remain intact.
- `SKILL.md` adds Composer/Cursor-Grok fallback families and adaptive effort/speed. Keep the existing canonical configuration contract. Unsupported configured selections remain incomplete, and selected options pass unchanged. These source changes require the separate model-policy decision identified in the audit.

The parent compared every mapped package file with the audited source. Remaining differences are the existing [documented adaptations](../../adaptations/interrogate.md): identity and invocation metadata, task authority and source identity, configured seats and host dispatch, terminal-result checks, reviewer read-only boundaries, tool naming, structural proposals and formatting. The extra execution reference and all other package files are unchanged. The package license matches the source notice. Source pins, manifest, reviewed checkpoint and model configuration remain unchanged.

The old local reference already stated that five findings was not a cap. This is an upstream alignment update, not evidence that jstack previously hid a sixth finding. The entrypoint still requires every supplied finding to receive a disposition and rationale, including dismissals.

## Reproduction

Reuse the existing [invoice source](../design-review-restoration/fixtures/interrogate/invoices.py) and [synthetic reviewer packet](../design-review-restoration/fixtures/interrogate/input.json). Copy them into owned scratch and change only the packet's `source_path` and writable result path to that scratch location. Do not duplicate the fixture in the repository.

Ask a fresh evaluator to read the current `jstack-interrogate/SKILL.md` and relevant review references, source-review the fixture, and reconcile the packet into a lead verdict. Limit writes to its assigned report. Do not spawn a reviewer panel, execute the application or change models/configuration. Withhold earlier reports and expected-case files.

Acceptance checks, chosen before dispatch, reuse the historical fixture's cases: retain reachable correctness/security defects including singletons; account for more than five independent issues; assess pass-through complexity; reject unconditional splitting of a generated file, premature removal of the compatibility route and the claimed missing-key crash. Identify synthetic attribution, report static-review limits and preserve source bytes.

## Results

One fresh native Codex evaluator used inherited GPT-6-Astra/high. It read the current entrypoint and review references, inspected the numbered Python source, then reconciled the supplied packet. It wrote only its assigned cache report and did not dispatch reviewers or execute the application.

| Evidence | Observed disposition |
| --- | --- |
| Missing delete ownership and payment retry idempotency, each raised by A and B | Retained; duplicate claims merged into two issues. |
| Read ownership, reversed expiry, raw-token logging, negative page index and unbounded search limit, each raised only by A | All five retained after tracing the supplied source and caller constraints. B's silence was not treated as evidence of safety. |
| Five pass-through status wrappers, raised only by B | Retained as a maintainability issue under the supplied strict review lens; no performance measurement claimed. |
| Unconditional split of a generated file and immediate removal of the compatibility route | Dismissed against the supplied generated-file and external-client context. The report disclosed that those files were not available for inspection. |
| Alleged unchecked missing `invoice_id` access | Dismissed because `validate_payload` raises before the lookup. HTTP handling of that exception remained unverified. |

All 13 claim instances received a disposition, resulting in eight distinct actionable issues and three dismissals. Seven actionable issues concern correctness/security; the eighth is the wrapper chain. The earlier historical exercise grouped both ownership paths and reported seven blocker groups. That grouping difference is not evidence of a newly found defect or higher accuracy.

The parent inspected the report against the source and all acceptance cases. Protected hashes confirmed the source, relocated packet and skill package unchanged by the evaluator. It identified the packet as synthetic, made no model-diversity claim, and disclosed that router, database, gateway, generated-file and compatibility facts came from supplied context. The outcome passes the bounded lead-judgment checks.

## Checks and limits

Four packaging tests, skill validation, documentation consistency and diff checks pass. The final lead reference matches the audited source except for list spacing. No installed package changes are part of this PR.

This checks lead judgment against supplied reviewer evidence. It does not exercise the production reviewer fan-out, configuration resolution, cross-provider behavior or application runtime. It is not a measurement of improved review accuracy. Raw evaluator output and input hashes remain in task-owned cache; this report and the existing fixture are the retained reproduction material.

## Normal use

After merge and a manual skill update, ask `jstack-interrogate`: "Review this invoice change before we merge." The lead checks reviewer claims against the source, retains real defects even when there are more than five, and explains rejected claims. Review permission alone does not apply fixes or merge the change.
