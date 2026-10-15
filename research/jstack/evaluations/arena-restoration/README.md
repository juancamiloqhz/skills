# Arena restoration

This correction follows merged PR #35 at `efd2afebcd4335e6ef54292316dc1817e2332f65`. Arena retains pin `11713c683fe4add4fd403ea880580abbc9e0875f`. It restores Frame, Fan out, Cross-judge, Pick a base, Graft, Verify and Outputs, with the source description and four standalone principle routes at their original decision points.

Ordinary Arena again proceeds after a candidate dropout. With one survivor it can judge, verify and return the artifact while reporting that comparison was unavailable. Architect's explicit requirement for two structurally distinct designs still applies. Its single changed caller sentence now identifies that requirement as Architect's own.

## Source comparison

[compare.py](compare.py) compares Arena's complete source directory, which contains only `SKILL.md`, with the final entrypoint. It checks the MIT license and inventories the T3 execution reference. [source-comparison.json](source-comparison.json) records every difference and the exact one-sentence Architect change against merged PR #35. The parent inspected the source and final diff. [Arena's adaptation record](../../adaptations/arena.md) accounts for all structural and substantive differences; [Architect's record](../../adaptations/architect.md) records the caller correction.

```sh
python3 -B research/jstack/evaluations/arena-restoration/compare.py > /tmp/arena-source.json
cmp research/jstack/evaluations/arena-restoration/source-comparison.json /tmp/arena-source.json
```

The four principle packages are now manifest context dependencies. Component pins and the reviewed checkpoint remain unchanged. T3 worktree instructions now use `delegate_task` with `isolation: "worktree"`, starting at the parent's committed baseline. No new worktree runtime claim follows from that instruction correction. Historical evaluations remain unchanged and describe their original skill versions.

## Runtime exercise

A fresh-context evaluator received the actual Arena skill, its explicitly supplied setup/principle source packages, a nine-line delivery function and a synthetic two-seat inherited configuration. Its request was to compare optional progress-reporting designs while preserving delivery behavior, then return a design without implementing it. The evaluator was authorized to run the configured candidate and judge children; all writes were restricted to its temporary output directory. It received no expected design or prior evaluation conclusions.

The run completed with two viable designs and one read-only judge. Both candidates converged; the coordinator and judge each scored them 20/20 and preferred A. The [final design](runtime/design.md) retained the consensus and added two verification cases from B, as recorded in [synthesis](runtime/synthesis.md). The [judge report](runtime/judge-report.md), [verification](runtime/verification.md) and [runtime result](runtime/result.md) separate design inspection from six executed baseline scenarios on unchanged source. The reporting feature itself was not implemented.

[runtime-record.json](runtime-record.json) retains exact text of all original output files, including the two candidates, full dispatch briefs, rubric, phase record, terminal responses, frozen hashes and compact catalog evidence, plus the original fixture and synthetic configuration. The readable outcome copies under `runtime/` add titles and normalize Markdown table spacing. This keeps duplicate frozen/original artifacts out of the maintained file tree while preserving their exact content. Full temporary catalogs were removed by the evaluator.

The parent read both candidates, the judge report and final synthesis, then independently verified source/configuration hashes, original/frozen byte equality, matching dispatch hashes, identical candidate briefs except their owned output paths and terminal child states. [Parent checks](parent-checks.json) retain those results. The recorded rubric time precedes candidate dispatch, and freezing precedes judge dispatch. These are coordinator records, not an independent host timing or file-read trace. Candidates ran serially while explicit-path behavior was established; this does not test concurrent writers.

The fixture lives at `/tmp/jstack-arena-restoration-20261015/runtime/`. The evaluation uses source packages, not an installation or slash-command discovery test. Native contexts inherit the coordinator model and effort without overrides. Same-model judging does not establish model-family diversity.

## Dropout and caller assessment

A separate fresh-context evaluator assessed six controlled states without dispatching agents: one ordinary survivor, one survivor under Architect, no survivors, a candidate still writing, a one-seat configuration before dispatch and mandatory different-family judging with only an inherited judge. All six matched the [acceptance criteria](assessment-cases.json). The [report](dropout-assessment.md) cites actual instructions and preserves limits around optional partial judging and same-model dropout retries. No automatic recovery or success claim follows from those unspecified branches. This is a continuation assessment, not an induced provider failure or live dropout test.

## Verification limits

These bounded exercises do not establish successful cross-family or cross-provider judging, code-worktree isolation, live provider failure recovery, full installed-provider discovery or all possible reframing/grafting outcomes. Both skill validators, Markdown lint, manifest/local-link checks and 11 upstream-checker tests pass. The actual global configuration retains SHA-256 `a9f0a27536cd061b5a6ed6bdf1ccfaf40f35eb8398bea846f0fac301ff81197b`. No saved model configuration, installation or schedule changed. Swarm and all 23 Juan-mode playbook procedures remain separate work.
