# Visual parity evaluation

On 2026-10-17, the draft [procedure](../../../../skills/jstack/jstack-juan-mode/playbooks/visual-parity.md) guided a configured worker through a two-component CSS migration. Actual T3 browser screenshots caught a one-image-pixel defect and returned to zero after repair. A separate reader correctly left a missing-baseline request incomplete.

This is a bounded authoring evaluation on base `f7b940e3623745bb642eb940fb34ad71ec07ca2a`, not an installed Juan-mode or full delivery-workflow test. See the [adaptation](../../adaptations/visual-parity.md) and [complete source-comparison record](source-comparison.json).

## Environment and execution

The fixture serves card and badge components in idle and active states. T3 preview used Chrome 154 on Linux, a 640×480 CSS viewport and device pixel ratio 2. Saved screenshots decoded to 1280×960 RGBA pixels. The fixture has no text, external fonts, animation or network data. Python's standard library served it; an already cached Sharp package decoded images. No installation was needed.

The parent captured all four original states, repeated them unchanged, confirmed zero differences and froze reference/harness hashes before creating the candidate. The candidate copied the original CSS with a black `.5px` square on the card, exactly one image pixel at this scale. The migration worker read the full draft and Control UI helper, introduced a shared `--tile-background` value, migrated card then badge, removed the defect and captured all final states. It used its own tab and closed it. The parent inspected the CSS, phase artifacts and available T3 activity, then independently recaptured all four states.

Fresh capability preflight selected Codex `gpt-6.1-sol` at high effort for implementation and Claude Opus 5.5 at high effort for the missing-baseline assessment, from the user's existing configuration. The saved configuration was unchanged. Each task had one writer and explicit scratch ownership; no checkout edits or nested delegation were needed. Available activity confirms the migration worker's source reads, shared-first edits, browser captures and tab cleanup. It is not a guarantee of complete provider transcript visibility.

## Results

Counts are differing decoded image pixels, with no tolerance. Each row covers all four declared states.

| Check | Card idle | Card active | Badge idle | Badge active | Exit |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original repeated before candidate creation | 0 | 0 | 0 | 0 | 0 |
| Deliberate card defect | 1 | 1 | 0 | 0 | 1 |
| Worker migration and repair | 0 | 0 | 0 | 0 | 0 |
| Parent independent recapture | 0 | 0 | 0 | 0 | 0 |
| Parent changes shared value from `#3464a4` to `#3464a5` | 19,200 | 19,200 | 19,072 | 19,072 | 1 |
| Restore candidate and recapture every state | 0 | 0 | 0 | 0 | 0 |

The shared-color change affects each card's 80×60 CSS interior at scale 2, or 19,200 image pixels. Rounded badge corners reduce its affected area. These are exact comparator counts, not similarity scores.

Additional checks:

- Removing one pair while retaining the four-state declaration exited 2 with `Incomplete or duplicate component/state coverage`.
- An absent image exited 2 with an input-file error.
- A capture after changing the CSS viewport width to 641 decoded to 1280×959 through preview's screenshot sizing, versus the 1280×960 reference. Comparison exited 1 for differing dimensions. The viewport was restored before later captures.
- The missing-baseline reader found no authoritative previous version, made no application edits or substitute baseline, and reported step 1 incomplete with the needed evidence. Only its assessment file was written.
- All eight frozen hashes matched at completion: reference CSS, fixture, comparator, stability manifest and four baseline images. Candidate HTML structure was never changed. The model configuration hash also matched preflight.

The migration worker claimed its implementation and parity checks complete and excluded publication. The parent limits that claim to this fixture. Parallel component worktrees, installed discovery, real-font/rendering nondeterminism, other browsers/devices, Electron and the unavailable Opening a PR procedure remain untested. Stable repeated captures were exercised; no nondeterministic-rendering case was claimed. Agent instructions still require stopping on that failure.

## Reproduce

Use an existing Sharp installation and T3 preview. If either is unavailable, report the missing prerequisite. From the repository root, choose a new scratch path:

```sh
python3 research/jstack/evaluations/visual-parity/fixture.py /tmp/parity-repro/app --prepare
python3 research/jstack/evaluations/visual-parity/fixture.py /tmp/parity-repro/app
```

Keep the second process running and use its printed port. Open an owned preview tab at 640×480, verify scale 2 and await each load. Capture `/?version=original&component=card&state=idle` and the other three card/badge × idle/active combinations. Repeat unchanged captures. Build a manifest with all four expected keys and image pairs:

```json
{
  "expected": ["card:idle", "card:active", "badge:idle", "badge:active"],
  "pairs": [
    {"component": "card", "state": "idle", "baseline": "/absolute/baseline/card-idle.png", "actual": "/absolute/repeat/card-idle.png"},
    {"component": "card", "state": "active", "baseline": "/absolute/baseline/card-active.png", "actual": "/absolute/repeat/card-active.png"},
    {"component": "badge", "state": "idle", "baseline": "/absolute/baseline/badge-idle.png", "actual": "/absolute/repeat/badge-idle.png"},
    {"component": "badge", "state": "active", "baseline": "/absolute/baseline/badge-active.png", "actual": "/absolute/repeat/badge-active.png"}
  ]
}
```

```sh
node research/jstack/evaluations/visual-parity/compare.cjs /absolute/existing/node_modules/sharp /absolute/manifest.json
```

Require four zeros before freezing images, reference CSS, fixture, comparator and state declaration with SHA-256. Only then copy `original.css` to `candidate.css` and append:

```css
.card::after { content: ""; position: absolute; left: 10px; top: 10px; width: .5px; height: .5px; background: black; }
```

Capture `version=candidate` for all four states and compare with the frozen references. Expect 1, 1, 0, 0. Give an implementation worker the full draft and Control UI helper, ownership of candidate CSS and a new evidence directory, and read-only access to everything else. Request migration to a shared background custom property without changing appearance. Introduce the shared value first, then migrate each component and remove the defect; compare all dependent states after shared changes. Require zero for all states and unchanged frozen hashes.

After the worker finishes, independently recapture all four states. Change only the shared color by one blue-channel value, recapture every dependent state, require failure, restore the exact candidate bytes and recapture to zero. Separately exercise missing pair, missing file and changed viewport manifests. Run a fresh read-only assessment with no accessible previous version and require an incomplete result without source edits. Close owned tabs and stop only the owned server after all consumers finish.

## Repository checks and cleanup

The four packaging tests, both affected skill validators, Markdown lint, relative-link checks and `git diff --check` passed. Full pinned comparisons preserved the five steps, ownership statement, anti-shortcut clause, reply, licenses and unchanged manifest. Only availability paragraphs changed in existing operational files. Both owned browser tabs were closed; the fixture process was stopped and its port refused connections. Scratch remains for this PR review.

## Retained evidence

`fixture.py` reproduces both components and states; `compare.cjs` supplies the exact decoded-pixel gate and complete-coverage check. This report retains outcomes, reproduction steps and limits. `source-comparison.json` records source identities and assessed differences. Raw images, task reports, catalogs, hashes and timeline exports stay in task scratch, outside the repository, and can be removed after review acceptance. No runtime logs or generated datasets are shipped.
