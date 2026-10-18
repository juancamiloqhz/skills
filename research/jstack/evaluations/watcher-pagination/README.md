# Watcher pagination and owner-approval checks

The bundled GitHub watcher now reads all review-thread pages before reporting readiness. It counts distinct Bugbot passes across the complete read, including resolved threads, and then reports unresolved findings. A named `Code Review Gate` awaiting owner approval reports as that gate on both check-reading paths, rather than as failed CI. This classification does not authorize a merge or satisfy human approval.

Base: merged coverage audit, `48f24827ffad99da38f8171db66ce187075b4f57`. This implements the first proposed fix from the [coverage audit](../../coverage-audits/2026-10-18/README.md). The rest of that inventory remains proposed work.

## Source comparison

Adopted source: [`pstack/skills/poteto-mode/scripts/watch-pr/` at `0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/poteto-mode/scripts/watch-pr). Local files are under `skills/jstack/jstack-juan-mode/scripts/watch-pr/`. The change starts with the six-file upstream delta from the original mode pin, `11713c683fe4add4fd403ea880580abbc9e0875f`.

| File | Final comparison with the adopted source |
| --- | --- |
| `github.ts` | Same pagination query, page parser, aggregation, owner-gate mapping and reader interface. Two narrow error checks additionally reject a promised next page without a cursor and any repeated cursor. Upstream otherwise treats the missing cursor as completion or can loop on repetition. Existing T3 single-pass errors require incomplete reads to return a query blocker. |
| `types.ts`, `policy.ts` | Same new raw-thread/page types and snapshot aggregation call. The only other differences are the existing T3 single-pass waiting return and immediate query-error behavior documented in the [Babysit adaptation](../../adaptations/babysit.md). |
| `fakes.test-helper.ts`, `policy.test.ts` | Identical to the adopted source. |
| `github.test.ts` | All adopted source tests retained, plus missing/null/empty-cursor and cyclic-cursor rejection cases. |

The operational Babysit qualification now describes the complete thread read and separate owner gate. Its other procedure steps, T3 watch ownership, priority order, manual dependency policy and merge authority are preserved. The existing executable fixture gained raw paginated responses and owner-gate cases; it runs the real packaged command against a temporary local `gh` response program.

This is a partial mode update. The whole-package `adaptedFrom` pin and reviewed upstream checkpoint remain unchanged because the other mode changes have not been adopted. The exact source revision and six-file adoption are recorded here rather than advancing the whole package prematurely. Notices and dependency versions are unchanged.

## Executed verification

On 2026-10-18, Linux x64, Bun 1.4.2 and cached Commander 14.0.0:

- Before the production change, the expanded executable fixture passed its five existing cases, then failed the new 120-thread case: the old reader returned exit 0 and `READY` despite unresolved thread 110.
- After the change, all 58 watcher unit tests passed. These retain the previous 48 tests, add eight upstream cases and add two local cursor-validation cases.
- All 14 executable scenarios passed. Thread 110 now produces exit 3 and a review-thread blocker with three distinct Bugbot passes, including a resolved pass on the later page. Resolved-only pages permit the existing ready classification. A later command failure, missing cursor or repeated cursor produces one status-query blocker, exit 7, within the five-second fixture deadline.
- Both the direct check path and GraphQL fallback classify owner-approval `ACTION_REQUIRED` separately. An unrelated `ACTION_REQUIRED` check and an actual `FAILURE` on the owner gate still produce a CI blocker, exit 4. Pending, conflict, hidden CI refusal, empty checks and status-only behavior retain their prior results.
- Strict watcher type checking passed with cached TypeScript 6.0.3, bun-types 1.4.2 and Node types 24.13.6. The first attempt lacked the cached Node type definitions; linking that prerequisite fixed the environment without source/config changes. The full lockfile development environment was not installed or verified.
- An authenticated read through the new reader and parser succeeded against merged PR #80 and returned zero unresolved threads. It verifies the live query shape, not live multi-page behavior. Four packaging tests, 124 local Markdown link paths and `git diff --check` passed.

Reproduce with the declared dependencies already available:

```sh
bun test skills/jstack/jstack-juan-mode/scripts/watch-pr
python3 -B research/jstack/evaluations/babysit/exercise.py
cd skills/jstack/jstack-juan-mode/scripts
./node_modules/.bin/tsc --project watch-pr/tsconfig.json --noEmit --strict
```

Temporary links reused existing cached dependency files during evaluation; no package installation or lifecycle script ran. The links are removed before handoff. The user still installs dependencies and skills manually. Only the tests, the expanded existing fixture and this report are retained; raw source diffs remain in task cache.

## Remaining limits

These are local tests using controlled GitHub responses, not a live 120-thread PR or an unattended T3 watch/wake evaluation. The first comment still owns thread classification. Commit history and stack-discovery caps remain, and the existing check-rollup pagination was not changed. A paginated read is not an atomic forge snapshot; current head/base and actual merge authority still need checking before delivery actions. Saved model configuration, installations and schedules were not changed.
