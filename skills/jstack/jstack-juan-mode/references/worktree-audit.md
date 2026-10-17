# Worktree audit inputs

Run `bash scripts/worktree-audit.sh REPO --base-ref BASE --json` from this package. The entrypoint needs Python 3, Git with `worktree list --porcelain -z`, and `du`. It reads local refs and never fetches, scans unrelated chats, installs tools or deletes files. Refresh the chosen remote base separately when authorized. A missing base fails the audit; do not substitute a guessed branch.

The JSON includes every Git registration, including the main, detached, locked and prunable worktrees. Each row retains size, commit age, ancestry against the recorded base commit, tracked/untracked/ignored paths, remote branch state, supplied PR state and usage evidence. Table mode escapes paths and evidence labels so spaces, tabs and newlines cannot split rows. Sizes and ages are prioritization hints, not evidence of abandonment.

Exit 0 means the inventory completed, not that deletion is safe. Exit 1 means invalid inputs or an unavailable inventory/base. Exit 2 means some rows could not be inspected; inspect their `errors`, hold those rows and do not describe the audit as complete. Missing PR or usage evidence stays unknown even on exit 0.

## Optional evidence snapshots

`--pr-json FILE` accepts the JSON array from a scoped `gh pr list --state all --json number,state,headRefName` or an equivalent forge read. Obtain enough pages to cover the candidate branches. A missing branch in a limited response is not proof that no PR exists. `OPEN` holds a row; `CLOSED` and `MERGED` do not prove its current HEAD landed. Squash merges need a separate source/patch comparison before removal when ancestry is false.

`--usage-json FILE` accepts an array of explicitly collected usage records:

```json
[
  {
    "path": "/absolute/path/from/git-worktree-list",
    "head": "full-current-commit-id",
    "state": "active",
    "source": "T3 thread/task ID or explicit user confirmation",
    "observedAt": "2026-10-17T19:00:00+00:00"
  }
]
```

States are `active`, `pinned`, `unused` and `unknown`. Read current project-scoped T3 bindings, pinned/active conversations and owned child work before assigning `unused`. Neither a settled thread nor an old transcript proves inactivity. Unknown ownership stays `unknown`; do not manufacture evidence to obtain a candidate. Optional `lastChat` records the latest identified chat and activity time; omit it when that scan is incomplete. A record for a different HEAD is ignored as a usage verdict. The snapshot retains its timestamp and source, but is not a live lock. Reconcile it again immediately before deletion; matching HEAD alone does not establish that a thread stayed inactive.

The shell tool cannot see T3's sidebar or task lifecycle by itself. It does not infer paths from branch listings, which omit detached checkouts, or automatically search private transcript stores. Supply only evidence scoped to this project. Long transcript inspection belongs to the playbook's configured read-only reviewers.

## Advisory buckets

The main and invoking checkouts are held. Locked, prunable, bare or incompletely inspected registrations are held. Tracked edits, untracked files and ignored files each hold a row; none is labeled disposable scratch. An open PR or active/pinned usage also holds it. Unmerged HEADs remain held even for closed/merged PR records. A clean merged row with unknown usage needs verification. Only a clean merged row with supplied `unused` evidence becomes a `candidate`.

`candidate` is advice, not authorization. The playbook still checks current usage, ignored files, branch preservation, fresh Git/forge state and the exact authorized target. Removal does not belong in this tool.
