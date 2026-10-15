# Setup restoration

This correction follows merged PR #34 at `3220da45879b202dec4430a01db2460ad7f53ea5`. Setup retains its primary pin `ccb5507cec1546dc88135c1139c811e6c59115ba`. It restores pstack's seven numbered steps, lettered budget/map substeps, exact four budget labels and inline 17-role example. The three candidate panels now default to two inherited seats for new unseeded files. Existing files and global seeds retain their counts. Whole-configuration validation remains unchanged by explicit user choice.

## Source comparison

[compare.py](compare.py) compares the complete entrypoint with the exact source, checks the package license, verifies the inline JSON against the executable template and inventories the six local support files. [source-comparison.json](source-comparison.json) retains hashes and the full unified diff. The parent inspected the complete pinned source and final instructions; the [adaptation record](../../adaptations/setup-jstack.md) accounts for each remaining difference by step. The shared investigation reference retains its distinct Why source pin.

```sh
python3 -B research/jstack/evaluations/setup-restoration/compare.py > /tmp/setup-source.json
cmp research/jstack/evaluations/setup-restoration/source-comparison.json /tmp/setup-source.json
python3 -B skills/jstack/setup-jstack/scripts/test_models.py
python3 -B skills/jstack/juan-mode/scripts/test_preflight.py
```

The manifest adds the verification generator as step 7's watched dependency. Component pins, reviewed checkpoint and prior review decisions stay unchanged. Arena and Swarm remain the next fidelity corrections; all 23 Juan-mode playbook procedures remain pending.

## Isolated setup exercises

Two fresh native children inherited Codex gpt-6-astra and the parent's effort after current T3 capability discovery. They received the actual source skill and a notes-only fixture, with write permission restricted to their own temporary directory. They received no expected answers, prior conclusions or other evaluation results. Neither was allowed nested delegation, real settings changes, installation, PR operations or schedule changes. Each helper subprocess used an explicit fixture `XDG_CONFIG_HOME` and empty `JSTACK_CONFIG`; neither changed HOME or CODEX_HOME.

| Child | Supplied request | Observed result |
| --- | --- | --- |
| `/root/setup_fresh_eval` | Save global defaults for the notes project, medium budget, every role inherited, default panel sizes. | Saved all 17 roles, two inherited seats in each candidate panel and one cross-judge alternative; effective lookup selected global. |
| `/root/setup_seed_eval` | Create a project file using global defaults, retaining the recorded budget and all assignments. | Saved a byte-identical copy of the older one-seat global file with its `small` budget; effective lookup selected project; global seed unchanged. |

Both children captured the complete live capabilities payload, validated and saved through the helper, reread the result and skipped verification generation because the fixture has no executable product. Explicit setup choices allowed them to proceed without redundant questions. The seed evaluator reported that one-seat Arena and Architect panels remain insufficient for comparison.

[Fresh report](fresh-result.md) and [seed report](seed-result.md) retain agent-reported actions and limits. [Fresh saved file](fresh-models.json) and [seed saved file](seed-models.json) retain the actual outputs. The parent independently checked the files, equality with the untouched original seed, current-catalog validation, lookup selection and panel resolution; [parent-checks.json](parent-checks.json) records the results and hashes. Temporary catalog/draft files were removed. The notes fixtures remain under `/tmp/jstack-setup-eval-20261015/`; durable evidence is in this directory.

## Checks and limits

The setup suite passes 16 tests, including all three new panel defaults, independent seat edits, preservation of one-seat project seeds and unrelated stale-role blocking. The 15 preflight tests and 11 upstream-checker tests pass. Skill validation, Markdown lint and manifest validation pass. The source comparison also confirms the unchanged MIT license and exact inline-template match. The actual user model file retains SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`.

These exercises establish bounded setup behavior, not successful execution of configured provider seats. They do not test live concrete budget remapping, catalog-unavailable fallback, unanswered questions, generator acceptance/failure, installed-provider discovery or persistence across provider restart. Two inherited candidates establish count, not model-family diversity. No existing user configuration was migrated, and no installation or schedule changed.
