# Eval evaluation

The [procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/eval.md) preserves pstack's seven steps and blinding rules. See the [adaptation record](../../adaptations/eval.md) and [source comparison](source-comparison.json) for the T3 execution differences.

## Configuration boundaries

Before the user's configuration import, an independent authoring agent handled three requests through the canonical resolver with fresh capabilities. One inherited runner failed Eval's count and diversity requirements. Two inherited seats resolved successfully but still failed diversity. An invalid unrelated `bug-fix` provider failed whole-map validation. All three stopped before candidate or judge dispatch, without configuration writes or fallback models.

The user then explicitly requested a permanent import of their laptop configuration. Setup validated and saved all 17 roles, preserving per-role effort, and readback matched the attachment. The selected global file was effective for this project. This was a separate authorized configuration change, not an Eval fallback. The earlier proposed temporary panel was never used. The personal configuration and full catalogs are not repository artifacts.

## Live exercise

On 2026-10-17, the coordinator executed the in-development procedure against a synthetic receipt utility. The two guide variants differ by one instruction: use `int(float(amount) * 100)`, or convert decimal strings without binary floating-point rounding. Both models received both guides in fresh T3-owned contexts, with the same organic request and separate scratch directories. Two waves respected capacity. No separate Git checkout was needed.

The saved runner panel supplied Codex `gpt-6.1-sol` with `reasoningEffort: high` and Cursor `claude-sonnet-5-5` with `reasoning_effort: high`. The configured pool supplied Claude Agent `claude-opus-5-5` with `effort: xhigh` for one judge. It differs from the GPT coordinator's family, as Arena requires, but shares a family with one runner. Whole-map validation and execution availability passed against fresh catalogs before dispatch and again before judging.

The private rubric assigned 0, 1 or 2 for each of four criteria: exact cents including fractions/refunds; settled-only filtering, counts and order; public CLI, empty input and preservation; small understandable code and design notes. File reads were assessed separately. A preparatory local pilot distinguished exact arithmetic from float truncation; it was not an agent result.

| Label | Model | Guide | Public CLI checks | Artifact observation |
| --- | --- | --- | --- | --- |
| birch | GPT-6.1-Sol | Earlier | 3/6 | Followed float conversion; 0.29 became 28 cents and -0.29 became -28. Combined USD total was 142 instead of 144. |
| maple | Sonnet 5.5 | Revised | 6/6 | Parsed decimal strings with integer arithmetic and strict format validation. |
| elm | GPT-6.1-Sol | Revised | 6/6 | Used signed integer arithmetic and trusted the promised input format. |
| ash | Sonnet 5.5 | Earlier | 6/6 | Rejected the guide's lossy conversion after checking it; used Decimal and documented the deviation. |

All four writers completed without pending descendants. All 12 planted input files retained their original hashes. The coordinator read every implementation and note, ran six fixed CLI cases per output, and froze copies before one judge reviewed all four under neutral labels. The judge received the task contract, private rubric, code, notes and observed CLI results, without model identities or variant grouping. No artifact text needed redaction. Notes and code reveal arithmetic choices, so grouping may be inferable; anonymity does not prove that style cannot reveal authorship.

The judge scored birch 5/8 and the others 8/8, agreeing with every supplied CLI outcome. The coordinator initially scored birch 7/8. On review, the coordinator accepted zero for exact cents because both named fraction/refund cases fail, but retained two for clear code and useful notes: penalizing the documented choice again would double-count correctness. Final coordinator scores on the fixed rubric are birch `[0, 2, 2, 2]`, all others `[2, 2, 2, 2]`. This reconciles the substantive result while retaining the subjective notes disagreement.

The fixed checks show an improvement for GPT and a tie for Sonnet, which repaired the old guide independently. The preset rule therefore does not establish improvement across both models. Defer promotion based on this one run; use a broader, predeclared follow-up if stronger evidence is needed. The Eval workflow completed with the limits below, and no artifact was promoted.

## Read evidence and limits

Scoped T3 activity reads reached the end of each of the four original runs with no truncated items. Actual `command_execution` items contain `cat guide.md` and its returned text for every worker. This supports guide-read verification, beyond assistant self-report. Birch's code follows the old rule; maple and elm follow the revision; ash reads and deliberately departs from the old rule. Reading an instruction and obeying it are separate findings.

No comparison leakage or out-of-scope reads appeared in exposed candidate tool activity. The visible transport wrapper only added an implementation-subagent role. Hidden provider context is not observable, so this is not proof of complete transport isolation. Summarized timelines are not complete private provider transcripts. A separate-checkout run, nested delegation, dropouts and live catalog drift were not exercised. The receipt task checks this procedure's orchestration; it does not validate all installed skills or persistent Juan-mode routing.

There is one stochastic run per model/variant, not statistical evidence of general quality. The judge did not independently execute code or inspect guide/read records; the coordinator verified those separately. The judge also missed Decimal's default precision limit. A supplemental CLI check after judging used `123456789012345678901234567890.12`: ash returned `12345678901234567890123456790000` cents instead of `12345678901234567890123456789012`. Maple and elm were exact; birch also failed. These are real artifact findings, but this case was not in the predeclared suite. It qualifies ash's 8/8 rather than retroactively replacing the blind scores or manufacturing a promotion result. No candidate artifact was installed.

## Reproduce

From the repository root, create new task-owned locations. Do not put private material under the candidate root or send candidates this report, generator, checker, model map or rubric.

```sh
python3 research/jstack/evaluations/eval/prepare.py \
  /tmp/cedar-ledger-run /tmp/receipt-review-private
```

The generator reproduces the exact planted inputs and private rubric. It records seat indices instead of hardcoding model substitutions. Capture current capabilities and resolve the selected complete configuration for `arena runners` and `arena cross-judge pool`. Require two distinct effective models and an eligible different-family judge; stop incomplete if absent. This fixture exercises two seats. A larger configured panel needs additional owned labels and both variants for every seat; do not silently drop seats.

For each owned label, dispatch a fresh context using its `request.md`, prefixed only with its absolute working directory. Run the two seat assignments in `assignments.json` for each variant. Keep the private directory and other workers outside its read scope. Preserve the original hashes, actual model options, task/run identities and exposed tool records. After all writers finish, inspect outputs and run:

```sh
python3 research/jstack/evaluations/eval/check_receipts.py \
  /tmp/cedar-ledger-run/birch /tmp/receipt-review-private/checks-birch
```

Repeat for maple, elm and ash, using a new output directory each time. Add `--include-large` to reproduce the separately reported post-judge precision check; it must not be presented as part of the original blind suite. The checker reports observations, including failures, rather than treating its exit code as a verdict. Freeze outputs, remove identity-bearing metadata, revalidate configuration and send all outputs to one fresh read-only judge with the fixed rubric. Score them independently, reconcile disagreements, then disclose the mapping and limitations. Do not promote on an unsupported result.

For boundary reproduction, generate scratch configurations with setup's `models.py template --preset medium`. Resolve both roles with an explicit file and a fresh catalog, using `resolve --with-source` or Juan-mode's `scripts/preflight.py`. Two inherited seats can resolve while still failing Eval diversity. Set an unrelated scratch `bug-fix` seat's provider to `missing-provider`; both resolutions must fail whole-map validation. Never alter saved settings for these checks.

## Retained evidence

This report records outcomes and qualifications. `results.json` retains compact machine-readable decisions and task identities. `prepare.py` generates reproducible inputs; `check_receipts.py` exercises the public CLI. `source-comparison.json` records the required pinned-source comparison. Raw conversations, catalogs, candidate snapshots, generated inputs and routine logs remain in task-owned scratch while review is active. None belong in the committed package.

The packaged generator reproduced all planted inputs byte for byte. The packaged checker reproduced 3/6, 6/6, 6/6 and 6/6. Packaging tests passed 4/4 and both affected packages passed quick validation. Three complete pinned-source comparisons cover the new procedure, mode and setup; their licenses match their pins. The manifest, all 44 mappings, source pins and reviewed checkpoint are unchanged.
