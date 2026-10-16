# Technical writing adaptation

Source: [pstack technical-writing](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/technical-writing/SKILL.md), revision `11713c683fe4add4fd403ea880580abbc9e0875f`. Local package: [jstack-technical-writing](../../../skills/jstack/jstack-technical-writing/SKILL.md). Its [MIT license](../../../skills/jstack/jstack-technical-writing/LICENSE) matches the pinned plugin notice, including Lauren Tan's attribution.

The entire source package consists of one `SKILL.md`. Keep its three top-level rules, vocabulary guidance, rhythm section, four writing layers, four document modes, PR/commit exception, voice rules and worked example inline. No model resolver, new workflow role, script, index or duplicated Unslop catalog is needed. The executing agent applies the standard to the requested prose.

## Complete differences

| Location | Difference and reason | Verification or limit |
| --- | --- | --- |
| Name and slash example | Use `jstack-technical-writing`. | The user-approved [portable naming policy](../skill-names.md). |
| Frontmatter | Omit `disable-model-invocation: true` because the mode must discover and call this helper. | The established [invocation compatibility assessment](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) explains the blocked Claude catalog-call route. Automatic selection remains possible; a full installed-provider invocation is not claimed. |
| After introduction | Bound review/edit/publication authority; preserve factual uncertainty, literal code and required repository/host templates. | A writing instruction cannot authorize edits on a findings-only request, invent missing facts or override repository conventions. The PR example exercises the required template; the unavailable-dependency case is findings-only. |
| Unslop bullet | Discover the intended external dependency, read it in full, assess a different same-name package before use, and report a missing/ambiguous/blocked dependency as incomplete. | Do not silently replace the upstream catalog, install it, or bypass host restrictions. The installed content assessment below is version-specific. |
| Code indentation bullet | Retain tabs as the default, with an exception for language syntax or repository conventions. | YAML syntax and existing repository formatting can require spaces. The bounded exercise includes repository-required Python and JSON indentation. |

## Unslop dependency assessment

Retain Unslop as the separately installed upstream dependency named `unslop`. It is not a newly shipped jstack skill, so the `jstack-` naming policy does not rename it. No installed package is edited, copied into jstack, or automatically installed.

On 2026-10-15, `/home/ubuntu/.agents/.skill-lock.json` identifies the installed `/home/ubuntu/.agents/skills/unslop/SKILL.md` as `cursor/plugins`, path `pstack/skills/unslop/SKILL.md`. The pinned source SHA-256 is `3126b9e2cf46022f5e0c332e84be5e17a9730669cb3d6ac0a7e5e7e94b1e24fa`; the installed SHA-256 is `c6d2572294d933a428211921069e9a248490e9b466ca59437cb4d9de248600ca`.

The full comparison finds an added Process heading and self-audit step, plus editorial differences in rules 8, 10, 14, 19, 23, 26, 30 and 31. Rule numbers, examples and prohibitions retain their meaning. In particular, rule 26 retains the same abstract-metaphor vocabulary and concrete replacements. The added self-audit repeats the stated cleanup objective. This installed version supplies the required writing behavior; it is not byte-identical and does not establish equivalence for an arbitrary same-name package or future update.

Both upstream and installed Unslop retain `disable-model-invocation: true`. Content equivalence does not make that dependency callable on every host. The tests supply an authoring path in the Codex evaluator; they do not bypass a rejected provider invocation. If a host blocks the dependency, the writing check remains incomplete. A cross-provider packaging or invocation change needs its own assessment; this PR does not change the user's installed skill.

## Caller and maintenance integration

The mode's docs/PR/commit trigger now calls `jstack-technical-writing`. Its helper list includes the new package and removes technical writing from the missing-package sentence. All remaining mode instructions and support files are preserved. Full pinned-mode and previous-local diffs are retained in the evaluation.

The manifest adds one component at the consuming mode's source pin and watches its Unslop and mode context. The mode directly watches both helper source paths. Existing pins, review decisions, checkpoint, configuration schema and model files stay unchanged. This supplies a writing helper, not the Opening a PR or any other pending playbook.

[Source comparison and bounded evaluation](../evaluations/technical-writing/README.md) records observed outputs and limits. Installation and merging remain separate from this implementation PR.
