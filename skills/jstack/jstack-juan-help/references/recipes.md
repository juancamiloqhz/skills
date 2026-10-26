# Prompts worth copying

Swap in the real paths, skills, and done checks. Informal wording works.

## Understand

- `/jstack-juan-mode read <thread>. restate the underlying issue in your own words, in plain english.`
- `/jstack-in-your-own-words <long or messy ask>`
- `/jstack-sharpen <the prompt you're about to send>`
- `/jstack-juan-mode investigate why <symptom>. give me what we know, what data you used, and your best hypotheses. don't change any code yet.`
- `use /jstack-how to understand <subsystem>. then use /jstack-why to find out why it broke recently.`
- `/jstack-recall my work on <topic> from last week, then read <issue>.`
- `/jstack-teach me why you implemented it this way and not <other way>. what did you trade off?`
- `/jstack-juan-mode take over this branch. read the decision log, find what's done, and continue. don't redo finished work.`

## Build

- Bug: `/jstack-juan-mode <symptom>. repro first, then fix and verify.`
- Bug in an app: `/jstack-juan-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.`
- Bug with a cheap test: `/jstack-juan-mode repro <bug> first. if there's a cheap test path, /jstack-tdd it. then fix and rerun.`
- Feature: `/jstack-juan-mode add <behavior>. <current output> stays byte-identical. verify both.`
- Refactor: `/jstack-juan-mode move <code> into one module, zero behavior change. record the current output first and prove it's unchanged after.`
- Perf: `/jstack-juan-mode <operation> takes <time> on <fixture>. trace it, fix the measured cause, show me before and after.`

## Design and plan

- `/jstack-juan-mode prototype a few options for <feature>. take screenshots or videos for me to compare.`
- `/jstack-juan-mode we need <feature>. /jstack-architect it first, and answer open questions with prototypes. let me review before proceeding.`
- `/jstack-juan-mode write a tutorial for how i would use <new package> first. then /jstack-teach me why it beats the current one.`
- `ask /jstack-arena for a second opinion on this thread and our approach.`
- `/jstack-juan-mode turn this design into a plan. small verifiable PRs, each with its own verification steps.`
- `/jstack-juan-mode plan the migration of <library> to <target>. small verifiable PRs. the result must match the original exactly, bugs included.`

## Review and ship

- `/jstack-interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's a real bug or regression.` Read the dismissals too.
- `/jstack-create-formal-verification-skill prove <property> holds in <module>, even when <steps> interleave or retry.` Report the scope and missing prerequisites. After merges or refactors, follow the generated skill's correspondence-review and rerun instructions before advancing its sync commit. Formal-maintenance support remains deferred.
- `/jstack-swarm check every package under <dir> against its check script. one worker per package. one report.`
- `/jstack-juan-mode open the pr. small ordered commits, evidence in the description.`
- `/jstack-juan-mode babysit this pr. get it green.` For status only: `/jstack-juan-mode check on pr <number>. anything outstanding?`
- `/jstack-juan-mode land the stack.`

## Away and back

- `/jstack-juan-mode im going to bed. <goal> in a fresh worktree off <base>. done means <checks>. keep a decision log. don't ask me before committing. continue until done. if you're truly stuck after a few hours, stop and write up why.`
- `/jstack-show-me-your-work catch me up on what you did last night.` Read its Attention section first.
- `/jstack-ketchup` catches you up on this chat since your last message and lists every call that waits on you. It reports without resuming work.
- `/jstack-juan-mode full autopilot on this queue. each item is independent.`
- `/jstack-juan-mode autopilot these changes but stack them, don't ship. i'll land the stack.`
- `/jstack-reflect capture what we learned so the next run doesn't repeat it.` Approve only edits that change a future decision.
- `/jstack-bro` restates the last reply in plain words.
