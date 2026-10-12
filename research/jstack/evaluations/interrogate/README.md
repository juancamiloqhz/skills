# Interrogate evaluation

Authoring-source evaluation against main revision `5e72f613a830f442c00a37e6e583f9aabebdeb30` plus the Interrogate working changes. Raw artifacts remain in `/tmp/jstack-interrogate-tzccn3tn`. Explicit source paths were used; installed skill discovery was not tested.

## Executed cases

| Case | Result | Evidence |
| --- | --- | --- |
| Two-reviewer code review | Both reviewers found the two seeded defects. The lead reproduced them, merged duplicate findings and returned Act on recommendations without fixes. | [Code record](code-results.json) |
| Single-reviewer design review | One reviewer found no supported defect in a valid half-open interval design. The lead checked the reasoning and reported static-only coverage without inventing findings or consensus. | [Design record](design-results.json) |
| Required two-family diversity with one configured seat | Canonical resolution succeeded, but the workflow stopped incomplete before any new reviewer dispatch. No seats or settings were changed. | [Design record, case 2](design-results.json) |

The code fixture deliberately replaced strict overlap comparisons with inclusive comparisons and removed the default from cancellation lookup. Reviewers were told the public contract, not the seeded defects. Each independently reported rejected adjacent reservations and `KeyError` for unknown or repeated cancellation. The lead checked public call paths and ran in-memory Python probes with bytecode disabled. All four original findings were attributed and deduplicated into two actionable issues. The reviewed source is retained in the JSON record, still defective by design.

The parent inspected the reports and verified protected source, notes and selected-config hashes against the baseline. All three reviewer children and both evaluation coordinators completed without pending nested work. The real global configuration was unchanged. Temporary configurations supplied two inherited seats for code and one for design; all executed reviewers used Codex `gpt-6-astra`. Same-model corroboration was disclosed, not described as model-family diversity.

## Limits

These are bounded code and design cases. Failed-reviewer coverage, input drift, explicit reviewer disagreements, dismissal of false positives, branch-base selection, concrete cross-provider routing and installed discovery remain untested. The code reviewers initially attempted unavailable `python` before successfully using `python3`; the evidence retains this recovery. Design reasoning is not executed product behavior. Hash and report-path checks do not constitute a complete filesystem audit.

Full live catalogs remain in raw evidence where captured. Committed records retain effective capability summaries, actual dispatch identities, exact briefs, terminal records and complete reports without the unrelated model catalog. No playbook is marked implemented by this helper evaluation.
