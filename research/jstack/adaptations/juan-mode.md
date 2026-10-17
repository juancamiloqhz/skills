# Juan-mode adaptation

The [2026-10-15 naming decision](../skill-names.md) additionally changes this package's local identity and callers. Its upstream identity, procedure and revision pin remain as recorded below.

Adapted from [poteto-mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md) at `11713c683fe4add4fd403ea880580abbc9e0875f`. The 2026-10-14 entrypoint restoration follows the [fidelity policy](../upstream-fidelity.md). [Comparison and evaluation](../evaluations/mode-restoration/README.md) distinguish restored instructions, runtime substitutions and pending implementation. The pin and reviewed checkpoint remain unchanged.

## Current playbook coverage

Investigation, Prototype, Trace forensics, Authoring or modifying a skill, Runtime forensics, Bug fix, Feature, Refactoring, Perf issue, Hillclimb and Eval are now implemented; 12 routes remain pending. The [Runtime forensics adaptation](runtime-forensics.md) and [evaluation](../evaluations/runtime-forensics/README.md) cover live capture, temporary instrumentation and restoration. The [authoring adaptation](authoring-a-skill.md) and [evaluation](../evaluations/authoring-a-skill/README.md) cover host authoring guidance, package validation and local delivery. The [Trace adaptation](trace-forensics.md) and [evaluation](../evaluations/trace-forensics/README.md) cover its source, configured reduction and fixed-artifact limits. See the [Prototype adaptation](prototype.md) and [evaluation](../evaluations/prototype-playbook/README.md) for its full procedure and later availability changes. The [Investigation adaptation](investigation.md) and [evaluation](../evaluations/investigation-playbook/README.md) account for its full source, three availability-paragraph changes and unchanged mode support files. The restoration tables below describe the earlier baseline; their statements that all procedures were pending are historical. Later benchmark, writing and No-comments ports also supersede the helper-gap statements. Source pins and the reviewed checkpoint remain unchanged.

## File accounting

| Source | Local disposition |
| --- | --- |
| `pstack/skills/poteto-mode/SKILL.md` | `skills/jstack/jstack-juan-mode/SKILL.md`. Restore Non-negotiables, Principles, Autonomy, Subagents, Writing the reply, Comments and Playbooks in the original order. The 23 inline route entries retain their source order and examples. Differences below. |
| `pstack/skills/poteto-mode/references/bugbot-triage.md` | Same relative reference under juan-mode. Restore the complete rubric and all learned patterns. Add only a pending-Babysit and task-authority qualification in the introduction. |
| `pstack/agents/poteto-agent.md` | Context dependency. Its full-mode and applicable-leaf reads become explicit ordinary-child brief instructions in Subagents and `references/execution.md`; no unsupported Cursor wrapper is packaged. |
| Remaining 43 files under upstream mode | Pending procedures or tooling, including all 23 playbooks. The comparison inventories their paths and hashes. This PR does not port or certify their algorithms. The [foundation audit](../fidelity-audits/2026-10-13/foundation.md) retains the detailed backlog. |
| `pstack/LICENSE` | Distributed juan-mode LICENSE remains byte-identical, including Lauren Tan's copyright. |

The previous jstack `references/routes.md` summary is removed; the original inline list owns routing again. Jstack's five support files remain: activation, configuration and execution references, preflight helper and its tests. Preflight code, tests and configuration reference are unchanged. Historical evaluations still describe their original files and tool capabilities.

## Entry-point differences

| Section | Difference and concrete reason | Verification or remaining limit |
| --- | --- | --- |
| Frontmatter and introduction | Rename Poteto to Juan-mode and describe explicit activation until opt-out. Omit Cursor's mode/icon/color/reminder metadata and manual-invocation flag. Reading for authoring or a child brief does not activate persistent state. | Until-opt-out is the [user's recorded requirement](../decisions.md#names-and-scope). Active continuation/catalog use needs the existing shared-package [invocation exception](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata); it does not reproduce upstream explicit-only metadata. Live cross-provider discovery, compaction and restart remain unverified. |
| Availability | Identify the 23 missing procedures and required helper gaps before execution; continue independent authorized work without inventing workflow support. | Restores triggers without falsely enabling absent code. Routing exercises inspect these disclosures; no playbook is marked implemented. |
| Non-negotiables | Restore every source trigger, empirical-question classification, throughput checkpoint requirement, helper selection, surface proof, benchmark gate and long-work decision trail. Replace Cursor `AskQuestion` and built-in `create-skill` with the host question mechanism and available skill-creator package. | The missing Prototype/Feature/Bug-fix procedures remain explicit. Their absence does not justify asking the user to decide an observable fact. |
| Helper discovery | Use catalog or explicit authoring paths, verify intended package identity and preserve selected config/task boundaries. Restore no-comments as a required gate instead of replacing it with generic review. | Technical-writing, no-comments and benchmark-checklist are not packaged yet; Deslop/control helpers are external. Missing gates remain incomplete. A project verifier is useful evidence, not proof of equivalent external control tooling. Manual install commands apply only to actual jstack packages. |
| PR triggers and Bugbot | Preserve Babysit status routing and Shipping's independently verified contiguous run. Use parent-owned T3 watches/wakes instead of polling/phase-agent `drive`. Restore the whole triage reference, with external replies/resolution conditional on user authority. | Actual `watch_pull_request` semantics are a host substitution, not evidence that missing readiness-classification tools exist. This correction performs no Bugbot replies or resolutions. |
| Broken-skill repair and Autonomy | Isolate a broken skill's repair, but create/publish its PR only within existing authority. Keep reversible in-scope autonomy, explicit user checkpoints and candor. Omit source's blanket team-chat/ticket authority; merge/install/scheduling remain separate. | Developer/user task boundaries override upstream's broader external-action grant. No extra approval is needed for already authorized work. |
| Principles | Keep all five inline groups, 24 summaries and full-leaf requirement from the previously restored version. Retain jstack catalog identity, manual installation and scoped-leaf qualification. | All 24 leaf bodies are separately maintained; this correction changes none. Principle decisions are named only after reading their leaves. |
| Subagents | Replace Cursor `Task`/wrapper/default-model mechanics with canonical jstack preflight, configured roles, inherited null targets and supported native/T3 tools. Ordinary children read the full style; specialized helpers keep their own briefs. Restore freshness for all new work, not just reviews. | No paid fallback or changed settings. Same-model contexts are not family diversity. Fresh ordinary-child evaluations cover actual fixture execution; separate worktree execution remains untested by this PR. |
| Reply and Comments | Restore the full source sections. Add accurate incomplete/paused/cancelled reporting and persistence-after-completion reminder. | Bounded child reports retain actual proof, limits and principle choices; no claim of full playbook replies. |
| Playbooks | Restore verbatim step copying and visible skipped steps for available procedures. Restore Figure-it-out priority for large/cross-cutting/unattended tasks even when a narrower playbook fits; standing programs still route to Orchestrate. Preserve planning-only and user checkpoints. Rename provider-restart example and gate Opening a PR on publication authority. | Missing narrower procedures alone do not justify a custom fallback. All procedures remain pending, so live todo copying from an implemented playbook is not tested. |

## Execution and activation references

`references/activation.md` now distinguishes the ordinary child's required full-style read from persistent mode activation and bounded authority. Other activation semantics are unchanged. `references/execution.md` adds that read to the brief, extends default freshness to new work/fixes/retries/queue items, and retains the stronger T3 rule that every delegated review round is fresh. A non-review reuse exception names expensive live state; stop/hold messages are not new work.

The old claim that T3 `delegate_task` has no workspace-binding option is obsolete. The current callable tool and injected host contract provide `isolation: "worktree"`. A child needing a separate checkout must use that option. It starts from the parent's local commit, completes project setup and does not copy uncommitted edits. Prompt paths and manual `git worktree add` are not substitutes for app binding. Shared checkouts remain suitable for bounded reads or serial writes; parallel writes still require ownership and demonstrated tool behavior. This is a current-tool contract correction, not a new all-provider isolation claim.

The manifest now watches `pstack/agents/poteto-agent.md` as context. Setup, Arena and Swarm remain the next scopes in fidelity group 7. Their unresolved defaults, validation and race choices are not changed here. This is not an official Cursor, pstack or T3 Code integration.

## Control CLI dependency

The matching-control trigger now discovers standalone `jstack-control-cli` for terminal apps while retaining external Control UI. The dependency paragraph distinguishes those packages. [Control CLI adaptation and caller comparison](control-cli.md) cover both changes; all route procedures and availability counts remain unchanged.

## Deslop dependency

The pre-commit trigger now discovers standalone `jstack-deslop` instead of the external Cursor plugin name. The dependency paragraph keeps Control UI external and identifies both shipped helpers. [Deslop adaptation and caller comparison](deslop.md) cover the two caller changes; all five procedures and the 18 pending routes remain unchanged. This supersedes the earlier table's external Deslop disposition.

## Bug fix availability

[Bug fix](bug-fix.md) is the sixth procedure. Availability lists and setup now agree on six available and 17 pending. The helper list adds `jstack-tdd`, and the dependency paragraph no longer labels Bug fix's reproduction exception unavailable. Runtime and Trace forensics may hand an authorized fix to this procedure; Perf issue remains pending. The manifest adds TDD and Sequence Work into Verifiable Units as caller context. No other route trigger or helper algorithm changes.

## Feature availability

The Feature procedure and its shared four-part throughput checkpoint are now available. Feature brought coverage to seven playbooks with 16 pending. Configured Architect and Arena panels retain their required counts; existing settings are not expanded. The [Feature adaptation](feature.md) and [evaluation](../evaluations/feature/README.md) record source comparison, isolated two-seat execution, the one-seat limitation and remaining publication dependency.

## Refactoring procedure

The [Refactoring adaptation](refactoring.md) adds the eighth available procedure, with 15 pending. Mode availability links now include it; routing triggers and the shared Feature checkpoint remain unchanged. See the [source comparison and evaluation](../evaluations/refactoring/README.md).

## Perf issue procedure

The [Perf issue adaptation](perf-issue.md) adds the ninth procedure, leaving 14 pending. The availability paragraphs add its existing route. Runtime forensics and Trace forensics may now hand an authorized fix to Perf issue. No helper algorithm, model role, watch or source pin changes. See the [source comparison and evaluation](../evaluations/perf-issue/README.md).

## Hillclimb procedure

The [Hillclimb adaptation](hillclimb.md) adds the tenth procedure, leaving 13 pending. The two availability paragraphs add its existing route. Its per-attempt data uses the shared trail format, and the manifest adds direct context for Show me your work and Build the Lever. Other routes and helper algorithms remain unchanged. See the [comparison and bounded evaluation](../evaluations/hillclimb/README.md).

## Eval procedure

The [Eval adaptation](eval.md) adds the eleventh procedure, leaving 12 pending. It preserves all seven steps and the source blinding rules, using configured model diversity and scoped run evidence. Its specialized child briefs keep orchestration metadata private. Other routes and helper algorithms remain unchanged. See the [bounded evaluation](../evaluations/eval/README.md).

## Control UI dependency

The UI trigger now discovers standalone `jstack-control-ui`, and the dependency paragraph lists both shipped control helpers. The [Control UI adaptation](control-ui.md) accounts for these two caller changes and the full helper source. No playbook route or existing procedure changes; Visual parity remains pending.

## Visual parity coverage

The [Visual parity adaptation](visual-parity.md) adds the twelfth procedure, leaving eleven pending. Availability paragraphs now list it; route triggers, existing procedures, setup defaults and model resolution remain unchanged. The [evaluation](../evaluations/visual-parity/README.md) records exact screenshot comparisons and explicit missing-baseline behavior.

## Opening a PR coverage

[Opening a PR](opening-a-pr.md) adds the thirteenth procedure, leaving ten pending. Availability paragraphs and seven existing callers now reach it; original caller algorithms, roles and setup behavior remain unchanged. Publication authority remains separate from local preparation, monitoring and merging. See the [evaluation](../evaluations/opening-a-pr/README.md).

## Babysit availability

The mode now bundles Babysit and its single-pass watcher, bringing the current count to 14 available procedures and nine pending. See the [Babysit adaptation](babysit.md) and [evaluation](../evaluations/babysit/README.md). Model roles, configuration selection and source pins are unchanged.
