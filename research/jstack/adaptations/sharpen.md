# Sharpen adaptation

Source: `pstack/skills/sharpen/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. Local: [jstack-sharpen](../../../skills/jstack/jstack-sharpen/SKILL.md).

The initial adoption preserved the complete body and explicit-invocation flag byte-for-byte. Only the frontmatter name and description's slash command gained the approved `jstack-` prefix. The exact pstack MIT notice is included. `agents/openai.yaml` adds a direct invocation prompt and `allow_implicit_invocation: false` for Codex. Installed discovery and invocation behavior on other providers remain unverified.

No new role, configuration, script, helper dependency or automatic Juan-mode trigger is added. The [evaluation](../evaluations/task-framing/README.md) distinguishes authoring-path exercises from installed-provider support. Provenance stays here rather than adding text to the operational skill.

## Prompt-only update, 2026-10-25

Adopt the complete body and description from `pstack/skills/sharpen/SKILL.md` at `99b609a72323b70204eab407c622f436e858e112`, with only the existing name and slash-command translation. The skill now states four framing points and returns a rewritten prompt. It does not perform the requested task. Update the Codex default prompt and current Help, guide, catalog and migration examples together. Preserve both explicit-invocation policies, the original manifest pin and exact license.

The [controlled comparison](../evaluations/sharpen-prompt/README.md) exercises both versions against the same fixture request. This is a new upstream behavior, not a local redesign or proof of installed-provider invocation. The broader guide-refresh recommendation remains pending beyond its Sharpen-related text.
