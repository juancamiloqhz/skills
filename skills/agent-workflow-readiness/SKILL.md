---
name: agent-workflow-readiness
description: "Audit a software repository before adopting Matt Pocock's engineering skills or another agent-first workflow. Use for readiness work spanning architecture, domain contexts, CONTEXT.md versus CONTEXT-MAP.md, ADRs, agent instructions, documentation drift, and issue-tracker migration. Produces an evidence-backed, read-only migration plan; use a setup or implementation workflow for the approved changes."
---

# Agent Workflow Readiness

Audit deeply enough that workflow configuration follows the repository's actual architecture and operating history. Make current-state understanding, uncertainty, and migration consequences explicit.

## Operating Boundary

Operate in read-only mode through the readiness report. Reserve repository edits, tracker mutations, setup-skill invocation, and visibility or configuration changes for a separately approved migration phase.

Inspect the configured tracker when access is available. If it is inaccessible, identify the missing coverage and keep tracker-dependent conclusions provisional.

## Investigation

1. Establish the repository root, current revision, remotes, tracker, agent instructions, and major workspace boundaries.
2. Read [repository-audit.md](references/repository-audit.md) and complete every applicable coverage area.
3. When the repository uses an issue tracker or the requested workflow depends on one, read [tracker-audit.md](references/tracker-audit.md) and inspect its current state.
4. Cross-check documentation, implementation, tests, configuration, history, and tracker records. Treat contradictions as findings rather than choosing a convenient source silently.
5. Read [readiness-report.md](references/readiness-report.md) and synthesize one report that satisfies its completion criteria.

For a substantial repository, use parallel agents when available for these bounded, read-heavy workstreams:

- architecture and domain topology;
- documentation and decision archaeology;
- issue-tracker workflow.

Keep every workstream read-only. The primary agent owns coverage, evidence reconciliation, architectural judgment, and the final recommendation.

## Evidence Standard

Classify material conclusions as:

- **Observed:** directly supported by current files, configuration, history, or tracker state.
- **Inferred:** the strongest explanation of observed evidence, with uncertainty stated.
- **Proposed:** a new decision for the user to approve.

Cite repository paths, revisions, issue numbers, and tracker resources close to the claims they support. Record missing or conflicting evidence. A directory boundary alone is not evidence of a domain boundary, and current code alone is not evidence of historical rationale.

## Completion Gate

Finish only when the report:

- accounts for every applicable audit area and identifies inaccessible coverage;
- recommends `CONTEXT.md` or `CONTEXT-MAP.md` from domain evidence;
- separates confirmed decisions, inferred constraints, and proposed ADRs;
- includes an exact tracker migration plan and a recommendation for every open issue when tracker access exists;
- supplies the concrete inputs needed by the downstream setup workflow;
- ends at explicit approval checkpoints before any mutation.

Present the report and discuss the decisions with the user. Continue into setup or migration only after the user approves that next phase.
