# TypeScript branded-ID guard

Adopt the branded-ID correction identified by the [complete coverage audit](../../coverage-audits/2026-10-18/README.md). The previous example already validated input through `isUUID`, then cast the result to `AgentId`. The current upstream example exposes `isAgentId(input): input is AgentId` and returns the narrowed value without a cast. This is a source-alignment correction, not evidence that the previous parser admitted invalid IDs.

## Source comparison

Local base: `f1808b879ad0893d9ecf26fb690bfa5c9365067a`, merged PR #85. Compared original source `11713c683fe4add4fd403ea880580abbc9e0875f` with audited source `0148b78c56c72a1b8412055913c79f767095b217` for the complete upstream package:

- [`pstack/skills/typescript-best-practices/SKILL.md`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/typescript-best-practices/SKILL.md): append the source's verifying-guard requirement to the branded-types rule.
- [`pstack/skills/typescript-best-practices/references/patterns.md`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/typescript-best-practices/references/patterns.md): copy its new guard and constructor exactly.

These are the only upstream changes in the package across that range. Compared both complete final local files with the audited source. Every remaining difference is unchanged from the [existing adaptation record](../../adaptations/typescript-best-practices.md): portable identity/discovery, invocation metadata, numeric-range validation, strict indexing and sparse-array handling, `satisfies` accuracy and object-argument wording. Package LICENSE bytes match the source. No principle caller, model configuration, installed package, manifest pin, review decision or reviewed checkpoint changes.

## Executed checks

The [reproducer](check.py) extracts the actual branded-ID code fence from the shipped patterns file and uses an existing compiler. Run from the repository root:

```sh
python3 -B research/jstack/evaluations/typescript-brand-guards/check.py \
  --tsc /path/to/typescript/lib/tsc.js
python3 -B research/jstack/evaluations/typescript-best-practices/replay.py \
  --tsc /path/to/typescript/lib/tsc.js
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
```

Executed on Linux with TypeScript 6.0.3 and Node v24.19.0, using `strict`, `noUncheckedIndexedAccess` and `noEmitOnError`. Nothing was installed.

| Check | Result |
| --- | --- |
| Valid lowercase/uppercase IDs through guard and parser | Compile and run; original strings preserved. |
| Empty, malformed, short and invalid-character IDs | Guard returns false and parser throws. |
| Raw string and unrelated `UserId` passed as `AgentId` | Both fail compilation with TS2345. |
| Replace type predicate with plain `boolean` | Constructor fails compilation with TS2322; narrowing is required. |
| Replace guard validation with unconditional true | Compiles, but runtime assertions reject the invalid input. |
| Retained duration validation | Zero/positive durations pass; negative/nonfinite durations, invalid start and out-of-range end fail. This is a fixture implementation of the documented boundary rule. |
| Existing non-empty selection replay | All seven checks pass, including sparse-head rejection and indexed fallback. |
| Packaging, skill validation, current docs and diff checks | Pass; four packaging tests. |

The source intentionally leaves `isUUID` to the consuming project. The fixture supplies a UUID-shape validator; it does not certify a production validator, every UUID version or ID ownership. TypeScript trusts user-defined predicates, so runtime checks remain necessary. The mutation test makes that limit explicit. Temporary source/build files are removed after the run; no compiler output or raw logs are committed.

This is a focused compiler/runtime check of the actual example, not a fresh agent-routing, installed-discovery or cross-provider evaluation. The prior full helper evaluation remains historical evidence for its original revision.

## Normal use

After merge and a manual skill update, ask `jstack-typescript-best-practices` to review an `AgentId` parser. For example, a parser that validates then returns `input as AgentId` should use a verifying `isAgentId` guard and return the narrowed input. The brand keeps a `UserId` from being passed accidentally to an agent-only API; the validator still owns the runtime check.
