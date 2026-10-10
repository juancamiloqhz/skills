# Jstack configuration contract

Schema version 1 is owned by jstack, not T3. The canonical role registry is
`ROLES` in `scripts/models.py`; `template` generates all 17 roles with inherited
selections. Grouped labels preserve pstack's role names. Missing, extra or
misspelled roles are errors, so setup cannot silently discard a user's mapping.

```sh
python3 scripts/models.py template --preset medium > /tmp/jstack-draft.json
python3 scripts/models.py validate /tmp/jstack-draft.json --catalog /tmp/t3-catalog.json
python3 scripts/models.py write /tmp/jstack-draft.json \
  --catalog /tmp/t3-catalog.json --output /tmp/jstack-test/models.json
python3 scripts/models.py resolve /tmp/jstack-test/models.json \
  --catalog /tmp/t3-catalog.json --role 'how explorer'
```

Resolve paths relative to the installed skill directory. The catalog file
contains the unwrapped `orchestrator_capabilities` payload, not an MCP content
wrapper or a permanent allowlist.

## Data shape

Top-level fields are `schemaVersion`, `preset` and `roles`. Presets are `small`,
`medium`, `large` and `unlimited`. They record the requested effort policy;
effective provider-specific options in each concrete seat are authoritative. The
validator checks those options against the live catalog, not whether every seat
matches the preset, because explicit overrides and disclosed downgrades are
valid.

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

This model is illustrative; setup must verify it in the live catalog. Empty
options preserve provider defaults. Model identity includes the provider
instance: identical model IDs across providers are distinct seats. Extra fields
and aliases such as `auto` are rejected. Provider Auto is a concrete catalog
selection.

Scalar roles have one seat. `arena runners`, `architect runners` and
`interrogate reviewers` have nonempty ordered lists. `arena cross-judge pool`
also has a nonempty list, but a consumer selects one seat rather than launching
the whole pool. The template uses one inherited seat per list; setup changes
fan-out only when requested. `swarm workers` is a scalar default for workers,
not the worker count.

## Consumer contract

Every invocation reads and validates current configuration before dispatch.
Validation covers the entire map; stale seats produce a configuration error
before execution, even when they belong to another role. Setup can repair those
seats. The helper's `resolve` command emits an ordered list of T3 delegation
targets; JSON `null` means omit `target` to inherit the parent. For top-level
launches, translate a concrete target into `modelSelection` using the current
tool schema; omission inherits the caller's selection.

Resolving a role does not authorize or launch it. A future consumer must declare
which routes it implements, preserve permission boundaries, and pass explicit
task context. Follow T3's child-task lifecycle and new-thread rules in [T3
integration](t3.md). This release implements no Investigation, Arena, shipping
or issue workflow.

Configuration is loaded by consumers, not by T3 itself. Re-running setup updates
the same file; consumers see changes on their next invocation. Repository
instructions or installation can make the skill discoverable, but do not turn
the configuration into a persistent system rule.
