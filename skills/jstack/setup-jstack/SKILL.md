---
name: setup-jstack
description: Configure jstack model assignments and reasoning budgets for T3 Code workflow roles. Use when setting up jstack or changing its model routing.
---

# Setup jstack

Configure jstack's model routing through T3 Code's live catalog. This skill writes a user-local configuration for future jstack workflows. It does not install providers, launch agents, or change the current model. After saving, it can offer a separate project-local verification task.

The bundle is named `jstack`. Its planned workflow entrypoint is `juan-mode`, the counterpart to pstack's `poteto-mode`; that consumer is not implemented yet.

## Discover and load

Call `orchestrator_capabilities` through the available T3 Code MCP tool. Use its current provider instances, models and option schemas, including custom models. If the tool is absent from discovery, make one direct attempt. For ACP's documented transport fallback and tool semantics, read [T3 Code integration](references/t3-code.md). If discovery remains unavailable, report that setup cannot validate concrete assignments; preserve the existing configuration.

Resolve the configuration path from `JSTACK_CONFIG` when explicitly supplied, otherwise `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`. Read existing state before proposing changes. Read the [configuration contract](references/configuration.md), which defines roles, aliases and consumer behavior. Keep credentials and host-specific selections outside the skills repository.

## Choose routing

Ask for a reasoning budget unless the request already specifies it. Keep pstack's labels and show their target effort: `unlimited = max`, `large = xhigh`, `medium = high`, `small = medium`. This is a setup convenience for adjusting reasoning across roles, not a dollar limit or spending cap. Unlimited targets max where supported; it does not promise unbounded reasoning. For an existing configuration, show the budget recorded in `preset` and any effective effort exceptions. Keep the schema field and CLI flag named `preset` for compatibility.

For a first setup, propose `inherit-parent` for every role until the user selects concrete models. Do not assume pstack's Grok/Opus preferences are Juan's choices. Group related roles for a readable selection, then show all 17 assignments before writing. On repeat setup, retain existing assignments and options unless the user requests a change. A rerun can update selected roles or every role, including model and effort. When applying a budget, show which concrete seats would change and resolve the scope and any effort overrides to retain. An explicit request to apply a budget to all concrete seats includes panel entries and judge alternatives; preserve model identities, other options, list order and list sizes unless the user requests those changes. Inherited seats stay inherited unless the user explicitly replaces them. Do not change existing options merely because a saved budget is present. The configuration records effective options, not the history of how they were chosen. Report unknown roles or unsupported versions instead of silently dropping them.

Concrete assignments specify a provider instance, model ID and provider-specific options. Keep reasoning separate from model IDs. Apply the requested reasoning budget to the selected seats' advertised effort options, such as `reasoningEffort`, `effort`, `reasoning_effort` or `variant`; inspect their values rather than assuming equivalent semantics. Preserve explicitly requested per-role effort overrides. If the provider lacks the target level, propose its highest advertised level at or below the target and disclose the downgrade. If the option's meaning is ambiguous, ask for a choice. Do not write unavailable model or option values.

Distinguish `inherit-parent` from provider Auto. Inheritance omits the delegation target and preserves the executing parent's selection. Auto is a concrete provider/model from the live catalog, such as Cursor's advertised Auto model; it is not a portable alias.

Panel roles hold ordered seat lists, with one agent per seat, including repeated or inherited seats. The cross-judge pool holds alternatives from which a workflow selects one judge. Show list sizes and explain that setup itself launches none. All execution routes remain unavailable until a consumer skill implements them.

## Validate and save

Prepare the proposed JSON and a temporary JSON copy of the full capabilities payload. Run the helper with Python 3 from the installed skill directory. Use `python3 scripts/models.py validate DRAFT --catalog CATALOG` to check the complete configuration, including every provider, model and option. Unavailable existing seats need an explicit replacement or inheritance choice; never silently substitute another paid model.

Present the concrete file path, reasoning budget and target effort, assignments, effort exceptions and changed roles. Resolve user choices before writing; when the request already specifies the full mapping, proceed without asking again. Save with `python3 scripts/models.py write DRAFT --catalog CATALOG --output CONFIG`, which validates and replaces the file atomically. Read the saved file back and report exactly what changed. Remove temporary catalog/draft files when finished.

Explain that the saved `preset` records the setup choice; the resolver uses each seat's effective options and never reapplies the budget. Editing only `preset` does not change any role's effort. Consumers must read the configuration at invocation time and revalidate against the current catalog. It is not a rule managed by T3 Code or an automatically loaded mode. Installation and slash-command discovery depend on the coordinating provider; source authoring alone does not register `/setup-jstack`.

## Offer project verification, optionally

After saving and reporting the model configuration, inspect the known target project's instructions, documented user interface, existing `verify-*` skills and verification tooling. This inspection is read-only; do not launch the app or run its tests merely to decide whether to offer generation. If no target project is known, the repository has no executable product, or an existing skill or harness already covers real user paths, skip the offer and briefly say why. Unit tests alone do not necessarily cover those paths, and an existing harness need not have a `verify-*` name.

If verification support is missing, offer once to generate a project-local skill that exercises the app, retains proof and cleans up its test state. A decline or unanswered offer leaves model setup complete; do not generate files or repeatedly ask in the same setup run. If the user has already requested generation for this project, proceed without asking again. Their acceptance authorizes the generator task under the existing repository and user permissions; it does not grant additional external-action permission.

On acceptance, resolve `create-verification-skill` from the current skill catalog or an explicitly supplied source path, read its `SKILL.md`, and follow it for the target repository with the known constraints. Do not assume a sibling directory exists when setup was installed on its own, invent a slash-command tool, or substitute another generator. If it is unavailable, report that model setup succeeded and provide this command for the user to run manually, then resume generation only once the skill is available:

```sh
npx skills add juancamiloqhz/skills --skill create-verification-skill --global
```

Never execute installation or updates on the user's behalf. Keep the saved model configuration intact whether the offer is declined, the generator is missing, or generation fails. Report the generator's outcome separately, including draft status or untested behavior. Maintenance of existing verification support is a separate task.

## Scope and provenance

Model routing provides configuration validation/resolution; it does not execute the configured workflow roles. The optional verification task is handled by the separately available generator. User and repository instructions govern execution permissions; model routing grants none. No live delegation is needed to configure roles.

This adapts pstack's setup concept and role registry. See [upstream attribution](references/upstream.md) for the pinned source and license. It is not an official Cursor or T3 Code integration.
