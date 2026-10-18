# How explorer prompt update

The [coverage audit](../../coverage-audits/2026-10-18/README.md) found that jstack retained an older, longer explorer template. This update follows upstream's deletion while preserving the existing evidence contract. It does not introduce a new investigation workflow.

## Source comparison

Local base is merged PR #88, `64ab2f96062f219de9f947cf83ffc52c1ef1dce9`. Compare `pstack/skills/how/` from the original adaptation pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/how).

Only two source paths changed:

- `references/explorer-prompt.md` removes introductory prose, the five-step exploration recipe and an output preamble. Adopt the current file, retaining only six existing blank lines after output headings. Components, flow, files read, boundaries, non-obvious behavior and open questions remain.
- `SKILL.md` adds adaptive effort/speed. Keep the existing selected model options unchanged, as required by the configuration policy. Adopting a new effort policy still requires a separate user decision.

The parent compared all package files against the audited source and checked the license. Remaining differences are the [recorded adaptations](../../adaptations/how.md): portable identity and catalog invocation, setup/configuration and lifecycle handling, read-only scope, citation checks, direct explanation without invented explorers, host tools and rendering, and heading spacing. The entrypoint, explainer template and shared investigation contract are byte-identical to the local base. Source pins and the reviewed checkpoint remain unchanged. No deleted exploration recipe was moved into another file.

## Reproduction and assessment

Reuse the three-file [How fixture](../investigation-restoration/fixtures/how) without copying it into a new tracked directory. Copy it into task-owned scratch. Obtain the baseline explorer template from the local base above and the updated template from this branch. Keep the same source, questions, assigned angles and shared Findings and citations contract in both runs. Give each stage its own writable output path and forbid source edits, application execution, network use and further delegation.

Complex question:

> Explain the architecture and lifecycle from API submission through queue ownership to delivery, including retries and failure boundaries. Do not change code or run the app.

Use two independent explorer contexts per version. Assign one the API submission, input handling, queue identity and repeated-submission slice. Assign the other worker processing, state transitions and delivery/failure boundaries. Fill the respective explorer template's question and angle placeholders. After both outputs are terminal and inspected, pass both to a fresh explainer using the unchanged explainer template. Keep baseline and updated outputs separate.

For the unchanged simple path, use one fresh explainer with no Explorer Findings section or prior-explorer claims:

> What does enqueue return if this owner submits the same payload again?

Before dispatch, the parent selected the existing fixture's acceptance cases: normalization and rejection before enqueue; owner/payload key; preserved pending job and attempt count on duplicates; attempt increment before delivery; timeout retention; success deletion; non-timeout propagation; honest gaps for scheduling, persistence and exactly-once delivery; source citations; and no invented explorer history on the simple path. Earlier expected cases and outputs are withheld from all evaluators.

## Results

Seven fresh native Codex contexts used inherited GPT-6-Astra/high: two explorers and one explainer for each complex variant, plus one direct explainer for the unchanged simple path. Independent explorers used disjoint output paths and ran concurrently where capacity allowed. Each complex explainer started only after its own two explorers had finished and the parent had inspected their outputs. No evaluator read the other variant's findings, historical outputs or expected cases.

| Acceptance case | Baseline | Updated |
| --- | --- | --- |
| Disabled/empty input rejected before enqueue; stripped payload and owner form the key | Both explorer findings and final explanation traced the correct source ordering. | Same result. |
| Pending duplicate preserves the job and attempt count; later submission after deletion creates a fresh job | Correctly distinguished pending-entry reuse from permanent deduplication. | Same result. |
| Worker increments before delivery; timeout retains entry; normal return deletes it; other exceptions propagate | Correctly traced all paths and distinguished a retry signal from a scheduled retry. | Same result. |
| Missing scheduler, queue implementation and delivery callback | Named the gaps; did not invent durability, exclusive processing, exactly-once delivery or historical intent. | Same result. |
| Grounded final explanation | Rechecked all three files, cited source lines and included a diagram showing the missing handoff. | Same result, with the absent worker caller shown separately. |

The direct simple explainer returned the tuple-key answer, preserved existing attempts, explained fresh insertion after deletion and cited the source. It did not claim explorers ran. All three final explanations explicitly distinguished static tracing from runtime proof. The parent read all seven outputs and checked their decisive claims against the 23-line fixture; all selected acceptance cases passed.

Protected hashes confirmed the fixture and operational skill/contract files unchanged during evaluation. No application code ran and no evaluator changed source or configuration. The shorter prompt passed this bounded comparison, but both versions passed; no accuracy or speed improvement was measured. The simple path was exercised once because its entrypoint and template did not change.

## Checks and limits

Four packaging tests, skill validation, documentation consistency and diff checks pass. Final source equality allows only the six heading-spacing lines. The existing fixture and this concise report are the reproduction material; prompt copies, findings, explanations and hash inventories remain in task-owned cache.

These are authoring-stage tests using inherited evaluation agents, not the saved `how explorer` or `how explainer` assignments. They do not test configured model dispatch, installed discovery, all providers, runtime behavior or production-scale exploration. One paired example cannot establish general equivalence or improved speed/accuracy. No model setting or installed skill changes are part of this PR.

## Normal use

After merge and a manual skill update, ask `jstack-how`: "How does a submitted job reach the worker, and what happens if delivery times out?" It explores the relevant source, explains the flow with references and names any missing scheduler or delivery guarantees it cannot establish. The invocation and output format stay the same.
