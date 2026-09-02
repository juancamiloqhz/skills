# Research: an `AGENTS.md` / `CLAUDE.md` audit-and-improve skill

_Research snapshot: 2026-08-30. Install and GitHub-star counts are volatile and are included only as adoption signals, not quality scores._

## Conclusion

The proposed skill is worth building, but the category is not empty. Matt Pocock does **not appear to publish an exact audit-and-fix skill** in [`mattpocock/skills`](https://github.com/mattpocock/skills). His [`writing-for-agents`](https://www.skills.sh/mattpocock/skills/writing-for-agents) skill supplies the writing philosophy, while [`setup-matt-pocock-skills`](https://www.skills.sh/mattpocock/skills/setup-matt-pocock-skills) scaffolds adjacent documentation and reads an existing agent-instructions file without auditing its quality.

Several exact or near-exact implementations already exist. The strongest opportunity is therefore not a literal reimplementation of Matt's article. It is a **tool-aware, evidence-backed auditor** that:

- computes what Codex and Claude actually load;
- verifies instructions against the repository;
- decides whether each item belongs inline, in a nested file, a linked document, a skill, enforcement tooling, or local/user configuration;
- reports contradictions and proposed dispositions before editing; and
- applies and validates minimal changes only when requested.

This also fits beside this repository's existing [`agent-workflow-readiness`](../skills/agent-workflow-readiness/SKILL.md) skill. That skill performs a broad, read-only readiness audit; a new skill can own the narrower inspect/propose/apply workflow for `AGENTS.md` and `CLAUDE.md`.

## What Matt's two articles contribute

### 1. Keep the always-loaded file small and route to deeper context

In [A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md), Pocock argues that a root file should contain only universally relevant, non-obvious instructions. His illustrative minimum is a short project description plus unusual package-manager, build, test, or type-check commands. Large generated inventories and stale file trees consume context and can mislead the agent.

The durable principle is **progressive disclosure**: keep high-frequency guidance inline and route specialized knowledge to nested instruction files, documentation, or skills. The useful audit sequence is: detect contradictions, extract root essentials, group the remainder by concern, move it to an appropriate carrier, link it clearly, and flag redundant, vague, stale, or obvious material.

This should be treated as a heuristic rather than a mandatory template. A security-sensitive or unusual repository can justify more root guidance; a conventional repository may need almost none.

### 2. Concise planning is a separate, conditional preference

In [My AGENTS.md File For Building Plans You Actually Read](https://www.aihero.dev/my-agents-md-file-for-building-plans-you-actually-read), Pocock describes a plan/execute/test/commit loop and recommends making plans extremely concise and ending them with unresolved questions.

That is a useful optional rule, but it is not automatically repository knowledge. The auditor should normally recommend it for a user-level configuration or a planning skill unless the whole team explicitly wants that planning style. If shared, a less brittle form is: “Keep plans concise and scannable; end with unresolved questions, or state that there are none.”

## Matt's existing skills

| Skill | Relationship to the proposal | Adoption snapshot |
|---|---|---:|
| [`writing-for-agents`](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/writing-for-agents/SKILL.md) | Strong conceptual foundation. Covers information hierarchy, progressive disclosure, context versus cognitive load, actionable steps and completion criteria, positive wording, single sources of truth, and pruning no-ops. It triggers when editing `AGENTS.md` or `CLAUDE.md`, but it is not a repository-verifying audit workflow. | Large adoption; the renamed skill's registry count is split from its former `writing-great-skills` identity. Parent repo ~20.5K stars. |
| [`setup-matt-pocock-skills`](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/setup-matt-pocock-skills/SKILL.md) | Adjacent setup skill. Scaffolds issue-tracker, triage, domain-documentation, and skill pointers and can read an existing instruction file. It does not grade, refactor, or validate that file. | ~734–736K installs; same repository |

A repository-tree and code search found references to agent-instructions files in these and a few other workflow skills, but no dedicated “audit `AGENTS.md` / `CLAUDE.md`, propose a report, then safely fix it” skill.

## Comparable skills

### Strong candidates

| Source | Match | What to borrow | Caveat | Adoption / license snapshot |
|---|---|---|---|---|
| Anthropic, [`claude-md-improver`](https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/plugins/claude-md-management/skills/claude-md-improver/SKILL.md) and its [quality criteria](https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/plugins/claude-md-management/skills/claude-md-improver/references/quality-criteria.md) | Exact for `CLAUDE.md` | Discovery, weighted quality report, targeted diffs, confirmation before update | A fixed rubric can reward bloat or penalize a global/user file for correctly omitting architecture and commands. An [open issue](https://github.com/anthropics/claude-plugins-official/issues/1476) illustrates scope-sensitive scoring problems. Use N/A-aware checks instead. | Official Anthropic repo; ~10.3K installs; ~35K stars; Apache-2.0 |
| Sentry, [`agents-md`](https://raw.githubusercontent.com/getsentry/skills/main/skills/agents-md/SKILL.md) and [spec](https://raw.githubusercontent.com/getsentry/skills/main/skills/agents-md/SPEC.md) | Exact create/maintain skill | Verify commands and paths; link instead of copy; remove duplication; retain a concise root; support both file names | Its numerical line limits are useful diagnostics, not universal pass/fail criteria. | ~5.0K installs; ~962 stars; Apache-2.0 |
| softaworks, [`agent-md-refactor`](https://www.skills.sh/softaworks/agent-toolkit/agent-md-refactor) | Exact and directly based on Pocock's refactor idea | Contradiction detection, root essentials, concern grouping, deletion report, reference validation | It is the popular direct article-derived precedent, so a new skill needs a clearer differentiator. | ~4.0K installs; ~2.4K stars; MIT |
| mblode, [`agents-md`](https://raw.githubusercontent.com/mblode/agent-skills/main/skills/agents-md/SKILL.md) with [quick checklist](https://raw.githubusercontent.com/mblode/agent-skills/main/skills/agents-md/references/quick-checklist.md), [full criteria](https://raw.githubusercontent.com/mblode/agent-skills/main/skills/agents-md/references/quality-criteria.md), and [refactor workflow](https://raw.githubusercontent.com/mblode/agent-skills/main/skills/agents-md/references/refactor-workflow.md) | Closest feature-complete exact match | Setup/audit/refactor modes; quick versus full audit; minimal diffs; command smoke tests; link validation; conflict checks; before/after report | Lower adoption means the design is less battle-tested. Its [`LICENSE.md`](https://github.com/mblode/agent-skills/blob/main/LICENSE.md) is MIT, but reuse concepts and independently written instructions rather than copying wholesale. | ~464 installs; ~95 stars; MIT |
| mcollina, [`init`](https://raw.githubusercontent.com/mcollina/skills/main/skills/init/SKILL.md) | Exact-ish optimizer | Excellent “discoverability filter”: retain only non-discoverable, operationally significant, actionable facts; prefer fixing root causes in tooling | Broader repository initialization scope | ~1.0K installs; ~1.9K stars; MIT |
| daymade, [`claude-md-progressive-disclosurer`](https://raw.githubusercontent.com/daymade/claude-code-skills/main/daymade-claude-code/claude-md-progressive-disclosurer/SKILL.md) | Strong restructuring match | Classify signal versus anti-signal; choose a carrier; move content before compressing it; validate coverage; line count is not the KPI | Its “zero information loss” posture may preserve noise. Claude imports organize content but do not defer it. | ~848 installs; ~1.4K stars; MIT |
| ykdojo, [`review-claudemd`](https://raw.githubusercontent.com/ykdojo/claude-code-tips/main/skills/review-claudemd/SKILL.md) | Adjacent, behavior-informed audit | Inspect recent sessions for repeatedly missed or absent instructions and stale guidance | Session-history inspection should be an explicit privacy-sensitive opt-in. The repo is **All Rights Reserved**; copy no text or implementation. | ~229 installs; ~10.0K stars; proprietary |

### Lower-confidence or narrower examples

- [`richtabor/agent-skills:review-agents-md`](https://raw.githubusercontent.com/richtabor/agent-skills/main/skills/review-agents-md/SKILL.md) is a direct implementation of Pocock's article. It had only ~46 installs and ~70 stars, and no license was detected. It is evidence that the obvious version already exists, but not a safe copying source.
- [`AI-Builder-Club/skills:agent-context-audit`](https://raw.githubusercontent.com/AI-Builder-Club/skills/main/skills/agent-context-audit/SKILL.md) audits the wider context ecosystem—agent files, skills, MCP, and docs. Its cross-layer conflict and “unknown knowns” ideas are useful, but it had ~17 installs and no detected license.
- `vr1e/claude-md-audit` was an exact but negligible-adoption example (~4 installs, 0 stars). It adds little evidence to the design.

## Loader semantics the audit must model

A generic “nearest file wins” model is not enough. The skill should identify the target harness and compute its actual effective instruction set.

### Codex

Official [Codex `AGENTS.md` documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) describes an instruction chain assembled once for a run:

- In the global Codex directory, `AGENTS.override.md` takes priority over `AGENTS.md`, and Codex uses the first non-empty candidate.
- From the project root down to the current working directory, each directory contributes at most one file, using override, standard, then configured fallback names.
- Files are concatenated root-to-working-directory, so closer instructions appear later and can override earlier ones.
- Discovery stops at the working directory. A nested file elsewhere is not loaded merely because a file in that subtree is later touched.
- The combined project instructions are capped by `project_doc_max_bytes` (32 KiB by default), so late content can be truncated.

Codex [skills](https://learn.chatgpt.com/docs/build-skills) provide genuine progressive disclosure: the initial context contains skill metadata; the full `SKILL.md` is read only when selected. This makes a skill the right carrier for reusable, conditional procedures.

### Claude Code

Official [Claude Code memory documentation](https://code.claude.com/docs/en/memory) distinguishes user, project, local, and nested scopes:

- `CLAUDE.md` content is loaded at launch; concise, specific, structured guidance is recommended.
- Child `CLAUDE.md` files are discovered on demand when Claude works in their subtree.
- `@path` imports are expanded at launch (up to five hops in the current documentation). Imports improve organization but do **not** save context.
- `.claude/rules/` can be path-scoped; skills are on-demand and are better for workflows that should not be always active.
- Claude does not natively read `AGENTS.md`. A project can import it from `CLAUDE.md` or use a symlink. An import permits a Claude-specific addendum; symlinks may be awkward on Windows.

Claude's [best-practices guide](https://code.claude.com/docs/en/best-practices) recommends treating the file like code: prune it and test whether it changes behavior.

The open [`AGENTS.md` standard](https://agents.md/) deliberately imposes no required headings. Nested files scope guidance to subprojects. Therefore, the proposed audit should check behavior and applicability rather than enforce a universal document shape.

## Research evidence and implications

The empirical evidence is useful but mixed:

- The 2026 preprint [Configuration Smells in Agent Configuration Files](https://arxiv.org/html/2606.15828) found at least one smell in 91 of 100 popular repositories. Its six categories—context bloat, skill leakage, lint leakage, blind references, initialization fossilization, and conflicting instructions—map well to audit checks. Automated conflict detection had only 57% precision, so contradictions require human confirmation.
- [Do Context Files Help Coding Agents?](https://arxiv.org/html/2607.27250) found no measurable correctness improvement in a small Claude/Codex evaluation, but did find a process benefit: a warning about a very slow full test suite reduced blind full-suite runs and time. The strongest content is therefore non-obvious operational cost, safety, and workflow guidance—not generic coding advice.
- [The Impact of AGENTS.md on AI Coding Agent Efficiency](https://arxiv.org/html/2601.20404) associates `AGENTS.md` with lower median runtime and fewer output tokens at comparable completion across ten repositories. This is encouraging but observational; the skill should promise better routing and lower instruction risk, not guaranteed code correctness.

## Recommended skill design

Chosen name: `agent-instructions` (the research working name was `agent-instructions-audit`).

### Modes

1. **Audit** — read-only default; inventory sources, compute effective loading, verify claims, and report findings.
2. **Propose** — show a reviewable file plan and patch without applying it.
3. **Apply** — make minimal, user-authorized edits, then validate references and safe commands.

### Workflow

1. Detect the target harnesses and in-scope working directories.
2. Inventory `AGENTS.md`, overrides/fallbacks, `CLAUDE.md`, imports, rules, skills, and the documents they reference.
3. Render the effective instruction chain for each relevant harness and directory; flag precedence conflicts, truncation, duplicated content, and portability gaps.
4. Verify paths and commands against manifests, CI, configuration, and repository state. Safely smoke-test only when authorized and proportionate.
5. Assign each instruction an evidence-backed disposition:
   - keep inline;
   - rewrite;
   - move to a linked document;
   - move to a nested/path-scoped file;
   - move to a skill;
   - enforce with a linter, hook, CI, or configuration;
   - move to user/local scope;
   - delete;
   - user decision required.
6. Report before editing: effective-load map, findings with file/line/evidence/severity/disposition, unresolved choices, and proposed diff/file plan.
7. Apply minimal changes. When moving content, retain an old-to-new trace; avoid moving and aggressively compressing in the same operation.
8. Validate links, loading behavior, context-cap exposure, and relevant commands. Show before/after bytes and line counts as diagnostics, not success criteria.

### Rubric

Use applicable checks and severities rather than a universal numerical grade:

- correctness and currency;
- conflicts, precedence, and effective scope;
- universal relevance versus conditional concern;
- discoverability from code/configuration;
- actionability, triggers, and completion criteria;
- reference quality: what to read, when, and why;
- correct carrier and enforceability;
- harness portability and context-cap risk;
- the six research-backed configuration smells.

If a score is offered, display the applicable denominator and all N/A decisions. Do not reward a document for adding architecture, commands, or sections it does not need.

### Optional extension

Offer a separate, opt-in behavior audit that examines recent local agent sessions for frequently violated guidance or repeated missing rules. Explain exactly what history is read and keep findings local. This borrows only the high-level idea from ykdojo's proprietary skill.

## Reuse and licensing guidance

The safest approach is an independently written synthesis with citations:

- Pocock's articles are source material to summarize and credit, not copy at length. His skills repository is MIT.
- Anthropic and Sentry are Apache-2.0; softaworks, mcollina, mblode, and daymade are MIT. Direct reuse requires satisfying the applicable notice and license terms.
- ykdojo is All Rights Reserved. Richtabor and AI Builder Club had no detected license. Use only general, independently implemented ideas from these sources.

The proposed skill's distinctive value should be its loader simulation, repository verification, carrier-placement decisions, contradiction approval, and post-fix validation—not copied wording or a larger checklist.
