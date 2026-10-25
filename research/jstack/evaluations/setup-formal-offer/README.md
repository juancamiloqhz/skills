# Setup formal verification offer

On 2026-10-25, five post-save scenarios checked setup's new optional formal-verification offer. All produced the expected routing. Saved model configurations and all other pre-existing fixture files stayed byte-identical. Acceptance used a generator double that recorded a handoff, not a real verification run.

## Source and scope

The previous setup ended with the app-verification offer. The update adds step 8 from `pstack/skills/setup-pstack/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`, plus its matching text from `pstack/docs/guide/01-setup.md`. It keeps the once-only question, existing-skill check and independent acceptance decision. The [adaptation](../../adaptations/setup-jstack.md#formal-verification-offer-2026-10-25) explains installed dependency discovery, actual authority, manual installation and incomplete generator outcomes.

The parent inspected the complete final entrypoint and guide against those pinned source files. Existing T3 differences remain documented in the setup and Help adaptation records. A direct comparison also confirmed original steps 1-7, including all 17 inline roles, are unchanged. Only the introduction, new step 8 and closing scope statement changed in the entrypoint. Both distributed licenses match `pstack/LICENSE` at the comparison revision. The manifest adds the formal generator as setup context; original adoption pins and the reviewed checkpoint stay unchanged.

## Consumer checks

Two fresh T3-owned Codex `gpt-6.1-sol` consumers inherited `reasoningEffort: high` and `serviceTier: priority`, after a live capability check. Returned targets and options matched. Each read the complete frozen setup skill and raw scenario requests, with no expected answers. Steps 1-6 were declared complete, and only the optional offers ran. Each scenario had its own project, complete 17-role configuration and bounded generator inventory.

| Scenario | Observed outcome |
| --- | --- |
| Existing formal skill | Recognized documented model-checking support and suppressed generation. Existing app support also suppressed that offer. No verification was run or claimed. |
| Decline | Honored the explicit formal decline without repeating the question or generating files. Model setup remained complete. |
| Acceptance after app decline | Used only the formal generator double from the supplied inventory. The receipt preserved the exact project and job-ownership property. Reported draft handoff only, no generated proof or verified property. |
| Generator unavailable | App support did not suppress formal inspection. Reported the missing formal generator, provided its correct manual installation command and left the optional task incomplete. No substitute output. |
| Unanswered | Presented the formal offer once while leaving generation unstarted and model setup complete. The fixture response ended without waiting for a live reply. |

The parent read every complete response, checked the exact accepted receipt, compared all original fixture bytes and rejected unexpected output paths. Only five response files and the accepted handoff receipt were added. Both consumers were terminal `completed`, `result_available`, with no pending child work when checked through `task_status`.

Consumer client request IDs were `jstack-setup-formal-offer-a-20261025-r1` and `jstack-setup-formal-offer-b-20261025-r1`, owned by conversation `5f7384b2-cbbe-431f-942d-929f327635a1`. A handled existing/decline/unanswered; B handled acceptance/unavailable. Their routine responses and snapshots stayed in owned cache. The small [case packet](cases.json) is the retained replay input.

## Replay and validation

Create a fresh disposable root per scenario. Write `projectFiles` beneath `project/`, apply `extraFiles` and `removeFiles`, and generate a complete fixture configuration with setup's `scripts/models.py template --preset medium`. Save it as `project/.jstack/models.json`. For the available-generator scenario, write `generatorFixture` to an owned `available/jstack-create-formal-verification-skill/SKILL.md` and list that absolute path in `inventory.json`; other inventories are empty. Give a fresh consumer the full setup skill, scenario request, project root and inventory, starting after model save. Permit writes only to its response and authorized generator receipt. Compare all original bytes, output paths and reported outcomes. Do not use real global settings or installed generators.

These checks passed:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s scripts/jstack -p 'test_skill_packaging.py'
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest discover -s skills/jstack/jstack-setup/scripts -p 'test_models.py'
node --test scripts/jstack/test_check_docs.mjs
node scripts/jstack/check_docs.mjs
python3 -B /home/ubuntu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/jstack/jstack-setup
git diff --check
```

Packaging passed 4 tests, model configuration passed 19, documentation passed 20 and current docs reported 0 problems. The skill validator passed. The upstream manifest loader passed schema and applied-commit ancestry checks, including Reflect PR #140's verified merge.

This is an authoring-path offer test, not live catalog discovery, host invocation registration, first-run model setup, repeated-turn prompting or execution of the shipped formal generator. The double deliberately leaves verification incomplete. No proof, tool installation or reliability rate is established. The actual generator update, formal maintenance and Statechart adoption remain separate work. No real configuration, installation or schedule changed.
