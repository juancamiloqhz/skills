# Live recovery results

Date: 2026-10-19. The bounded loopback pilot passed browser-triggered delivery, failed-request draining, saved-result redisplay and local-server restart checks. It did not cause or test a new T3 rollback. Tailnet access and the standalone Make bot UI skill remain pending.

Used the [fixed plan](README.md), helper commit `ce634053316b5c69ea7316026a65afa4693b61bf`, and conversation `5f7384b2-cbbe-431f-942d-929f327635a1`. PR #112 was the fixed read-only target. The private card's first attempt expired before provisioning; the second consumed a fresh reference while the task was disabled. The agent inspected key-file metadata only. No key value was read or printed.

| Request | Observed result |
| --- | --- |
| `recovery-probe-20261019` | Signed POST returned 202/recorded with a relay delivery ID. Receiving turn 244 completed silently. |
| `recovery-unsigned-probe-20261019` | Returned 401/invalid_signature. Only the signed probe was queued before the check request. This is a bounded absence-of-dispatch observation, not a complete server audit log. |
| `c56c52dd1e75e583e71485993ed9b458` | First browser click returned 409/disabled and remained unowned. The subsequent receiver drained it, saved the result at `2026-10-19T22:30:19.075Z`, published it, then acknowledged. |
| `4e91759db94b5781343fe08a684db908` | Second browser profile returned 202/recorded, queued turn 245, and saved the result at `2026-10-19T22:29:56.160Z` before publication and acknowledgement. |

Both observations returned MERGED, merge time `2026-10-19T22:20:40Z`, merge commit `ce634053316b5c69ea7316026a65afa4693b61bf`, and PR head `1b2c80624c9ee39d4b5acba7d10fb397b304033c`. Turn 245 completed. The later coordinator turn 246 read both journal results and confirmed their matching messages remained in T3's timeline at positions 10647 and 10651. It redisplayed the second request's saved observation and timestamp without querying GitHub again.

Stopped the recorded local server and restarted the same pinned helper against the same journal. The default browser profile retained the second request ID and displayed completed after reload. The original preview tabs were no longer attached to the later turn. A new incognito tab had lost the first request's local storage; restoring its known ID displayed that journal record as completed too. This verifies journal recovery, not incognito storage persistence. No further Check PR click or webhook send occurred. Both repeat claim attempts returned `granted:false`; pending was empty.

## Cleanup and limits

Disabled the exact temporary task, verified its state, deleted it and confirmed its absence. Stopped the restarted owned server, closed the owned preview tabs, removed only their pilot storage key, and confirmed loopback port 8879 was no longer listening. The task ID was `scheduled-task:command:mcp:c6c70834-a476-41e7-a9ef-0cbd5867d02c:schedule-task:jstack-bot-ui-recovery-pilot-20261019-r1`.

After preserving this report, removed the successful pilot's private directory, including its key, endpoint, journal and duplicate helper snapshot. No raw logs or database are committed. The previous incomplete pilot's retained evidence was not modified. Weekly scheduling, installed skills, saved models and tailnet settings were unchanged.

Compared the result with `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. The page, server-side credentials, small authenticated request, harmless probe, single send and routine-side failed-request drain worked in this T3 pilot. T3-specific receipt handling and saved-result recovery preserve those requirements. No executable change was needed; documentation/link and diff checks passed. The prior 26-test result remains fixture evidence. Full tailnet access, actual rollback recovery and a packaged standalone skill are not claimed.
