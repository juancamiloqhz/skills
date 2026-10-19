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

1. The current receipt classifier returned unknown for both live HTTP-202 deliveries, although T3 queued them. It was tested against the installed direct-server response contract. The successful public-relay response headers/body were not retained, so the exact field mismatch is not established. Do not fix this by treating every HTTP 202 as successful. A follow-up should inspect the public contract or collect only the relevant response metadata in a separately bounded test, then add a meaningful fixture before changing classification.
2. External journal acknowledgements survived a T3 turn rollback. Their evidence fields reference that conversation and request ID, but the corresponding recovery report is no longer visible. Keep those IDs acknowledged and reconcile the evidence; resetting them could repeat work. A later live test must establish receiving completion and its durable evidence together. The successful first request remains independently supported by its retained transcript.

The planned browser restart check and post-recovery duplicate-claim check were not completed. Local fixture tests cover those behaviors, but they do not replace this missing live evidence. Tailnet access was outside this pilot. No extra webhook requests were sent to compensate for missing evidence.

## Cleanup and retained evidence

Disabled the exact pilot task, confirmed the disabled state, deleted it by its recorded ID and confirmed its absence from the project task list. Its ID was `scheduled-task:command:mcp:9abbe32a-8109-479b-88fb-ea560c655c3f:schedule-task:jstack-bot-ui-live-pilot-20261019-r1`. The server had already stopped. Closed both owned tabs and removed only their pilot local-storage key. Deleted the local signing key, endpoint file and duplicate helper snapshot. The weekly schedule, saved model configuration, skills installation and tailnet settings were unchanged.

Retained only `requests.sqlite` and a sanitized `pilot-state.json` in `/home/ubuntu/.cache/jstack/bot-ui-pilot-20261019`. They preserve the external acknowledgements and cleanup ownership while the rollback finding is reviewed. Neither is committed. They can be removed after that review is accepted and no recovery investigation needs them. The deleted webhook and key are not available for another run; a future pilot must use a fresh creation request ID and private provisioning.

No executable code changed in this report. Documentation/link and diff checks passed; the earlier 22-test result remains historical fixture evidence. The source comparison remains `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`: server-only credentials, authenticated small JSON, one attempt, harmless probe and routine-side failure recovery were the relevant requirements. Receipt fidelity and recovery evidence remain open, so no standalone skill or completed upstream-coverage claim was added.
