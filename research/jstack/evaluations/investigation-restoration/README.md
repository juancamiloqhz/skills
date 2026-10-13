# How and Why restoration evaluation

This correction restores How and Why from their exact manifest pin, `11713c683fe4add4fd403ea880580abbc9e0875f`: both entrypoints, two How prompts and all 12 Why references. The [How](../../adaptations/how.md) and [Why](../../adaptations/why.md) records explain each remaining adaptation. Configured delegation and the existing shared investigation contract are preserved. Provider invocation metadata remains a separate unresolved question.

## Source and package checks

[compare.py](compare.py) reads the pinned files from the shared bare Git cache and emits source/local hashes and complete unified differences. [source-comparison.json](source-comparison.json) covers all 16 mapped files and confirms both package licenses match the pin. The parent read the full difference set. Epistemics and the incident/postmortem reference are byte-identical to upstream; other references retain the source procedures with the recorded runtime, authorization and formatting substitutions.

```bash
python3 -B research/jstack/evaluations/investigation-restoration/compare.py > /tmp/jstack-investigation-source-comparison.json
cmp research/jstack/evaluations/investigation-restoration/source-comparison.json /tmp/jstack-investigation-source-comparison.json
```

Both skill validations, manifest validation and Markdown lint checks passed. Local Markdown file targets were checked, excluding the source template's literal `(url)` placeholder. [Parent checks](parent-checks.json) also record final hash checks and unchanged protected paths. Source pins, the reviewed checkpoint, shared setup contracts and historical evaluations are unchanged. These checks establish package integrity and the recorded differences; they do not prove behavioral equivalence.

## Agent exercises

Two independent coordinators applied the restored skills through explicit repository authoring paths. They inherited conversation context, so these are forward exercises rather than blinded evaluations. Each captured fresh capabilities, used the canonical resolver and ran native inherited children without model or effort overrides. Source investigation was read-only; children wrote only assigned temporary findings files.

[cases.json](cases.json) records the questions and expected checks. Portable source fixtures are in [fixtures](fixtures), with [hashes](fixture-hashes.json). These small examples test delegation and interpretation of evidence, not execution of the fixture applications. The selected configuration remained unchanged.

### How

The complex question ran two explorers, then one explainer after both findings were checked. The simple question ran one explainer directly. The parent inspected all four outputs against the three fixture files. Findings correctly described pending-job deduplication, account/payload ownership, retry and exception boundaries, and the missing scheduler and delivery implementation. They did not claim execution, persistence or exactly-once delivery.

[how-evaluation.json](how-evaluation.json) records child identifiers, phase order, hashes and checks. [how-outputs.json](how-outputs.json) stores the coordinator report and four original child outputs as unchanged strings. Paths in those strings refer to the original temporary workspace; the equivalent sources are in `fixtures/how/`.

The explorers ran serially. This did not test concurrent How exploration. The coordinator initially repeated the scalar `--role` argument, then resolved the explorer separately; the parent had independently resolved both roles before dispatch. The complete capabilities response was unnecessarily printed and its display truncated, but the stored full payload was used for validation. These execution imperfections remain in the original record.

### Why

Seven source investigators completed before one synthesizer ran. The first findings writer ran alone; later pairs ran concurrently after assigned-path behavior was demonstrated. The parent read all seven findings and the synthesis against every supplied archive. The final answer used the full PR review and parent ticket to establish the recorded partner-contract rationale. It retained the superseded draft and chat context without treating either as approval.

The synthesis rejected the unsupported benchmark and proven-fix premise. It preserved telemetry retention gaps, manual error resolution and regrouping, missing sampling information and the analytics instrumentation change. It used the supplied warehouse schema without claiming SQL execution. All seven categories remained visible, and the partner's own rationale stayed unknown. It also noticed that the archived stack's `limiter.check` was not mapped to the snapshot's `allowed` function.

[why-evaluation.json](why-evaluation.json) records child identifiers, phase order, source hashes and limits. [why-outputs.json](why-outputs.json) stores the original shared brief, coordinator report, seven findings and synthesis as unchanged strings. Their temporary source paths correspond to `fixtures/why/`; the seven archive files lived under `archives/` during execution. The supplied baseline is retained with those raw outputs. This exercise demonstrates bounded archive interpretation and delegation, not live connector discovery or historical completeness.

## Limits

The exercises use synthetic sources, inherited same-provider agents and explicitly supplied authoring paths. They do not prove installed skill discovery, automatic invocation, juan-mode persistence, concrete-model dispatch, cross-provider execution, production-scale searching or current live connector schemas. Why's archive access is a deliberate fixture override of normal connector discovery. No live Git history, forge, chat, observability, error service or warehouse investigation is represented by that override.

Missing-source and dispatch failure branches were not rerun here. Earlier evaluations remain historical evidence tied to their own instruction versions. No source pin, model configuration, installation, schedule or external project record changed during these exercises. The broader fidelity correction backlog remains open.
