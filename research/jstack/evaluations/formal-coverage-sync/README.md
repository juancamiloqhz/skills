# Formal generator coverage and sync records

On 2026-10-25, three bounded authoring scenarios exercised the generator update. Generated-input tests caught real parser mutations and preserved an existing finding. A specifically required TLC run without Java/TLC remained a draft with no confirmed sync commit. No new formal proof or production verification is claimed.

## Source comparison

The complete final entrypoint was compared with `pstack/skills/create-formal-verification-skill/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`. All headings and seven quality requirements remain. The update adopts the TLA+ default for event-order questions, real-code generated-input fallback, files/functions coverage and last-confirmed correspondence commit. Tests are explicitly not a formal proof, and incomplete required checks cannot advance the sync commit.

The [adaptation record](../../adaptations/create-formal-verification-skill.md#tool-selection-and-sync-records-2026-10-25) accounts for the retained authority, portable destination, automatic Claude link and incomplete-result differences. Statechart result reading and the formal-maintenance command remain deliberately deferred, rather than introducing unshipped dependencies. The matching guide section was compared with `pstack/docs/guide/06-verify-and-ship.md` at the same revision. License bytes match `pstack/LICENSE`; original adoption pins and the reviewed checkpoint are unchanged.

## Live authoring and direct inspection

Two fresh T3-owned Codex `gpt-6.1-sol` consumers inherited `reasoningEffort: high` and `serviceTier: priority` after a live capability check. Dispatch receipts matched. A handled the valid parser; B separately handled the existing defect and missing TLC. Each read the full frozen skill and raw [requests/fixtures](cases.json), without expected answers. The supplied tool inventory was deliberately limited to Python 3 and Git. No machine-wide verifier discovery, installation, model changes, product fixes or publication was authorized.

| Scenario | Observed result |
| --- | --- |
| Valid parser | Generated tests executed actual `limits.py:parse_limit`, passed the baseline, detected five real-code mutations and passed after restoration. The skill names the covered function/contract, actual source commit and conditions for updating it. |
| Existing parser defect | Kept the three original findings for `0`, `00` and `000`. Widening the upper bound in a scratch copy added a `256` finding; restoration returned to exactly the original three. Sync confirms correspondence, not product correctness. |
| Missing TLC | Generated a labeled draft. Actual check and negative-control commands exited 2 before TLC execution. No mutation success, restored TLC pass or confirmed sync commit was claimed. Python graph export and the existing serial example test were explicitly not formal evidence. |

The parent read every complete handoff, generated skill, checker and negative-control procedure relevant to these outcomes. It independently replayed the valid parser through the retained package, reran the existing-finding negative control, invoked both blocked TLC commands and checked original fixture bytes, relative links and support-file resolution. All original product files remained unchanged. Both consumers were terminal `completed`, `result_available`, with no pending child work.

In the valid case each baseline executed 3,977,952 cases under Python 3.14.4. This counts executions, including overlapping groups, not distinct inputs. The deterministic generator includes 2,113,665 ASCII strings of length 0-3, 1,114,112 single Unicode code points, 729,000 non-ASCII decimal substitutions, decimal/boundary/type samples and 10,000 fixed-seed mixed strings. The five detected mutations widened the numeric bound, widened the length bound, removed the ASCII guard, changed the returned value and removed the type guard. This is finite generated-input testing, not correctness over every Python value or input length.

One generated documentation command used a symbolic commit placeholder despite the existing no-placeholder instruction. The parent replaced it with the already confirmed actual source commit before retaining and replaying the package. No checker behavior or shipped instruction was changed to conceal this authoring limitation. Live provider discovery and general generation reliability remain unverified.

Client request IDs were `jstack-formal-coverage-a-20261025-r1` and `jstack-formal-coverage-b-20261025-r1`, owned by conversation `5f7384b2-cbbe-431f-942d-929f327635a1`. Keep the concise report, case packet and one runnable generated [package patch](solution.patch) with its [replay](replay.py). These reproduce the actual valid-parser baseline/mutations and sync record; they are evaluation artifacts, not a new shipped skill. Do not retain duplicate generated packages, raw transcripts, catalogs, graph dumps or routine logs in Git.

## Replay and repository checks

From the repository root, choose a nonexistent disposable destination:

```bash
python3 -B research/jstack/evaluations/formal-coverage-sync/replay.py /tmp/jstack-formal-replay
```

The replay creates the case packet's parser repository, applies the retained package, runs its five real-code negative controls and restoration through the Claude link, checks original bytes and cleanup, then records the new fixture's source commit only after confirmation. It leaves the repository for inspection. Remove that owned directory when finished. It needs Python 3 and Git, without installing anything. Exact generated-input counts can depend on Python's Unicode version. The existing-finding and missing-TLC authoring scenarios can be repeated separately from `cases.json`; the latter reuses the adjacent historical lease fixture generator. Do not supply the result table or expected findings to a fresh consumer.

Packaging passed 4 tests, documentation passed 20, current docs reported 0 problems, and manifest schema/applied ancestry passed. The retained upstream frontmatter and explicit-invocation metadata are unchanged and parsed successfully. The generic Codex `quick_validate.py` still rejects `disable-model-invocation` as an unknown key, as it did at original adoption. That validator is not reported as passing, and the source flag was preserved.

The formal generator's runtime-independent coverage and fallback behavior were exercised here. Executed TLC semantics, the draft model/exporter, Statechart, formal maintenance, live skill registration and cross-provider reliability remain outside the result. Missing proof prerequisites remain incomplete. The older finite-state lease evaluation remains historical and is not reclassified as a new TLA+ run.
