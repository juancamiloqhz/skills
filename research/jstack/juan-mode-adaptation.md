# Juan-mode adaptation research

Current jstack skill identities use the `jstack-` prefix. See the [name mapping and manual migration guide](skill-names.md). Earlier assessments and evaluation artifacts retain their original names; current local links point to the renamed packages.

Reviewed on 2026-10-11 against cached upstream commit `11713c683fe4add4fd403ea880580abbc9e0875f`. This note assesses the source and proposes implementation boundaries. It does not implement or activate a workflow.
Source: [watched repository](upstream.json), [upstream poteto-mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md).

This initial assessment led to the user's request to assess the complete 23-playbook set. The [specification](juan-mode-spec.md) and [roadmap](roadmap.md) now record that accepted target and replace the three-playbook first-release proposal below. The user also chose conversation activation until explicit opt-out. Other initial proposals remain historical design input where the specification resolves them differently.

## Observed upstream behavior

Poteto-mode is a working style and task router. Its 23 playbooks cover investigation, implementation, diagnosis, verification, PR work, autonomous work and session management. The read-only Investigation playbook is one route. The local roadmap proposed investigating that route first; it did not establish the whole scope of juan-mode.
Source: [upstream playbooks](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks), [roadmap](roadmap.md), [naming decision](decisions.md).

The reusable structure is a lead agent that classifies the request, loads the matching playbook, records its steps, applies relevant principles, delegates scoped work, reviews results and verifies the actual output. Feature assigns implementation to a child while the parent owns design and verification. Bug fix requires a reproduced failure and evidence of the cause before implementation. Investigation produces a cited explanation or recommendation without code changes or a PR.
Source: [mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [feature](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/feature.md), [bug fix](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/bug-fix.md), [investigation](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/investigation.md).

Upstream relies on other skills for substantial behavior. The mode names `how`, `why`, `architect`, `arena`, `swarm`, `interrogate`, `figure-it-out`, principle leaves and writing helpers. It also uses Cursor's `Task`, a `poteto-agent` wrapper, Custom Mode support, `/loop` and external plugin control skills. Copying the top-level file would leave those dependencies unresolved.
Source: [mode](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [agent wrapper](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/agents/poteto-agent.md), [mode guide](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/docs/guide/02-poteto-mode.md).

Upstream's broad autonomy grants include team chat and ticket updates. Its PR playbook also prescribes branch resets in some recovery cases and ready PRs. These are source policies to assess, not permissions conferred by reading or adapting the skill. Jstack already separates workflow configuration from execution authority, merges from implementation approval and installations from agent execution.
Source: [upstream autonomy](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [opening a PR](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/opening-a-pr.md), [decisions](decisions.md), [upstream maintenance permissions](upstream-maintenance.md).

## Existing jstack and T3 Code contracts

Setup already defines all 17 model roles. Implementation roles include `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb` and `hardest tasks`; other roles cover investigation, judgment and panels. A consumer must load the current configuration, validate the entire map against the live catalog, then resolve the roles it implements. Missing or stale configuration cannot silently become upstream's default model choices. Effective seat options control effort, and `inherit-parent` omits the delegation target.
Source: [role registry](../../skills/jstack/jstack-setup/scripts/models.py), [configuration contract](../../skills/jstack/jstack-setup/references/configuration.md), [setup discovery and resolution](../../skills/jstack/jstack-setup/SKILL.md).

T3 Code delegation creates parent-owned child work. The current `delegate_task` schema takes an explicit task prompt without copied conversation history, supports provider/model/options targets and returns a task ID. Each review round needs a fresh task with consolidated prior context. Independent top-level conversations require a separate user request. A catalog selection establishes availability in the selector, not successful execution by that provider.
Source: live `mcp__t3_code__delegate_task` and `mcp__t3_code__orchestrator_capabilities` tool descriptions inspected on 2026-10-11; [local integration contract](../../skills/jstack/jstack-setup/references/t3-code.md).

T3 Code provides native PR linking and event-driven watching. `watch_pull_request` wakes the parent on relevant changes and explicitly forbids child-owned watching. A future Babysit route should use this lifecycle instead of importing upstream's watcher process. Its handoff must stop watching when returning responsibility to the user.
Source: live `mcp__t3_code__link_pull_request`, `mcp__t3_code__watch_pull_request` and `mcp__t3_code__unwatch_pull_request` descriptions inspected on 2026-10-11; [upstream PR lifecycle](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/opening-a-pr.md).

Upstream's guide attributes cross-turn continuity to Cursor Custom Mode. Jstack's configuration explicitly is not a persistent system rule. A portable skill with `mode: true` would therefore not establish equivalent T3 Code or cross-provider persistence by itself. A persistent activation promise would need a documented client mechanism and behavior checks for new tasks, opt-out and resumed conversations.
Source: [upstream mode guide](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/docs/guide/02-poteto-mode.md), [configuration consumer contract](../../skills/jstack/jstack-setup/references/configuration.md).

The shipped jstack bundle contains setup and the two verification-skill tools. Verification generation and maintenance are separate operations from running an existing verifier. Their contracts already cover real public interfaces, retained evidence, owned-state cleanup and T3 preview selection. A workflow can reuse that behavior without inventing another verifier or generating one on every task.
Source: [setup](../../skills/jstack/jstack-setup/SKILL.md), [generator](../../skills/jstack/jstack-create-verification-skill/SKILL.md), [maintenance](../../skills/jstack/jstack-maintain-verification-skill/SKILL.md), [release history](roadmap.md).

## Initial implementation proposal

Preserve juan-mode as the entrypoint for the whole working style. Build a compact router and common execution rules, with separate files for each implemented playbook. State supported routes and unresolved dependencies explicitly. Investigation can be an early evaluation case without redefining the skill as an investigation-only product.
Basis: proposed adaptation of the [upstream router](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md) and [local naming decision](decisions.md).

Preserve the principles that change behavior, including evidence before claims, reproduction before fixes, scoped delegation, minimal changes and verification through the real interface. Decide whether a principle belongs in the common rules or a separate reusable skill based on its size and reuse. Do not retain mandatory references to unavailable upstream leaves merely to preserve their names. Resolve independently installed dependencies through the skill catalog, following setup's existing practice.
Basis: proposed adaptation of [upstream principles](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md) and [setup dependency handling](../../skills/jstack/jstack-setup/SKILL.md).

Implement configuration loading and role resolution once, then pass explicit scope, permissions, evidence requirements and review context to delegated work. Reuse the setup helper through a documented dependency or extract shared support deliberately. A separately installed `juan-mode` must not assume `setup-jstack` is its filesystem sibling. Keep current conversation model selection and model configuration unchanged during ordinary workflow execution.
Basis: proposed consumer design under the [configuration contract](../../skills/jstack/jstack-setup/references/configuration.md), [T3 integration](../../skills/jstack/jstack-setup/references/t3-code.md) and [independent installation behavior](../../skills/jstack/jstack-setup/SKILL.md).

Deliver the router and configuration/delegation contract in a focused first change, then prove Investigation, Feature and Bug fix as usable routes. Select the first tested route with the user. Defer the advanced autonomous, stacked-PR and project-coordinator routes until their dependencies and runtime behavior are implemented. Preserve ordinary task authorization throughout; a routed playbook must not silently authorize communications, destructive recovery, merge or installation.
Basis: proposed delivery sequence informed by [upstream playbooks](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks), [delivery decisions](decisions.md) and [configuration permission boundary](../../skills/jstack/jstack-setup/references/configuration.md).

Evaluate observable behavior, not just frontmatter validity. Cases should cover correct routing, a read-only boundary, concrete and inherited model seats, stale configuration rejection, fresh review rounds, unavailable dependencies, a failing-then-passing bug reproduction, blocked verification and an unsupported route. Report the actual coordinating and child providers exercised. Test persistence only if the implementation promises it.
Basis: proposed checks derived from the [consumer contract](../../skills/jstack/jstack-setup/references/configuration.md), [upstream investigation boundary](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/investigation.md), [bug proof](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/bug-fix.md) and [verification outcome contract](../../skills/jstack/jstack-maintain-verification-skill/SKILL.md).

## Initial choices and current resolution

- The target now covers all 23 playbooks, with shared foundations and grouped implementation described in the specification.
- The user chose activation that remains in effect until turned off; persistence requires runtime evidence.
- The specification proposes bundled helper procedures and an explicitly discovered `setup-jstack` resolver dependency.
- Publication follows the user's requested delivery, while merge and installation retain the established boundaries.
- The specification proposes a provider coverage target and names the execution questions that remain unverified.

The accepted scope and activation preference are decisions. Proposed packaging and execution mechanisms still need implementation and evaluation; the saved role map and successful setup tests do not establish runtime support.
Source: [roadmap](roadmap.md), [decisions](decisions.md), [configuration contract](../../skills/jstack/jstack-setup/references/configuration.md).
