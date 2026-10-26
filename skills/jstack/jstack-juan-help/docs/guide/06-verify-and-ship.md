# Verify the result and open a PR

"It compiles" is not evidence. The [Prove It Works principle](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-principle-prove-it-works/SKILL.md) makes the agent check the real artifact before it reports success, and your job is to make "the real artifact" checkable. This page covers stating a finish condition, vetting a measured number, generating a verification skill for your app, formally verifying a property tests rarely reach, opening the PR, and driving it to merged.

Verification is the slowest step in most agent work, because it's the step that usually waits on a human. Make the agent able to do it, and you stop being the bottleneck. Skip it, and running more agents only gets you more unchecked work to review.

![A prototype plane flies a real test course while she times it with a stopwatch and robots film and checklist the run; the terminal reads verify: pass, evidence: captured.](./images/verification.jpg)

The illustration retains the original command labels. Use the jstack commands in the text; Cursor's `/loop` is not a jstack command.

## State the finish condition up front

Put what done means in the first prompt, in whatever words fit:

```text
/jstack-juan-mode add json output to this command. text output stays byte-identical, the json parses, both run against the sample project. show me the evidence.
```

Now the agent has three checks it can run, not a mood to satisfy. When the reply comes back, it should carry the exact commands and outputs. If a check couldn't run, a good reply says "inconclusive". A confident reply without evidence is a warning sign.

Match the check to the change:

- A CLI change runs the real command.
- A UI change walks the changed flow in the running app. When it must match a reference pixel for pixel, the [Visual parity playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/visual-parity.md) diffs screenshots against a frozen baseline instead of judging by eye.
- A parser or migration replays a saved input.
- A perf change compares before and after profiles.
- A storage change reads back the written value.

Ask for the proof as an artifact you can inspect yourself: the failing test and then the passing one, a before-and-after video, the trace, the screenshot. If the fix already merged, ask for the same check again on main. An artifact beats a plausible explanation, because you can challenge it without replaying the whole run.

For a small diff you don't fully trust, [`/jstack-blast-radius`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-blast-radius/SKILL.md) finds what it could break elsewhere. It finds the one fact that makes the change safe and proves that fact by running code, not by arguing for it.

## Vet a measured number with `/jstack-benchmark-checklist`

A before-and-after number is the easiest evidence to get wrong by accident. A warm cache, a debug build on one side, or work that never ran inside the timed region can each produce a convincing speedup. Before you report or act on a number, type:

```text
/jstack-benchmark-checklist vet the export speedup before it goes in the pr
```

[`/jstack-benchmark-checklist`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-benchmark-checklist/SKILL.md) asks seven questions and wants evidence from a run for each:

1. What limits the number, and why isn't it double?
2. Did every side run tuned the way production runs?
3. Does the result break a physical limit, like disk bandwidth or core count?
4. Did anything error or return wrong output?
5. Does it reproduce over alternating runs, with a median and a range?
6. Does it matter end to end, on the path a user waits on?
7. Did the work actually happen inside the timed region?

The verdict comes back as faster, slower, no measurable difference, or inconclusive, with the run count, range, and limiter. It says inconclusive when it can't name the limiter or a side ran untuned. `/jstack-juan-mode` already runs the checklist inside the Perf issue and Hillclimb playbooks, so you type it yourself when you measured something outside them, or when someone else's number looks too good. It's the working form of the [Explain the Number principle](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-principle-explain-the-number/SKILL.md).

## Create a project verification skill

The UI bullet above hides a real requirement. The agent needs a scripted way to drive your app. If your project has one, great. If not, run:

```text
/jstack-create-verification-skill
```

[`/jstack-create-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-verification-skill/SKILL.md) interviews the repository, not you. It works out what a user touches, how the app launches locally, what can drive it (an existing harness first, otherwise browser and CDP, a PTY, or plain HTTP), what evidence proves behavior, and whether two instances can run side by side. It asks you only what the code can't answer.

It writes `.agents/skills/verify-<app>/` by default, plus an automatic project-local `.claude/skills/verify-<app>` link with conflicts preserved, agent-facing instructions with exact Launch, Doctor, Drive, Evidence, and Cleanup sections, a Helpers section for any script it ships, plus a feature map under `features/` that indexes what the app does and what result proves each feature works. The skill ships a [worked feature-map example](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-verification-skill/references/feature-map-example/) with a README index and one file per feature using the four required H2s. Before handing it over, the generator proves the skill once end to end: launch, doctor check, drive one feature, capture evidence, clean up, then confirm the evidence survived the cleanup. If that proof fails, don't use the output.

From then on, "verify it in the app" is a step any agent can execute, in this repo, with no setup conversation. Name it in the prompt when you want the proof in a specific form:

```text
/jstack-juan-mode build the bulk-archive action. use /verify-<app> to verify your changes and show me a video and screenshots as proof.
```

```text
/jstack-juan-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.
```

Once the verify skill works, a [`/jstack-swarm`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-swarm/SKILL.md) can split a full pass by feature-map entry and aggregate the results. A swarm of verifiers also confirms a perf win over a big enough sample, or fuzzes the app for regressions before a PR ships.

Treat the verification skill as infrastructure, not a one-off. Commit it, so every person and every agent on the team drives the app the same way. Then [build the lever](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-principle-build-the-lever/SKILL.md). When agents keep writing throwaway scripts to click through the app, ask for a small control CLI that the skill calls instead. Agents spend fewer tokens, and every run becomes repeatable. A CLI that agents use well has these traits:

- A few composable commands, each doing real work, rather than many thin ones.
- A `--dry-run` option on anything destructive.
- Subcommands that reveal features gradually instead of all at once.
- Error messages that say what to do instead.
- Rich `--help` text.
- Machine-readable output, such as JSON.

While you're there, make the dev setup repeatable too: seeded data, test users, and one command that brings the environment up the same way every time.

## Keep the verification skill honest

Apps change, and feature maps go out of date. Run this at least once a day, ideally from a scheduled automation so nobody has to remember:

```text
/jstack-maintain-verification-skill
```

[`/jstack-maintain-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-maintain-verification-skill/SKILL.md) audits the generated skill: one read-only source reader per feature in parallel, then one live pass that drives every mapped feature. It ends in exactly one of three outcomes. `clean` means full coverage and nothing to ship. `changed` means one PR of proven corrections, confined to the verification skill's own directory. `blocked` names the blocker. It never edits product code. If the live pass catches a product regression, it reports the regression instead of hiding it with a doc edit.

## Prove a property with a formal verification skill

A verification skill proves the paths you drive. Some bugs live on paths nobody drives: two retries that overlap, a lock that expires mid-write, a state change that arrives out of order. Tests rarely reach those cases. For code where such a bug is costly, run:

```text
/jstack-create-formal-verification-skill
```

[`/jstack-create-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-formal-verification-skill/SKILL.md) picks the target from the code: a promise the code makes, where a break harms users and tests rarely reach the case that breaks it. It picks the strongest target, not the easiest to verify. Name an area or a bug to start there instead:

```text
/jstack-create-formal-verification-skill the job lease and retry logic. a job must never run twice at once. leave product code unchanged.
```

The question picks the tool. Whether events can happen in a bad order suits a model checker over a small model of the design, and TLA+ is the default for that in any language. Whether the code behaves for every input suits a verifier that runs on the code. If no verifier runs on your language, the agent says so and tests the real code with generated inputs, not a hand-written model of the function. Those tests are not a formal proof. An explicitly requested proof remains unmet. A property that must hold at every size can need a proof. Missing tools remain manual prerequisites, and the agent explains its choice and limits.

It checks one property and shows that property failing on a broken variant of the code, because a check you've never seen fail proves nothing. When the current code already breaks the property, you get the counterexample in your code's terms. The property stays as stated, so the finding stays a finding. Product code doesn't change unless you ask.

It writes a project-local skill, normally `.agents/skills/verify-<area>-formal/`, with the automatic relative `.claude/skills/` link and preserved conflicts. The skill tells the next agent which files and functions a check covers, how to run it, and how to distinguish a real bug from a modeling error. Before handoff, the generator follows it on a scratch change that breaks the property, requires the check to catch the break, then restores the original baseline. An unrun verifier or mutation leaves the result a draft.

The generated skill records the commit where each check last matched its covered code. After merges or refactors, revisit the code correspondence and rerun the required checks before advancing that commit. A passing check against stale code assumptions is insufficient. The handoff states the tool, bounds, findings, run command and exclusions. A pass covers only the stated model, bound or tested inputs.

After merges or refactors that skipped the check, run [`/jstack-maintain-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-maintain-formal-verification-skill/SKILL.md). It reads changes since each recorded sync commit, updates the verification from current code, and reruns it. Passing updates must still detect a broken real-code variant. Failures are replayed on real code to distinguish drift from a bug. A check can be both updated and reveal a bug; blocked checks keep their previous sync commits. Product fixes remain separate.

## Open the PR

```text
/jstack-juan-mode open the pr. small ordered commits, evidence in the description.
```

The [Opening a PR playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/opening-a-pr.md) works from a worktree, rebases the work into small ordered commits, cleans the diff, unslops the prose, and returns the PR link. Five narrow PRs beat one fat one, and stacked follow-ups beat a growing branch.

## Drive the PR to merge-ready with Babysit

An open PR starts collecting blockers immediately. Checks fail, reviewers comment, trunk moves. Hand that churn to the [Babysit playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/babysit.md):

```text
/jstack-juan-mode babysit this pr. get it green.
```

Babysit uses the supported host PR watcher when available, or its documented read/check procedure and takes blockers in order: conflicts, then review threads, then CI. Every known fix batches into one push, so the checks restart once instead of after every fix. The comment triage is skeptical, because humans and bots file real catches and noise in the same list. A real finding gets a fix, and noise gets dismissed with the disproof posted on the thread. When all you want is status, ask smaller and Babysit answers without starting the loop:

```text
/jstack-juan-mode check on pr 123. anything outstanding?
```

Babysit stops at merge-ready. It never merges, even with everything green, because merging is a different decision.

## Land the stack with Shipping

Green is not the same as safe. When you're ready to land, say so:

```text
/jstack-juan-mode land the stack.
```

The [Shipping playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/shipping.md) verifies each PR independently before it arms anything. One fresh agent per PR proves the behavior live, and the agent that judges a change is never the one that wrote it. Then Shipping lands only the contiguous verified run from the bottom, one PR at a time through GitHub or Origin as resolved by the procedure, and reports the first PR that breaks the chain. Live Origin integration remains unverified. A verified PR sitting above an unverified one waits, because merging it would pull the gap in underneath.

Next: [Run work while you sleep](./07-overnight.md).
