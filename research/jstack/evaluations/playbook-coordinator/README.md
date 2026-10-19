# Receiving-chat playbook coordination

The conversation receiving Juan-mode now explicitly owns the playbook. Ordinary children receive assigned steps or bounded subtasks. This adopts a rule identified by the [coverage audit](../../coverage-audits/2026-10-18/README.md), while preserving specialized workflow children and existing model selection.

## Source assessment

Local base is merged PR #92, `2671cb6375705ae3a854b7de7e79bd4897b2dffe`. Compared `pstack/skills/poteto-mode/SKILL.md` from original pin `11713c683fe4add4fd403ea880580abbc9e0875f` through audited revision [`0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/poteto-mode/SKILL.md). All changes to that upstream entrypoint are accounted for below.

| Source change | Local disposition |
| --- | --- |
| Rename `Poteto Mode` to `poteto-mode`; remove `mode` and `reminder` metadata | Keep the user-selected `jstack-juan-mode` identity and existing conversation-state contract. Jstack already omits unsupported Cursor metadata. Invocation-metadata behavior and provider persistence remain open verification items. |
| Add the absolute mode path to every ordinary agent prompt, using sibling skills | Already satisfied by jstack's Subagents paragraph and child-brief checklist. Keep catalog discovery for independently installed helpers instead of assuming sibling installation. No duplicate introduction is added. |
| Revise Attack the Premise, Fix Root Causes and Test Behavior summaries | Already adopted by [PR #85's principle update](../principle-behavior-updates/README.md). These lines are unchanged here. |
| Make the receiving chat run the playbook instead of spawning an ordinary wrapper to run it | Adopt the two source sentences with local naming and `ordinary playbook child` replacing Cursor's `poteto-agent`. Add the assigned step or bounded subtask to the existing execution-brief checklist. |
| Add adaptive effort/speed selection | Keep exact saved model options under the [existing policy decision boundary](../../coverage-audits/2026-10-18/README.md). This update does not authorize task-based effort changes, fallback models or saved-config edits. |

The parent inspected the full final upstream/local entrypoint diff. Remaining differences are the [recorded runtime and authority adaptations](../../adaptations/juan-mode.md): portable identities and helper discovery, until-opt-out state, supported host tools, explicit authorization, configured role resolution, ordinary versus specialized briefs, fresh review tasks, availability reporting and parent-owned watches. Existing route summaries and procedure ordering remain intact. The model-policy difference above stays explicit.

Removing the two added coordination sentences reproduces the base entrypoint byte for byte. Reversing the one checklist edit reproduces the base execution reference. The latter has no upstream counterpart; it makes the source rule concrete in the T3 child brief. Every other shipped file is unchanged, including all 23 playbooks, activation/configuration references, preflight and setup. The license matches upstream. Source pins, the manifest and reviewed checkpoint remain unchanged.

## Instruction exercise

[Four cases and expectations](cases.json) cover a whole-playbook handoff, an ordinary serializer brief, a specialized How explorer and a bounded read-only child. Reproduce with a fresh agent given the requests without their expectations, the complete authoring mode entrypoint and its execution/activation references. Ask for concrete decisions or a draft prompt only. Keep tool execution, nested dispatch, application writes, forge actions, installation and configuration changes out of the exercise. Compare actual answers with the retained expectations.

One fresh native Codex agent, using inherited gpt-6-astra/high, answered all four cases on 2026-10-19. It read the mode and references, plus the relevant Bug fix, Feature, Investigation and How instructions. The parent inspected the actual report; all eight recorded expectations were met.

| Case | Observed decision |
| --- | --- |
| Receiving chat | Rejected the complete-playbook child assignment. Kept coordination, patch review and verification in the parent; proposed bounded assignments with inherited options omitted. |
| Ordinary brief | Included the exact mode path, full-read requirement, independent catalog discovery, assigned file/base/config, acceptance placeholders, evidence return and parent-reserved actions. |
| Specialized helper | Kept Investigation coordination in the receiving chat and explorer briefs with How. Preserved its configured explorer/explainer roles. |
| Bounded child | Kept the hypothetical parser inspection read-only. Did not claim persistent activation, a complete Bug fix run, actual findings or PR creation. |

The agent received no expectation list, prior result or diff. The four cases shared its context. This is one instruction exercise, not four independent trials or a measured improvement over the previous text. It drafted a brief but did not dispatch that brief to another worker. Actual delegation, model resolution, cross-provider behavior, compaction and full playbook execution remain outside this result. Tracked skill files and the upstream manifest were unchanged during the exercise.

## Checks and limits

The four packaging tests, mode skill validation, documentation checker and whitespace checks pass. The documentation checker reports 45 skills and 23 playbooks with zero problems; guide coverage remains pending. Relative links in this report and the updated adaptation record resolve. The parent checked the exact two-edit scope and complete source diff, including the unchanged absolute-path contract. These checks validate the instructions and package, not enforcement by the runtime.

```sh
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
node scripts/jstack/check_docs.mjs
git diff --check
```

The evaluation retains only this report and the four prompts/expectations. Raw agent output and source diffs remain in task-owned cache. No installation, model configuration or schedule changes are part of this update.

## Normal use

With Juan-mode active, ask: "Fix CSV export dropping the last column." The main conversation runs the Bug fix procedure. It can give a child a scoped implementation task, then inspect the returned patch and verification evidence. It does not hand the entire playbook to an ordinary child. Specialized How or Why investigation keeps its own briefs. The user needs no new command.
