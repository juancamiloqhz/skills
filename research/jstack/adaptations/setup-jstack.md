# Upstream attribution

The [2026-10-15 naming decision](../skill-names.md) additionally changes this package's local identity and callers. Its upstream identity, procedure and revision pin remain as recorded below.

Updated on 2026-10-15 after comparing the complete setup entrypoint with its exact source pin. The [fidelity audit](../fidelity-audits/2026-10-13/foundation.md) identified the seven-step and inline-map drift corrected here. [Restoration evidence](../evaluations/setup-restoration/README.md) separates source comparison, executable checks and bounded agent exercises. This correction does not close Arena, Swarm or the broader fidelity backlog.

jstack is a portable adaptation of pstack's model setup concept and 17-role registry for T3 Code, independently implemented here. It is not an official Cursor, pstack or T3 Code release.

- Repository: [cursor/plugins](https://github.com/cursor/plugins).
- Inspected revision: `ccb5507cec1546dc88135c1139c811e6c59115ba`, October 10, 2026.
- Primary source: [setup-pstack](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/setup-pstack/SKILL.md).
- Consumer context: [poteto-mode](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/poteto-mode/SKILL.md).
- License: MIT, Copyright 2026 Lauren Tan. The upstream notice is retained in [package LICENSE](../../../skills/jstack/jstack-setup/LICENSE).

Adaptations replace Cursor's always-applied rule, Task model slugs and Auto alias with a JSON contract for global defaults and optional project configuration, T3 Code live model/option discovery, explicit provider identity and parent inheritance. Project files replace the full global role map, and explicit file selections remain highest priority. No upstream playbooks or autonomous shipping rules are enabled. The repository's earlier pstack research and review evaluations retain their own separate source pins.

## Complete entrypoint comparison

The source directory contains only `SKILL.md`. The local entrypoint restores `Steps`, all seven numbered steps in order, the three lettered budget/map substeps, the exact four budget labels and all 17 role labels inline. Step 5 is named "Write the configuration" because the saved JSON is not a Cursor rule. Remaining differences are accounted for below.

| Source location | Local difference and reason | Verification or limit |
| --- | --- | --- |
| Frontmatter and introduction | Rename pstack to jstack and describe T3 configuration, scopes and optional verification. Clarify that saving does not switch models or implement Juan-mode's missing procedures. No upstream invocation-policy flag is removed; setup has none. | Source comparison and skill validation. |
| Step 1: detection | Replace Task slugs/entitlement lookup with current T3 provider/model/option discovery, one direct attempt and the documented ACP fallback. Stop if unavailable instead of accepting pasted slugs, which lack the provider identity and option schema required for validation. | Live catalog used in isolated setup; unavailable-catalog transport was not exercised here. |
| Step 2: state | Replace the single Cursor path with the approved explicit/environment/project/global lookup. Offer scope and seed a new project from the complete global map. Report unknown roles instead of dropping them. | Existing scope decision and complete-map contract; CLI lookup and seed tests. |
| Step 3(a): budget | Keep all four labels. The inherited draft has `medium`, rather than source concrete defaults at `large`; setup still asks for the budget before saving unless supplied. No draft label changes inherited effort. | Both exercises supply a budget or explicitly preserve it; unanswered-budget interaction is untested here. |
| Step 3(b): assignment | Preserve saved identities, options and lists. Use inherited assignments until the user selects concrete models rather than automatically choosing source Grok/Opus defaults. Materialize requested effort in advertised provider options, with disclosed downgrade or a new choice when none qualifies. Retain explicitly requested exceptions. | Saved-choice requirement; concrete-option and drift tests. Live bulk concrete budget editing remains untested by this correction. |
| Step 3(b): aliases | `inherit-parent` omits a target. Provider Auto is an advertised concrete model, not an always-valid portable alias. | Existing T3 adapter contract and resolver tests. |
| Step 3(c), step 5: panels | New unseeded Arena, Architect and Interrogate panels now have two inherited entries by the user's 2026-10-15 decision, matching source candidate counts. Existing files and global seeds keep their counts. Two inherited agents do not establish model-family diversity. | New-template, independent-seat and unchanged one-seat seed checks; no migration. |
| Step 3(c), step 5: judge pool | Preserve one inherited judge alternative rather than duplicating the alias into the source's two different concrete families. A pool selects one judge; duplicate inherited entries add no family alternative. Retain the source different-family preference and Swarm per-arm override semantics in the role explanation. | Pool resolves one inherited target. Arena/Swarm implementation fidelity remains the next correction; this explanation alone does not prove either consumer behavior. |
| Step 4: validation | Validate every provider, model and option in the complete exact role map before save or resolution. The user explicitly retained whole-configuration blocking on 2026-10-15; no silent repair, missing-role fallback or extra-role deletion. | CLI test requests a valid How role while an unused bug-fix model is stale: it fails without output or file mutation. |
| Step 5: persistence | Replace `.mdc`, `alwaysApply` and comment-based overrides with complete schema-version-1 JSON and atomic writes. The inline example matches the generated template. Preserve `preset` for compatibility; effective options govern delegation. | CLI roundtrip, invalid-write preservation and source-example comparison. |
| Step 6: confirmation | Read back and show effective lookup, including shadowing overrides. Consumers reload at invocation; do not claim T3 automatically loads a rule in new sessions. Clean temporary drafts/catalogs and preserve the other scope. | Isolated setup and existing lookup/preflight tests. No provider restart/persistence claim. |
| Step 7: optional verification | Retain one post-save offer, acceptance handoff and no repeated prompting. Skip non-products or existing real-path coverage; discovery comes from the installed catalog or an explicit path. Missing generator gives manual installation instructions, never automatic installation. Existing authorization can satisfy acceptance. Generator failure does not undo settings. | Both new exercises cover the docs-only skip. Earlier offer/generator evaluations remain separate evidence; decline, missing generator and failure were not rerun here. |
| Closing scope statement | Clarify that configuration itself neither launches workflow agents nor grants permissions; the optional accepted generator owns its task. | Fixtures only save settings; no consumer delegation or installation. |

The [decision record](../decisions.md#setup-defaults-and-validation-2026-10-15) preserves the new-panel and whole-map choices for future upstream updates. All-inherit routing and saved-choice preservation predate this correction. The one-entry pool is a consequence of retaining inheritance without inventing a concrete judge family, not a claim that the source pool has one entry.

## Local support files

The source has no corresponding helper files. `scripts/models.py` implements the JSON schema, lookup, current-catalog validation, atomic save and target resolution required by the T3 adaptation. This correction changes only fresh-template panel cardinality and separates the three panel roles from the judge pool; lookup, validation and save logic are unchanged. `scripts/test_models.py` checks executable behavior, including preserving older one-seat files. `references/configuration.md` owns the shared consumer contract; its new-default paragraph is updated. `references/t3-code.md` retains actual transport/catalog/delegation mechanics. `agents/openai.yaml` retains Codex UI metadata without changing invocation policy. `references/investigation.md` remains the separately attributed contract below. `LICENSE` remains byte-identical to the pinned package license. The comparison records each support-file hash; hashes are an inventory, not proof of semantic equivalence.

The manifest now watches `pstack/skills/create-verification-skill` as setup's step-7 dependency, alongside its existing mode/how/why context. No source pin or reviewed checkpoint advances.

## Reasoning-budget rationale

[Pstack PR #366](https://github.com/cursor/plugins/pull/366), introduced in [commit 5bf2b1544db739998121a306340631963c2ff3de](https://github.com/cursor/plugins/commit/5bf2b1544db739998121a306340631963c2ff3de), explains that reducing reasoning spend previously required changing each role by hand. The budget choice applies an effort target across the working assignments before per-role confirmation.

Jstack keeps the four labels and target levels for conceptual compatibility. It adapts model slugs to provider-specific options and explicitly resolves the scope of rerun changes and retained overrides. This does not reproduce Cursor's rule-loading mechanism or make the budget a runtime spending limit. The source pin for the shipped setup adaptation above is unchanged.

## Investigation consumer contract

The shared [investigation contract](../../../skills/jstack/jstack-setup/references/investigation.md) supports the standalone how/why consumers without activating a workflow during setup. Its evidence categories and confidence guidance derive from [pstack why](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why) at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. The existing MIT notice covers this attribution. T3 Code capability checks, explicit configuration handoff and artifact ownership adapt that guidance to jstack. This additional source pin does not change the setup implementation's pin above.

## Swarm task-local resolution, 2026-10-15

The subsequent [Swarm restoration](../evaluations/swarm-restoration/README.md) adds `resolve --worker-override ARM_JSON`, limited to the `swarm workers` role. This restores the source setup step 3(c) distinction between a saved scalar default and explicitly assigned race/comparison arms. The helper validates the entire saved map first, validates the override with the existing seat/catalog rules, then returns its effective target without writing either file. The original selected config path stays in `--with-source`; the task retains the override separately. No schema, default budget, saved-model or other-role behavior changes. The accompanying configuration-contract paragraph and executable tests document the new flag. Source pins remain unchanged; the earlier setup snapshot remains historical evidence of its prior support-file hashes.

## Investigation availability, 2026-10-16

The setup entrypoint and configuration reference now identify Juan-mode's read-only Investigation playbook as available. The remaining 22 procedures are still pending. This corrects two jstack-owned availability statements; no setup procedure, model behavior or source pin changes. See the [Investigation assessment](investigation.md) and its complete source comparison.

## Prototype availability, 2026-10-16

The same two availability statements now include the throwaway Prototype procedure and identify 21 remaining routes. See the [Prototype assessment](prototype.md). Setup steps, model behavior and source pin remain unchanged.

## Trace forensics availability, 2026-10-16

The entrypoint and consumer contract now include Trace forensics and identify 20 remaining procedures. See the [Trace assessment](trace-forensics.md). Setup behavior, configuration schema and source pin remain unchanged.

## Skill-authoring availability, 2026-10-16

The entrypoint and configuration consumer note now include Authoring or modifying a skill and report 19 pending procedures. [Source comparison and evaluation](../evaluations/authoring-a-skill/README.md) cover these availability-only changes. Setup behavior, model roles, existing configuration, source pin and installation remain unchanged.

## Runtime-forensics availability, 2026-10-16

The entrypoint and configuration consumer note now include Runtime forensics and report 18 pending procedures. [Source comparison and evaluation](../evaluations/runtime-forensics/README.md) cover these availability-only changes. Setup behavior, roles, existing configuration, source pin and installation remain unchanged.

## Bug fix availability, 2026-10-16

The entrypoint and configuration reference now include Bug fix as the sixth available Juan-mode procedure, leaving 17 pending. [Bug fix comparison and evaluation](../evaluations/bug-fix/README.md) cover these availability-only edits against setup's own pin. Configuration lookup, roles and scripts remain unchanged.

## Feature availability

The Feature procedure and its shared four-part throughput checkpoint are now available. Feature brought coverage to seven playbooks with 16 pending. Configured Architect and Arena panels retain their required counts; existing settings are not expanded. The [Feature adaptation](feature.md) and [evaluation](../evaluations/feature/README.md) record source comparison, isolated two-seat execution, the one-seat limitation and remaining publication dependency.

## Refactoring availability

Setup and its configuration reference now list Refactoring as an available consumer, with eight procedures and 15 pending. This changes no setup step, role, default, resolver behavior or user configuration. See the [Refactoring adaptation](refactoring.md).

## Perf issue availability

The opening availability paragraph and configuration consumer list now include Perf issue. Nine mode procedures are available and 14 pending. Setup behavior, role assignments, existing configuration and defaults are unchanged. The [complete pinned comparison](../evaluations/perf-issue/source-comparison.json) includes the final entrypoint and exact configuration-reference diff.

## Hillclimb availability

The opening paragraph and configuration consumer list now include Hillclimb. Ten mode procedures are available and 13 pending. No setup behavior, role assignment, saved configuration or default changes. The [comparison](../evaluations/hillclimb/source-comparison.json) records both availability updates.

## Eval availability

Setup and its configuration reference now list Eval as an available consumer. Eleven procedures are bundled and 12 remain pending. Existing saved configurations, templates and resolver behavior are unchanged. Eval checks distinct candidate models and a different-family judge after configuration resolution; repeated inheritance cannot satisfy those requirements. See the [source comparison](../evaluations/eval/source-comparison.json).

## Visual parity coverage

The [Visual parity adaptation](visual-parity.md) adds the twelfth procedure, leaving eleven pending. Availability paragraphs now list it; route triggers, existing procedures, setup defaults and model resolution remain unchanged. The [evaluation](../evaluations/visual-parity/README.md) records exact screenshot comparisons and explicit missing-baseline behavior.

## Opening a PR coverage

[Opening a PR](opening-a-pr.md) adds the thirteenth procedure, leaving ten pending. Availability paragraphs and seven existing callers now reach it; original caller algorithms, roles and setup behavior remain unchanged. Publication authority remains separate from local preparation, monitoring and merging. See the [evaluation](../evaluations/opening-a-pr/README.md).

## Babysit availability

The mode now bundles Babysit and its single-pass watcher, bringing the current count to 14 available procedures and nine pending. See the [Babysit adaptation](babysit.md) and [evaluation](../evaluations/babysit/README.md). Model roles, configuration selection and source pins are unchanged.

## Shipping availability

Shipping is now the fifteenth bundled procedure; eight remain pending. See the [Shipping adaptation](shipping.md) and [evaluation](../evaluations/shipping/README.md). This changes availability and caller links only; configuration roles, selection, pins and existing adaptations are unchanged.

## Multi-phase plan availability

Multi-phase plan and its structural checker are now bundled, bringing coverage to 16 procedures with seven pending. See the [adaptation](multi-phase-plan.md) and [evaluation](../evaluations/multi-phase-plan/README.md). Configuration roles, selection, source pins and the reviewed checkpoint are unchanged. Execution through either Autopilot or Orchestrate remains unavailable.

## Session pickup availability

Session pickup is now the seventeenth procedure, with six pending. See its [adaptation](session-pickup.md) and [evaluation](../evaluations/session-pickup/README.md). Model roles, configuration lookup, pins and reviewed checkpoint are unchanged.
