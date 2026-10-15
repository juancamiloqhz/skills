# Jstack skill names and manual migration

The user approved these portable identities on 2026-10-15. Every shipped jstack skill starts with `jstack-`. The setup skill is `jstack-setup`, avoiding a repeated bundle name. Invoke `jstack-juan-mode` to activate the mode, or invoke a standalone helper such as `jstack-how` for one task.

Use the exact catalog name. Record its resolved name and absolute SKILL.md path in evaluation evidence. If the same prefixed name appears more than once, identify the intended source from catalog metadata or an explicit authoring path. A prefix distinguishes packages but does not authenticate their contents. Unresolved ambiguity remains an unavailable dependency.

Portable skill names use lowercase letters, digits and hyphens. A colon is a plugin namespace supplied by a host, not a portable SKILL.md name. This change keeps the existing Skills CLI distribution.

## Manual migration after merge

Updating skills under their new names can leave old installed copies behind. This PR does not edit installations.

1. Inspect your provider's skill catalog, installation paths, symlink targets and installer ownership records. Identify only copies that came from `juancamiloqhz/skills`. Do not remove pstack or another collection just because it has an old name from the table below.
2. Install the renamed packages you use in the same global or project scope as before. For example:

   ```sh
   npx skills add juancamiloqhz/skills --skill jstack-setup --skill jstack-juan-mode --skill jstack-how --skill jstack-why
   ```

   Select your providers and scope in the installer. Add the other helpers and principles you use by their new names below. Mode activation still requires its selected helper dependencies.
3. Remove only the verified old jstack installation entries using your installer's supported removal flow. Preserve unrelated packages, local modifications and model files. Resolve uncertain ownership before deleting anything.
4. Refresh the host's skill catalog or start a fresh conversation. Confirm the new names resolve to the intended installation and the former jstack entries are gone. Existing conversations may still hold old skill text and paths; reload the renamed entrypoint before continuing active mode.
5. Invoke `jstack-how` on a small read-only question. Confirm the task identifies its actual skill path and uses `jstack-setup`. If a dependency is missing or ambiguous, it must report that gap rather than substitute `how` or `setup-pstack`.

There are no unprefixed compatibility aliases. Existing `.jstack/models.json`, global model files and all 17 role keys remain valid. For example, `jstack-swarm` still resolves `swarm workers`. This rename does not require rerunning setup. Generated project skills remain `verify-<app>` with the existing Claude link behavior.

## Name mapping

| Former local name | Current catalog name |
| --- | --- |
| `juan-mode` | `jstack-juan-mode` |
| `setup-jstack` | `jstack-setup` |
| `create-verification-skill` | `jstack-create-verification-skill` |
| `maintain-verification-skill` | `jstack-maintain-verification-skill` |
| `how` | `jstack-how` |
| `why` | `jstack-why` |
| `arena` | `jstack-arena` |
| `architect` | `jstack-architect` |
| `interrogate` | `jstack-interrogate` |
| `swarm` | `jstack-swarm` |
| `reflect` | `jstack-reflect` |
| `figure-it-out` | `jstack-figure-it-out` |
| `show-me-your-work` | `jstack-show-me-your-work` |
| `principle-attack-the-premise` | `jstack-principle-attack-the-premise` |
| `principle-boundary-discipline` | `jstack-principle-boundary-discipline` |
| `principle-build-the-lever` | `jstack-principle-build-the-lever` |
| `principle-encode-lessons-in-structure` | `jstack-principle-encode-lessons-in-structure` |
| `principle-exhaust-the-design-space` | `jstack-principle-exhaust-the-design-space` |
| `principle-experience-first` | `jstack-principle-experience-first` |
| `principle-explain-the-number` | `jstack-principle-explain-the-number` |
| `principle-fix-root-causes` | `jstack-principle-fix-root-causes` |
| `principle-foundational-thinking` | `jstack-principle-foundational-thinking` |
| `principle-guard-the-context-window` | `jstack-principle-guard-the-context-window` |
| `principle-laziness-protocol` | `jstack-principle-laziness-protocol` |
| `principle-make-operations-idempotent` | `jstack-principle-make-operations-idempotent` |
| `principle-migrate-callers-then-delete-legacy-apis` | `jstack-principle-migrate-callers-then-delete-legacy-apis` |
| `principle-minimize-reader-load` | `jstack-principle-minimize-reader-load` |
| `principle-model-the-domain` | `jstack-principle-model-the-domain` |
| `principle-never-block-on-the-human` | `jstack-principle-never-block-on-the-human` |
| `principle-outcome-oriented-execution` | `jstack-principle-outcome-oriented-execution` |
| `principle-prove-it-works` | `jstack-principle-prove-it-works` |
| `principle-redesign-from-first-principles` | `jstack-principle-redesign-from-first-principles` |
| `principle-separate-before-serializing-shared-state` | `jstack-principle-separate-before-serializing-shared-state` |
| `principle-sequence-verifiable-units` | `jstack-principle-sequence-verifiable-units` |
| `principle-subtract-before-you-add` | `jstack-principle-subtract-before-you-add` |
| `principle-test-behavior-not-implementation` | `jstack-principle-test-behavior-not-implementation` |
| `principle-type-system-discipline` | `jstack-principle-type-system-discipline` |
| `benchmark-checklist` | `jstack-benchmark-checklist` |

## Upstream maintenance and evidence

`upstream.json` maps each new local identity to its original pstack path and unchanged revision pin. The shared reviewed checkpoint does not move. Preserve pstack's boundaries, headings, procedures and role labels; translate only package identities and their callers. Future adaptations must apply this mapping rather than restoring unprefixed names.

Old reports, audit outputs, task transcripts and reproduction scripts retain the paths and hashes they actually tested. Run those scripts at their recorded commits. For the last pre-migration tree, use commit `3c2e32c17ea6a08900af822fe205703e47be0072`. They are historical evidence, not current installation instructions. The [migration evaluation](evaluations/skill-names/README.md) records current checks and pinned-source comparisons.
