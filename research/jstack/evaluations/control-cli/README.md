# Control CLI evaluation

Standalone `jstack-control-cli` supplies the terminal-control dependency for future engineering playbooks. Juan-mode discovers it for CLI/TUI work while Control UI remains external. This adds one helper, not another playbook. Four procedures are available and 19 remain pending.

## Source and scope

[Complete comparison](source-comparison.json) covers the entire new helper and Juan-mode entrypoint against `11713c683fe4add4fd403ea880580abbc9e0875f`. The source helper has one file under `cursor-team-kit/skills/control-cli`. Its package retains the exact Cursor team-kit MIT notice. The [adaptation record](../../adaptations/control-cli.md) accounts for all differences.

The source's section order, eight steps, tool choices, tmux examples and profiling recipes remain intact. Required changes name the jstack package, preserve task/ownership boundaries and correct the Python example's timeout and cleanup behavior. The two mode edits select the new helper and distinguish it from external Control UI. Existing mode support files and all four playbooks match the base commit recorded in the comparison.

There are 42 mappings. New watches cover the exact helper subtree and its upstream license, with the helper source also recorded as mode context. Existing mappings, source pins, decisions and reviewed checkpoint remain unchanged.

## Live terminal exercise

The [fixture](inputs.json) is a real Python process that requires PTY stdin/stdout. It asks for a name, handles help/status/quit and provides two startup-failure modes. Its source and caller-owned note remain fixed. No application harness is supplied.

A fresh agent reads the standalone helper and exercises the actual process. [Live evidence](live-evaluation.json) retains the discovered files, temporary harness, exact commands/environment, initial terminal screens, byte transcripts, prompt matches, actions, exit statuses, owned PIDs and reaping checks. It uses standard-library PTY tools without installation. Direct helper invocation does not activate Juan-mode.

| Case | Result | Interaction status |
| --- | --- | --- |
| Normal | Ada receives the greeting; help and status match; quit prints BYE; exit 0. | Complete |
| Stall | STARTING appears; the Name prompt misses its deadline; owned process terminated and reaped. | Incomplete |
| Early exit | BOOT FAILED appears; process exits 7 before the Name prompt; reaped. | Incomplete |

The agent reports verified failure handling separately from successful application interaction. No input is sent into either failed startup. The fixture launches no descendants. All owned direct children return from `wait`; subsequent `waitpid` reports ECHILD and their `/proc` paths are absent. PTY descriptors are closed.

[Parent replay](parent-replay.json) executes the retained harness in a fresh owned output directory. All three raw transcripts match the original byte for byte. [Parent verification](parent-verification.json) reconstructs each transcript from read events, checks the four input actions and confirms original inputs and the global model file are unchanged. The replay preserves the first run rather than overwriting its evidence.

## Python example correction

[Example evidence](example-evaluation.json) executes the pinned source snippet with only its command/prompt placeholders substituted and its deadline shortened. A stalled CLI never prints the requested prompt, but the original snippet returns normally. This is a reproduced false-success path.

The final example uses a monotonic deadline and raises on timeout or EOF. Cleanup closes descriptors, terminates a still-running direct child, waits for it and escalates to kill/wait if needed. Captured output is printed after cleanup so error evidence remains visible. A first correction omitted captured output on failures; the final check includes it.

The parent executes the exact final template against normal, stalled and early-exit inputs. The normal readiness probe returns normally. Stall raises `TimeoutError`. Early exit raises Linux PTY `EIO`, with BOOT FAILED retained and child exit 7. All three children are reaped and master descriptors are closed. This minimal example proves a readiness/send operation, not a complete command flow; the separate live harness supplies that evidence.

The independent agent run preceded the example correction. Its retained skill snapshot differs from the final skill only in that Python block. The parent separately tests the exact final block and replays the full interaction harness. This is not a claim that a fresh agent reran every final instruction.

## Checks and limits

[Validation](validation.json) records four packaging tests, both affected skill validators, actual manifest validation, Markdown lint, relative links and whitespace checks. No runtime resolver or shipped script changed. The embedded Python example has direct execution evidence.

No existing-repository harness, tmux session, arrow/Escape/Ctrl-C flow, resize/layout behavior, CPU profile, heap snapshot, process descendant cleanup, force-kill escalation, browser or other provider is exercised. Missing-tool recovery and installed catalog discovery remain untested. These limits stay with the relevant consuming playbooks; terminal output alone does not establish profiling capability.

Raw files are archived in JSON without rewriting responses or terminal bytes. Scratch paths remain `/tmp/jstack-control-cli-20261016`, `/tmp/jstack-control-cli-example-20261016` and `/tmp/jstack-control-cli-parent-replay-20261016`. Scripts retain their original absolute paths; replay elsewhere requires rebinding owned paths. No installed skills, model configuration or schedules changed.
