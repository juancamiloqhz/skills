# Plan checker code fences

The plan checker now keeps headings and prose inside fenced code examples out of structural plan validation. It recognizes backtick and tilde fences, up to three leading spaces, and closing fences with the same character and at least the opening length. Shorter, mismatched or suffixed closing lines remain inside the example. Actual prose after a proper close is still checked.

Base: merged watcher update, `2409b3c062db0493209bbe2e4db652e73002d5db`. This is the plan-parser fix proposed in the [coverage audit](../../coverage-audits/2026-10-18/README.md). It changes a bundled tool, not a standalone skill or the planning workflow.

## Source comparison

Source: [`pstack/skills/poteto-mode/scripts/` at `0148b78c56c72a1b8412055913c79f767095b217`](https://github.com/cursor/plugins/tree/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/poteto-mode/scripts). Local files use the same names under `skills/jstack/jstack-juan-mode/scripts/`.

- `check-plan.mjs` matches that source byte for byte after replacing its single scheduling-marker line with jstack's existing `schedule_task` and compact `"everyMs":3600000` markers. The fence algorithm has no local redesign. Its existing non-executable file mode remains; callers invoke it with Node.
- `check-plan.test.ts` retains all five upstream tests. Its generated plan uses the matching jstack scheduling text instead of `/loop 1h`; that is its only source difference. The tests run the actual checker against temporary files and remove those files afterward.
- `package.json` adds the test file to the default test command, matching upstream. Jstack's package name and additional strict Orchestrate typecheck remain. Dependencies and lock data are unchanged.

The initial patch check rejected the combined upstream diff because local package metadata differs. Applying the checker change and the one test-command edit separately preserved those adaptations. This is a partial mode update, so the whole-package source pin and reviewed upstream checkpoint remain unchanged. Other current-upstream playbook changes remain unadopted.

## Executed checks

On 2026-10-18, Linux x64, Node v24.19.0 and Bun 1.4.2:

- Against the old checker, four of the five new tests failed. Valid nested/indented examples were rejected, while an invalid backtick opener incorrectly hid a later heading.
- After adopting the source scanner, all five tests passed, covering 14 checker executions. They verify ordinary/indented/longer fences, nested backticks, tilde info strings, mismatched/shorter/suffixed closers, checked prose outside a proper close and invalid backtick info strings.
- The updated default `bun run test` passed all 112 tests across the checker, watcher and Orchestrate suites. This confirms the new file participates in the normal test command.
- The existing plan exercise passed one/two-PR documents, a no-review gate, 16 rejection cases and the usage-error exit. Generic unresolved placeholders still pass, as documented by the original structural checker.
- JavaScript syntax, strict type checking of the new test file, four packaging tests and source-comparison assertions passed. Type checking used cached TypeScript 6.0.3, bun-types 1.4.2 and Node types 24.13.6. An initial explicit type-root command omitted the Node type root; adding it resolved those environment errors without source changes. This does not verify the complete frozen development environment.

Reproduce from the repository root:

```sh
bun test skills/jstack/jstack-juan-mode/scripts/check-plan.test.ts
python3 -B research/jstack/evaluations/multi-phase-plan/exercise.py
node --check skills/jstack/jstack-juan-mode/scripts/check-plan.mjs
```

With the declared dependencies already present, `bun run test` in the skill's `scripts` directory runs the complete suite. Evaluation temporarily linked existing cached dependencies and removed the checkout link afterward. No package installation or lifecycle script ran. Only the source tests and this report are retained; no generated plans or logs are committed.

This remains a structural checker, not a complete Markdown parser or proof of plan feasibility. Passing it does not establish real artifacts, valid model choices, completed verification or approval to execute the plan. No planning agent, schedule, implementation program or installed-skill workflow was started by these tests.
