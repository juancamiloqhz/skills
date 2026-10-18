# External upstream watch coverage

The [complete coverage audit](../../coverage-audits/2026-10-18/README.md) found four pstack integration paths outside the checker's watch list. A change confined to one of these paths could incorrectly produce `no_changes`.

## Source and scope

Compared with cursor/plugins at `0148b78c56c72a1b8412055913c79f767095b217`, pstack v0.15.27, from jstack base `2e5cb405f175eacdab26a6c91f58b334e01e6f46`. Each added path exists in that upstream tree:

| Added watch path | Purpose |
| --- | --- |
| `harness/pstack` | Generated provider distribution and supporting files |
| `.claude-plugin/marketplace.json` | Claude plugin discovery metadata |
| `scripts/generate-pstack-harness-trees.mjs` | Distribution generator |
| `scripts/check-pstack-docs.mjs` | Documentation consistency checker |

The [manifest](../../upstream.json) adds these literal paths. The existing checker already supports directory coverage and invalidates cached results when manifest contents change, so its implementation stays unchanged. This is jstack maintenance coverage, not a port of upstream tooling or approval to ship provider distributions. No operational skill changes or upstream procedure deviations are introduced.

## Reproduction and results

Run from the repository root:

```sh
python3 -B -m unittest scripts/jstack/test_check_upstream.py
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
```

The two added regression methods run the actual checker CLI against disposable local Git repositories. With the previous manifest, they produced five expected assertion failures: four missing-path detections and one cache reassessment. With the expanded manifest, all 13 checker tests and all four packaging tests pass.

The new cases inspect JSON evidence and patches for each external path, verify `not_reviewed` status and an unchanged manifest, and exclude unrelated sibling paths. Expanding the watch list produces a new report for a source range previously cached as `no_changes`; the old report remains intact.

Comparing manifest objects before and after, excluding `watchPaths`, confirms every mapping, source pin and decision is unchanged. `reviewedThrough` remains `4bf3e083c6dec126e254f96181b84a105b6e3e70`. Existing watch paths are preserved.

This evaluation does not run the scheduled review, assess all outstanding upstream changes or execute upstream code. Shared cache receipts and schedule settings remain untouched. Fixtures and test caches are temporary and removed by the tests.

## Normal use

After merge, the weekly review uses this watch list from current main. For example, an upstream change confined to the Claude marketplace will now appear in its evidence for assessment. The user does not need to invoke or reinstall a skill for this maintenance change.
