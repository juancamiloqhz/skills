# Recall evaluation

Source: `pstack/skills/recall/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. Local: [jstack-recall](../../../../skills/jstack/jstack-recall/SKILL.md). [Adaptation record](../../adaptations/recall.md).

Recall reconstructs context across recent project conversations, checks current state and named-target shared records, then returns a brief and one next move. It does not resume implementation. The six source steps, findings schema, output contract and explicit invocation remain intact.

## Controlled history exercise

The [fixture interface](history_fixture.py) returns synthetic history, forge state and completed investigator findings. [Cases](cases.json) retain the prompts and expected behavior. This is an agent exercise over executable controlled responses, not a test of a production history adapter or live Why delegation.

The primary case asks for recent lease-ownership context as of 2026-10-19 12:00 UTC. Two metadata pages include the current chat, an evaluation chat, another workspace, an old chat, a settled eligible chat, and a newer eligible chat whose title does not mention leases. The first page ends with an old row even though the second contains newer candidates. The settled chat claims PR #11 fixed ownership; the newer chat and current-state response show #12 reverted it and #13 remains open. A second timeline page and text continuation reveal that a claimed passing check actually exited 2 because the verifier was missing. Shared findings include an unresolved user report and explicit source gaps.

Fresh native authoring evaluators inherited the parent GPT-6-astra/high runtime. One used the supplied authoring skill; one used the same task and interface without Recall. Neither used real history, external apps, saved model roles or child investigators. All reports and call logs stayed in owned cache. The parent read the reports and audited the operation logs.

| Observation | With Recall, initial | Without Recall |
| --- | --- | --- |
| Read both list pages and both eligible chats | Yes | Yes |
| Avoid reading current, other-workspace, test and old chats | Yes | Attempted old and test chat reads; fixture rejected them |
| Recover timeline page and truncated result | Yes | Yes |
| Correct stale merge and verification claims | Yes | Yes |
| Preserve shared-source gaps and supplied-evidence limits | Yes | Yes |
| Read eligible chats newest first | No | No |
| Use the source's tagged brief | Yes | Free-form prose |

The first Recall run said it sorted by update time but read the older chat first. The skill now explicitly applies newest-first order to inline reads as well as delegated slices. A fresh evaluator then read `zzz-newer` before `aaa-older`, recovered position 17 and offset 240, excluded all four disallowed chat contents, and retained the correct reverted/open statuses and verification gap. Its final brief kept the source tags and one proposed next move. The parent checked both the brief and actual call order. The initial failure remains part of the evidence. One pair cannot establish general accuracy or performance improvement; both versions correctly identified the unresolved issue.

The supplied-capsule case called only `state` and `shared`, skipping history mining. It retained the revert, open PR, unrun checks and source gaps, with no next-step execution. Five supplied-evidence boundary cases kept incomplete all-history coverage, refused model substitution when a role was unavailable, did not promote a summarized test claim to verified success, routed one-session resumption to Session pickup, and disclosed unavailable Automate me. These boundary responses are hypothetical, not executed failure-path integrations.

## Live tool inspection and limits

The live T3 list/read/search schemas were inspected. A project-scoped `t3_thread_list` with `includeSubagents: false` returned only the current parent conversation, which Recall excludes. No other real conversation was read. This confirms only metadata discovery for this environment, not multi-chat mining.

List metadata does not promise a workspace path. The live read API rejects `limit: 0` and `runLimit: 0` with `Expected a value greater than or equal to 1`, so a metadata-only read cannot be assumed. The skill requires established workspace identity and reports a gap when tools cannot establish it without reading an unscoped conversation; a supplied binding or workspace export can fill that gap. The controlled fixture supplies explicit workspace identities. Live multi-workspace recovery remains unverified.

The search API is active-only, bounded and has no exhaustive-result guarantee. The skill therefore preserves list pagination and eligible-content search instead of treating search results as all history. T3 activity is summarized; full execution evidence may remain unavailable. No real chat-reader fan-out, configured-role dispatch, cross-provider run, full tool-transcript retrieval, installed discovery or production current-state verification was tested here. Existing Why and Session pickup evidence remains separate.

## Reproduce

Give a fresh agent case 1 from `cases.json`, the absolute Recall authoring path, and this controlled interface. For the baseline, omit the skill path and forbid reading Recall. Permit only assigned scratch writes and the fixture operations; do not let either evaluator read fixture source or expected assertions. Treat `shared` as supplied completed investigator findings, not permission to launch real searches.

```sh
run_dir=$(mktemp -d)
python3 research/jstack/evaluations/recall/history_fixture.py "$run_dir/calls.jsonl" list
# Available operations: list [cursor], read ID [position [offset]], state, shared.
```

Audit call logs for both list pages, eligible read IDs only, newest-first reading, position 17 and continuation offset 240. Inspect the answer for reverted #11, open #13, missing verifier, unresolved LEASE-8, explicit coverage limits, citations and one proposed next move. For case 2, expect no list/read operations. Case 3 is a supplied-evidence assessment only. Agent wording is nondeterministic; the fixture responses are deterministic.

Retain only this report, prompts and the small fixture program. Raw reports and access logs remain under `/home/ubuntu/.cache/jstack/recall-20261019/` for the pending review. They are not durable documentation links or installed skill contents.

## Validation and source comparison

Four packaging tests passed. `node scripts/jstack/check_docs.mjs` reported 54 skills, 30 commands, 24 principles, 23 playbooks and zero problems; guide coverage remains pending. Manifest loading passed, and a parsed comparison confirms that existing mappings, review decisions and the reviewed checkpoint are unchanged. New research links resolve. Source comparison verified all headings, six step labels, output bullets and the exact license; the full diff was reviewed against the adaptation record.

The generic Codex validator rejects the source's retained `disable-model-invocation` field. A temporary copy omitting only that field passed its remaining checks. The shipped source flag and Codex `allow_implicit_invocation: false` metadata remain. This is qualified packaging validation, not proof of installed host discovery.

## Use after merge and manual installation

`$jstack-recall Catch me up on my lease ownership work from the last seven days.`

The answer should explain what still holds, which attempted fix was reverted, what remains open, and the next useful action. A supplied handoff avoids repeated history mining. Missing history or dependencies yield a partial brief rather than invented completion.
