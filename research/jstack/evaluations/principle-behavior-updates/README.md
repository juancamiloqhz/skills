# Four substantive principle updates

Adopt the four substantive principle corrections identified by the [complete coverage audit](../../coverage-audits/2026-10-18/README.md), together with the matching Juan-mode summaries. These change existing instructions; no new skill or model policy is introduced.

## Source and behavior

Local base is `610b901da3e9f2728ac9e15f15d30b09769e72c1`, merged PR #84. Source is cursor/plugins at `0148b78c56c72a1b8412055913c79f767095b217`. Paths below are under `pstack/skills/`; local leaves use the same suffix under `skills/jstack/jstack-principle-*`.

| Source | Previous instruction | Current instruction |
| --- | --- | --- |
| `principle-attack-the-premise/SKILL.md` | Require an actor census after repeated fixes fail. | Write down and directly test the premise, including problems without actors. Follow evidence that confirms or contradicts it. |
| `principle-fix-root-causes/SKILL.md` | Treat guards as symptom fixes. | Determine whether the state is legitimate. Handle valid states where required; fix the producer of invalid states. Propose a cheap diagnostic when a key fact was hard to find. |
| `principle-test-behavior-not-implementation/SKILL.md` | Reject certain assertion shapes, including absence checks. | Judge the observable contract. Catch broken behavior and survive internal refactors; pair absence with a positive control. |
| `principle-make-operations-idempotent/SKILL.md` | List convergent startup, cleanup, locks and scheduling patterns. | Derive each step from current state and judge leftovers using evidence valid across interruption points. |
| `poteto-mode/SKILL.md` | Older inline summaries for three of those principles. | Copy the three changed summary lines exactly. The idempotency summary already matches. |

The [principle adaptation record](../../principle-adaptations.md) links each exact source file. The [mode record](../../adaptations/juan-mode.md#current-principle-summaries) records the bounded summary update.

## Complete source comparison

Compared all four final files with Git objects at the frozen revision. After reversing the recorded differences below, each entire file matches its source exactly. The three changed mode lines match exactly, and reverting those lines produces the base mode file byte for byte. All four leaf LICENSE files match upstream.

Retained differences:

- Portable `jstack-` names and catalog references replace relative sibling skill links.
- Existing standalone authority and helper-discovery paragraphs remain.
- Existing omission of `disable-model-invocation: true` remains an explicit provider-verification gap; this update does not resolve automatic invocation semantics.
- The idempotency leaf retains one sentence requiring process identity and liveness for a process-owned lock. A reused PID does not prove ownership.

The earlier actor-census exception is retired because the new source no longer contains that census-specific inference. No replacement redesign was added. The other 20 principle leaves, mode routing, configuration and installed copies are unchanged. Original `adaptedFrom` values, review decisions and `reviewedThrough` remain unchanged; this report records the later bounded source adoption without claiming a complete upstream review.

## Evaluation procedure

[Cases and expectations](cases.json) contain four bounded tasks. Run each prompt once with its previous skill from the local base and once with the updated skill, in separate scratch directories. The tasks request executable Python demonstrations, not just explanations. They cover Unicode search without a cache, a nullable avatar and invalid balance decoder, checkout effects under mutations/refactoring, and recovery around an external commit.

Two fresh agents, without parent conversation history, each handled one version across all four tasks. Both used the inherited Codex gpt-6-astra model at high effort. Neither saw the other version or the expectation list. Cases share a context within each version, so this is a paired smoke evaluation, not eight fully independent trials or a statistical benchmark. The parent inspected answers and code and reran each demonstration. Raw outputs remain in task-owned cache. Durable retention is limited to the prompts/expectations, this report and one compact runnable file containing the four updated examples.

| Case | Old instructions | Updated instructions | Parent verification |
| --- | --- | --- | --- |
| Premise | Correct Unicode correction, but reported the mandatory actor census as inapplicable and the helper chain incomplete. | Directly tested the stale-cache premise without inventing actors. | Both scripts reproduce the cache-free miss and find the normalized match. Updated example also checks uppercase forms. |
| Root cause | Correct avatar fallback and decoder fix, explicitly overriding the blanket guard ban to honor the task contract. | Chose each correction by distinguishing legitimate and illegitimate states. | Both reproduce the original failures, preserve zero and populated values, and reject missing balances. |
| Behavior tests | Correctly used the existing positive-control guidance despite the assertion-shape framing. | Explained the external-effect versus private-helper distinction directly. | Both retain the no-charge case, reject four broken implementations and accept helper removal. |
| Idempotency | Converged under both requested interruption points. | Converged under both requested interruption points using current state and stable IDs. | Both preserve the committed result, produce one effect across retries, reject payload changes and respect live identity; reused PID remains untouched. |

All eight original demonstrations exited 0 when rerun by the parent. Each version met all 13 task expectations. This does **not** demonstrate a success-rate improvement. The baseline agent compensated for two instruction conflicts using the task's explicit contract. Adoption is justified by the upstream correction and clearer instructions, not by claiming the old version failed these tasks.

The runs were not blinded. A late coordinator message disclosed two baseline findings to the updated runner. Helper access also differed: the baseline read only the supplied leaves; the updated premise case read installed Build the Lever and Laziness Protocol but did not traverse their further references. Neither proves a complete dependency-chain execution or automatic invocation. These limits prevent a controlled comparative performance claim.

The only execution setup error was that `python` was unavailable; both agents used `python3` successfully. The parent inspected generated code and reports rather than relying only on exit status. The runnable retained examples preserve the updated code inside separate functions, with no behavioral changes:

```sh
python3 -B research/jstack/evaluations/principle-behavior-updates/run_examples.py
```

The retained runner also passes. It illustrates the decisions; it does not execute an LLM or prove that a future agent will use the principles correctly. Repeating the agent evaluation requires the prompts and both skill versions described above.

## Package checks and limits

All four existing packaging tests and the current documentation checker pass. The five edited skills pass skill validation. Complete source comparison, exact license checks and unchanged-manifest checks pass.

```sh
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
```

These exercises do not prove installed-provider discovery, persistent mode behavior, general debugging quality or real distributed recovery. No configuration, installation, external service, schedule or unrelated user work was changed.

## Normal use

After merge and a manual skill update, activate `jstack-juan-mode` and ask: "Fix the profile crash when a user has no avatar." The revised principle recognizes that a missing avatar is valid and permits the default-avatar handling there. If an impossible state caused the crash instead, it directs the agent to fix the code that created that state.

The principles also remain directly invocable, for example `jstack-principle-fix-root-causes`. Direct use does not activate Juan-mode.
