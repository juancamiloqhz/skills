---
name: jstack-setup
description: Configure jstack model assignments and reasoning budgets for T3 Code workflow roles. Use when setting up jstack or changing its model routing.
---

# Setup jstack

Configure jstack's model routing through T3 Code's live catalog. Save global defaults or an optional project configuration. This skill does not install providers, launch agents, or change the current model. After saving, it can offer a separate project-local verification task.

The bundle is named `jstack`. Its workflow entrypoint is `jstack-juan-mode`, the counterpart to pstack's `poteto-mode`. Juan-mode provides an execution foundation and the Investigation, Prototype, Trace forensics, Authoring or modifying a skill, Runtime forensics, Bug fix, Feature, Refactoring, Perf issue, Hillclimb, Eval, Visual parity, Opening a PR and Babysit playbooks; its other 9 playbook procedures remain unavailable.

## Steps

### 1. Detect available models

Call `orchestrator_capabilities` through the available T3 Code MCP tool. Use its current provider instances, models and option schemas, including custom models. If the tool is absent from discovery, make one direct attempt. For catalog capture, ACP's documented transport fallback and tool semantics, read [T3 Code integration](references/t3-code.md). If discovery remains unavailable, report that setup cannot validate concrete assignments; preserve the existing configuration.

### 2. Load current state

Read the [configuration contract](references/configuration.md) for shared lookup, scope selection, roles and consumer behavior. Run the installed helper's `locate` command to report the effective file. Use the task's project root with `--project-root` when known; the installed skill directory is not the target project. Honor an explicit configuration path or `JSTACK_CONFIG` unless the user requests a different scope.

When scope is not already specified, offer global defaults or this project. Show the effective file and suggest its current scope. Use `locate --scope global` or `locate --scope project --project-root PROJECT` to obtain the chosen write target. These explicit scope queries ignore other overrides. Read that target before proposing changes. Project setup is optional; an ordinary workflow does not create `.jstack/models.json`.

For a new project configuration, seed a temporary draft from the complete global configuration when it exists. Obtain that seed with `locate --scope global`, so an environment override cannot accidentally become the global seed. Preserve all 17 roles, options, list entries and budget, then apply only the requested edits. If no global file exists, start with the inherited template. Report invalid existing or seed configuration for repair instead of silently replacing it. Keep credentials out of model configuration; provider identities still need validation on each machine.

### 3. Budget, map, and confirm

**(a) Ask for a budget.** Ask for a reasoning budget unless the request already specifies it. Prefer the host question tool when available. Offer these labels and name the current budget when recorded:

- `unlimited — max reasoning`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

With no existing configuration, the inherited draft uses `medium`; confirm the user's budget before saving. That label does not override inherited effort. This is a setup convenience for adjusting reasoning across roles, not a dollar limit or spending cap. Unlimited targets max where supported; it does not promise unbounded reasoning. For an existing configuration, show the budget recorded in `preset` and any effective effort exceptions. Keep the schema field and CLI flag named `preset` for compatibility.

**(b) Apply it.** For a first setup, propose `inherit-parent` for every role until the user selects concrete models. Do not assume pstack's Grok/Opus preferences are Juan's choices. On repeat setup, retain existing assignments and options unless the user requests a change. A rerun can update selected roles or every role, including model and effort. When applying a budget, show which concrete seats would change and resolve the scope and any effort overrides to retain. An explicit request to apply a budget to all concrete seats includes panel entries and judge alternatives; preserve model identities, other options, list order and list sizes unless the user requests those changes. Inherited seats stay inherited unless the user explicitly replaces them. Do not change existing options merely because a saved budget is present. The configuration records effective options, not the history of how they were chosen. Report unknown roles or unsupported versions instead of silently dropping them.

Concrete assignments specify a provider instance, model ID and provider-specific options. Keep reasoning separate from model IDs. Apply the requested reasoning budget to the selected seats' advertised effort options, such as `reasoningEffort`, `effort`, `reasoning_effort` or `variant`; inspect their values rather than assuming equivalent semantics. Preserve explicitly requested per-role effort overrides. If the provider lacks the target level, propose its highest advertised level at or below the target and disclose the downgrade. If no supported level qualifies or the option's meaning is ambiguous, mark the role as needing a choice and ask. Do not write unavailable model or option values.

Distinguish `inherit-parent` from provider Auto. Inheritance omits the delegation target and preserves the executing parent's selection. Auto is a concrete provider/model from the live catalog, such as Cursor's advertised Auto model; it is not a portable alias.

**(c) Show the roles and confirm.** Show all 17 roles from step 5 with their proposed models and effort, mark unavailable choices, and offer the detected models or inheritance. Panel roles hold ordered seat lists, with one agent per seat, including repeated or inherited seats. The cross-judge pool holds alternatives from which a workflow selects one judge. Arena selects a judge from a different model family than the parent when possible. `swarm workers` supplies the default for every worker unless a race or comparison assigns a model per arm. Show list sizes and explain that setup itself launches none. Execution is supplied by installed consumer skills such as jstack-how, jstack-why, jstack-arena and jstack-architect. For new configurations without an existing seed, default to two inherited seats in each of `arena runners`, `architect runners` and `interrogate reviewers`. These are two separate agents using the parent model and effort, not different model families. The cross-judge pool starts with one inherited alternative; duplicating it would not supply a different-family judge. Existing configurations and global seeds retain their counts unless the user requests a change. A one-seat saved panel remains valid configuration but insufficient for Arena or Architect comparison; report that requirement instead of silently adding a seat.

Present the chosen scope and concrete file path, reasoning budget and target effort, assignments, effort exceptions and changed roles. Resolve user choices before writing; when the request already specifies the scope and mapping, proceed without asking again.

### 4. Validate

Prepare the proposed JSON and a temporary JSON copy of the full capabilities payload. Run the helper with Python 3 from the installed skill directory. Use `python3 scripts/models.py validate DRAFT --catalog CATALOG` to check the complete configuration, including every provider, model and option. Unavailable existing seats need an explicit replacement or inheritance choice; never silently substitute another paid model.

### 5. Write the configuration

Save with `python3 scripts/models.py write DRAFT --catalog CATALOG --output CONFIG` using the chosen target, which validates and replaces that file atomically.

Write the complete file idempotently. The inherited first-run shape is below; `preset` records the selected budget and the three panels each contain two seats. Generate a draft with `python3 scripts/models.py template --preset CHOSEN_BUDGET`, then apply the confirmed selections. Do not replace an existing or seeded map with this example.

```json
{
  "schemaVersion": 1,
  "preset": "medium",
  "roles": {
    "feature, refactoring": {"alias": "inherit-parent"},
    "bug-fix": {"alias": "inherit-parent"},
    "perf-issue": {"alias": "inherit-parent"},
    "hillclimb": {"alias": "inherit-parent"},
    "judgment and prose": {"alias": "inherit-parent"},
    "hardest tasks": {"alias": "inherit-parent"},
    "how explorer": {"alias": "inherit-parent"},
    "how explainer": {"alias": "inherit-parent"},
    "why investigators": {"alias": "inherit-parent"},
    "why synthesizer": {"alias": "inherit-parent"},
    "reflect tooling": {"alias": "inherit-parent"},
    "reflect judgment, divergent, synthesizer": {"alias": "inherit-parent"},
    "arena runners": [{"alias": "inherit-parent"}, {"alias": "inherit-parent"}],
    "arena cross-judge pool": [{"alias": "inherit-parent"}],
    "swarm workers": {"alias": "inherit-parent"},
    "architect runners": [{"alias": "inherit-parent"}, {"alias": "inherit-parent"}],
    "interrogate reviewers": [{"alias": "inherit-parent"}, {"alias": "inherit-parent"}]
  }
}
```

### 6. Confirm

Read the saved file back and report exactly what changed. Run `locate` again to show the effective lookup result; explain when an environment, explicit or project override still takes precedence over the file just saved. Preserve files in the other scope and remove temporary catalog/draft files when finished.

Explain that the saved `preset` records the setup choice; the resolver uses each seat's effective options and never reapplies the budget. Editing only `preset` does not change any role's effort. Consumers must read the configuration at invocation time and revalidate against the current catalog. It is not a rule managed by T3 Code or an automatically loaded mode. Installation and slash-command discovery depend on the coordinating provider; source authoring alone does not register `/jstack-setup`.

### 7. Offer a verification skill (optional)

After saving and reporting the model configuration, inspect the known target project's instructions, documented user interface, existing `verify-*` skills and verification tooling. This inspection is read-only; do not launch the app or run its tests merely to decide whether to offer generation. If no target project is known, the repository has no executable product, or an existing skill or harness already covers real user paths, skip the offer and briefly say why. Unit tests alone do not necessarily cover those paths, and an existing harness need not have a `verify-*` name.

If verification support is missing, offer once to generate a project-local skill that exercises the app, retains proof and cleans up its test state. A decline or unanswered offer leaves model setup complete; do not generate files or repeatedly ask in the same setup run. If the user has already requested generation for this project, proceed without asking again. Their acceptance authorizes the generator task under the existing repository and user permissions; it does not grant additional external-action permission.

On acceptance, resolve `jstack-create-verification-skill` from the current skill catalog or an explicitly supplied source path, read its `SKILL.md`, and follow it for the target repository with the known constraints. Do not assume a sibling directory exists when setup was installed on its own, invent a slash-command tool, or substitute another generator. If it is unavailable, report that model setup succeeded and provide this command for the user to run manually, then resume generation only once the skill is available:

```sh
npx skills add juancamiloqhz/skills --skill jstack-create-verification-skill --global
```

Never execute installation or updates on the user's behalf. Keep the saved model configuration intact whether the offer is declined, the generator is missing, or generation fails. Report the generator's outcome separately, including draft status or untested behavior. Maintenance of existing verification support is a separate task.

Model routing provides configuration validation/resolution; it does not execute the configured workflow roles. The optional verification task is handled by the separately available generator. User and repository instructions govern execution permissions; model routing grants none. No live delegation is needed to configure roles.
