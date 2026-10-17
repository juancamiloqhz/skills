# Jstack configuration contract

Schema version 1 is owned by jstack, not T3 Code. The canonical role registry is `ROLES` in `scripts/models.py`; `template` generates all 17 roles with inherited selections. Grouped labels preserve pstack's role names. Missing, extra or misspelled roles are errors, so setup cannot silently discard a user's mapping.

```sh
python3 scripts/models.py template --preset medium > /tmp/jstack-draft.json
python3 scripts/models.py validate /tmp/jstack-draft.json --catalog /tmp/t3-catalog.json
python3 scripts/models.py write /tmp/jstack-draft.json \
  --catalog /tmp/t3-catalog.json --output /tmp/jstack-test/models.json
python3 scripts/models.py resolve /tmp/jstack-test/models.json \
  --catalog /tmp/t3-catalog.json --role 'how explorer'
```

Locate bundled scripts relative to the installed skill directory. Relative configuration and catalog paths use the caller's working directory. The catalog file contains the unwrapped `orchestrator_capabilities` payload, not an MCP content wrapper or a permanent allowlist.

## Configuration location and setup scope

`scripts/models.py` owns lookup for setup and consumers. Select the first applicable file in this order:

1. An explicit file, supplied to `locate --config PATH` or as `resolve PATH`.
2. A nonempty `JSTACK_CONFIG` environment variable.
3. `<project_root>/.jstack/models.json`, when present.
4. `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`.

Use `--project-root` for the task's known root, including a project without Git. Otherwise the helper discovers the current Git checkout root from the caller's working directory, including nested directories and linked worktrees. Outside a Git checkout it uses global defaults. It does not search parent repositories for additional `.jstack` files or infer the project from the installed skill path. An invalid explicit project root is an error when project lookup is needed.

```sh
python3 /installed/jstack-setup/scripts/models.py locate --project-root /path/to/project
python3 /installed/jstack-setup/scripts/models.py resolve \
  --project-root /path/to/project --catalog /tmp/t3-catalog.json \
  --role 'how explorer' --with-source
```

`locate` returns an absolute `path`, its `source` and whether an entry `exists`. It selects without creating files or validating their contents. `resolve --with-source` returns `config`, `configSource` and `targets` after validating the selected complete configuration. Without `--with-source`, `resolve` retains its ordered-list output. Explicit and environment selections remain selected when missing. A present project file that is malformed, partial, unreadable, a directory or a dangling symlink fails resolution; it does not fall back to global settings.

Each file contains the complete schema-version-1 configuration. Project selection replaces the global map as a whole; there is no role or option merge. `inherit-parent` retains the executing conversation's provider, model and effort, and does not refer to the global role assignment.

For setup, `locate --scope global` and `locate --scope project --project-root PROJECT` return the intended save path even before it exists. They ignore `JSTACK_CONFIG` and effective-file precedence because the user has selected a destination. `--scope` and `--config` are mutually exclusive. A new project draft starts from the complete global file when available, otherwise from `template`. Keep this draft in an owned temporary file until edits and validation are complete, then pass the chosen absolute destination to `write --output`. Updating one scope leaves the other untouched. A higher-priority override may still shadow a newly saved global file; show the effective selection after saving.

Before changing checkout or delegating, retain the selected absolute `config` path. Pass it as the child's explicit configuration path and revalidate the current file there. Git does not copy an untracked project configuration into a new worktree; rediscovering from the child checkout could otherwise select a different file. The selected path fixes file choice, not contents or model choices across future invocations. New top-level tasks repeat lookup in their own project context.

## Data shape

Top-level fields remain `schemaVersion`, `preset` and `roles` in schema version 1. The UI calls `preset` the reasoning budget. Retain the field and `--preset` flag for compatibility with existing jstack configurations.

The budget labels follow pstack: `unlimited` targets `max`, `large` targets `xhigh`, `medium` targets `high`, and `small` targets `medium`. They express a setup preference for reasoning expenditure, not monetary limits. Setup maps the target to each selected model's advertised effort options and discloses unsupported levels or downgrades.

Each concrete seat's `options` is authoritative. The validator checks those options against the live catalog, not whether every seat matches the recorded budget. The resolver ignores `preset`: changing that field alone changes no delegation target. For example, `preset: "unlimited"` may coexist with a max-effort seat, a seat limited to xhigh by its model, and a deliberately retained medium-effort override. An inherited seat preserves the executing parent's model and effort.

On a rerun, setup can update one role, several roles, or all roles. Applying a budget materializes the chosen effort into the affected concrete seats, including list entries, before validation and saving. It preserves model choices, unrelated options, and list structure unless requested otherwise. Keep inherited seats unchanged unless explicitly replaced. Resolve which existing effort overrides to retain; the file does not record why a particular option was chosen. There is no automatic runtime budget enforcement or separate per-role preset.

An inherited seat is exactly:

```json
{"alias": "inherit-parent"}
```

A concrete seat is:

```json
{
  "providerInstanceId": "codex",
  "model": "gpt-6.1-sol",
  "options": {"reasoningEffort": "high"}
}
```

This model is illustrative; setup must verify it in the live catalog. Empty options preserve provider defaults. Model identity includes the provider instance: identical model IDs across providers are distinct seats. Extra fields and aliases such as `auto` are rejected. Provider Auto is a concrete catalog selection.

Scalar roles have one seat. `arena runners`, `architect runners` and `interrogate reviewers` have nonempty ordered lists. `arena cross-judge pool` also has a nonempty list, but a consumer selects one seat rather than launching the whole pool. A new template uses two inherited seats per panel and one inherited alternative in the cross-judge pool. Two inherited panel seats launch separate agents, not different model families. Existing configurations and copied global seeds retain their list lengths; setup changes those counts only when requested. The template budget defaults to medium as a draft value, and setup asks for the actual budget before saving. `swarm workers` is a scalar default for workers, not the worker count.

## Consumer contract

Every invocation reads and validates current configuration before dispatch. Validation covers the entire map; stale seats produce a configuration error before execution, even when they belong to another role. Setup can repair those seats. The helper's `resolve` command emits an ordered list of T3 Code delegation targets; JSON `null` means omit `target` to inherit the parent. For top-level launches, translate a concrete target into `modelSelection` using the current tool schema; omission inherits the caller's selection.

The standalone jstack-how and jstack-why consumers also follow the [investigation contract](investigation.md) for capability checks, evidence and child coordination. Resolving a role does not authorize or launch it. Each consumer must declare which routes it implements, preserve permission boundaries, and pass explicit task context. Follow T3 Code's child-task lifecycle and new-thread rules in [T3 Code integration](t3-code.md). Standalone Arena and Architect supply their own comparison and design procedures. Juan-mode supplies Investigation, throwaway Prototype, captured-artifact Trace forensics, Authoring or modifying a skill, Runtime forensics, Bug fix, Feature, Refactoring, Perf issue, Hillclimb, Eval, Visual parity, Opening a PR, Babysit, Shipping, Multi-phase plan, Session pickup, Pause safely, Worktree cleanup, Autonomous run and Autopilot-full. Shipping is available with independent verification and current-patch evidence; native continuation across stack merges remains unverified.

Configuration is loaded by consumers, not by T3 Code itself. Re-running setup updates the selected scope; consumers see changes on their next invocation when that file is effective. Repository instructions or installation can make the skill discoverable, but do not turn the configuration into a persistent system rule.

## Task-local Swarm arm selections

`swarm workers` is the saved default, not a restriction to one model for every arm of an explicitly assigned model race. A user or authorized caller can supply an exact task-local seat using the same inherited or concrete schema. `resolve --role 'swarm workers' --worker-override ARM_JSON` validates the complete selected configuration first and then the override against the catalog. It returns a one-element target list without writing settings; unavailable or malformed overrides fail instead of falling back. This flag is only valid for `swarm workers`.

With `--with-source`, `config` and `configSource` still identify the saved defaults. The task record and child brief retain the explicit override separately. Passing no override preserves ordinary resolution. An override cannot bypass a stale unrelated role, alter other workflow roles, change saved budgets or migrate settings. It grants no execution authority; Swarm owns the supplied task's dispatch and capability checks.
