# Explicit data directories

Why does every Pocket note command require `--data-dir`?

The maintainer chose explicit directories so examples and automated checks can use independent stores. Each directory contains its own `notes.json` file. A note ID identifies a note within that store.

An implicit shared directory would save an argument, but examples and checks could affect the same notes. Explicit directories make the caller choose the store on every command. That choice also creates a possible mistake: a valid ID can retrieve a different note when the caller selects a different store.

Separate directories fit this small local fixture. Pocket reads and rewrites a JSON file, and concurrent writers to one store are unsupported. An explicit path does not add concurrency protection or turn Pocket into a service.

The trade-off favors independent stores over shorter commands. This is a choice about data separation, with no measured performance comparison behind it.
