# Jstack implementation plan

Original research: 2026-10-06. Updated: 2026-10-10. Status: `setup-jstack` shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). The configuration helper is implemented; `juan-mode` and its execution routes remain proposed. Historical audit and evaluation pins below are unchanged.

## Intended experience

Configure model roles once with `setup-jstack`, then invoke `juan-mode` for a task. The mode reads that configuration, selects the upstream playbook, reads applicable principle leaves, and routes internal workflows through T3-owned tasks. `setup-jstack` is an installable portable skill. `juan-mode` is the planned workflow entrypoint; it is not implemented or registered by this plan.

The first proposed workflow release will support read-only Investigation through `how`. A motivation question additionally needs `why`; do not advertise that route until its evidence-category mapping works. Other upstream routes remain explicitly unavailable in the first release. This is a staged port of the central entrypoints, not a full pstack release.

## Evidence and baseline

- Audit pin: `cursor/plugins` commit `df581122cde17e6e27686b5a448bde23e4ad4318`, pstack 0.15.15. [Manifest](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/.cursor-plugin/plugin.json).
- [Inventory](./pstack-t3-upstream-inventory.json): paths, byte counts, and SHA-256 hashes for 164 files, including 51 skill entrypoints, 24 principle leaves, and 23 mode playbooks. It records source content, not a proven execution dependency graph.
- [Dependency map](./pstack-t3-dependency-map.md): entrypoints, routed skills, external dependencies, and classification.
- [Setup](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/setup-pstack/SKILL.md) writes Cursor role rules; [mode](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/SKILL.md) consumes roles, principles, and playbooks.
- [Investigation](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/playbooks/investigation.md) routes through `how`, optionally `why`, and `unslop`. [How](https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/how/SKILL.md) uses one direct explainer for simple questions or 2–4 partitioned explorers followed by an explainer for complex questions. It is not an Arena bakeoff.
- Existing [manual panel](../evaluations/pstack-t3-review.md) and [fresh-parent panel](../evaluations/pstack-t3-review-parent.md) demonstrate selected T3 delegation mechanics only. Their baseline remains `e5a8186...`; do not update it silently or describe them as tests of full mode routing.
- Current callable T3 schemas and injected orchestration instructions are the operational authority. [T3 source](https://github.com/pingdotgg/t3code/blob/main/apps/server/src/provider/T3OrchestrationInstructions.ts) is a moving reference; implementation must capture its audited revision and revalidate against the installed runtime rather than infer support from a release label.
- [Selected live capabilities](./pstack-t3-capabilities-snapshot.json) record the features observed on 2026-10-06 and Codex/Claude candidate model option schemas. This intentionally filtered snapshot is not the entire provider catalog and must not be used as a permanent allowlist.

## Packaging and source ownership

Maintain an immutable source pin and a small explicit adapter set. Keep fetched upstream in a cache outside the installable skills tree; do not register all upstream Cursor skills automatically. Preserve its MIT notice in distributed adapted material.

Proposed adapter layout, alongside the shipped setup skill:

```text
adapters/jstack/
  upstream.lock.json       Repository, commit, version, content hashes
  routes.json              Declared dependency and support registry
  transforms/              Explicit adaptations with checked expectations
  scripts/                 Fetch, build, validate, and update tools
skills/setup-jstack/        Shipped authored setup skill and configuration helper
skills/juan-mode/           Proposed mode and supported dependency closure
evaluations/               Execution records and fixture results
```

Create files only when the implementation needs them. Generated installed views must be self-contained. Existing skill-installation methods may install one folder without siblings, so a relative pointer outside that folder is insufficient. Materialize required references under the generated mode view, with a skill-ID-to-path registry. Plain reference filenames can avoid registering nested upstream entrypoints as additional skills; validate actual discovery behavior rather than assume it.

Unchanged leaves may remain byte-identical in the cache. Where generated packaging renames paths or metadata, record that separately from semantic changes. Every transformed file needs a source path, source hash, transformation identifier, and output hash. Reject changed inputs that no longer satisfy an expected transformation. Preserve the old generated version when updates fail.

This reduces a broad manual content fork; it does not remove responsibility for inspecting orchestration changes. Do not use a blanket instruction to ignore conflicting upstream instructions. Replace the affected execution boundaries in the generated view.

## Persistent model configuration

The shipped setup resolves `JSTACK_CONFIG` when supplied, otherwise `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`. See the [configuration contract](../skills/setup-jstack/references/configuration.md). Keep machine-specific provider assignments outside this repository. This is our configuration, not a T3-owned or automatically loaded rules file.

The shipped schema contains only `schemaVersion`, `preset`, and `roles`. Keep source pins and route support status in package references or a future route registry, outside the user model configuration. A concrete seat stores `providerInstanceId`, `model`, and validated provider-specific `options`. A panel role stores an ordered seat list; a judge pool stores selectable seats, not simultaneous fan-out. An inheritance alias stores no concrete model and resolves against the executing parent. Map model family separately from provider instance because one provider may expose several families.

The shipped canonical registry preserves all 17 grouped upstream role names. Consumers must declare supported routes separately; configured roles do not imply executable workflows. First Investigation execution needs `how explorer` and `how explainer`; `why investigators` and `why synthesizer` are needed for the later motivation branch.

Setup calls `orchestrator_capabilities`, reads existing state, presents reasoning preset and assignments, validates against runnable providers/models/options, and writes atomically after the user's choices. Re-running preserves explicit overrides and reports removed or unavailable assignments. Do not choose paid model substitutions silently. No API keys belong in this file.

Upstream labels map `small` to medium effort, `medium` to high, `large` to xhigh, and `unlimited` to max. Preserve that meaning in the UI, but map to each provider's actual option ID and advertised values. T3 often separates effort from the model ID; never append Cursor effort suffixes to a T3 model ID. Resolve unsupported effort deliberately and display any downgrade. Inheritance semantics need verification against the runtime rather than treating `auto` as a universally equivalent provider mode.

Do not infer a permanent default from our earlier Astra/Opus experiments. Ask for reasoning preset and role choices during the actual setup phase. Show which roles will execute and the likely fan-out; a reasoning preset is not a monetary cap.

## Mode, loading, and child grounding

Each invocation reads the local model configuration and installed dependency registry. Select the playbook before dispatch; retain its ordered steps and recorded skips. Load principle leaves when their triggers apply, and cite only principles actually read during that session. Retain upstream task-specific output contracts, including Investigation's throughput checkpoint.

T3 does not register `subagent_type: poteto-agent` through a copied Markdown file. Replace that wrapper with explicit child bootstrap instructions that point to the installed mode and needed references. Pass original scope, later directives, evidence pointers, selected route, support boundaries, and configuration location. Give `how` explorer and explainer roles their prescribed specialized prompts; do not make them redispatch the parent Investigation recursively.

Use fresh T3 delegation rounds with distinct request IDs and retained task IDs. Grounding paths must be absolute or resolved before dispatch. Children do not receive parent conversation history. Complete results must be collected before the next dependent phase. Use completion notifications rather than polling. Read-only is an instruction boundary until actual permissions are verified.

Mode persistence across turns is unresolved. Cursor's custom-mode UI and reminder metadata do not automatically carry over. The first release uses explicit invocation, including after compaction or a fresh task where loading is uncertain. A later mechanism must be demonstrated before promising a persistent mode.

Missing principle or prompt references, stale configuration, or an unsupported route produce an explicit unavailable result before work starts. Report partial results and missing seats if a runtime fails; do not present incomplete exploration as full coverage.

## Host and policy boundaries

The user's and repository's instructions remain authoritative. Adapt upstream autonomy text wherever it grants broader external-action permission. A read-only Investigation must not post chat messages, mutate tickets, push branches, or create PRs. A future shipping route must preserve explicit approval requirements and use T3 PR linking/watch operations where available.

Principle applicability does not grant extra actions. For example, Build the Lever requires a produced tool artifact before citing it; a read-only Investigation cannot invoke that requirement to write files. Never Block on the Human needs policy adaptation in its leaf as well as in the mode's autonomy section.

Replace Cursor transcript paths with reads of specifically owned T3 threads; never scan unrelated private sessions. Map browser work to T3's collaborative preview tools. Do not claim preview inspection is a general replacement for CLI/TUI control. A project verification-skill generator remains a later route.

Writing candidates, cloud placement, worktree handoff, orchestration stores, PR queues, scheduled loops, and simulator cleanup require separate adapters and tests. `delegate_task` inheriting the parent's checkout is not isolated writing. Top-level workspace launches remain a separate, explicitly requested operation. Upstream's watcher and orchestration scripts are not T3 task lifecycle substitutes.

## Implementation sequence and acceptance gates

1. **Source and dependency tooling.** Fetch the exact pin with hashes, retain license, resolve every dependency in the selected route, and generate a support report. Checks must catch a missing leaf, changed source hash, and an incompatible transformation. No automatic provider installation.
2. **Setup entrypoint: shipped.** Configuration reading, live catalog validation, explicit role choices, and atomic writing are implemented. Six helper tests and structural validation passed for the release. This is not proof of every provider interaction or the future mode workflow. Keep repeat-setup, provider ambiguity, unavailable seats, effort mapping, aliases, and changing catalogs in future setup evaluation coverage. No live delegation is needed to configure roles.
3. **Mode and Investigation/how.** Generate the adapted mode, supported playbook, principle closure, unslop, and specialized how prompts. Preserve simple versus complex routing. Static checks catch unresolved names, Cursor execution fields, outside-folder paths, and competing autonomy rules.
4. **End-to-end execution.** Run setup in an isolated user-config location, then a fresh agent invokes mode on a disposable repository fixture. Inspect actual thread activity for config reads, mode/playbook/leaf reads, selected models, explorer partitioning, dependent explanation, and cited real code. Test a simple question and a complex one. Candidate/explainer prompts are organic task requests; the evaluator holds the hidden grading rubric. Preserve failure records and the generated outputs.
5. **Motivation branch.** Adapt why's evidence-category discovery and prompts. Test missing sources, source-control-only evidence, and any available MCP-dependent child access. Report unavailable categories; never invent intent from runtime structure alone.
6. **Installable pilot.** Verify discovery and reference resolution for the coordinating provider, then test cross-provider children reading the packaged files. Describe precisely which providers were tested. Leave inactive routes visibly disabled. Installation follows implementation and evaluation; publishing or pushing requires the applicable approval.

The current panel tests are workflow smoke tests, not blinded upstream Eval runs: their candidates were told their role and asked to acknowledge files. Future promotion evaluation should inspect real read activity under a task-shaped fixture and keep evaluation metadata away from the execution agent. Judge labels must omit model identities. A cross-judge is not required for every how invocation; follow how's actual routing.

## Decisions and outstanding questions

Proceed with the central entrypoints and a supported Investigation/how subset. Keep the earlier panel as evidence and a possible later Arena adapter, not as a replacement for how. Preserve upstream content and role names where possible; adapt host assumptions explicitly.

Before the installer phase, determine each provider's discovery behavior and whether children can read the generated shared references in its runtime. Before motivation investigations, demonstrate MCP availability in the chosen child provider. Before writing workflows, settle workspace isolation and lifecycle completion. Before persistent mode, demonstrate reload behavior across turns and compaction. These uncertainties do not invalidate the shipped setup helper; resolve them before promoting the corresponding consumer routes.

The dependency audit also found an upstream forge inconsistency: Opening a PR and autopilot say not to require Graphite, while Orchestrate's stack safety still depends on `gt` metadata. Resolve that contract before enabling Orchestrate; do not choose a silent replacement during this first slice.
