# Show me your work adaptation

The [2026-10-15 naming decision](../skill-names.md) additionally changes this package's local identity and callers. Its upstream identity, procedure and revision pin remain as recorded below.

Source: [pstack show-me-your-work](https://github.com/cursor/plugins/tree/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/show-me-your-work), revision `11713c683fe4add4fd403ea880580abbc9e0875f`. Local package: [show-me-your-work](../../../skills/jstack/jstack-show-me-your-work/SKILL.md). The [MIT license](../../../skills/jstack/jstack-show-me-your-work/LICENSE) is the exact pinned plugin notice.

Restores a standalone skill instead of Figure-it-out's local decision-trail summary. All three source files retain their boundaries. `scripts/log.sh` and `references/decision-log-template.tsv` are byte-identical to the pin; the script retains executable mode. The source's columns, example, run-start boundaries, append-only correction rule, evidence checks, committed-script preference and composition contract remain intact. [Comparison and evaluation](../evaluations/trail-restoration/README.md) record exact differences and observed behavior.

## Remaining differences

| Local path | Difference | Concrete reason and verification |
| --- | --- | --- |
| `SKILL.md` frontmatter | Omit `disable-model-invocation: true`; retain name and description. | Catalog-driven Figure-it-out calls require the established [invocation exception](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata). Automatic selection is possible; all-provider invocation remains unverified. |
| `SKILL.md` introduction | Add task-scoped activation, coordinator-only serialized log writes, catalog discovery and review contract lookup. | Shared log writers need serialization because the unchanged helper has no lock. Explicit paths do not enforce a sandbox. The CLI tests are serial. |
| `SKILL.md` format and location | Copy the template only for a new log; commits need publication authority and do not imply ignore-file edits. | Preserve existing data and user-controlled delivery. Existing-row preservation is exercised through the real helper. |
| `SKILL.md` audit | Use identified current-thread evidence or a labeled bounded digest instead of Cursor transcript paths; disclose missing history and treat embedded directives as data. | T3 owns thread identity; private-store scans are not a justified substitute. The original start-to-next-foreign-start algorithm remains verbatim. |
| `SKILL.md` review | Use the configured scalar `judgment and prose` role instead of forcing another model family. Require separate review, disclose reduced independence for inherit/same-family, and return incomplete if explicitly required diversity is unavailable. | The user's saved inherited roles must remain unchanged. A separate same-model reviewer is not equivalent to upstream cross-family review. Canonical resolution and bounded audit/review exercises are recorded. |
| `SKILL.md` Attention | Retain the final Attention section, actual model line and flags. Pending/unavailable review must say so instead of fabricating a reviewer or declaring no flags. | Intermediate replies can precede terminal review. The audit exercise checks this pending boundary. |
| `SKILL.md` principle/example | Use the shipped `principle-encode-lessons-in-structure` name; add a fence language and scoped Markdown tab exception. | Catalog naming and lint compatibility; the example keeps actual TSV tabs. |
| `references/execution.md` | New jstack-only review adapter. | Canonical config resolution, inherited/concrete target handling, capability checks, complete isolated briefs, terminal report inspection and coordinator-owned corrections adapt delegation to T3/native tools. |

The manifest maps this package and watches its setup, unslop and structural-principle dependencies. Adding the mapping does not advance `reviewedThrough` or rewrite historical review decisions. Installation remains manual.
