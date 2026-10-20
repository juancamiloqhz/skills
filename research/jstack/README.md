# Jstack research

Current jstack skill identities use the `jstack-` prefix. See the [name mapping and manual migration guide](skill-names.md). Earlier assessments and evaluation artifacts retain their original names; current local links point to the renamed packages.

For jstack implementation and maintenance, follow the [upstream-fidelity policy](upstream-fidelity.md). Preserve upstream structure by default and document only necessary or explicitly approved deviations.

Jstack is a portable skills bundle developed for T3 Code as a close adaptation of pstack. This directory holds decisions, source comparisons, evaluation evidence and the complete upstream inventory with a proposed backlog. The recorded delivery target remains the 23 playbooks and their dependencies; the audit does not expand that target or approve implementation.

## Current status

As of 2026-10-20, the current jstack tree ships 57 packages and all 23 Juan-mode playbook procedures, with bounded evaluations. These include 54 pstack skill mappings and three Cursor team-kit helpers. After manual reinstallation, all 57 Orbit packages match the repository. A fresh Codex/T3 conversation exercised Help, Investigation, configured delegation, later-task activation and opt-out acknowledgement; see the [catalog and runtime evidence](evaluations/catalog-discovery/README.md). The earlier 45-package omarchy-mac result remains user-reported; its current installation has not been checked here. Full provider and persistence release verification remains open.

The [complete coverage audit](coverage-audits/2026-10-18/README.md) found 12 unported top-level pstack skills plus external Unslop, three missing Benny automation procedures, incomplete guide/distribution coverage, and upstream changes in 22 existing mapped packages. It accounts for all 171 pstack source files and the related adapter/integration files, with recommendations and verification scopes. Bro and Ketchup are now implemented under the [2026-10-19 adoption decision](decisions.md#bro-and-ketchup-adoption-2026-10-19), and In your own words and Sharpen merged in PR #99 under the [task-framing decision](decisions.md#goal-restatement-and-task-framing-2026-10-19). [Blast radius](evaluations/blast-radius/README.md) merged in PR #100. [Teach](evaluations/teach/README.md) merged in PR #101. [Correct](evaluations/correct/README.md) merged in PR #102. The [formal verification generator](evaluations/formal-verification/README.md) merged in PR #103. [Recall](evaluations/recall/README.md) merged in PR #104. [Automate me](evaluations/automate-me/README.md) merged in PR #105. [Juan help and the full guide](evaluations/help/README.md) merged in PR #106, leaving Make bot UI unported, plus external Unslop. The [Make bot UI design](integrations/make-bot-ui.md) merged in PR #107. Its [transport foundation](evaluations/bot-ui-transport/README.md) merged in PR #108 and tests the sender and local key setup against one installed verifier. The [local page and recovery journal](evaluations/bot-ui-local/README.md) merged in PR #109 with fixture and browser evidence. The [live pilot results](evaluations/bot-ui-live-pilot/results.md) establish one real receiving result; a source-backed receipt correction distinguishes recording from acceptance, while live verification and recovery evidence remain incomplete after a rolled-back recovery turn. The [second live pilot](evaluations/bot-ui-recovery-pilot/results.md) verified corrected receipts, failed-request draining, saved-result redisplay and server restart. Both temporary services were removed. The [private HTTPS pilot](evaluations/bot-ui-tailnet-readiness/README.md) additionally verified the page, a user-confirmed laptop click and targeted cleanup. [Make bot UI packaging](evaluations/make-bot-ui/README.md) now ships the standalone entrypoint and its tested PR-status helper. Actual rollback, the direct HTTP/IP deployment variant and general custom actions remain outside that evidence. Benny automation, distribution integrations and provider/persistence verification remain open. All 23 procedures being present does not mean all of pstack is current or supported.

The [current fidelity status](fidelity-status.md) preserves earlier correction and runtime evidence. The [Orchestrate release assessment](evaluations/orchestrate-release/README.md) adds the landed pilot and bounded service recovery. Existing model configuration, portable names, manual installation and explicit merge authority remain unchanged. Upstream maintenance continues separately; this audit does not advance its reviewed checkpoint.

## Read by purpose

- [Investigation write boundary and Claude trial](evaluations/investigation-write-boundary/README.md): configured Claude-to-Codex execution, observed failures and explicit incomplete handling when all file writes are forbidden.
- [Complete catalog discovery](evaluations/catalog-discovery/README.md): all current identities pass a real Skills CLI listing; the refreshed Orbit installation matches, with bounded fresh-Codex workflow evidence and wider provider checks still open.
- [Make bot UI design](integrations/make-bot-ui.md): proposed T3 integration, source differences and required live evidence.
- [User guide](../../skills/jstack/jstack-juan-help/docs/guide/README.md): setup, workflow examples and choosing a skill.
- [Decisions](decisions.md): agreed names, delivery approach, and existing configuration boundaries.
- [Complete coverage audit](coverage-audits/2026-10-18/README.md): full upstream inventory, missing components, newer changes, proposed implementation order and decision gates.
- [Current fidelity status](fidelity-status.md): merged correction evidence and remaining prerequisites.
- [Benny integration design](integrations/benny.md), [inactive pack evaluation](evaluations/benny-dormant-pack/README.md) and [event/adapter contracts](evaluations/benny-event-contracts/README.md): complete procedures, copy/discovery checks and synthetic failure tests. Real integration and runtime gates remain open. No live automation.
- [Roadmap](roadmap.md): completed work and proposed next steps, with completion checks.
- [Sources](sources.md): pinned references and attribution carried forward from existing work.
- [Juan-mode adaptation](juan-mode-adaptation.md): source assessment, T3 Code integration constraints and design proposals.
- [Juan-mode specification](juan-mode-spec.md): accepted scope and activation behavior, complete playbook inventories, proposed packaging, execution contracts and release checks.
- [Upstream maintenance](upstream-maintenance.md): run a pstack change check, review its impact, or implement an approved recommendation. The [first review](upstream-reviews/2026-10-11.md) records the live trial; the roadmap records the completed scheduling handoff.

## Open questions

Conversation activation until explicit opt-out is the accepted behavior. Implementation must prove it across compaction and resume, verify delegated workspace isolation and merge continuation, and establish which runtime evidence supports workflow evaluation. The specification distinguishes proposed implementation choices from measured support.

## Earlier experiment

The old pstack review prototype, evaluation receipts, and broad portability audit are excluded from the current tree. They remain recoverable in [the earlier PR #4 commit](https://github.com/juancamiloqhz/skills/commit/28be989). They are historical material, not the active jstack plan or evidence that a jstack workflow works.

The [roadmap](roadmap.md), [adaptation records](adaptations/README.md) and dated evaluations retain the earlier implementation history. Their historical pending counts are not current availability statements.
