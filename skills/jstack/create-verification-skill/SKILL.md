---
name: create-verification-skill
description: Generate and exercise a project-local verification skill for real UI, CLI, API, or library behavior. Use when creating reusable verification instructions for a repository or when jstack setup offers them; not for running an existing verification skill or configuring models.
---

# Create a verification skill

Build instructions another agent can follow without this conversation: start the real application, exercise a user-visible behavior, preserve evidence, and clean up owned state. This is jstack's adaptation of pstack's generator. Read [the output contract](references/output-contract.md) before writing; [upstream attribution](references/upstream.md) records the source and adaptations.

## Inspect the project

Establish the target repository from the request and read its applicable instructions. Inspect its documented startup commands, public entry points, existing verification skills and test tooling. Ask only for missing information that prevents a grounded or authorized run.

Identify the primary user interface and any secondary interfaces, prerequisites, observable results, and how to isolate processes, data, profiles and ports. Prefer the repository's existing harness. A short-lived CLI can use ordinary subprocesses; interactive terminal behavior needs a PTY. API proof uses the public endpoint, and library proof uses a real public-API client.

If a suitable verify skill already exists, assess it and make only requested repairs rather than creating a competing one. Reuse a working test harness as the execution mechanism when it exercises the intended user path. A documentation-only repository with no executable product needs no invented app skill; explain that outcome and stop without generating files.

Check that the documented baseline actually runs before claiming verified output. Report missing credentials, dependencies, startup failures or inaccessible tools precisely. Small verification scaffolding must be identified and cleaned up; broader application fixes, system installation and external changes require authorization under the current task. Do not manufacture passing output or bypass a broken startup path.

## Select tools and output location

For browser interaction in T3 Code, start with `preview_status`, then `preview_open` if no automation-capable preview is attached. Use current callable schemas and observed snapshot locators. Respect human-owned tabs and current T3 Code fallback rules. An existing repository harness remains useful for its documented tests. A failed T3 Code preview is not permission to install system libraries or silently switch browser systems. Record the blocker if the required route cannot run. Outside T3 Code, use the available project harness and state its prerequisites.

Write one canonical project-local skill. Honor an explicit output path or repository convention; otherwise author `.agents/skills/verify-<app>/`. Use a stable lowercase app name. Check the destination before writing and preserve unrelated content. The project-local Claude Code link below is part of generation. Global skill installations, updates and provider settings remain user-managed.

## Generate the instructions and feature map

Write `SKILL.md` with a valid name and a description naming the product, interface, and verification triggers. Follow the output contract for Launch, Doctor, Drive, Evidence, Cleanup and any Helpers. Ground commands, selectors, assertions, and prerequisites in this checkout. Resolve paths from the repository or skill location instead of relying on the author's working directory or temporary machine paths.

Add `features/README.md` and a small set of feature files, usually three to five when that many meaningful features exist. The index defines baseline state, links the features and tracks tested versus untested entry points. Each feature explains what users do, exact steps to reproduce it, and the observable result. Do not treat a map of intended coverage as completed verification.

Keep scratch data separate from retained evidence. Limit changes to owned instances and authorized test state. A skill, test mode, or dry-run flag grants no permission to send messages, charge accounts, publish, push, or mutate shared services. Verify a claimed dry-run's effects rather than trusting its name. Keep credentials and private payloads out of artifacts.

## Link the generated skill for Claude Code

For every generated skill, automatically create `.claude/skills/verify-<app>` as a relative symlink to its canonical directory, regardless of the executing provider or the project's current use of Claude Code. Create missing parent directories. Link the whole directory so features and helpers share one source. If the canonical skill already lives at that path or an existing link resolves to it, leave it in place.

For the default layout, the link target is `../../.agents/skills/verify-<app>`. Resolve this from the link's containing directory, `.claude/skills/`: the two `..` steps reach the repository root, not the home directory. Calculate the relative target from the actual parent location for custom layouts. Check that resolved parents and targets stay in the authorized repository. Preserve conflicting files, directories or links, including dangling links, and report the conflict instead of replacing them. If no skill was generated, create no link.

Verify that `SKILL.md` and the generated supporting files resolve to the canonical files through the link. Report both paths and any linking failure at handoff. [Claude Code supports project-local symlinked skill directories](https://code.claude.com/docs/en/skills#choose-where-skills-load); report live client discovery as untested unless checked in a Claude Code session. Linking is a generator step, not an instruction the generated skill must execute on every run.

## Exercise and hand off

Follow the generated instructions end to end for at least one mapped feature: launch, doctor, perform the real action, assert its result and relevant side effects, retain evidence, then clean up. Use the generated helper invocation if one exists. Clean up owned processes and scratch data on failure too; preserve diagnostics and never kill by process name. After cleanup, check that the proof still exists and that the owned process or scratch state is gone.

Fix recipe defects and repeat the failed path. If execution is blocked, label the output a draft and name the failed command or missing prerequisite; do not claim a proven skill. If no skill was generated, say so. Successful handoff names the output path, feature and entry points exercised, evidence location, cleanup result, and untested interfaces or features.

For later upkeep, `maintain-verification-skill` audits an existing map against source and live behavior. Resolve it from the current catalog or an explicitly supplied source path before handing off; it may be installed separately. If unavailable, provide manual installation instructions rather than assuming a sibling directory or installing it. Model setup may offer this generator as a separate project verification task; invoking it does not change `models.json`.
