# Jstack upstream fidelity

User decision, 2026-10-13: jstack should remain a close, maintainable adaptation of pstack. Preserve upstream organization and behavior unless the target runtime or an explicit user requirement requires a difference. This policy governs new work, updates and reviews; it supersedes earlier packaging choices where they conflict.

## Default to upstream

Start from the exact source revision recorded in `upstream.json`. Preserve skill boundaries, names except required jstack renames, section organization, principle groupings, trigger placement, procedure order and substantive rules. Keep upstream wording where it still applies. Do not move an inline section into an index, combine standalone skills, summarize away behavior, or introduce an abstraction solely to shorten files or match a preferred style.

Runtime adaptations may replace Cursor-specific tools and metadata with supported T3 Code behavior, resolve models through jstack configuration, and honor actual user authorization and repository constraints. Make the smallest change that addresses the demonstrated incompatibility. Distinguish a requirement from a preference; generic portability or readability claims alone do not justify divergence.

Optional structural or behavioral redesign requires an explicit user decision before implementation. Existing authorization for a specific adaptation remains valid and needs no repeated confirmation. When uncertain, preserve upstream and report the proposed alternative rather than silently adopting it.

## Provenance location

Keep upstream source paths, revision pins and adaptation rationale in `research/jstack/` and the upstream manifest. Do not add provenance-only sections to operational SKILL.md files. Preserve required license and copyright notices in each distributed package. Discovery must not depend on a prose Attribution section. Existing helper provenance should be assessed during the broader fidelity audit rather than silently changed in an unrelated task.

## Evaluation evidence retention

User decision, 2026-10-17: keep the minimum evidence needed to review and reproduce jstack changes. Do not commit an entire evaluation workspace. This applies to future skills, playbooks, reviews and maintenance work, starting with PR #55.

Commit:

- Small fixtures and scripts needed to reproduce meaningful behavior checks. Generate deterministic datasets instead of storing them.
- One concise results report with the claim, environment, commands, outcomes, failures and remaining limitations. Keep individual measurement samples when needed to assess repeatability.
- Required upstream pins, adaptation decisions and source comparisons. Keep a primary trace or failure excerpt only when it supports a claim the report and reproducer cannot establish alone; explain its purpose.

Keep routine command transcripts, full subagent conversations and reports, capability catalogs, duplicate snapshots, generated datasets, intermediate databases, SQL dumps and raw debugging logs in task-owned scratch or cache by default. Do not replace hundreds of unnecessary files with one giant JSON file, archive, hash inventory or transcript. Summarize relevant findings once, preserving material failures and qualifications.

Before staging, inspect the file list and diff size. For each retained artifact, identify the claim or reproduction step that needs it. Remove redundant or generated artifacts, repair references and rerun the documented reproduction commands when their inputs or packaging change. A passing exit code does not justify retaining every log. Record only the validation result needed by the reviewer.

Keep temporary evidence while a run, review or recovery still needs it. After acceptance, task-owned scratch can be removed when no active task depends on it. Scratch paths are not durable evidence links. Preserve unique evidence needed for an unresolved failure until its finding is captured or the investigation is closed. Do not delete unrelated user data, shared caches or earlier merged review records as part of routine cleanup; historical cleanup needs its own scope.

This is a repository-retention rule, not permission to skip upstream-required verification, decision trails or reviews during execution. Preserve required notices and substantive findings. The approved PR #55 cleanup removes redundant unmerged evidence without changing the operational skills or the reviewed checkpoint.

## Before delivery

Compare the pinned upstream source with the final jstack files, not only the previous local version. Account for each structural and substantive difference in the skill's attribution/difference record or a linked assessment. Record the upstream path and revision, local location, exact difference, concrete runtime or user requirement, and verification or remaining limitation. Do not treat an old difference as approved merely because it exists.

Keep upstream mappings current for moved files, standalone skills and external dependencies. Preserve source pins and historical review evidence; a packaging correction does not advance the reviewed checkpoint. PR descriptions must state material deviations and their reasons. Static mapping checks detect missing files, not semantic fidelity; inspect the actual instructions.

If a review finds unnecessary drift, restore alignment within the authorized scope or record a concrete unresolved item. Before adding more playbooks, audit existing jstack adaptations against this policy, identify necessary substitutions separately from optional redesign, and resolve material unapproved divergence. Do not label that audit complete based only on this principles correction.

## Current packaging decisions

User decision, 2026-10-15: every shipped skill uses a portable `jstack-` name. `setup-jstack` becomes `jstack-setup`; every other former local name receives the prefix. The user additionally chose `poteto-help` → `jstack-juan-help` on 2026-10-19, matching the `poteto-mode` → `jstack-juan-mode` identity. Keep this naming translation in future adaptations and update all operational callers. Preserve original upstream paths and pins in the manifest. This is an identity change, not permission to redesign procedures or rename configuration role keys. See the [name mapping and migration guide](skill-names.md).

The 24 `jstack-principle-*` skills remain standalone. Juan-mode preserves poteto-mode's inline Principles groups and trigger summaries and discovers the leaf skills through the catalog. There is no separate principle index. Figure-it-out discovers its relevant standalone principles instead of duplicating their bodies. The 23 playbooks remain procedures within juan-mode, matching the upstream boundary.

Generated verification skills automatically get a project-local Claude directory link, regardless of the executing provider. The user explicitly reaffirmed this jstack addition on 2026-10-14; see the [recorded decision](decisions.md#automatic-claude-linking-2026-10-14). Preserve it in future restorations.

This policy does not approve merging, installation, model changes, external messages or schedule changes. Existing task authorization still governs those actions.
