# Reflect edit destinations

On 2026-10-25, five application scenarios exercised the new Apply guard. All produced the expected result. This is a bounded authoring check, not a complete Reflect run or an installation/publication test.

## Change and source comparison

The previous Apply section checked authority and drift but did not distinguish cached skills from editable source. The update adopts the cache guard added in `pstack/skills/reflect/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`. It stays between Backlog filing and approved routing. The [adaptation record](../../adaptations/reflect.md#cache-destination-update-2026-10-25) explains the provider-portable destinations and preservation of explicit source-edit/publication authority.

The parent compared the complete final entrypoint with that exact upstream object. All other differences remain those recorded for the existing T3 adaptation. The four upstream templates are unchanged since the original restoration pin, and no local template or execution contract changed. The distributed license matches `pstack/LICENSE` at the new comparison revision. Original adoption pins and the reviewed checkpoint remain unchanged.

## Method and results

Two fresh T3-owned Codex `gpt-6.1-sol` consumers inherited the parent selection, `reasoningEffort: high` and `serviceTier: priority`, after a live capability check. Both dispatch receipts matched. Consumer A handled copy, conflict and symlink scenarios; B handled assessment and source scenarios. Each received the frozen full skill and raw requests, without expected answers, and executed only Apply/Summarize with an already supplied synthesis. No reflection reviewers or synthesizer were dispatched.

| Scenario | Directly checked outcome |
| --- | --- |
| Assessment only | Proposed a concrete project-owned destination. No package copy or edit. |
| Approved copy | Copied all four package files, then made exactly the requested sentence replacement. Reference, script and license bytes remained identical, including the script's executable mode. No repeated approval request. |
| Existing destination | Reported application incomplete because the custom skill lacked the sentence to replace and replacement authority was withheld. Custom skill and notes stayed unchanged; no partial copy. |
| Symlink into cache | Identified the resolved cache path, left the link and package intact, and proposed an alternative without creating it. Application remained incomplete pending destination authorization. |
| Authorized source | Edited exactly one source sentence and prepared a local PR description. Support files stayed unchanged. It did not redirect the edit to an installed copy or claim publication. |

The parent read every complete response and PR draft, compared original fixture bytes, modes and link targets with the baseline, checked the complete copied file set, and rejected unexpected fixture outputs. Only the authorized source entrypoint changed among pre-existing files. All cache packages and conflicting destination files stayed intact. Both tasks were terminal `completed`, `result_available`, with no pending child runs when checked through `task_status`.

Consumer client request IDs were `jstack-reflect-destination-a-20261025-r1` and `jstack-reflect-destination-b-20261025-r1`, owned by conversation `5f7384b2-cbbe-431f-942d-929f327635a1`. Routine outputs and snapshots stayed in task-owned cache. The small [case packet](cases.json) is the retained replay input.

## Replay and checks

For a replay, create a fresh disposable directory for each `scenarios` entry in `cases.json`. Write the `package` map beneath its `target`, or beneath `symlinkTo` and create the specified target link. Give `scripts/check.py` mode `0755`. Write any `existing` map beneath `destination`. Supply the entry's request, common lesson and complete Reflect skill to an independent consumer, scoped to that scenario. Start at Apply with the supplied synthesis; do not run earlier reflection phases. Compare files, modes, links and reported destinations before and after. Permission from one scenario does not carry to another. No real installation or GitHub operation is needed.

Repository verification passed:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s scripts/jstack -p 'test_skill_packaging.py'
node --test scripts/jstack/test_check_docs.mjs
node scripts/jstack/check_docs.mjs
python3 -B /home/ubuntu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/jstack/jstack-reflect
git diff --check
```

The packaging suite passed 4 tests, the documentation suite passed 20, current documentation reported 0 problems, and the skill validator passed. The upstream manifest loader also passed schema and applied-commit ancestry checks against refreshed `origin/main`, including Sharpen PR #139's verified merge.

The consumers could not perform upstream comparison or find a skill validator within their deliberately restricted fixture scope. The parent performed both checks on the actual changed skill. No real installed package, model configuration or schedule changed. Live source publication, installer-managed discovery, cross-provider behavior and the earlier Reflect assessment/delegation phases remain outside this check. The scenarios share two consumer contexts and establish no reliability rate.
