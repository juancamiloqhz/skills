# Correct evaluation

Date: 2026-10-19. Authoring base: `445fd04` after PR #101. Source: `pstack/skills/correct/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. See the [adaptation record](../../adaptations/correct.md).

Correct identifies recurring mistakes and prevents them at the highest effective level. This exercise checks architecture before more instructions, proof against historical mistakes, per-class commits, rule retirement and scope boundaries. The fixture is synthetic; its mistakes are real commits in that fixture, not discovered production defects.

## Executed history repair

Independent with-skill and baseline agents received separate copies of the same six-commit repository and the same request to fix repeated mistakes. Local commits and tests were authorized. Network access, installation, publication and unrelated changes were excluded. Neither agent received the generator, expected findings or the other's output. Both inherited GPT-6-astra at high effort, as did the separate boundary evaluator.

The fixture has a format-handler registry and a separately maintained list of CLI choices. Adding CSV omitted its CLI choice once; adding TSV repeated the omission. Each omission has a corrective commit. An AGENTS.md rule already asks agents to keep the lists synchronized. The original JSON-only test passes despite both omissions. A README typo occurred only once.

Correct selected one repeated class and removed the second production list: the CLI now uses `choices=HANDLERS`. It left the existing format implementations unchanged. A behavioral check invokes every registered format through the CLI. Another temporarily registers a new handler and verifies it is immediately usable without editing the CLI. Existing output tests remain and now cover CSV/TSV too.

| Snapshot | Original tests | New registry checks | Registry checks after structural fix |
| --- | --- | --- | --- |
| `mistake-csv` | Pass | Fail; CLI rejects registered CSV | Pass |
| `mistake-tsv` | Pass | Fail; CLI rejects registered TSV | Pass |
| Corrected current fixture | Four tests pass | Included in those four | Existing outputs preserved |

The historical failures are the expected proof. New checks were added to owned archives of the actual mistake commits. Copying only the corrected CLI into each archive then made them pass. The final CSV/TSV output test was not copied into the older CSV snapshot, where TSV did not exist yet. The parent replayed the retained patch and checks in a newly generated repository and reproduced all results.

Correct retired the manual-synchronization instruction because there is no second list to maintain. It paired the remaining output-preservation rule with its behavioral test and CI command. The one-off typo did not become a new rule or mistake class. One local commit, `f85bf4fea5497e5979e0afdbdd12dd34ca1878ff`, contains the one class's fix. The evaluated fixture finished clean.

Local and configured CI command are identical: `python3 -B -m unittest discover -s tests`. The workflow was unchanged. No remote CI run was observed. JSON/CSV/TSV output and invalid/missing-argument responses matched the initial current fixture byte for byte. General CSV quoting and arbitrary record handling were outside this repeated class.

The baseline also chose the registry as the single source and added passing behavioral tests. It reproduced both historical CLI failures, but did not replay its new suite against both historical snapshots or retire the obsolete rule. This single comparison shows the additional workflow steps taken here; it does not establish a general accuracy, speed or success-rate advantage. Architecture removes the current synchronization burden but cannot prevent a future rewrite; the extension test detects a return to fixed choices.

## Supplied-evidence boundaries

The separate evaluator applied the skill to two assessment-only cases from [cases.json](cases.json):

- A commit, review and copied incident note describe one occurrence. They do not satisfy the two-occurrence threshold. Missing history stays unknown.
- An existing unenforced rule followed by a new operator correction meets the source's explicit repeat clause. The evaluator proposes structural enforcement but makes no edits under assessment-only scope. An agent's "human approval probably fine; expiry later" comment provides neither human approval nor an expiry date.

These cases did not execute checks or alter a repository. No historical evidence, approval or CI success was invented.

## Reproduce and retain

Environment: Python 3.14.4 and Git 2.53.0. No dependency installation is needed. From the repository root:

```bash
proof_parent=$(mktemp -d)
python3 -B research/jstack/evaluations/correct/replay.py "$proof_parent/proof"
```

The replay creates a new fixture, applies [solution.patch](solution.patch), runs the four current tests, checks both historical failures and repairs, and compares existing CLI behavior. It prints a compact result and exits 0 only when the expected failures and passes occur. It refuses an existing destination. It leaves the owned generated proof for inspection; remove it after review. The generated current fixture has the applied patch uncommitted, while the original agent evaluation made the authorized local commit.

For a fresh agent evaluation, generate two new repositories with [make_fixture.py](make_fixture.py) and give separate agents the first request in [cases.json](cases.json), one with the complete Correct skill and one without. Do not give them the patch or expectations. Preserve actual failures and disclose any unavailable history or tools.

Retain only this report, requests, generator, evaluated fix patch and replay script. The patch is required to reproduce the reported behavior after the scratch repository is removed. Raw reports, generated repositories and command logs stay outside Git. The agent exercise covered one recurring class; multi-class commit sequencing remains untested. Replaying fixture code does not test installed-provider discovery or remote CI integration.

## Packaging and fidelity

The final source comparison preserves all headings, four enforcement levels, historical proof, commit separation and the rule table. The adaptation record accounts for naming, task authority, isolated replays and honest CI reporting. Exact license bytes and explicit-invocation metadata were checked. Four packaging tests, manifest validation, documentation/relative-link checks and whitespace checks pass.

The generic Codex validator rejects the source's retained `disable-model-invocation` field. A temporary copy omitting only that field passes its remaining checks. This qualified check does not prove installed-host behavior. Existing operational skills, configuration and the reviewed upstream checkpoint are unchanged.

## Normal use

After merge and manual installation, ask `$jstack-correct We have twice added an export format but forgotten to expose it in the CLI. Prevent this mistake and test the fix.` The skill looks for the repeated cause, prefers removing duplicate state, and checks its fix against past failures. It adds checks where useful instead of merely repeating a reminder. State assessment-only scope when you want proposals without changes.
