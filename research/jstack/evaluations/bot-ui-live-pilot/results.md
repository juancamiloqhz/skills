# Bot UI live pilot results

Date: 2026-10-19. Outcome: incomplete. The [approved pilot](README.md) established a real signed browser-to-conversation request and acknowledgement. The recovery journal contains acknowledgements, but T3 marks the recovery turn rolled back and its result is absent from the visible timeline. The temporary service has been removed. This is not release evidence for the full Make bot UI skill.

## Observed results

| Check | Evidence and limit |
| --- | --- |
| Disabled creation and binding | Created one disabled webhook bound to conversation `5f7384b2-cbbe-431f-942d-929f327635a1`. T3 returned a Connect URL. |
| Private provisioning | The user saved a mode-0600 key through the hidden-input CLI and supplied the same value through T3's private card. Its reference was consumed once while the task stayed disabled; signature configuration was verified before enabling. No key value was read or printed by the agent. |
| Signed probe | One `probe` request returned HTTP 202 and queued receiving turn 234. That turn ended silently as required. The sender classified the response as unknown. |
| Unsigned probe | One request returned HTTP 401, body error `invalid_signature`. Before the next signed click, the thread still showed only the signed probe as a new queued run. This combines HTTP rejection with a bounded thread observation, not a complete server audit log. |
| Real browser click | Request `18473cae97ddd3a4bb5c9a05da51ecc2` queued turn 235. The receiver claimed it, queried GitHub, reported PR #109 merged at `2026-10-19T21:03:41Z`, commit `e4e9316ae2875e3ee16a1b06082ed83a5805bea9`, then acknowledged. The next ordinary turn refreshed the page and saw completed. |
| Failed delivery | With only the pilot task disabled, request `19a46146c54c26a1fa0c6ffacdb458e2` returned HTTP 409/disabled and remained unowned in the journal. |
| Recovery wake | After re-enabling the signed task, a separate browser profile sent `eb52fd2141f1d9429ab4c31b1c19d6a8`. It queued turn 238. Before that turn, the journal showed both recovery records unowned. Later, both had distinct owners and acknowledgement references, with no pending entries. However, turn 238 is now `rolled_back`; the visible timeline contains no retained result from it. Those journal changes alone do not prove the required visible report-before-ack sequence. |
| Server exit | The background command reported exit `-1`. The recorded PID no longer existed and loopback port 8879 had no listener. The cause of exit was not established. No automatic restart or resend was attempted. |

The first page used the incognito profile. The recovery wake used a separate default-profile tab with a new request ID, since reusing the first profile preserves its unresolved request. Both were owned test tabs; only their exact pilot storage key was removed during cleanup. This differs from the plan's wording “fresh incognito profile” without changing the request count or scope.

## Findings

1. The pilot receipt classifier returned unknown for both live HTTP-202 deliveries, although T3 queued them. It was tested against the installed direct-server response contract. The successful public-relay response headers/body were not retained, so the exact field mismatch is not established. Do not fix this by treating every HTTP 202 as successful. The source-backed correction below addresses the known contract mismatch without inferring dispatch from HTTP 202.
2. External journal acknowledgements survived a T3 turn rollback. Their evidence fields reference that conversation and request ID, but the corresponding recovery report is no longer visible. Keep those IDs acknowledged and reconcile the evidence; resetting them could repeat work. A later live test must establish receiving completion and its durable evidence together. The successful first request remains independently supported by its retained transcript.

The planned browser restart check and post-recovery duplicate-claim check were not completed. Local fixture tests cover those behaviors, but they do not replace this missing live evidence. Tailnet access was outside this pilot. No extra webhook requests were sent to compensate for missing evidence.

## Cleanup and retained evidence

Disabled the exact pilot task, confirmed the disabled state, deleted it by its recorded ID and confirmed its absence from the project task list. Its ID was `scheduled-task:command:mcp:9abbe32a-8109-479b-88fb-ea560c655c3f:schedule-task:jstack-bot-ui-live-pilot-20261019-r1`. The server had already stopped. Closed both owned tabs and removed only their pilot local-storage key. Deleted the local signing key, endpoint file and duplicate helper snapshot. The weekly schedule, saved model configuration, skills installation and tailnet settings were unchanged.

Retained only `requests.sqlite` and a sanitized `pilot-state.json` in `/home/ubuntu/.cache/jstack/bot-ui-pilot-20261019`. They preserve the external acknowledgements and cleanup ownership while the rollback finding is reviewed. Neither is committed. They can be removed after that review is accepted and no recovery investigation needs them. The deleted webhook and key are not available for another run; a future pilot must use a fresh creation request ID and private provisioning.

The original report changed no executable code. The follow-up below changes receipt classification and page wording only. The source comparison remains `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`: server-only credentials, authenticated small JSON, one attempt, harmless probe and routine-side failure recovery were the relevant requirements. Live verification of the corrected receipt and recovery evidence remain open, so no standalone skill or completed upstream-coverage claim was added.


## Public relay receipt correction

Inspected T3 source at `54983e3f458871dffe755ea908ffe0d60cea101b` after the pilot. [HookForwarder.ts](https://github.com/pingdotgg/t3code/blob/54983e3f458871dffe755ea908ffe0d60cea101b/infra/relay/src/hooks/HookForwarder.ts) forwards the environment's status and body but omits `x-t3-hook-outcome` from its response headers. When offline holding is enabled, it instead returns HTTP 202 with exactly `{"queued":true}`. [webhookRoute.ts](https://github.com/pingdotgg/t3code/blob/54983e3f458871dffe755ea908ffe0d60cea101b/apps/server/src/scheduledTasks/webhookRoute.ts) and [ScheduledTaskService.ts](https://github.com/pingdotgg/t3code/blob/54983e3f458871dffe755ea908ffe0d60cea101b/apps/server/src/scheduledTasks/ScheduledTaskService.ts) show that accepted, duplicate and prompt-too-long outcomes all return 202 with a delivery ID. Therefore a public receipt cannot distinguish dispatch acceptance from prompt rejection. This explains a concrete incompatibility with our direct-route fixture; the pilot's missing raw response still prevents proving its exact bytes or deployed relay revision.

The sender now retains a valid delivery ID without that header as `recorded`, and recognizes the exact offline-hold body as `queued`. Neither counts as accepted or completed, and both retain the CLI's nonzero exit status. The page explains the uncertainty and prevents resending. Explicit direct-route outcomes keep their existing behavior; malformed, contradictory and unrecognized responses remain unknown. There is no journal migration or reclassification of historical receipts.

Reproduce with `python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'`. Add `JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3` to include the pinned signature verifier. The browser fixture accepts `--receipt recorded` or `--receipt queued` to reproduce each new message without a real endpoint or signing key. This preserves pstack's one attempt, server-only credentials and routine-side recovery; only the T3 response interpretation changes. Full recovery and tailnet evidence remain pending.

Validation: all 23 Python tests passed with the installed-verifier probe enabled; documentation checks and JavaScript syntax checks passed. Collaborative-browser fixtures displayed both new states, kept submission disabled, and sent one POST per click. Refreshing the recorded request sent no additional POST. No live webhook was created or called for this correction.
