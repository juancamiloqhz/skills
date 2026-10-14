# Pocket skill reuse result

The existing `verify-pocket` skill worked on the fresh checkout at `/tmp/jstack-verification-restoration/reuse`. The helper exited 0, its summary reports `passed: true`, and independent inspection confirmed that the recorded scratch directory is absent while all four evidence files survive. No application or skill changes were needed.

I read the installed skill, its feature map and recipes, its executable helper, and the fixture README. I did not open prior generation evidence or reports. The skill's feature map contains a prior-run claim, which I did not use as proof. I used new evidence under the requested reuse directory.

## Commands executed

From `/tmp/jstack-verification-restoration/reuse`:

```sh
python3 pocket.py --version
.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/reuse-evidence
```

The doctor returned exactly `Pocket 1.0` with a newline and exited 0. The helper printed:

```text
Evidence: /tmp/jstack-verification-restoration/reuse-evidence/pocket-90jmlh11
PASS: add, show, list; evidence retained; scratch removed
```

The helper ran `/usr/bin/python3 /tmp/jstack-verification-restoration/reuse/pocket.py` for every subprocess. It supplied `--data-dir /tmp/jstack-verification-restoration/reuse/.pocket-verify-afomf9w0/data` for all commands except `--version`.

| Command arguments after the data directory | Exit | Observed result |
| --- | --- | --- |
| `--version`, without a data directory | 0 | `Pocket 1.0` |
| `list` | 0 | `[]`; the helper asserted no data directory was created |
| `add --title '  Packing list  ' --body 'Passport and charger'` | 0 | ID 1, trimmed title, supplied body |
| `show 1` | 0 | The persisted first note |
| `list` | 0 | Exactly the first note |
| `add --title '   '` | 2 | `title must not be blank` |
| `show 999` | 2 | `note not found` |
| `add --title 'Groceries'` | 0 | ID 2 and an empty body |
| `show 2` | 0 | The persisted second note |
| `list` | 0 | Both notes in insertion order |

The helper checked persisted JSON after each successful add and compared storage bytes around the first reads and rejected commands. I inspected every retained command record, the identity, summary, and final notes snapshot using a Python script. That inspection also asserted the summary was true, the scratch path was absent, there were ten command records, all four required artifact files existed, no failure file existed, the recorded checkout was the fresh reuse checkout, and both recorded source hashes still matched. It exited 0.

## Surviving evidence and cleanup

Evidence directory: `/tmp/jstack-verification-restoration/reuse-evidence/pocket-90jmlh11`.

- `identity.json` records the actual reuse checkout, Python 3.14.4 at `/usr/bin/python3`, and SHA-256 hashes for `pocket.py` and `README.md`.
- `commands.jsonl` retains all ten actual argv arrays, stdout, stderr, feature IDs, and exit codes.
- `notes.json` contains ID 1 with title `Packing list` and body `Passport and charger`, followed by ID 2 with title `Groceries` and an empty body.
- `summary.json` reports success and completed cleanup.

The helper removed its owned scratch directory `/tmp/jstack-verification-restoration/reuse/.pocket-verify-afomf9w0`. Independent inspection found no `.pocket-verify-*` directories remaining in this checkout. The helper ran subprocesses synchronously and completed before cleanup; no persistent application service was launched. Evidence remains outside scratch. No installs, network requests, commits, settings changes, or app/skill repairs were performed.

## Limits and observations

No blocking reuse problem occurred. The recipes show the generation evidence directory in their example commands; SKILL.md explicitly allows choosing another authorized directory, so I passed the requested reuse directory without editing anything.

This result covers the documented add, show, and list paths. It does not establish behavior for corrupt stored data, other argument-parser errors, concurrent writes, process timeouts, forced termination, or cleanup after a failed run. Those paths were not exercised. The reusable helper passed as installed; the prior generation success claim was unnecessary to this result.
