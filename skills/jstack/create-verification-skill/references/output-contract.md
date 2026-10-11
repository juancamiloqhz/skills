# Generated verification skill contract

Write concrete instructions for the target repository. This document specifies required information, not commands to copy into every application. A fresh reader must be able to run the skill without the generation conversation.

## Skill entrypoint

Use YAML frontmatter with `name: verify-<app>` and a description identifying the app, interfaces, and when verification is useful. Use a single H1, then the following sections. Include only helpers that earn their maintenance cost.

### Launch

Give the actual repository-root command, prerequisites and an observable readiness check. Establish unique owned scratch state and a separate evidence directory. Document how ports, profiles, databases and authentication are isolated, or explicitly state when safe concurrent use is unavailable. Bind local services to loopback unless the user has authorized broader exposure. Track only processes created by the run.

For a short-lived CLI, launch means verifying the executable or building it if necessary, then invoking commands against the isolated state. Do not invent a background server or require a PTY for a noninteractive command. For a library, use its public interface through a runnable client and record the invocation.

### Doctor

Give a read-only check of the identity and readiness needed for this interface. It must distinguish the intended executable, build or instance from an unrelated one and report unmet prerequisites. It must not seed or repair state as a hidden side effect. Run it before driving an instance whose state is uncertain.

### Drive

Link the feature index. Use actual public commands, routes or observed UI locators. For UI actions, prefer accessible names and stable attributes over coordinates. Show the user action and expected result, and how the recipe detects a failure. Invoke real public entry points instead of internal setters or test-only shortcuts. Existing mocks are acceptable only at established external boundaries; disclose what was not exercised.

### Evidence

Name a retained location outside the scratch tree, and give exact capture commands or tool operations. Capture the action and result: CLI argv, stdout, stderr and exit status; HTTP requests and responses with secrets removed; UI action context, snapshots and screenshots. Include app identity and the feature/entry point. Verify persistent mutations with a second read or independent state observation where applicable.

Assertions must fail the run on a mismatch; process exit success alone may not prove the feature. Record failures and skipped entry points. Never imply a UI was tested through an API-only run, or all features were proven by one path. Generated evidence should identify the revision when available without publishing local credentials or private data.

### Cleanup

Give exact commands to stop owned processes and remove only owned scratch state, including failed attempts. Specify a post-cleanup check. Do not delete proof artifacts. Never use broad process-name termination or delete an unverified user-supplied directory. Cleanup should be safe to repeat after a partial launch.

### Helpers

If needed, put small scripts under `scripts/` and document their invocation and prerequisites. Use executable permission for directly invoked scripts or an explicit interpreter command. Propagate application and assertion failures as nonzero results; keep action logs even when a run fails. Avoid shell pipelines that discard the application's exit status.

## Feature map

`features/README.md` describes baseline preconditions, isolation, driving conventions, evidence location, and tested versus untested coverage. Link one file per feature. Do not invent extra features to reach a count.

Each feature file has an H1 and a short description of user-visible behavior, followed by these four H2 sections:

1. `Sub-features`: stable short IDs and the behaviors they cover.
2. `How to get to it (user POV)`: known user entry points and required state.
3. `Driving it with <actual tool or harness>`: concrete preconditions, actions, expected observations and evidence capture. Replace the angle-bracket phrase in generated headings.
4. `Gotchas`: relevant traps, permissions, timing, isolation, cleanup, and incomplete coverage.

After the first execution, mark only the paths actually exercised as verified and link their evidence. Others remain mapped but untested. Store dynamic run locations in the evidence report rather than making future invocations depend on a previous temporary directory.
