---
name: arena
description: "Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
---

# Arena

Open a task plan with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

Direct invocation is task-scoped and leaves juan-mode activation unchanged. A calling playbook supplies the artifact, source scope, selected configuration and return boundary. Design-only callers receive a design package without implementation. Establish permitted actions, owned outputs and observable acceptance checks from the request. Read [configuration and execution](references/execution.md) before dispatch.

Discover the named **principle-*** skills through the current catalog or explicitly supplied authoring paths and read them at their decision points below. Resolve their resources relative to the discovered package. A missing required dependency makes the affected phase incomplete; provide the manual command `npx skills add juancamiloqhz/skills --skill NAME` rather than installing or replacing its procedure.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Resolve `arena runners` through setup-jstack, or `architect runners` when the caller explicitly selects that panel. Preserve all configured seats in order, including duplicates and inheritance; require at least two configured candidates to start. Inherited seats omit the dispatch target and retain the parent's model and effort. Keep model choices and counts fixed unless the user requests a configuration change; no default-model substitution or automatic fan-out expansion. Resolve the cross-judge pool and check that an eligible judge exists before spending candidate work. Prefer a different family from the parent's; disclose same-family or inherited judging. If the caller requires diversity and it cannot be established, stop incomplete.
4. Give each candidate its own output location (a git worktree where possible, otherwise `/tmp/arena-<slug>/candidate-<n>/`), per the **principle-separate-before-serializing-shared-state** principle skill. For a child needing a separate checkout, use T3 `delegate_task` with `isolation: "worktree"`; it starts from the parent local commit and does not copy uncommitted edits. For design or text, use separate owned temporary directories. Preserve unrelated work. A prompt path alone does not change app workspace binding.

## Phase B: Fan out

Dispatch all N candidates asynchronously when capacity and demonstrated path ownership permit, using the native or T3 transport described in the execution reference. Keep writers serial until explicit-path behavior is established. Each receives the same task, the path to shared grounding, its own output path, selected absolute configuration, permitted actions and completion condition, and instructions to produce the artifact and a short rationale naming the alternatives it considered and what it rejected. Use fresh task context; candidates must not receive other candidates, the rubric, judge notes or the coordinator's preferred answer. If the transport cannot provide that isolation, report the gap before dispatch.

Wait for every candidate and its nested work to finish, inspect actual outputs and freeze the artifacts before judging. If a candidate produces no output, proceed with N-1 and note the dropout. With one viable survivor, ordinary Arena can judge, verify and return that artifact, explicitly stating that no multi-candidate comparison was possible. With none, return incomplete. A caller requiring two viable or structurally distinct candidates, including Architect, remains incomplete when its requirement fails. Do not invent replacement seats or silently retry on another model.

## Phase C: Cross-judge

After all Phase B candidates complete, revalidate the selected configuration and current catalog, then choose one eligible model from the configured `arena cross-judge pool`. Prefer a different model family from the parent's. Spawn one read-only judge subagent on that model. It sees the rubric and the candidates by path label, scores each criterion, and recommends a base with rationale. Keep provider/model identity mappings in the coordinator's record; labels do not guarantee that artifact style cannot reveal authorship. The judge does not edit or synthesize. It runs in parallel with your reading in Phase D. Don't spawn it while candidates are still writing.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the **principle-laziness-protocol** principle skill. Honor any caller requirement for structurally distinct candidates before accepting a base.

## Phase E: Graft

Keep original candidates intact; synthesize in a separately owned destination. The coordinator performs synthesis unless the calling workflow supplies an already authorized synthesis role.

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **principle-redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and return the consensus shape within the task's delivery authority. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

Reframing uses fresh tasks with the corrected common brief and the same selected panel. Do not rerun unchanged work indefinitely when progress requires new information or authority. Design-only scope and explicit caller checkpoints remain in force; selecting a candidate does not authorize implementation, installation, PRs or merges.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **principle-prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

Execute the original acceptance checks in the correct checkout when authorized. For design artifacts, trace caller usage, ownership and failure paths against the grounded source. Distinguish inspection from executed behavior; an unavailable prerequisite is incomplete verification.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.

Retain the per-criterion comparison, disagreements, task IDs and artifacts needed to review the result. Reconcile owned writes and terminal child state before claiming completion; remove owned temporary catalogs. Return at the caller's requested boundary, disclosing failed diversity, dropout or verification requirements.
