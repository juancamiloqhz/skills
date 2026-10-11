# Configuration discovery and resolution

Find `setup-jstack` in the executing provider's available skill catalog and expand its advertised `SKILL.md` path. Read its configuration contract relative to that installation. Pass the entrypoint's parent directory to `--setup-skill`; its directory need not share a parent with `juan-mode`. Do not search arbitrary repositories for a convenient resolver or copy `models.py`. A missing installation is a dependency error with manual installation as the remedy.

Call live `orchestrator_capabilities` and write the unwrapped payload to a task-owned temporary JSON file. Read the installed setup skill's T3 Code integration reference for catalog capture, lazy discovery and the supported ACP transport. Record its observation time with task evidence, refresh it for each new routed task, and refresh again after a dispatch rejection that might indicate catalog drift. Remove temporary catalog files when no longer needed.

Run the preflight from any working directory using absolute paths:

```sh
python3 /path/to/juan-mode/scripts/preflight.py \
  --setup-skill /discovered/path/to/setup-jstack \
  --project-root /path/to/target-project \
  --catalog /task-owned/path/catalog.json \
  --role 'how explorer'
```

Setup-jstack's configuration contract owns lookup. The preflight passes `--config` and `--project-root` to its canonical `models.py resolve --with-source` command, then reports the selected absolute `config` path and `configSource`. Precedence is explicit file, `JSTACK_CONFIG`, an existing project `.jstack/models.json`, then global defaults. The selected file supplies all 17 roles; malformed or incomplete project settings produce an error. The preflight does not initialize, repair or save configuration. An error in another role still prevents execution. On error, report the file and role or dependency, and let setup-jstack handle a user-requested repair.

Pass the task's known project root explicitly when the current directory belongs to another checkout or the installed skill. Without `--project-root`, the canonical helper discovers the caller's Git checkout root. Before dispatch or a checkout change, retain the returned absolute `config` path and supply it as `--config` for children and later phases of that task. Re-read and validate that file; do not rediscover from a child's worktree, where an untracked project configuration may be absent. A new task repeats project lookup. An installed setup-jstack that lacks the shared lookup CLI requires a manual update; do not fall back to a second lookup implementation.

Each returned `targets` entry is either a concrete T3 Code target or JSON `null`. Pass concrete targets unchanged, including their options. For `null`, omit `target` to preserve the current parent's provider, model and effort. The helper reports the effective inherited identity only for capability checks; that identity is not a replacement target and does not establish model-family diversity. Read current thread configuration when effective options matter to evidence.

## Role and fan-out semantics

Use `feature, refactoring`, `bug-fix`, `perf-issue` and `hillclimb` for their implementation routes. Use `hardest tasks` for a task whose difficulty needs that configured role. Delegated prose and judgment use `judgment and prose`. Helpers use their named `how`, `why`, `reflect`, `architect`, `arena`, `swarm` and `interrogate` roles as their procedures are implemented. For a step with no dedicated role, declare the relevant existing role or keep the work in the parent.

Preserve every configured list entry in order, including repeated and inherited selections. `architect runners`, `arena runners` and `interrogate reviewers` are panels. `arena cross-judge pool` supplies alternatives; the procedure selects one eligible judge, not the entire pool. `swarm workers` supplies a model default, not a worker count. The preflight reports these three selection kinds so callers cannot confuse alternatives with fan-out.

The `availability` array aligns with `targets` by index. A pool alternative with `canDispatch: false` remains in the output with its reason; select only executable alternatives that also meet the procedure's independence requirement. A pool with no executable alternative fails. Scalar and panel roles require every selected seat to execute. This capability handling does not relax whole-map validation of saved provider, model or option selections.

Before dispatch, check the procedure's required count and independence against the effective selections. One inherited seat is a valid configuration, but does not satisfy a two-candidate design or a different-family judge requirement. Report the exact unmet requirement. Retain existing choices until the user authorizes an adjustment; do not invent extra models or increase fan-out.
