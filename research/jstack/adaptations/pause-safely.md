# Pause safely adaptation

Source: `pstack/skills/poteto-mode/playbooks/pause-safely.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [Pause safely](../../../skills/jstack/jstack-juan-mode/playbooks/pause-safely.md).

The port retains the source heading, explicit-only trigger, four ordered steps, WIP checkpoint, off-context resume note, existing-trail reuse and pause reply. It remains an internal playbook, not a standalone skill. The package's MIT notice is unchanged.

| Location | Difference | Requirement and verification |
| --- | --- | --- |
| Trigger | Compaction checkpoints continue authorized work; authoring or reviewing the text does not execute it. | The source's explicit-only trigger excludes keep-going requests. The existing mode activation contract distinguishes reading from invocation; the user reaffirmed that boundary on 2026-10-17. Bounded cases check both distinctions. |
| Step 1 | Cancel only owned children through their runtime lifecycle and confirm termination, including pending child runs. Preserve files and report unknown state. | T3 cancellation is asynchronous; a request is not terminal evidence. The evaluation separates actual T3 cancellation from a simulated still-running receipt. Native-child interruption and nested-writer termination remain unverified. |
| Step 1 | Unwatch worked PRs on handoff and preserve unrelated tasks, watches and schedules. | T3's parent handoff contract requires unwatching. A conversation pause does not authorize changing unrelated recurring work. The fixture has no live watch; watch/scheduler mutation is not claimed as tested. |
| Step 2 | An existing PR/branch does not supply new publication authority; pause does not authorize merge, installation, deletion or model changes. | Current user authority governs external actions. Retains upstream's restriction on new PRs/pushes and records its authorization boundary. |
| Step 3 | Commit owned work only; preserve unrelated index/worktree edits, handle unsafe ownership or prohibited commits as a stated gap, and report a dirty tree honestly. | Shared checkout and user-work preservation requirements. Isolated Git fixtures include a task-owned broken implementation, staged user edit and untracked user file. No blanket staging, reset or stash is needed. |
| Step 4 | Record checkout, ownership, stop evidence, PR/watch/schedule state, authority, activation and selected config path; choose storage that survives the intended interruption. | T3 continuation needs task and workspace identity, and `/tmp` may not survive a restart. The cold-read check assesses the produced note against retained local artifacts. No system-restart durability claim. |
| Callers | Mode/setup and current research show 18 available procedures and five pending. | Availability only. No changes to the 17 role keys, model configuration, upstream mappings, source pins or reviewed checkpoint. |

See the [evaluation](../evaluations/pause-safely/README.md) and [final source comparison](../evaluations/pause-safely/source-comparison.json). Creating and evaluating this procedure does not activate juan-mode or invoke its pre-review helpers. Evaluation agents come from the separately applied skill-creator process and inherit the executing model; they do not resolve jstack workflow roles.
