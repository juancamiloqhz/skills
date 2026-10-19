# Recipes and pitfalls

Prompts worth copying, then the mistakes everyone makes once. Swap in your own paths and finish conditions. The recipes are deliberately informal. That's how they get typed in practice, and the skills read intent fine.

![She tastes a finished dish while robots cook from a recipe box, with pinned cards reading /how, /tdd, and /loop above the counter.](./images/recipes.jpg)

The illustration retains the original command labels. Use the jstack commands in the text; Cursor's `/loop` is not a jstack command.

## Understand an unfamiliar subsystem

```text
use /jstack-how first to understand how this initialization works. then use /jstack-why to figure out why it broke recently.
```

Mechanics first, history second. Each skill's report tells you which sources it searched, so you know what the answer is grounded in.

## Restate a noisy report before touching code

```text
/jstack-juan-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.
```

A misreading shows up in the restatement, where it costs one message to correct. Keep your own theory to yourself until the agent has stated its own.

## Prototype before you pick

```text
/jstack-juan-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```

You pick from things that run, not from descriptions. The agent answers its own layout and timing questions along the way.

## Turn a settled design into a plan

```text
/jstack-juan-mode turn this design into a plan. small verifiable PRs, each with its own proof.
```

Ask only after the design settles. The plan is the deliverable, and it names the playbook that will execute it.

## Get a second opinion on a design

```text
ask /jstack-arena for a second opinion on this thread and our approach
```

Your current design becomes one candidate among several, and the synthesis tells you whether the panel found something better or confirmed what you had. It costs little next to a design that is expensive to reverse.

## Check independent slices in parallel

```text
/jstack-swarm check every package under packages/ against its check.sh. one worker per package. one report.
```

Each worker owns one package. The parent waits for every slice and returns one `PASS`, `ISSUES`, or `BLOCKED` report instead of raw worker dumps.

## Review a branch skeptically

```text
/jstack-interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's an actual bug or regression in behavior.
```

The qualifiers do real work. "don't change anything yet" keeps it read-only, and the nitpick rule pre-filters the noise so `Act on` findings are worth your time.

## Fix a bug through a failing test

```text
/jstack-juan-mode repro the duplicate write first. if there's a cheap test path, /jstack-tdd it. then fix and rerun.
```

"if there's a cheap test path" matters. Forcing a test through brittle mocks proves less than running the real command, and the playbook is allowed to say so.

## Repro and fix a report with proof

```text
/jstack-juan-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.
```

"if it repros on main" lets the run stop early when the bug is already gone. The video lets you check the fix before you read the diff.

## Vet a number before you post it

```text
/jstack-benchmark-checklist vet this 40% speedup before it goes in the pr description
```

You get faster, slower, no measurable difference, or inconclusive, with the run count, the range, and what limits the number.

## Stop correcting the same mistake

```text
/jstack-correct agents keep adding new config flags without registering them in the schema
```

The fix lands in the repo as architecture, a type, a lint, or a test, so the next agent can't make the mistake.

## Ask how without starting the work

```text
/jstack-help how do i get juan-mode to stay on every turn?
```

You get an answer, a prompt to send, and a link to the source. Nothing runs until you send that prompt.

## Keep a run honest while you're away

```text
im going to bed, keep going autonomously until every fixture passes. do not stop. keep a decision log i can audit in the morning.
```

The full contract is on the [overnight page](./07-overnight.md). The short form works once the task and finish condition are already in the conversation.

## Redirect a drifting run

Steering prompts are one line:

```text
i said the goal is to repro. i did not ask for a fix yet.
```

```text
apply prove it works. show me the real output, not the build log.
```

```text
/unslop that, no emdashes
```

You rarely need more words. You need the right name, and [the principles page](./08-principles.md) is the vocabulary.

## Get the reply in plain words

```text
/jstack-bro
```

That's the whole prompt. [`/jstack-bro`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-bro/SKILL.md) restates the last message like one human talking to another, no jargon, shorter. Use it when a reply is technically thorough and you still don't know what it said.

## The pitfalls

- **Enumerating skills in the prompt.** "use /jstack-how then /jstack-architect then /jstack-arena" reorders steps the playbook already sequences. State the goal and constraints. Name a skill only to override a default.
- **A vague finish condition.** "make it better" gives the run nothing to check. Give a command or artifact that can pass or fail.
- **Leading with your theory of the cause.** The agent searches wherever you pointed. Ask it to restate the problem first, then share your hunch.
- **Taking the first design.** One attempt locks in the first shape the model thought of. Ask for prototypes or `/jstack-architect` and pick from evidence.
- **Polishing an abstract plan.** Adversarial review of a plan with no code behind it invents risks that will never happen. Settle the open questions with prototypes, then review what got built.
- **Parallel agents in one worktree.** They overwrite each other, and nobody can tell which agent changed what. Use app-owned isolated workspaces, or say "own worktree per attempt".
- **Looping before you trust the loop.** A loop that can't verify its own work only makes unchecked work faster. Get the verification skill working first.
- **Trusting an unvetted number.** A warm cache or a skipped code path can fake a speedup. Run `/jstack-benchmark-checklist` before the number goes anywhere.
- **Correcting the same mistake by hand.** A correction in chat helps one run. `/jstack-correct` fixes the repo so no later run repeats it.
- **Using `/jstack-arena` for coverage.** `/jstack-arena` repeats one design or code brief, then picks a base and grafts the best parts. `/jstack-swarm` partitions slices or declared race arms and aggregates one report.
- **Accepting every review comment.** Bots and humans both file real catches and noise in one list. `/jstack-interrogate` sorts findings into act-on and dismissed buckets with reasons, and you can override either way.
- **Treating Auto as inheritance.** `inherit-parent` preserves the parent provider, model and effort. Auto is a concrete provider/catalog choice, not a portable alias. [Setup](./01-setup.md) covers the roles.
- **Reporting success off a green build.** A build proves it compiles. Ask for the real command, flow, stored value, or profile, and expect the evidence in the reply.
- **Writing a `SKILL.md` freehand.** Route it through the [Authoring or modifying a skill playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/authoring-a-skill.md) so validation and review happen.

That's the guide. If you skipped ahead, go back to [setup](./01-setup.md) and run one real task. The habits stick from use, not from reading.

Back to the [guide index](./README.md).
