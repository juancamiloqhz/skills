---
name: jstack-juan-help
description: Guides users through jstack setup, /jstack-juan-mode, and picking the skill, playbook, or principle for a task. Type /jstack-juan-help with a question.
disable-model-invocation: true
---

# Juan help

Answer the user's question about jstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a jstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use jstack to fix this bug", is not a help question. Discover and read `jstack-juan-mode`, do the requested work under its scope and activation contract, and mention once that explicit invocation is intended to stay active in this conversation until opt-out. If it is not installed, name the dependency instead of inventing its procedure. Reading it to answer a help question does not activate it.

This file maps questions to the skills and guide pages that hold the answers. Those files own the details. Read the file you route to before you quote it, and trust it when it disagrees with this map. Read bundled guide pages relative to this package. Discover independent skills through the provider catalog or explicit authoring paths rather than assuming sibling directories; public links here identify their canonical copies. If the relevant source cannot be read, say what is missing and qualify the answer. Give the user the public jstack file URL under `https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/`; for bundled pages append `jstack-juan-help/` and their package-relative path. Use an explicit authoring revision when reviewing an unpublished change. Unported upstream capabilities are background, not installed jstack commands.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with `/jstack-juan-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make jstack my own

Check the state that changes the answer, and mention it only when it does:

- Use the discovered `jstack-setup` helper's read-only configuration lookup for the current project, respecting explicit, environment, project and global precedence. A missing effective file means configured delegation needs setup; it does not activate default models. If lookup is unavailable, report unknown configuration rather than assuming it is missing. Do not read or expose credentials.
- No `verify-*` skill or other app harness in the project means agents have no scripted way to drive the app. Mention `/jstack-create-verification-skill` when the question is about proving a change works.
- No formal verification skill in the project means no property is checked beyond the available tests. Mention `/jstack-create-formal-verification-skill` for races, invariants or cases tests rarely reach. When covered code changed after the skill's recorded sync commit, mention `/jstack-maintain-formal-verification-skill` and read the existing skill's correspondence-review and rerun instructions. Generated-input tests remain tests, and missing tools leave a draft.

When the effective model configuration is missing and it matters, ask whether the user wants to pick a model for each role and a reasoning budget now. It matters when the user is new, the question is about setup or cost, or the answer depends on which models run. Reuse an explicit Now/Later choice already given; otherwise ask at most once per chat. If the need is also unclear, ask both questions together. Offer two choices:

- Now: give them `/jstack-setup` to type, and answer their question too.
- Later: answer their question, and state that configured delegation remains unavailable until a valid configuration is saved. Help itself does not launch delegates or change settings.

## Get set up

1. Install manually with `npx skills add juancamiloqhz/skills`, select the required packages, and refresh the provider catalog.
2. Run [`/jstack-setup`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-setup/SKILL.md). It asks for global or project scope, reasoning budget and all 17 roles, then writes the selected `models.json`. Consumers read it on their next invocation; saving does not switch the current chat model. Then it offers once each to generate app and formal verification skills for the project, unless existing support covers the respective need. The choices are separate, and missing generators remain manual prerequisites.
3. Start a real task with `/jstack-juan-mode`, a goal, and a check that can pass or fail.

Installation makes skills available to the host catalog; invocation behavior depends on their metadata and the provider. Help is explicit-only. The [guide index](docs/guide/README.md) and [guide page 1](docs/guide/01-setup.md) have the details. Offer to word their first prompt with them, per [`references/prompting.md`](references/prompting.md).

If cost is the worry, explain that subagents and review panels spend additional tokens. Rerun `/jstack-setup` to choose supported lower effort or cheaper models. `inherit-parent` preserves the current chat's provider, model and effort; provider Auto is a concrete selection, not an alias. A smaller panel launches fewer agents, subject to the workflow's minimum candidate requirements. Budget labels alone do not change inherited effort or cap spending. Save `/jstack-juan-mode` for work that needs rigor.

Jstack is adapted for T3 Code and uses the Agent Skills format. Configured delegation requires the live provider catalog and supported child-task tools. Other hosts may read the files without supplying all runtime behavior. Cross-provider execution, wake/restart recovery and persistence must be supported by actual evidence, not assumed from installation.

## Start a task with `/jstack-juan-mode`

`/jstack-juan-mode` matches the task to a playbook, copies the playbook's steps into the todo list, and runs the other skills as the steps need them. A step it skips stays in the list as `skip: <reason>`. A good prompt states the goal and how to tell it's done. It doesn't list skills, because a hand-written sequence tends to drop or reorder steps the playbook would keep. Read [`references/prompting.md`](references/prompting.md) before you help word one. [Guide page 2](docs/guide/02-juan-mode.md) has examples.

Explicit `/jstack-juan-mode` invocation activates it in this conversation until explicit opt-out. Task completion leaves it active; casual questions do not start a playbook. New conversations start inactive. Use "turn off juan-mode" to stop subsequent routing; stopping already requested work is a separate instruction.

This is intended conversation behavior, not a Cursor Custom Mode shortcut. Resume and compaction support remain provider-specific verification gaps. Read the [activation contract](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/references/activation.md) before making a persistence claim. Mid-chat, "new task" matches a fresh playbook. Delegated agents receive explicit task/style briefs and configured targets; there is no required `poteto-agent` type or automatic persistent activation in children.

## Pick a skill

The default answer is `/jstack-juan-mode`, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`/jstack-juan-mode`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/SKILL.md) |
| Check that the agent understood their goal and the problem before it starts | [`/jstack-in-your-own-words`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-in-your-own-words/SKILL.md) |
| Get a prompt rewritten deeper, not bigger, before sending it: what a top professional would add, their raw material and methods, and an outside check. It returns the prompt and doesn't do the task | [`/jstack-sharpen`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-sharpen/SKILL.md) |
| Know how code works now, or where new code should live | [`/jstack-how`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`/jstack-why`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`/jstack-teach`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`/jstack-recall`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-recall/SKILL.md) |
| Catch up on what changed in this chat since their last message, in plain words and small visuals, with every item waiting on them listed and decidable from the reply alone | [`/jstack-ketchup`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-ketchup/SKILL.md) |
| Know what a small diff could break outside itself | [`/jstack-blast-radius`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`/jstack-architect`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`/jstack-arena`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-arena/SKILL.md) |
| Run parallel checks over slices, or race workers with supported isolation | [`/jstack-swarm`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-swarm/SKILL.md) |
| Have different models review a diff and try to break it | [`/jstack-interrogate`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`/jstack-tdd`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`/jstack-typescript-best-practices`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-typescript-best-practices/SKILL.md) |
| Strip comments before review, using a reviewer that didn't write them | [`/jstack-no-comments`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-no-comments/SKILL.md) |
| Clean AI tells out of prose | [`/unslop`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/pstack/skills/unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`/jstack-technical-writing`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`/jstack-bro`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`/jstack-create-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`/jstack-maintain-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-maintain-verification-skill/SKILL.md) |
| Formally verify a race, invariant, or other property that tests rarely reach | [`/jstack-create-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-formal-verification-skill/SKILL.md) |
| Bring a formal verification back in line after covered-code changes and distinguish drift from bugs | [`/jstack-maintain-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-maintain-formal-verification-skill/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`/jstack-benchmark-checklist`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`/jstack-figure-it-out`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`/jstack-show-me-your-work`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-show-me-your-work/SKILL.md) |
| Pick a model for each role and a reasoning budget | [`/jstack-setup`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-setup/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`/jstack-automate-me`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`/jstack-reflect`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`/jstack-correct`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-correct/SKILL.md) |
| Build a private PR-status button page that wakes this T3 conversation | [`/jstack-make-bot-ui`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-make-bot-ui/SKILL.md) |
| Find their way around jstack | `/jstack-juan-help` |

If an installed skill is missing from the table, discover it through the catalog, read its frontmatter and route by its description. The `jstack-principle-*` packages are covered under principles below. Make bot UI is explicit-only; its bundled action is a fixed read-only PR status check.

Close calls:

- `/jstack-how` explains what the code does. `/jstack-why` explains the reasons. `/jstack-teach` runs one or both and explains the result plainly.
- `/jstack-arena` gives every worker the same brief and merges the best parts. `/jstack-swarm` splits work into slices or a race and returns one report.
- `/jstack-architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `/jstack-interrogate` reviews the diff. `/jstack-blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `/jstack-recall` rebuilds context across recent chats. `/jstack-ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `/jstack-figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

External helpers and host integrations:

- `/jstack-deslop`, `/jstack-control-cli`, and `/jstack-control-ui` ship as independent jstack packages. `/unslop` is an external dependency; discover it before use.
- Cursor's `/loop` and `/create-skill` are not jstack commands. Use the discovered host authoring helper and explicitly authorized, supported wake mechanisms; never invent a scheduler.
- jstack has no `/orchestrate` skill. Orchestrate is a `/jstack-juan-mode` playbook. If the slash menu shows `/orchestrate`, another plugin provides it.
- Upstream Statechart and video catch-up remain deferred. They are not shipped jstack commands. For formal checks after a code change, follow the generated skill's coverage, sync and rerun instructions; for a read-only chat recap, use `/jstack-ketchup`.

## Playbooks and principles

Playbooks are step lists inside `/jstack-juan-mode`, not skills, so they have no slash command. Inside `/jstack-juan-mode`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" runs Babysit in drive mode to merge-ready. "check on pr 123" requests one read-only status check. Neither merges unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "stack them, don't ship" runs Autopilot-stack.
- "run the eval playbook" runs Eval.

Without active `/jstack-juan-mode`, the host may select another workflow for the same phrase. The Playbooks section of [`jstack-juan-mode`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/SKILL.md) lists every playbook and when it applies. [Guide page 6](docs/guide/06-verify-and-ship.md) covers opening, babysitting, and landing a PR.

Jstack has no separate planning skill. The host's available planning mode may work alongside it. For work that spans phases or stacked PRs, asking `/jstack-juan-mode` for a plan runs the [Multi-phase plan playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/multi-phase-plan.md), which writes the plan and doesn't implement it. For a design question, the Prototype playbook or `/jstack-architect` settles it in code first.

Principles are one-rule skills that `/jstack-juan-mode` reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output." Typing `/jstack-principle-<name>` still loads one on demand. [Guide page 8](docs/guide/08-principles.md) lists them.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The mode stopped applying after a few turns | Check the latest activation/opt-out and handoff record; re-invoke `/jstack-juan-mode` if needed. Host reload and resume are not guaranteed. |
| A question got treated as the next step of the last task | Say "new task", or say the turn doesn't need the mode. |
| A new model choice had no effect | Check effective config precedence and the resolved role. Consumers reread settings at invocation; inherited roles retain the parent effort, and saving does not change the current chat model. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A skill didn't load on its own | Check installation, catalog discovery and invocation metadata. Some entrypoints are explicit-only; Juan-mode does not route every available skill automatically. |
| Parallel agents overwrote each other | Give each writer an app-owned worktree and separate ports/output paths; a worktree alone is not a separate machine. |
| An overnight run moved but finished nothing | The run needs a check that can pass or fail and an actually supported wake mechanism, not a duration. See [guide page 7](docs/guide/07-overnight.md). |
| The reply claims success from a green build | Ask for the real command, flow, stored value, or profile. That's the prove-it-works principle. |

For a run that drifts, [`references/prompting.md`](references/prompting.md) has one-line steers. [Guide page 10](docs/guide/10-recipes-and-pitfalls.md) has more pitfalls and the recipes worth copying.

## Make jstack my own

- [`/jstack-automate-me`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-automate-me/SKILL.md) drafts a personal mode skill from the user's own history, to use alongside `/jstack-juan-mode`.
- [`/jstack-reflect`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-reflect/SKILL.md) after a session turns its lessons into proposed skill edits, honoring existing authorization and explicit review checkpoints.
- `/jstack-juan-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Fix a misbehaving skill in its own PR, not inside the feature work where it went wrong.

[Guide page 9](docs/guide/09-make-it-yours.md) covers each of these.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then the link to that file. Keep it short unless the user asked for the whole map.
