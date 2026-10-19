# Benny dormant pack evaluation

2026-10-19, Orbit/Linux, local Python and Node, Skills CLI 1.7.2. Source pin and per-file differences: [adaptation record](../../adaptations/benny.md). No Slack, tracker, scheduler, model configuration, installed skill or target application was changed. Temporary Git checkouts were removed by the tests.

## Results

- **Copy and refresh:** eight offline tests pass. Preview writes nothing; a fresh copy reproduces every pack byte; repeat copy adds nothing; configuration and destination-only files survive. A differing file blocks all additions, including on apply. Incomplete source packs, symlinked paths, overlapping trees and a file in a required directory position are rejected; a conflicting destination directory is preserved. The helper is for a single setup writer, not hostile concurrent filesystem mutation or transactional rollback after disk failure.
- **Real discovery and fresh checkout:** one optional integration test passes with the already-present Skills CLI. The fixture commits actual jstack dependencies and external Unslop, clones them, removes the source, and runs list-only discovery from the clone. Default, full-depth and wildcard listings include the dependencies and hide all three Benny procedures. Explicit named selection and the internal-skills environment override expose them as expected. A target-style `.agents/automations/benny/` copy remains directly readable without adding procedures to the listing. No installation or lockfile is created. This proves local file/discovery access, not fresh-provider activation or complete runtime dependency closure.
- **Maintenance:** all 17 upstream checker tests pass, including mapped pack and license changes, deleted upstream packs, dirty-pack rejection and missing attribution. Existing no-change caching, history and full-path detection tests pass. Normal skill mappings remain 57; Benny has its own automation-pack mapping.
- **Compatibility:** all four normal skill-packaging tests and six installation-checker tests pass. Documentation checking reports zero problems.
- **Fidelity:** all 12 source files plus the unchanged MIT license are present. The three procedures retain 8/10/15 phases. All four references retain substantive content. Full source diff reviewed; runtime changes are listed in the adaptation record. Relative pack links and both canonical `ts` prompt examples validate.

## Reproduce

From the repository root:

```sh
python3 -B -m unittest discover -s scripts/jstack -p test_benny_pack.py -v
python3 -B -m unittest discover -s scripts/jstack -p test_check_upstream.py -v
node scripts/jstack/check_docs.mjs
```

The first command explicitly skips real CLI discovery unless these paths are supplied. Use an already-reviewed CLI and external Unslop directory; this test does not download or install either:

```sh
JSTACK_SKILLS_CLI=/path/to/skills/dist/cli.mjs \
JSTACK_UNSLOP_SOURCE=/path/to/unslop \
python3 -B -m unittest discover -s scripts/jstack -p test_benny_pack.py -v
```

The tested CLI was the cached `skills@1.7.2` executable and Unslop was the existing external package at `~/.agents/skills/unslop`. The fixture supplies jstack-setup alongside How, Why, TDD and the six source-required principles because their shared helpers use it. Tests disable CLI telemetry and use `--list` only.

## Use this unit

To preview a copy into an existing target repository:

```sh
python3 scripts/jstack/copy_benny_pack.py --target-root /path/to/project
```

After reviewing the destination and with setup authorized, add `--apply`. Exit 1 means managed-file conflicts need manual diff/merge; exit 2 means an incomplete copy/preflight. Inspect and rerun after an interrupted apply; never overwrite a local edit to make the command pass. This helper copies only the pack and creates no configuration, installation or live task. Continue by reading the copied `.agents/automations/benny/FOR_AGENTS.md`.

Example request: “Read `automations/jstack/benny/FOR_AGENTS.md` and prepare an inactive Benny copy for my test project. Show the missing dependencies before enabling anything.”

## Next evidence

Implement and test the intake/adapter contracts with synthetic events: fixed root coordinates, authentication, duplicate delivery, ambiguous writes and tracker compensation. Fresh-provider dependency loading remains a setup gate before any live pilot. A target repository, workspace/channel, tracker, control adapter, model contexts and enforceable child isolation still need selection and proof. Neither successful copying nor scheduler dispatch establishes working triage/reproduction.
