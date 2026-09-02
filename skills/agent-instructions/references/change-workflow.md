# Change Workflow

Use this reference in Propose and Apply modes after completing the evidence-backed audit.

## Preserve Policy Ownership

- Preserve explicit user and repository policy unless it is impossible, unsafe, internally contradictory, or explicitly in scope for reconsideration.
- Do not convert a generic recommendation into repository policy without evidence.
- Treat planning-format and communication-style preferences as shared repository policy only when the team has chosen them; otherwise route them to a user-level instruction or a planning skill.
- When two active instructions conflict and repository evidence does not resolve them, describe the concrete behavioral choice and ask the owner.
- Keep strong wording when it encodes a demonstrated costly failure. Improve its scope or testability without silently weakening it.

## Form a File Plan

Before drafting or patching, assign each instruction to a destination and explain why that carrier is appropriate. Prefer:

- root entrypoints for universal policy and routing;
- nested or scoped instructions for subtree behavior;
- ordinary documentation for detailed knowledge, paired with a trigger;
- skills for specialized repeatable procedures;
- executable configuration for deterministic enforcement;
- deletion for stale or behaviorally empty content.

Choose one source of truth for shared Codex/Claude policy. Do not duplicate whole files when an import, symlink, or small native entrypoint will work.

## Choose the Change Size

Use a targeted patch when the current structure is sound and findings are localized. Use a coherent rewrite when precedence, duplication, or organization is fundamentally misleading. Preserve useful repository-specific content either way.

When moving content:

1. create or verify the destination;
2. leave a concise pointer that states the trigger for reading it, if routing is needed;
3. update links and imports;
4. verify the effective loaded form, not only each file in isolation.

Avoid combining a major relocation with aggressive semantic compression unless both are needed and the evidence is clear; otherwise it becomes difficult to tell whether behavior was preserved.

## Creating Files from Scratch

Inspect the repository before drafting. A near-empty instruction file can be correct when the repository is self-describing and automated checks own its constraints. Do not fill a universal template merely to create sections.

Candidate root content must earn its always-loaded cost by being broadly applicable and behavior-changing. Typical justified content includes:

- unusual authoritative commands or package boundaries;
- essential safety or approval constraints;
- routing to specialized documentation with explicit triggers;
- completion requirements that are not already enforced;
- recurring non-obvious failure modes supported by evidence.

State uncertain conventions as proposals or questions rather than facts.

## Validate After Changes

- Re-inventory instruction files and local references.
- Recompute the effective Codex chain for every relevant working directory.
- Recompute Claude launch candidates, imports, subtree instructions, and scoped rules.
- Confirm shared-policy single-source-of-truth behavior in both harnesses.
- Check the effective Codex project instruction bytes against the configured limit or documented default.
- Run focused lint, formatting, or tests only when relevant to changed executable files.
- Review the final diff for accidental policy changes, lost guardrails, duplicate instructions, and unrelated edits.

Report what changed, what intentionally remained, any decisions deferred to the owner, and the exact validation performed.
