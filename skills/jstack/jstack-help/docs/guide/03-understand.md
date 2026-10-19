# Understand the code before changing it

Editing code you don't understand is how subtle regressions ship, and that's as true for the agent as for you. Agents usually fail in one of two ways. They misread what you want, or they don't have the context to do the work right. [What goes in a prompt](./02-juan-mode.md#what-goes-in-a-prompt) handles the first. This page handles the second.

jstack gives you four ways in. `/jstack-how` explains what the code does now. `/jstack-why` digs up the reasons it's shaped that way. `/jstack-teach` blends both into one explanation. `/jstack-recall` rebuilds your own recent context on a topic. Each one also makes the agent explain itself in words you can check. That's how you supervise an agent that may know the code better than you do.

![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under /how and /why.](./images/understanding.jpg)

The illustration retains the original command labels. Use the jstack commands in the text; Cursor's `/loop` is not a jstack command.

## Start with a read-only investigation

When the cause is unclear, ask for findings, not a fix:

```text
/jstack-juan-mode investigate why background jobs time out every few hours. give me what we know, what data you used, and your best hypotheses. don't change any code yet.
```

"don't change any code yet" routes this to the [Investigation playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/investigation.md). It runs `/jstack-how`, adds `/jstack-why` for questions about motivation, and returns a cited explanation. For a choice between options, it returns a recommendation with a trade-offs table. Asking "what data you used" makes the agent separate its evidence from its guesses. When the findings point at a fix, start the fix as a new task.

## Trace behavior with `/jstack-how`

```text
/jstack-how do we dedupe notifications? is there an n+1 when we look up subscribers?
```

Ask the question you actually have. [`/jstack-how`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-how/SKILL.md) reads the code and answers at the level of a senior engineer onboarding you onto the subsystem, with the runtime flow, the key types, and the non-obvious parts. For a big subsystem it fans out two to four read-only explorers first. For a narrow question it just reads and explains.

## Dig up history with `/jstack-why`

```text
/jstack-why was the retry limit set to five? does the reason still hold?
```

[`/jstack-why`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-why/SKILL.md) starts from source control, then queries whatever evidence categories your MCPs expose, such as the issue tracker, long-form docs, team chat, observability, error tracking, and analytics, all in parallel. The report cites everything, separates direct evidence from inference, and says "appears to" when the record is thin. A null result gets reported too, because "nobody wrote down why" is itself an answer.

The two compose naturally. `do why first then how` is a good prompt when you suspect the history explains the mess.

## Actually understand it with `/jstack-teach`

```text
/jstack-teach me how this PR changes retries. convince me it fixes the cause and not the symptom.
```

[`/jstack-teach`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-teach/SKILL.md) is for when a summary isn't enough. It runs `/jstack-how` and `/jstack-why`, for a small change maybe just one of them, and weaves the findings into a plain explanation that builds up diagram by diagram. The "convince me" framing is worth reusing. It turns the explanation into an argument you can test instead of a tour.

It works on the agent's own choices too:

```text
/jstack-teach me why you implemented it this way and not with a queue. what did you trade off, and why?
```

Teaching helps the agent as much as you. An agent that has to explain its work must read the code and back each claim with evidence, instead of stating it confidently and moving on.

## Rebuild your own context with `/jstack-recall`

```text
/jstack-recall catch me up on the export work from last week
```

[`/jstack-recall`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-recall/SKILL.md) reconstructs context from scoped project chats and the shared record, then hands back a brief on where things stand and what is next. Missing workspace identity, pages or full tool records stay explicit gaps. A supplied state capsule skips repeated chat mining. Use it to load earlier context before handing over the new input:

```text
/jstack-recall my work on the virtualized list from yesterday, then read this bug report.
```

If you want to resume one specific chat, that's the Session pickup playbook below, not `/jstack-recall`.

## Take over prior work with Session pickup

When another agent (or you, last week) left a branch mid-flight:

```text
/jstack-juan-mode take over this branch. read the decision log, figure out what's done, and continue from there. don't redo finished work.
```

The [Session pickup playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/session-pickup.md) treats the prior trail as authoritative. It reconstructs the branch state and decisions, names the resume point, and verifies inherited claims against the original goal instead of re-deriving everything from scratch.

**Pitfall:** don't skip this page's skills because "the agent will read the code anyway." An agent that starts editing without a traced model tends to fix the symptom at the first plausible spot. `/jstack-how` first is cheaper than the second bug.

Next: [Design the change](./04-design.md).
