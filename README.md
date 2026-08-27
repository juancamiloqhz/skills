# Skills

[![skills.sh](https://skills.sh/b/juancamiloqhz/skills)](https://skills.sh/juancamiloqhz/skills)

Reusable agent skills for Codex and other tools that support the open Agent Skills format.

This repository is the canonical source for skills I have developed and validated through real project work. Each skill is self-contained under [`skills/`](./skills) and includes a `SKILL.md` entrypoint plus only the resources its workflow needs.

## Catalog

| Skill | Purpose | Status |
| --- | --- | --- |
| [`deep-understanding`](./skills/deep-understanding) | Makes the human's understanding a first-class deliverable through incremental explanation, active recall, and lightweight knowledge checks. | Experimental |

## Install

Use the Skills CLI to discover the available skills and choose where to install them:

```sh
npx skills add juancamiloqhz/skills
```

Install `deep-understanding` directly:

```sh
npx skills add juancamiloqhz/skills --skill deep-understanding
```

Codex users can alternatively ask `$skill-installer` to install an individual skill from this repository:

```text
Use $skill-installer to install deep-understanding from
https://github.com/juancamiloqhz/skills/tree/main/skills/deep-understanding
```

For local authoring with Codex, clone this repository and symlink the skill directory into `~/.agents/skills`:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "/path/to/skills/skills/deep-understanding" "$HOME/.agents/skills/deep-understanding"
```

Codex discovers user-level skills from `~/.agents/skills`. Repository-specific skills should instead live in that repository's `.agents/skills` directory.

## Repository Structure

```text
skills/
  deep-understanding/
    SKILL.md
    agents/
      openai.yaml
```

Skills may also contain `references/`, `scripts/`, or `assets/` when those resources directly support the workflow. Empty scaffolding is intentionally avoided.

## Design Principles

- Build skills from workflows proven in real projects.
- Keep each skill focused on one job with clear activation boundaries.
- Prefer concise instructions over speculative rules or unnecessary scripts.
- Keep repository-specific knowledge in the repository that owns it.
- Preserve approval boundaries for external or destructive actions.
- Validate skills before publishing releases.

## Attribution

`deep-understanding` was inspired by Suzanne's original “Learn Quiz” teaching concept, shared publicly by [Thariq Shambaugh](https://x.com/trq212/status/2061545633560010826). It generalizes the teaching loop into a reusable skill for understanding codebases, systems, decisions, documents, research, workflows, and other complex topics.

## Maturity

The repository is currently experimental. Skill behavior and packaging may evolve as the skills are tested across different projects.

## License

Released under the [MIT License](./LICENSE).
