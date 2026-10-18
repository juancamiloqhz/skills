# Installed package comparison

The repository has 45 jstack packages, but an earlier installation can still have fewer packages or older files. The read-only [checker](../../../../scripts/jstack/check_installation.py) compares each manifest package's Git-tracked files in the current checkout with one explicit installed root. It does not install anything.

## Usage

From the repository root, before testing installed workflows or after manually reinstalling:

```sh
python3 scripts/jstack/check_installation.py --installed-root "$HOME/.agents/skills"
```

Use the actual root for the provider being checked. Add `--json` for missing/changed file lists. `--repo-root PATH` selects another source checkout. The checker reads working-tree bytes for tracked paths, so use clean current main when assessing a released installation. Staged additions count; untracked source caches do not.

Exit 0 means every expected file matches. Exit 1 means packages or files are missing or different. Exit 2 means the check is incomplete, such as an invalid manifest, missing installed root or read error. A regular file where a package directory should be is also a read error. A package without `SKILL.md` is missing; other missing files or changed bytes make it different. Differences can include intentional local edits. Inspect them before reinstalling.

Directory symlinks are followed. Extra installed files and obsolete package names are ignored. This compares content, not executable permissions or provider registration. It does not prove catalog invocation, external dependencies, model dispatch or end-to-end workflow behavior. Run it separately for each installation root. No report or cache is written unless the caller redirects output.

## Observed installation

On 2026-10-18, source package bytes at merged PR #78, commit `4f9f1b06027bf0d85ee051c1db26c084bac0fd88`, were compared with `/home/ubuntu/.agents/skills` on this host. The result was exit 1: **34 matching, 7 missing, 4 different**.

Missing packages were `jstack-control-cli`, `jstack-control-ui`, `jstack-deslop`, `jstack-no-comments`, `jstack-tdd`, `jstack-technical-writing` and `jstack-typescript-best-practices`.

| Different package | Missing expected files | Changed files |
| --- | ---: | ---: |
| jstack-juan-mode | 50 | 3 |
| jstack-setup | 0 | 2 |
| jstack-principle-type-system-discipline | 0 | 1 |
| jstack-benchmark-checklist | 0 | 1 |

The 38 present packages are not proof of a current installation. In particular, repository Orchestrate availability does not update the installed Juan-mode. Preserve local customizations, manually refresh the selected packages, rerun the checker, then verify discovery in a fresh provider conversation. No installation or saved model change was performed in this assessment.

## Validation and fidelity

```sh
python3 -B -m unittest discover -s scripts/jstack -p test_check_installation.py -v
python3 -B -m unittest discover -s scripts/jstack -p test_skill_packaging.py -v
```

Six CLI tests pass against disposable Git repositories. They cover symlinked packages, missing entrypoints, missing nested scripts, changed bytes, ignored extras, invalid inputs, failed reads and the documented text command. A before/after byte snapshot includes the fixture's Git metadata to check that the comparison makes no writes. Four existing packaging tests pass separately.

A configured Claude Opus 5.5/high review independently reproduced the installation result, reran the original five CLI tests and four packaging tests, and found no blockers. It used a bounded digest and actual artifacts, not a full transcript. The parent then added the text-command test and clarified incomplete reads, retained open recovery checks, and test commands that avoid bytecode artifacts. Checker implementation bytes are unchanged from the reviewed candidate.

This is a local maintenance tool with no one-to-one upstream skill. The manifest remains the source of package identities; no shipped skill, procedure, upstream mapping or checkpoint changes. Existing pins remain `11713c683fe4add4fd403ea880580abbc9e0875f` for 42 packages and `ccb5507cec1546dc88135c1139c811e6c59115ba` for setup and the two verification helpers. PR #78's [pinned-source comparison](../orchestrate-release/source-comparison.json) remains applicable because those operational files are unchanged. Routine JSON and command logs stay in task-owned cache.

This closes the reproducible file-comparison step only. Full release verification still needs installed dependency calls, external Unslop and project-specific tools, invocation metadata, and activation/opt-out persistence on each claimed coordinating provider. The existing T3 worktree, concrete-model and service-recovery trials remain bounded evidence, not a general provider support guarantee.
