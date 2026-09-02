# Harness Loading Semantics

Last verified: 2026-08-30. Tool behavior changes; recheck the official documentation when a conclusion depends on an edge case.

## Codex

Official reference: [Codex `AGENTS.md` guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

For a run, Codex builds an instruction chain once:

1. At the user level (`$CODEX_HOME`, normally `~/.codex`), it loads the first non-empty `AGENTS.override.md` or `AGENTS.md`.
2. At the project level, it walks from the project root to the current working directory.
3. In each directory, it loads at most one file: `AGENTS.override.md`, then `AGENTS.md`, then configured fallback filenames in order.
4. It concatenates files from root toward the working directory. Later, closer instructions override earlier ones.
5. It stops at the current working directory; descendants are not loaded merely because they exist.
6. Project instruction content is capped by `project_doc_max_bytes`, which defaults to 32 KiB. Configured fallback names and the byte cap may change this behavior.

Audit each materially different starting directory. A root-only audit can miss a nested override; a repository-wide file list does not by itself describe an effective chain.

## Claude Code

Official reference: [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)

Claude Code uses `CLAUDE.md`-family files rather than `AGENTS.md` directly:

- Project instructions may live in `CLAUDE.md` or `.claude/CLAUDE.md`.
- Project-root and ancestor instruction files are loaded at launch.
- `CLAUDE.local.md` supports local, non-shared project instructions.
- Child-directory `CLAUDE.md` files are discovered when Claude reads files in those subtrees, so their behavior differs from Codex's start-directory chain.
- `.claude/rules/` can hold modular instructions, including path-scoped rules.
- `@path` imports are expanded into the importing file's context. They are eager composition, not progressive disclosure. Current documentation limits recursive imports to five hops; verify this before relying on the exact limit.

Inventory both launch-time candidates and subtree instructions relevant to the files the task will touch.

## Supporting Both Harnesses

Do not maintain two complete manual copies. Prefer one of these designs:

1. Keep shared repository policy in `AGENTS.md`; make `CLAUDE.md` import it with `@AGENTS.md`, then add only Claude-specific guidance.
2. Symlink `CLAUDE.md` to `AGENTS.md` when no Claude-specific addendum is needed and symlinks are reliable in the repository's environments.
3. Keep a small shared document and thin harness-native entrypoints only when import or symlink constraints require it.

Validate the chosen design in both tools. A normal Markdown link to `AGENTS.md` creates navigation, not guaranteed loading. An instruction such as “For database migrations, read `docs/migrations.md` before editing schemas” is progressive routing. A Claude `@docs/migrations.md` import loads the document eagerly.

## Audit Boundaries

- Do not inspect `~/.codex`, `~/.claude`, managed organization policy, or other user-level files unless the user explicitly includes them.
- Record configured fallback filenames or non-default byte limits when available. Otherwise label the Codex chain as using default configuration.
- Treat harness behavior as independent from the prose quality of the files. Validate both.
