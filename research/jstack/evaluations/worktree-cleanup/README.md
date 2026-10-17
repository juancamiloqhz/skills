# Worktree cleanup evaluation

The nineteenth juan-mode procedure adds a read-only worktree auditor and a separately authorized cleanup process. It preserves pstack's six-step structure while correcting path parsing, untracked-file and PR-state assumptions. See the [adaptation record](../../adaptations/worktree-cleanup.md), [source comparison](source-comparison.json) and [audit input contract](../../../../skills/jstack/jstack-juan-mode/references/worktree-audit.md).

Run date: 2026-10-17. Repository base: `3d4c3e9af3ba8526ee871afbb1c45181a668af36`, merged PR #65. The host is Ubuntu Linux with Git, Python 3 and `du`. No installation occurred. Authoring followed skill-creator and writing-for-agents; juan-mode and its pre-review helpers stayed inactive. The two native evaluation agents inherited Codex `gpt-6-astra` and high effort. Saved jstack model configuration was unchanged.

## Reproduce tool checks

Run from the repository root with a new output directory:

```bash
python3 -B research/jstack/evaluations/worktree-cleanup/fixture.py /tmp/jstack-cleanup-example --check
```

This creates 12 registered worktrees entirely inside the supplied scratch directory, including the primary checkout. It checks the real audit CLI, deliberately tests invalid/incomplete inputs, and removes one generated clean candidate without force. It preserves the other worktrees and the removed checkout's branch ref. The fixture uses only local Git repositories and synthetic PR/usage JSON; it does not contact a forge or T3. Omit `--check` to generate a fresh fixture for report-only agent evaluation.

| Case | Observed behavior |
| --- | --- |
| Primary or invoking linked checkout | Held even when clean and merged |
| Clean merged path containing a space or literal newline | Enumerated as one exact path; conditional candidate with matching unused evidence |
| Closed PR over unmerged HEAD | Held; changing the supplied label to MERGED still holds it |
| Detached active checkout | Included and held; branch-only enumeration would miss it |
| Valuable untracked source | Held and named; never labeled disposable scratch |
| Ignored database and tracked edits | Held in their respective categories |
| Open PR or locked registration | Held despite other favorable evidence |
| Missing or mismatched-HEAD ownership evidence | Requires usage verification |
| Missing base or invalid usage JSON | Nonzero incomplete audit, exit 1 |
| Missing registered path or replacement symlink | Row error and incomplete audit, exit 2 |
| Untracked file arriving after first audit | Candidate becomes held on recheck |
| Authorized generated candidate removal | Normal Git removal succeeds; branch ref and every other worktree survive |

The controller compared all fixture file hashes, including Git metadata, around the initial audit; they matched. It also checked table row count and escaping, exact untracked/ignored paths, remote-ref state, registration counts after removal and retained branch reachability. Expected nonzero cases are assertions, not ignored failures. The final reproducer passed after adding the symlink and stale-evidence cases. No unexpected test failure remained.

## Paired report-only evaluation

Both fresh agents received the same auditor and generated fixture. Only one received the cleanup playbook and its input reference. [cases.json](cases.json) retains the task and five assertions. Neither saw the generator, assertions or the other's output. Both were prohibited from deletion, external calls and nested delegation.

Both scored 5/5: complete path inventory, correct holds, conditional candidate treatment, no audit-only mutation, and appropriate reassessment/scope boundaries. Each identified 12 worktrees, two conditional candidates and ten held rows. Each disclosed that synthetic snapshots are not live T3 or forge evidence. The parent compared the entire fixture's before/after file hashes, including Git metadata; they matched.

This is one bounded case pack with a shared auditor, not evidence that the playbook improved classification, reliability or speed. The agents' reports are not evidence of actual deletion. The only removal was the separately scoped controller fixture check. The with-playbook agent measured `df -h /` before and after its report-only run; the rounded output was unchanged. Neither report claimed reclaimed space. Directory-size estimates are not measured filesystem savings.

## Actual repository and host reads

The auditor ran against `/home/ubuntu/Dev/skills` with separately fetched `origin/main` and no usage/PR snapshots. It returned four registrations without row errors: one main/current hold and three unmerged holds. No real worktree was removed, unlocked or pruned. Scoped T3 status and ref lookup confirmed that this conversation uses the root checkout on the implementation branch. They do not establish that every other checkout is unused, and the audit made no such claim.

## Limits and retained evidence

Full pinned-chat discovery, configured transcript-review fanout, live child-worktree ownership, squash-merge source verification and user-worktree deletion remain unverified. Usage snapshots can become stale even when HEAD matches; the procedure requires a fresh pre-removal check. The auditor does not acquire a lock against concurrent writers. macOS simulator/runtime deletion and broader cache cleanup were not run and are inapplicable on this Linux host.

Packaging tests, mode/setup skill validators, Bash syntax, Markdown/link/whitespace checks and final source hashes are the delivery checks. The upstream manifest, source pins, reviewed checkpoint and package license remain unchanged. The existing mode subtree mapping covers the new procedure and auditor support files.

Retain only this report, the small fixture reproducer, task/assertions and source comparison in the repository. Raw audit JSON, generated repositories, full agent reports, grading and the review viewer stay under `/tmp/jstack-cleanup-20261017` for the pending review. Their dirty, ignored, detached and locked fixture states are intentional. All evaluation agents have finished. Remove task-owned scratch only after acceptance when no work depends on it, under the [retention policy](../../upstream-fidelity.md#evaluation-evidence-retention).
