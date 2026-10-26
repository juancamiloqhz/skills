# Formal verification maintenance evaluation

Date: 2026-10-26. Source: `pstack/skills/maintain-formal-verification-skill/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`. The user selected this previously deferred candidate after PR #145. This adds a standalone explicit entrypoint, not another playbook or model role. No production code or installed skill was changed.

## Source comparison and integration

The complete final [skill](../../../../skills/jstack/jstack-maintain-formal-verification-skill/SKILL.md) retains every heading, all six Pass steps, the four outcomes and combined updated/bug result, original-baseline run, every covered-code change, moved/new state writers, intentional-promise evidence, mutation/counterexample rules, per-check sync discipline and separate product-fix boundary. The [adaptation record](../../adaptations/maintain-formal-verification-skill.md) accounts for naming, actual tools/authority, owned scratch, committed-code checkpoints and honest generated-input labels. License bytes match `pstack/LICENSE`; source explicit-invocation metadata is preserved in both frontmatter and Codex policy.

The manifest maps the new package and its generator context at that exact source revision. The existing generator watches maintenance and recommends it at handoff. Root catalog, migration instructions, Help/recipes and the two relevant guide pages now discover it. The source catalog has 58 packages, with 24 principles and 23 playbooks unchanged. Historical installation/runtime reports retain their actual earlier counts. Statechart and video catch-up remain deferred. Neither adoption pins of existing packages nor the reviewed checkpoint advances.

## Live authoring trials

Three fresh native Codex consumers inherited the parent model without an override. Each read the entire frozen skill and independently handled two assigned fixture projects with real Git histories. Requests named the task/project but not the expected result or suspected defect. Only verification edits, owned scratch and a handoff were allowed. No installation, network, publication, model changes, product edits, commits or nested delegation were allowed.

The [fixture generator](make_fixture.py) builds on the earlier finite lease fixture. Its old checker explores a copied model, which passes with 15 reachable states. The product domain has at most 48 structural combinations: two workers, four phases each, and three owner values. Calls are atomic/serialized. It models no crashes, retries, timing, network, fairness, liveness or larger worker set. A model pass is not evidence that a changed product still matches it.

| Case | History and observed outcome |
| --- | --- |
| a | Covered product change adds a comment. **In sync.** Property/bounds unchanged. Consumer binds verification to the real transition so a real-code negative control is effective, then confirms the current commit. |
| b | `lease.py:advance` moves to `dispatcher.py:step`, with no recorded sync metadata. **Updated.** Consumer discloses fallback to the last verification-changing commit, locates the move, updates coverage/binding and confirms current code. |
| c | Ready-phase ownership guard is removed while the old model still passes. **Updated and bug.** Updated check fails. Actual `advance(A), advance(B), advance(A), advance(B)` reaches two holders; introducing commit identified. Product remains broken and unchanged. |
| d | New `force_grant` function writes guarded state but is absent from the old model. **Updated and bug.** Consumer includes the new action. Actual `force_grant(A), force_grant(B)` reaches two holders; introducing commit identified. |
| e | Required external runner unavailable; existing command exits 2. **Blocked.** Consumer preserves the required runner and old sync, instead of substituting the historical checker or reporting a code bug. |
| f | Sync field records an unresolvable all-zero revision. **Blocked.** Consumer keeps it unchanged and reports unavailable history. It also demonstrates that the unbound old checker misses a scratch real-code mutation; no new sync is invented from the model-only pass. |

For a/b, maintained checks pass with 15 reachable states, catch a real guard-removal mutation as a two-holder failure, and pass after restoring scratch. Property/bounds stay unchanged. For c/d, model updates describe current code and counterexamples replay on actual product functions. Their sync commits confirm correspondence with a known defect, not safety. For e/f, execution/history remains incomplete and checkpoints stay unchanged.

The parent inspected handoffs and decisive artifacts, independently ran every original model from its committed history, and reproduced c/d directly on immutable current product source. It then ran the [completed-trial replay](replay.py) on actual consumer outputs: passing baselines, real-code mutations, restoration, current-code counterexamples, blocked prerequisites, sync records and unchanged product bytes/HEADs all matched. Both positive cases now import the actual transition; c/d retain a finite model whose source matches the product, with the checker including all declared actions. No current finding was hidden or property weakened.

Native tasks `formal_maintenance_ab`, `formal_maintenance_cd` and `formal_maintenance_ef` completed in this turn with no requested further agents. Their six raw handoffs, snapshots and scripts stay in owned cache, not Git. The fixtures and replay retain the reproducible premises and artifact checks without storing duplicate generated packages or conversations.

## Reproduce

Create a nonexistent owned destination:

```bash
python3 -B research/jstack/evaluations/formal-maintenance/replay.py /tmp/jstack-maintenance-trial
```

This creates six histories and confirms original model passes; it does not execute a skill or claim maintenance completed. Give a fresh consumer the complete candidate skill and one case's `request.json`, with writes confined to its verification and owned scratch. Withhold the generator, this results table and other cases from the consumer. Do not commit its edits. After all consumers finish:

```bash
python3 -B research/jstack/evaluations/formal-maintenance/replay.py /tmp/jstack-maintenance-trial --completed
```

The completed mode checks the known fixture outcomes and actual generated artifacts, including real-code trace replay and scratch restoration. It is not an automatic general-purpose maintenance implementation. The parent ran it against the six completed trials successfully. Remove the owned directory after inspection. Python 3 and Git suffice; no tool installation is required.

## Checks and limits

Four packaging tests and 20 documentation tests passed; current docs report 0 problems for 58 packages, 24 principles and 23 playbooks. Manifest schema, unchanged original pins/checkpoint, exact license, all headings/six steps and explicit metadata were checked. Both replay modes ran successfully on the fixture premises and completed consumer artifacts. The generic Codex validator rejects the preserved upstream `disable-model-invocation` field; it is not reported as passing and the source flag was retained.

The existing committed-catalog test passed with locally available Skills CLI 1.7.4. In a disposable clone, normal, full-depth and wildcard listings all discover the committed catalog, including the new package and all 58 jstack identities. A deliberate rename of a different skill changes the observed catalog, and listing preserves the clone. This uses the existing cached CLI with telemetry disabled; nothing is installed or fetched from a package registry. A later report-only amendment leaves the tested package and manifest contents unchanged. Native provider slash registration remains unverified.

These are six bounded authoring cases in three contexts, not a reliability rate, native slash-registration test or all-provider certification. Intentional promise changes, dirty covered product files, multiple checks with mixed sync outcomes, no-check discovery, user-authorized product fixes and generated-input fallback labels were not separately exercised. There is no new TLC or proof-assistant run. Outcomes e/f remain deliberately blocked; passing example unit tests are not substituted for the missing obligations. Installation stays manual.

## Normal use

After merge and manual installation, ask `$jstack-maintain-formal-verification-skill Recheck our lease verification after the dispatcher refactor. Leave product code unchanged.` A stale check can pass before maintenance and expose a real bug after its model catches up. The handoff distinguishes that result from a modeling mistake or missing tool, and gives each check its own confirmed sync status.
