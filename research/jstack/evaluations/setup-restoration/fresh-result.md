# Fresh global setup evaluation

Setup completed using `/home/ubuntu/Dev/skills/skills/jstack/setup-jstack/SKILL.md` and its bundled helper. All helper subprocesses explicitly used `XDG_CONFIG_HOME=/tmp/jstack-setup-eval-20261015/fresh/xdg` and `JSTACK_CONFIG=''`. HOME and CODEX_HOME were unchanged.

The initial effective lookup and explicit global lookup both selected `/tmp/jstack-setup-eval-20261015/fresh/xdg/jstack/models.json`, which did not exist. The supplied global scope, medium budget and inheritance mapping were sufficient to proceed without confirmation.

Live `orchestrator_capabilities` returned 8 provider instances and 537 model entries. The complete unwrapped payload was saved temporarily and parsed by the helper during validation. The helper generated the medium template, validated all 17 roles, then saved the complete configuration atomically. Each command exited successfully.

Saved file: `/tmp/jstack-setup-eval-20261015/fresh/xdg/jstack/models.json`.

- `schemaVersion` is 1 and `preset` is `medium`.
- All 17 roles use `inherit-parent`.
- Arena runners, Architect runners and Interrogate reviewers each retain two ordered seats.
- The Arena cross-judge pool retains one alternative.
- All 13 scalar roles retain one inherited assignment each.

Readback confirmed the complete saved map. A final `locate --project-root /tmp/jstack-setup-eval-20261015/fresh/project` returned the saved path with `source: global` and `exists: true`. No project override shadows it. Resolving Arena runners with the live catalog and `--with-source` selected this global file and returned `[null, null]`, meaning two seats that omit an explicit delegation target.

Medium records a setup preference targeting high effort for concrete seats. Because every seat inherits, this setup does not change effective reasoning effort. Consumers must read and validate the file at invocation time. The resolver does not reapply `preset`; changing that field alone changes no effort. Two inherited panel seats do not provide different model families, and the single inherited cross-judge alternative does not ensure a different-family judge.

The target project's only discovered file was README.md, which says it contains research notes and no executable product. The optional verification-skill offer was therefore skipped. No application or tests ran. No agents were launched, models switched, providers executed, or installations changed. Catalog validation is not a provider execution test. Configuration is consumed by jstack skills and is not an automatically loaded T3 Code mode or registered slash command.

All writes stayed inside the fresh fixture. Temporary catalog and draft files were removed after validation. The saved global file and this report remain. No source files changed, so there was no implementation delta to compare with pinned upstream.
