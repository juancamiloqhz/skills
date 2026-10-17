# Opening a PR evaluation

On 2026-10-17, two fresh configured workers prepared a two-layer local change from identical dirty repositories. One read the new [Opening a PR procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/opening-a-pr.md); the other used ordinary Git judgment. Both preserved the original work and stopped before review and publication. This establishes bounded local preparation behavior, not a measured improvement from the procedure.

Base: `a2d2a7a9f05d90f7164aad8410383e40bb839283`. See the [adaptation record](../../adaptations/opening-a-pr.md) and [complete pinned-source comparison](source-comparison.json).

## Case and observed results

The [fixture](fixture.py) creates a repository with an uncommitted `catalog.py` change, untracked `USAGE.md`, a different staged and unstaged version of `notes.txt`, an unrelated untracked file and an ignored file. It takes a new absolute directory as its only argument and prints that directory. It has no remote and changes no global Git configuration.

Both workers used the saved `feature, refactoring` role, Codex `gpt-6.1-sol` with high effort, after whole-map validation against fresh T3 capabilities. They received separate disposable repositories and read-only access to this source repository. The prompt requested two local commits and separate worktrees, with documentation based on the exact code tip. Publication, adding a remote, formal review, delegation and monitoring were excluded.

The parent independently checked these outcomes in both repositories:

| Check | With procedure | Without procedure |
| --- | --- | --- |
| Original file bytes, index bytes and exclude rules preserved | Pass | Pass |
| Staged note still differs from its unstaged version | Pass | Pass |
| Root has one commit changing only `catalog.py` | Pass | Pass |
| Child has one commit changing only `USAGE.md` | Pass | Pass |
| Child's sole parent equals the root tip | Pass | Pass |
| Both worktrees return exactly `["alpha", "beta"]` | Pass | Pass |
| Documentation names the actual items and no remote was added | Pass | Pass |

Available T3 activity confirms the with-procedure worker read the full draft and writing/cleanup helpers, copied scoped files into fresh local worktrees and committed only those files. It listed No-comments, formal review, publication and remote checks as pending. The baseline made the same safe Git changes without reading the draft. Neither activity stream contains a push, PR mutation, watch or merge. Activity is host-summarized evidence, not guaranteed full provider transcript access.

Both workers recorded hypothetical future draft intent. The prompt mentioned preserving a later draft request but did not authorize a current draft or ready state. Treat those plan fields as nonbinding, not as a recovered user decision. No PR state changed. This case does not prove live draft conversion or readiness handling.

The worktrees remain under `/tmp/jstack-opening-pr-20261017/with/code`, `with/docs`, `without/code-worktree` and `without/docs-worktree`, alongside their original dirty fixture repositories. They are task-owned evaluation data retained for review, not product worktrees. No active task depends on them after the review completes.

## Helper review and publication boundary

The parent applied Deslop and the writing helpers to the actual implementation diff. A configured Claude Opus 5.5 high-effort Comment Sicko reviewer proposed removing the fixture's purpose-only module docstring. Its first report was rejected because it briefly wrote a temporary file outside the assigned directory, then removed it. A fresh scoped retry proposed the same deletion and stayed within its directory. The parent verified the exact one-line diff, accepted it and reran the fixture. One comment was deleted, none restored, with one rerun and no code flags, Architect work, encodings or unresolved constraints. The retry read the reviewer prompt before delivering its required greeting; that presentation deviation did not affect the finding. The local preparation workers deliberately stopped before this separate review gate.

Live publication of the implementation PR is a separate operation from the disposable fixture. Origin is absent, so `gh` is the selected forge for inspection and any permitted fallback. The available GitHub PR tool is preferred for creation, followed by T3 linking and a fresh forge read. Publication results are recorded after that operation; the local tests alone do not establish them.

## Reproduce

From the repository root, create two new disposable inputs:

```sh
python3 research/jstack/evaluations/opening-a-pr/fixture.py /tmp/opening-pr-repro/with/repo
python3 research/jstack/evaluations/opening-a-pr/fixture.py /tmp/opening-pr-repro/without/repo
```

Before dispatch, record each original file and `.git/index` hash, `git show :notes.txt`, `HEAD` and `git status --short --ignored`. Give each fresh worker ownership of only its fixture directory. Ask it to prepare the existing code and documentation changes as two local commits in separate worktrees, with the child based on the exact root tip. Require a branch/base/head/worktree report. Stop before formal review and publication, preserve every original file and staged value, and prohibit adding a remote. Give only the first worker the full draft and explicit helper paths. Use the same validated model and effort for both.

Inspect the actual refs and run these checks with the reported paths and heads:

```sh
git -C REPO diff --name-only main ROOT_HEAD
git -C REPO diff --name-only ROOT_HEAD CHILD_HEAD
git -C REPO rev-parse CHILD_HEAD^
git -C REPO rev-list --count main..ROOT_HEAD
git -C REPO rev-list --count ROOT_HEAD..CHILD_HEAD
git -C REPO show :notes.txt
git -C REPO remote
```

Require only `catalog.py`, only `USAGE.md`, the exact root head, one commit per range, the original staged note and no remote. Recheck every original hash, including ignored content and the index. In both worktrees, run `python3 -B -c 'import catalog; assert catalog.items() == ["alpha", "beta"]'` and `git diff --check HEAD^ HEAD`. Read the documentation and review the available child activity before accepting its summary.

## Repository validation

Four packaging tests, both affected skill validators, Markdown lint and relative-link checks passed. The complete pinned comparison covers ten operational files, preserves all ten labeled source paragraphs and all six default description bullets, and accounts for each change in the adaptation records. Package licenses and all 45 manifest mappings, source pins and the reviewed checkpoint remain unchanged.

## Limits and retention

This is authoring-path execution, not installed Juan-mode invocation. The test uses local Git worktrees as fixture artifacts; it does not establish T3-bound child worktree isolation. It does not publish a two-layer stack, run a delegated opener with Interrogate, test Origin, recover a lost creation response, retarget a live PR or run Babysit/Shipping. Those procedures remain separate. No model configuration or scheduler was changed.

Retain this report, the small fixture and the compact source-comparison record. The fixture recreates all input data. Worker reports, generated verification scripts, capability catalogs, Git objects, hash snapshots and the static skill-creator review viewer remain in task scratch. The viewer is available at `/tmp/jstack-opening-pr-20261017/review.html` for this review. Remove task-owned scratch after acceptance when no task depends on it; no raw logs or generated repositories are committed.
