# Jstack research

Archived on 2026-10-10. This index connects the original pstack research to the shipped jstack setup skill and proposed workflow work.

## Current status

[`setup-jstack`](../skills/setup-jstack/SKILL.md) shipped in [PR #2](https://github.com/juancamiloqhz/skills/pull/2), followed by [the paragraph-formatting fix](https://github.com/juancamiloqhz/skills/pull/3). It provides model configuration and validation only. `juan-mode` is the planned workflow entrypoint, starting with a read-only Investigation/how route. No consumer workflow is implemented yet.

The [implementation plan](./pstack-t3-implementation-plan.md) now uses the agreed jstack names and shipped configuration contract. Adapter generation and broader workflow packaging remain proposals, to be built only as needed.

## Sources and evidence

- [Dependency map](./pstack-t3-dependency-map.md): the 2026-10-06 audit of pstack 0.15.15, including routing, principles, host assumptions, and deferred workflows.
- [Upstream inventory](./pstack-t3-upstream-inventory.json): source paths, sizes, and hashes at the audit pin. These are source records, not execution results.
- [T3 capability snapshot](./pstack-t3-capabilities-snapshot.json): selected provider schemas observed during the audit. Query the live catalog before execution; this is not an allowlist.
- [Review-panel experiment](../experiments/pstack-t3-review/README.md): archived prototype, license, and adaptation references.
- [Manual evaluation](../evaluations/pstack-t3-review.md) and [fresh-parent evaluation](../evaluations/pstack-t3-review-parent.md): historical execution evidence, complete results, and limitations.

## Separate upstream baselines

The Arena prototype uses `e5a8186d7b43be8d6ac4452440fbead5f1a51c70`. The broader dependency audit uses `df581122cde17e6e27686b5a448bde23e4ad4318`. The shipped setup skill uses `ccb5507cec1546dc88135c1139c811e6c59115ba`, documented in its [upstream reference](../skills/setup-jstack/references/upstream.md). These pins record separate investigations; archiving does not upgrade or equate them.

## Preservation and publication review

Evaluation text, JSON snapshots, and prototype source bytes are preserved from the local research. The parent-result Markdown adds only lint comments to retain its original heading and table formatting. The prototype entrypoint is stored as `PROTOTYPE.md`, so recursive skill discovery does not register it. The dependency map gains an archive note; the implementation plan is updated rather than treated as an immutable result.

The receipts describe synthetic PostgreSQL queue and webhook problems. They contain historical task/thread IDs, submitted model options, and `/home/ubuntu/Dev/skills` grounding paths. These identify the original execution context; they are not portable file links or current routing instructions. No credential-pattern matches were found in the publication scan. No user model configuration or unrelated personal files are included.

The fresh-parent evaluation records a rubric-disclosure deviation. The archived prototype contains the subsequent wording correction, which passed structural validation but has not had another behavioral run. Preserve that distinction when using the experiment to design a future Arena workflow.
