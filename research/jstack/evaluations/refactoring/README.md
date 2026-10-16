# Refactoring evaluation

This evaluation checks a close port of the pinned Refactoring playbook. It distinguishes a blocked run using the existing global configuration from a separate run using setup's unmodified two-seat inherited template. Neither run changes the user's settings.

## Source and scope

The source is `pstack/skills/poteto-mode/playbooks/refactoring.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. The [adaptation record](../../adaptations/refactoring.md) accounts for every difference. [Complete source comparisons](source-comparison.json) include the new playbook, the full current mode and setup entrypoints against their pins, package licenses, existing-file changes and manifest invariants.

[Inputs](inputs.json) retain the realistic request, fixture revisions, source hashes and both configurations. Two independent copies of a small CommonJS task-status formatter started with identical bytes and no tests. The evaluator could simplify structure, add tests and make local commits, but could not publish, install, change settings or write outside its assigned scratch scope. The parent supplied no intended implementation.

The explicit authoring root was `skills/jstack`. Evaluators read current repository packages, not stale installed copies. Native children inherited the parent model and effort. Captured T3 selection was `codex/gpt-6-astra`; this establishes separate contexts, not model-family diversity or independently attested provider execution.

## Existing one-seat configuration

The evaluator interpreted new lookup calls as crossing a function boundary and conservatively required Architect. The saved one-seat panel was valid configuration but insufficient for its two-candidate requirement. It did not add a seat, change configuration, dispatch design candidates or claim the main reshape completed.

It added nine passing characterization tests before editing production code and delegated only deletion of the unused `unusedPrefix` binding. The six status branches stayed intact. Its lead checked 425 direct formatter cases and 49 public CLI cases against the baseline. Reader-load improvement was limited to one unused binding; the requested repetitive structure remained.

The outer author independently checked 87 CLI cases, 119 imported-function cases, the nine tests and unchanged CLI/consumer/package/README bytes. A deliberately changed status label failed seven public cases despite successful process exits. No local commits were created, so commit replay was not applicable; the evaluator retained the proposed test-then-subtraction order. Independent replay of both captured source states passed the nine tests and 87 CLI cases per state.

This run is incomplete and does not pass full workflow evaluation. Parent diff inspection preceded Comment Sicko. Some initial reads were recaptured, the failed `python` bootstrap record abbreviated its script, and the reviewer had a partial transcript. Three `npm test` runs also wrote debug logs under `~/.npm/_logs`, breaching the evaluator's scratch-only write boundary. Attribution evidence distinguishes those logs from concurrent unrelated npm work. The logs were left untouched. The separate run was told to use direct `node --test` or a task-local npm cache.

Evidence: [run archive](one-seat-evaluation.json), [independent baseline](one-seat-parent-baseline.json), [independent final verification](one-seat-parent-verification.json), [empty commit replay](one-seat-parent-history-verification.json), [captured source-state replay](one-seat-parent-slice-verification.json). The run archive includes the evaluator report, decision log, briefs, task IDs, raw runtime outputs, fixture bytes and review findings. All four child tasks are terminal.

## Two-seat fixture run

The separate evaluator used the unmodified `models.py template --preset medium` output, with two inherited Architect, Arena and Interrogate seats. It completed How, captured six baseline tests before production edits and compared two design-only candidates: a private Map and a local conditional prefix expression.

The Arena judge preferred the conditional expression. The coordinator preferred the mapping because Refactoring requires removing branches. Two configured Interrogate reviewers assessed the contested choice; neither reported an ordinary-input defect. The coordinator selected the private Map and retained the judge's dissent and its reasoning. The reviewers provide independent contexts, not model-family diversity.

A scoped implementation child removed the unused local first, checked the unchanged tests, then replaced the six branches with the private map and checked again. The existing function signature, named CommonJS export, title-addition operation and callers stayed unchanged. This centralizes the six mappings and one common output expression. Its tradeoff is one private module-lifetime collection and native lookup semantics. No helper API, validator or compatibility path was introduced.

The evaluator's equivalence set covers 368 function cases and 20 CLI cases; three PTY scenarios exercise the terminal interface. The outer author independently confirmed 87 CLI cases, 119 imported-function cases and all six tests. Exact stdout, stderr and exit codes matched the original. A wrong-label negative control was detected. The CLI, consumer, package metadata and README remained byte-identical.

The outer author also replayed the captured original, subtracted and reshaped source files with the unchanged six-test pin and 87 CLI cases per state. These are source-snapshot replays. No Git delivery commits were created; local delivery retains the patches and proposed order.

Both Interrogate reviewers demonstrated that replacing `Map.prototype.get` can change the Map candidate's behavior. Neither fixture caller replaces built-ins, so the evaluator accepted ordinary native Map behavior as the environment assumption. The case does not prove equivalence under modified built-ins. This observed distinction is preserved, not folded into a blanket unchanged-behavior claim.

The How child initially read a stale installed helper before rereading the supplied current source. The coordinator first used unavailable `python`; the implementation child first tried nonexistent mode and Unslop paths. These attempts were corrected, but some initial reads were recaptured. The four throughput dimensions were recorded before fan-out and added to the host plan only at final reconciliation.

The original evaluator also omitted Show me your work, its canonical decision log and its required trail reviewer despite the multi-phase run. Its claim that all local gates ran is therefore too broad. The outer author identified this omission, preserved the original report and created a clearly labeled retrospective trail for a fresh independent review. The late audit does not establish contemporaneous logging or erase the original mode-conformance gap. See [parent audit](parent-audit.json). All eight original child tasks are terminal. The late reviewer also found an overbroad "no execution or test failed" claim in the implementation handoff; reproduced path-lookups exited 1. The audit corrects the claim to passing application checks and supersedes a weak log evidence pointer without rewriting the originals.

Evidence: [run archive](two-seat-evaluation.json), [independent baseline](two-seat-parent-baseline.json), [independent final verification](two-seat-parent-verification.json), [empty commit replay](two-seat-parent-history-verification.json), [source-state replay](two-seat-parent-slice-verification.json).

## Boundaries

Opening a PR remains unavailable in the installed procedure. Neither evaluator publishes a PR or grants merge/install authority. The outer author creates the skill PR under the user's separate project authorization.

These bounded fixtures do not establish API/caller migration, browser equivalence, cross-model diversity, provider persistence or every Refactoring branch. Source-reading dumps are indexed by hash to avoid duplicating packaged files; full capability catalogs are represented by hashes and focused role outputs and may be removed after use. The archives are not complete conversation transcripts. Temporary fixtures and evidence remain under `/tmp/jstack-refactoring-20261016`.

[Validation](validation.json) records packaging, entrypoint, manifest, Markdown, link and whitespace checks. The manifest still has 44 mappings and unchanged pins, watch paths, decisions and reviewed checkpoint. Eight of 23 playbooks are now bundled; 15 remain pending.
