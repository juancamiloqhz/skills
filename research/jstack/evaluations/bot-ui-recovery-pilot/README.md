# Bot UI recovery pilot

Prepared 2026-10-19 after PR #112 merged. The user asked to merge and continue with live verification. This plan uses the [durable-result helper](../bot-ui-durable-results/README.md) and the corrected public relay receipts. It does not reuse or alter the retired pilot's journal. The [execution report](results.md) records the later bounded success and cleanup; this file preserves the setup plan.

## Fixed scope

- Read-only GitHub status of `juancamiloqhz/skills` PR #112 in conversation `5f7384b2-cbbe-431f-942d-929f327635a1`.
- One temporary webhook named `Jstack bot UI recovery pilot 20261019`, created disabled with request ID `jstack-bot-ui-recovery-pilot-20261019-r1`, structured `{"type":"webhook"}` and current-thread binding. Use the complete [receiver prompt](receiver-prompt.md).
- Private directory `/home/ubuntu/.cache/jstack/bot-ui-recovery-pilot-20261019`, mode 0700. Helpers are copied from merged commit `ce634053316b5c69ea7316026a65afa4693b61bf`. Keep the task ID, process/session ID, owned tabs and request IDs there; never store a consumed secret reference.
- One local server on `127.0.0.1:8879`, allowed origin `http://127.0.0.1:8879`, opened through T3's collaborative browser. No tailnet exposure or service installation.
- At most two check-pr requests, one signed ignored probe and one unsigned negative probe. No retries, polling, delegation or model changes. Only the coordinator's ordinary continuation turns manage setup, verification and cleanup; webhook turns have the receiver prompt's narrower authority.

## Setup

1. Check that the owned directory does not represent an active earlier run and the port is free. Never stop an unrelated listener. Record the new task ID and verify disabled state and exact conversation binding. Save and report only T3's returned HTTPS webhook URL; if absent, remove the owned disabled task and report the T3 Connect dependency.
2. The user privately chooses a fresh key and saves it through the hidden-input command below. Request the same value through the private secret card, using request ID `jstack-bot-ui-recovery-key-20261019-r1`. Consume its returned reference once in `update_scheduled_task`, retaining disabled state and setting HMAC-SHA256 header `x-jstack-signature`, hex encoding, prefix `sha256=`. Verify the task reports its signature set. A cancelled/timed-out card needs a new request ID; a lost update response requires inspecting the task before another save. Never enable an unsigned task.
3. Save the returned endpoint as `webhook-url` privately. Start the pinned helper with fixed journal, repository and PR, loopback bind and allowed origin, and the private endpoint/key files. Record the process identity before sending. The sender reads the key; the agent must not print or inspect it. Check the page's fixed scope.

User terminal command, on Orbit:

```sh
python3 /home/ubuntu/.cache/jstack/bot-ui-recovery-pilot-20261019/code/scripts/jstack/bot_ui_transport.py \
  init-secret /home/ubuntu/.cache/jstack/bot-ui-recovery-pilot-20261019/signing-key
```

The server command is the earlier [pilot setup](../bot-ui-live-pilot/README.md#setup-after-approval), with every private-directory reference changed to this pilot directory and `--pr 112`. Use only this pilot's returned endpoint and fresh key. Inspect recorded state before repeating setup.

## Evidence sequence

1. With the signed task still disabled, click once to create the failed request. Require HTTP 409/disabled and one unowned pending record. If anything differs, stop and reconcile instead of generating more requests.
2. Enable only this signed task. Send one signed ignored probe and one unsigned probe with the fixed PR/repository and action `probe`. The signed public relay may return `recorded`, which does not prove dispatch; expect the signed probe's receiving turn to end silently. Require HTTP 401 for the unsigned request and inspect the bounded receiving-run evidence for absence of unsigned dispatch. Stop on unexpected acceptance. Do not infer completion from HTTP 202.
3. In a separate browser profile, click once with a fresh request ID. The receiver claims this request, queries GitHub, saves the exact result, reads it back, publishes here, then acknowledges. Its single pending snapshot drains the earlier disabled request through the same sequence. End the initiating turn to let the queued webhook turns run. A missing or rolled-back receiving turn remains incomplete; do not manually substitute for its execution or add requests.
4. On an ordinary continuation, verify both request IDs have saved observations and acknowledgements, and retained conversation messages match them. Refresh each page and restart only the owned server against the same journal. Require completed status without another webhook send. Attempts to claim the completed IDs must return false.
5. Read one saved result with `result --request-id` and redisplay it here with its saved timestamp, explicitly as a historical observation. Do not query GitHub again. This proves later-turn redisplay from the journal; it does not simulate, cause or claim survival of an actual new T3 rollback. Keep that distinction in the result report.

If a claim has no result, preserve it for investigation. If a saved result has no acknowledgement, follow the original-owner rules in the [receiver recovery contract](../bot-ui-local/README.md#durable-recovery-contract). Never reset an owner or backfill an acknowledged record. Do not delete or roll back conversation turns for this test.

## Cleanup and report

On completion or abandonment, disable and delete only the recorded temporary task, verify its absence, stop only the owned process after checking identity, and verify the socket is gone. Close owned browser tabs and remove only their `jstack-check:juancamiloqhz/skills:112` storage entry. Preserve one concise report with request IDs, actual observations, failures and limits. Remove the temporary key, endpoint and code snapshot once no owned run needs them. Retain uncertain journals privately until reconciliation is complete; never commit them. The earlier pilot's retained evidence, weekly upstream schedule, saved model configuration and installations remain untouched.

The source comparison remains `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`, read in full for this preparation. The sequence preserves private server credentials, small authenticated payloads, a harmless probe, one attempt and routine-side failure draining. The saved result is the necessary T3 recovery adaptation from PR #112. Tailnet verification and the standalone skill remain pending.

Preparation checks: reviewed the prompt's validation, claim, query failure, save failure, lost response, publication, acknowledgement and bounded drain branches against the pinned helper. Documentation/link and diff checks apply to this plan; the merged helper's 26 tests remain fixture evidence, not evidence that this live pilot passed.
