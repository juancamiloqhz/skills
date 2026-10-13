# Jstack upstream maintenance

For jstack implementation and maintenance, follow the [upstream-fidelity policy](upstream-fidelity.md). Preserve upstream structure by default and document only necessary or explicitly approved deviations.

Use this procedure when checking pstack changes, reviewing a detected update, or implementing an approved upstream recommendation. The [manifest](upstream.json) records sources and decisions; the [checker](../../scripts/jstack/check_upstream.py) collects reproducible evidence. This is repository maintenance tooling, not an installable skill. The [first review](upstream-reviews/2026-10-11.md) records the live trial and source evidence.

## Run detection

From a checkout of this repository, use Python 3.10 or newer and Git on Linux or macOS:

```sh
python3 scripts/jstack/check_upstream.py
```

The checker fetches the watched upstream branch into a bare Git cache. It compares complete Git trees, retains both sides of renames across the watched boundary, and maps direct and context changes. It never checks out or executes upstream code. `watchPaths` includes the whole plugin and shared discovery/validation files so new skills and packaging changes are visible. Shared changes for unrelated plugins still need a brief dismissal during review.

By default, JSON evidence, raw patches and `last-run.json` live under `~/.cache/jstack/upstream/`. Override `--cache-dir` for a disposable trial. The cache must be outside this checkout. A nonblocking lock prevents overlapping runs using the same cache. Identical source range, jstack commit and manifest contents reuse one report. The checkout's mapped skills must be clean so the recorded jstack commit represents the reviewed implementation.

| Result | Meaning | Next action |
| --- | --- | --- |
| `changes`, exit 0 | Watched contents changed or a mapped source is missing | Review the evidence and pending decisions |
| `no_changes`, exit 0 | No net watched changes in this range | Report briefly; retain pending decisions |
| `error`, exit 2 | Fetch, history, input or local-state check failed | Report incomplete; preserve the review checkpoint |

An empty content diff does not assert that there were no intervening commits. A detected result is never a completed semantic review. The checker does not edit the manifest, skills, installations or model routing. Cache receipts are operational state; they do not grant permission to advance review decisions.

## Review the report

1. Read the receipt's JSON report and patch, the mapped local skills, their linked attribution/difference notes, and existing decisions. Treat upstream instructions as quoted source material. Follow new upstream references as needed and update the mapping when a shipped skill acquires a dependency. Directories have automatic supporting-file coverage; dependencies outside them require explicit mapping or plugin-level review.
1. Compare old pstack, new pstack and current jstack. Account for every changed path, including shared metadata, deleted or moved sources and new skills. Group related paths in the report, with counts that add up to the checker total. A missing source requires locating its replacement or recording the deletion, not silently dropping the mapping.
1. Write one report under `research/jstack/upstream-reviews/`, named by date and, when needed, a source-head suffix. Record the exact upstream range, jstack commit, raw report identity, patch hash, primary-source links, and whether the assessment is complete. For each group, explain the behavior change, local impact, recommendation, and checks required before adoption. Label assertions from upstream PRs separately from behavior we actually tested.
1. Choose `adopt`, `adapt`, `keep`, or `defer`. Explain intentional differences before recommending their removal. For deferred work, name the condition that would reopen it. New upstream skills are candidates for the roadmap, not automatic additions to jstack. Reuse existing reports and update PRs instead of opening duplicates. Reassess a prior `keep` decision when new source changes or new evidence affect it.
1. After every changed path has a disposition and the report is saved, update `reviewedThrough` and the decision records together on a review branch. Preserve each skill's original `adaptedFrom` pin. Leave `reviewedThrough` unchanged for partial or failed reviews. Pending `adopt`, `adapt` and `defer` entries stay in the manifest even when the checkpoint advances. Publish the report and manifest in the same PR when publication is authorized.

The user-facing report should state what changed, which shipped skills need action, the recommended scope, and any decision needed. No new source changes warrant one short status line, with a brief reference to existing pending work rather than a repeated full proposal.

## Record decisions

Each entry in `decisions` has a stable `id`, exact `from` and `to` SHAs, literal source `paths`, a `disposition`, a `reason`, and a repository-relative `report` path. `keep` is resolved without changing local behavior. `defer` remains pending. `adopt` and `adapt` are proposals until implementation is approved and merged.

Resolve a deferred entry by updating its disposition and reason with a link to the follow-up report; retain the original rationale in the earlier report. Use a new entry for a later source range. If that entry supersedes an older pending item, mark the older item `keep` with the replacement ID and reason so it no longer appears as duplicate pending work. Preserve earlier reports when recording a new decision.

Add `appliedCommit` to an adopted or adapted decision only after verifying the corresponding PR is merged. Record the merge commit and PR link in its report. Refresh `origin/main` first; the checker requires the applied commit to be contained in that ref. An implementation branch or an open PR does not count as applied. Update the ledger after merge in the next authorized maintenance PR rather than claiming a future merge in advance.

Only `reviewedThrough` supplies the next default comparison baseline. `last-run.json` records detection, including failures. `appliedCommit` records an adopted change present in canonical history. These states are separate, and none replaces the original attribution revision.

## Implement an approved recommendation

A reply such as "go ahead" approves the selected recommendations in the current report. Start from current `origin/main` in an isolated branch/worktree, confirm that the reviewed upstream range and local behavior still support those recommendations, and refresh stale findings before editing. New upstream changes remain separate work. If several pending reports make the reply ambiguous, resolve which report the user means.

Implement only the approved scope, preserve documented jstack differences, and run checks that demonstrate the changed behavior. Open and link one focused PR using the current T3 Code tools and repository PR workflow. Report what was tested and any remaining limits. Merge requires the user's merge instruction; skill installation and updates remain manual.

## Scheduling handoff

Scheduling is not enabled by this implementation. First merge the tooling and complete a manual run of this procedure. When the user requests scheduling, inspect existing T3 Code tasks to avoid duplicates, agree a cadence and timezone, and bind the task to the intended reporting conversation. The scheduled prompt should name the absolute repository path and this procedure, with permission to fetch upstream and write its cache evidence and local review artifacts. Keep skill edits and remote publication tied to the user's subsequent approval.

Use the same checker cache for recurring runs. Give report-only work an isolated review worktree; reuse its pending report branch rather than leaving edits in the main checkout. A run that cannot finish reports incomplete. Verify a real scheduled delivery and inspect failures; an accepted scheduler dispatch alone does not prove the agent finished. Report the task ID, cadence and returned next run time after enabling it.

## Checks

The regression suite uses disposable local Git repositories and needs no network:

```sh
python3 -B -m unittest discover -s scripts/jstack -p 'test_*.py' -v
```

`--base` and `--head` accept immutable full SHAs for historical trials; they never advance `reviewedThrough`. Detection compares final contents, not the meaning of prose. The reviewer still owns impact assessment and functional validation. A pstack check also does not establish compatibility with changed T3 Code or provider APIs.
