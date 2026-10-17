# Engineering playbook inventory

Assessed on 2026-10-11 at upstream commit `11713c683fe4add4fd403ea880580abbc9e0875f`. This inventory covers nine complete playbooks and the shared helpers listed below. Adaptations and acceptance scenarios are design proposals, not implemented or executed workflows.

Source: [upstream router](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md).

## Shared dependencies and adaptation rules

`how` has a simple path with one explainer and a complex path with two to four explorers followed by an explainer. Preserve traced entry points, boundaries, source references and admitted gaps. `why` adds historical evidence, seven evidence categories and explicit confidence levels. Preserve missing-category reporting while discovering available tools through T3 Code and its providers. Git history can work without external connectors; PR discussion needs reachable source hosting. Read in full: both `SKILL.md` files, `how/references/{explorer-prompt,explainer-prompt}.md` and `why/references/{epistemics,source-playbook,investigator-prompt,synthesizer-prompt}.md`.

Sources: [how](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/how/SKILL.md), [why](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/SKILL.md), [confidence contract](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/why/references/epistemics.md).

`architect` calls `arena` for competing designs; `arena` owns isolated candidates, a rubric, one cross-judge, selection, integration and verification. `interrogate` returns a reviewed verdict without automatically applying changes. Preserve these distinct responsibilities. A composed Feature call needs an explicit design-only return from `architect`, because its standalone workflow also includes implementation. Reuse current grounding evidence rather than recursively repeating `how`. Read in full: these three `SKILL.md` files, `architect/references/{runner-prompt,design-red-flags,rationale-template}.md` and `interrogate/references/{reviewer-prompt,lead-judgment,rubric,code-quality-review}.md`.

Sources: [architect](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/architect/SKILL.md), [arena](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/arena/SKILL.md), [interrogate](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/interrogate/SKILL.md).

Proposed role mappings below use jstack's existing 17-role registry. Validate the complete configuration against the live catalog before dispatch, preserve seat order/options and inherited targets, and fail on stale selections instead of adopting upstream fallback models. `architect runners` and `interrogate reviewers` can each contain one inherited seat. Upstream nevertheless requires two distinct design candidates and describes review diversity as its source of adversarial signal. The specification must resolve these cases explicitly; neither silently increasing configured fan-out nor describing one-model review as cross-model review is acceptable. Role resolution alone proves no provider execution.

Sources: [configuration contract](../../../skills/jstack/jstack-setup/references/configuration.md), [role registry](../../../skills/jstack/jstack-setup/scripts/models.py), [T3 Code delegation contract](../../../skills/jstack/jstack-setup/references/t3-code.md).

Replace Cursor `Task` and model slugs with supported child-task dispatch, explicit context and retained task IDs. Use fresh children for review rounds. Replace `/loop` with the current task's bounded progress mechanism; persistent scheduling requires task-specific authorization. Root-triggered writing helpers, principles, `swarm`, `figure-it-out` and Opening a PR are additional common dependencies, even when a leaf omits them. An upstream route never expands the user's permissions or authorizes publication, installation or communication. Global skill availability on this machine is not a bundled dependency contract.

Sources: [root triggers and autonomy](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/SKILL.md), [local execution boundary](../../../skills/jstack/jstack-setup/references/configuration.md).

Proposed packaging: bundle the helper procedures inside `juan-mode` references for the initial complete package. Keep `setup-jstack` as an explicitly discovered dependency for the resolver and the verification tools as separate optional operations. Upstream standalone skill names below identify the behavior to adapt; they do not require a separate jstack installation for every helper.

Read `cursor-team-kit/skills/control-cli/SKILL.md`, `control-ui/SKILL.md` and `pstack/skills/benchmark-checklist/SKILL.md` in full. Their useful contracts are deterministic driving, application identity, retained artifacts and meaningful measurement. Adapt browser selection to T3 Code preview rules; preserve repository harnesses and use a PTY only for interactive terminal behavior. Browser driving does not establish CPU/heap capture or Electron attachment. Choose profiling tools from the target runtime and report missing access. Keep measurement runs separate from intrusive profiling, count errors and completed work, alternate comparable runs and report noise.

Control CLI now has a [standalone jstack port](../../../skills/jstack/jstack-control-cli/SKILL.md) and [bounded terminal evaluation](../evaluations/control-cli/README.md). Runtime forensics now has a separate live CPU-profile evaluation below. Bug fix, Feature, Refactoring and Perf issue now have their own procedures and evaluations. This helper alone does not enable pending callers or establish profiling and Control UI support.

Sources: [CLI control and profiling](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/cursor-team-kit/skills/control-cli/SKILL.md), [UI control and CDP](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/cursor-team-kit/skills/control-ui/SKILL.md), [benchmark checklist](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/benchmark-checklist/SKILL.md).

The shipped verification generator and maintainer already specify public-interface proof, owned-state isolation, evidence retention and cleanup. Reuse an existing project verifier when appropriate; generation, maintenance and ordinary execution remain separate operations. Their retained evaluations establish focused CLI behavior, not browser, profiling, pixel parity or cross-provider workflow execution. Read both shipped skills, the generator's output contract and both evaluation READMEs.

Sources: [generator](../../../skills/jstack/jstack-create-verification-skill/SKILL.md), [output contract](../../../skills/jstack/jstack-create-verification-skill/SKILL.md), [maintainer](../../../skills/jstack/jstack-maintain-verification-skill/SKILL.md), [generator evaluation](../evaluations/create-verification-skill/README.md), [maintenance evaluation](../evaluations/maintain-verification-skill/README.md).

## investigation

Trigger: a read-only question about behavior, motivation, confidence or a choice. Output: a cited architectural explanation or recommendation with tradeoffs. Dependencies are `how`, conditional `why` and writing rules. Preserve its explicit exclusion of code changes, PR creation and Babysit; investigation preceding implementation returns control for a separately authorized route.

Source: [investigation](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/investigation.md).

Adapt delegation to `how explorer`/`how explainer`, adding `why investigators`/`why synthesizer` only for motivation. T3 Code tool replacement must preserve read-only behavior even if the child transport has no readonly flag. Prerequisites are a readable target and usable configured child providers; missing history or connectors becomes an evidence gap.

Acceptance scenario: explain one narrow fixture function and then a subsystem rationale. Verify the simple route uses one explainer, the complex route reconciles independent findings, unsupported rationale stays labeled, all citations resolve and repository status stays unchanged. A mention of a possible fix must not create a PR.

## feature

Trigger: new or changed behavior. Output: an implemented, reviewed and publicly exercised change with design rationale and open decisions. Dependencies are `how`, `architect`, conditional `arena` for multiple viable implementation shapes, conditional `interrogate`, a control/verifier path and Opening a PR. Preserve the named data shape, four-part throughput checkpoint and lead ownership of review and proof.

Source: [feature](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/feature.md).

Use `feature, refactoring` for implementation, `hardest tasks` for qualifying complexity, plus the helpers' roles. Adapt design-only composition and publication to requested delivery. Prerequisites are resolved helper packages, sufficient configured design candidates, isolated writable state and a runnable public interface. The skill must distinguish blocked runtime verification from completed implementation.

Acceptance scenario: add a public CLI filter to a fixture with existing data. Require a grounded design, scoped child implementation, parent inspection, assertions on real stdout/persistent state and proof retained after cleanup. A child claiming success with incorrect output must fail verification. An explicit local-only request must remain local.

The [Feature procedure](../../../skills/jstack/jstack-juan-mode/playbooks/feature.md) is now implemented, including the shared throughput checkpoint. Its [evaluation](../evaluations/feature/README.md) separates isolated two-seat execution from the existing global one-seat configuration, which cannot satisfy Architect. Opening a PR remains unavailable.

## bug-fix

Trigger: a defect to reproduce and correct. Output: the observed failure, evidenced mechanism, minimal fix and failing-then-passing output. Dependencies are a matching control path, `how`, regression-oriented `why`, conditional `architect`, optional cheap-path `jstack-tdd` and Opening a PR. Preserve mechanism confirmation before design fan-out and verification on the original interface.

Source: [bug-fix](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/bug-fix.md).

Use `bug-fix` plus investigation/design roles and `hardest tasks` where justified. Replace Cursor `/loop` with scoped continued diagnosis. Prerequisites are a reachable reproducer or authorized synthetic trigger, the target's runtime and isolated state. If the real interface is inaccessible, retain the failed attempt and exact prerequisite; a unit-test pass must not imply reproduced-bug absence.

The [standalone jstack-tdd helper](../../../skills/jstack/jstack-tdd/SKILL.md) now preserves the pinned six-step test-first procedure and impractical-test alternative. Its [bounded evaluation](../evaluations/tdd/README.md) covers a public CLI regression and an unavailable native prerequisite. The [Bug fix procedure](../../../skills/jstack/jstack-juan-mode/playbooks/bug-fix.md) now consumes this helper, with [bounded delegated CLI evidence](../evaluations/bug-fix/README.md) and local commit sequencing. Opening a PR remains unavailable.

Acceptance scenario: seed a CLI defect that exits zero but returns the wrong persisted value. The public reproducer must fail before implementation and pass afterward; review must reject unrelated defensive changes. In a cheap-test fixture, stage the failing regression test before the fix. An inaccessible-interface case must report blocked proof.

## refactoring

Trigger: a focused or medium structural change that preserves behavior. Output: the new structure, initial behavior contract, equivalence proof and evidence of simpler tracing. Dependencies are `how`, conditional `architect`, control/verification, structural principles and Opening a PR. Preserve the pre-change characterization test and migration of every affected caller; a discovered feature or bug belongs in a separate scope.

Source: [refactoring](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/refactoring.md).

Use `feature, refactoring`, with helper roles as needed. Tool replacement is ordinary isolated child editing and supported verification. Prerequisites are an executable baseline, characterized outputs and visibility of all consumers. Large cross-cutting work hands off to the separately specified bespoke-planning dependency.

Acceptance scenario: replace a branching CLI formatter with a lookup table while retaining exact public outputs. Capture baseline cases before edits, replay afterward, inspect string references and every caller, and reject an unrelated output improvement. Type checking alone must not satisfy equivalence.

The [Refactoring procedure](../../../skills/jstack/jstack-juan-mode/playbooks/refactoring.md) is now implemented. Its [evaluation](../evaluations/refactoring/README.md) covers a focused formatter with baseline capture before edits and independent public equivalence checks. The evaluation distinguishes a one-seat Architect blocker from a separate two-seat fixture run; API/caller migrations remain untested by these cases.

## perf-issue

Trigger: a measured, one-off slowdown. Output: comparable before/after measurements, delta, limiter and retained trace paths. Dependencies are control/profiling, `benchmark-checklist`, `how`, conditional `architect`, artifact parsing and Opening a PR. Preserve baseline-first diagnosis, the ordered optimization choices and verification after each attempt.

Source: [perf-issue](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/perf-issue.md).

Use `perf-issue`, the relevant grounding/design roles and `judgment and prose` for delegated analysis without a dedicated role. T3 Code browser tools can drive the workload; a compatible runtime profiler must produce the measurement artifact. Prerequisites include representative data, comparable builds/configurations, countable successful work and tolerable or characterized host noise.

Acceptance scenario: diagnose repeated parsing in a controlled CLI workload, prove the limiter in a separate profiling run, then alternate baseline/treatment runs at least five times each. Report median/range and end-to-end effect. A treatment that merely skips work or errors faster must be rejected; a gap within noise is not a speedup.

The [Perf issue procedure](../../../skills/jstack/jstack-juan-mode/playbooks/perf-issue.md) is now implemented. Its [evaluation](../evaluations/perf-issue/README.md) records a synthetic batch CLI, independent measurement and output checks, and remaining runtime limits.

## hillclimb

Trigger: sustained improvement of one metric against a stop predicate. Output: the final metric, accepted/reverted attempt counts, accepted changes and decision-log path. Dependencies add a sensitivity-proven frozen harness, a regression gate and `show-me-your-work` to the perf route. Preserve one hypothesis per measured attempt and removal of rejected changes; a plateau does not silently relax the target.

Source: [hillclimb](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/hillclimb.md).

Use `hillclimb`, relevant helper roles and isolated worktrees for concurrent hypotheses. Adapt unattended wakes to explicit runtime support and authorization. Reconcile the leaf's experiment columns with the shared decision-log contract instead of maintaining two contradictory canonical formats. Read `show-me-your-work/SKILL.md` in full; its Cursor transcript path and mandatory different-family reviewer need T3 Code equivalents and a disclosed limitation when unavailable.

Source: [decision trail](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work/SKILL.md).

Acceptance scenario: run a small declared number of attempts against a controlled workload, including a correct win, a noisy apparent win and a faster but incorrect change. Only the correct measurable win survives, each outcome appears in the log, the frozen harness stays unchanged, and the target/minimum-attempt predicate remains intact. Prerequisites are a reproducible metric, runtime budget, regression gate and traceable run evidence; persistence across turns needs its own test.

The [Hillclimb procedure](../../../skills/jstack/jstack-juan-mode/playbooks/hillclimb.md) is now implemented. Its [bounded evaluation](../evaluations/hillclimb/README.md) records observed iteration behavior, stop predicates and remaining coverage gaps. The shared trail owns the canonical format; per-attempt measurement evidence preserves the source's experiment fields.

## runtime-forensics

Trigger: a live symptom such as a leak, idle CPU or rendering glitch. Output: captured signal, reduced finding, tested mechanism and mapped source location. Dependencies are matching runtime instrumentation, artifact parsing and source mapping. Preserve diagnosis-only delivery and escalation to Bug fix or Perf issue when implementation is later requested.

Source: [runtime-forensics](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/runtime-forensics.md).

The [implemented procedure](../../../skills/jstack/jstack-juan-mode/playbooks/runtime-forensics.md) uses `judgment and prose` for delegated artifact analysis, with `hardest tasks` for difficult causal analysis. Its [bounded evaluation](../evaluations/runtime-forensics/README.md) covers an owned Node process. Upstream calls the route read-only while permitting live CDP injection or hotfixes. Adapt that to temporary instrumentation of an authorized instance with restoration and cleanup, keeping source files unchanged. T3 Code page interaction does not imply permission or capability to instrument an arbitrary process. Prerequisites include a reachable instance, supported profiler/debugger and attributable symbols.

Acceptance scenario: capture an owned test process repeatedly scheduling an idle timer, reduce its profile, instrument that mechanism and map it to source. Preserve before/after evidence and remove owned instrumentation. If the environment can capture but cannot test the mechanism, report a supported hypothesis and the missing proof rather than a confirmed diagnosis.

## trace-forensics

Trigger: an existing CPU profile, trace, heap snapshot or spindump. Output: artifact identity/format, reduced finding, source mapping and whether paired evidence confirms it. Dependencies are format-appropriate parsing/querying, optional delegated reduction and symbols. Preserve the fixed input dataset and the distinction between paired confirmation and the strongest unconfirmed hypothesis.

Source: [trace-forensics](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/trace-forensics.md).

The [implemented procedure](../../../skills/jstack/jstack-juan-mode/playbooks/trace-forensics.md) uses configured `judgment and prose` for reduction and `hardest tasks` when warranted. Preserve the source's SQLite normalization step before querying, without modifying the original artifact. Prerequisites are a supported parser and source mapping; missing symbols are an explicit diagnostic limit. Captured-artifact analysis does not require a live browser or service. The [bounded evaluation](../evaluations/trace-forensics/README.md) records synthetic CPU-profile coverage and remaining formats.

Acceptance scenario: supply a known CPU profile with symbols and a paired capture, plus a separate unmapped capture. Require attribution to the known hot path and reproducible query evidence in the first case. The second must name absent symbols and avoid inventing a source line or rerunning the application. Original input hashes must remain unchanged.

## visual-parity

Trigger: pixel-equivalent migration or comparison of two implementations. Output: each component's image-diff result, baseline location and remaining scope. Dependencies are a frozen visual regression harness, browser/control execution, isolated component work and Opening a PR. Preserve the baseline before migration, shared primitives before dependent components and zero pixel difference as the specified gate.

Source: [visual-parity](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/poteto-mode/playbooks/visual-parity.md).

Propose `feature, refactoring` for component owners and `swarm workers` only when the shared fan-out workflow is used. Replace `/loop` with bounded per-component correction and T3 Code preview or the repository's documented visual harness. Prerequisites include deterministic viewport, fonts, rendering environment, animation state, fixed test data and preserved baseline images. A capture or comparison tool must actually expose pixel differences; screenshots reviewed by eye are insufficient.

Acceptance scenario: migrate two fixture components after capturing all declared states, including one intentional one-pixel defect. The defect must fail the gate and get repaired without baseline/harness edits. A later shared-primitive change reruns every dependent component. Rendering nondeterminism must surface as a blocked baseline, never a silently relaxed parity threshold.
