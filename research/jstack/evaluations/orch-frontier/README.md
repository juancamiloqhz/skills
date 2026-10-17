# Orchestrate frontier evaluation

The helper can refresh a supplied PR chain from GitHub and published Git branches without Graphite. It records current PR numbers, branches, commit IDs, merge state and the first open PR in the existing `frontier.json` format. A failed inspection keeps the previous generation intact.

Source pin is `11713c683fe4add4fd403ea880580abbc9e0875f`; local base is merged PR #70, `1de37148702a711666110a062d57306b29d8dd88`. The [adaptation record](../../adaptations/orch-frontier.md) explains the required explicit scope and every source difference. [Source comparisons](source-comparison.json) identify the exact source and local files. This is a tool dependency, not an enabled Orchestrate playbook.

## Results

On 2026-10-17, Ubuntu Linux, Bun 1.4.2, Git 2.53 and Python 3.14.4:

- The complete executable suite passed 83 tests: 12 retained upstream store/CLI tests, 23 new frontier tests and 48 unchanged watcher tests. Frontier cases use real local commits, branches and a bare published origin. Modeled GitHub responses use real Git ancestry for comparisons. Cases cover stale local branches, valid merged prefixes with deleted branches, all-merged scope, incorrect or ambiguous order, stale API heads, malformed commit IDs, wrong repositories, forks, closed-unmerged links, invalid JSON, unavailable API, missing refs, ancestry mismatch and changes during inspection. Each rejected refresh with a prior record verifies byte-for-byte preservation.
- The actual CLI passed through child processes, including missing `--prs` and successful JSON output. An initial run had 81 passes and one CLI fixture failure because the child did not receive the modified executable search path. Explicit environment forwarding fixed the fixture. A type-check error in a test callback was also corrected. Final results above include the added malformed-SHA regression.
- Both strict TypeScript projects passed using the available TypeScript 5.9.3 and bun-types 1.4.2. The locked development environment with TypeScript 7.0.2 and bun-types 1.3.14 was not installed or tested. Tests ran from an exact isolated source copy using the existing cached Commander 14.0.0.
- All four packaging tests, changed-document Markdown lint, relative-link checks and `git diff --check` passed. Final TypeScript files matched the tested copy, and source comparisons accounted for the three edited upstream files plus the new adapter tests.
- The previous [six-part CLI exercise](../orch-runtime/exercise.py) passed. Units, verdicts, duplicate inbox pointers, gates, lock recovery and manual dependency refusal retain their previous behavior.
- A live authenticated CLI read of this repository's merged PR #70 succeeded. It recorded `MERGED`, the published PR head `c80fceb7ae1adda851e34c1ac6850e892c9d6596`, generation 1 and no lowest unmerged PR in an isolated scratch store. This exercised real repository/PR reads and published trunk refs. The all-merged path does not call the commit comparison endpoint.

The adapter tests are executable tool checks, not agent prompt evaluations. No workflow activation, delegated reviewer, model change or installation was required. Test fixtures cannot establish GitHub race timing or provider persistence. Live stacked restacks and full coordinator restart recovery remain unverified.

## Reproduce

With Bun and the declared dependencies already present, run from the repository root:

```bash
bun test skills/jstack/jstack-juan-mode/scripts/orch skills/jstack/jstack-juan-mode/scripts/watch-pr
python3 -B research/jstack/evaluations/orch-runtime/exercise.py
```

Run `bun run typecheck` from the bundled scripts directory. Installing dependencies is a separate manual action. The test fixture creates and removes only its own temporary repositories and stores; it makes no live GitHub calls. The source comparison uses UTF-8 unified diffs with the recorded source/local paths as labels and SHA-256 hashes of source, local file and diff bytes.

For a live read, use an owned store and actual PR numbers in dependency order. Authenticated `gh`, Git access to origin and an origin on github.com are required. The command below is an example with hypothetical PR numbers:

```bash
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board init
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board --json frontier set --repo /path/to/project --prs 101,102,103
bun skills/jstack/jstack-juan-mode/scripts/orch/orch.ts --store /tmp/pagination-board status
```

Use durable owned storage for a real ongoing task. `frontier set` updates the saved PR record; `status` renders that record alongside the task board. Neither command implements a task or merges a PR.

## Normal use and limits

Suppose a pagination feature has an API PR, a UI PR built on the API, and a tests PR built on the UI. You can ask:

> Refresh jstack's saved status for PRs 101, 102 and 103, in that order. Tell me which PR is first still open. Leave them open.

If the API PR has merged and the remaining chain has been correctly retargeted and restacked, the helper records the UI PR as first open. If someone pushes a newer API commit that the UI branch does not contain, the refresh fails and retains the old record. The agent must report the failed refresh; an old saved generation is not current proof.

The supplied list defines the scope. The helper cannot discover omitted PRs or prove historical merged-prefix order. Open PRs must form one same-repository chain rooted at the current default branch. Forks, enterprise hosts and non-default target roots remain unsupported. Checks, approvals and merge eligibility are outside this helper. A successful repeated read is not a guarantee against later changes.

The full Orchestrate route remains unavailable, with 22 playbooks shipped. Next work is completion deduplication, acknowledged drains and T3 child reconciliation before coordinator recovery trials. Source pins, reviewed checkpoint, licenses, lockfile, saved models and schedules remain unchanged. Retained evidence is this report, the source comparison and executable tests; routine logs and temporary stores stay outside Git.
