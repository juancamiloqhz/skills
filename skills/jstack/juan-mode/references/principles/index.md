# Engineering principle discovery

When framing, implementing or reviewing a task, select relevant conditions below and discover the corresponding standalone skill in the current catalog. Read its advertised `SKILL.md` and verify its jstack attribution before applying it. Do not assume sibling installation paths or substitute an unrelated same-name skill. Explicit authoring paths are valid during development and evaluation.

Each principle is independently usable without juan-mode, setup-jstack or a configured model. Loading one does not activate juan-mode. Principles guide the current task; they are not executable playbooks and grant no additional authority.

If a selected principle is unavailable, identify the missing dependency and provide `npx skills add juancamiloqhz/skills --skill principle-NAME` with its actual name for manual installation. Report the affected guidance unavailable, continue independent authorized work, and do not pretend the principle was loaded or copy a hidden fallback into the caller.

| Standalone skill | Read when |
| --- | --- |
| `principle-attack-the-premise` | After multiple fixes sharing an assumption fail the same gate. |
| `principle-boundary-discipline` | When wiring validation, adapters or error handling. |
| `principle-build-the-lever` | When tooling would make nontrivial work repeatable or reviewable. |
| `principle-encode-lessons-in-structure` | When a mechanical correction recurs. |
| `principle-exhaust-the-design-space` | When a consequential novel decision has multiple viable shapes. |
| `principle-experience-first` | When user experience and implementation convenience conflict. |
| `principle-explain-the-number` | Before reporting or acting on a measured performance or evaluation result. |
| `principle-fix-root-causes` | When diagnosing a failure. |
| `principle-foundational-thinking` | Before choosing structures or sequencing features. |
| `principle-guard-the-context-window` | When large evidence or a long run strains context. |
| `principle-laziness-protocol` | When tempted to add layers or widen a refactor. |
| `principle-make-operations-idempotent` | For commands or loops subject to retries and partial failure. |
| `principle-migrate-callers-then-delete-legacy-apis` | When replacing an internal API. |
| `principle-minimize-reader-load` | When code is hard to trace. |
| `principle-model-the-domain` | When state or domain rules spread across branches. |
| `principle-never-block-on-the-human` | When a reversible scoped action is already authorized. |
| `principle-outcome-oriented-execution` | During an explicitly planned rewrite or migration. |
| `principle-prove-it-works` | Before declaring an outcome complete. |
| `principle-redesign-from-first-principles` | When a new requirement challenges the existing design. |
| `principle-separate-before-serializing-shared-state` | When multiple actors might mutate the same object. |
| `principle-sequence-verifiable-units` | For multi-step edits or dependent delivery. |
| `principle-subtract-before-you-add` | When sequencing a refactor or addition. |
| `principle-test-behavior-not-implementation` | When adding or reviewing tests. |
| `principle-type-system-discipline` | When designing types or handling untyped inputs. |

All 24 skills retain pinned pstack attribution. Discovery coverage does not establish runtime readiness for the 23 planned playbooks.
