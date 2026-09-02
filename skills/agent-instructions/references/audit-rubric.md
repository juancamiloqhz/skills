# Audit Rubric

Use this rubric for every audit, creation, or refactor. It applies the progressive-disclosure ideas in Matt Pocock's [AGENTS.md guide](https://www.aihero.dev/a-complete-guide-to-agents-md) as context-sensitive heuristics, not universal size or structure rules. The unit of analysis is an instruction, not a file or section.

## Evidence Standard

Classify the basis for each material conclusion:

- **Observed**: directly supported by files, configuration, scripts, executable behavior, or official harness documentation.
- **Inferred**: likely from repository structure or conventions but not explicitly established.
- **User-owned**: a policy or preference only the repository owner can decide.
- **Proposed**: a new convention offered for consideration rather than claimed as existing fact.

Do not present an inference or generic recommendation as an observed repository rule.

For each material instruction, record enough information to answer:

| Field | Question |
| --- | --- |
| Source and scope | Where is it written, and which work should it govern? |
| Evidence | What repository fact or owner decision supports it? |
| Finding | Is it correct, current, unambiguous, discoverable, and actionable? |
| Carrier | Is this the mechanism that should deliver or enforce it? |
| Disposition | Keep, rewrite, scope, move, automate, consolidate, remove, or ask? |
| Impact and confidence | What fails if ignored, and how certain is the conclusion? |

## Audit Checks

### Correctness and currency

- Verify paths, commands, package names, tool names, branch names, and referenced files.
- Compare prose with executable configuration and scripts.
- Flag stale initialization instructions and completed migration rules.
- Distinguish current workflow from historical explanation.

### Conflicts and precedence

- Compute the effective instruction chain for each relevant working directory.
- Identify direct contradictions and softer mismatches between parent, child, override, imported, and local instructions.
- State which rule wins according to the harness instead of merely listing both.
- Treat conflicting user-owned policy as a decision request, not an invitation to invent policy.

### Scope and loading cost

- Root instructions should usually be universal, behavior-changing, and non-obvious or costly to rediscover.
- Safety constraints, output contracts, and demonstrated recurring failures can justify always-on placement even when verbose.
- Move directory-specific rules closer to the governed files when the harness supports scoping.
- A small file can still be poor; a large file can still be justified. Measure relevance, not only line count.

### Discoverability and actionability

- A pointer must say what the target contains and when the agent should read it.
- Instructions should include triggers, concrete actions, and completion criteria where ambiguity would change behavior.
- Flag advice that is true but cannot affect a decision or be verified.
- Flag a normal Markdown link that is being mistaken for an automatically loaded instruction.

### Carrier and enforceability

Choose the carrier that delivers the rule at the right time:

| Carrier | Best fit |
| --- | --- |
| Root `AGENTS.md` or `CLAUDE.md` | Universal repository policy and essential routing |
| Nested or override instructions | Directory- or subtree-specific policy and deliberate precedence |
| `.claude/rules/` with paths | Claude-only conditional rules for matching files |
| Referenced repository document | Detailed knowledge with an explicit read trigger |
| Skill | Reusable or specialized procedure invoked for a class of tasks |
| Linter, formatter, hook, CI, or config | Deterministically enforceable checks |
| User/local instructions | Personal preference or machine-specific setup |
| No carrier | Stale, redundant, contradicted, or valueless content |

Normal documentation is a valid cache, but it needs a routing instruction if the agent would not otherwise know when to read it.

### Reference quality

- Resolve local imports and links, including case-sensitive paths.
- Verify that the target still contains the promised information.
- Detect reference cycles, chains that are needlessly deep, and eager imports that recreate root-file bloat.
- Prefer one authoritative source to synchronized copies.

### Cross-harness behavior

- Do not assume Codex and Claude discover the same filenames or nested files.
- Account for overrides, configured fallbacks, eager imports, scoped rules, and size limits.
- If both harnesses are targeted, identify shared policy, harness-specific additions, and the source of truth.

## Common Smells

- **Context bloat**: specialized or explanatory material is loaded for every task.
- **Skill leakage**: a reusable procedure has been copied into repository instructions.
- **Lint leakage**: machine-enforceable rules exist only as prose.
- **Blind reference**: a link names a document but gives no read trigger.
- **Initialization fossilization**: setup or migration guidance remains after the state changed.
- **Conflicting instructions**: two active carriers demand incompatible behavior.

## Severity

- **Critical**: likely to cause destructive, insecure, or materially unauthorized behavior.
- **High**: likely to make agents execute the wrong workflow or violate an important repository policy.
- **Medium**: recurring ambiguity, stale guidance, broken routing, or avoidable context cost.
- **Low**: clarity or maintainability improvement with limited behavioral effect.

Confidence is separate from severity. A high-impact inference with low confidence should usually become a question or a narrowly stated risk.

## Report Contract

Use this structure, adjusting detail to the repository:

1. **Summary**: the most important behavioral conclusions.
2. **Effective loading**: what each target harness loads for each relevant working directory.
3. **Findings**: prioritized, evidence-backed instruction-level findings with disposition.
4. **Decisions needed**: unresolved user-owned policy only.
5. **File plan or patch**: proposed or applied changes, depending on mode.
6. **Validation coverage**: references, loading chains, byte limits, and commands checked.

Do not assign a universal letter grade. Counts and size measurements are diagnostics, not quality scores.
