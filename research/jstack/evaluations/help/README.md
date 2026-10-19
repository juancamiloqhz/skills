# Help and guide evaluation

Source: `pstack/skills/poteto-help/` and `pstack/docs/guide/` at `0148b78c56c72a1b8412055913c79f767095b217`. Local: [jstack-juan-help](../../../../skills/jstack/jstack-juan-help/SKILL.md). [Adaptation record](../../adaptations/help.md).

This change adds a read-only help entrypoint and the complete 11-page source guide inside its independently installable package. Help reads the relevant skill or guide, answers briefly, and supplies at most one prompt plus a source link. A request to execute work remains distinct from a help question. The package keeps the original guide organization and illustrations while explaining actual jstack configuration, activation and host limits.

## Consumer exercises

A fresh native authoring evaluator inherited GPT-6-astra/high and read the entrypoint and relevant current authoring sources. It answered the first three [cases](cases.json), then a separate missing-configuration case. These were read-only authoring exercises, not operational configured-role dispatch or a blinded comparison. The parent inspected the returned answers.

| Case | Observed answer and boundary |
| --- | --- |
| PR status | Read Babysit, supplied one `/jstack-juan-mode check on PR #123` prompt specifying a read-only pass, and linked the owning procedure. Did not review the PR. |
| Activation after reopening | Distinguished intended same-conversation activation until opt-out from unverified provider resume. New conversations start inactive. Offered explicit re-invocation without claiming persistence had been tested. |
| Make bot UI and `/loop` | Identified the former as unported and the latter as Cursor-specific. Required an actual supported wake mechanism and checkable finish condition, without starting or scheduling a task. |
| Missing config, user selects Later | Honored Later without asking again, explained unavailable configured delegation, and provided a setup prompt. Explained that inherited effort stays unchanged and a smaller budget is not a spending cap. Used the supplied lookup result, not the real saved configuration. |

The consumer runs preceded the user-requested rename from `jstack-help` to `jstack-juan-help`. The rename changes identity and paths only; packaging, documentation and source-link checks were rerun afterward. Consumer behavior was not rerun for that rename.

All four answers linked the source under the explicit authoring branch and used at most one prompt block. No delegate, setting write, installation or external action was requested by these answers. Their content establishes bounded help behavior, not proof that the recommended workflows work on every provider.

The first consumer found Help's short Babysit summary misleading: it grouped a status check with drive mode. The owning procedure and guide already distinguished them, so the answer was correct despite the summary. The final summary now explicitly distinguishes `check` and `drive`. The Later case also prompted a clarification to reuse an explicit choice already supplied.

## Source review and corrections

An independent read-only reviewer compared Help, both references and every guide page with the pinned source, then checked actual jstack procedures. It found the same Babysit distinction and two further wording problems: Reflect appeared to require fresh approval despite existing authorization, and Shipping's Origin wording obscured an implemented but live-unverified route. Both were corrected. The reviewer reread all three corrected passages and reported no outstanding findings.

All 14 Markdown source files retain their heading counts and page/section order, with the documented identity/runtime heading substitutions. Both prompt references, all workflow table rows, 24 principles and all six JPEGs remain. Image and license bytes match upstream exactly. Comparing headings is only a structural check; the actual source-body review supports the fidelity assessment. The adaptation record accounts for packaging, model/configuration, authority, activation, workspace, host and pending-integration differences.

## Packaging and documentation checks

- Four skill-packaging tests passed with the new package and mapping.
- All 20 documentation-checker tests passed after switching its guide path from the reserved research location to the actual package location.
- The current-doc checker reports 56 packages, 32 commands, 24 principles and 23 playbooks, with zero problems. The guide names 26 of 32 commands; it preserves the source guide's scope, not exhaustive command-by-command documentation. Help's map and dependency discovery cover additional commands.
- Separately checked 128 public repository links against local targets, including anchors. The existing checker validates relative links but does not fetch public URLs. This is local target validation, not a network availability claim.
- Manifest loading passed. Removing only the new Help entry yields the exact previous manifest, including every existing mapping, decision and reviewed checkpoint.
- The generic Codex validator rejects the preserved upstream `disable-model-invocation` field. A temporary copy omitting only that field passes its remaining checks. The shipped field remains intact, with Codex `allow_implicit_invocation: false`. This qualified check does not establish installed-provider discovery.

No existing operational skill, model configuration, schedule or installed package was changed. The six illustrations total about 2.3 MB and are required guide assets, not test logs. Retained evaluation evidence is this report and four prompts; no raw conversations, generated HTML or duplicate guide copy is committed.

## Reproduce

From the repository root:

```sh
node --test scripts/jstack/test_check_docs.mjs
node scripts/jstack/check_docs.mjs
python3 -B -m unittest discover -s scripts/jstack -p test_skill_packaging.py
python3 /home/ubuntu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/jstack/jstack-juan-help
```

The final command is expected to report the unsupported preserved frontmatter field described above; locate the host's validator if installed elsewhere. Compare the source tree at the recorded revision with `skills/jstack/jstack-juan-help/`, mapping `skills/poteto-help/*` to the package root and `docs/guide/02-poteto-mode.md` to `docs/guide/02-juan-mode.md`. Compare each image and license byte-for-byte. Read the substantive diff using the adaptation table rather than treating name substitutions or matching counts as a semantic pass.

For consumer reproduction, give a fresh reader the entrypoint, one case and access to relevant `skills/jstack/` authoring files. Supply an explicit revision for unpublished-source links. Permit read-only source access; do not provide this report as an answer key, dispatch children, touch real configuration or execute the suggested work. For case 4, supply its missing-config facts. Inspect the actual response for source grounding, a single usable prompt, accurate limitations and no task execution.

## Limits and normal use

Installed slash-menu discovery, interactive question delivery, real configuration lookup, explicit-work execution routing, all recommended workflows, cross-provider behavior and persistence were not exercised. Make bot UI and Benny remain unported; Unslop stays external. This work does not close distribution integrations or the provider/persistence release matrix.

After merge and manual installation, try `$jstack-juan-help Which skill should I use to check whether PR #123 is ready?` It should explain the status-check route and give a prompt you can send when ready. Asking for help does not start the review or activate Juan-mode.
