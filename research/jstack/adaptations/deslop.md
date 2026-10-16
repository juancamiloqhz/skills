# Deslop adaptation

Source: `cursor-team-kit/skills/deslop/SKILL.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [jstack-deslop](../../../skills/jstack/jstack-deslop/SKILL.md). The source directory contains one file. Preserve its standalone boundary, description, heading, focus areas, guardrails and concise reply instruction.

## Complete differences

| Location | Change | Requirement |
| --- | --- | --- |
| Frontmatter name | `deslop` becomes `jstack-deslop`. | User-approved portable identity policy. The entire body and description are otherwise byte-identical. |
| Package license | Include the exact pinned `cursor-team-kit/LICENSE`. | Preserve the Cursor copyright and MIT notice with the distributed adaptation. |
| Juan-mode trigger | Replace external plugin `/deslop` with the standalone `jstack-deslop` helper. | The pre-commit caller must discover the shipped identity. |
| Juan-mode dependency paragraph | Identify Deslop and Control CLI as jstack helpers while retaining external Control UI. | Discovery should reflect the actual packages. |

The source's clear-bug exception remains intact. A narrower user request still controls scope, including a cleanup-only task that forbids behavior changes. Invoking this helper does not itself request a commit or activate Juan-mode. No new procedure, delegation role or shared configuration rule is added.

## Maintenance and verification

The manifest adds one mapping, the exact Deslop watch subtree and the mode's caller context. The Cursor team-kit license is already watched and becomes the helper's license context. Existing mappings, source pins, decisions and reviewed checkpoint remain unchanged. There are 43 mapped skills, five implemented playbooks and 18 pending procedures.

[Full comparison and evaluation](../evaluations/deslop/README.md) cover the complete helper, license and mode entrypoint. The cleanup exercise runs existing public behavior checks and preserves unrelated staged and untracked work. It uses an explicit authoring path, so installed discovery and full-mode pre-commit execution remain unproven. Installation remains manual.
