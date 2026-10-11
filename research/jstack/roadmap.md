# Jstack roadmap

Status as of 2026-10-11. Model setup, verification tooling and upstream maintenance are released. The next work is the `juan-mode` adaptation specification. The sequence below records the agreed direction; implementation details and release checks remain to be specified.

## Completed: setup-jstack

Model configuration and validation shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with prose formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). Release checks included six helper tests, skill validation, and Markdown linting. Setup was installed for the four selected providers and invoked successfully in a T3 Code session.

Those checks cover setup. They do not establish the behavior of a future workflow consumer.

## Completed: organize research

[PR #4](https://github.com/juancamiloqhz/skills/pull/4) established this research directory and excluded the old experiment archive from the current tree.

## Completed: create-verification-skill

[PR #6](https://github.com/juancamiloqhz/skills/pull/6) added the generator. [Evaluation](evaluations/create-verification-skill/README.md) covered a CLI fixture, independent reuse, failure detection and a documentation-only boundary. Browser and cross-provider execution remain untested. Installation and updates are manual.

## Completed: optional verification offer

[PR #7](https://github.com/juancamiloqhz/skills/pull/7) added the optional offer. After model configuration, `setup-jstack` inspects the target repository for a real application and existing verification support, then offers generation when needed. Acceptance hands off to the separately available generator. A missing generator produces manual installation instructions; declining or a failed generation leaves the saved model configuration intact.

## Completed: maintain-verification-skill

Released in [PR #8](https://github.com/juancamiloqhz/skills/pull/8). Maintain an existing project-local verification skill in place. Review every mapped feature against source, exercise it through the public interface, repair evidenced drift within the skill directory, and report product regressions without weakening expectations. Delivery follows the requested task; invoking maintenance alone does not create a PR. The [evaluation](evaluations/maintain-verification-skill/README.md) records deliberate application changes, a regression, and an unchanged baseline. Installation remains manual.

## Completed: upstream maintenance

Released in [PR #12](https://github.com/juancamiloqhz/skills/pull/12). The [upstream maintenance procedure](upstream-maintenance.md) and manifest support source change detection, complete impact reviews and retained decisions. The [first review](upstream-reviews/2026-10-11.md) covers the manual trial. The weekly review is enabled in the skills project and bound to the [jstack conversation](t3-thread://v1/5f7384b2-cbbe-431f-942d-929f327635a1). Its report delivery and fresh completion receipt were verified on 2026-10-11 before the old lifeOS schedule was deleted. Implementation recommendations require approval, merges remain separate, and installation stays manual.

## Next: specify the juan-mode adaptation

Adapt poteto-mode's working approach through the `juan-mode` entrypoint: shared engineering principles, task routing, scoped delegation, review and verification. The [source assessment](juan-mode-adaptation.md) records upstream behavior and T3 Code integration constraints. Investigation is one playbook within this scope. The earlier investigation-first proposal described a delivery slice, not the whole product.

Write the adaptation specification before implementing the skill. Define the entrypoint and common rules, playbook contracts, configuration loading and role resolution, explicit child context, permission boundaries, verification outcomes and unsupported-route behavior. Reuse the shipped configuration and verification contracts. Map every required upstream dependency to an adapted skill, bundled reference, existing capability or explicitly deferred behavior.

Settle activation for a single request versus later tasks in the conversation, helper-skill packaging, standalone access to the configuration resolver, PR publication defaults and required provider coverage. Cursor's mode metadata alone does not establish persistence in T3 Code. Completion means the specification accounts for these choices and defines observable acceptance checks for the first release.

## Then: implement the entrypoint and first playbooks

The agreed first usable release targets Investigation, Feature and Bug fix. Build in focused PRs: the router and shared configuration/delegation behavior, then complete playbook paths with their required dependencies. Choose the implementation and evaluation order in the specification. A route is supported only when its dependencies and completion checks work.

Investigation produces a cited explanation or recommendation within a read-only scope. Feature covers understanding, design, delegated implementation, review and verification. Bug fix covers reproduction, evidence of the cause, implementation and verification against the original failure. Reuse existing project verification when it covers the task; generation and maintenance remain separate operations.

## Release checks: evaluate observable behavior

Evaluate correct routing, concrete and inherited model assignments, stale configuration rejection, explicit delegation context, fresh review rounds, unavailable dependencies and unsupported routes. Demonstrate that Investigation preserves its read-only scope, Feature verifies the requested behavior, and Bug fix produces failing-then-passing evidence. Incomplete or blocked verification must remain visible in the result.

Record which coordinating and child providers were actually exercised, and test persistence if the specification promises it. Source review and successful setup tests do not prove workflow execution. Merge completed work before installation; the user installs and updates skills manually.

## Later: extend the supported workflows

Assess advanced autopilot, stacked-PR shipping and multi-day project coordination after the everyday playbooks work. Additional upstream workflows and reusable helper skills can follow demonstrated needs. The broad working-style scope does not commit jstack to porting all 23 playbooks or all pstack skills.
