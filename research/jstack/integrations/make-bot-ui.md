# Make bot UI: proposed T3 adaptation

Status: design merged in PR #107 on 2026-10-19. The user asked to continue with the recommended T3 target. The [transport foundation](../evaluations/bot-ui-transport/README.md) merged in PR #108. The [local button page and recovery journal](../evaluations/bot-ui-local/README.md) merged in PR #109 with fixture and browser evidence. The [live pilot](../evaluations/bot-ui-live-pilot/results.md) verified one real browser-triggered result and acknowledgement, but remains incomplete because the public receipt was unknown and the recovery turn was rolled back. A source-backed correction now distinguishes recorded delivery from dispatch acceptance; its live verification and the recovery finding remain open. The [durable-result correction](../evaluations/bot-ui-durable-results/README.md) now saves the small PR observation before publication so a missing message can be redisplayed without rerunning the check. Its temporary task, server and key have been removed. The standalone skill, full recovery evidence and tailnet verification remain pending. The implementation retains pstack's page → local server → authenticated agent wake.

Source: [`pstack/skills/make-bot-ui/SKILL.md`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/make-bot-ui/SKILL.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The complete source body was compared with the live T3 tool declarations. This is the remaining unported top-level pstack skill; Unslop remains an external dependency. Benny is a separate automation pack.

## What the user would get

A small page with a button such as **Check my PR**. Clicking it sends a bounded request to an existing T3 conversation; the agent checks the chosen PR and reports there. The page shows whether delivery was accepted or failed. Acceptance is not a claim that the review completed. The first version would not need to stream the conversation back into the page.

Proposed future request, after implementation and manual installation:

```text
$jstack-make-bot-ui Build a page with a Check PR #123 button. Send a read-only status request to this conversation. Make the page reachable on my existing tailnet.
```

`jstack-make-bot-ui` is a proposed name, not an available command. The example authorizes a specific status action, not fixes, merges or arbitrary commands from the page.

## What T3 exposes, and what is still unknown

On 2026-10-19, `orchestrator_capabilities` reported `scheduledTasks: true`. The callable `schedule_task` declaration accepts a structured webhook trigger, an optional HMAC-SHA256 signature configuration and a private `secretRef`. Runs bind to the current conversation by default. It returns a public `webhookUrl` only when T3 Connect managed remote access is available. Capability exposure does not establish that remote access is enabled on this machine.

The `request_secret` declaration returns an opaque reference consumed once by a receiving tool. It does not return the secret value or promise a file that a local UI server can read. This is the main provisioning difference from pstack's Grok Bot connector credential file. The agent must not treat the reference as a signing key or extract the app's stored credential.

T3 webhook prompts receive request values only through explicit placeholders such as `{{body.action}}` and `{{body}}`, framed as untrusted data. They do not receive Grok Bot's `[routine]` / `<webhook_event>` envelope. The tool declaration exposes signature header, encoding and prefix, but it does not fully specify the bytes to sign, HTTP acceptance codes, duplicate-delivery behavior or replay prevention. The subsequent [runtime inspection and verifier probe](../evaluations/bot-ui-transport/README.md#runtime-evidence) establish the exact signing bytes and local response contract for one installed version. The later pilot verified one live delivery; the public relay response differs from this direct-route contract as recorded in the linked results.

No secret request, schedule creation, webhook POST, tunnel inspection, installation or network exposure was performed for this design. The existing weekly upstream schedule was not read or modified.

## Preserve each upstream phase

| Upstream phase | Proposed T3 behavior | Why it must differ / remaining proof |
| --- | --- | --- |
| Create the webhook routine | Create one explicitly requested webhook task using `schedule_task`, bound to the current conversation, initially disabled while wiring is incomplete. Record the returned task ID and reuse it during setup recovery. Apply the signature with `update_scheduled_task` before enabling delivery. | T3 has no Grok `update_state` routine interface. The update tool advertises `enabled` and signature changes; confirm the disabled-task and enable lifecycle in a pilot before relying on it. |
| Copy the URL and the sender key | Use the returned public URL. If absent, explain that T3 Connect remote access is required and stop live setup. The sender's key comes from the user's private local provisioning, not a copied Grok routine panel. | Do not invent Cursor UI clicks, derive an endpoint or silently replace T3 Connect with another tunnel. |
| Request the sender key | The user provisions one signing secret privately to the local server and enters the same value through `request_secret` for the scheduler's `signature.secretRef`. Use only advertised secret-reference consumers. | T3 provides no advertised secret-reference-to-local-file bridge. The local provisioning mechanism must be reviewed and tested before shipping. Never request the value in chat or bake it into a page. |
| Host the page on this computer | Browser buttons call the local server; only the server signs and sends a small JSON object. Preserve the eight-second timeout, one attempt, no automatic retry, harmless probe and failed-delivery log. | Replace the two Grok bearer headers with the verified T3 signature protocol. Confirm actual success responses instead of hardcoding Grok's HTTP 200 assumption. |
| Put the page on the tailnet | Reuse an existing online node and return its actual hostname and IPv4 HTTP URLs. Retain the source's `0.0.0.0:<port>` binding for the requested tailnet use. Missing installation/login is an explicit setup dependency. | Tailnet access to the page and T3 Connect access to the webhook are separate paths. Do not promise one establishes the other. Node installation, login and service exposure need the user's concrete setup request. |
| Handle the webhook wake | Declare the expected action/parameters in the task prompt, insert the relevant request placeholders, and handle them as data within the selected action's authority. Report completion in the bound conversation. | Replace the Grok event parser; untrusted fields cannot select new skills, tools or broader permissions. Verify the actual receiving conversation and action, not only the sender's HTTP result. |

Preserve the source's failure log and routine-side draining rather than quietly dropping delivery recovery. The implementation must settle how the bound task reads that task-owned log, who acknowledges processed entries, and how it avoids applying a timed-out-but-delivered request twice. The [local recovery implementation](../evaluations/bot-ui-local/README.md) uses stable request IDs, durable intent, atomic claims and explicit acknowledgement. Fixture tests cover ambiguous receipt, concurrent ownership and restart; an actual bound routine must still prove that it follows the protocol. Do not claim exactly-once transport or live recovery. Polling remains outside the primary delivery path, and media bytes stay outside the webhook payload.

## Proposed implementation boundary

Keep one standalone `jstack-make-bot-ui` package with the six upstream phases, explicit invocation metadata and the original license. Record substitutions in `research/jstack/adaptations/` and add its source mapping only when a package exists. Do not create an empty installed skill to improve the coverage count. Help and the guide should continue to call it pending until the implementation meets its acceptance conditions.

The first implementation should provide a bounded read-only action such as the PR-status example. It needs a task-owned local server/config location, protected server-side secret provisioning, a fixed receiving endpoint and an explicit action contract. Browser responses and logs must omit secret material. Browser requests must not be able to change the endpoint, choose another repository or enlarge the allowed action. Implement ordinary request validation and protection against unrelated browser origins at that boundary. These requirements follow from the page issuing authenticated requests on the user's behalf; the bot is not a general remote shell.

Do not add a new model role. Scheduler execution inherits the calling conversation's provider/model/runtime settings according to its tool contract. Any workflow that delegates later must use existing jstack model resolution; a webhook does not override saved roles or activate Juan-mode automatically.

Benny's Slack triage, issue creation, deduplication, compensation and reproduction/fix stages are not part of this port. Plugin distribution, full conversation streaming, alternate bot backends and a general secret broker also remain separate work. Retain the current portable Skills CLI distribution and external Unslop choice.

## Verification before marking it supported

| Check | Required evidence |
| --- | --- |
| Sender protocol | Receiver implementation or primary protocol documentation establishes the exact signed bytes/header format. A real signed request is accepted; missing/invalid signatures and modified bodies are rejected without an agent run. |
| Private provisioning | The same user-provided secret reaches both sides privately. Browser assets, requests to the local server, responses and logs contain no signing key. A secret reference never becomes a local substitute key. |
| One-click wake | A browser click on the owned page reaches exactly the intended bound conversation with the expected action and request ID. The visible UI separates delivery from completed work. |
| Untrusted input | Unsupported actions, changed repository targets and instruction-like payload fields cannot exceed the fixed read-only scope. Invalid input produces no product mutation. |
| Failure and recovery | Timeout/failure appends the original small JSON once; routine-side draining and acknowledgement account for ambiguous delivery without repeating an effect. This is measured recovery, not assumed scheduler deduplication. |
| Missing capabilities | No Connect URL, absent secret consumer, unavailable local server or missing tailnet access yields an accurate incomplete result without invented endpoints or silent fallback. |
| Tailnet access | Check the actual node/address, requested binding and page response from an authorized peer; a successful local loopback request alone does not prove peer reachability. |
| Ownership and cleanup | Failed setup leaves its own task disabled or removes it by recorded ID; cleanup stops only its server and removes only task-owned test data. Existing schedules, nodes and services remain intact. |

Unit tests can cover the sender and payload handling after the receiving protocol is known. A local fake receiver cannot establish T3 integration. Use a harmless ignored probe first, then a bounded read-only live action with explicit provisioning authority. Keep one concise results report and necessary fixtures, not secret captures or full transcripts.

## Next decision and completion boundary

Recommend the T3 webhook target because jstack already targets T3 and its scheduler can bind delivery to the current conversation. A Grok-specific port would retain the original backend but require a separate supported Grok host; silently changing the original instructions to unsigned URL-only delivery would discard its authenticated-server behavior.

The approved design selects the T3 target. Continue from the tested local sender, button page and recovery journal. Resolve the public-relay receipt mismatch and recovery evidence, then complete tailnet verification before claiming support. For a later live pilot, define its fresh task, request budget, private provisioning and cleanup before execution. Merging this design records the plan; it does not create a webhook or claim a finished skill. If the required secret/protocol path cannot be established, retain Make bot UI as an explicit gap and continue provider verification separately.
