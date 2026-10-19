# Benny dormant pack

Source: [`pstack/automations/benny`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/automations/benny) at `0148b78c56c72a1b8412055913c79f767095b217`. Local counterpart: [`automations/jstack/benny`](../../../automations/jstack/benny). The separate `automationPacks` mapping in `upstream.json` keeps this out of the normal skill catalog while covering pack changes, deletion and the pstack license in upstream detection. The reviewed checkpoint and existing decisions are unchanged.

The user approved the next inactive unit after the [integration design](../integrations/benny.md) in PR #116. The port preserves all 12 source files, three nested procedure names, eight setup phases, ten triage phases, fifteen reproduction phases, four references and three templates. The pstack MIT license is copied unchanged to the pack root. This is source availability with local setup evidence, not a completed live integration.

## Differences from the pin

| Local file, relative to the pack | Exact change and reason |
| --- | --- |
| `README.md` | Same setup entry and six-step lifecycle; T3 project dependencies replace Cursor plugin JSON. Adds inactive status and the tested discovery limitation. |
| `FOR_AGENTS.md` | Keeps human intent, two independent triggers, configuration list and seven copy steps. Translates paths, helper identities and host name. Replaces Cursor settings/editor handoff with verified project dependencies and reviewed T3 task creation/update by recorded ID. |
| `skills/setup-benny/SKILL.md` | Retains all eight numbered phases, separate first-time/update paths, both intent checklists and seven safety checks. Replaces unsupported Cursor plugin settings and built-in Automate with capability-gated T3 draft/review/disabled-creation/read-back. Requires actual Slack intake, fresh-checkout dependency proof, inherited model-context verification and enforced child isolation before live readiness. Model selection remains four explicit Benny choices; no global jstack role is added. |
| `skills/triage-issue-reports/SKILL.md` | Shared helper names use `jstack-`; Unslop stays external. Adds internal discovery metadata and explains that T3 isolation must cover nested helper children; coordinator fallback preserves upstream's isolation rule. All ten operational phases and tracker compensation rules remain. |
| `skills/reproduce-and-fix-issues/SKILL.md` | Same identity/metadata/isolation adaptation; configured T3 Slack actions replace Cursor actions. Independent media review remains mandatory; missing isolation produces Blocked, never confirmed repro. All fifteen phases, trusted-marker/ownership gates, twice-per-build proof and draft-only boundary remain. |
| `skills/triage-issue-reports/references/routing.example.md` | Only `.cursor` → `.agents` locations for the pack and user-owned map. |
| `skills/reproduce-and-fix-issues/references/control-adapter.md` | Only the user-owned map's pack-directory reference changes. All seven capabilities, environment-translation rules and nine setup checks remain. |
| `skills/reproduce-and-fix-issues/references/feature-map.example.md` | Only the pack and user-owned map locations change. All fictional feature examples remain. |
| `skills/reproduce-and-fix-issues/references/verify-existing-fix.md` | Byte-identical to upstream. |
| `templates/configuration.example.yaml` | Paths use `.agents`; `prefer_cursor_actions` becomes `prefer_configured_actions`. Adds explicit `slack.workspace_id` for the selected intake boundary. All other field groups, four model placeholders, markers and budgets remain. |
| Both `templates/*-automation-prompt.md` | Stable `.agents` operational paths and reviewed T3 setup replace Cursor Automate. Corrects upstream's `message_ts` to the procedures' canonical `ts`. Requires string timestamps, authenticated fixed-scope intake, conflict rejection and independent delivery to both workflows. Marks placeholders as template inputs, not native T3 webhook interpolation. No event normalizer is implemented by these templates. |

The three nested procedures retain `disable-model-invocation: true` and add `metadata.internal: true`. Cursor's plugin-root boundary does not apply to Skills CLI recursive repository scanning. The flag is the smallest supported packaging adaptation that preserves filenames and nesting. [Skills CLI's parser](https://github.com/vercel-labs/skills/blob/main/src/skills.ts) excludes internal skills by default; explicit named selection or `INSTALL_INTERNAL_SKILLS=1` opts in. The actual local Skills CLI 1.7.2 was tested with default, full-depth, wildcard and explicit opt-in discovery. This is not a guarantee for every installer/provider and is not an access-control mechanism.

The repository-only `scripts/jstack/copy_benny_pack.py` previews the whole copy and optionally creates missing files. It reports every differing managed file for manual review and writes nothing when any conflict is known. It never deletes destination-only files or overwrites a managed file. It intentionally does not perform an automatic three-way merge, provision dependencies, commit or create tasks. Only disposable fixtures were copied during this change.

## Source comparison and limits

Reviewed the final diff against all 12 pinned files. Routing, control and feature-map references are byte-identical after the documented path substitutions; existing-fix verification and LICENSE are exact copies. Inspected the changed operational instructions, setup replacement and prompts, including marker trust, human ownership, compensation, independent media review and bounded follow-up. Step counts are supporting checks, not semantic proof.

See the [reproduction commands and results](../evaluations/benny-dormant-pack/README.md). Local discovery from a fresh clone resolves the copied shared dependency entrypoints, including external Unslop and jstack-setup. A fresh provider agent, target-specific dependency provisioning, Slack/tracker behavior, child isolation, live task creation and UI reproduction remain unverified. Do not describe this pack as enabled or production-ready.

## Synthetic event and adapter contracts

The [contract evaluation](../evaluations/benny-event-contracts/README.md) adds repository-only HMAC/normalization, durable intake/claim/effect code and injected-adapter tests for the approved T3 boundary. The copied pack remains byte-for-byte unchanged from PR #117. These helpers do not replace the agent procedures or ship a live bridge. Lost responses remain incomplete with retained ownership; compensation requires the confirmed creation receipt for the exact issue owned by the run. Actual vendor behavior, dispatch, dependency loading and child isolation remain deployment gates.
