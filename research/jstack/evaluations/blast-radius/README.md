# Blast radius evaluation

Date: 2026-10-19. Authoring base: `cac8ba1a74a54a61693854853e3976deb6d0caa5`. Source: `pstack/skills/blast-radius/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. See the [adaptation record](../../adaptations/blast-radius.md).

The new standalone skill follows a change into its consumers and runs evidence strong enough to support its conclusion. It preserves upstream's proof ladder, six-step procedure and handback fields. It does not add an automatic Juan-mode trigger.

## Executed case

An independent authoring evaluator received the complete skill, exact helper paths and an owned two-commit fixture. It did not receive the expected finding or fixture generator. The fixture changes a Python JSON producer from string IDs to numeric IDs. Its unchanged JavaScript consumer parses the payload and indexes records by ID.

The evaluator traced the actual code and local history, read Why's code-anchor procedure and external Unslop, and ran a cross-language proof. IDs `9007199254740992` and `9007199254740993` become the same JavaScript number. The cache loses invoice A and returns invoice B under the shared key.

| Check | String-ID base | Numeric-ID head |
| --- | --- | --- |
| Small IDs and maximum safe integer | Pass | Pass |
| Repository samples, exact keys and labels | Pass, exit 0 | Fail, exit 1; one record lost |
| Existing producer unit test | Not needed for comparison | Pass; only checks labels for small IDs |

The finding reaches proof level 4, executable real code within the fixture. It is not a running-application demonstration. The collision is deterministic for the supplied records; production frequency is unknown. There is no remote PR history, deployment runtime pin or locally available Node parser implementation. Those gaps remain explicit.

The parent generated a fresh fixture and replayed the retained proof with the same results. Both fixture checkouts stayed clean, and their consumer files were unchanged between commits. The intentionally failing head is successful defect detection, not a product fix.

## Bounded decision cases

A second independent evaluator read the skill and complete Arena instructions. It assessed the remaining requests in [cases.json](cases.json) without executing hypothetical code or delegating a panel.

- An unavailable native decoder, binary and version pin leave compatibility unproven. A supplied callsite is not evidence that decoding is safe or broken.
- Two inherited candidates using the same model do not meet the source's multi-model requirement. A valid judge does not resolve that gap. The comparison stays incomplete without silently substituting models or changing configuration.
- Unavailable Unslop leaves its writing pass incomplete. The assessment does not install or impersonate the missing helper.

Both authoring evaluators inherited GPT-6-astra at high effort. These are bounded authoring checks, not configured production-role runs or statistical measurements. Exact helper paths were supplied, so installed catalog discovery remains unverified. No live Arena panel, application deployment or provider persistence was tested.

## Reproduce

Environment used: Python 3.14.4, Node.js 24.19.0 with V8 13.6.233.17-node.51, Git 2.53.0. No dependency installation is needed. From the repository root:

```bash
fixture_parent=$(mktemp -d)
fixture_root="$fixture_parent/ledger"
python3 research/jstack/evaluations/blast-radius/make_fixture.py "$fixture_root"
python3 research/jstack/evaluations/blast-radius/check_fixture.py "$fixture_root" HEAD~1
python3 research/jstack/evaluations/blast-radius/check_fixture.py "$fixture_root" HEAD
git -C "$fixture_root" status --short
```

The second proof command must exit **1** and report the lost record. Run the original passing producer test separately:

```bash
(cd "$fixture_root" && python3 -B -m unittest discover -s tests)
```

The generator refuses an existing destination. The checker executes trusted fixture source and its unchanged current consumer; use it only with this generated repository. Remove the owned temporary directory after reviewing the results. Commit only this report, the cases, generator and parameterized proof. Raw reports and generated repositories stay in task-owned cache.

## Packaging and source comparison

The pinned-source comparison preserves every heading, numbered procedure and substantive rule. The adaptation record accounts for naming, helper discovery, execution authority, configured Arena models and missing-dependency behavior. The package retains the exact upstream license and explicit-invocation flag; Codex metadata also disables implicit invocation.

Four packaging tests, manifest validation, documentation checks and whitespace checks pass. The generic Codex metadata validator rejects upstream's `disable-model-invocation` field. A temporary copy with only that field removed passes its remaining checks. The shipped field is retained; this is a qualified compatibility check, not a claim that the unmodified package passes that validator.

## Normal use

After merge and manual installation, invoke:

> $jstack-blast-radius Review this change from string IDs to numeric IDs. Run local proofs, but don't fix anything.

The skill follows the IDs into downstream consumers and checks whether records survive. Its report separates demonstrated breakage, cleared concerns and missing evidence. A fix or merge remains a separate action.
