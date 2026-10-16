---
name: jstack-no-comments
description: "Spawn Comment Sicko, fix accepted findings, and offer encodings for claimed constraints."
---

# No comments

Spawn Comment Sicko. Act on accepted findings.

Defer to Comment Sicko's fresh perspective.

Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. A findings-only request returns proposed deletions and fixes without changing the project. Apply comment deletions and code fixes only within the caller's edit authority. Repository-required comments and directives remain protected; identify the exact requirement when it conflicts with a deletion. This skill does not authorize publication, installation, model changes or merge.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree. Pin the base, HEAD and scoped working-tree contents, including caller-owned edits. Read [configuration and execution](references/execution.md) before dispatch.

## Steps

1. Spawn one fresh Comment Sicko reviewer through the execution contract. Supply the complete [reviewer prompt](agents/comment-sicko.md), scope, snapshot, authority and owned output paths. Do not restate its rules.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, run `/jstack-how` or `/jstack-why` on their symbol. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Discard only that reviewer's proposed changes and rerun one rejected report with the failure named. Reject a second, report it open, and fail `/jstack-no-comments`.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, run `/jstack-architect` once for the accepted set and surrounding code. Stop at the sketch. Architect shapes. Step 4 implements.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The **jstack-principle-fix-root-causes** and **jstack-principle-redesign-from-first-principles** skills guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise delete only within the caller's comment-edit authority, report the constraint open, and sketch out-of-scope work. Preserve exact keep-list exceptions and repository-required comments. A missing investigation or unverified external constraint is incomplete evidence, not proof that an exception is false.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work. Verify accepted edits with the scoped language, lint and behavior checks; report unavailable or failed checks as incomplete. Distinguish proposed from applied deletions and count comments consistently, not diff lines.
