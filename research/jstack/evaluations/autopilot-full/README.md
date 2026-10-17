# Autopilot-full evaluation

Autopilot-full keeps one logical owner per independent PR through merge. The root supplies independent verification and the final verdict. This port preserves all seven source steps and updates Planning, Babysit and availability records to 21 procedures. Autopilot-stack and Orchestrate remain pending.

Base: `fb7dd9ffe9f65aae572aa523398be087c7623b6b`. Procedure, mode and callers use source `11713c683fe4add4fd403ea880580abbc9e0875f`; setup uses `ccb5507cec1546dc88135c1139c811e6c59115ba`. See the [adaptation](../../adaptations/autopilot-full.md) and [final source comparison](source-comparison.json). Pins, mappings, license and reviewed checkpoint are unchanged.

## Reproduce the bounded queue

From the repository root, choose a fresh scratch path:

```sh
python3 -B research/jstack/evaluations/autopilot-full/fixture.py /tmp/jstack-autopilot-example
python3 -B /tmp/jstack-autopilot-example/forge.py list
python3 -B /tmp/jstack-autopilot-example/forge.py proof 101 head
python3 -B /tmp/jstack-autopilot-example/forge.py proof 102 head
python3 -B /tmp/jstack-autopilot-example/forge.py proof 102 trunk
```

The generator creates a local Git repository with three independent PR branches, a later trunk change and fixture receipts. PR 101 has a stale passing verdict and a subsequent multiplier defect. PR 102 was rebased after verification without changing its patch; later trunk movement changes only README text. PR 103 is reserved for the operator. The local forge endpoint deliberately does not enforce those policy gates. It checks the expected head and performs a real local squash/commit, so an incorrect merge decision would leave observable evidence.

Give a fresh agent the task in [cases.json](cases.json), the fixture path and a separate output directory. Withhold the generator, assertions and other runs. The with-playbook agent also reads [Autopilot-full](../../../../skills/jstack/jstack-juan-mode/playbooks/autopilot-full.md) and [Shipping](../../../../skills/jstack/jstack-juan-mode/playbooks/shipping.md); the baseline reads no jstack instructions. Only the simulated owner endpoint may mutate the fixture. Preserve `packet.json`, `forge.py`, the branches and recorded input hashes. Inspect outputs and actual Git state against the assertions, not merely the agent's report.

## Observed results

Two fresh native agents ran the queue case on Ubuntu with Python 3 and Git. Two more ran the focused monitoring explanation. All inherited Codex `gpt-6-astra` with high effort. Skill-creator supplied the evaluation; no saved jstack model role was selected or changed. Juan-mode stayed inactive. Each condition has one run per case.

| Observation | With playbook | Without playbook |
| --- | --- | --- |
| PR 101 current CLI returns 12, expected 9 | Blocked stale verdict and defect | Blocked stale verdict and defect |
| PR 102 preserves patch after rebase | Merged through simulated owner | Merged through simulated owner |
| PR 103 operator hold | Preserved | Preserved |
| Current-trunk merge conflict check | Explicit `merge-tree` before merge | Omitted |
| Fix-forward asks for red regression coverage | Included | Omitted |
| Stop explanation includes owned watches and in-flight writes | Included | Omitted |
| Original queue/lifecycle assertions | 7/8 | 4/8 |
| Focused monitoring explanation | 3/3 | 3/3 |

The original explanations both omitted explicit parent ownership of ongoing watches and wakes, failing the combined monitoring assertion. The targeted follow-up asks who monitors each PR, what a pending child means and whether a general go authorizes hourly scheduling. Both then assigned monitoring to the coordinator, rejected unrequested recurring work and kept incomplete children from supporting a merge claim. The original failures remain recorded; a prompted follow-up does not erase them. These small, partly explanatory cases do not establish a general performance advantage.

The parent reran CLI checks and verified protected input hashes, unchanged PR branch heads, exactly one new trunk commit per run and an `invoice.py`-only diff. Each action log contains only owner-merge 102. Final trunk outputs are cart 6, invoice 9 and export 6, preserving the blocked and held changes. Actual old/current patch IDs differ for 101 and match for 102. Both agents inspected JSON `complete=false` despite a successful proof process exit. The with-playbook command evidence records no command failures. The baseline guessed a nonexistent CI workflow path, got exit 128, then inspected the tree and confirmed that CI evidence was simulated.

## Evidence limits

Git identities, patch comparisons, CLI runs and local squash commits are real. Forge state, owner actions, CI and independent lane receipts are simulated inputs. The static list endpoint does not update PR state; the merge event, actual trunk commit and post-merge behavior establish local landing. The controller invoking that endpoint represents an owner action, not live delegation of a merge.

Cancellation, replacement, whole-program stop, parent watch ownership and statement-then-wait were explanation-only cases. Live owner worktrees, independent Swarm reviews, early publication, leased pushes, hourly audits, PR wake continuation, restart recovery, countersigns, trail reviews, retro and bot sweeps were not executed. Full live Autopilot-full completion remains unverified. T3 capability/tool inspection supports the documented substitutions, but does not prove those runtime paths.

Four packaging tests, mode/setup metadata validation, changed Markdown links/lint and `git diff --check` passed. The source comparison covers the final procedure, Planning and Babysit callers, mode and setup. No model configuration, installation, recurring schedule or real evaluation PR changed. Only this implementation PR is published through the normal authorized workflow.

## Normal use

After merge and manual skill update, a user could say:

> Use jstack-juan-mode's Autopilot-full for these independent fixes: the empty search result crash, the CSV header typo and the missing settings tooltip. You may open and merge their PRs after verification, but leave the tooltip PR for me to merge. Run at most two owners at once. State the plan first and wait for my go.

The first response states the plan without starting owners. After go, owners build their assigned changes and the coordinator verifies each candidate. The crash and CSV fixes can land independently when their evidence passes; the tooltip remains held. An hourly recurring audit requires its own explicit request and supported runtime. A missing dependency or runtime guarantee remains visible rather than becoming assumed success.

Retain this report, the fixture generator, case specification and source comparison in Git. Generated repositories, command logs, full agent reports, grading, capability data and the static viewer remain in task-owned scratch while review needs them. Remove that scratch after acceptance only when no active task depends on it; preserve shared caches and unrelated work.
