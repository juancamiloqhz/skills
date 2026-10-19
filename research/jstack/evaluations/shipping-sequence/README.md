# Shipping sequence update

Date: 2026-10-19. Local base: `db0a610bd76c0ad40e992fb65f5e22dc51f646d1` (merged PR #94). Audited source: `0148b78c56c72a1b8412055913c79f767095b217` in `cursor/plugins`; original adaptation source: `11713c683fe4add4fd403ea880580abbc9e0875f`.

## Source scope and result

Compared both source revisions and the complete final local files for these three paths under `pstack/skills/poteto-mode/playbooks/`:

| Path | Adopted change |
| --- | --- |
| `shipping.md` | Nine steps become six, preserving current headings and order. Allow a genuinely independent upper change to leave a blocked chain only with a fresh verdict. Confirm actual merges into trunk, then move only the immediate child. Keep the rest of the run frozen. Adopt plain Origin merge, shorter build-noise wording, reduced waiting instructions and the new reply contract. |
| `opening-a-pr.md` | Add the source sentence sending child movement after a parent merge to Shipping step 4, with a working relative link. |
| `babysit.md` | Remove the duplicated merge/arming warning and final Reply paragraph, exactly as upstream does. Step 9 retains the merge-authority boundary. |

[Shipping's adaptation record](../../adaptations/shipping.md) accounts for every current source difference, including configured T3 verifiers, publication authority, original ancestry cut points, leases, actual merge-commit proof and native watches. [Opening](../../adaptations/opening-a-pr.md) and [Babysit](../../adaptations/babysit.md) retain their previously documented runtime and authority adaptations. No watcher implementation changes.

The PR #94 evaluation raised a question about reusing lane evidence when the caller records verdicts by PR/head. Shipping now states that old receipts retain their original identity and a current-head assessment cites them plus fresh checks. This does not change Autopilot's verification cadence. Bro/Ketchup adoption and broader Autopilot source changes remain pending. The upstream manifest and reviewed checkpoint are unchanged.

## Executed Git checks

Environment: Ubuntu, Python 3 and Git; disposable repository plus a local bare remote, with no network or forge. Run from the repository root:

```sh
python3 -B research/jstack/evaluations/shipping-sequence/check_git.py
```

All four groups passed:

- Three sequential squash landings preserve one patch per PR. Only the immediate child moves after each merge; higher local and remote refs stay unchanged. C uses old B's recorded tip after B has been rewritten and squash-merged. Each actual squash result is confirmed on fetched trunk.
- An independent extracted patch runs on trunk. A second patch cherry-picks without conflicts but fails because it needs an API from the blocked parent; it runs successfully with that parent present. Clean application alone cannot prove independence.
- A stale explicit expected-ref lease rejects publication and preserves the competing writer's remote ref.
- Empty patch identity is rejected; using a different comparison base changes the identity.

The script removes its temporary repositories on exit. These checks establish Git mechanics and the fixture's runtime dependency, not forge PR metadata, production independence, or a fresh verifier verdict.

## Independent instruction exercise

One fresh native Codex `gpt-6-astra`/high authoring evaluator read the three proposed playbooks and task requests, without the expected answers, prior reports or diffs. It returned decisions without executing Shipping. The parent assessed them against the ten expectations in [cases.json](cases.json): all ten were met across five cases.

| Case | Observed decision |
| --- | --- |
| Merge proof | Advance only on confirmed trunk merge with assessed identity and actual merge commit present; queue/auto requests, wrong base, missing commit and query error do not advance. |
| Immediate child | Move B after A, then C after B using C's original old-B cut point. Accept automatic retargeting, check actual patch movement, and stop on missing ancestry or a failed lease. |
| Independent extraction | Require resulting-diff/runtime proof and a fresh verdict despite an unchanged patch ID; leave dependent work blocked and extract outside an active frozen run. |
| Receipt reuse | Retain old evidence identities, record current-head eligibility, require two original builds/one current build for compiled-noise comparison, rerun no-artifact lanes and re-verify product changes. |
| Babysit boundary | A status-only check does not start Shipping or auto-merge; report owner approval separately and end without a shell watcher. |

The evaluator noted that failed-lease recovery is not a separate written procedure. It correctly inferred stop, inspect ownership/remote state, preserve the local result and avoid overwriting another writer. The Git fixture independently verifies lease rejection. No blocking instruction ambiguity was observed in these cases.

This is one context with five tasks, not five independent trials or a controlled improvement measurement. Expectations were retained before the parent read the response, not preregistered before execution. No forge calls, builds, ledger writes, watch wakes, product control sessions or nested agents ran in this exercise. All 197 protected shipped/manifest files matched their pre-dispatch hashes afterward. Saved model configuration was not changed.

## Structural checks and limits

- All four `scripts/jstack/test_skill_packaging.py` tests passed; juan-mode passed the system skill creator's `quick_validate.py`.
- `node scripts/jstack/check_docs.mjs` reported 45 skills, 23 playbooks and zero problems; its existing guide-coverage note remains.
- Exact checks confirmed all six Shipping headings, bold introduction and reply match the audited source; Opening adds only the one sentence and Babysit removes only the two paragraphs relative to the local base.
- All other shipped files and the upstream manifest are unchanged. The packaged MIT notice matches the pinned upstream bytes. Final changed Markdown links and whitespace checks passed.

No new live GitHub stack, Origin operation, published verifier verdict, build-noise comparison or unattended T3 wake continuation was tested. The current PR's ordinary publication does not establish those behaviors.

Retain this report for outcomes and limits, `cases.json` for replayable decision requests, and `check_git.py` for executable mechanics. Full evaluator output, protected-file hashes and raw source diffs stay in task cache, outside the repository.

Example: ask juan-mode to ship verified PRs A, B and C. It confirms A actually landed, moves B's own change onto that result, checks B again, and merges B before moving C. A queued merge request never counts as A having landed.
