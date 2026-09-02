---
name: agent-instructions
description: Audit, create, or repair repository AGENTS.md and CLAUDE.md files using repository evidence and actual Codex or Claude loading behavior. Use for persistent coding-agent instructions; not for SKILL.md or broad workflow-readiness audits.
---

# Agent Instructions

Treat persistent agent instructions as a routing and policy layer, not a repository encyclopedia. Keep always-loaded files small enough to remain useful, but retain explicit guardrails that repository evidence or the user shows are important.

## Modes

Infer the mode from the request:

- **Audit**: inspect and report. Do not edit files.
- **Propose**: show a replacement, patch, or file plan. Do not edit files.
- **Apply**: create or edit files when the user explicitly asks to create, fix, update, refactor, rewrite, or otherwise change them.

An audit may recommend changes, but a request to "audit" or "review" alone does not authorize them. In Apply mode, make the requested in-scope edits without asking for another confirmation. Pause only when a material policy choice or contradiction cannot be resolved from repository evidence.

Default to repository-owned instructions. Keep global, home-directory, private local, and session-history sources outside the audit unless the user explicitly includes them.

## Workflow

1. Establish the repository root, the working directories whose behavior matters, the target harnesses, and the mode.
2. Discover all relevant instruction carriers and their evidence: `AGENTS.md`, `AGENTS.override.md`, configured fallback files, `CLAUDE.md`, `CLAUDE.local.md`, `.claude/CLAUDE.md`, `.claude/rules/`, referenced documentation, repository configuration, and executable checks.
3. If Python is available, run the bundled `scripts/inventory_agent_instructions.py --root <root> --cwd <cwd>` for each materially different working directory. Resolve the script path from this skill's directory. Treat its output as discovery evidence, not a complete semantic audit.
4. Compute what each harness actually loads. Read [references/harness-loading.md](references/harness-loading.md) whenever there is more than one instruction level, an override, fallback name, import, scoped rule, both Codex and Claude, or a context-size concern.
5. Read [references/audit-rubric.md](references/audit-rubric.md). Test every material instruction against repository evidence and assign a disposition. Never grade solely from file length or a universal template.
6. Report the effective loading behavior and highest-impact findings before proposing mutations. Separate observed facts, inferences, and user-owned policy.
7. In Apply mode, read [references/change-workflow.md](references/change-workflow.md), form a file plan, and make the smallest coherent change. Prefer one source of truth over duplicated `AGENTS.md` and `CLAUDE.md` content.
8. Validate the result: rerun discovery, resolve local references, recompute loading chains, check the Codex byte budget, and run only safe, relevant repository checks.

## Completion Gate

Do not call the work complete until:

- every material instruction has an evidence-backed disposition;
- every affected harness and working-directory chain has been modeled;
- every retained pointer or import resolves and states when it matters;
- contradictions and unresolved policy choices are explicit;
- any changed files have been re-audited in their effective loaded form;
- the final response distinguishes changes made, recommendations not applied, and validation performed.

## Boundaries

- Keep repository preferences repository-specific rather than promoting them to universal best practices.
- Route enforceable formatting, linting, and test policy to configuration, hooks, or CI when those mechanisms can own it.
- Keep specialized procedures behind a root-level trigger that states when to load them.
- Preserve emphatic or absolute guardrails until evidence shows whether they encode a costly past failure.
- Route `SKILL.md` review to a skill-authoring or writing-for-agents workflow.
- Keep architecture, domain-model, ADR, documentation-drift, and issue-tracker readiness in a broader audit unless the user includes them.
