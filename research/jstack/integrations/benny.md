# Benny: proposed T3 integration

Status: inactive source pack implemented, 2026-10-19. The [pack and local setup evaluation](../evaluations/benny-dormant-pack/README.md) cover the first implementation unit's copy/discovery checks; fresh-provider dependency proof remains pending. No Slack app, tracker issue, task, child agent, service or installation was created. Existing model choices and the reviewed upstream checkpoint are unchanged.

Source: all 12 files in [`pstack/automations/benny`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/automations/benny) at `0148b78c56c72a1b8412055913c79f767095b217`, read in full. Preserve its dormant pack boundary and two-stage lifecycle. The weekly upstream schedule and Make bot UI do not implement Benny.

## What it would do

A person posts “Saving a draft loses the title” in a configured Slack issue channel. Triage reads that exact thread, checks the repository and tracker, and posts one short verdict there. A separate reproduction workflow accepts only a configured triage identity's bug marker, respects anyone already fixing it, and tries the reported UI path twice. It may prepare a small draft PR only after confirmed evidence and the fix gates. It never merges or deploys.

This is useful for a project that receives bug reports in Slack. Ordinary jstack work does not require it. A target repository, channel, tracker and runnable test app have not been selected for this design.

## Preserve the complete source pack

Paths below are relative to the pinned source directory. These are direct automation instructions, not three new catalog commands.

| Source files | Required counterpart |
| --- | --- |
| `README.md`, `FOR_AGENTS.md` | Human setup entry, conflict-preserving whole-pack copy, user-owned configuration outside the pack, separate approval for live creation. |
| `skills/setup-benny/SKILL.md` | All eight steps, including project dependency proof, configuration, capabilities, routing, control adapter, sequential creation/update flow and seven thread-safety checks. |
| `skills/triage-issue-reports/SKILL.md` | All ten steps: immutable coordinates, full evidence, cause tracing, classification, routing, tracker adapter, dedupe, new-issue gates, one verdict and bounded follow-up. |
| `skills/triage-issue-reports/references/routing.example.md` | Evidence-based routing, no cross-posts and owner pings off by default. |
| `skills/reproduce-and-fix-issues/SKILL.md` | All fifteen steps, trusted markers, human ownership, existing-fix branch, two independent repros, media review, rejection window, bounded fix, draft-only PR and cleanup. |
| `skills/reproduce-and-fix-issues/references/control-adapter.md` | Seven capabilities and nine-step harmless setup check. Real UI actions, read-only state inspection, reset, screenshots, recordings and owned cleanup. |
| `skills/reproduce-and-fix-issues/references/feature-map.example.md` | User paths, stable selectors, states, preconditions, reset and discriminating evidence. Keep all fictional example sections. |
| `skills/reproduce-and-fix-issues/references/verify-existing-fix.md` | Isolated baseline/patched builds, twice on each, confirmed/insufficient/inconclusive outcomes, no competing edits or PR. |
| `templates/configuration.example.yaml`, `templates/triage-automation-prompt.md`, `templates/reproduce-automation-prompt.md` | External configuration and small prompts reading exact committed operational files; preserve every source field group and marker. |

Repository packaging is `automations/jstack/benny/`, copied to a target's `.agents/automations/benny/`. User-owned configuration/maps live separately, for example `.agents/benny/`. These translate Cursor-owned directories while preserving the source tree, nested names and direct-read boundary. The actual Skills CLI 1.7.2 discovery test excludes the nested procedures through `metadata.internal: true`, including full-depth and wildcard listings; explicit internal opt-in overrides this filter. Other installers still require their own discovery check. If that cannot be excluded, resolve distribution before shipping the pack; do not silently flatten, rename away, or strip its procedures.

Preserve MIT notices and keep source pins/differences in research. A future installer must preserve destination-only files and review changed source-managed files; no overwrite-by-copy refresh. Existing target configuration remains user-owned.

## Available runtime and concrete gaps

Inspected the current callable tool declarations and T3 capabilities on 2026-10-19. `scheduledTasks` and app-owned subagents are advertised. This is capability evidence, not a deployed integration test. No Slack, Linear or general tool-search entry was exposed in this session's catalog. Jira tools are present, but no account/project was read or selected. This does not establish which integrations another runtime may provide.

| Boundary | Proposed adaptation and remaining evidence |
| --- | --- |
| Project dependencies | Replace Cursor plugin activation with verified project-scoped jstack dependencies plus external Unslop. Preserve the fresh-checkout test for How, Why, TDD and all six named principles. Current-session or global installations do not satisfy it. No automatic installer or plugin redesign is selected here. |
| Slack event trigger | T3 `schedule_task` advertises interval, fixed-time and generic webhook triggers, not a native new-top-level-Slack-message trigger. A supported connector trigger or an explicitly deployed event bridge is required. A Slack read/reply connector alone is not event ingestion. |
| Two live workflows | Keep triage and reproduction independently configured and lifecycle-managed. For a bridge, route each accepted root report to both workflow endpoints, retaining the repro marker wait. Do not replace repro with “triage calls a fixer.” |
| Conversation/model selection | T3 tasks inherit their creating thread's provider/model; the schedule schema has no per-task model selector. Recommend separately requested automation conversations when stages need independent execution/settings. Creating top-level threads requires an explicit user request. Preserve the four Benny configuration choices for triage, reproduce, code and media review; validate against live capabilities without adding global role keys or changing saved models. Shared helpers continue their established jstack role resolution. |
| Creation/update | Replace Cursor's unavailable built-in `/automate` editor flow with a concrete reviewed T3 draft: trigger, fixed scope, prompt, repository revision, dependencies, model settings, credentials and cleanup. Obtain live-creation authority; create triage disabled, verify it, then prepare repro. Commit referenced files first. Reuse recorded task IDs for updates and lost-response reconciliation. This runtime replacement requires user selection before deployment; it is not permission to bypass upstream review. |
| Slack reads/writes | Require thread reads, stable permalinks, attachment access, exact thread-only replies and read-back verification. Optional operations-channel posts/edits stay separate. Keep the source coordinates immutable and preflight before tracker writes and each source reply. No connector capability is inferred from its name alone. |
| Tracker | Preserve vendor-neutral search/read/create/update/source-link/compensation contract. GitHub Issues, Linear or Jira can be selected only after all required semantics are demonstrated. No tracker has been selected. Compensate only issues created by this run; never undo unrelated edits or a pre-existing issue. |
| Child isolation | The current `delegate_task` schema exposes model/runtime/worktree selection, not a tool allowlist or credential exclusion. A prompt ban or a worktree alone does not prove that Slack writes are impossible. Keep optional analysis/editing in the coordinator until exclusion is demonstrated. Independent media review remains a repro gate; if a suitable isolated reviewer cannot run, repro cannot be marked confirmed. |
| UI control | Existing jstack browser tooling is a candidate, not a complete target-app adapter. Require a selected app/environment, completed feature map, real interaction, independent reset, read-only cross-check, screenshot, video and cleanup. No target app was tested here. |
| Waits and races | Preserve source verdict, rejection and follow-up budgets. Verify that waiting for a marker cannot block the triage workflow that produces it, and that repeated event delivery cannot start competing fixes. A scheduler dispatch receipt is not a verdict or completed work. |

## Event boundary proposal

Prefer a supported native Slack trigger if it proves the source contract. Otherwise propose a small separately authorized bridge. It authenticates Slack delivery, normalizes only allowed event fields, records durable intake and wakes the two fixed T3 endpoints. It does not classify reports, post verdicts, choose repositories or execute commands. Keep Slack request signing, Slack API credentials and T3 sender keys distinct and private.

Slack signs `v0:<timestamp>:<raw body>` and checks request age; T3's tested verifier signs raw body bytes with a configurable header/prefix. Thus changing T3's header to `X-Slack-Signature` alone cannot make it a Slack receiver. This is an inference from [Slack's signing contract](https://docs.slack.dev/authentication/verifying-requests-from-slack/) and the [inspected T3 verifier](../evaluations/bot-ui-transport/README.md#runtime-evidence). A bridge must validate Slack first, then create a separately signed T3 request; never disable verification to connect them.

The [Slack Events API](https://docs.slack.dev/apis/events-api/#responding-to-events) expects a prompt 2xx acknowledgement and can redeliver events. Persist authenticated intake before acknowledging, keep event identity and per-stage dispatch/effect records, and decouple that acknowledgement from agent work. Slack's `event_id` can deduplicate transport; immutable workspace/channel/root coordinates identify the report across different deliveries. Claims, external-write receipts and ambiguous-result reconciliation need their own tested design. The bot UI journal is specific to one PR-status observation and must not be reused as if it implemented issue compensation or Slack posting transactions.

The pinned templates emit `message_ts`, while both operational procedures fall back to `trigger.ts`. This is a source inconsistency, not proof of a live bug. Choose a canonical normalized `ts`, preserve timestamps as strings, and verify it with fixtures plus real connector envelopes before deployment. Reject missing/conflicting coordinates. For the configured root-message trigger, replies, edits, deletion events and bot echoes must not start new report workflows. Never infer the root from whichever reply was read most recently. Require the configured workspace/channel and read back the actual root before any product write.

## Implementation units and acceptance gates

1. **Dormant pack and setup fixtures.** Preserve the 12-file structure and full procedures, translate runtime references, verify discovery exclusion and conflict-preserving copy with user-owned maps untouched. Prove dependency access from a fresh target checkout. Synthetic data only; no schedules or integrations enabled.
2. **Event and adapter contracts.** Test authentication/normalization, missing or mismatched roots, duplicate and concurrent events, lost responses, tracker duplicate/update behavior and compensation. Prove zero Slack/tracker writes on failed preflight. Keep the event bridge separate from the two agent procedures. No real service is implied by fixture success.
3. **Explicit triage pilot.** User selects repository, test workspace/channel, tracker, triage identity, dependency provisioning and model choices. Prepare the exact temporary resources, bounded writes and cleanup for approval. Verify one thread-only verdict, duplicate suppression, known/possible/new bug branches, failed-handoff compensation and owned teardown. Do not enable normal traffic yet.
4. **Reproduction pilot.** Select the safe app and feature map, prove all control capabilities and isolated media review. Test trusted versus spoofed markers, human ownership, baseline twice/patched twice, existing-fix no-edit behavior, failed/inconclusive outcomes and the rejection window. A bounded fix may open only an explicitly authorized draft PR after every gate. Complete all seven upstream thread-safety checks before normal operation.

Required failure cases include an inaccessible/deleted parent, reply/root confusion, an unrelated operations thread, an untrusted marker author, conflicting markers, a marker timeout, an unreadable attachment, missing compensation, ambiguous external-write outcomes and a worker with Slack write capability. Preserve evidence and report incomplete; do not retry at the channel root or manufacture a replacement thread. A duplicate event cannot create another verdict, issue or competing fix merely because the earlier run's acknowledgement is missing.

## Recommendation and decision boundary

The dormant pack and local copy/discovery fixtures are available. Next test the event and adapter contracts with synthetic inputs, keeping all live integrations disabled. Fresh-provider dependency resolution remains required before a live pilot. The remaining runtime gaps should be visible tests and dependencies, not removed source requirements.

Before live implementation, the user must choose the target repository, source/test channel, tracker, app-control environment, four stage model selections and credential/trigger provisioning. Reuse established choices where they apply and ask only for missing scope. Existing authorizations in another workflow do not select these resources. If Slack intake or worker isolation cannot be established, leave Benny unsupported and continue the independent provider/distribution checks. No project, connector or model is selected by this design PR, and merging it does not enable automation.

Design validation: reconciled all 12 source paths, checked the eight setup, ten triage and fifteen reproduction step counts, inspected all templates/references, and checked local links and current documentation consistency. That design-only review changed no operational code and ran no live integration. The later dormant-pack evaluation records implementation validation separately.
