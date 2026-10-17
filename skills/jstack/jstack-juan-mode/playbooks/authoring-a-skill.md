### Authoring or modifying a skill

**You own the skill's voice.**

1. Use the host's advertised skill-authoring skill, such as **skill-creator**, in place of Cursor's built-in **create-skill**. Read its discovered entrypoint; an absent or inaccessible authoring dependency leaves this step incomplete.
2. Validate the skill: frontmatter has `name` and `description`, referenced files exist, cross-skill links resolve. Resolve packaged files from the skill's own location and independent helpers through the host catalog; do not assume separately installed skills are siblings. Frontmatter validation alone does not establish working references or behavior.
3. Test cases if structural. Skip if subjective.
4. Run **Opening a PR** when publication is authorized. Read and follow [Opening a PR](opening-a-pr.md). Preserve the requested delivery boundary, including local-only drafts. Authoring does not authorize merging or installation.

When in doubt, delete. Keep only prose that changes a decision. Tell it to do the thing and skip the reason. Explain only when the rule is confusing without one. Match tone to scope. Point at structural sources (types, READMEs, config) per the **jstack-principle-encode-lessons-in-structure** principle skill. Delegate to other skills by path. Don't restate. A workflow you keep hitting but isn't captured → propose a new skill.

**Reply:** summary of the skill, key design decisions, validation notes.
