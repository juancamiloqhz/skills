# Set up jstack

In this page you install the skills, pick which models jstack uses, and run your first task. Setup is one command plus a short conversation.

## Install the skills

Install manually from the skills repository:

```sh
npx skills add juancamiloqhz/skills
```

Select the jstack packages you need and refresh the provider's skill catalog. The examples use `/jstack-*`; Codex also accepts `$jstack-*`. Help can explain setup without installing or changing anything.

## Pick your models

Run:

```text
/jstack-setup
```

[`/jstack-setup`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-setup/SKILL.md) discovers the live T3 provider catalog, asks whether to save global defaults or a project configuration, then asks for a reasoning budget and all 17 model roles. Global defaults are `${XDG_CONFIG_HOME:-$HOME/.config}/jstack/models.json`; an optional project file is `<repo>/.jstack/models.json`. Explicit configuration and `JSTACK_CONFIG` overrides take precedence, then project, then global. See the [configuration contract](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-setup/references/configuration.md).

A new inherited draft uses the medium budget label. The targets are unlimited/max, large/xhigh, medium/high and small/medium where the provider supports them. Setup confirms your choices and discloses unsupported effort levels. A budget is a reasoning preference, not a spending cap; inherited roles retain the parent effort.

A configuration contains all 17 roles. Do not delete role entries to reset them: incomplete or stale configurations fail whole-map validation. Rerun setup for requested changes; it preserves unrelated assignments and options. A project map replaces the global map as a whole, rather than merging individual roles. Missing configuration blocks configured delegation until setup is completed.

Set a role to `inherit-parent` to retain the executing conversation's provider, model and effort. Provider Auto is a concrete catalog selection, not an alias for inheritance. Each panel entry launches a separate agent; new Arena, Architect and Interrogate panels start with two inherited seats. Two inherited seats do not supply model diversity. Setup also configures `swarm workers`, the default model for each worker unless an authorized race names an arm selection.

## Accept the verification offers, or don't

At the end of setup, `/jstack-setup` looks for a way to prove app behavior in your project, either a `verify-*` skill or an existing harness. If it finds neither, it offers once to generate one with [`/jstack-create-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-verification-skill/SKILL.md).

Say yes and it writes a project-local `verify-<app>` skill, normally under `.agents/skills/`, and the existing automatic `.claude/skills/verify-<app>` link. It proves the skill works before handing it over and preserves conflicting links. Say no and setup moves on. You can invoke `/jstack-create-verification-skill` later. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers it in depth.

If you're new to jstack, say yes. An agent that can check its own work keeps going until the check passes. An agent that can't hands every result back to you to check by hand. Of everything in this guide, the verification skill pays off the most.

Then setup offers once to generate a formal verification skill with [`/jstack-create-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-formal-verification-skill/SKILL.md), unless the project already has one. This is a separate choice even when you skip or decline app verification. Tests check the cases someone thought to write. A formal verification skill checks a key property, such as "a job never runs twice at once", in every case within a stated scope. Say yes when your code has concurrency, retries, a state machine, or a parser, where a bug is costly and tests rarely reach the case that breaks. Otherwise say no and run it later if that changes.

Acceptance starts the available generator for this project and property. Missing tools leave a draft with explicit prerequisites; setup does not install them. A result states its bounds, findings and what was actually verified. The saved model configuration stays intact if you decline, the generator is unavailable, or verification is incomplete.

Consumers read the effective configuration again on their next invocation. Saving it does not switch the current conversation model and does not require a new chat. Invalid choices remain errors; consumers do not silently fall back to another model.

## Keep the cost in check

jstack spends extra tokens on subagents and review panels. That's the price of the rigor. To spend fewer:

- Rerun `/jstack-setup` and pick a smaller reasoning budget or cheaper models. A strong model in the main chat with cheaper, faster models in the code roles is a good split.
- Set a role to `inherit-parent` to retain the chat's own model and effort. Changing a budget label alone does not lower inherited effort.
- Shorten a panel list within the workflow's candidate minimum. Each entry runs one subagent.
- Save `/jstack-juan-mode` for work that needs rigor. A small, obvious edit doesn't.

## Run your first task

Pick something real but small, and describe it the way you'd describe it to a colleague:

```text
/jstack-juan-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

Watch the todo list. Its first items are the matched playbook's steps copied in, the Feature playbook for this prompt. If `/jstack-juan-mode` skips a step, the step stays in the list with `skip: <reason>`, so you can see what it chose not to do.

From here you can type normal follow-ups. Explicit `/jstack-juan-mode` invocation is intended to remain active in this conversation until you turn it off. New conversations start inactive. This is a conversation instruction, not a Cursor Custom Mode or guaranteed host reload. Resume/compaction support still needs provider-specific runtime evidence; see [conversation state](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/references/activation.md).

Next: [Route work through `/jstack-juan-mode`](./02-juan-mode.md).
