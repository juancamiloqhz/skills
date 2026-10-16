# Runtime forensics evaluation

Runtime forensics is Juan-mode's fifth internal playbook. It captures a live signal, reduces the artifact, tests the mechanism and maps the diagnosis to source. Five procedures are available and 18 remain pending.

## Source and scope

[Complete comparison](source-comparison.json) covers the entire new procedure and Juan-mode entrypoint against `11713c683fe4add4fd403ea880580abbc9e0875f`, plus setup at its own pin. The [adaptation record](../../adaptations/runtime-forensics.md) accounts for each difference. The heading, five-step order, live evidence requirement, diagnosis-only reply and exact throughput checkpoint remain intact.

Changes resolve configured delegation, distinguish terminal control from profiler access, scope temporary runtime intervention and require restoration. Missing instrumentation or symbols remain explicit gaps. Bug fix and Perf issue are still unavailable. All 42 manifest mappings, watches, context paths, pins, decisions and reviewed checkpoint are unchanged. Existing playbooks and support scripts match the base commit recorded in the comparison.

## Live process exercise

A fresh evaluator reads the full parent mode and new playbook, then diagnoses an owned Node terminal application. The [fixture archive](inputs.json) retains the source, caller note, authorization and input hashes. The brief permits one bounded artifact reducer, temporary instrumentation, restoration and cleanup. It does not supply the cause or a diagnostic driver.

The evaluator builds a PTY owner and inspector client with installed Node v24.19.0 and Python standard-library tools. The inspector listens only on an ephemeral loopback port. Profiling uses `Profiler.enable`, `Profiler.start` and `Profiler.stop`; intervention uses `Runtime.evaluate`, as documented by [Node's inspector API](https://raw.githubusercontent.com/nodejs/node/v24.x/doc/api/inspector.md). The [live archive](live-evaluation.json) retains the actual driver, commands, protocol messages, raw profile, runtime observations, reducer output, report and cleanup evidence.

The baseline profile lasts 3,030,211 microseconds and contains 2,718 samples. `refreshPreview` accounts for 734 self samples, with `listOnTimeout` and `processTimers` as callers. The reducer sees only the artifact and proposes timer-driven work. It does not inspect fixture source or alter the process. Its configured `judgment and prose` selection inherits the executing Codex model; the archive retains preflight and terminal task evidence.

On the same PID, 529457, the evaluator temporarily changes `preview.enabled`, observes three approximately 1.5-second windows and restores the original property descriptor. No terminal input occurs in these windows.

| Window | Frames produced | Process CPU, user plus system |
| --- | ---: | ---: |
| Enabled | 73 | 441,650 microseconds |
| Disabled | 0 | 10,682 microseconds |
| Restored | 73 | 450,123 microseconds |

The live script maps `refreshPreview` to `preview.cjs:7`, a clock-polled arithmetic loop at lines 9–12, scheduled every 20 milliseconds at line 18. The intervention supports that mechanism in this fixture. Sample counts do not establish exact function CPU duration; process CPU includes inspector and other work. These numbers are not a production speedup claim.

The enabled descriptor is restored, no probe globals remain and frame production resumes. The owner terminates its Node child with SIGTERM and reaps it after about 74 seconds. This tests owned-process termination, not the application's interactive quit path.

## Independent evidence check

[Parent verification](parent-verification.json) reads the actual raw artifacts. It checks sample IDs and deltas, callback ancestry, the saved profile against the raw stop response, matching PIDs, live source against fixture bytes, the three counter windows and restored state. All 15 inspector requests have matching responses without protocol errors or evaluation exceptions. The Node and owner PIDs are absent afterward, and the inspector port refuses connections.

Fixture inputs, caller note and global model configuration match their original hashes. The verification script is retained in the live archive. This is an independent check of the captured run, not a second live execution.

## Workflow misses and limits

The evaluator did not open the host task list with verbatim playbook steps before execution. It records those steps retrospectively and marks the timing requirement failed. The general parent Architect trigger was also unexecuted because the bounded brief allowed only one artifact reducer. Neither omission is a passing full-mode evaluation. The runtime diagnostic steps have evidence, while these broader workflow gates remain unproven in this run.

Initial combined instruction reads truncated; targeted reads recovered the missing text. The archive preserves the evaluator's process record and corrections. No procedure change was made to conceal those misses. A future full-mode exercise should verify the plan before capture and allow the applicable design delegation.

The evaluator also assesses unavailable profiling, forbidden intervention, missing symbols and unrelated-process ownership. Those are instruction-only cases, not live failures. Heap leaks, browser traces, hot code replacement, source maps for transformed code, descendant cleanup, forced-kill escalation, failed restoration and other providers remain untested. This run uses an explicit authoring root, so it does not prove newly installed catalog discovery.

[Validation](validation.json) records four packaging tests, affected entrypoint validators, manifest validation, Markdown lint, relative links and whitespace checks. No shipped runtime script changes. Scratch evidence remains at `/tmp/jstack-runtime-forensics-20261016`; archived scripts retain their original absolute paths. The complete profile and protocol exchanges are retained. The large live capability catalog is represented by its hash and focused preflight result. No installation, model configuration or schedule changes.
