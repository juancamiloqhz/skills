# Issue-Tracker Audit

Use this reference when the repository has GitHub Issues, GitLab Issues, local issue files, or another configured work tracker. Adapt the mechanics to the tracker while preserving the audit outcomes.

## Inventory

Inspect the current:

- labels and their descriptions, colors, overlaps, and actual usage;
- open issues individually, including labels, milestone, project state, dependencies, and specification quality;
- closed issues sufficiently to understand historical conventions without rewriting history by default;
- milestones, including dates, completion state, stale scopes, and unassigned work;
- project boards and the coverage of open issues;
- issue and pull-request templates, forms, automation, and contribution guidance.

Report inaccessible tracker surfaces explicitly. Do not infer an empty project or missing label from an incomplete API response.

## Matt Pocock Workflow Compatibility

When compatibility with `setup-matt-pocock-skills` and `triage` is the target, compare the tracker with these five canonical triage roles and default strings:

| Role | Default label |
| --- | --- |
| Needs initial classification | `needs-triage` |
| Needs information before routing | `needs-info` |
| Ready for autonomous agent work | `ready-for-agent` |
| Ready for human judgment or action | `ready-for-human` |
| Intentionally declined | `wontfix` |

Recommend the default strings unless an established tracker vocabulary justifies an explicit role mapping. These are workflow-state labels; retain useful type, area, platform, priority, risk, and release labels as independent dimensions.

For every current label, propose exactly one action:

- keep;
- rename;
- merge into another label;
- map to a canonical triage role;
- deprecate after removing or replacing its active uses.

Include affected open issues and collision risks. Avoid blind bulk conversion based only on similarly worded labels.

## Open-Issue Review

Give every open issue a target disposition. Check whether it has:

- one clear outcome and current motivation;
- acceptance criteria that describe observable completion;
- appropriate type, area, priority, and triage state;
- dependencies, blockers, milestone, and project state where applicable;
- stable references to repository documentation rather than large volatile code snapshots;
- scope small enough for the intended agent or an explicit decomposition recommendation.

The migration report must include a row for every open issue, even when the recommendation is “no change.”

## Mutation Boundary

Produce proposed commands or API operations only when they make the migration unambiguous. Keep the audit read-only. Apply label changes, issue edits, project moves, milestone changes, and template updates only in the separately approved migration phase.
