# Batch event summary

Run `node cli.cjs ../events.json ../rules.json` to summarize a batch using its rules.
The CLI reads files, parses all events and prints totals plus processed, accepted and rejected counts. Its CommonJS `summarize` function is also public. Run tests with `node --test summary.test.cjs`.

This is a deterministic synthetic batch of 80,000 events in 67 categories, with rules for 64 categories. It represents a single-process batch import, not an HTTP or concurrent workload. All events must be accounted for. Keep the CLI, data format, empty-batch behavior and error behavior compatible. No third-party dependencies or production services are involved.
