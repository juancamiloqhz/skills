# Jstack roadmap

Status as of 2026-10-10. Only setup is implemented. The remaining steps describe a proposed sequence, not authorization to start new research or implementation.

## Completed: setup-jstack

Model configuration and validation shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), with prose formatting corrected in [PR #3](https://github.com/juancamiloqhz/skills/pull/3). Release checks included six helper tests, skill validation, and Markdown linting. Setup was installed for the four selected providers and invoked successfully in a T3 session.

Those checks cover setup. They do not establish the behavior of a future workflow consumer.

## Current: organize research

Replace the old experiment archive with the four documents in this directory. Completion requires coherent status and source references, valid local links, passing Markdown checks, and no prototype in the installable skill catalog.

## Deferred: define the first workflow

When requested, research a read-only codebase investigation for `juan-mode`. Define its scope, required evidence, relationship to the saved configuration, and how successful behavior will be verified. Record unresolved choices before implementation. No investigation, prompt design, or live delegation is part of the current reorganization.

## Later: implement and evaluate one workflow

After the scope is agreed, build that workflow in a focused PR. Verify the supported behavior, configuration use, permission boundaries, and failure handling against the agreed criteria. Merge before installation and report which coordinating providers and child providers were actually tested.

Choose additional workflows after that result. Arena panels, writing workflows, persistent modes, and larger packaging systems remain outside the committed scope.
