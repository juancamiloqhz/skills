# Portable name migration evaluation

Date: 2026-10-15. Baseline: `3c2e32c17ea6a08900af822fe205703e47be0072`. Scope: all 38 shipped packages and their operational callers. This evaluates package identity and preserves the existing workflow evidence; it does not rerun every orchestrator or establish installed-provider discovery.

## Checks

The four executable suites total 50 tests. [Recorded test output](tests.json).

- All 38 packages pass the Codex skill format validator. [Validation output](validation.json).
- The four [packaging tests](../../../../scripts/jstack/test_skill_packaging.py) check frontmatter/directory/manifest identity, explicit callers and installation commands, package-local links, and chooser prompts.
- The 16 preflight tests pass, including a new case rejecting legacy `setup-jstack` and upstream `setup-pstack` before executing their resolver. Existing inheritance, panel order, project/global precedence and full-configuration failure cases pass.
- All 19 model tests and 11 upstream-checker tests pass. The model resolver and its tests are byte-identical to the pre-migration files. The user's model configuration was not modified.
- Current research file links and Markdown lint pass. Historical evidence is not rewritten or counted as current link/identity validation.

## Exact source comparison

[compare.py](compare.py) reads the manifest through the real checker, verifies every upstream mapping field and checkpoint against the baseline, and compares each final file with its exact pinned source where that source exists. It also compares every package file with its pre-migration counterpart. All 128 files retain their package-relative location; all 38 licenses match both the baseline and pinned upstream notice. Missing upstream playbooks and existing local runtime additions remain visible in the inventory. They are not introduced or resolved by this rename.

[comparison.json](comparison.json) contains the original/new names, local paths, source paths, pins, file hashes and equality results. The 35 newer pins remain `11713c683fe4add4fd403ea880580abbc9e0875f`; setup and the two verification helpers remain at `ccb5507cec1546dc88135c1139c811e6c59115ba`. The reviewed checkpoint remains `4bf3e083c6dec126e254f96181b84a105b6e3e70`.

Reproduce the comparison without fetching or advancing a checkpoint:

```sh
python3 -B research/jstack/evaluations/skill-names/compare.py \
  --upstream /home/ubuntu/.cache/jstack/upstream/upstream.git \
  --diff-dir /tmp/jstack-name-review
python3 -B scripts/jstack/test_skill_packaging.py
python3 -B skills/jstack/jstack-juan-mode/scripts/test_preflight.py
python3 -B skills/jstack/jstack-setup/scripts/test_models.py
python3 -B scripts/jstack/test_check_upstream.py
```

Full migration and pinned-source diffs are generated in the selected temporary directory. They need not duplicate the source in version control. The retained [normalized residual diff](normalized-residual.json) removes only literal identity translations to expose all remaining edits. Nine files have residual differences, assessed as follows:

| Files | Exact difference and purpose |
| --- | --- |
| Mode, Architect and Figure-it-out entrypoints | Record the selected name/path and resolve duplicate identities from source metadata. Makes the user's package-identity requirement observable; unresolved ambiguity remains unavailable. Architect's final rerun call also gains bold markup around the exact catalog name. |
| Mode configuration reference | Clarifies that saved roles retain names such as `how explorer` and `swarm workers`; prevents a caller from prefixing schema keys. |
| Preflight tests | Adds rejection-before-execution coverage for old jstack and upstream setup identities. |
| Setup entrypoint | Changes two title-case helper labels into exact catalog names; reversing the prefix leaves lowercase names. No setup behavior changes. |
| Three chooser metadata files | Adds visible Jstack labels; default prompts invoke their renamed package. |

All other content differences reduce exactly to name translations. The preflight's executable identity check now requires `jstack-setup`; its algorithm is otherwise unchanged. Prior runtime, authorization and deliberate-behavior differences remain owned by each manifest-linked adaptation record and the [fidelity status](../../fidelity-status.md). Prefix translation is the new user-approved deviation from pstack. Source names and procedures are preserved for future comparison.

## Bounded discovery exercise

One fresh native Codex subagent inherited the parent model and effort with no target override. Task name: `/root/naming_discovery_eval`. It received the current router path, this scenario and three complete case catalogs:

> Active mode user asks: "How does the configuration lookup work? Please explain it without changing anything." Stop at dependency selection before executing an investigation, resolving model settings or dispatching children. Select the next helper and its setup dependency if possible, read selected entrypoints, and report exact names/paths and unresolved requirements. Use only the supplied catalogs. Write only the assigned temporary result file.

Catalogs: [present](present.json), [absent](absent.json), [ambiguous](ambiguous.json). [Actual result](discovery-result.md).

The present case selected and read `jstack-how` and `jstack-setup`, including the shared investigation contract. The absent case reported a missing `jstack-how` and gave its exact manual install command. The ambiguous case declined to select between two same-name entries without source metadata. Legacy entries were not selected. The evaluator also reported the fixture's missing external Unslop dependency.

The catalogs record the actual paths used. Legacy fixtures contained baseline SKILL.md files; the unidentified-copy fixture contained the current `jstack-how/SKILL.md`. Those scratch copies are reconstructible from the baseline and comparison hashes. All cases ran in one evaluator context, not three isolated trials. This is bounded instruction-following evidence, not a measured reliability rate, a real host-catalog refresh or full workflow execution.
