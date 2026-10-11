# Jstack roadmap

Status as of 2026-10-11. Model setup and the verification generator are released. The remaining steps describe a proposed sequence, not authorization to start new research or implementation.

## Completed: setup-jstack

Model configuration and validation shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with prose formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). Release checks included six helper tests, skill validation, and Markdown linting. Setup was installed for the four selected providers and invoked successfully in a T3 session.

Those checks cover setup. They do not establish the behavior of a future workflow consumer.

## Completed: organize research

[PR #4](https://github.com/juancamiloqhz/skills/pull/4) established this research directory and excluded the old experiment archive from the current tree.

## Completed: create-verification-skill

[PR #6](https://github.com/juancamiloqhz/skills/pull/6) added the generator. [Evaluation](evaluations/create-verification-skill/README.md) covered a CLI fixture, independent reuse, failure detection and a documentation-only boundary. Browser and cross-provider execution remain untested. Installation and updates are manual.

## Current: optional verification offer

After model configuration, `setup-jstack` inspects the target repository for a real application and existing verification support, then offers generation when needed. Acceptance hands off to the separately available generator. A missing generator produces manual installation instructions; declining or a failed generation leaves the saved model configuration intact.

## Next: maintain-verification-skill

Build maintenance in its own PR after the setup offer. Evaluate it against deliberate changes to an application with an existing verification skill: identify stale recipes, update affected features, and rerun the relevant proof. No maintenance implementation is included in the current change.

## Deferred: define the first workflow

When requested, research a read-only codebase investigation for `juan-mode`. Define its scope, required evidence, relationship to the saved configuration, and how successful behavior will be verified. Record unresolved choices before implementation. No investigation, prompt design, or live delegation is part of the current reorganization.

## Later: implement and evaluate one workflow

After the scope is agreed, build that workflow in a focused PR. Verify the supported behavior, configuration use, permission boundaries, and failure handling against the agreed criteria. Merge before installation and report which coordinating providers and child providers were actually tested.

Choose additional workflows after that result. Arena panels, writing workflows, persistent modes, and larger packaging systems remain outside the committed scope.
