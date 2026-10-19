# Automate me evaluation

Source: `pstack/skills/automate-me/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. Local: [jstack-automate-me](../../../../skills/jstack/jstack-automate-me/SKILL.md). [Adaptation record](../../adaptations/automate-me.md).

The port preserves the seven-step flow from finding a personal mode through feedback and authorized publication. It uses the host's authoring helper and scoped history tools. This evaluation checks update preservation and evidence handling, not whether a fictional preference profile matches a real person. Upstream's subjective user review remains the acceptance step for generated personal modes.

## Executed update exercise

[make_fixture.py](make_fixture.py) creates a new isolated Git repository, refusing an existing destination. It contains a categorized `.agents/skills/river/river-mode` package, Codex invocation metadata, a referenced review helper and an unrelated bundled-router sentinel. The personal mode has a fixed October 10 commit date. Supplied slice findings include repeated short-answer/example preferences, contradicted delegation requests, a duplicated assistant claim about automatic merging and model effort, an older preference, and an unrelated workspace's publication request. Direct current answers authorize only a response-style draft and explicitly supply the history findings instead of live mining.

One fresh native authoring evaluator read Automate me; a baseline received the same task without it. Both inherited the parent GPT-6-astra/high runtime. Each used a separate generated repository and the real supplied Codex skill-creator and Unslop instructions. The with-skill run also read Juan-mode for shape without activating it. No operational reader roles, real chats or external apps were used.

Both runs made the same one-paragraph edit:

```diff
-Use short paragraphs. Use tables when comparing options.
+Use concise paragraphs. Include one practical usage example per proposed change. Use tables when comparing options.
```

Both retained the mode's path, name, description, invocation metadata, existing table preference, review/process sections and working helper reference. They declined the contradicted delegation signals, duplicated assistant assertions and foreign-workspace instruction. The with-skill run checked the mode's last Git edit and excluded the October 1 statement from the update window; the baseline discarded that statement as superseded by the current answer. The parent inspected both reports and repository diffs rather than relying only on completion messages.

No commit, new worktree, installation, activation or publication occurred in either fixture. The only tracked change was the personal mode's response paragraph. Both stopped with the concrete draft for feedback. User feedback and approval were not simulated. There is no superiority, speed or token-efficiency claim from this one pair.

The external author's documented `python` validator command could not run because the executable was absent. Retrying with `python3` ran the validator but rejected the existing `disable-model-invocation` field. Both evaluators preserved the requested invocation policy and disclosed this failure. Scope/whitespace checks passed; the with-skill run also parsed frontmatter and Codex metadata and verified the helper link. These narrower checks do not turn the generic validator failure into a pass.

## Supplied boundary assessment

[Cases](cases.json) record the prompts. An independent reader compared the entrypoint with its pinned source and assessed eight hypothetical cases without executing them: unspecified update/fresh intent, multiple matching modes, missing edit history, no multi-select tool, unavailable mining/reader role, a global destination outside Git, every-turn activation, and a narrow commit-message workflow.

The review retained the original phases and found no removed phase or unnecessary structural redesign. It confirmed explicit precedence over generic authoring defaults for destination and invocation. It identified two wording gaps: a host might lack a usable structured question tool, and the inherited repetition guardrail could be read as rejecting a current explicit preference. The final text supplies ordinary short chat questions as the fallback and limits the repetition rule to inferred history. The reviewer reread the final text and confirmed both findings were resolved. No interactive questioning or activation mechanism was exercised by these hypothetical cases.

## Source and packaging checks

The full diff was compared with the frozen source. All headings, six mining signals, eight suggested clusters, both routing exclusions and the substantive existing-mode rules remain. Necessary runtime changes and the historical-inference clarification are recorded in the adaptation. The license is an exact copy. Recall's existing route now names `jstack-automate-me`, retaining availability and task-scope checks.

Four packaging tests passed. The documentation checker reported 55 skills, 31 commands, 24 principles, 23 playbooks and zero problems; guide coverage remains pending. Manifest loading, unchanged existing mappings/checkpoint, new research links and explicit-invocation metadata passed inspection. The generic Codex validator also rejects the new entrypoint's retained source flag; a temporary copy omitting only that field passes its remaining checks. This is qualified validation, not installed-discovery proof. Existing model configuration, Juan-mode, review decisions and the upstream reviewed checkpoint remain unchanged.

## Reproduce

```sh
run_dir=$(mktemp -d)
python3 -B research/jstack/evaluations/automate-me/make_fixture.py "$run_dir/with"
python3 -B research/jstack/evaluations/automate-me/make_fixture.py "$run_dir/without"
```

Give fresh evaluators case 1, their assigned root, and `answers.md`/`supplied-findings.json`. Only the with-skill evaluator gets the Automate me entrypoint and Juan-mode shape reference. Supply the actual host authoring and Unslop paths. Permit writes only to the assigned fixture and report; forbid real history, external apps, additional children, installation, publication and reads of the generator, expected outcomes or another run. Supplied findings replace mining and direct answers replace question rounds for this exercise.

Inspect the diff against the fixture's initial commit. Only the response paragraph should change; no other tracked file, metadata or existing rule should change. Verify the referenced review helper still exists and the mode stays explicit-only. Check the report's evidence decisions and its stop at a local draft. Case 2 is a supplied-evidence assessment; it does not prove runtime support.

Keep only this report, prompts and generator. Raw reports and generated repositories remain under `/home/ubuntu/.cache/jstack/automate-me-20261019/` while the review is pending; they are not durable documentation dependencies.

## Limits and normal use

Live history mining, configured reader dispatch, interactive question delivery, new-mode generation, worktree/PR publication, global destinations and installed-provider discovery were not exercised. T3 history retains the [Recall evaluation's limitations](../recall/README.md#live-tool-inspection-and-limits): list metadata does not guarantee workspace identity; a zero-item metadata-only read is rejected; search is bounded and activity is summarized. Those limitations require explicit gaps, not invented history. This port adds no provider persistence guarantee.

After merge and manual installation, try `$jstack-automate-me Help me create a personal mode with short explanations and practical examples. Draft only.` It should identify the intended personal mode, gather missing preferences and show a draft. Creating a personal mode does not activate it or modify jstack's shared Juan-mode router. A real user's review determines whether the resulting rules fit them.
