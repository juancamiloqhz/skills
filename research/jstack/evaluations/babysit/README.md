# Babysit evaluation

Babysit now supplies the four upstream modes and the bundled GitHub watcher. T3 owns waiting. The executable assesses once, returns pending status without sleeping and never installs its dependencies. This evaluation proves local classification and bounded agent decisions; it does not prove an unattended T3 monitoring cycle.

Source: `11713c683fe4add4fd403ea880580abbc9e0875f`. Base: merged Opening a PR, `90ba52a`. See the [adaptation record](../../adaptations/babysit.md) and [source comparison](source-comparison.json).

## Executed checks

On 2026-10-17, Linux x64, Bun 1.4.2:

- All 38 unchanged upstream tests passed. They cover query fallback, check pagination, hidden GitHub CI refusal, stack priority, queue advancement, error handling and rendering.
- Ten added `once.test.ts` cases passed. They cover pending return without sleep, immediate query failure, empty checks, conflict priority, status-only exit semantics, frontier-ready queues, merged queues and new-head invalidation.
- The actual packaged executable passed all five local response cases in [exercise.py](exercise.py). A temporary `gh` fixture supplies raw JSON. Pending CI returns within the five-second limit; no polling process remains. Conflicts, hidden CI refusal and unavailable checks retain exits 2, 4 and 7. A status-only conflict returns zero with the conflict still present in its JSON.
- The actual executable read merged PR #60 through authenticated GitHub and returned `STATUS`, a merged row and head `974e84bba42e8a87bcc40043617a6204df99dbff`. This read did not start a watch or modify GitHub.
- After publication, a single read of open PR #61 at `2c3219f62861e019ad956510ca5994051848fe69` returned exit 7, `BLOCKER/status-query/checks-unavailable`, with one failure and no retry. GitHub reported a clean merge state but no check runs. This verifies the documented empty-check limitation on a real open PR; it is not a readiness pass. No watch was registered.
- Missing and mismatched runtime dependencies produced the manual-prerequisite error without installation. The initial test run lacked Commander and failed CLI module resolution while 29 core tests passed. Temporary links to cached Commander 14.0.3 then allowed all 48 tests to run. The final runtime tests and executable exercise used exact Commander 14.0.0, downloaded only into task scratch and verified against the lockfile SHA-512. No package-manager installation or lifecycle scripts ran.
- Strict type checking passed with available TypeScript 6.0.3 and bun-types 1.4.2. The source lock pins TypeScript 7.0.2 and bun-types 1.3.14; that complete frozen development environment was not installed or tested.
- Four packaging tests, both skill validators, changed Markdown lint, relative links and `git diff --check` passed. The manifest, source pins and saved model configuration are unchanged.

With the declared dependencies already present, reproduce from the repository root:

```sh
bun test skills/jstack/jstack-juan-mode/scripts/watch-pr
python3 -B research/jstack/evaluations/babysit/exercise.py
```

For a new installation, the user runs `bun install --frozen-lockfile` in the skill's `scripts` directory. The executable reports this prerequisite; it never executes it. Tests need Bun; live GitHub status also needs authenticated `gh`. Do not treat the local fake-GitHub exercise as a live monitoring test.

## Bounded workflow comparison

Two fresh native Codex children used the configured `feature, refactoring` model, `gpt-6.1-sol` at high effort. One read the playbook and triage reference. The baseline read neither. Both answered the four independent [cases](cases.json), wrote only their scratch outputs and made no live PR calls. The parent graded the answers against the supplied facts and the pinned procedure.

| Case | With playbook | Baseline |
| --- | --- | --- |
| Read-only check with conflict, threads and failed CI | Reports conflict first, rejects exit-zero readiness, leaves all changes to the owner | Same boundary and first blocker |
| Queued frontier ready, upper build pending | Stops at `WAITING/merge-queue`, preserves queue and hands off without merging | Keeps waiting for the upper build, contrary to this playbook's stop condition |
| Third-pass auth finding and proven upper-stack export use | Escalates auth, proposes evidence-backed dismissal of export claim, obeys no-reply/no-edit scope | Same substantive dispositions and scope |
| Unsupported host wake, missing dependency, old ready head | Reports incomplete readiness and monitoring, offers manual prerequisite, refuses a substitute loop | Reports the gaps and stale proof; no monitoring or installation claim |

That is four acceptable case decisions with the playbook and three without it in one run per condition. The queue case provides a useful distinction; the other cases do not establish an advantage. These are hypothetical decision tests, not evidence of actual CI repair, review replies, watch registration or wake handling. Raw answers, grading JSON and the static review viewer remain in task scratch.

Configured Comment Sicko review used Claude Opus 5.5 at high effort on a private snapshot of newly authored watcher hunks. It returned an empty diff because those hunks contain no comments. Parent inspection accepted the result and preserved all unchanged upstream comments and compile assertions. Subsequent code-only error-guard/formatting changes and the executable fixture received parent review. Deslop found no further scoped cleanup.

## Limits and retained files

Live T3 watch/wake continuation, multi-PR progression across external merges, Origin, authenticated open-PR CI repair and published review replies remain unverified. Source limits include permissive unknown-state classification, bounded thread/history queries and no empty-check success. The playbook explicitly qualifies those results. Shipping is still unavailable.

The copied TypeScript files and tests are runnable upstream tool code, not evaluation logs. The added unit tests and small executable fixture reproduce the T3 substitution. This directory retains only that fixture, four prompts, this report and the required source comparison. Raw logs, catalogs, downloaded dependency files, private review copies and agent outputs stay in task-owned scratch. No raw transcripts or generated repositories are committed.
