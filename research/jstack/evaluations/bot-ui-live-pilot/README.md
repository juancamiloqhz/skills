# Bot UI live pilot preparation

Prepared 2026-10-19 after PR #109 merged and approved with PR #110. The [execution results](results.md) record the later incomplete pilot and completed service cleanup. The procedure below is the reviewed plan, not a claim that every check passed. The sender, page and local recovery tests are recorded in the [transport](../bot-ui-transport/README.md) and [local UI](../bot-ui-local/README.md) reports.

The test will answer one question: can a browser click reach this T3 conversation, produce a read-only PR status result and acknowledge the same saved request? The page runs on Orbit at `http://127.0.0.1:8879`. It is opened through T3's collaborative browser, not exposed to the tailnet. A later peer-access test is still required before the full skill ships.

## Fixed scope

| Item | Value |
| --- | --- |
| GitHub action | Read the status of `juancamiloqhz/skills` PR #109, which is already merged. No PR writes. |
| Receiving conversation | `5f7384b2-cbbe-431f-942d-929f327635a1`, this jstack conversation. |
| Task title | `Jstack bot UI live pilot 20261019` |
| Task creation request ID | `jstack-bot-ui-live-pilot-20261019-r1`, reused if the create response is lost. |
| Trigger | Structured `{"type":"webhook"}`, `enabled:false`, `bindToCurrentThread:true`. No timer. |
| Prompt | Complete contents of [receiver-prompt.md](receiver-prompt.md), supplied literally as the tool's prompt string. |
| Signing | `x-jstack-signature`, HMAC-SHA256, hex, prefix `sha256=`; user-provided secret through the private card. |
| Private directory | `/home/ubuntu/.cache/jstack/bot-ui-pilot-20261019`, mode 0700. |
| Server | One foreground process, bind `127.0.0.1`, port `8879`, only origin `http://127.0.0.1:8879`. No service installation. |
| Helper code | `code/` inside that directory, copied from merged commit `e4e9316ae2875e3ee16a1b06082ed83a5805bea9`. |
| Cleanup | Disable and delete only the recorded pilot task, stop only the recorded pilot server, then remove its private files after preserving the concise result. |

The private directory holds `signing-key`, `webhook-url`, `requests.sqlite` and the pilot's task/process identifiers. No file contains an application secret reference after consumption. The approved setup must record the returned task ID and verify the returned bound conversation before continuing. The receiver uses fixed paths and scope; request data never chooses them.

## Setup after approval

1. Confirm the code snapshot and available loopback port again. If the private directory contains an existing task or pending journal, reconcile that pilot rather than creating another. An occupied port is a dependency, not permission to stop another service. Keep the weekly upstream schedule untouched.
2. Call `schedule_task` with the fixed creation request ID, title, full receiver prompt, structured webhook trigger, disabled state and current-thread binding. Record the returned task ID. Read the returned state: it must be disabled and bound to the fixed conversation. Report the returned `webhookUrl`. If absent, delete this owned disabled task and stop with “T3 Connect remote access is required.” Do not derive a URL or enable another tunnel.
3. The user privately provisions one signing key in their own Orbit terminal with the command below. Then call `request_secret` with clientRequestId `jstack-bot-ui-pilot-key-20261019-r1`, asking for the same value in the private card. The agent never sees the value. Do not read/print the key or request it in chat. If the card times out or is cancelled, leave the task disabled; a subsequent card uses a new request ID. An opaque reference is not a local key.
4. Consume the returned `secretRef` once through `update_scheduled_task`, keeping `enabled:false` and setting schedule to a structured webhook with signature `{header:"x-jstack-signature",encoding:"hex",prefix:"sha256=",secretRef:...}`. Verify `webhookSignature:"set"` and the expected signature metadata while still disabled. If the save response is lost, inspect this task by ID before requesting a new secret. Never resubmit a consumed reference or enable an unsigned task.
5. Save only the returned HTTPS endpoint to `webhook-url` under the private directory. Start the server with the command below. Retain its process/session identifier. The private key is read only by the sender. Verify the local page and fixed scope before enabling the recorded task with `update_scheduled_task({scheduledTaskId:...,enabled:true})`. Re-read that task's binding and signature state after enabling.

The user runs this hidden-input command after setup reaches step 3. It refuses to replace an existing file:

```sh
python3 /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/code/scripts/jstack/bot_ui_transport.py \
  init-secret /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/signing-key
```

The agent starts the server only after the approved private provisioning:

```sh
python3 -B /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/code/scripts/jstack/bot_ui_local.py \
  --journal /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/requests.sqlite \
  --repository juancamiloqhz/skills --pr 109 serve \
  --bind 127.0.0.1 --port 8879 --origin http://127.0.0.1:8879 \
  --url-file /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/webhook-url \
  --secret-file /home/ubuntu/.cache/jstack/bot-ui-pilot-20261019/signing-key
```

## Live evidence to collect

Use one request per check, with no automatic retry. On an uncertain response, inspect the saved state and receiving conversation before taking another action.

1. Send the harmless `probe` payload through the existing transport CLI, with request ID `pilot-probe-20261019`, repository `juancamiloqhz/skills`, PR `109`. It should receive an accepted delivery and produce no PR action. It is not a journalled check request. Do not claim the page is live from this HTTP response alone.
2. Send one unsigned probe using the same fixed payload and returned endpoint. Expect signature rejection and no corresponding receiving turn. Inspect T3's task/conversation evidence. A 401 alone proves only HTTP rejection; if absence of dispatch cannot be established, record that limitation. Stop on unexpected acceptance rather than probing with arbitrary inputs.
3. Open the loopback page with `preview_status`, `preview_open` if needed, then `preview_navigate`. Click Check PR once. Record its request ID and delivery receipt. End the initiating turn so the scheduled wake can run in this conversation; do not substitute a manual invocation for a webhook wake. The receiving turn must read the fixed prompt, acquire the claim, publish the actual GitHub result and acknowledge it. Only after that turn, refresh the page and expect completed. A missing wake remains incomplete. Resume the remaining pilot coordination on an ordinary continuation turn; the webhook turn itself has only the receiver authority in its prompt. Do not add a timer or broaden the receiver to bypass that boundary.
4. Test recovery with one new request: temporarily disable only this pilot's task, click Start another check and Check PR. Confirm disabled delivery and an unowned pending record. Re-enable the signed task. This failed request will not replay automatically. Create one additional local request ID in a fresh incognito browser profile and click once to produce a real wake. The receiver handles that new request, then drains the previously failed record. Both require their own successful claim, result and acknowledgement. Record one result per ID. This uses a separate profile because the ordinary page correctly blocks replacing an unresolved request.
5. Reload the original page and restart only the local server against the same journal. Verify completed state persists without another webhook send. Repeated claim attempts for acknowledged IDs must return `granted:false`. Retain any uncertain or claimed-but-unacknowledged record for investigation.

This pilot uses at most three check-pr requests: the initial success, one failed delivery, and one new wake for recovery. The probe and unsigned negative check are separate. Do not expand the action set, add polling or alter model assignments. Permission to run this test covers its temporary webhook and these bounded requests, not a permanent service.

## Cleanup and completion

On success or abandonment, disable the recorded pilot task and confirm that state. Delete it by its exact recorded ID and confirm deletion. Stop the owned server by its recorded process/session, checking identity before signalling it. Close only the owned preview tab. Confirm the listening socket is gone. Do not kill whatever later occupies the port.

After the task is deleted and owned runs are no longer active, preserve one concise result with request IDs, outcomes, actual receiving evidence and remaining limits. Then remove only this pilot's directory, including key, endpoint and journal. On incomplete recovery, retain its journal privately until the finding is captured or investigation closes; do not commit it. If task deletion cannot be confirmed, keep it disabled and retain ownership records. Do not declare cleanup complete or delete recovery evidence prematurely.

The success claim is deliberately limited to loopback-page delivery and real receiving-agent recovery. Tailnet peer reachability, broader button actions and the packaged standalone skill remain pending. A successful test does not authorize keeping the webhook or server running.

## Preparation evidence and source comparison

Read the current scheduler/secret tool contracts and checked `orchestrator_capabilities` on 2026-10-19. Scheduled tasks are available; the calling conversation is the fixed ID above. Orbit's proposed loopback port was available at preparation time and the pilot directory did not previously exist. A private read-only helper snapshot was prepared from PR #109's merge. No task, live endpoint, signing key or network exposure was created. Connect availability cannot be inferred from the capability flag and remains a setup gate.

Manually checked the receiver branches against the merged helper: malformed and mismatched bodies, ignored probe, missing/owned/already acknowledged records, granted and denied claims, GitHub failure, acknowledgement failure and recovery draining. Checked the helper CLI's advertised options. This is a contract review, not live execution or a new agent-evaluation result. Existing 22-test evidence remains applicable because no executable code changed. Documentation/link and diff checks passed.

Compared with all six phases of `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. The plan preserves create → URL → private key → local server/probe/recovery → network access → wake handling. T3's disabled webhook task, one-use secret card, HMAC signature and `{{body}}` template replace Grok-specific mechanisms as recorded in the design. The receiver prompt and SQLite ownership steps implement the source's routine-side log drain for asynchronous T3 delivery. This pilot intentionally leaves the source's tailnet phase untested; it does not silently change the final skill to loopback-only or mark that phase supported.
