# Complete catalog discovery

On 2026-10-19, Skills CLI 1.7.2 discovered every shipped skill from a fresh local Git clone of `f0ce7692d7925cf3ecaaf56b396b5d102fa8ebec`. This closes a distribution check. It does not establish provider invocation or workflow correctness.

## Executed checks

The [integration test](../../../../scripts/jstack/test_catalog_discovery.py) uses an already-present CLI, disables telemetry, and runs `add --list` only. It clones the committed repository with `--no-local`, so Git does not borrow objects from the source checkout. Package, automation or manifest edits must be committed before running it. Temporary files are removed when the test ends.

Default, full-depth and full-depth wildcard listings each contain exactly the 60 expected identities: 57 jstack skills and three other repository skills. There are no duplicate identities or exposed Benny procedures. Expected jstack identities come from the manifest; the full catalog comes from the cloned entrypoints. The test compares catalog rows, not names that happen to appear in descriptions. A before/after file-content snapshot, including Git metadata, shows that listing leaves the clone unchanged.

A negative control renames `jstack-bro` inside the disposable clone. The next listing loses that identity and gains only the replacement identity. This confirms that the check detects a packaging error and reads this clone. No user installation is altered.

One integration test passes, containing three listing variants and the negative control. The four existing package checks and six installation-checker tests also pass. Documentation checking reports zero problems. This run used Orbit/Linux, Node and Python through the Codex harness in T3 Code. It did not start a fresh model session or delegate to another provider.

## Installed prerequisite

The read-only installation checker compared the same source revision with `/home/ubuntu/.agents/skills` on Orbit. It returned exit 1: **28 matching, 12 missing, 17 different**. The missing set is the twelve later additions, from Bro and Ketchup through Make bot UI. Differences also affect existing packages, including Juan-mode, How and Why. They have not been overwritten or classified as safe to overwrite; inspect any intentional local edits before updating.

The earlier user-reported matching installations covered the then-current 45-package release. They do not certify the current 57-package source. No current omarchy-mac installation check was run in this assessment.

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

The last command reports the installation as it exists when run. It is expected to fail until that installation matches. The cached CLI used here was `/home/ubuntu/.npm/_npx/ac0ed6aa23b37c1e/node_modules/skills/dist/cli.mjs`. This test does not download it, exercise GitHub transport, install packages, or validate executable permissions.

## Remaining provider evidence

| Check | Current evidence and next condition |
| --- | --- |
| Skills CLI source discovery | Passed on Linux with CLI 1.7.2, independently of model providers. |
| Latest installed Codex catalog and dependency calls | Blocked by the observed stale installation. Refresh manually, check file equality, then test a fresh session. |
| Latest Claude Code, Cursor and OpenCode coordinator behavior inside T3 | Not exercised in this run. Each needs its own installed catalog, dependency, configured dispatch and activation/opt-out evidence. |
| Standalone providers and plugin distribution | Not established by T3 or CLI listing. Portable skill distribution remains the approved choice. |
| Compaction, resume and wider persistence | Prior bounded trials remain valid within their recorded scope; the full provider matrix remains open. |
| Benny live pilot | Deferred by the user because no target repository, Slack channel or tracker is available. The pack remains inactive. |

After a manual update, an example discovery check is: “Use `jstack-juan-help` to explain how to start an investigation. Report the installed path you loaded.” That checks one entrypoint and its guide. Follow with an authorized bounded workflow to test actual dependency calls and configured delegation; merely naming a skill is insufficient. A fresh child can test child behavior, but does not prove top-level coordinator persistence.

## Fidelity and retained evidence

This is repository maintenance tooling, with no corresponding upstream skill procedure. The final change leaves all shipped skills, automation files and `upstream.json` byte-identical to the evaluated merge. Their recorded per-package source pins and adaptation records remain applicable. No upstream wording, structure, checkpoint or runtime policy changes. The [coverage audit's distribution assessment](../../coverage-audits/2026-10-18/README.md#agents-automation-distribution-and-external-dependencies) remains the boundary: portable discovery is separate from upstream plugin packaging and provider execution. Direct comparison with `pstack/plugin.json` and `pstack/docs/harness/claude-code.md` at audit pin `0148b78c56c72a1b8412055913c79f767095b217` confirms that this test covers neither the namespaced plugin entrypoints nor its provider tool/model translations. Those remain distinct from the approved `jstack-` portable catalog; no new deviation is introduced. Keep only this report and the reproducer; temporary clones and routine CLI output are not retained.
