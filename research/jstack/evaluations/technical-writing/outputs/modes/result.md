# Writing evaluation result

Completed four standalone documents from the supplied fixture files.

| Document | Mode | Reason |
| --- | --- | --- |
| [first-note.md](first-note.md) | Tutorial | A newcomer creates and retrieves one note, with visible expected output. |
| [retrieve-note.md](retrieve-note.md) | How-to | An experienced user retrieves a note with a known ID and data directory. |
| [command-reference.md](command-reference.md) | Reference | Commands, options, data, output, and errors are available for lookup. |
| [explicit-data-directories.md](explicit-data-directories.md) | Explanation | Explains the maintainer's reason for explicit stores and the resulting trade-off. |

## Skills and sources

The resolved writing skill is `jstack-technical-writing` at `/home/ubuntu/Dev/skills/skills/jstack/jstack-technical-writing/SKILL.md`.
The resolved dependency is `unslop` at `/home/ubuntu/.agents/skills/unslop/SKILL.md`, the supplied authoring path for the cursor/plugins dependency.
Both files were read in full. The dependency has `disable-model-invocation: true`; this task explicitly supplied and requested that dependency. No substitute package was used or installed.

The factual sources are `pocket.py`, `draft.md`, and `context.md` in `/home/ubuntu/Dev/skills/research/jstack/evaluations/technical-writing/fixtures/`.
The context supplies runtime requirements, maintainer intent, concurrency limits, and formatting conventions. Source code supplies command behavior. JSON examples use two spaces when multiline. No Python examples were needed in the documents.

The upstream-fidelity policy at `/home/ubuntu/Dev/skills/research/jstack/upstream-fidelity.md` was read before work. This task creates fixture documentation only. No jstack skill or other repository file changed, so there is no final jstack change to compare with the upstream pin and no adaptation deviation to record.

## Verification

The supplied CLI was copied to [pocket.py](pocket.py). All CLI runs used this output directory as their working directory. Every data directory used by a CLI run is inside this output directory.

[command-evidence.json](command-evidence.json) contains the complete arguments, working directory, exit code, standard output, and standard error for every CLI invocation. Expected failure cases are intentional checks.

The checks confirmed title trimming, ID allocation, the default body, preservation of body whitespace, retrieval, listing, an absent store, help, version output, argument errors, a missing note, invalid JSON, an incompatible note, and a filesystem error. The stored JSON was also inspected for indentation and field values. The documented tutorial output matches its first creation and retrieval runs.

The following commands were exercised:

| Command | Exit code |
| --- | --- |
| `python3 pocket.py --help` | 0 |
| `python3 pocket.py --version` | 0 |
| `python3 pocket.py --data-dir first-note-data add --title '  Travel  ' --body Passport` | 0 |
| `python3 pocket.py --data-dir first-note-data show 1` | 0 |
| `python3 pocket.py --data-dir first-note-data add --title Packing` | 0 |
| `python3 pocket.py --data-dir first-note-data list` | 0 |
| `python3 pocket.py --data-dir empty-store list` | 0 |
| `python3 pocket.py --data-dir first-note-data add --help` | 0 |
| `python3 pocket.py --data-dir first-note-data show --help` | 0 |
| `python3 pocket.py --data-dir first-note-data list --help` | 0 |
| `python3 pocket.py list` | 2 |
| `python3 pocket.py --data-dir first-note-data` | 2 |
| `python3 pocket.py --data-dir first-note-data add` | 2 |
| `python3 pocket.py --data-dir first-note-data add --title '   '` | 2 |
| `python3 pocket.py --data-dir first-note-data show` | 2 |
| `python3 pocket.py --data-dir first-note-data show abc` | 2 |
| `python3 pocket.py --data-dir first-note-data show 99` | 2 |
| `python3 pocket.py --data-dir first-note-data delete` | 2 |
| `python3 pocket.py --data-dir first-note-data list --unknown` | 2 |
| `python3 pocket.py list --data-dir first-note-data` | 2 |
| `python3 pocket.py --data-dir invalid-json list` | 1 |
| `python3 pocket.py --data-dir blocked-path add --title Test` | 1 |
| `python3 pocket.py -h` | 0 |
| `python3 pocket.py --data-dir first-note-data add --title` | 2 |
| `python3 pocket.py --data-dir body-check add --title Body --body '  kept  '` | 0 |
| `python3 pocket.py --data-dir incompatible-data show 1` | 1 |

## Limits and prerequisites

No missing prerequisite blocked this exercise. Python 3 was available. Documentation requires the supplied `pocket.py` in the working directory. The tutorial requires a fresh data directory, so reruns need a new name. The verification directory now contains two notes from the checks and is not fresh.

Parent-directory creation and the absence of writes during `show` and `list` were checked in source rather than through separate filesystem assertions. Concurrent writing was not tested. Its unsupported status comes from the maintainer context. Maintainer intent and the lack of measured performance comparisons also come from that context. The explanation's comparison with an implicit shared directory is design reasoning, not a measured result. No unsupported product claim remains in the documents.

The draft's future deletion promise, server claims, performance claim, title-preservation claim, fixed-ID claim, and backup-removal instruction were removed. No user data outside this output directory was touched. Nothing was published or installed.

## Proposed Unslop addition

The draft uses "coordination membrane" for the JSON file. This proposal adds a concrete replacement to rule 26. The installed skill was not edited.

```diff
--- unslop/SKILL.md
+++ unslop/SKILL.md
@@
+"Coordination membrane" becomes the actual file or mechanism, such as "JSON file".
```
