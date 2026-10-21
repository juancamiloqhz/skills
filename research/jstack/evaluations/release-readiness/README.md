# Jstack release readiness

Reviewed clean main `110705c8525b365e784e58ba7fd7d3388e61a527` on Orbit, 2026-10-21, after PR #135. The follow-up at `7807ddea30d3350c881da1a71f47c8b755b2480d`, after PR #136, corrected runtime selection and passed all 95 root tests with the unchanged verifier probe. After the user prepared source dependencies, the recheck at `56e9f7b59c6870bdf7b98c8a9e7cd0f53eed722c` passed all 112 Bun tests and both strict typechecks. The assessment is complete; full release verification is **not green**. Existing evidence supports human-reviewed daily use on exercised Codex paths, with prerequisites checked per workflow. It does not certify every provider, dependency or unattended workflow.

## Current source and installation

The frozen census against pstack `0148b78c56c72a1b8412055913c79f767095b217` finds 54 of 55 top-level skill trees mapped. The remaining tree is the declared external Unslop dependency. Jstack ships 57 packages including three Cursor team-kit helpers, and all 23 playbooks. No mapped file is absent at its corresponding relative path. This is coverage, not a new semantic fidelity audit or a review of newer upstream commits.

The census still reports 60 changed source paths in 22 mapped packages relative to their historical pins. The [existing coverage checkpoint](../../coverage-audits/2026-10-18/checkpoint-2026-10-19.md#all-60-changed-source-paths-accounted-for) accounts for those paths; they are not 60 new unresolved fixes. Source pins and the reviewed checkpoint remain unchanged.

The actual installation comparison returns **57 matching, 0 missing, 0 different**, exit 0. It checks expected tracked content, not extra installed files, runtime dependencies or provider behavior. Initially Commander and local TypeScript were absent in both the source and installed Juan-mode scripts directories. The user then prepared the source directory with `bun install --frozen-lockfile`. The source recheck finds Commander 14.0.0, TypeScript 7.0.2 and bun-types 1.3.14. The separate installed copy still lacks those dependencies. Matching skill files therefore do not make its CLI tools runnable.

## Checks executed

Environment: Python 3.14.4, Node 24.19.0, Bun 1.4.2 and the existing Skills CLI 1.7.4. The user installed source dependencies separately. Tests used disposable fixtures; no agent installation, real webhook delivery, PR mutation, agent dispatch or service restart ran during validation.

| Existing check | Current result | Meaning |
| --- | --- | --- |
| Root Python suite, including opt-in catalog/Benny discovery and pinned T3 probe | Initially 94 passed, 1 failed; exit 1. Follow-up: all 95 passed; exit 0. | The first run selected an old outer launcher. The active application has the exact reviewed verifier hash and passes the unchanged wire probe. |
| Model helper fixtures | 19 passed; exit 0 | Lookup, validation and configuration behavior tested with fixtures. |
| Consumer preflight fixtures | 16 passed; exit 0 | Configured role/option and dependency behavior tested with fixtures. |
| Documentation checker fixtures | 20 passed; exit 0 | Existing checker behavior passes. |
| Current documentation check | 0 problems; exit 0 | Current catalog and local-link checks pass. Six command names absent from guide prose remain an informational note, not a failure or proof of broken workflows. |
| Bundled Bun suite | Initially 88 passed, 7 failed, 2 reported errors; exit 1. After manual setup: all 112 passed, 0 failed; exit 0. | The prepared source checkout runs all eight selected test files, including the actual frontier and Orchestrate CLI cases previously blocked by missing Commander. |
| Bundled strict typecheck | Initially exit 127, `tsc: command not found`. After manual setup: exit 0. | Both watcher and Orchestrate projects pass `--noEmit --strict` with local TypeScript 7.0.2. |
| Saved configuration against fresh complete live catalog | Valid, all 17 roles; exit 0 | Global map preserved. This does not check every workflow's model-diversity requirements. |
| Canonical How preflight | Exit 0, `canDispatch: true` | Saved `codex / gpt-6.1-sol / reasoningEffort: high` selection retained. No new helper was dispatched. |

The first runtime probe stopped at `Runtime verifier section not found; inspect this runtime before updating the probe.` Its input was the October 3 outer launcher rather than the active application. The [follow-up](../bot-ui-transport/README.md#active-runtime-follow-up-2026-10-21) identifies both through process ancestry and verifies the application at `0.1.2-nightly.20261021.3473`. No hash guard was weakened, older build substituted or verifier code changed. It also corrects the [Cursor policy mapping](../cursor-runtime-boundaries/README.md#active-application-recheck) previously attributed to the current application.

## Provider and persistence evidence

These rows summarize existing runtime records. This review runs no new model experiment.

| Coordinator | Evidence | Current boundary |
| --- | --- | --- |
| Codex in T3 | [Installed Help/Investigation, concrete delegation, continuation and opt-out](../catalog-discovery/README.md#fresh-codex-conversation); [manual compaction in both states](../conversation-compaction/README.md); [active continuation after manual service recovery](../conversation-recovery/README.md). | Bounded exercised paths. Writing verification is qualified in the compaction run. Automatic backend recovery failed before separate manual service recovery; general automatic restart, live-child recovery and unattended operation remain unverified. |
| Claude in T3 | [Configured cross-provider Investigation](../investigation-write-boundary/README.md); [exported active/inactive compaction observations](../conversation-compaction/README.md#claude-export-follow-up). | Exports are evidence from the other host, not a new Orbit execution. The inactive answer lacks a fresh source read; complete writing/package-identity and broader workflow checks remain qualified. |
| Cursor in T3 | [Installed discovery, exact capture and configured helper](../provider-discovery/README.md#installed-configuration-investigation); guided preservation of the short cited explanation and initial full task list. | Overall workflow remains incomplete for read scope, writing and stated recording limits. [Workspace controls](../cursor-runtime-boundaries/README.md) do not isolate response files from older runs in the same project folder. |
| OpenCode in T3 | Fresh catalog now exposes 457 models and `canRunChildTask: true`. Earlier no-model observations remain historical. | Availability prerequisite improved; execution, discovery, options and persistence have not been tested. No model was chosen or configuration changed. |
| Standalone providers and native distribution | Portable source listing and bounded T3 records above. | They do not certify standalone hosts, native slash registration or plugin distribution. |

## Finite remaining work

1. **Prepare the installed CLI prerequisites before using those tools.** The source setup and previously blocked checks are complete. Installed workflows use their discovered installation's separate `scripts` directory, currently `/home/ubuntu/.agents/skills/jstack-juan-mode/scripts` on Orbit. That directory still lacks Commander. The user-run command there is `bun install --frozen-lockfile`. Installing dependencies in the checkout does not prepare this global copy. No agent installation was performed.
2. **Select each further runtime claim before testing it.** OpenCode needs an explicitly selected test model. Cursor's read-scope and writing limits need a supported integration path, not repeated full Investigations. Automatic compaction/restart, cancellation/watch continuation, nested writers and complete per-route external dependency checks remain release work. Passing model validation or a prior pilot does not close them.

The current pure verifier assessment is complete in the follow-up above. It establishes fixture signing compatibility for that active build, not a new live endpoint, relay or receiving-agent result. Prior live pilots and their limits remain separate.

Benny's live pilot remains **deferred by the user** because no repository, Slack channel or issue tracker is selected. Its dormant pack is not missing source. Origin, automatic chain discovery and alternative native distribution remain separate product decisions. These deferred choices do not prevent the exercised daily-use paths, and this review does not approve them.

The stale current-count and no-compaction-evidence claims in `fidelity-status.md` are corrected by this assessment. That was an actionable documentation defect. No new shipped-skill implementation defect is established by these checks. The source CLI behavior and strict compilation now pass after prerequisite setup; this does not certify the unprepared installed copy or full live workflows.

## Reproduce

From the repository root, use the already-present CLI, reviewed external Unslop and the identified application executable. The corrected command below passed all 95 root tests. The initial failed command selected `0.0.46-nightly.20261003.2610` instead.

```sh
PYTHONDONTWRITEBYTECODE=1 \
JSTACK_SKILLS_CLI=/home/ubuntu/.npm/_npx/ac0ed6aa23b37c1e/node_modules/skills/dist/cli.mjs \
JSTACK_UNSLOP_SOURCE=/home/ubuntu/.agents/skills/unslop \
JSTACK_TEST_T3_RUNTIME=/home/ubuntu/.t3/runtime/versions/0.1.2-nightly.20261021.3473/t3 \
python3 -B -m unittest discover -s scripts/jstack -p 'test_*.py'
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s skills/jstack/jstack-setup/scripts -p 'test_*.py'
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s skills/jstack/jstack-juan-mode/scripts -p 'test_*.py'
node --test scripts/jstack/test_check_docs.mjs
node scripts/jstack/check_docs.mjs
python3 -B scripts/jstack/check_installation.py --installed-root "$HOME/.agents/skills" --json
```

Run `bun run test` and `bun run typecheck` from `skills/jstack/jstack-juan-mode/scripts` after manual frozen-lockfile setup. The recheck returns 112 tests passed and both strict projects compiled, exit 0 for each command. Omitting the root suite's runtime/CLI environment variables produces skips, not new compatibility evidence. The [existing census](../../coverage-audits/2026-10-18/inventory.py) accepts `--local-ref 110705c8525b365e784e58ba7fd7d3388e61a527` and the frozen source clone. Saved-map validation and preflight require a fresh complete capability capture through the [shared contract](../../../../skills/jstack/jstack-setup/references/t3-code.md), not an old catalog retained from this review.

## Daily-use example and retention

In an installed Codex/T3 conversation, ask: `/jstack-juan-mode investigate how this repository loads its configuration. Give source citations and do not change code.` Include temporary findings permission when needed for configured preflight. Review the returned evidence and any incomplete phase. Before a later watcher or Orchestrate task, satisfy its separate CLI prerequisites; this example does not require those tools.

This assessment changes research and status only. Saved models, installed packages, operational source, pins and the reviewed checkpoint are preserved. The frozen census and existing adaptation records support the coverage statements; no fresh full semantic audit or upstream fetch ran. Keep this report and existing reproductions, not raw catalogs, test transcripts, cloned fixtures or hash inventories. Failed and blocked results remain visible.
