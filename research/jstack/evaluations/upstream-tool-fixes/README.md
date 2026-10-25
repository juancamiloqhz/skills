# Upstream watcher and plan fixes

Implements the user-selected `watcher-fork-identity`, `watcher-deadline` and `plan-inline-code` recommendations from the [2026-10-25 review](../../upstream-reviews/2026-10-25.md). Baseline is canonical main `6a954013104bba70bcf4cdd2797f46cd9e034c27`. The saved complete review and ledger are published with this implementation; their other recommendations remain pending.

## Behavior

- The watcher validates GitHub's `isCrossRepository` flag. A fork head cannot stand in for a same-named branch in the base repository, and a fork target cannot acquire local children just because their branch names match. An unrelated fork from `main` to `main` no longer hangs stack discovery. Missing or malformed fork identity makes the read incomplete.
- Internal polling and retry sleeps stop at the remaining deadline. A five-second timeout with a 60-second interval sleeps five seconds. This does not bound an in-flight GitHub request. The bundled T3 command still adds `--once`, so it performs no polling sleep and leaves subsequent wakes to the host.
- The plan checker strips matching multi-backtick inline code spans before checking prose punctuation. Nested literal backticks no longer expose code punctuation as prose. Unmatched delimiters and punctuation outside the span remain checked. Existing fence and plan structure rules remain.

Example after merging and manually updating skills: ask `/jstack-juan-mode check whether PR #123 and its connected stack are ready.` An unrelated fork named `main` must not hang that check or become one of its stack parents. A watcher `READY` classification still does not grant merge authority.

## Exact source comparison

Adopted source is [`pstack/skills/poteto-mode/scripts/` at `99b609a72323b70204eab407c622f436e858e112`](https://github.com/cursor/plugins/tree/99b609a72323b70204eab407c622f436e858e112/pstack/skills/poteto-mode/scripts). Applied only the reviewed delta from frozen `0148b78c56c72a1b8412055913c79f767095b217`. Local paths are under `skills/jstack/jstack-juan-mode/scripts/`. The original package pin `11713c683fe4add4fd403ea880580abbc9e0875f` remains historical provenance; the existing [Babysit](../../adaptations/babysit.md), [pagination](../watcher-pagination/README.md) and [plan](../../adaptations/multi-phase-plan.md) records account for earlier differences.

| Final file | Difference from the adopted source |
| --- | --- |
| `watch-pr/github.ts` | Identical fork query, boolean validation and stack algorithm. Retains the existing missing/repeated review-thread cursor guards. |
| `watch-pr/policy.ts` | Identical remaining-deadline sleep cap. Retains the existing T3 `once` returns, waiting-result types and immediate one-shot query failure. |
| `watch-pr/types.ts` | Identical required fork-identity field. Retains the existing optional `once` and waiting-result type. |
| `watch-pr/policy.test.ts` | Byte-identical to the adopted source, including all four new deadline/cadence cases. |
| `watch-pr/github.test.ts` | Retains every adopted source test plus existing cursor-error tests and a local actual-reader fixture rejecting absent, null, string and numeric fork identity. |
| `check-plan.mjs`, `check-plan.test.ts` | Same algorithms and upstream cases. Only the existing `schedule_task` scheduling markers replace `/loop 1h`; the checker's existing non-executable mode is preserved because callers invoke Node. |

The executable `watch-pr/watch-pr`, dependency bootstrap, store, model configuration, package dependencies, locks and licenses are unchanged. No automatic model fallback, installation, watch service or additional upstream recommendation was adopted.

## Executed verification

On Orbit, Linux x64, Bun 1.4.2, Node 24.19.0, Python 3.14.4, Commander 14.0.0, TypeScript 7.0.2 and bun-types 1.3.14, using the user's already prepared source dependencies:

- **Before production edits:** the three-file regression run had 46 passes and eight failures. The valid inline-code case returned 1 instead of 0; single, queued and query-retry timeout cases slept 60 instead of five seconds; fork parent/child cases included unrelated PRs; the fork `main` subprocess exceeded its two-second bound; and the reader did not request fork evidence. A separate added boundary test also failed because absent fork identity was accepted.
- **After production edits:** `bun run test` passes all **123 tests across eight files**, zero failures. This includes the original one-shot cases with no sleep/retry, same-repository stack ordering, the bounded fork loop case, boolean validation, positive/disabled deadlines and existing plan/fence cases.
- `bun run typecheck` passes both watcher and Orchestrate projects under `--noEmit --strict`. `node --check check-plan.mjs` passes.
- The expanded actual watcher CLI exercise passes all **16 scenarios** against an owned local `gh` fixture, including an unrelated fork and missing fork identity. The fork yields a stack `STATUS` followed by `READY` containing only the requested PR. Missing identity yields one status-query blocker and exit 7. No real GitHub response or live T3 watch is simulated as external proof.
- The existing plan exercise passes one/two-PR plans, a no-review gate, 16 rejection cases and the usage error. Its existing generic-placeholder limitation remains.
- The checker regression suite passes **17 tests**. Packaging's **four tests** pass after the test-only scope correction below. The documentation checker reports zero problems.

The first expanded CLI exercise incorrectly expected one event for a ready stack. The actual command emits a status snapshot before its final verdict. Correcting that new assertion preserves the single-event expectations for the original cases and verifies both stack events.

The first packaging run inspected the user's installed `node_modules/typescript/README.md` and treated its `mailto:` link as a package file. The packaging test now scans Git-tracked package files, matching the distributed source boundary, rather than locally installed dependencies. This is a test-only correction needed to validate a prepared checkout; it changes no shipped skill behavior.

## Reproduce and limits

With declared dependencies already available:

```sh
cd skills/jstack/jstack-juan-mode/scripts
bun run test
bun run typecheck
node --check check-plan.mjs
```

From the repository root:

```sh
python3 -B research/jstack/evaluations/babysit/exercise.py
python3 -B research/jstack/evaluations/multi-phase-plan/exercise.py
python3 -B -m unittest discover -s scripts/jstack -p 'test_check_upstream.py'
python3 -B -m unittest discover -s scripts/jstack -p 'test_skill_packaging.py'
node scripts/jstack/check_docs.mjs
```

These are local regressions, actual command fixtures and strict compilation, not a live fork PR, new provider trial or watch/restart certification. Stack discovery still has the existing 300-open-PR cap. This is not a redesign for arbitrary malformed same-repository cycles. The plan checker remains structural rather than a full Markdown parser or proof of feasibility.

Only the three selected decision reasons gain this implementation reference. They have no `appliedCommit` until an authorized merge is verified. Original adaptation pins and other decision dispositions remain unchanged. Keep the small report and executable tests; no raw test transcript, generated repository, catalog or dependency tree is committed. Installation and merge remain separate user actions.
