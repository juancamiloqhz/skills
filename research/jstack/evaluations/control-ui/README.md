# Control UI evaluation

The [helper](../../../../skills/jstack/jstack-control-ui/SKILL.md) preserves the pinned Control UI procedure and both JavaScript examples. The [adaptation record](../../adaptations/control-ui.md) accounts for T3 browser selection, ownership and missing-capability reporting. Visual parity remains unimplemented; screenshots are not pixel-diff proof.

## Executed behavior

On 2026-10-17, the coordinator and two fresh T3-owned Codex `gpt-6.1-sol` high-effort children drove the local [fixture](fixture.py) through native preview. The children used the resolved `feature, refactoring` role from the selected global configuration. One read the authoring draft; the baseline did not. Both received the same task to enter Ada, add two parcels, save screenshots, assess profiling capability and close owned tabs. No model or configuration change occurred.

| Check | With draft | Baseline |
| --- | --- | --- |
| Select Parcel desk and observe both increments | `0 parcels`, `1 parcels for Ada`, `2 parcels for Ada` | Same |
| Refresh selectors after the button is replaced | Two current accessibility references, with intervening snapshots | Same |
| Retain real before/after screenshots | Two 1280×800 PNGs; parent inspected final image | Same |
| Close only the returned owned tab | Closed its own tab | Closed its own tab |
| Classify unavailable CPU capture | Incomplete; no exposed native raw-CDP/profiler API | Incomplete; page Profiler API also rejected capture |

The baseline's actual API error was `NotAllowedError: Failed to construct 'Profiler': JS profiling is disabled by Document Policy.` Neither run installed tools, guessed a debug port or substituted a screenshot for a CPU profile. The parent verified tool/read events and saved artifacts rather than accepting only terminal reports. Both original tasks completed with no pending descendants. Each child began with no tab in its own thread; the parent's pre-existing tab remained available and unchanged by them.

The coordinator independently drove the same sequence for Lin and inspected the final screenshot. It then requested nonexistent text through `preview_wait_for` with a 500 ms timeout. The tool returned `Preview automation waitFor timed out after 500ms.` This was an incomplete condition, not a passing readiness check. Navigating the owned tab to `/archive` exposed a distinct title, heading and Export button, confirming that the intended page can be distinguished by content. The coordinator closed its tab and stopped the owned fixture server after both readers finished.

The five checks passed in both arms. This is a small behavioral smoke test, not evidence that the draft improves performance over host instructions. The task itself states several boundaries, so it does not isolate every skill rule's effect. CPU capture remains incomplete. Human takeover, a user-controlled tab, fallback-browser execution, Electron attachment, real CDP profiling, pixel comparisons, installed catalog discovery and other providers were not exercised. The unchanged Playwright snippets were source-compared but not executed in this run.

Task IDs share prefix `node:delegated-task:command%3Amcp%3A1306b48b-98ae-44eb-8d85-8c0e6f409fb9%3Adelegate-task%3A`, with suffixes `control-ui-with-skill-20261017-r1` and `control-ui-baseline-20261017-r1`; both original runs have ordinal 1. Scoped activity pagination ended; truncated tool items were recovered. This does not establish access to full private provider transcripts. Token counts were not supplied by completion notifications; no cost or speed claim is made.

## Reproduce

From the repository root, run the fixture in a terminal you own:

```sh
python3 research/jstack/evaluations/control-ui/fixture.py
```

It binds a free loopback port and prints its number. Keep it running for the browser exercise. In T3 Code, call `preview_status`, then `preview_open` if needed. Open a dedicated tab and navigate with `target: {kind: "environment-port", port: PORT}`. Verify the Parcel desk heading, Recipient textbox and Add parcel button. Take a fresh snapshot, enter Ada, refresh, click once, refresh, click again and refresh. The expected states are the three listed above; the app rebuilds the button after each click. Save screenshots with the tool's supported capture mechanism when evidence is requested.

For the timeout case, wait for `Shipment complete` with `timeoutMs: 500`; the fixture never produces it. Inspect `/archive` separately, without treating its Export button as the target control. Discover current capture capabilities; do not assume the profiling limitation will hold on another host. Close only the owned tab and stop the owned server. This fixture needs only Python's standard library, no installation or project dependency.

For the independent-reader comparison, use two fresh contexts with the same request and separate tabs/output directories. Give only the with-skill arm the explicit authoring path. Validate the current selected role against fresh capabilities before dispatch. Inspect actual actions, snapshots, image files and terminal task state; preserve errors and missing capabilities. A larger provider matrix requires separate execution evidence.

## Source and package validation

The complete helper and Juan-mode caller were compared with their exact pinned sources. All helper headings, the original numbered sequences, source description, both JavaScript examples and license match apart from the recorded adaptations. The manifest adds the 45th mapping; previous mappings, context/watch paths, pins and reviewed checkpoint are unchanged. The caller changes only its UI helper identity and dependency availability. Eleven playbooks remain available and twelve pending.

The package tests passed 4/4 and upstream-checker tests passed 11/11; both affected packages passed frontmatter validation. Markdown, relative links and whitespace checks passed. Retain this report, the 47-line fixture and the [source comparison](source-comparison.json). Routine tool activity, full agent reports, screenshots, catalogs, grading files and the generated review viewer stay in task-owned scratch while review is active. They are not shipped evidence dependencies.
