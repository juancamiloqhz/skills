# Bot UI transport foundation

Date: 2026-10-19. This implements the server-side sender and private local key setup for the [Make bot UI design](../../integrations/make-bot-ui.md), merged in PR #107. It does not ship `jstack-make-bot-ui`, serve a page, create a scheduled task, change an installation or establish live T3 delivery. The package count remains 56.

## Implemented behavior

[`bot_ui_transport.py`](../../../../scripts/jstack/bot_ui_transport.py) accepts one bounded `check-pr` or ignored `probe` request, serializes it once, signs those exact UTF-8 bytes with HMAC-SHA256 and posts them once. Its receiver configuration must use header `x-jstack-signature`, encoding `hex` and prefix `sha256=`. It follows no redirects, retries nothing and uses an eight-second socket timeout. Only an explicit test-only API option permits HTTP to a literal loopback IP; the CLI requires HTTPS.

The request has exactly `requestId`, `action`, `repository` and positive integer `pr`. The future server must still bind repository/PR/action to its user-approved button; this transport validates shape, not browser authorization. Keep the request ID stable when investigating an uncertain delivery. It is not an idempotency guarantee.

Receipts distinguish accepted delivery, a duplicate relay delivery, rejection and unknown outcome. HTTP 202 is accepted only with the expected outcome header and a valid delivery ID. A `prompt_too_long` outcome is rejected even with HTTP 202. A dropped connection, unexpected success body, redirect or server error is unknown. Neither accepted nor duplicate means the agent started or completed the requested action. Outputs omit the endpoint, key, signature and response body.

`init-secret` is a command the user runs in their own terminal. It collects and confirms hidden input, creates a new mode-0600 key file under an owned private directory, and refuses to replace an existing file. It stops if input cannot be hidden. Key reads reject public permissions, symlinks, nonregular files and opaque `secret-ref:` values. It never reads T3's credential store. The user must later enter the same key through T3's private secret card; that second leg was not exercised here.

## Runtime evidence

Inspected the installed executable at `/home/ubuntu/.t3/runtime/versions/0.1.1-nightly.20261019.3360/t3`, using its bundled source-region markers. No application database, credential store or live scheduler was accessed.

| Runtime source region | Observed contract |
| --- | --- |
| `src/scheduledTasks/webhookVerification.ts` | HMAC-SHA256 covers the exact body bytes. The configured header name is normalized to lowercase; hex or base64 encoding and a configured prefix are supported. |
| `src/scheduledTasks/webhookRoute.ts` | Reads raw request bytes, limits bodies to 1 MiB, returns 202 with `deliveryId` plus `x-t3-hook-outcome`, and maps signature rejection to 401, missing hooks to 404, disabled hooks to 409, expired delivery to 410, oversized body to 413 and rate limits to 429. |
| `src/scheduledTasks/ScheduledTaskService.ts` | Dispatch is asynchronous after acceptance. Oversized rendered prompts can produce a 202 outcome `prompt_too_long`; trusted relay duplicates can produce `duplicate`. Direct deliveries get fresh delivery IDs. Payload request IDs are not automatically deduplicated. |
| `src/secrets/SecretRequests.ts` | The secret reference is consumed within the application; the advertised tool contract supplies no reference-to-local-file export. The helper therefore provisions its own user-provided file. |

Only the pure signature verifier was executed, extracted from the installed binary into an isolated JavaScript context with Node crypto. [probe_runtime.mjs](probe_runtime.mjs) checks the extracted section SHA-256 `f8f78ec57c6ead5396df95fa4af3eb8d6a9988da1136fbf0478e3f3dacd0be67` before evaluating it. It refuses changed source until reviewed. It does not launch T3 or copy its runtime source into this repository. Route/status and scheduling conclusions above are source inspection, not live endpoint results.

## Tests and observations

Thirteen tests passed, including the optional installed-verifier probe. The [test suite](../../../../scripts/jstack/test_bot_ui_transport.py) uses owned temporary directories and a loopback fixture server, with public dummy key material explicitly identified as a fixture.

- Captured the sender's real POST bytes and header. The actual T3 verifier accepted them and rejected a missing header, different key, appended newline, changed PR and incorrect prefix: six checks against the pinned verifier.
- Checked accepted and duplicate receipts, all documented rejection statuses, redirect refusal, malformed/oversized response bodies, missing outcome metadata and the HTTP-202 oversized-prompt case. Each fixture saw one request.
- Closed the connection after receiving a request. The sender returned unknown without resending. This exercises ambiguous receipt handling, not durable queue recovery.
- Exercised the key CLI through a real pseudo-terminal. It saved the exact Unicode key bytes with private permissions without echoing the key. Rejected piped input, failed hidden input, pre-existing files, insecure directories/files, symlinks and secret-reference misuse.
- Rejected invalid action/extra fields, boolean PR numbers, malformed request IDs and unsafe endpoint forms before network transmission. A valid request on the same fixture was then accepted.
- Simulated a timeout to verify the safe CLI receipt and socket timeout configuration. The local wire fixtures use HTTP; TLS and the eight-second wall-clock behavior were not measured.

The first test run had a test-harness `patch.object` call error; correcting its target allowed the timeout assertion to execute. This was not a demonstrated product defect. The probe hash and final test results above describe the final code.

## Reproduce

```sh
python3 -B -m unittest discover -s scripts/jstack -p test_bot_ui_transport.py
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p test_bot_ui_transport.py
node scripts/jstack/check_docs.mjs
```

The first command runs portable transport tests and skips the installed-verifier check. The second includes it and requires the reviewed verifier region; point it at the installed T3 executable, not a running service. The probe consumes captured fixture bytes from the test. It never needs a real key or endpoint. Unix file permissions and pseudo-terminals are part of this tested Linux implementation; other platforms need their own evidence.

For the later authorized pilot, the user can run `python3 scripts/jstack/bot_ui_transport.py init-secret <private-dir>/signing-key` in a private terminal after creating that directory with mode 0700. The sender CLI reads a known returned HTTPS endpoint from `--url-file`, the key from `--secret-file`, and the JSON request from stdin. It does not discover or create a webhook. Do not treat these development commands as an installed skill or expose them directly to arbitrary browser input.

## Fidelity and remaining work

Compared this unit with `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. It addresses parts of Request the sender key and Host the page on this computer: server-only key storage, a small JSON POST, one attempt, timeout and honest delivery reporting. T3's HMAC header and 202 receipt replace Grok's bearer headers and 200 wake response. The source's other four phases are not implemented by these helpers.

The private card-to-scheduler leg, fresh task creation/disabled-state recovery, browser UI and origin/scope checks, tailnet and Connect reachability, real receiving-agent behavior, durable failure log, routine-side draining and acknowledgement, duplicate-effect prevention and owned service cleanup remain pending. The failed-delivery log is not silently replaced by receipts; the complete UI must implement it before live support is claimed. No automatic retry or live probe was added to compensate for those missing pieces.

The next unit can build the bounded local UI and recovery handling against this transport. A live pilot still needs a concrete task, endpoint provisioning and network exposure scope. Preserve the weekly upstream schedule, saved models, manual installation and upstream reviewed checkpoint. Retain this report and reproducer; raw runtime excerpts and temporary test artifacts are not committed.
