# Verification helper restoration

This correction follows merged PR #32 at `99932fdba316c1be3702ef497a64f913a19d292d`. Both helpers retain their original pstack pin `ccb5507cec1546dc88135c1139c811e6c59115ba`.

The generator again ships all three worked example files and keeps its six output requirements inline within the original five stages. Maintenance again runs one read-only source child per feature, reconciles their findings and drives the app only from the coordinator. It retains upstream's evidenced unreachable result and separates product regressions from independently proven verification corrections.

Automatic project-local Claude linking remains an intentional jstack addition, explicitly [reaffirmed by the user](../../decisions.md#automatic-claude-linking-2026-10-14). It applies regardless of the executing provider. The fidelity policy and adaptation record now preserve that decision for future work.

## Source accounting

[compare.py](compare.py) inventories all five upstream files and verifies both MIT notices. [source-comparison.json](source-comparison.json) records exact hashes and unified differences. All three example files are byte-identical to upstream. The parent inspected every entrypoint difference. [Generator](../../adaptations/create-verification-skill.md) and [maintenance](../../adaptations/maintain-verification-skill.md) records account for each remaining runtime, authority and packaging difference, the removed output-contract summary and the new source-reader execution reference.

```sh
python3 -B research/jstack/evaluations/verification-restoration/compare.py > /tmp/verification-source.json
cmp research/jstack/evaluations/verification-restoration/source-comparison.json /tmp/verification-source.json
```

Manifest context paths now track the helpers' actual dependencies. Pins, reviewed checkpoint, deferred decisions and historical evaluations are unchanged. The saved model file also remains unchanged; no installation or schedule changes are included.

## Fresh generation and independent reuse

The generation evaluator received the restored skill and the existing [Pocket fixture](../create-verification-skill/fixture/README.md), copied to a fresh temporary directory. It authored the [six-file verification package](outputs/generation/SKILL.md), created its relative Claude link and ran ten real CLI commands. Assertions checked exact output, persisted notes, read-only paths, rejected commands and source preservation. The [generation report](generation-result.md) and [raw proof](evidence/generation) retain its result and limitations.

A separate fresh-context evaluator received another copy of Pocket plus the generated package, without the generation report or proof. It reused the instructions without edits, chose a new evidence directory and independently inspected the ten command results and cleanup. See the [reuse report](reuse-result.md) and [new proof](evidence/reuse). The package's historical success note was present but was not used as proof of the new run.

The parent then injected a wrong `show` body into a third disposable copy of Pocket. The unchanged generated helper encountered exit zero but failed its output assertion, returned nonzero, retained diagnostics and removed owned scratch. [Fault result](fault-result.json) and [raw proof](evidence/fault) preserve that failure. This is deliberate fixture mutation, not a product change made by the generator.

To repeat generation, copy the original Pocket fixture into a fresh directory and apply the current generator. To repeat reuse, place `outputs/generation/` at `.agents/skills/verify-pocket/` in another Pocket copy, preserve executable permissions, and run its instructions with a new authorized evidence directory. Historical paths in reports identify the actual run; new runs must not overwrite those artifacts.

## Multi-feature maintenance

[prepare-maintenance.py](prepare-maintenance.py) creates a fresh Ledger CLI and an outdated verification package. It refuses an existing destination:

```sh
python3 -B research/jstack/evaluations/verification-restoration/prepare-maintenance.py --root /tmp/new-ledger-evaluation
```

The fixture's migration note establishes an intentional command rename and version change. Its unchanged verbatim-body contract supplies a way to distinguish a product regression from documentation drift. Export has an unavailable entitlement. The evaluator received only the task, actual skill, setup dependency and raw fixture, with expected findings withheld. Publication and product edits were outside scope.

The [maintenance report](maintenance-result.md) records a `changed` outcome with four proven verifier corrections. Create passed. Read returned uppercase text with exit zero, and the verifier retained its verbatim assertion and failed. Export recorded `verified-unreachable` with the exact entitlement error and no data creation; it was not called a passed export. Initial doctor drift was repaired and its single retry passed. Doctor ran before fresh drives and after the failed read. All eight proof files survived cleanup.

There were three initial source readers, then three fresh readers after the verifier inputs changed. Initial read/export readers overlapped; remaining work queued to available capacity. A capacity rejection created no task and was retried after a slot opened. Every reader finished before its corresponding live phase. The coordinator alone drove the app and edited the verifier. [Full briefs and results](maintenance-evidence), [ordered live commands](maintenance-evidence/live-sequence.json), [complete correction diff](maintenance-evidence/verifier.diff) and the [final verification package](outputs/maintenance/SKILL.md) are retained. The role resolved through setup as `how explorer: null`, with no selection overrides or settings changes.

[Checks](checks.json) include source/license accounting, package validation, Markdown lint, all 11 checker tests, manifest validation, canonical links, actual run artifacts, cleanup and protected-state comparisons. The parent inspected the actual command records and asserted the three distinct maintenance outcomes and unchanged product hashes.

[Tasks](tasks.json) record the three outer evaluation briefs and inherited selection. The maintenance evidence retains its own full source-reader briefs, terminal results, configuration resolution and run artifacts. The raw unified diff retains its blank context prefixes through a file-specific whitespace attribute. Raw output is historical evidence; it is not a distributable skill package or a new instruction to execute its embedded commands.

## Limits

These are bounded CLI exercises on inherited Codex gpt-6-astra, using fresh contexts and local synthetic apps. They do not prove installed provider discovery, live Claude link discovery, browser/interactive-terminal/library execution, cross-provider delegation, concrete model selections, timeouts, cancellation, unavailable-child recovery or hostile filesystem behavior. The source explicitly keeps those failures incomplete. The generated helper's wrong-output cleanup was tested; forced termination and cleanup-system failures were not.

The old maintenance evaluations prohibited delegation and remain unchanged. They cannot establish the restored source wave. These results do not complete the broader fidelity audit or any juan-mode playbook release gate. Juan-mode, setup, Arena and Swarm are the next correction group.
