# Coverage checkpoint after PR #97

The existing-port update batch is complete against the audited pstack revision, with intentional differences retained. Jstack is still not a complete pstack port or a fully verified implementation on every provider.

This checkpoint compares the original audit at local `1f5a8d7184d24a0d95be9626ae63642c4163e09d` with merged PR [#97](https://github.com/juancamiloqhz/skills/pull/97), `9d41e2843473232ce6f1ad9dbd33ca14426919b4`. Upstream remains frozen at `0148b78c56c72a1b8412055913c79f767095b217`. It reconciles the [original audit](README.md) with merged implementation reports, rather than replacing historical results or reviewing newer upstream commits.

## What is available

| Measure | Audit baseline | After PR #97 |
| --- | ---: | ---: |
| Mapped top-level pstack skills | 42 of 55 | 44 of 55 |
| Additional Cursor team-kit helpers | 3 | 3 |
| Total shipped jstack packages | 45 | 47 |
| Bundled mode playbooks | 23 of 23 | 23 of 23 |
| Unported top-level pstack skills, excluding external Unslop | 12 | 10 |

Bro and Ketchup account for the two added skills. Unslop remains a separately installed dependency. Provider discovery, persistence and full unattended execution have separate evidence requirements; these counts establish source/package coverage only. The earlier user-reported installation checks covered 45 packages and do not establish installation of the current 47.

## All 60 changed source paths accounted for

The audit found 60 changed paths in 22 mapped trees relative to their original pins. **37 paths have merged updates or mixed adopt/keep assessments; 23 retain their existing implementation for documented reasons.** A mixed row does not mean every upstream hunk was adopted. Model policy, runtime and ownership exceptions remain explicit in its linked report.

All paths below are relative to `pstack/skills/`. Braces list exact alternatives. Counts are distinct files and sum to 60.

| Source paths | Count | Current disposition and evidence |
| --- | ---: | --- |
| `poteto-mode/scripts/watch-pr/{github.ts,policy.ts,types.ts,fakes.test-helper.ts,github.test.ts,policy.test.ts}` | 6 | Updated in PR #81: [pagination and owner gates](../../evaluations/watcher-pagination/README.md). |
| `poteto-mode/scripts/{check-plan.mjs,check-plan.test.ts,package.json}` | 3 | Updated in PR #82: [fence parsing and test wiring](../../evaluations/plan-fences/README.md). Retain local strict Orchestrate typechecking. |
| `principle-{attack-the-premise,fix-root-causes,test-behavior-not-implementation,make-operations-idempotent}/SKILL.md` | 4 | Updated in PR #85: [substantive principle changes](../../evaluations/principle-behavior-updates/README.md). |
| `typescript-best-practices/{SKILL.md,references/patterns.md}` | 2 | Updated in PR #86: [branded-ID guards](../../evaluations/typescript-brand-guards/README.md), preserving prior range/index corrections. |
| `create-verification-skill/SKILL.md` | 1 | Updated in PR #87: [usable startup](../../evaluations/verifier-usable-startup/README.md). Automatic Claude linking remains the user's choice. |
| `interrogate/references/lead-judgment.md` | 1 | Updated in PR #88: [lead judgment](../../evaluations/interrogate-lead-update/README.md). |
| `how/references/explorer-prompt.md` | 1 | Updated in PR #89: [explorer prompt](../../evaluations/how-explorer-update/README.md). |
| `why/references/sources/{code-archaeology,incident-postmortem,sentry,slack}.md` | 4 | Updated in PR #90: [source guides](../../evaluations/why-source-guides/README.md). |
| `swarm/SKILL.md` | 1 | Updated in PR #91: [wording](../../evaluations/swarm-wording-update/README.md), retaining explicit worker count and saved model options. |
| `principle-{encode-lessons-in-structure,exhaust-the-design-space,guard-the-context-window,laziness-protocol,migrate-callers-then-delete-legacy-apis,type-system-discipline}/SKILL.md` | 6 | Updated in PR #92: [shorter source bodies](../../evaluations/principle-source-trimming/README.md). |
| `poteto-mode/SKILL.md` | 1 | Updated in PR #93: [receiving-chat coordination](../../evaluations/playbook-coordinator/README.md), retaining activation/configuration contracts. |
| `poteto-mode/playbooks/orchestrate.md` | 1 | Updated in PR #94: [stack ownership](../../evaluations/orchestrate-topology/README.md). Existing explicit GitHub scope remains. |
| `poteto-mode/playbooks/{shipping,opening-a-pr,babysit}.md` | 3 | Updated in PR #95: [landing sequence and callers](../../evaluations/shipping-sequence/README.md). |
| `poteto-mode/playbooks/{autopilot-full,autopilot-stack,multi-phase-plan}.md` | 3 | Updated in PR #97: [verification cadence, recovery records and topology](../../evaluations/autopilot-update/README.md). |
| `{how,why,arena,interrogate,reflect,figure-it-out,show-me-your-work}/SKILL.md` | 7 | Keep configured model/effort and visible failure instead of the new adaptive effort/speed and Cursor-family fallback rules. Existing [configuration contract](../../../../skills/jstack/jstack-juan-mode/references/configuration.md) and original audit govern; a changed policy needs a user decision. |
| `poteto-mode/playbooks/{autonomous-run,bug-fix,eval,feature,hillclimb,perf-issue,refactoring,runtime-forensics,session-pickup,trace-forensics}.md` | 10 | Keep. Each source delta only adds task-selected effort/speed. These procedures already use the configured contract; no behavioral update is omitted beyond that deliberate policy difference. |
| `no-comments/SKILL.md` | 1 | Keep. Source changes the Cursor registered-agent identifier and adds adaptive effort. Jstack loads the complete bundled `agents/comment-sicko.md` through its configured execution contract. A human-readable “Comment Sicko” name is not a stale registry call. [Adaptation](../../adaptations/no-comments.md). |
| `poteto-mode/playbooks/worktree-cleanup.md`, `poteto-mode/scripts/worktree-audit.sh` | 2 | Keep explicit base and conservative content/ownership checks. Upstream's new default-base and Origin interface remain unsupported differences. Its automatic fetch and untracked-content assumptions do not replace local loss checks. [Adaptation](../../adaptations/worktree-cleanup.md). |
| `poteto-mode/scripts/orch/{orch.ts,store.ts,orch.test.ts}` | 3 | Keep the remote-verified explicit GitHub frontier and recoverable inbox. Automatic chain discovery, Origin and the corresponding upstream tests are not adopted. [Frontier](../../adaptations/orch-frontier.md) and [inbox](../../adaptations/orch-inbox-recovery.md) explain the concrete differences. |
| **Total** | **60** | **37 updated/mixed; 23 kept. No remaining unassigned path in this frozen changed-path set.** |

PR #83's [external watch paths](../../evaluations/upstream-watch-coverage/README.md) and PR #84's [documentation check](../../evaluations/docs-consistency/README.md) address integration findings outside those 60 paths. PR #96 adds [Bro and Ketchup](../../evaluations/recap-skills/README.md), which were outside the baseline's mapped trees.

The inventory still prints 60 changed paths because it compares upstream with historical `adaptedFrom` pins, not with the merged implementation dispositions above. Do not report that number as 60 outstanding fixes or advance pins merely to make it zero. The shared reviewed checkpoint also remains unchanged: this batch is not the scheduled review's complete watched-range assessment.

## What remains and the next proposal

Ten top-level skills remain absent: `in-your-own-words`, `sharpen`, `blast-radius`, `teach`, `correct`, `create-formal-verification-skill`, `recall`, `automate-me`, `poteto-help` and `make-bot-ui`. The original audit retains their full scope and acceptance cases. Unslop is external, not an eleventh unimplemented workflow.

The next recommended addition is the pair **In your own words and Sharpen**, in one bounded PR after explicit selection. In your own words restates the goal; Sharpen improves the approach and then performs the authorized task, retaining an outside check. Preserve their standalone boundaries, invocation intent, source wording and license; add package mappings and minimal examples. Evaluate an ambiguous request without inventing requirements, and an over-specified task without erasing the user's constraints. Keep model configuration unchanged and test supported dependency discovery. Do not infer approval for the other eight missing skills from selection of this pair.

For example, a user says “Rewrite the importer with a queue because uploads time out.” In your own words should restate the goal and distinguish it from the proposed solution. Sharpen should improve the approach, preserve real constraints and then do the authorized work with an outside check. These are proposed capabilities, not commands currently available in jstack.

Other open work remains explicit:

- The source-grounded help entrypoint and eleven-page guide need a coordinated port; current guide coverage is zero. Help must describe the shipped catalog rather than promise absent skills.
- Recall and Automate me need scoped history evidence. Formal verification needs executable proof and a mutation/counterexample case.
- Make bot UI and Benny need concrete host-integration designs and separately authorized live tests. A webhook timer alone does not implement them.
- Origin, automatic chain discovery, plugin/harness distribution and bundled Unslop remain separate decisions. Their absence is a capability or distribution difference, not proof they are unnecessary.
- Installed-provider tests must cover dependency calls, invocation metadata, exact configured delegation, later-task activation, compaction/resume, opt-out, cancellation, watch continuation and recovery. Existing bounded tests remain evidence only for their recorded cases. Full unattended Autopilot is still unproven.

## Verification and retention

Reran the existing census at both immutable local revisions using the frozen source. The current census reports 44 mapped pstack skills, three team-kit helpers, 47 shipped packages and all 23 playbooks. Its exclusive source groups still sum to 171 files: 120 mapped-tree files, 12 unported-tree files, one external Unslop file, two agents, 12 automation files, 18 documentation files and six root/branding files.

The table's expanded path set is checked against all 60 original changed paths without duplicates. Every cited implementation PR #81 through #97 has a merge commit on current `origin/main`. The retained model-only source deltas and No-comments dispatch were reread; existing implementation reports provide the source comparisons and tests for merged changes. This is a reconciliation, not a new line-by-line audit of all 171 files or a rerun of their runtime tests.

Reproduce the census with the existing script, substituting a clone containing the source objects:

```sh
python3 -B research/jstack/coverage-audits/2026-10-18/inventory.py \
  --upstream /path/to/cursor-plugins \
  --local-ref 9d41e2843473232ce6f1ad9dbd33ca14426919b4
node scripts/jstack/check_docs.mjs
```

The documentation checker and changed-document links pass. All operational skill files, scripts, model settings, source pins and schedules are unchanged by this checkpoint. Retain this report and its navigation links; census JSON and inspection output remain in task cache. No new test harness or runtime log is added.
