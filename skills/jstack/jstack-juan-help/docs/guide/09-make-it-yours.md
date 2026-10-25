# Make it yours

Juan-mode adapts a specific working style. The playbooks, routing, and model roles underneath it work just as well with yours. This page covers generating a personal mode, capturing lessons from a session, fixing the repo so agents stop repeating mistakes, authoring a focused skill, and testing a skill change before you trust it.

Start smaller than you think. You don't need many skills on day one, or even this whole bundle. Prompt plainly, watch where agents fail, and add a skill or a check when the same failure shows up twice.

## Generate your own mode with `/jstack-automate-me`

```text
/jstack-automate-me
```

[`/jstack-automate-me`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-automate-me/SKILL.md) combines scoped history with your direct answers, then drafts or updates the intended personal mode through the host's authoring helper and external Unslop. It preserves existing categories and uncontradicted rules. New project modes default to `.agents/skills/<your-name>-mode/SKILL.md`; personal destinations use the actual host root. Missing history stays visible. A draft-only request stops for feedback; authorized repository publication uses a worktree and PR. It does not activate the personal mode or rewrite the shared Juan-mode router.

Run it again whenever your habits drift:

```text
/jstack-automate-me update my mode skill with everything since its last edit
```

Update mode mines only the history since the skill last changed. It keeps rules you haven't contradicted, revises the ones with new evidence, and adds sections only for new patterns.

## Capture a session's lessons with `/jstack-reflect`

Right after a task that taught you something, run:

```text
/jstack-reflect that took way too long. capture what we learned so the next run doesn't repeat it.
```

[`/jstack-reflect`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-reflect/SKILL.md) sends the transcript to three parallel reviewers, then a synthesizer sorts the proposals into `Accepted`, `Rejected`, and `Backlog` and honors your existing authorization or explicit review checkpoint before applying skill changes. Approve a proposal only if it would change a future decision. One weird session is an anecdote, not a rule.

## Fix the environment with `/jstack-correct`

When you correct agents for the same mistake again and again, the fix belongs in the repo, not in your next prompt. Rank the options by how well they hold:

1. Make the mistake impossible with architecture or a better data structure.
2. Block it with types, or with a lint or CI check whose error names the fix.
3. Catch it with a test.
4. Write it down as a doc or agent rule. Nothing fails when an agent skips a rule, so this comes last.

Human review isn't on the list. A reviewer who must catch the same mistake on every PR is the problem this fixes. [`/jstack-correct`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-correct/SKILL.md) does the work:

```text
/jstack-correct agents keep calling the database client directly instead of going through the repository layer
```

It reads recent commits, reverts, review comments, and comments that explain workarounds, then groups the mistakes into classes. A class counts once it has happened twice. It fixes the most frequent classes one commit each, at the highest level that works, and proves each new check fails on a real past mistake. It also keeps a table in the agent instruction file that pairs each rule with what enforces it, so a rule that nothing enforces shows up as a repeat. The reply lists each class with its evidence, the level chosen, and why a higher level didn't work.

Run it with no argument and it finds the classes from history on its own. `/jstack-reflect` and `/jstack-correct` split the work. `/jstack-reflect` improves skills from one session. `/jstack-correct` changes the repo so a mistake class can't come back. Pair it with `/jstack-architect` when the fix is a new boundary. [Run many projects in parallel](./07-overnight.md#run-many-projects-in-parallel) has a prompt that does both across a whole repo.

## Author a focused skill

When you already know the workflow you want to capture:

```text
/jstack-juan-mode write a skill for verifying database migrations in this repo
```

Writing a skill matches the [Authoring or modifying a skill playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/authoring-a-skill.md), which uses the host's advertised skill-authoring helper, validates the frontmatter and links, and ships the result through the Opening a PR playbook. Agent-facing prose has a higher bar than human prose, because an unhelpful sentence becomes an instruction some future agent follows. Let the playbook hold that bar rather than writing a `SKILL.md` freehand.

Two special cases have their own generators. A skill that must drive your app and prove behavior is a verification skill, so use [`/jstack-create-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-verification-skill/SKILL.md) and [`/jstack-maintain-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-maintain-verification-skill/SKILL.md) instead. A skill that checks a property of your code with a model checker, a proof, or another verifier is a formal verification skill, so use [`/jstack-create-formal-verification-skill`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-create-formal-verification-skill/SKILL.md). [Verify and ship](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill) covers both kinds. After covered-code changes, follow the generated skill's correspondence and rerun instructions; the separate upstream formal-maintenance skill remains deferred.

## Write docs to a standard with `/jstack-technical-writing`

Skills aren't the only prose you ship. For docs, RFCs, readmes, PR descriptions, and commit messages:

```text
/jstack-technical-writing review the readme changes
```

[`/jstack-technical-writing`](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-technical-writing/SKILL.md) applies a layered standard. Its goal is prose that a tired engineer understands on the first read. It picks the document's mode first (tutorial, how-to, reference, or explanation), then works sentence by sentence: who does what, one thought per sentence, nothing readable two ways. Use it to review what you or an agent just wrote, or name it up front when you ask for a doc.

## Test a skill change blind

A skill edit affects every future session, so test it like the experiment it is. The same goes for adopting someone else's skill. Check that it makes the agent better on your work before you keep it.

```text
/jstack-juan-mode run the eval playbook on this skill change. same task for both variants, candidates stay blind.
```

When a skill keeps missing and you know what it should do, change and test it in one task:

```text
/jstack-juan-mode update the review skill so it flags missing migrations, and eval the change.
```

Asking for the eval up front keeps the edit honest. A fix written from one bad session tends to overfit that session, and over many edits the skill drifts. The eval catches the drift before it ships.

The [Eval playbook](https://github.com/juancamiloqhz/skills/blob/main/skills/jstack/jstack-juan-mode/playbooks/eval.md) is built around one failure mode, the observer effect. An agent that knows it's being evaluated behaves differently. So candidate agents get an organic-looking task in sanitized directories, never the words "eval" or "candidate", and never each other's existence. One judge scores all outputs under neutral labels, and chain-following gets graded from which files each candidate actually read, not from what it claims.

Read every output yourself before accepting the verdict. If you disagree with the judge, suspect the rubric before you suspect your judgment.

## Build a bot UI

Use `/jstack-make-bot-ui` when a task would benefit from a page with a button you can click later. The page lives on the computer running its helper, with optional private Tailscale access. It is not a built-in T3 button and ordinary jstack tasks do not require it.

```text
/jstack-make-bot-ui Build a button to check the status of owner/repo PR #123 and report here. Make the page reachable on my existing tailnet.
```

The bundled action reports that fixed PR's state, commit and merge time. It does not review or change the PR. Setup creates a signed T3 webhook and needs private key provisioning; the key stays on the server. HTTP delivery is separate from completed agent work. Other buttons need an explicit action contract and their own implementation and checks. Host changes follow the requested scope, and the service records how to restart or retire only its own resources.

**Pitfall:** don't edit a skill mid-task because it's misbehaving. Fix it in its own PR and keep the task moving. A skill edit that ships tangled into feature work is invisible to review and impossible to evaluate.

Next: [Recipes and pitfalls](./10-recipes-and-pitfalls.md).
