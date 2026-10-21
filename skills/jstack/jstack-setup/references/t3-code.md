# T3 Code integration

Use the actual callable tool schemas and injected T3 Code instructions as authority. Tool names may have a harness prefix such as `mcp__t3_code__`.

- `orchestrator_capabilities` discovers provider instances, model IDs, options and inheritance. It is the validation source, not a model list copied into this skill.
- `delegate_task` creates parent-owned work. Concrete seats become `target` with `providerInstanceId`, `model` and `options`. Inherited seats omit `target`. Retain returned task IDs; use fresh delegated tasks for new review rounds with consolidated briefs and distinct retry-stable request IDs. Prefer asynchronous completion delivery over polling.
- `t3_thread_launch` creates independent conversations only when requested. Its `modelSelection` differs from a delegation target. Bind writing threads to separate worktrees using the tool's workspace strategy, rather than asking an agent to change its binding with shell commands.
- `t3_thread_configure` changes a conversation's selection. Setup does not call it: storing routing preferences should not switch the user's current model.

Save the unwrapped capabilities payload through a file-writing tool or streamed standard input. Embedding a large catalog in a shell command, including a heredoc passed as command text, can exceed the operating system's argument limit. If the transport only supports command strings, write bounded chunks. Preserve the full payload and parse the saved JSON before validation; do not shorten the catalog to make it fit.

Verify complete parsed equality with the original response before accepting capture. Parsing, matching provider/model counts and successful preflight do not establish fidelity. Use a programmatic comparison against the complete source when available; if a lossless transfer cannot be verified, report capture incomplete.

When the current tool result or runtime supplies the full response as a file, parse that exact file and copy its complete unwrapped payload programmatically into the task-owned catalog. If it is already unwrapped, copy bytes and verify equality before validation. Keep the runtime-owned source intact. Use only the current response's supplied path; an unidentified or partial file leaves capture incomplete.

For inline-response recovery in T3, the supported `t3_thread_read` can provide a complete record of the same capability call. Verify the source thread/item, capability tool name and arguments, successful result, caller identity and absence of truncation. Extract its actual output programmatically without filtering, then compare the saved object with that source. Preserve the observation's identity and time; recovering an older call does not refresh the catalog for a new workflow. If the complete source is unavailable, leave recovery incomplete.

For ACP when MCP tools are absent and `T3_ACP_MCP_NODE` is present, the supported discovery transport is:

```sh
ELECTRON_RUN_AS_NODE=1 "$T3_ACP_MCP_NODE" \
  ${T3_ACP_MCP_ENTRYPOINT:+"$T3_ACP_MCP_ENTRYPOINT"} \
  acp-mcp-call orchestrator_capabilities '{}'
```

Use this only when the current runtime documents the fallback. Do not install providers or inspect authentication secrets to make catalog entries runnable. Catalog availability confirms exposed selections, not successful provider execution; setup must not describe it as a cross-provider runtime test.
