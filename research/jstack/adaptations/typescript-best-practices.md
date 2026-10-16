# TypeScript best practices adaptation

Source revision: `11713c683fe4add4fd403ea880580abbc9e0875f`. Complete upstream scope: `pstack/skills/typescript-best-practices/SKILL.md` and `references/patterns.md`. Local package: [jstack-typescript-best-practices](../../../skills/jstack/jstack-typescript-best-practices/SKILL.md). The license matches the pinned `pstack/LICENSE`.

Preserve the rule table, full patterns file, heading order, examples and standalone boundary. Type System Discipline remains a language-independent principle with a conditional TypeScript helper pointer. This helper adds no model role, resolver, runtime dependency or playbook.

## Complete differences

| Location | Difference | Reason and verification |
| --- | --- | --- |
| Identity and calls | Prefix the skill and referenced principles with their exact `jstack-` catalog names; update the principle's helper pointer. | User-approved naming policy; caller and packaging checks. |
| Metadata | Remove Cursor `paths` and `disable-model-invocation: true`. Retain the .ts/.tsx description trigger. | Portable skills cannot assume Cursor path activation. The principle must discover this helper; use the established catalog-invocation compatibility exception. Installed-provider selection remains unverified. |
| Entrypoint introduction | Discover/read actual dependencies, reuse the already-read calling principle, and preserve task/repository authority. | Avoid assumed sibling installation and a recursive principle/helper call. Review does not authorize edits, installations or configuration changes. |
| Rule table formatting | Add spaces to the separator row. | Repository Markdown lint requires compact table spacing; rule text and order are unchanged. |
| Patterns pointer | Make the source pointer a Markdown link and explicitly read it when applying the rules. | The independently shipped package must expose its supporting examples; link check and caller exercise. |
| Constructive modeling table and range example | Correct the claim that plain numeric duration excludes negative ranges. Keep the plain number representation, but require finite/nonnegative boundary validation and relevant date checks. | The original negative-duration defect is recorded in the fidelity audit. A TypeScript `number` admits negative values, NaN and infinity. This is a factual correction, not a new branded-duration design. |
| Non-empty random selection | Add `?? entries[0]` to the positive example and explain arbitrary-index uncertainty under `noUncheckedIndexedAccess`. | The compiler cannot infer the arithmetic index bound from tuple non-emptiness. The known head provides a typed fallback without a cast or assertion. |
| Non-empty guard | Require the first index to exist as well as positive length; state element-validation and mutation assumptions. | A typed sparse array can have positive length without a head, so length alone did not prove the tuple claim. The bounded compiler/runtime exercise reproduces this defect. |
| `satisfies` example | Supply the previously implicit `Config` type; distinguish retained inference from a const assertion and note numeric widening. | The theme literal is retained for this target type, but `cols` is still `number`. The correction preserves the selected design without promising that every property is literal. |
| Object-argument example | Replace the claim that swapping the shown arguments compiles with an accurate description. | The example has a string and an options object, so swapping them already fails compilation. Keep the original object-argument preference and both examples. |

The numeric representation remains intentionally simple. Values from external sources still require boundary validation. The helper does not claim `number`, brands, `satisfies`, or a tuple prevents all invalid runtime values after unchecked casts or mutation.

Primary compiler references: [unchecked indexed access](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html) and [the satisfies operator](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html). The [evaluation](../evaluations/typescript-best-practices/README.md) records the concrete local compiler, examples, actual outcomes and limits.

The manifest adds one mapping and watches both principle dependencies. Type System Discipline's helper source is watched through its context mapping. Existing revision pins, review decisions and checkpoint remain unchanged. Full final source and caller differences are retained; no installed skills, models or schedules are changed.
