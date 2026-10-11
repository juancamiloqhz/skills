# Route registry

Select by requested deliverable, not merely a matching word. All 23 routes below are **planned** in this foundation build. None has an executable playbook yet. Report the selected route and this limitation before workflow dispatch or mutation. Registry membership does not establish support.

| Route | Requested outcome | Boundary or distinction |
| --- | --- | --- |
| `investigation` | Explain behavior or recommend an approach from evidence. | Read-only; a question does not authorize implementation. |
| `bug-fix` | Reproduce and repair a reported defect. | Verify against the original failure. |
| `perf-issue` | Diagnose and fix measured slowness. | One bounded performance problem with a baseline. |
| `hillclimb` | Improve a metric through repeated measured experiments. | Sustained iteration toward an explicit target. |
| `runtime-forensics` | Diagnose a symptom using live runtime evidence. | Diagnosis only; instrumentation needs appropriate scope. |
| `trace-forensics` | Diagnose an already captured trace or profile. | Diagnosis only; preserve the supplied artifact. |
| `feature` | Add or change behavior. | Scope implementation to the requested behavior. |
| `refactoring` | Change structure while preserving behavior. | Verify the preserved behavior. |
| `prototype` | Resolve a design question with a disposable experiment. | Keep the experiment separate from production changes. |
| `visual-parity` | Match a target interface's appearance. | Requires real visual evidence. |
| `authoring-a-skill` | Create or modify a skill package. | Validate the package and exercise its behavior. |
| `eval` | Measure the effect of a skill, prompt or agent change. | Isolate candidates and judge only observable evidence. |
| `opening-a-pr` | Publish a requested change for review. | Opening a PR does not start monitoring or authorize merge. |
| `babysit` | Assess or drive a PR toward readiness. | Derive read-only status versus repair scope from the request. |
| `shipping` | Verify and land an authorized PR or stack. | Land only the contiguous verified portion within merge authority. |
| `multi-phase-plan` | Produce a plan spanning phases or PRs. | Planning alone does not authorize executing the plan. |
| `session-pickup` | Reconcile prior work and resume its next step. | Verify inherited claims against current artifacts. |
| `pause-safely` | Suspend current work with a recoverable handoff. | Reconcile owned child work; preserve user changes. |
| `worktree-cleanup` | Assess disk use and remove authorized disposable checkouts. | Inventory first; untracked files and closed PRs are not proof of safety. |
| `autonomous-run` | Continue one bounded task until its exit condition holds. | Does not create recurring scheduled work. |
| `orchestrate` | Coordinate an ongoing program across tasks and PRs. | Requires durable ownership and recovery beyond one task. |
| `autopilot-full` | Build, verify and land a queue of independent changes. | Requires explicit landing authority and respects named holds. |
| `autopilot-stack` | Build and verify a linear PR stack for the user to land. | The deliverable excludes merging. |

For overlapping requests, retain the requested boundary. A diagnosis with an explicit later fix has a diagnosis phase followed by a repair route. A pause or stop applies immediately to ongoing work. A PR status question selects Babysit in assessment scope; merely creating a PR does not. A plan request remains planning even when it describes a large implementation.

Once playbooks exist, mark a route implemented only after its dependencies, permitted actions and acceptance evidence are available. Add its actual playbook path then. Custom workflow composition remains unavailable until the shared planning procedure is implemented; do not substitute an upstream helper that happens to be installed.
