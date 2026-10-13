# Custom workflow evaluation

Two independent T3-owned evaluations exercised Figure it out on 2026-10-13 using separate copies of a small JSON inventory CLI. The requested addition was CSV output preserving string IDs and names containing commas and quotes. Both coordinator tasks completed; the execution task's separate trail reviewer also completed with no pending child work.

## Planning-only result

The planning agent inspected source and captured actual default JSON output, then returned hypotheses, owned paths, prerequisites, observable checks, recovery actions, estimates and explicit assumptions. It stopped without implementing CSV or delegating work. The parent checked the original script, input and user-notes hashes: all matched. Proposed implementation checks are not execution evidence. [Planning results](planning-results.json) retain the plan, report, baseline and hashes.

## Execution result

The execution agent captured the failing CSV baseline, implemented the standard-library option and passed seven checks across six CLI invocations: default JSON values, byte-identical default JSON, explicit JSON, CSV field round-trip, invalid format, empty header, and newline/Unicode/quote/comma data. The parent independently reran default JSON and CSV, checking original JSON bytes and exact ordered CSV fields. Input, user notes and real configuration were preserved. All final source/config/fixture hashes matched the saved final manifest.

One separate trail reviewer used the canonical `judgment and prose` role from a copied explicit configuration, resolving to inheritance. The receipt reports Codex `gpt-6-astra`, the same model as the coordinator. No model diversity is claimed. The reviewer inspected actual artifacts without rerunning the CLI and returned four flags; the coordinator retained them and recorded its disposition. [Execution results](execution-results.json) include code, verifier, raw output, trail, review, terminal receipt and hashes.

## Process failure and source drift

A preservation assertion failed, but the evaluator's shell continued and appended false preservation and audit success claims. The evaluator added correction rows identifying the superseded timestamps; the reviewer flagged the original error. This is a completed workflow with a recorded process failure, not a clean procedural pass. The current instructions already require evidence-backed results and append-only corrections; this run does not justify adding duplicate prose.

Both agents detected a change to the tested decision-trail reference during evaluation. The parent had added two Markdown lint comments around the literal TSV header. Removing exactly those comments reproduces the recorded initial SHA-256, establishing that the instruction text was unchanged. The preserved evaluator reports correctly lacked that attribution at their own handoffs. Their source-stability flags remain in the raw evidence; the parent's narrower explanation does not make the earlier false claims correct.

## Limits and retained evidence

These are two bounded cases, not a baseline comparison or broad reliability benchmark. Review relied on a labeled digest and artifacts rather than a complete archived tool transcript. Recovery, consequential architecture choices, invalid configuration, cross-provider selection, delegated implementation and later review rounds remain untested. The CSV fixture has a fixed schema; malformed input, other schemas, large data and Windows behavior are untested.

The raw directories remain at `/tmp/jstack-custom-plan-6galxeq4/planning` and `/tmp/jstack-custom-plan-6galxeq4/execution`. Saved JSON embeds text artifacts so the main evidence remains readable after those temporary paths expire. The execution capability catalog was removed after review; its hash and resolution receipt remain. No installation or real configuration change occurred.
