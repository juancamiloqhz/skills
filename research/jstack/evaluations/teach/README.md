# Teach evaluation

Date: 2026-10-19. Authoring base: `1966cfe0f8a68c412b54e9625c6452912cad68fd`. Source: `pstack/skills/teach/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. See the [adaptation record](../../adaptations/teach.md).

Teach combines actual How and Why investigations into short explanations. The evaluation checks helper execution, confidence preservation, follow-up pacing and honest handling of missing dependencies. It does not claim that Teach improves factual accuracy over the baseline.

## Live helper exercise

The evaluator received the new skill, exact authoring helper paths and an owned Git fixture. It did not receive the fixture generator or expected findings. The learner knew Python and JSON, asked why the exporter uses string IDs, and asked whether the batch limit of 200 came from measurement. Only fixture code and local history were authorized.

The evaluator read the complete How/Why procedures and shared setup contracts. It captured fresh capabilities and resolved each role through the canonical helper using the existing global configuration. No settings changed.

| Phase | Resolved model and effort | Result |
| --- | --- | --- |
| How simple-module explainer | Codex GPT-6.1-Sol, high | Completed concurrently with the investigator |
| Why source-control investigator | Codex GPT-6.1-Sol, high | Completed; code, both commits and measurement searches checked |
| Why synthesizer | Codex GPT-6-astra, xhigh | Completed after reader findings and citation checks |

Native same-provider tasks supported the exact selections. The evaluator reconciled all three terminal results before delivery and removed its temporary capability catalog. No nested work remained. The authoring evaluator, baseline reader and separate failure-case evaluator inherited GPT-6-astra at high effort.

The fixture's conversion commit explicitly attributes string IDs to preserving distinct browser cache keys. The initial commit supplies no rationale for 200. The evaluator checked the generated `exporter.py:3,7`, `consumer.cjs:2`, full commit messages and patches. It recorded all seven Why evidence categories; external categories and forge reads were outside the local-only scope. No application or tests ran during the investigation.

The initial answer was two sentences:

> The ID conversion writes each ID as text because JavaScript numbers can round away digits and make different IDs share one cache key, as the conversion commit explains. Whether 200 came from measurement is unknown.

The actual reply linked the inspected exporter line and named its commit. The uncertainty sentence was preserved verbatim from Why's synthesis. The independent baseline also found the correct mechanics and unknown rationale, but returned a longer explanation with a JSON example. This single paired exercise establishes neither a general accuracy improvement nor a timing advantage.

For the supplied follow-up, "Does this prove 200 is the fastest setting?", Teach reused completed findings and answered no. It explained that the slice includes only the first 200 records, rather than splitting all records into batches. It labeled the records-versus-work tradeoff as an inference and kept the author's intended tradeoff and optimal value unknown. No extra helper run or product edit occurred.

Two minor tool-use issues were corrected before dispatch: an overbroad read was truncated and reread in bounded sections; a repeated `--role` argument selected only its final value, so the evaluator resolved every role separately. There was no model substitution or failed helper phase.

## Missing-dependency case

A separate presentation-only exercise supplied completed How findings for a three-part scrolling subsystem, a failed Why phase caused by invalid configuration, and unavailable visual tools and Unslop. The response explained only the supplied mechanics and disclosed the unknown rationale, missing spatial picture and incomplete writing pass. It did not repair settings, install a dependency or claim helper execution. Its example row numbers were explicitly illustrative.

This checks failure handling. It does not verify image generation, progressive diagram rendering or T3 visual publication. Those paths and installed-provider discovery remain unverified. The live exercise used authoring paths and one simple local module, not a complex How explorer run or a cross-provider investigation.

## Reproduce and retain

Python 3.14.4 and Git 2.53.0 generated the fixture. From the repository root:

```bash
fixture_parent=$(mktemp -d)
python3 research/jstack/evaluations/teach/make_fixture.py "$fixture_parent/export"
git -C "$fixture_parent/export" log -p -- exporter.py
git -C "$fixture_parent/export" status --short
```

Use [cases.json](cases.json) for the live request and follow-up. Supply the current authoring Teach, How, Why and setup paths, the intended external Unslop, the generated root/revision and local-only evidence scope. Let the resolver validate the current saved configuration against live capabilities. If validation or dispatch fails, report that run incomplete without replacing models. Run the first case independently without Teach for the baseline; do not expose expected findings to either reader. The third case uses supplied findings rather than live helpers.

The generator refuses existing destinations. The evaluated fixture remained clean. Remove owned scratch after review. Retain only this report, the small generator and requests; raw helper reports, catalogs and generated repositories do not belong in Git.

## Packaging and source comparison

Final comparison preserves the pinned source's heading, five steps, inline writing standard, proof of actual helper use and confidence exception. The adaptation record accounts for all substantive differences. License bytes and explicit-invocation metadata match the intended source behavior. Four packaging tests, manifest validation, documentation/relative-link checks and whitespace checks pass.

The generic Codex metadata validator rejects upstream's retained `disable-model-invocation` field. A temporary copy omitting only that field passes its remaining checks. This is a qualified metadata check, not an unmodified-package pass or a provider discovery test. Existing operational skill bodies and the reviewed upstream checkpoint are unchanged.

## Normal use

After merge and manual installation, ask `$jstack-teach Explain our login flow. Start short.` It investigates how the code works and why it took that shape, then gives a short explanation. Ask "Why do we store the session there?" to go deeper. Unknown historical reasons remain unknown; teaching does not authorize changing the code.
