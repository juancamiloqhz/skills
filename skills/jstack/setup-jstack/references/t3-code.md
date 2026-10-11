# T3 Code integration

Use the actual callable tool schemas and injected T3 Code instructions as authority. Tool names may have a harness prefix such as `mcp__t3_code__`.

- `orchestrator_capabilities` discovers provider instances, model IDs, options and inheritance. It is the validation source, not a model list copied into this skill.
- `delegate_task` creates parent-owned work. Concrete seats become `target` with `providerInstanceId`, `model` and `options`. Inherited seats omit `target`. Retain returned task IDs; use fresh delegated tasks for new review rounds with consolidated briefs and distinct retry-stable request IDs. Prefer asynchronous completion delivery over polling.
- `t3_thread_launch` creates independent conversations only when requested. Its `modelSelection` differs from a delegation target. Bind writing threads to separate worktrees using the tool's workspace strategy, rather than asking an agent to change its binding with shell commands.
- `t3_thread_configure` changes a conversation's selection. Setup does not call it: storing routing preferences should not switch the user's current model.

For ACP when MCP tools are absent and `T3_ACP_MCP_NODE` is present, the supported discovery transport is:

```sh
ELECTRON_RUN_AS_NODE=1 "$T3_ACP_MCP_NODE" \
  ${T3_ACP_MCP_ENTRYPOINT:+"$T3_ACP_MCP_ENTRYPOINT"} \
  acp-mcp-call orchestrator_capabilities '{}'
```

Use this only when the current runtime documents the fallback. Do not install providers or inspect authentication secrets to make catalog entries runnable. Catalog availability confirms exposed selections, not successful provider execution; setup must not describe it as a cross-provider runtime test.
