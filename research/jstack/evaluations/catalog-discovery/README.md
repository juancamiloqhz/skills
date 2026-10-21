# Complete catalog discovery

On 2026-10-19, Skills CLI 1.7.2 discovered every shipped skill from a fresh local Git clone of `f0ce7692d7925cf3ecaaf56b396b5d102fa8ebec`. This closes a distribution check. It does not establish provider invocation or workflow correctness.

## Executed checks

The [integration test](../../../../scripts/jstack/test_catalog_discovery.py) uses an already-present CLI, disables telemetry, and runs `add --list` only. It clones the committed repository with `--no-local`, so Git does not borrow objects from the source checkout. Package, automation or manifest edits must be committed before running it. Temporary files are removed when the test ends.

Default, full-depth and full-depth wildcard listings each contain exactly the 60 expected identities: 57 jstack skills and three other repository skills. There are no duplicate identities or exposed Benny procedures. Expected jstack identities come from the manifest; the full catalog comes from the cloned entrypoints. The test compares catalog rows, not names that happen to appear in descriptions. A before/after file-content snapshot, including Git metadata, shows that listing leaves the clone unchanged.

A negative control renames `jstack-bro` inside the disposable clone. The next listing loses that identity and gains only the replacement identity. This confirms that the check detects a packaging error and reads this clone. No user installation is altered.

One integration test passes, containing three listing variants and the negative control. The four existing package checks and six installation-checker tests also pass. Documentation checking reports zero problems. This run used Orbit/Linux, Node and Python through the Codex harness in T3 Code. It did not start a fresh model session or delegate to another provider.

## Installed prerequisite

The read-only installation checker compared the same source revision with `/home/ubuntu/.agents/skills` on Orbit. It returned exit 1: **28 matching, 12 missing, 17 different**. The missing set is the twelve later additions, from Bro and Ketchup through Make bot UI. Differences also affect existing packages, including Juan-mode, How and Why. The agent left those files untouched; the user subsequently reinstalled the skills manually.

The earlier user-reported matching installations covered the then-current 45-package release. They do not certify the current 57-package source. After the user reinstalled, the agent reran the checker against source `c074c923b93a9434aa09618ec6c8f5d3af39948f`: **57 matching, 0 missing, 0 different**, exit 0. No current omarchy-mac installation check was run in this assessment.

## Reproduce

Use a trusted, already-present Skills CLI executable. Without the environment variable, unittest explicitly skips this optional integration test; a skip is not discovery evidence.

```sh
JSTACK_SKILLS_CLI=/path/to/skills/dist/cli.mjs \
python3 -B -m unittest discover -s scripts/jstack -p test_catalog_discovery.py -v
python3 -B -m unittest discover -s scripts/jstack -p test_skill_packaging.py -v
python3 -B -m unittest discover -s scripts/jstack -p test_check_installation.py -v
node scripts/jstack/check_docs.mjs
python3 -B scripts/jstack/check_installation.py --installed-root "$HOME/.agents/skills"
```

The last command reports the installation as it exists when run. It returns exit 1 for a completed comparison with differences; the post-update Orbit check returned exit 0. The cached CLI used here was `/home/ubuntu/.npm/_npx/ac0ed6aa23b37c1e/node_modules/skills/dist/cli.mjs`. This test does not download it, exercise GitHub transport, install packages, or validate executable permissions.

## Remaining provider evidence

| Check | Current evidence and next condition |
| --- | --- |
| Skills CLI source discovery | Passed on Linux with CLI 1.7.2, independently of model providers. |
| Installed Codex entrypoints and dependency calls | Post-update file equality and the bounded fresh-thread Help/Investigation trial below pass. This does not test every entrypoint or catalog registration mechanism. |
| Claude coordinator behavior inside T3 | User exports establish configured Claude-to-Codex Investigation and [active/inactive state retention after manual compaction](../conversation-compaction/README.md#claude-export-follow-up). The inactive follow-up has no fresh source-read evidence. Full installed-catalog, dependency and workflow coverage remain open. |
| Cursor behavior inside T3 | The [scoped capture repeat](../provider-discovery/README.md#scoped-capture-and-integrated-repeat) passes exact current capture, preflight and read-scope review. A subsequent integrated run resolves the saved model, completes one Codex/high explainer and preserves the technical answer with light edits. Directory listings, partial mode-read evidence and an unverified host task list keep that full protocol qualified. Native invocation, automatic dependency discovery, persistence and broader workflow coverage remain open. |
| OpenCode behavior inside T3 | CLI 2.1.1 is installed, but the live T3 catalog exposed no models during the [provider prerequisite check](../provider-discovery/README.md). No model execution was attempted. |
| Standalone providers and plugin distribution | Not established by T3 or CLI listing. Portable skill distribution remains the approved choice. |
| Later-task activation, opt-out and wider persistence | The [compaction follow-up](../conversation-compaction/README.md) records both states after manual Codex/T3 and Claude/T3 compaction, with the Claude inactive source-read limitation preserved. A [manual Codex service recovery](../conversation-recovery/README.md) retained active routing and completed delegation after automatic backend recovery failed. Automatic compaction, automatic restart, inactive-state recovery and other providers remain open. |
| Benny live pilot | Deferred by the user because no target repository, Slack channel or tracker is available. The pack remains inactive. |

After a manual update, an example discovery check is: “Use `jstack-juan-help` to explain how to start an investigation. Report the installed path you loaded.” That checks one entrypoint and its guide. Follow with an authorized bounded workflow to test actual dependency calls and configured delegation; merely naming a skill is insufficient. A fresh child can test child behavior, but does not prove top-level coordinator persistence.

## Fresh Codex conversation

The user opened [Start an Investigation with Juan Help](t3-thread://v1/0fdfffb0-c122-496f-a9df-cd8a37238812), a new top-level T3 conversation using Codex `gpt-6.1-sol`. We inspected its recorded commands, tool calls, child results and final answers, not only the pasted response. Help ran on 2026-10-19; Investigation, a later task and opt-out ran on 2026-10-20. The source checkout was `c074c923b93a9434aa09618ec6c8f5d3af39948f`, whose operational files match the discovery baseline. The thread's app workspace was a scratch directory; investigation commands explicitly targeted `/home/ubuntu/Dev/skills`.

| Turn and timeline positions | Observed behavior |
| --- | --- |
| Help, 0–8 | Found and read installed `jstack-juan-help`, external Unslop, bundled prompting/recipes and the installed Investigation playbook. Returned the expected prompt without starting investigation or delegation. This establishes filesystem discovery and loading, not native slash-command registration. |
| Explicit Juan-mode invocation, 9–36 | Loaded activation, How and setup contracts; used the four-step Investigation plan and read-only throughput checkpoint. Validated the global configuration and launched one How explainer through T3. Parent and child inspected the checker, the parent executed it, and the final answer cited source and preserved limitations. Git status/diff checks showed a clean repository. |
| New task without reinvocation, 37–52 | Investigated configuration precedence using the same playbook plan, fresh preflight and another configured explainer. Executed read-only locator cases for project, environment and explicit paths. Repository status stayed clean. |
| Explicit opt-out, 53–55 | Replied “Juan-mode is off. No new task started.” The turn contained no tool or delegated-task activity. This verifies acknowledgement and immediate inactivity, not behavior on a subsequent task. |

Both explainer dispatch receipts report `codex / gpt-6.1-sol / reasoningEffort=high / serviceTier=default`, matching the saved concrete `how explainer` selection plus the same-model inherited service tier. The coordinator catalog reported low effort. Thus these calls demonstrate the configured high-effort override, not inherited-effort routing or cross-provider dispatch. Both child results and completion notifications are visible before the corresponding final answers. The first task ran the real installation checker and reported 57 matching packages; the second distinguished executed locator probes from inspected tests. No application or model configuration edits were requested or observed.

The first investigation initially passed an empty catalog to the resolver and received a JSON parse error. It corrected the catalog transfer and obtained successful resolution and preflight before delegation. Record that recovered input failure rather than claiming an error-free run. File-creating fixture tests were deliberately not executed under the user's no-file-modification instruction. Git cleanliness supports the repository boundary; it is not a filesystem-wide write audit.

This original trial supports explicit activation, one later-task continuation, configured same-provider delegation and opt-out acknowledgement for this Codex/T3 session. The [2026-10-20 follow-up](../conversation-compaction/README.md) adds post-opt-out task behavior and observed state preservation across two actual manual compactions in the same conversation, including resumed preflight and completed delegation when active. The [manual service-recovery trial](../conversation-recovery/README.md) adds active continuation after automatic backend recovery failed. These checks do not certify all 23 playbooks, every dependency, other coordinating providers, automatic compaction, automatic restart or standalone hosts. Keep the thread reference and concise assessments; do not commit raw transcripts or capability catalogs.

## Fidelity and retained evidence

This is repository maintenance tooling, with no corresponding upstream skill procedure. The final change leaves all shipped skills, automation files and `upstream.json` byte-identical to the evaluated merge. Their recorded per-package source pins and adaptation records remain applicable. No upstream wording, structure, checkpoint or runtime policy changes. The [coverage audit's distribution assessment](../../coverage-audits/2026-10-18/README.md#agents-automation-distribution-and-external-dependencies) remains the boundary: portable discovery is separate from upstream plugin packaging and provider execution. Direct comparison with `pstack/plugin.json` and `pstack/docs/harness/claude-code.md` at audit pin `0148b78c56c72a1b8412055913c79f767095b217` confirms that this test covers neither the namespaced plugin entrypoints nor its provider tool/model translations. Those remain distinct from the approved `jstack-` portable catalog; no new deviation is introduced. Keep only this report and the reproducer; temporary clones and routine CLI output are not retained.
