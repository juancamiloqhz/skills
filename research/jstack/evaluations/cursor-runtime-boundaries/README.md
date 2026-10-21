# Cursor read scope and explicit writing

Assessment on 2026-10-21 at jstack revision `73f83579e1d52f45a93efb08bf1af3d57e5834e9`, after PR #134. The question is whether supported runtime controls enforce the earlier task's read scope, and what the existing Unslop evidence permits us to claim. This review launches no agent and changes no permissions or configuration.

The exposed T3 dispatch controls do not provide a per-task path allowlist. Cursor documents broader workspace controls, but they do not separate older response files inside the same project's runtime folder. Explicit Unslop application has evidence; native slash invocation and reliable automatic use remain unverified. The prior incomplete workflow results stand.

## Installed T3 adapter

The user-service executable is `/home/ubuntu/.t3/runtime/versions/0.0.46-nightly.20261003.2610/t3`, with SHA-256 `0906bd3c2dbf5eeb8e832c0e5b996a4df5825a8c75ffe1ab4002d39f415f9c71`. Its embedded `src/orchestration-v2/Adapters/CursorAdapterV2.ts` supplies the primary implementation evidence:

- `cursorRuntimeAgentPolicy`, byte offset 160606766, maps runtime policy to `autoReview` and `sandboxEnabled`.
- `makeCursorAgentOptions`, byte offset 160608975, passes those values, the checkout, model and setting sources to the Cursor Agent SDK. It supplies no per-task read-path list. Setting sources include project, user, team, MDM and plugins.
- The current `delegate_task` schema exposes broad runtime/interaction modes and checkout isolation, with no advertised filesystem allowlist field. The live catalog identifies the Cursor driver and the caller's `full-access` mode. No undocumented argument was attempted.

Evaluating only the extracted pure policy function, with no approval or sandbox override fields, produced this mapping:

| Input runtime mode | `autoReview` | `sandboxEnabled` |
| --- | --- | --- |
| `approval-required` | true | true |
| `auto-accept-edits` | false | true |
| `auto` | false | true |
| `full-access` | false | false |

Explicit approval/sandbox policies can override those defaults. The catalog does not expose every effective override. This table verifies the adapter's pure mapping, not an operating-system sandbox or the complete policy of an earlier child. T3 uses the SDK here; CLI help is not proof of SDK behavior. Separately, `cursor-agent --version` returned `2026.10.01-e373342`, and its help advertises sandbox and broad review controls.

## Workspace controls do not isolate one run

[Cursor's read-access documentation](https://cursor.com/docs/agent/security/run-modes#read-access) describes a workspace boundary covering file tools and sandboxed commands. It includes the project's `~/.cursor/projects` folder and does not apply in Run Everything mode. Therefore, enabling it alone would not distinguish this run's response file from older files in that folder. This is an inference from the documented scope, not a newly executed denial test.

The [sandbox reference](https://cursor.com/docs/reference/sandbox) defines `readBoundary` and extra readable paths. The [CLI permissions reference](https://cursor.com/docs/cli/reference/permissions) describes file and shell rules. Neither document proves a task-specific boundary in the installed T3 SDK integration. No live rule or mode was changed, and no shell-bypass or denied-file test ran. An isolated checkout is also not proof of filesystem isolation.

The earlier task's narrower source restriction remains an authorization rule the agent violated. Broader runtime access does not authorize broader task work. Stronger enforcement would need a separately assessed runtime integration, including its own response storage, required installed skills/configuration and helper access. Do not treat a longer prompt, automatic review, a worktree or a passed model preflight as that enforcement.

## Explicit Unslop evidence

[Cursor's skills reference](https://cursor.com/docs/skills#disabling-automatic-invocation) defines `disable-model-invocation: true` as disabling automatic context selection while retaining explicit invocation. The flag alone is not a recorded host rejection.

The parent reread the [existing explicit-use trial](t3-thread://v1/thread:delegated-task:command%3Amcp%3A43e44741-8770-4b39-baaa-3c5c3e38701e%3Adelegate-task%3Ajstack-cursor-unslop-invocation-20261020-r1). Its complete installed-body read at position 7 matches the current Unslop body, and the rewrite at 9 applies rules 7, 9, 23 and 31. The flag remains true. No native invocation call or rejection appears. This establishes explicit filesystem loading/application only, not slash expansion, automatic dependency invocation or a complete Investigation. See the [version-specific dependency assessment](../../adaptations/technical-writing.md#unslop-dependency-assessment).

Usage example for that bounded route: "Explicitly apply the installed Unslop skill to your final reply." The agent must discover the intended dependency and follow the host's supported explicit-loading mechanism. An actual rejection remains incomplete; explicit loading is not permission to bypass one. The [guided Investigation's](../provider-discovery/README.md#guided-presentation-follow-up) skipped writing phase remains incomplete, rather than becoming a host-incompatibility finding or a pass.

## Reproduce the adapter mapping

This reads the pinned installed executable and evaluates only its verified policy function. It does not start T3, create a Cursor agent, read credentials or change settings. The hash assertion deliberately stops on another build.

```sh
python3 -B - /home/ubuntu/.t3/runtime/versions/0.0.46-nightly.20261003.2610/t3 <<'PY'
import hashlib, json, subprocess, sys
from pathlib import Path
data = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(data).hexdigest() == '0906bd3c2dbf5eeb8e832c0e5b996a4df5825a8c75ffe1ab4002d39f415f9c71'
start = data.index(b'function cursorRuntimeAgentPolicy(')
end = data.index(b'\n}', start) + 2
function = data[start:end].decode()
modes = ['approval-required', 'auto-accept-edits', 'auto', 'full-access']
script = function + '\nconsole.log(JSON.stringify(' + json.dumps(modes)
script += '.map(runtimeMode => ({runtimeMode, ...cursorRuntimeAgentPolicy({runtimeMode})}))));'
subprocess.run(['node', '--input-type=module', '-e', script], check=True)
PY
```

## Fidelity and disposition

This is a completed bounded integration assessment, not provider certification. Preserve the existing skill procedures and Unslop flag. No further provider run, settings change or repeated full Investigation is needed to restate the existing evidence. Current read-scope compliance and reliable writing invocation remain open.

All operational files and the manifest are unchanged. Comparison with How, mode and Unslop at `11713c683fe4add4fd403ea880580abbc9e0875f` preserves the light-edit rule, verbatim task requirement and explicit-only flag. The installed adapter review introduces no pstack deviation or checkpoint advance. Only this concise report, its reproduction command and status links are retained; no executable, SDK code copy, catalog, transcript or host configuration is committed.
