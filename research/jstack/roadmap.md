# Jstack roadmap

Status as of 2026-10-11. Model setup and the verification generator are released. The remaining steps describe a proposed sequence, not authorization to start new research or implementation.

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

## Current: upstream maintenance

Track pstack revisions, detect complete source changes and review their impact through the [upstream maintenance procedure](upstream-maintenance.md). The manifest preserves original adaptation pins, reviewed ranges and deferred decisions. The [first review](upstream-reviews/2026-10-11.md) covers the manual trial. Merge the tooling before enabling a weekly T3 Code task; verify actual report delivery after scheduling. Implementation recommendations require approval, merges remain separate, and installation stays manual.

## Deferred: define the first workflow

When requested, research a read-only codebase investigation for `juan-mode`. Define its scope, required evidence, relationship to the saved configuration, and how successful behavior will be verified. Record unresolved choices before implementation. That investigation remains outside the current verification-tooling work.

## Later: implement and evaluate one workflow

After the scope is agreed, build that workflow in a focused PR. Verify the supported behavior, configuration use, permission boundaries, and failure handling against the agreed criteria. Merge before installation and report which coordinating providers and child providers were actually tested.

Choose additional workflows after that result. Arena panels, writing workflows, persistent modes, and larger packaging systems remain outside the committed scope.
