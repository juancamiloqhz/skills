# Formal verification generator evaluation

Date: 2026-10-19. Authoring base: `4db319bdd51b41c3b3bb9916bdbbe7865df879a4`, after PR #102. Source: `pstack/skills/create-formal-verification-skill/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. See the [adaptation record](../../adaptations/create-formal-verification-skill.md).

The generator must leave a reusable project-local verifier, demonstrate that it detects a broken property in real code, and state the proof's scope. The exercised target is a synthetic lease dispatcher. No production system was verified or changed.

## Live generation

Independent with-skill and baseline agents received separate copies of the same fixture and the same request. They could generate local proof files, instructions and discovery links, run checks and mutate owned scratch copies. Product edits, installation, network access and publication were excluded. Neither agent saw the generator, expected results or the other's output. Both, and the supplied-evidence evaluator, inherited GPT-6-astra at high effort.

The fixture's important promise is exclusive lease ownership: workers A and B must never both be in phase `holding`, or they could both perform the exclusive job. An unrelated display label was not selected. The existing example test exercises only serial acquisition.

Tool discovery found Python 3.14.4 and no installed standalone verifier among the queried tools. The generated checker uses Python's standard library to explore explicit states breadth first. It imports the actual `lease.State` and calls the actual `lease.advance` for each worker at every reachable state. It does not copy the transition logic into a separate model.

| Check | Observed result |
| --- | --- |
| Unmodified protocol | Exit 0; 15 reachable states, 30 evaluated transitions including self-loops |
| Scratch copy with acquisition recheck removed | Exit 1; actual simultaneous-holder counterexample |
| Restored scratch | Exit 0; 15 states, 30 transitions; original product bytes unchanged |
| Checker through Claude link | Same passing result; all three package files resolve to canonical files |
| Existing example test | Pass |

The broken execution is four dispatcher actions: A observes a free lease; B observes it too; A acquires it; B acquires it while A still holds it. This is a property violation, not just a changed-source warning. The mutation helper removes only the `ready` branch's acquisition guard in a temporary copy, requires the specific violation, restores the original bytes and removes the temporary copy. Product code in the target repository remains untouched.

The generated package contains `SKILL.md`, `check.py` and `mutation_check.py` under `.agents/skills/verify-lease-formal/`. The relative `.claude/skills/verify-lease-formal` link points to `../../.agents/skills/verify-lease-formal`. An AGENTS.md pointer tells the next agent to revisit the proof when lease state, transition atomicity or proof tooling changes. The generated instructions explain code correspondence, commands, tool version, findings, scope changes and incomplete outcomes. No scratch paths or placeholders are embedded as required runtime locations.

The parent inspected every generated file, independently enumerated the original transition graph and replayed the retained generated patch in a fresh fixture. All results agreed. The baseline also produced a working finite-state verifier, mutation proof and linked skill; it additionally checked owner consistency. This exercise demonstrates the candidate's required behavior, not superiority over ordinary authoring or a general performance improvement.

## Exact scope and limits

The domain has at most 48 states: two workers, four phases per worker and three owner values. Only the 15 states reachable from the actual empty initial state are relevant to this property. The checker explores both worker actions from each reachable state until closure, without a schedule-depth cutoff. Each entire `advance` call is atomic and serialized, as the fixture declares. The reviewed transition is deterministic and reads only its arguments and fixed worker identities, so revisiting a state does not introduce new futures.

This is finite explicit-state model checking, not a proof-assistant certificate. It trusts the checker, Python and the reviewed state completeness/atomicity assumptions. It does not cover additional workers, repeated acquisitions, crashes, restarts, network effects, concurrent execution inside `advance`, fairness, liveness or a separate owner-consistency property. Failure traversal counts are partial, so they are not reported as the full broken graph size.

Live provider discovery and generation against a real application remain unverified. The generated mutation helper requires a passing baseline in this fixture; if current code already has a finding, it reports incomplete negative-control execution rather than hiding that finding. A complete generation run against an already-failing baseline was not exercised.

## Supplied-evidence boundary cases

The separate evaluator assessed the remaining requests in [cases.json](cases.json), without executing those hypothetical scenarios:

- A current ownership violation remains a finding with its counterexample. Verification-only authority does not permit a product fix or weaker property. Restoration returns to the original failing baseline.
- A queue-length-three checker cannot fulfill an all-queue-sizes requirement. Missing proof tools and an unrun mutation leave delivery incomplete. No installation occurs, and no link is made when no skill exists.
- A conflicting dangling Claude link is preserved. A runnable canonical verifier does not make the unresolved linking requirement complete or prove live discovery.

These checks establish bounded response behavior, not executed all-sizes proofs or a filesystem conflict exercise.

## Reproduce and retain

Environment: CPython 3.14.4 and Git 2.53.0. No dependencies need installation. From the repository root:

```bash
proof_parent=$(mktemp -d)
python3 -B research/jstack/evaluations/formal-verification/replay.py "$proof_parent/proof"
```

The replay creates a new owned repository, applies [solution.patch](solution.patch), runs the verifier and mutation helper, verifies the relative link and reruns the original test. It checks product bytes and owned mutation cleanup. The destination must not already exist. The generated repository remains for inspection and can be removed after review. Agent-generated files are intentionally uncommitted in that fixture.

For a fresh authoring exercise, use [make_fixture.py](make_fixture.py) and the first request in [cases.json](cases.json), supplying the complete candidate skill to one agent and withholding it from an independent baseline. Do not reveal expected outputs or the evaluated patch. Tool absence must stay explicit rather than triggering installation.

Retain only this report, requests, generator, evaluated generated package patch and replay script. The patch preserves the runnable verifier and instructions needed to reproduce the reported result after scratch removal. Raw agent reports, catalogs, generated repositories and routine logs stay outside Git.

## Packaging and fidelity

Final comparison preserves every source heading, seven quality requirements, code/model correspondence, mutation/restoration procedure and handoff. The adaptation record accounts for naming, authorized execution, portable output paths and the user's existing automatic-Claude-linking decision. License bytes and invocation metadata were checked. Four packaging tests, manifest validation, documentation/relative-link checks and whitespace checks pass.

The generic Codex validator rejects the source's retained `disable-model-invocation` field. A temporary copy omitting only that field passes the remaining checks; this is qualified validation, not a claim of installed-host support. Existing skill bodies, model configuration and reviewed upstream checkpoints are unchanged.

## Normal use

After merge and manual installation, ask `$jstack-create-formal-verification-skill Check that two workers cannot hold our lease at once. Leave product code unchanged.` It chooses a suitable available tool, checks the property within stated assumptions and leaves a local skill for future changes. The handoff explains the command and its limits in the project's terms.
