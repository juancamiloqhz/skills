# Readiness Report Contract

Produce one Markdown report in the conversation unless the user explicitly requests a repository file. Keep claims close to their evidence and use tables where repeated comparisons benefit from them.

## Required Sections

### 1. Executive Assessment

State the repository's readiness, the major structural recommendation, the most consequential risks, and the proposed migration order.

### 2. Audit Coverage

List the revision, remotes, tracker, access limitations, major paths and documentation inspected, and any coverage that remains incomplete.

### 3. System and Domain Topology

Describe runtime and dependency boundaries, candidate bounded contexts, their evidence, and their relationships. Include glossary candidates and ambiguous terminology.

### 4. Domain Documentation Decision

Recommend `CONTEXT.md` or `CONTEXT-MAP.md`. Show the proposed document paths and the responsibility of each document. For a context map, include every important inter-context relationship.

### 5. ADR Candidate Matrix

Use these columns:

| Candidate | Classification | Evidence | Rationale confidence | Current status | Recommendation |
| --- | --- | --- | --- | --- | --- |

Keep confirmed history, current constraints, and new proposals visibly distinct.

### 6. Documentation and Agent-Instruction Findings

Inventory drift, contradictions, missing material, duplication, dead links, obsolete instructions, and proposed sources of truth.

### 7. Tracker Findings

When tracker access exists, include:

- label inventory and exact migration map;
- milestone and project-board findings;
- one migration recommendation for every open issue;
- template and automation findings;
- historical issues that should remain untouched and why.

### 8. Setup Inputs

State the recommended downstream configuration explicitly:

```text
Issue tracker:
Canonical triage label strings or mappings:
Domain layout: single-context | multi-context
Root agent-instruction file to update:
Context and ADR paths:
```

### 9. Migration Plan and Approval Gates

Order the smallest coherent phases. Separate at least:

- workflow scaffolding;
- context and ADR authoring;
- documentation cleanup;
- tracker migration;
- validation.

Name the user decisions and external mutations that require approval before each phase.

### 10. Risks and Open Questions

Include only questions whose answers could materially change the layout, ADRs, tracker migration, or implementation order. Recommend an answer when the evidence supports one.

## Completion Criteria

Before presenting the report, verify that:

- each applicable repository-audit area is represented or marked inaccessible;
- each context and ADR recommendation cites evidence and confidence;
- every open issue has a row when tracker access exists;
- every proposed label has a clear workflow role;
- observed, inferred, and proposed claims remain distinguishable;
- the setup-input block is complete enough for the downstream setup workflow;
- the report stops before repository or tracker mutation.
