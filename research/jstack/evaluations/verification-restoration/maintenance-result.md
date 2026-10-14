# Ledger verification maintenance result

Outcome: **changed**. Proven verifier corrections remain locally in the canonical `.agents/skills/verify-ledger` directory. Nothing was committed, pushed, published, installed, or changed in product code or model settings. All three mapped features received fresh source review and live coverage. A product read regression remains visible; successful licensed export remains unreachable.

## Feature results

| Feature | Source result | Live result | Evidence |
| --- | --- | --- | --- |
| Create | README's accepted migration changes `add` to `create`; storage remains verbatim. | Passed. Public `create --body 'Case Sensitive'` returned exact JSON and persisted exact body. | [create.json](maintenance-evidence/create.json) |
| Read | README and feature map require verbatim reads; `ledger.py:19` applies `.upper()`. | Failed product contract. Public `get` returned `CASE SENSITIVE` with exit 0; verifier correctly exited 1. The assertion was preserved. | [read.json](maintenance-evidence/read.json) |
| Export | README requires licensed-export entitlement, unavailable in this fixture; source rejects before data access. | `verified-unreachable`. Public export exited 3 with exact entitlement error, empty stderr, and no target directory created. This is prerequisite proof, not successful export. | [export.json](maintenance-evidence/export.json) |

The initial doctor failed because it expected `ledger 1`, while the public identity was `ledger 2`. After the correction, its single retry passed. Doctor also passed before each fresh feature session and after the failed read. The helper uses isolated short-lived subprocess sessions; no server or shared process was launched. The final shared helper was exercised by all three features after source refresh. See [initial doctor](maintenance-evidence/doctor-initial.json), [doctor retry](maintenance-evidence/doctor-retry.json), and [ordered live sequence](maintenance-evidence/live-sequence.json).

## Corrections and proof

- `SKILL.md`: expect `ledger 2`; document export's missing entitlement, explicit `verified-unreachable` outcome, and helper exit semantics. Keep the read assertion verbatim.
- `features/create.md`: replace obsolete `add` with documented `create`.
- `features/export.md`: explain the entitlement prerequisite and rejection verification route without promising successful export in this fixture.
- `scripts/drive.py`: use `ledger 2` and `create`; validate export exit 3, exact error JSON, empty stderr, and no data creation; retain an explicit unreachable outcome and prerequisite.

README.md:5 and its accepted migration at line 9 establish intent for these corrections. Source behavior alone was not used to weaken the read contract. The final changes were re-read and compared against the saved original verification package; [verifier.diff](maintenance-evidence/verifier.diff) contains the complete patch. No jstack authoring files were edited, so there is no jstack upstream adaptation delta from this task.

The feature index has exactly create, read, and export, with no duplicate, missing, or dead links. The `.claude/skills/verify-ledger` symlink resolves to the canonical directory and remains intact. This exported fixture has no Git metadata/history; README's accepted migration is the supplied change range. The parser's create/get/export commands all map to existing feature files. See [index and history](maintenance-evidence/index-and-history.json).

## Source wave and configuration

The explicit setup-jstack authoring dependency and maintenance execution reference were read. A fresh full unwrapped capability catalog was captured and used to validate the whole existing map. `/home/ubuntu/.config/jstack/models.json` selected `how explorer` as `inherit-parent`; native fresh-context readers used no model/effort override. The inherited catalog identity was `codex` / `gpt-6-astra`, with child-task support. The absolute selected configuration path was retained and subsequently resolved explicitly. Settings remained unchanged.

Every source reader returned all required sections and reached terminal completion before its corresponding live phase. Each edited input was reviewed again in a fresh task. Readers only read source/docs, never drove or wrote. Full briefs and terminal finding content are retained in `maintenance-evidence/*-brief.txt` and `*-result.md`.

| Native task ID | Status | Retained findings |
| --- | --- | --- |
| `/root/verification_maintenance_eval/ledger_create_source` | completed | [create source](maintenance-evidence/create-source-result.md) |
| `/root/verification_maintenance_eval/ledger_read_source` | completed | [read source](maintenance-evidence/read-source-result.md) |
| `/root/verification_maintenance_eval/ledger_export_source` | completed | [export source](maintenance-evidence/export-source-result.md) |
| `/root/verification_maintenance_eval/ledger_create_refresh` | completed | [create refresh](maintenance-evidence/create-refresh-result.md) |
| `/root/verification_maintenance_eval/ledger_read_refresh` | completed | [read refresh](maintenance-evidence/read-refresh-result.md) |
| `/root/verification_maintenance_eval/ledger_export_refresh` | completed | [export refresh](maintenance-evidence/export-refresh-result.md) |

Actual four-agent capacity was respected. Initial create ran alone; read/export overlapped once a slot opened. Refresh readers queued serially while another authorized evaluator occupied a slot. One read-refresh spawn was rejected at capacity before creating a task, then retried as a fresh task after a reader completed. None were dropped or substituted with coordinator-only review. Observed lifecycle notes are in [reader events](maintenance-evidence/reader-events.jsonl).

## Cleanup and limitations

All eight doctor/feature evidence files were checked at their named paths after cleanup. Every recorded owned data directory is absent. The empty owned runtime directory and temporary capability capture were removed. The executable helper remains executable. Source and README SHA-256 values match their initial values; the model-configuration hash is unchanged. Original verifier snapshots, hashes, briefs, terminal findings, diff, and transcripts remain as evidence. See [cleanup and routing checks](maintenance-evidence/routing-and-cleanup.json), [initial hashes](maintenance-evidence/initial-hashes.json), and [final hashes](maintenance-evidence/final-hashes.json).

The read defect is not repaired because product edits were forbidden. Successful export cannot be tested without an unavailable entitlement; none was changed or bypassed. The live pass covered the three feature-map claims with mixed-case text, not exhaustive CLI argument validation, overwrite behavior, Unicode/empty-body variants, or missing-note reads. No claim of those untested sub-features is made. This is a changed verifier outcome with a documented product failure and evidenced unreachable feature, not a clean product bill of health.
