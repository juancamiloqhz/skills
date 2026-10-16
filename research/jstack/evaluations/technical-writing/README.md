# Technical writing evaluation

Date: 2026-10-15. Merged baseline: `7490738e484e81824538ea75aab238b0090223a8`. Upstream pin: `11713c683fe4add4fd403ea880580abbc9e0875f`. This bounded evaluation covers the new standalone writing helper and its Juan-mode caller, not a complete documentation or PR workflow.

## Source and dependency assessment

[compare.py](compare.py) compares the complete upstream package with the local skill, both MIT notices, the whole mode entrypoint, unchanged mode support files, existing manifest pins and checkpoint, and the external Unslop dependency. [source-comparison.json](source-comparison.json) retains hashes and complete diffs. The parent inspected those diffs against the [adaptation record](../../adaptations/technical-writing.md). Mapping and packaging checks alone do not establish semantic fidelity.

The installed Unslop is from `cursor/plugins` and retains the pinned catalog's substantive rules, with editorial changes and an additional self-audit step. Its assessed SHA-256 is `c6d2572294d933a428211921069e9a248490e9b466ca59437cb4d9de248600ca`. It remains an external dependency; no installed skill was modified. Both versions carry `disable-model-invocation: true`. Explicit authoring-path reads here do not prove that every provider permits a catalog invocation. A blocked, missing or ambiguous dependency leaves the writing check incomplete.

## Fresh evaluation cases

Three independent native subagents received the new skill's explicit authoring path and only their task's fixture context. The `judgment and prose` role resolved to inherited model/effort, and all three used the executing Codex provider with `gpt-6-astra`, without overrides. These were fresh task contexts, not different-model reviewers. The skill-creator independent forward-testing procedure authorized the evaluations.

| Agent | Brief | Observed result |
| --- | --- | --- |
| `/root/writing_modes_eval` | Rewrite the mixed draft for a newcomer, an experienced user retrieving a note, a command lookup reader, and a reader asking why stores are explicit. Inspect source, use the supplied Unslop, and run only scratch CLI data. | Four distinct modes; unsupported claims removed; 26 recorded CLI invocations, including expected errors. |
| `/root/writing_pr_eval` | Describe the before/after title-validation change using the exact three-section repository template; provide a commit message, Python example, evidence and an unapplied writing-guidance proposal. | Accurate PR and one-line commit, repository formatting preserved, 10 fixture behavior checks passed. No forced Diátaxis mode for the PR. |
| `/root/writing_unavailable_eval` | Review the draft, findings only, with a catalog containing the new writing helper but no Unslop. No installed-skill access, CLI execution or edits. | Explicitly incomplete dependency check, with useful source-backed findings; no substitution, installation or false complete claim. |

The fixture is the existing Pocket CLI from the create-verification-skill evaluation. [before.py](fixtures/before.py) removes title stripping and blank-title rejection to provide a concrete fictional change. [context.md](fixtures/context.md) supplies maintainer intent, concurrency limits and repository indentation. [draft.md](fixtures/draft.md) deliberately contains unsupported claims, mixed document modes and invented jargon. It is test input, not documentation guidance.

## Outputs and parent assessment

The parent read every document and the findings report, checked claims against the fixture and supplied context, and replayed the runnable tutorial and PR checks in new temporary directories.

- [Tutorial](outputs/modes/first-note.md): a fresh-directory prerequisite, ordered steps and observed JSON. Both commands replayed with the exact expected note.
- [How-to](outputs/modes/retrieve-note.md): direct retrieval steps and missing-note recovery for an experienced reader.
- [Reference](outputs/modes/command-reference.md): source-backed flags, defaults, results and failures, with two-space multiline JSON.
- [Explanation](outputs/modes/explicit-data-directories.md): the supplied maintainer rationale and tradeoffs; no invented speed or server claim.
- [PR description](outputs/pr/pr-description.md): exactly the repository's three headings, factual before/after behavior, evidence links, compatibility and rollback limits. Its Python example parses and uses four spaces.
- [Unavailable-dependency findings](outputs/unavailable/result.md): review authority preserved and incomplete status visible.

[checks.json](checks.json) records the parent assertions and replay results. The parent reran the agent's PR verification script with only its temporary output root replaced; all 10 assertions passed again. [parent-replay.json](outputs/pr/parent-replay.json) retains the actual commands and outputs. This tests the factual support for the generated writing, not a new jstack runtime implementation.

The [mode report](outputs/modes/result.md), [26-command evidence](outputs/modes/command-evidence.json), [PR report](outputs/pr/result.md), [PR command evidence](outputs/pr/evidence.json), and [skill identities](outputs/pr/skill-identities.json) retain the observed execution. Agent exploratory failures remain recorded: an incorrect manifest path, truncated search, absent temporary upstream checkout, and adaptation report not yet written by the parent. No conclusion relies on those failed reads; the parent performed the complete source comparison separately.

The agents proposed adding “coordination membrane” to Unslop's abstract-metaphor examples. Neither proposal was applied. The PR agent's exact diff text is serialized in [writing-guidance-proposal.json](outputs/pr/writing-guidance-proposal.json) to retain whitespace without adding trailing-space errors. The two PR command logs are likewise serialized as JSON strings to preserve literal whitespace test inputs. Only evidence links in the copied PR description and report were changed; their substantive text is unchanged. Reports refer to their original temporary execution directories; generated scratch data is not retained. Source copies and text evidence are retained.

## Reproduction and checks

From the repository root:

```sh
python3 -B research/jstack/evaluations/technical-writing/compare.py
python3 -B scripts/jstack/test_skill_packaging.py
python3 -B /home/ubuntu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/jstack/jstack-technical-writing
```

The comparison expects the shared upstream cache and assessed external Unslop path; both can be overridden with flags. Reproduce the tutorial with a copied fixture in a fresh temporary directory. The retained PR verification runner uses its original absolute fixture and output paths and refuses to overwrite existing data. Copy it to a fresh temporary directory and replace only its output root before replaying; do not run it over the original evidence directory.

Validation includes the real upstream-manifest loader, four packaging tests, skill frontmatter validation, changed-Markdown lint, relative evidence links and whitespace checks. Final results are recorded in [validation.json](validation.json). The initial lint run found MD041 violations in the intentionally heading-free rewrite/findings and the two PR-template artifacts. Those four files are linted with only MD041 disabled; other files use the repository configuration. Raw outputs are preserved. Model resolution code and configuration schema were not changed, so their unrelated test suites were not rerun.

## Limits

These cases establish bounded behavior from explicit authoring paths. They do not establish installed catalog discovery, cross-provider invocation, complete Juan-mode routing, or all writing tasks. Language quality and mode separation were human-readable judgments by the parent agent, not a deterministic score or a claim of perfect writing. No performance benchmark, concurrent storage guarantee, or future product feature was inferred.

The global model configuration retained SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`. Existing source pins, reviewed checkpoint, model files and installed skills stayed unchanged. Merging, manual installation and the pending No-comments/Comment Sicko work remain separate.
