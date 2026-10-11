# Verification generator evaluation

Executed on 2026-10-10 against the [generator](../../../../skills/create-verification-skill/SKILL.md). The [results record](results.json) contains source/output hashes and observed outcomes. The [Pocket fixture](fixture/README.md) is a Python-standard-library CLI with creation, reads and validation errors; it has no services or credentials.

## Cases and observations

| Case | Execution | Observed result |
| --- | --- | --- |
| Generate for Pocket | A fresh Codex subagent read the generator and a standalone fixture checkout, authored a project skill, and ran its instructions | Generated `verify-pocket` with a helper, three feature recipes and evidence; 11 real CLI calls passed |
| Reuse in another checkout | A different fresh subagent received only the generated skill and another fixture checkout, with instructions not to read previous evidence | Ran the documented command unchanged; 11 new CLI calls passed; new proof retained |
| Detect wrong behavior | Parent changed `show` in a third fixture checkout to return an incorrect body while still exiting zero | Generated verifier exited 1 with `Show mismatch across processes`; failure proof survived scratch cleanup |
| Documentation-only repository | A fresh subagent received the generator and a README-only checkout with no executable product | Generated nothing and left the working tree clean |

The parent inspected the reports and verified that scratch paths were absent after success and failure, evidence reports remained, application files were unchanged in generation and reuse, and copied verification files were unchanged by the consumer. No skills or dependencies were installed, and no provider settings or external services were changed.

## What the generated skill proved

The public CLI checks covered version/help, empty listing, invalid IDs and blank titles, two note creations, a subsequent show and list, and errors against populated data. Assertions checked title trimming, bodies, sequential IDs, persisted JSON, reads across separate processes, and the absence of writes from reads or rejected inputs. The helper captured argv, stdout, stderr, exit statuses and state observations, then removed only its owned scratch directory.

The repeatable invocation was:

```sh
python3 .agents/skills/verify-pocket/scripts/verify.py
```

The consumer ran it from a different checkout without editing the generated source or relying on an old temporary path. A doctor-only invocation was also executed during generation. An initial evaluator inspection expected 13 commands; inspection corrected that count to the 11 actually logged. No generator change was required by the behavioral runs.

## Reproduce the evaluation

1. Copy `fixture/` to a disposable repository and make a separate worktree for each run. Keep the generator source outside those worktrees.
2. Give a fresh agent this request, replacing the paths with the actual locations: "Use the skill at GENERATOR/SKILL.md to create a verification skill for Pocket in FIXTURE. Do not modify the application, install anything, change provider settings, use external services, commit, push, or delegate. Return the generated paths, actions, evidence, cleanup outcome and limitations."
3. Copy the generated project-local skill into another clean fixture checkout. Give another fresh agent only that skill and checkout, asking it to verify Pocket without editing files or reading earlier reports. Require newly generated evidence.
4. In a third checkout, insert `result = dict(result, body='INJECTED REGRESSION')` immediately before output when `args.command == 'show'`. Run the generated verifier and inspect its failure status, evidence and cleanup. The mutation must not enter the source fixture.
5. For the no-app case, give the generator a separate repository containing only a README stating that it holds Markdown notes and has no executable interface. Check that the agent generates no app skill and changes no files.

Inspect evidence rather than accepting only agent summaries. Generation is nondeterministic; subsequent output hashes may differ. The saved hashes identify this run, not required golden output.

## Limits

These are focused functional evaluations, not a comparative benchmark. No without-skill baseline was run. They demonstrate a generated CLI recipe, independent reuse, one injected output regression and a no-app boundary. They do not establish browser, API, library, desktop, mobile, interactive terminal, cross-provider or automatic-discovery behavior. T3 browser execution was not part of this trial.

The generated Pocket recipe does not cover corrupt storage, concurrent writers, filesystem faults, forced process termination, or the complete argument-error matrix. The failure injection tested an already-generated verifier; generator behavior against a broken starting application remains untested. Raw proof was inspected locally; this repository retains the small outcome/hash record and fixture instead of full agent transcripts or generated skills in the installable tree.
