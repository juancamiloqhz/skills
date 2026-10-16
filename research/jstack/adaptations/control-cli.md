# Control CLI adaptation

Source: `cursor-team-kit/skills/control-cli/SKILL.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [jstack-control-cli](../../../skills/jstack/jstack-control-cli/SKILL.md). The complete source directory contains one file. Preserve its standalone boundary, section order, eight-step loop, tooling options, tmux examples, profiling recipes and guardrails. The package license is the pinned `cursor-team-kit/LICENSE`, copyright Cursor, rather than pstack's separate notice.

## Complete differences

| Location | Change | Concrete requirement and evidence |
| --- | --- | --- |
| Name | `jstack-control-cli`. | Approved portable identity policy. Description and heading remain upstream's. |
| Introduction | Bind execution to the authorized command/workspace/runtime; report missing tools and preserve installation/configuration authority. | Driving a terminal does not authorize installing tools or controlling unrelated processes. Direct use does not activate Juan-mode. |
| Loop steps 6 and 8 | Bound waits; mark timeout/early exit incomplete; stop only owned processes and reap them on every outcome. | The source requires deterministic waits and clean termination. Bounded PTY cases verify readiness, failure classification and cleanup. |
| Python example | Use a monotonic deadline, reject readiness timeout/EOF, retain captured output and close/reap in `finally`, with kill/wait after a failed graceful termination. | Executing the original against a stalled owned CLI returned normally without its expected prompt. The corrected example makes failure observable and releases owned resources on normal, timeout and early-exit paths. |
| Cleanup guardrail | Restrict removal to owned resources and retain requested evidence without retaining running processes. | Existing caller files and sessions are not disposable. The evaluation explicitly requests retained transcripts. |
| Juan-mode caller | Name the standalone CLI helper and leave Control UI external. | Catalog discovery must select the shipped prefixed package and keep unsupported UI capabilities explicit. |

The minimal examples remain probes, not a complete multi-action application test. The tmux example is unchanged. A full run still follows the eight-step loop, saves the required evidence and checks application-specific outputs. The PTY example controls its direct child; descendant process groups and richer terminal controls need the target's own lifecycle handling and verification.

## Maintenance and verification

The manifest adds one mapping, the exact Control CLI watch subtree and its package license, plus the mode's caller context. Existing mappings, pins, decisions and reviewed checkpoint remain unchanged. There are 42 mapped skills and still four implemented playbooks. No runtime resolver, model role or configuration migration is added.

[Full source and caller comparison, execution evidence and limits](../evaluations/control-cli/README.md) cover the complete new helper, its license and the mode entrypoint. Actual terminal driving does not establish CPU/heap profiling, rich TUI layout/resize behavior, browser control or cross-provider support. Those remain gates for the consuming playbooks. Installation remains manual.
