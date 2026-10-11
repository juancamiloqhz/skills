# Project model configuration evaluation

Evaluated on 2026-10-11 against the change based on `b14ebc42ae1b119346c2bb169bb0a65743af36d2`. This adds optional project configuration to the existing setup and juan-mode foundation. [Results](results.json) identify source hashes and observed coverage. The earlier [foundation evaluation](../juan-mode-foundation/README.md) remains a historical record of its original source revision.

## Executed behavior

The setup/resolver suite has 14 passing tests and the consumer suite has 15. Eleven new tests cover project lookup and scope; the prior 18 continue to pass.

- Exact file precedence: explicit path, environment selection, project file, then XDG global defaults. Missing explicit or environment paths stay selected and fail at resolution.
- Git root discovery from nested directories and linked worktrees, paths with spaces, explicit project roots outside Git and global fallback outside a checkout.
- Paths containing a symlink followed by `..` preserve filesystem traversal semantics for explicit configuration, environment selection and explicit project roots.
- Complete-file replacement without role merging. Malformed JSON, duplicate fields, incomplete schemas, directory entries and dangling project symlinks cannot silently select global settings.
- Read-only scope selection for setup, including a project path that does not exist yet. Explicit scope queries ignore unrelated environment overrides.
- A temporary project draft seeded from all 17 global roles, a changed assignment saved through the real `write` command, and byte-for-byte preservation of the global file. A later global save also preserves project settings.
- The consumer and canonical locator agree on the selected project file. Explicit and environment overrides retain their precedence through the consumer CLI.
- An absolute parent-selected configuration remains selected in a child worktree, including when the child has a different or invalid project file. The file is read again on each invocation.

The scope and write cases run in disposable fixtures. They do not configure this repository or alter the user's saved model assignments. Worktree tests create a real local Git repository and linked checkout, with fixture cleanup after each test.

An independent review found that lexical path normalization could select a different valid file when a symlink preceded `..`. The regression test failed against the original implementation. Making paths absolute without collapsing `..` fixed the selection, and the regression passes alongside the full suite.

## Live read-only compatibility check

The parent obtained a fresh T3 Code catalog and ran the new consumer against the currently installed setup-jstack. That installation predates shared lookup, so the consumer returned a CLI compatibility error with manual-update guidance. No installation was changed.

Against the new setup source, the same consumer selected `/home/ubuntu/.config/jstack/models.json` with `configSource: global`, returned `[null]` for `how explorer`, and identified the inherited `codex` / `gpt-6-astra` selection. The saved configuration's hash was unchanged, and no `.jstack` directory was created in this repository. Raw local evidence is under `/tmp/jstack-project-config-20261011` and may expire.

## Repeat

```sh
python3 -B -m unittest discover -s skills/jstack/setup-jstack/scripts -p 'test_*.py' -v
python3 -B -m unittest discover -s skills/jstack/juan-mode/scripts -p 'test_*.py' -v
npx --yes markdownlint-cli2 'skills/jstack/setup-jstack/**/*.md' 'skills/jstack/juan-mode/**/*.md'
```

## Limits

The setup scope conversation is documented and the underlying CLI sequence is executed in fixtures; this is not an independent end-to-end setup conversation on every provider. Worktree handoff is verified through actual CLI invocations in separate checkouts, without launching a new paid-model task. The earlier foundation's compaction, restart, cross-provider execution and playbook implementation gaps remain unchanged. Users update both skills manually after the change lands.
