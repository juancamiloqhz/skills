# Configuration and worker lifecycle

Discover setup-jstack through the current skill catalog or an explicit authoring path. Read its `references/configuration.md` and `references/t3-code.md`. A missing dependency stops incomplete with manual installation guidance: `npx skills add juancamiloqhz/skills --skill setup-jstack`. Swarm does not depend on Arena or juan-mode.

Capture a fresh unwrapped capability catalog using setup's file/streaming guidance. Resolve the scalar worker role:

```sh
python3 /discovered/setup-jstack/scripts/models.py resolve \
  --project-root /target/project --catalog /owned/catalog.json \
  --role 'swarm workers' --with-source
```

Pass a caller-selected config positionally after `resolve`; otherwise use canonical lookup. Retain the returned absolute config and pass it explicitly across workers and worktrees. Whole-map validation errors stop execution. Keep settings unchanged. A null target means omit the target to inherit provider, model and effort; concrete targets pass through unchanged, including options.

For an arm whose model was explicitly selected by the user or authorized caller, write that single seat to a task-owned JSON file. It uses setup's exact seat schema: `{"alias":"inherit-parent"}` or `{"providerInstanceId":"...","model":"...","options":{...}}`. Do not convert a request for unspecified diversity into guessed targets. Resolve the original selected configuration with the override:

```sh
python3 /discovered/setup-jstack/scripts/models.py resolve /selected/models.json \
  --catalog /owned/catalog.json --role 'swarm workers' \
  --worker-override /owned/arm-seat.json --with-source
```

This validates the complete saved map first, then the override, and returns that arm's target without editing either file. `config` and `configSource` still identify the original saved defaults; the brief and task record identify the override separately. Validate every declared arm before starting the race. Invalid overrides stop incomplete; they never fall back to the default. Workers without an explicit arm selection keep the saved scalar default. Pass the original absolute config and effective arm selection to the worker, so re-reading defaults does not erase its task-local assignment. Revalidate against a fresh catalog for new attempts. If the installed helper lacks `--worker-override`, report the missing capability and manual update prerequisite rather than copying its validator or rewriting settings.

Check the effective provider's `canRunChildTask`, selected model availability and, when different from the parent's provider, `canRunCrossProviderChildTask` against the same catalog. Use inherited identity for checks without materializing a target. Capability failure or rejection does not authorize fallback models. Refresh discovery when rejection suggests drift and report the unmet condition.

For a separate checkout, use T3 `delegate_task` with `isolation: "worktree"`, based on the parent local commit without uncommitted edits. Otherwise prefer native same-provider workers when they support the selected model/options, required context and lifecycle. Otherwise use T3 `delegate_task`, with complete briefs because T3 children do not inherit conversation history. Use retry-stable request IDs and retain returned task IDs. New attempts or review rounds use fresh tasks, never a child backing thread. Use async completion notifications where available; inspect actual terminal state, not scheduler dispatch or a finished turn with pending work.

Prepare source workspaces before writing tasks. Read/write scope in a prompt does not change app binding or enforce a sandbox. Use absolute paths and explicit command working directories, then inspect original and assigned paths. Run artifact writers serially until assigned-path handling has been demonstrated for the provider/tools. Keep shared plans, integration and final delivery coordinator-owned. A rejected dispatch, cancellation or timeout must be reconciled before retrying so two writers cannot own the same output.

Remove owned temporary catalogs and override drafts after recording effective selections and checks. Retain reports, exact briefs, task IDs and useful artifacts needed to audit gaps and selection. Do not install tools, change models, push or merge to repair an execution prerequisite.
