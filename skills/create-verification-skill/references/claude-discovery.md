# Claude Code discovery

Use this guidance for every generated verification skill's handoff, regardless of the executing provider or the project's current use of Claude Code. Provide commands for the user to run manually; generation does not create provider links or install skills.

Claude Code's project location is `<repo>/.claude/skills/<skill-name>/SKILL.md`. Its personal location, `~/.claude/skills/`, applies across projects and is unsuitable for this project-specific recipe. The [official skill documentation](https://code.claude.com/docs/en/skills#choose-where-skills-load), checked on 2026-10-11, supports individual skill directories that are symlinks.

## Select the link

Keep the generated directory as the canonical copy, including its feature map and helpers. If it already lives in the project's `.claude/skills/`, no link is needed. For the default `.agents/skills/verify-<app>/` location, offer one link at `.claude/skills/verify-<app>`. Link the whole skill directory so supporting files share the same source.

Inspect the destination and its parent directories before giving commands. If it already resolves to the canonical directory, report that the link exists. Preserve any other file, directory or symlink, including a dangling link, and report the conflict instead of replacing it. If a parent directory is itself a symlink, resolve its actual location before calculating the relative target. For a custom canonical location, calculate the target relative to the link's containing directory; do not reuse the example's `../../` blindly.

## Manual command

For a skill named `verify-myapp` in the default location with ordinary in-repository parent directories, give this command to run from the repository root. Replace `verify-myapp` with the actual generated directory name:

```sh
if [ ! -f .agents/skills/verify-myapp/SKILL.md ]; then
  printf '%s\n' 'Canonical skill is missing; no link created.'
elif [ -e .claude/skills/verify-myapp ] || [ -L .claude/skills/verify-myapp ]; then
  printf '%s\n' 'Destination already exists; inspect it before making changes.'
else
  mkdir -p .claude/skills &&
    ln -s ../../.agents/skills/verify-myapp .claude/skills/verify-myapp
fi
```

The symlink target is resolved from `<repo>/.claude/skills/`. The first `..` reaches `.claude/`; the second reaches the repository root. Both `.agents/` and `.claude/` belong to this repository. Neither path refers to the home directory. Relative links preserve that relationship in clones and Git worktrees that retain symlinks.

## Verify discovery

After the user creates the link, check that its `SKILL.md`, feature map and helpers resolve to the canonical files. A valid filesystem link alone does not establish client discovery. In a Claude Code session for that repository, confirm that the generated skill appears in the available skill/command list. If it is absent, check the client's version and discovery settings before claiming the setup works. Discovering the command does not require executing its application checks.

Maintenance should resolve the link and edit the same canonical files. Keep the link intact and avoid creating a second copy of the skill.
