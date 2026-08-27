# Repository and Domain Audit

Use this reference for architecture, documentation, domain modeling, ADR archaeology, and agent-readiness coverage.

## Coverage Map

Account for every applicable area and record what was inspected:

- top-level structure, applications, packages, shared tooling, and dependency direction;
- runtime entrypoints, user-facing flows, background jobs, events, and external integrations;
- data stores, schemas, ownership, authorization boundaries, and cross-boundary transactions;
- build, test, CI/CD, deployment, environment, and operational configuration;
- root and package READMEs, feature and reference docs, roadmaps, diagrams, and links;
- `AGENTS.md`, `CLAUDE.md`, installed repository skills, and other durable agent instructions;
- tests, configuration, and focused Git history that explain or contradict documented behavior.

Prefer targeted repository search and dependency tracing over reading files in arbitrary order. Follow important execution paths far enough to identify ownership, invariants, and coupling.

## Domain Topology

Extract the language the system uses:

- actors and their goals;
- core nouns, commands, events, and lifecycle states;
- business rules and invariants;
- data and policy ownership;
- workflows that cross ownership boundaries;
- overloaded, synonymous, or ambiguous terms.

Propose a bounded context only when the evidence shows a meaningful boundary in language, invariants, ownership, lifecycle, or change pressure. Applications, packages, services, and folders are supporting evidence, not automatic contexts.

For each candidate context, report:

| Field | Question |
| --- | --- |
| Purpose | What business or system capability does it own? |
| Language | Which terms have a stable meaning inside it? |
| Invariants | Which rules must it protect? |
| Data | Which records or state does it own? |
| Interfaces | How do other contexts interact with it? |
| Evidence | Which files, flows, issues, or history support the boundary? |
| Confidence | High, medium, or low, and why? |

## Context Layout Decision

Recommend a root `CONTEXT.md` when one coherent model, vocabulary, and decision body describes the repository without hiding material differences.

Recommend a root `CONTEXT-MAP.md` plus per-context `CONTEXT.md` files when several contexts have distinct language, invariants, ownership, or integration relationships. A monorepo is a reason to investigate multi-context structure, not proof that it is needed.

For a context map, define:

- every context and its documentation path;
- upstream, downstream, shared-kernel, translation, or external-system relationships where useful;
- the important commands, events, APIs, or data that cross each boundary;
- unresolved ownership or coupling risks.

## Decision Archaeology

Search existing ADRs, documentation, focused Git history, issues, tests, configuration, comments, and implementation seams for decisions with lasting architectural consequences.

Classify each ADR candidate:

- **Confirmed historical decision:** evidence establishes both the decision and meaningful rationale.
- **Current architectural constraint:** implementation establishes the constraint, while historical rationale remains uncertain.
- **Proposed decision:** the audit exposes a choice that has not yet been made explicitly.

Record the evidence and confidence separately from the proposed ADR title. Preserve uncertainty instead of inventing a retrospective rationale.

## Documentation Drift

Find contradictions, obsolete commands, renamed paths, inaccurate architecture, dead links, duplicated sources of truth, stale roadmap items, and detailed examples that are likely to decay. Recommend one authoritative home for each meaning.

Distinguish documentation that should be:

- corrected;
- consolidated or linked;
- converted into a context document or ADR;
- removed because the implementation or tracker is authoritative;
- retained as historical material with explicit status.

## Agent Readiness

Evaluate whether durable agent instructions are scoped, current, and navigable. Flag conflicting files, duplicated rules, stale inventories, volatile issue tables, missing pointers, and instructions that conceal rather than clarify the repository's domain model.

Keep repository-specific facts in repository documentation. Keep reusable procedures in skills.
