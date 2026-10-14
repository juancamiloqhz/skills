# Pocket verification generation result

Created and executed a project-local verification skill for Pocket. The end-to-end run passed.

Generated paths:

- `/tmp/jstack-verification-restoration/generation/.agents/skills/verify-pocket/SKILL.md`
- `/tmp/jstack-verification-restoration/generation/.agents/skills/verify-pocket/scripts/verify.py`, executable
- `/tmp/jstack-verification-restoration/generation/.agents/skills/verify-pocket/features/README.md`
- Feature recipes `features/add.md`, `features/show.md`, and `features/list.md` in the same canonical directory
- `/tmp/jstack-verification-restoration/generation/.claude/skills/verify-pocket`, a relative symlink to `../../.agents/skills/verify-pocket`

All six generated files resolve to their canonical files through the Claude link. Live Claude Code discovery was not tested.

Executed from the fixture root:

```sh
python3 pocket.py --version
.agents/skills/verify-pocket/scripts/verify.py --evidence-root /tmp/jstack-verification-restoration/generation-evidence
```

The standalone doctor reported `Pocket 1.0`. The helper ran ten real subprocess commands: version doctor; empty list; add with title trimming and body; show ID 1; one-note list; rejected blank title; missing ID 999; add with default body and incremented ID; show ID 2; two-note list. It checked exact JSON, expected exit codes, error text, persisted notes, absence of writes on initial list, and unchanged storage after read/error paths. All three mapped user entry points were exercised. Assertions fail independently of the app's exit code.

Retained evidence is `/tmp/jstack-verification-restoration/generation-evidence/pocket-lijm32z3/`:

- `identity.json` records source SHA-256 hashes, application path, interpreter, and Python version.
- `commands.jsonl` records feature IDs, argv, stdout, stderr, and exit codes for all ten commands.
- `notes.json` captures the persisted two-note result before cleanup.
- `summary.json` reports `passed: true`, the owned scratch path, and successful cleanup.

Cleanup removed the helper's unique `.pocket-verify-*` directory. A separate post-run check confirmed that directory and any other run scratch were absent and all four evidence files survived. Commands were short-lived subprocesses; no service was started. No failed helper iteration occurred. A post-run inspection initially expected eleven commands instead of ten; correcting that counting mistake let the inspection pass without application or helper changes. Failure cleanup, timeout handling, and assertion failures are implemented but were not fault-injected. Forced termination remains a manual ownership-check cleanup case.

`README.md` and `pocket.py` match their initial SHA-256 hashes. No product changes, installations, network services, model changes, commits, pushes, or PRs occurred. Jstack files were read without modification; the upstream-fidelity policy and the generator's example feature map were consulted. No jstack adaptation was proposed or edited, so no new upstream deviation was introduced.

Uncovered behavior includes malformed CLI arguments beyond the mapped errors, corrupt JSON data, filesystem permission errors, and unsupported concurrent writes to one data directory. Version/hash identity is checked; client skill discovery is untested. Use `/maintain-verification-skill`, available in the skill catalog, to keep the feature map current when Pocket changes.
