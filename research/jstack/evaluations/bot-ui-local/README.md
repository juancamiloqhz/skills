# Local bot UI and recovery

Date: 2026-10-19. Builds on the sender merged in PR #108. This is development tooling for the [Make bot UI design](../../integrations/make-bot-ui.md), not an installed skill or a live service. The package count remains 56.

## What changed

The [local server](../../../../scripts/jstack/bot_ui_local.py) serves a small [button page](../../../../scripts/jstack/bot_ui_assets/index.html). Its configuration fixes one repository and PR. The browser sends only a request ID. The server constructs `check-pr`, repository and PR, saves that exact payload, then calls the existing signed sender once. Neither the key nor webhook URL reaches the browser.

The page keeps the request ID in local browser storage. Refreshing or reopening it reads status without sending another webhook. It permits a new check after the receiver saves the result and acknowledges the previous one. Older acknowledgements without a saved result require reconciliation. Different browser profiles or devices can create different IDs; this is deduplication by request ID, not a global limit of one PR check.

The server requires an explicitly allowed Host and a matching Origin on POST, a small JSON body and the exact field set. It serves only the page, script, fixed scope and request status. It rejects attempts to select another endpoint, repository, PR or action. CSP blocks inline scripts, framing and external connections. These browser controls do not authenticate a non-browser client. An eventual tailnet service must be restricted to the intended peers; this unit binds only to loopback by default and does not expose a service.

## Durable recovery contract

A task-owned SQLite database keeps the original request, delivery receipt, processing owner, bounded PR-status result and acknowledgement. The result is stored in the same private database, not in a separate log. An additive results table leaves existing request records unchanged. Its directory must be owned and mode 0700; the database must be an owned private regular file. Reusing it for another repository or PR fails. Keep it outside Git alongside the UI's private configuration.

1. Save the request before sending. A crash before or after the POST leaves an unknown receipt rather than losing the request. Repeated POSTs with the same ID return the saved state without resending.
2. The receiving agent uses the configured journal path, repository and PR, never paths or scope supplied by a webhook. It compares the incoming fields with the recorded payload. A `probe` does no work. Unknown IDs and mismatches do no work.
3. Before performing the read-only check, call `claim` with that request ID and a unique identifier for the receiving run. Only `granted: true` permits execution. A second claim, including the same owner's second claim, returns false. The CLI returning successfully alone is not permission to execute.
4. Run the fixed read-only `gh pr view` command and require success. Pass its exact JSON output to `save-result` with the claim owner. Require `saved: true` before publishing. The helper checks the fixed PR number, URL, state, commits and merge time; it rejects other fields. A repeated identical save succeeds without changing its timestamp. A different result or owner fails. If saving fails, stop with the claim retained and report incomplete.
5. Publish the saved result in the bound conversation with its request ID, then call `ack` with the recorded owner and a result reference. An identical repeated acknowledgement succeeds; another owner or conflicting reference fails. A new acknowledgement requires a saved result. Delivery acceptance alone never acknowledges work.
6. On a later wake, or an explicit manual recovery, read `pending` and claim each unowned request through the same protocol. Failed and uncertain requests are processed from their recorded payload, without another webhook POST. Claimed but unacknowledged requests require reconciliation with the original run and result. They are never automatically reassigned.

For an explicit recovery of a missing conversation message, use `result --request-id` to read the saved payload, PR status, save time and acknowledgement. Confirm that they match the fixed scope and requested ID. Redisplay that saved observation with its timestamp and explain that it is historical, not a fresh GitHub query. Leave an existing acknowledgement unchanged. For a saved but unacknowledged result, only the original owner can acknowledge after publication; another run must leave the claim in place. No new claim, webhook or PR query is needed to redisplay a saved result.

A missing result is not permission to rerun the action. Legacy acknowledgements are exposed as `acknowledged_without_result`, excluded from pending work, and cannot be backfilled with a later observation. A claim without a saved result still needs reconciliation with its original run. The helper cannot prove that a conversation message remains visible or detect a T3 rollback; saved results make recovery possible without repeating the action.

These are receiver integration requirements, not an implemented agent routine. The helper CLI tests exercise the ownership protocol locally. If no wake arrives, the record waits for a later wake or manual recovery; no background poller drains it. A crashed owner can leave a request stuck. Preserve it and investigate instead of granting duplicate execution. This does not promise exactly-once effects or enforce what an agent does after receiving a claim.

Receiver command shape, with a fixed task-owned path and scope:

```sh
python3 scripts/jstack/bot_ui_local.py --journal /owned/private/ui/requests.sqlite \
  --repository owner/repo --pr 123 pending
python3 scripts/jstack/bot_ui_local.py --journal /owned/private/ui/requests.sqlite \
  --repository owner/repo --pr 123 claim --request-id REQUEST_ID --owner RUN_ID
# Only after granted:true, run the fixed check and save its successful output.
# Save only after gh exits successfully; also detect a failed save pipeline.
set -o pipefail
pr_status_json=$(gh pr view 123 --repo owner/repo --json number,state,mergedAt,mergeCommit,headRefOid,url) && \
  printf '%s' "$pr_status_json" | \
  python3 scripts/jstack/bot_ui_local.py --journal /owned/private/ui/requests.sqlite \
    --repository owner/repo --pr 123 save-result --request-id REQUEST_ID --owner RUN_ID
# Require saved:true; read and publish the saved observation before acknowledging.
python3 scripts/jstack/bot_ui_local.py --journal /owned/private/ui/requests.sqlite \
  --repository owner/repo --pr 123 result --request-id REQUEST_ID
python3 scripts/jstack/bot_ui_local.py --journal /owned/private/ui/requests.sqlite \
  --repository owner/repo --pr 123 ack --request-id REQUEST_ID --owner RUN_ID \
  --evidence RESULT_REFERENCE
```

## Verification

The [durable-result evaluation](../bot-ui-durable-results/README.md) records the later rollback correction and current reproduction steps. The original PR #109 evidence below used acknowledgements without saved results; its protocol is superseded above.

Twenty-two tests passed on Ubuntu/Python 3, including the 13 existing transport tests and the pinned installed-runtime verifier probe. Nine new tests cover the button server and journal:

- A real HTTP click request reaches a loopback webhook with the fixed payload. Browser assets/responses contain neither the fixture key nor endpoint. Acceptance leaves processing pending.
- Wrong origins/hosts, content types, transfer encoding, oversized bodies, extra fields and changed targets are rejected before sending.
- Concurrent identical submissions produce one send. Concurrent receiver claims grant one owner. Repeated claims cannot authorize a second execution.
- Dropping the receiver connection after receipt leaves unknown delivery. Restarting preserves the original payload, owner and acknowledgement. Repeated browser submissions after restart do not resend.
- Failure to write intent prevents sending. Failure to save a receipt after sending retains the original unknown record and prevents a retry. Crashes after intent or claim require reconciliation.
- Rejected signatures and local sender errors remain pending without exposing raw error text. The CLI drains and acknowledges a fixture request; conflicting or unowned acknowledgements fail.
- Public directories/files, symlink databases and reuse with another scope fail.

The T3 collaborative browser exercised the actual page against [preview_fixture.py](preview_fixture.py). One click produced accepted delivery, reloading kept the same ID and the fake receiver count stayed one. A fixture receiver claim and acknowledgement enabled a second check. The second receiver deliberately disconnected after receipt; the page displayed unknown delivery and disabled another check. Restarting the local server preserved it. Manual fixture recovery and acknowledgement changed the page to completed; the receiver count remained two. These acknowledgements represent fixture results, not actual PR reviews. One browser-tool click used invalid locator syntax; correcting it completed the scenario. No application failure was observed.

```sh
python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
node scripts/jstack/check_docs.mjs
```

The portable command skips the installed-verifier probe. The runtime path used was `/home/ubuntu/.t3/runtime/versions/0.1.1-nightly.20261019.3360/t3`; its verifier pin and limitations remain in the [transport report](../bot-ui-transport/README.md).

For a local browser reproduction with public fixture credentials only:

```sh
fixture_dir=$(mktemp -d)
python3 -B research/jstack/evaluations/bot-ui-local/preview_fixture.py --directory "$fixture_dir"
```

Open `http://127.0.0.1:8879` and click Check PR. Run the receiver commands above against `$fixture_dir/requests.sqlite`, repository `example/fixture`, PR `123`, and the page's request ID. Save a synthetic status JSON object with that fixture URL/number and valid commit fields, then use an explicitly named fixture result reference. Refresh status to see completion, then start another check. Create `$fixture_dir/drop` before the next click to simulate lost delivery confirmation. Stop/restart the fixture with the same directory to check persistence. `$fixture_dir/received-count` records how many POSTs reached the fake webhook. A new directory requires clearing this page's local storage or using a fresh browser profile.

Stop the fixture server before deleting its scratch directory. The fixture database, public dummy key, counter and browser trace are temporary evidence and are not committed. A real service's journal is operational data: retain its request IDs and acknowledgements for that service's lifetime so old deliveries cannot be treated as new. Retiring the service and its receiver is a separate cleanup step.

## Source comparison and remaining work

Compared the final files with all six phases of `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`.

| Source requirement | Implementation / necessary difference |
| --- | --- |
| Host page; buttons call local server; key stays server-side | Implemented by the server and assets. Fixed read-only PR scope follows the approved first implementation boundary. |
| Small JSON, eight-second timeout, one attempt | Uses the merged transport unchanged. The measured contract is an eight-second socket timeout, not a total wall-clock deadline. |
| Append the same failed JSON locally; drain from routine | SQLite retains exact payloads and separates receipt, claim and acknowledgement. Intent is saved before sending because T3 dispatch is asynchronous and direct deliveries do not deduplicate payload IDs. Atomic claims handle racing wake/recovery attempts. Routine-side integration remains pending. |
| Bind `0.0.0.0` for tailnet access | CLI supports explicit `--bind 0.0.0.0` and exact allowed HTTP origins. The prototype defaults to loopback because no exposure was requested. The final tailnet workflow must preserve the source's requested binding. |
| Create routine, copy URL/key, secret request, tailnet, handle wake | Prior design and sender work remain applicable. This PR does not create or test these live integrations. |
| Harmless ignored probe before saying live | Still required for the live pilot. A local fixture is not this probe and nothing is advertised as live. |

The next unit must make the live task prompt, shared journal location, private key provisioning, Connect endpoint, requested exposure and cleanup concrete for approval. Verify an actual bound receiving run and its recovery path before shipping the standalone skill. No schedules, saved model choices, installed skills, Tailscale settings or reviewed upstream checkpoint changed here.
