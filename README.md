# AI Agent Kit

This is my broader personal operating system for AI agents.

The goal is to keep reusable agent behavior in one durable place: skills, prompts, instructions, templates, scripts, and examples that make AI agents work more like long-term collaborators instead of one-off chat sessions.

The first artifact in this kit is the `deep-understanding` skill, adapted from Suzanne's teaching-mode prompt shared by Thariq. Its core idea is simple: the human's understanding should be a first-class deliverable.

## Repository Structure

This repo is intentionally broader than a skills-only library. A useful long-term shape could look like this:

```text
ai-agent-kit/
  skills/
    deep-understanding/
      SKILL.md
      agents/
        openai.yaml
  instructions/
    AGENTS.md
    CLAUDE.md
  prompts/
    research.md
    planning.md
    debugging.md
  templates/
    project-brief.md
    prd.md
    status-update.md
  scripts/
    install-skills.sh
  examples/
    deep-understanding-session.md
```

## Current Contents

- `skills/deep-understanding`: A multipurpose teaching skill for code, research, strategy, systems, documents, workflows, and other complex topics.
- `scripts/install-skills.sh`: Copies skills from this repo into `~/.codex/skills` so Codex can discover them.

## Install Skills

From the repo root:

```sh
./scripts/install-skills.sh
```

This copies every folder in `skills/` into:

```text
~/.codex/skills/
```

## Design Principles

- Keep reusable agent behavior versioned.
- Prefer skills for procedures that are useful sometimes, but should not load into every session.
- Prefer `AGENTS.md` or `CLAUDE.md` for small default preferences and pointers to skills.
- Keep prompts and instructions portable across tools when possible.
- Let the kit grow slowly from real usage, not from speculative organization.
