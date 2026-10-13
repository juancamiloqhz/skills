# Investigation alignment review

Follow-up to PR #30's initial `d7eb9dbdeb7dae3911da1cacf68fdc0d7589f368` snapshot, after the user requested justification of the remaining differences. This review covers both entrypoints and all 14 reference files against `11713c683fe4add4fd403ea880580abbc9e0875f`.

## Corrections

How's explainer again names Mermaid for structured flows and ASCII for simpler relationships. Its only rendering exception is an explicit requirement from the executing host. The T3 instructions in this session require HTML preview/render for user-facing diagrams; that justifies a conditional exception, not removal of the upstream default for every host.

Why again specifies one investigator per available evidence category, with one source/MCP per investigator. The added automatic expansion into multiple investigators within a category is removed from the entrypoint and source index. The investigator prompt again names the one-investigator-per-category design. Upstream does not fully specify selection among multiple relevant sources in a category; this review preserves that limitation instead of inventing an algorithm. The existing actual-search and coverage reporting rules still apply.

Configured model resolution, inherited selections, supported read tools, capacity limits, owned findings paths and checked evidence remain. These follow the existing shared investigation contract and recorded user decisions. No shared contract or caller was redesigned.

## Invocation metadata

Retain the omission of `disable-model-invocation: true` in How and Why. It now has a concrete compatibility basis: our approved caller design discovers these helpers through the provider catalog, and a Claude Code coordinator cannot ordinarily invoke a flagged helper merely because another skill instructs it to. The user authorized restoring metadata unless an incompatibility was demonstrated. This is that exception, not a claim that the field is meaningless or Cursor-only.

Provider evidence checked on 2026-10-13:

| Provider | Evidence | Consequence for this change |
| --- | --- | --- |
| Claude Code 2.1.296 | [Official invocation documentation](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill) describes hidden discovery and blocked agent calls. The installed code checks the flag against `userTypedThisTurn`. The extracted guard rejects the flagged/non-user-typed case and permits passage through this gate for the explicit case. | A catalog-driven juan-mode call does not establish that the user typed How or Why in the current turn. Restoring the flag would block this calling route. |
| Cursor Agent 2026.10.01-e373342 | [Official skills documentation](https://cursor.com/docs/skills#disabling-automatic-invocation) describes explicit slash invocation and exclusion from automatic context. | The common catalog assumption cannot be taken for granted with this field enabled. No complete Cursor session was tested. |
| Codex CLI 0.162.1 | [Official skill policy documentation](https://learn.chatgpt.com/docs/build-skills) uses `agents/openai.yaml` with `allow_implicit_invocation: false`, while retaining explicit invocation. Local skill-creator guidance documents the same setting. | This does not establish that the pstack frontmatter field enforces equivalent behavior. No new Codex policy file was added or discovery-equivalence claim made. |
| OpenCode 2.0.28 | [Official V2 documentation](https://dev.opencode.ai/v2/docs/skills/#frontmatter) says the frontmatter flag hides the advertised skill while retaining explicit loading by ID. | Explicit loading and catalog visibility differ. No complete OpenCode session was tested. |

The tradeoff is explicit: these two helpers remain eligible for automatic model selection. This does not reproduce pstack's explicit-only policy. Keeping one shared package and the existing catalog-based callers requires this exception today; a provider-specific invocation adapter would be separate work. Reading a hidden skill's files to evade Claude's rejected invocation is not a supported workaround.

## Local guard probe

[check_claude_gate.py](check_claude_gate.py) reads the installed Claude Code 2.1.296 binary and extracts only its invocation guard. It executes that code with stubs for error wording and a sentinel before unrelated permission checks. [claude-gate.json](claude-gate.json) retains binary and extracted-code hashes plus all four combinations of flag and user-typed state. The flag blocks only the non-user-typed case at this gate.

```bash
python3 -B research/jstack/evaluations/investigation-restoration/alignment-review/check_claude_gate.py --binary /path/to/claude-2.1.296
```

This is a test of installed guard logic, not an end-to-end provider invocation. Passing the guard does not prove that discovery, other permissions or model execution succeed. The probe starts no agent session, performs no model request, installs no skill and changes no saved settings. It deliberately refuses other versions, whose code needs separate inspection. Official documentation establishes the supported explicit invocation route; the probe corroborates the local rejection condition.

## Final comparison and validation

[source-comparison.json](source-comparison.json) records the current 16-file comparison and both exact licenses. Reproduce it with the existing comparison script:

```bash
python3 -B research/jstack/evaluations/investigation-restoration/compare.py > /tmp/jstack-investigation-alignment.json
cmp research/jstack/evaluations/investigation-restoration/alignment-review/source-comparison.json /tmp/jstack-investigation-alignment.json
```

[checks.json](checks.json) records package validation, Markdown and link checks, protected-file comparisons and final hashes. The parent inspected all current pinned-source differences, including the restored diagram default and category rule.

The earlier four How children and eight Why children were run against the initial PR snapshot. Their reports and hashes remain unchanged. They covered one source per Why category and source explanation, but did not test the revised diagram wording or multiple-source selection. No fresh agent workflow is claimed by this follow-up; the corrections have source-level checks, and invocation metadata has documentation plus the bounded guard probe. Live connector compatibility, all-provider discovery and end-to-end explicit/workflow invocation remain unverified.
