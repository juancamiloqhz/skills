# Engineering principles

When framing, implementing or reviewing a task, select the relevant conditions below and read those sections. These are internal juan-mode references, not standalone skills or executable playbooks. Existing user instructions, repository contracts and the requested scope govern their application. No principle grants permission to expand the task.

| Upstream principle | Read when | Reference |
| --- | --- | --- |
| `attack-the-premise` | After multiple fixes sharing an assumption fail the same gate. | [evidence](evidence.md#attack-the-premise) |
| `boundary-discipline` | When wiring validation, adapters or error handling. | [design](design.md#boundary-discipline) |
| `build-the-lever` | When tooling would make nontrivial work repeatable or reviewable. | [evidence](evidence.md#build-the-lever) |
| `encode-lessons-in-structure` | When a mechanical correction recurs. | [evidence](evidence.md#encode-lessons-in-structure) |
| `exhaust-the-design-space` | When a consequential novel decision has multiple viable shapes. | [design](design.md#exhaust-the-design-space) |
| `experience-first` | When user experience and implementation convenience conflict. | [design](design.md#experience-first) |
| `explain-the-number` | Before reporting or acting on a measured performance or evaluation result. | [evidence](evidence.md#explain-the-number) |
| `fix-root-causes` | When diagnosing a failure. | [evidence](evidence.md#fix-root-causes) |
| `foundational-thinking` | Before choosing structures or sequencing features. | [design](design.md#foundational-thinking) |
| `guard-the-context-window` | When large evidence or a long run strains context. | [coordination](coordination.md#guard-the-context-window) |
| `laziness-protocol` | When tempted to add layers or widen a refactor. | [change](change.md#laziness-protocol) |
| `make-operations-idempotent` | For commands or loops subject to retries and partial failure. | [coordination](coordination.md#make-operations-idempotent) |
| `migrate-callers-then-delete-legacy-apis` | When replacing an internal API. | [change](change.md#migrate-callers-then-delete-legacy-apis) |
| `minimize-reader-load` | When code is hard to trace. | [change](change.md#minimize-reader-load) |
| `model-the-domain` | When state or domain rules spread across branches. | [design](design.md#model-the-domain) |
| `never-block-on-the-human` | When a reversible scoped action is already authorized. | [change](change.md#never-block-on-the-human) |
| `outcome-oriented-execution` | During an explicitly planned rewrite or migration. | [change](change.md#outcome-oriented-execution) |
| `prove-it-works` | Before declaring an outcome complete. | [evidence](evidence.md#prove-it-works) |
| `redesign-from-first-principles` | When a new requirement challenges the existing design. | [design](design.md#redesign-from-first-principles) |
| `separate-before-serializing-shared-state` | When multiple actors might mutate the same object. | [coordination](coordination.md#separate-before-serializing-shared-state) |
| `sequence-verifiable-units` | For multi-step edits or dependent delivery. | [change](change.md#sequence-verifiable-units) |
| `subtract-before-you-add` | When sequencing a refactor or addition. | [change](change.md#subtract-before-you-add) |
| `test-behavior-not-implementation` | When adding or reviewing tests. | [evidence](evidence.md#test-behavior-not-implementation) |
| `type-system-discipline` | When designing types or handling untyped inputs. | [design](design.md#type-system-discipline) |

All 24 leaves are adapted from `pstack/skills/principle-*` at revision `11713c683fe4add4fd403ea880580abbc9e0875f`. See [attribution and differences](../upstream.md#engineering-principles). Mapping coverage is not runtime evidence for all principles or the 23 planned playbooks.
