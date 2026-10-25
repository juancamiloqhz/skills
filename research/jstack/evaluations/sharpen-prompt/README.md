# Sharpen returns a rewritten prompt

The user selected Sharpen and its matching Help text from the [2026-10-25 upstream review](../../upstream-reviews/2026-10-25.md). Base is merged PR #138, `8570fe9ed84f7f152e98e3e385d5f102ab5dcc52`. The earlier [task-framing record](../task-framing/README.md) and its cases remain historical evidence for the version that performed the task.

Sharpen now names what a professional would add, their raw material, their methods and tools, and an outside check. It then returns a rewritten prompt and leaves the user's choices open. The user decides when to send that prompt to perform the work.

## Source and coordinated changes

The final `skills/jstack/jstack-sharpen/SKILL.md` matches [pstack's complete skill at `99b609a72323b70204eab407c622f436e858e112`](https://github.com/cursor/plugins/blob/99b609a72323b70204eab407c622f436e858e112/pstack/skills/sharpen/SKILL.md), changing only the name and description's slash command to `jstack-sharpen`. Both invocation flags stay explicit, and the license remains byte-identical. The original manifest `adaptedFrom` pin is preserved.

The Codex default prompt now requests a rewritten prompt. Help's skill row, its recipe, the Sharpen-related guide sections, root catalog and current migration usage match that boundary. The guide additions follow the corresponding source paragraphs with jstack identities and canonical independent-package links. No other formal-verification, new-skill, Reflect or setup recommendation is implemented. The guide-refresh decision therefore remains pending beyond this subset.

The three already merged tool decisions additionally receive PR #138's verified merge commit in this maintenance update. Sharpen receives no `appliedCommit` before its own merge.

## Controlled behavioral comparison

The [replay case](case.json) contains one request and its two raw fixture files. Two fresh T3-owned Codex children received identical briefs except for the skill snapshot and exclusive fixture path. Each could read its skill/request/fixture and edit that fixture if the task, interpreted through the skill, called for it. Neither brief supplied expected behavior or grading criteria. Both inherited the parent's `codex / gpt-6.1-sol / reasoningEffort: high / serviceTier: priority`, verified against dispatch receipts. No saved model setting changed.

| Skill snapshot | Actual result checked by the parent |
| --- | --- |
| Original skill from current main | Rewrote the fixture `onboarding.md`, returned a completion message and left the tuning-placement choice open. Its report distinguished supplied facts from an actual importer run. |
| New pinned-source body | Returned all four framing points and a rewritten prompt. Both fixture files stayed unchanged. The rewrite retained the exact command, word limit and unresolved tuning placement, and disclosed that no importer executable was available. |

Both tasks were terminal `completed`, `result_available`, with no pending child runs. Task identifiers end in `jstack-sharpen-consumer-a-20261025-r1` and `jstack-sharpen-consumer-b-20261025-r1` under command `539882a9-7da7-498e-8811-5c4c78e65e9d`. The parent read both complete responses and checked the actual fixture contents and file lists. The baseline's initial `python` command was unavailable; it used Python 3 for its checks. No real importer execution, network action or product edit occurred.

This is one controlled comparison on an explicit authoring path, not a reliability estimate, installed slash-registration test or all-provider certification. Help text was checked structurally and against the source, not through another live Help workflow. Native invocation and automatic dependency behavior remain separate claims.

## Validation and reproduction

- Four repository packaging tests and all 20 documentation-checker tests pass. YAML parsing verifies names, descriptions and preserved `disable-model-invocation: true` / `allow_implicit_invocation: false` for both packages.
- The generic system skill-creator validator rejects `disable-model-invocation` as an unknown key. It also rejects the original baseline and unchanged Help flag. That validator is incompatible with this existing upstream metadata; its check is incomplete, not a pass. The flag was preserved and the validator was not weakened.
- The source comparison verifies the full current body, original pin, license and supported metadata changes. Report/manifest links and the existing docs checker are checked before publication.

To replay, materialize `files` from `case.json` in two owned temporary directories. Give separate fresh consumers the request and raw files, omitting `checks` and prior results. Supply the old skill from `8570fe9:skills/jstack/jstack-sharpen/SKILL.md` to one and the new authoring skill to the other. Permit fixture edits, record their responses outside the repository, then compare actual file contents and user-facing answers. No provider/model override is required.

```sh
python3 -B -m unittest discover -s scripts/jstack -p 'test_skill_packaging.py'
node --test scripts/jstack/test_check_docs.mjs
node scripts/jstack/check_docs.mjs
```

## Usage and retention

After merging and manually updating Sharpen and Help, send `/jstack-sharpen write an onboarding guide for our importer.` Read its framing and rewritten prompt. Send the rewrite, for example with `/jstack-juan-mode`, when you want execution. No setup rerun or model change is needed.

Keep this report and the small replay case. Raw child responses and fixture outputs stay outside the repository during evaluation; remove the owned copies after the findings are captured and publication is verified. No transcript dump, capability catalog, installation, model edit or schedule change is part of the PR.
