# Architect implementation and checkpoint evaluation

Executed against revision `17c11694c6f41033635d1b76a404cb4dfb27d0ed` using explicit authoring paths. Raw artifacts remain in `/tmp/jstack-architect-runtime-p8f02zdw`. Two independent coordinators received the same greenfield reservation-library request, with different implementation authority. Temporary settings supplied two inherited architect seats and one inherited judge; the ordinary Arena panel remained one seat. Real user settings were unchanged.

## Observed boundaries

| Request | Observed result | Evidence |
| --- | --- | --- |
| Architect and implement, no checkpoint | Two candidates and one judge completed, then the coordinator wrote working source and ran tests without asking for redundant approval. | [Implementation record](implementation.json) |
| Architect with explicit checkpoint | Two candidates and one judge completed, then the coordinator returned a design awaiting sign-off. The project still contained only its unchanged user-owned file. | [Checkpoint record](checkpoint.json) |

Both comparisons explored the requested single booking ledger and resource-owned booking structures. Both selected the ledger. Candidate ID-lifetime assumptions differed and were disclosed; the selected design uses a module-lifetime allocator. These are directed structural comparisons, not evidence of spontaneous diversity. All six nested candidate/judge tasks completed without pending children. Design verification was static; only the authorized implementation case executed product tests.

The generated implementation passed its six tests, including a seeded 2,000-operation discrete-cell oracle. The parent inspected the source and independently ran six public-contract tests prepared before seeing that source. They cover half-open overlaps, adjacent and separate-resource reservations, cancellation, ID nonreuse, invalid-operation preservation, nonmutating queries and independent books. Source, selected-config, candidate and protected-file hashes were checked. The parent also verified the real global configuration hash.

## Reproduce product checks

The retained [fixture](fixture/reservations.py) is evaluation output, not a shipped jstack library. Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 research/jstack/evaluations/architect/runtime/verify_reservations.py research/jstack/evaluations/architect/runtime/fixture
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s research/jstack/evaluations/architect/runtime/fixture -p 'test_*.py' -v
```

These commands replay product behavior. They do not rerun the agent workflow. The JSON records retain exact briefs, resolutions, task receipts, designs, judging and final responses for that assessment.

## Deviations and remaining limits

The implementation run recorded its private rubric after inspecting the first candidate instead of during framing. That may bias coordinator scoring and prevents calling the entire run a clean procedural pass. It also attempted an oversized catalog heredoc despite existing guidance, recovered using a file tool, and corrected a rejected duplicate-path patch. These failures remain in the evidence; successful output does not erase them. No skill instruction was changed in this evaluation PR.

The evaluator's final whole-repository cleanliness check observed the parent's newly saved checkpoint evidence. Assigned source-file hashes remained unchanged; that observation was not a child source edit. Both runs preserved their user-owned file. Filesystem checks and recorded task scope are not an exhaustive operating-system audit.

All children inherited Codex `gpt-6-astra`. Other providers, installed discovery, checkpoint continuation after approval, architecture reconsideration and persistence across compaction or restart remain untested. These tests establish the two requested execution boundaries on this fixture, not complete coverage of Architect or the 23 planned playbooks.
