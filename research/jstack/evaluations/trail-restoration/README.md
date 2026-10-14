# Workflow and decision-trail restoration

This correction follows merged PR #31 at `6feca1dd9d8b9b2e902649f150724ae838f6bfed`. It restores Figure-it-out and standalone Show me your work from the unchanged pstack pin `11713c683fe4add4fd403ea880580abbc9e0875f`.

Figure-it-out again has Start and Phase A–E, high-biased rigor, a judge for every delegated unit and an explicit audit-trail phase woven through execution. The separate trail skill owns its format, logger, template, run-boundary audit and Attention handoff. The previous local decision-trail summary is removed.

## Exact-source accounting

[compare.py](compare.py) compares all four source files and both MIT notices against the shared bare cache. [source-comparison.json](source-comparison.json) records exact hashes and unified differences, plus the three jstack-only support references. The parent read every difference. The executable logger and TSV template are byte-identical to upstream. The source example retains actual tabs; lint exceptions preserve it rather than converting the example to spaces.

```bash
python3 -B research/jstack/evaluations/trail-restoration/compare.py > /tmp/jstack-trail-source.json
cmp research/jstack/evaluations/trail-restoration/source-comparison.json /tmp/jstack-trail-source.json
python3 -B research/jstack/evaluations/trail-restoration/test_log.py
```

[Figure-it-out](../../adaptations/figure-it-out.md) and [Show me your work](../../adaptations/show-me-your-work.md) document remaining runtime, authority and formatting differences. New standalone mapping and dependency watches do not change old pins, reviewed checkpoint or historical decisions. The two existing Figure-it-out support references remain unchanged. [Checks](checks.json) record package, manifest, link, syntax and Markdown validation, with protected-file comparisons.

## Executed logger checks

[test_log.py](test_log.py) invokes the real executable in temporary directories. [Results](logger-results.json) cover invalid argument counts, nested directories, first/later append, exact template header, UTC timestamps, existing-row preservation, empty cells, embedded CR/tab/newline normalization, all four formula prefixes and appended corrections. The logger is tested with serial writes; no concurrent-write or network-mount fault-injection claim is made. The skill explicitly makes serialization the coordinator's responsibility.

## Forward exercises

The parent wrote [expected cases](cases.json) before dispatch and withheld them from fresh-context evaluators. [Fixtures](fixtures) are synthetic and preserve the exact original inputs. Paths inside them refer to the original `/tmp/jstack-trail-eval/` directories. Recreating those directories from the matching fixture subdirectories permits replay; the deliberately missing evidence files must remain absent. The parent inspected actual artifacts, not just agent summaries.

The audit evaluator applied the skill and real logger to a log alternating between runs A and B. It appended a new A start boundary, a correction for a false pass, a repair to an absent evidence pointer, an omitted pivot and an audit receipt. Original bytes stayed intact. It audited A's two historical stretches and its continuation, leaving B's claims outside scope. Its handoff reported pending review and bounded synthetic history rather than inventing verification or a reviewer.

The planning evaluator applied Figure-it-out to a proposed strict-date CSV migration. It reused the existing verification design, proposed baseline capture, avoided an unnecessary architecture comparison, required a separate judge for both delegated units, and routed the trail to its standalone owner. It returned at the planning boundary without implementation or dispatch. The source retains all A–E phases; the artifact ends at B and describes the later execution phases prospectively.

A separate reviewer then inspected the corrected trail and supplied evidence through the resolved inherited `judgment and prose` selection. [Evaluation](evaluation.json) records the outcome, task identities and limits. [Outputs](outputs.json) retain the unedited evaluator/reviewer reports and corrected trail as strings. [Hashes](fixture-hashes.json) identify the original fixtures. This is a bounded audit/review sequence, not a full production migration or a cross-family comparison.

## Limits

Saved settings remain unchanged. Canonical resolution of the global `judgment and prose` role returned `[null]`; native children inherited the executing Codex gpt-6-astra model and effort without overrides. The separate reviewer supplies another context, not upstream's required model-family diversity. That difference is explicit and follows the user's inherited-model configuration. Explicitly required cross-family review would remain incomplete under these settings.

The fixture test outcomes are supplied JSON evidence, not parser tests executed by these agents. Their historical transcript is a bounded digest. Full-history fidelity, installed discovery, provider invocation, cross-provider dispatch, failure/cancellation paths, real delegated implementation and the later end-to-end workflow remain unverified. Historical evaluations retain their original files and limitations. No installation, schedule or model configuration changes are included.
