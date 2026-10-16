---
name: jstack-typescript-best-practices
description: TypeScript best practices. Use when reading or editing any .ts or .tsx file.
---

# TypeScript best practices

Apply the **jstack-principle-type-system-discipline** principle skill first.

Discover referenced jstack skills through the current catalog or explicit authoring paths and read their full entrypoints. Reuse an already-read principle when it called this helper; do not recurse through the same call. A missing or ambiguous dependency leaves the affected guidance incomplete. Apply within the requested review or edit scope and repository conventions; direct invocation does not activate jstack-juan-mode, install dependencies or change model configuration.

| Rule | Summary |
| --- | --- |
| Discriminated unions | Model variants with a `kind` literal discriminant so impossible states can't be represented. No optional-field bags. |
| Branded types | Brand primitives with `& { readonly __brand: "X" }` so they can't be mixed up. Validate once at the boundary. |
| Constructive modeling | Build the shape so the illegal value can't be constructed. `[T, ...T[]]` for non-empty, `[T, T][]` for even length, `start` plus a boundary-validated nonnegative `duration` for a range. A plain `number` does not enforce sign or finiteness. Use construction where the type can express the invariant; validate numeric constraints at the boundary. |
| Simplest total type | Keep `T[]` while every operation on it stays total. Strengthen to `NonEmpty<T>` only where the loose type forces `!`, a cast, or a "should never happen" throw. |
| `unknown` over `any` | External data is `unknown`. |
| Schemas before guards | Before hand-writing a property-by-property type guard, use the repository's runtime schema library and infer the type from the schema, such as `z.infer`. |
| No `as` casts | Every `as` is a runtime crash waiting. Cast only after validation. |
| Narrowing hierarchy | Discriminant switch > `in` operator > `typeof`/`instanceof` > user-defined type guard > `as`. |
| Type guards | Must verify the claim. A lying guard is worse than `as` because the bug hides behind a name that says it's safe. Name them `isX` or `hasX`. |
| Exhaustiveness | Inline `const _exhaustive: never = x;` in default arms so the compiler errors when a new variant is added. |
| `satisfies` over `as` | Checks compatibility while retaining the expression's inferred type. |
| Boundary validation | Parse where data crosses in, into a named domain type. `Record<string, unknown>` (however spelled) stops at that parse. Trust types inside. See the **jstack-principle-boundary-discipline** principle skill. |
| Schema-derived types | Reach for `Pick`/`Omit`/`Parameters`/`ReturnType`/`Awaited`/`typeof` before declaring a new interface. |
| Object args | Pass objects, not positional, so argument order is self-documenting. Skip on hot paths (per-frame render, tokenizers, parsers). |
| Real tests | Don't mock what you can run. Prefer the framework's real test primitives with leak/disposable checks, and verify UI in a running build. Mock only what you can't run locally. |
| Structured telemetry | Prefer structured logger diagnostics with enough context to debug from an id. No `console.log` in shipped code. |

Read [TypeScript patterns](references/patterns.md) for the examples and qualifications when applying these rules.
