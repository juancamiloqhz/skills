---
name: setup-benny
description: Configure Benny and prepare its triage and repro automations. Use when installing Benny or changing its Slack, tracker, repository, routing, control, model, or budget settings.
disable-model-invocation: true
metadata:
  internal: true
---

# Set up Benny

Benny ships as a dormant automation pack alongside jstack. The three nested procedures carry `metadata.internal: true` for normal Skills CLI discovery exclusion; read them directly, never register them as slash skills. This pack supplies no live Slack trigger or tracker adapter.

The human enters setup by pointing T3 Code at the pack's `FOR_AGENTS.md`. The bootstrap flow copies the whole pack into the target repository, then reads this file directly at `.agents/automations/benny/skills/setup-benny/SKILL.md`.

Benny needs external configuration and two separately configured live T3 tasks, after their runtime prerequisites are demonstrated.

Do not create or update an automation until the user explicitly asks. Never put a secret value in plugin files, prompts, or committed configuration.

## 1. Copy the pack and enable shared jstack skills

Do this before asking for Benny configuration and before preparing live task drafts.

Ask which repository will run the automations. The source pack is the directory containing `FOR_AGENTS.md`. The destination is `<target-repository>/.agents/automations/benny/`.

Merge the entire source pack into the destination:

1. Create the destination when it is absent.
2. Copy every source file to the same relative path.
3. Preserve destination-only files. Never delete unrelated files during install or refresh.
4. Keep user-owned configuration, feature maps, and routing maps outside the destination. Never overwrite them.
5. When an existing source-managed file differs, inspect the diff and merge without discarding local edits. If ownership is ambiguous, stop and ask before replacing it.
6. Verify that the destination contains `FOR_AGENTS.md`, this setup file, both operational files, their references, and the templates.

If this file is already being read from the target destination, treat the copy as complete and run the same verification before continuing.

Provision shared dependencies through the target provider's supported project-scoped mechanism. Preserve unrelated project settings. Do not invent a T3 plugin setting or substitute global installations. A fresh target checkout must contain or reproducibly obtain the exact reviewed dependencies and any files they need.

Reload the target project or start a fresh agent rooted in a fresh target checkout. Verify these dependencies resolve from project scope:

- `jstack-how`
- `jstack-why`
- `jstack-tdd`
- `unslop`
- `jstack-principle-separate-before-serializing-shared-state`
- `jstack-principle-minimize-reader-load`
- `jstack-principle-guard-the-context-window`
- `jstack-principle-sequence-verifiable-units`
- `jstack-principle-fix-root-causes`
- `jstack-principle-prove-it-works`

Do not count a skill loaded from the current session or a user-scoped plugin. The check must show that a fresh agent in the target repository can read each dependency and its required references/helpers from the committed project setup. A file-copy or CLI discovery test is preliminary evidence, not proof that a fresh provider agent receives the skills.

If project-scoped dependency provisioning is unavailable or any shared dependency does not resolve, stop and explain the failure.

The Benny files are read directly from `.agents/automations/benny/`. Do not add that directory to a plugin manifest or expect its `SKILL.md` files to appear in the slash-skill list.

Tell the user that the project dependency setup, `.agents/automations/benny/`, and any referenced secret-free configuration must be committed before either automation is enabled. Do not commit them unless the user asks.

Once this check passes, live automation prompts may read the committed operational files by their stable repository-relative paths. They must not embed a plugin cache path or copy the file contents.

## 2. Adapt the configuration

Open these copied examples:

- `../../templates/configuration.example.yaml`
- `../reproduce-and-fix-issues/references/feature-map.example.md`

Create user-owned copies outside `.agents/automations/benny/`. These are configuration files, not pack files. Example locations:

- Project config, such as `.agents/benny/configuration.yaml`
- Project feature map, such as `.agents/benny/feature-map.md`
- Project routing map, such as `.agents/benny/routing.md`
- User config, such as `~/.config/benny/configuration.yaml`
- User feature map, such as `~/.config/benny/feature-map.md`

Fill one feature-map section for every user-facing feature the automation may reproduce. Keep it at the user point of view. Do not freeze implementation details or current code paths in the map.

Do not edit the copied examples. Pack refreshes may update source-managed files after conflict review, but they must never touch the user-owned copies.

Prefer committed, secret-free files in the target repository when a fresh automation checkout must read them. Otherwise paraphrase the required values into the live prompt. Reference a repository file only after setup verifies that the file is committed in the repository where the automation runs.

Use stable repository-relative paths for committed pack and configuration files. Never reference the plugin source directory or a plugin cache path from a live automation.

## 3. Fill the required choices

Ask for or confirm:

- Source Slack workspace ID
- Source Slack channel ID
- Optional operations or status channel ID
- Repository URL and default branch
- Triage identity or Slack user ID
- Issue tracker type, team, project, labels, and intake status
- Tracker adapter skill or MCP actions
- Optional routing map path
- Required control skill name
- Required user-facing feature-map path
- Status emoji strings
- Pull request URL format
- Polling and effort budgets
- Model slug for triage, repro, code work, and media review

Resolve all four model choices against T3's live provider/model capabilities, including effort support. T3 tasks inherit the creating conversation's model; the scheduler has no per-task model selector. Do not pretend the YAML changes that model. Separate model contexts need explicitly requested conversations or another demonstrated runtime. Shared helpers retain their jstack configuration resolution. Do not add global role keys, silently substitute models, or change saved model configuration.

The source workspace/channel, triage identity, repository, tracker adapter, control skill, and feature map must be explicit. Fail setup if any required value stays ambiguous.

Use the external `unslop` skill on the final automation names, descriptions, and prompt shims before saving them.

## 4. Check integration capabilities

The triage automation needs:

- Read access to the configured source Slack channel and its threads
- Thread-reply access in that channel
- Attachment metadata and file download access when reports include media
- Search, read, create, and update access through the configured issue-tracker adapter

The repro automation needs:

- Read access to the source thread
- Thread-reply access in the source channel
- Optional post and edit access in the configured operations channel
- Repository read and history access
- A pull request action that can open a draft pull request
- The configured control-adapter skill

Prefer configured T3 Code Slack actions for reads and posts. The optional `BENNY_SLACK_BOT_TOKEN` may fill a narrow gap such as editing one operations status message or downloading an attachment. Store the value in a secret manager or environment, not in YAML.

Do not use undocumented integration endpoints.

The authenticated intake must deliver each new top-level human report from the configured workspace/channel to both independent workflows. Reject replies, edits, deletions and bot echoes. Normalize timestamps to string `ts` and optional string `thread_ts`; reject conflicting aliases. Preserve a durable event identity for deduplication. A generic T3 webhook is not a native Slack trigger; Slack signing must be verified by a supported connector or separately authorized bridge. Never point Slack directly at a generic webhook with an incompatible signature verifier.

Prove that optional children, including children launched by shared helpers, cannot access Slack credentials or write tools. A worktree or prompt prohibition does not establish exclusion. Keep analysis and edits in the coordinator if exclusion cannot be demonstrated. Repro requires an independent, isolated media reviewer; if unavailable, leave repro disabled.

## 5. Prepare the routing map

If the user wants reroutes or owner pings:

1. Copy `../triage-issue-reports/references/routing.example.md` outside `.agents/automations/benny/`.
2. Replace every placeholder with public or organization-local values.
3. Keep owner pings off by default.
4. Allow a ping only for a configured feature owner or a confirmed likely regression author.

If no routing map is configured, triage may classify a report but must not guess a destination or owner.

## 6. Verify the control adapter

Read `../reproduce-and-fix-issues/references/control-adapter.md` and the user's completed feature map.

Confirm that the named skill can:

- Bring up the target app
- Navigate every mapped feature through the real UI
- Exercise mapped states through declared adapter actions
- Inspect state without forcing the result
- Capture screenshots
- Start and stop a recording
- Clean up its processes and temporary data

If any capability is missing, leave the repro automation disabled. It must fail closed rather than claim a reproduction it did not perform.

## 7. Prepare the live automations

Ask whether this is first-time creation or configuration of existing automations.

Read `../../FOR_AGENTS.md` from the copied pack as the primary user-intent source for either path. Use it to understand the two triggers, tools, instructions, outcomes, and shared rules.

### First-time creation

Create one automation at a time.

For each automation:

1. Read the matching copied prompt template as secondary internal source material.
2. Turn `FOR_AGENTS.md`, the finished Benny configuration, and the template intent into a complete natural-language request.
3. Tell the live prompt to read and follow its exact committed operational file under `.agents/automations/benny/`.
4. Use the stable repository-relative path, not a plugin source or cache path. Do not copy the operational file contents into the live prompt.
5. Inspect supported T3 task capabilities and the selected Slack intake and adapters. If any prerequisite is absent, report the missing capability and stop before creating a task.
6. Resolve the configured workspace/channel, repository, tracker and model context without guessing. Prepare the complete draft: trigger, scope, prompt, repository revision, dependencies, models, credential references and cleanup. Secret values stay private.
7. Verify that the pack and referenced configuration/dependency files are committed and accessible in a fresh checkout of the actual automation branch.
8. Present the draft for live authorization and readiness review. Only after explicit authority, create this task disabled using supported T3 tools. If disabled creation is unavailable, stop; do not create an enabled substitute. A generic webhook still needs the separately verified intake adapter.
9. Record its returned ID and read back its disabled state, prompt, trigger and scope before preparing the next task. Reconcile a lost response against existing tasks instead of retrying creation.

Use this complete triage intent, filled from configuration:

- Name `benny-triage`.
- Read and follow `.agents/automations/benny/skills/triage-issue-reports/SKILL.md` for every run.
- Trigger on each new top-level report in the configured source Slack channel.
- Read the triggering thread and reply only inside it.
- Use the configured issue-tracker integration.
- Classify, inspect evidence, trace cause, dedupe, and create only clear new bugs.
- End one thread-only verdict with the configured `[benny:bug]`, `[benny:performance]`, or `[benny:other]` marker and optional tracker URL.
- Never post a source-channel root message.

After triage draft review and disabled-task verification, use this complete repro and fix intent:

- Name `benny-reproduce`.
- Read and follow `.agents/automations/benny/skills/reproduce-and-fix-issues/SKILL.md` for every run.
- Trigger on the same new top-level reports in the configured source Slack channel.
- Use the configured repository and default branch.
- Read the source thread and reply only inside it.
- Include pull request creation and the configured tracker, control-adapter, and feature-map requirements. Paraphrase mapped user paths and states unless setup verifies an eligible committed file in the same repository.
- Wait for a trusted triage marker before acting.
- Reproduce the exact symptom twice through the mapped real UI and capture evidence.
- Verify an existing fix without authoring over it.
- Attempt an optional bounded fix only after confirmed repro, then open a draft pull request when proof and checks pass.
- Never post a source-channel root message.

Keep the two tasks independent. Both receive the same accepted root report; repro waits for the trusted triage marker. Demonstrate that its wait cannot block triage and that repeated delivery cannot start duplicate verdicts or competing fixes.

### Existing automations

Read the recorded task IDs with supported T3 tools. Confirm ownership, scope and current state before preparing changes. An unavailable or ambiguous ID is a reconciliation task, not permission to create a replacement.

Finish configuration, routing, control-adapter, and feature-map validation. Then review the exact changes using this checklist.

For the existing triage automation, update:

- Name and description
- Direct instruction to read `.agents/automations/benny/skills/triage-issue-reports/SKILL.md`
- New top-level Slack report trigger and source channel
- Slack thread read and reply capabilities
- Issue-tracker integration
- Paraphrased triage instructions, thread-only rule, and Benny verdict markers

For the existing repro automation, update:

- Name and description
- Direct instruction to read `.agents/automations/benny/skills/reproduce-and-fix-issues/SKILL.md`
- Matching Slack trigger and source channel
- Repository and default branch
- Slack thread read and reply capabilities
- Pull request action
- Tracker, control-adapter, and feature-map requirements
- Paraphrased marker wait, evidence, verification, and bounded-fix instructions

Apply only the authorized update to each recorded task ID using supported T3 tools, then read back the result. Keep tasks disabled during safety validation. Preserve unrelated tasks and settings. Do not create replacements or duplicates.

### Creation boundary

Use only the supported T3 task interface after draft review and explicit live authorization. Do not bypass review with private backend calls, URLs carrying draft fields or protocol deep links. Creating a top-level automation conversation also requires an explicit user request. The current pack is inactive; installing or merging it never supplies deployment authority.

Do not enable either automation for normal traffic until the thread-safety test passes. A separately authorized test may activate only bounded test intake, with cleanup and re-disabling on failure.

## 8. Test thread safety

Use a test channel or a harmless test report.

Before testing, confirm that the target repository's project dependency setup, `.agents/automations/benny/`, and every referenced secret-free configuration file are committed on the branch used by the automation checkout. Confirm that both live prompts point at their exact committed operational files. If any check fails, stop. Tell the user that the automation cannot be enabled yet.

Verify:

1. Triage stores the root `thread_ts` and posts exactly one verdict as a reply.
2. The verdict contains one configured marker.
3. Repro accepts the marker only from the configured triage identity.
4. Repro keeps the same immutable source coordinates.
5. No source-channel root message appears.
6. A delegated worker cannot use any Slack write action.
7. Missing coordinates, a deleted parent, or a failed preflight produces no post and no tracker issue.

Enable normal traffic only after all seven checks pass.
