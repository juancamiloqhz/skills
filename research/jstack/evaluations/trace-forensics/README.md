# Trace forensics evaluation

Trace forensics is the third internal Juan-mode playbook. It analyzes an existing artifact, creates a queryable representation, attributes findings to source when symbols exist and returns the limits of the diagnosis. The other 20 procedures remain pending.

## Source and scope

[Complete comparison](source-comparison.json) covers the entire new playbook and mode entrypoint at `11713c683fe4add4fd403ea880580abbc9e0875f`, plus setup's entrypoint at its own `ccb5507cec1546dc88135c1139c811e6c59115ba` pin. The [adaptation record](../../adaptations/trace-forensics.md) accounts for each new difference. The original heading, six steps, SQLite normalization, source attribution, paired comparison and throughput line remain intact. Existing entrypoint differences retain their earlier assessments.

All existing mode/setup files except the three availability-bearing files match base `61d78c5f4b8fc91cc6aac0a528dd1f7fef664d5d`. Investigation and Prototype are unchanged. Licenses match their pins. The manifest adds Guard the Context Window as mode context while preserving the 41 mappings, watched roots, source pins, decisions and reviewed checkpoint.

## Fixed inputs

The [fixtures](fixtures/README.md) are constructed protocol-shaped data. No application ran to produce them. The mapped pair contains 5,000 samples per capture, shared frame identities and source text. The second file is gzip-compressed. A separate three-sample capture has no function name, source URL or valid source line. The source file is for attribution only. A caller-owned note tests preservation.

[Input hashes](inputs.json) bind the retained fixtures to the actual supplied files. The mapped evaluator receives only the pair, provenance, source and note. The unmapped evaluator receives only its capture, provenance and note, so it cannot borrow the source mapping or pair. Both write derived evidence in owned scratch directories.

## Execution and verification

[Paired execution](paired-evaluation.json) retains the original brief, verbatim steps, configured-role preflight, T3 dispatch and completion, parser/schema/query code, raw results, corrections, final diagnosis and writing process. The `judgment and prose` role resolves to inheritance on Codex `gpt-6-astra`. One parser child owns the bulk normalization; the coordinator receives reduced findings. The pair maps `normalize` to source line 9 and `lookupLabel` to line 13. Both have the same sample counts before and after, while the interval attribution is ambiguous as described below.

[Unmapped execution](unmapped-evaluation.json) retains the parser, schema, SQL, raw query results, exact final response, six-step record and writing audit. The parser creates SQLite before querying, preserves the raw JSON and ordered samples, and checks foreign keys and integrity. The response identifies node 2's missing symbols, states that no pair exists and leaves the source-level diagnosis incomplete. No source file is read or guessed in that exercise.

[Parent verification](parent-verification.json) checks fixture/configuration hashes, independently computes sample counts and timing conventions, and queries the actual unmapped database. It verifies raw JSON round-trip for the unmapped capture and ordered sample/delta preservation for all captures. For the pair it also checks every timestamp, tree edge and exact source URL/line, replays the base and sensitivity queries, and independently verifies corrected per-profile percentages. Scratch databases remain at `/tmp/jstack-trace-unmapped-20261016/profile.sqlite` and `/tmp/jstack-trace-pair-20261016/parser/profiles.sqlite`.

The raw execution records are archived as JSON text to preserve original prose, SQL and output without formatting edits. SQLite binaries remain in scratch. Archived scripts retain absolute fixture/output paths; extract them into a fresh owned directory and rebind those paths before replay elsewhere. The fixture source URLs also retain the original source path.

## Timing semantics and assisted assessment

The [DevTools protocol](https://github.com/ChromeDevTools/devtools-protocol/blob/master/json/js_protocol.json) defines `timeDeltas` as microseconds between adjacent sample timestamps, with the first relative to profile start. Its source line numbers are zero-based. Grouping each delta under the same-index node is an explicit attribution convention; it does not measure exact function CPU duration. The [DevTools CPU-profile model](https://github.com/ChromeDevTools/devtools-frontend/blob/main/front_end/models/cpu_profile/CPUProfileDataModel.ts) also uses sample counts and accumulated timestamps for different views.

The parent identified this distinction while the mapped parser was running and sent a clarification before its final diagnosis. This is an assisted evaluation, not evidence of an unassisted initial pass. Initial queries and the clarification are preserved. A first sensitivity query omitted `GROUP BY profile` in its denominator calculation. The corrected `sensitivity-v2.sql` is the accepted result; the original remains as failure evidence. Parent verification checks the corrected totals and per-profile percentages independently. The fixed input was not modified to obtain a preferred result.

The coordinator also accidentally printed the initial capabilities catalog and attempted one nonexistent manifest path before using file discovery. These are recorded execution misses. Bulk profile samples stayed in the parser child. Early parser reads and preflight calls were not included in its command log, and its first hashes were taken after those read-only steps. The parent input baseline precedes parsing; the parent also verifies all 150 final parser hashes. The parser could not find the upstream pin in the project Git database; the parent comparison uses the shared upstream cache and covers that separate authoring gate. The complete catalogs and fetched protocol remain in scratch; the archive keeps hashes and fetch/preflight evidence, rather than duplicating those large files.

| Before capture attribution | normalize, node 4 | lookupLabel, node 5 |
| --- | --- | --- |
| Sample count | 4,000 | 1,000 |
| Preceding delta grouped under current node | 400,000 microseconds | 1,000,000 microseconds |
| Interval following current sample | 1,300,000 microseconds | 99,900 microseconds |
| Count fraction multiplied by profile span | 1,120,000 microseconds | 280,000 microseconds |

The following-interval calculation leaves the initial 100 microseconds unattributed. There is no trailing interval beyond the final timestamp in these fixtures. Different conventions change the apparent hottest leaf, so the pair cannot establish a unique causal bottleneck. It establishes the encoded sample sequence and interval differences. Its total recorded deltas change from 1,400,000 to 500,000 microseconds while counts stay fixed. That is fixture arithmetic, not a measured improvement.

## Limits

This is explicit-authoring-path Codex execution, not installed discovery, cross-provider execution or conversation persistence. Synthetic CPU-profile parsing and source mapping do not validate heap retainers, spindump wait analysis, arbitrary trace formats, missing-parser recovery, malformed-input handling or real workload diagnosis. The inventory's real known-hot-path acceptance case remains open. No installation, model configuration, schedule, application execution or source modification occurs in the exercises. Bug fix and Perf issue remain unavailable routes.

Repository validation is recorded separately in [validation.json](validation.json). No runtime script changed, so unrelated resolver suites are not repeated. The upstream H3 fragment is linted through a byte-identical temporary copy with MD041 disabled.
