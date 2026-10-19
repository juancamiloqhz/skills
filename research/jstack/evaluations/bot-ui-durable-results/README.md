# Recovering a bot UI result after a missing conversation turn

Date: 2026-10-19. Development tooling only. The [live pilot](../bot-ui-live-pilot/results.md) found acknowledgements in the external journal after T3 rolled back the receiving turn. A transcript search reference alone could no longer recover what the agent had reported.

## Change and use

The [journal helper](../../../../scripts/jstack/bot_ui_local.py) now saves the small, fixed PR-status JSON before publication. Its `save-result` command accepts successful `gh pr view` output through bounded stdin, verifies the configured PR, and requires the original claim owner. The result and its save time are immutable. New acknowledgements require a saved result. `result --request-id` reads that observation without calling GitHub or sending a webhook.

Example: a check says PR #123 was merged, but the conversation message later disappears. Ask the agent to recover the page's request ID. It reads the saved status, redisplays it with the save time, and identifies it as an earlier observation. This does not refresh the PR status or repeat the original action. The [receiver procedure](../bot-ui-local/README.md#durable-recovery-contract) specifies claim, check, save, publish and acknowledge order, plus recovery for missing messages.

The page distinguishes saved-but-unacknowledged results from completion records. An older acknowledgement without a saved result is flagged for reconciliation and cannot be backfilled with a new observation. Its owner, acknowledgement and exclusion from pending work stay unchanged. The actual retired pilot journal was not opened or modified for this change.

Only the local helper can read the saved result; HTTP status responses contain no result body. This remains a fixed read-only PR-status prototype. The helper checks data shape and ownership, not whether GitHub actually produced the observation or whether a conversation message is still visible. It does not detect rollback or automatically republish results. A claimed request without a result still requires investigation rather than reassignment.

## Verification

All 26 Python tests passed, including the pinned installed T3 signature verifier. The added checks cover:

- Saving before acknowledgement, reopening the database before and after acknowledgement, and recovering the exact observation without the referenced conversation message.
- Idempotent identical saves preserving their timestamp, and rejection of another owner or replacement observation.
- Fixed PR/URL, commit and merge-time validation, unexpected fields, malformed data, and bounded CLI input. Open, closed and merged PR observations are supported.
- Opening the old database schema without changing its acknowledgement, exposing the missing result, and refusing replay or backfill.
- Existing one-send, atomic claim, origin, failure, restart and signature behavior.

The conversation-loss case is simulated by retaining only the journal and reopening it; it does not trigger an actual T3 rollback. A collaborative-browser fixture exercises the saved, completed and legacy-without-result messages and their new-check button states. It uses public dummy credentials and a synthetic PR observation. No live webhook, schedule, GitHub comment, installation or model configuration was changed.

```sh
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
node scripts/jstack/check_docs.mjs
node --check scripts/jstack/bot_ui_assets/app.js
```

Omit the environment variable for portable tests; only the pinned installed-verifier probe is skipped. Browser reproduction uses the [local fixture](../bot-ui-local/preview_fixture.py) and receiver command examples. Keep its generated database and dummy key in scratch, then remove them after stopping the fixture. Retain the actual retired pilot's two private evidence files while its unresolved recovery finding still needs them.

## Source comparison and limits

Compared the final change with all six phases of `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. Upstream requires a local failure log drained by the routine and one POST attempt. Saving the bounded result beside that request is a T3 adaptation for the demonstrated external-journal/conversation-rollback mismatch. It adds no retry, poller, new skill boundary or action. Server-only credentials, fixed small payload, eight-second socket timeout and routine-side recovery remain intact.

The SQLite change adds a results table; existing request rows are preserved. Reverting to an older helper would lose the result requirement and legacy warning, although it would leave the added table untouched. The historical pilot prompt remains pinned to its original helper. A future pilot must use the updated receiver procedure and a matching committed helper.

Full live recovery, durable redisplay in T3 and tailnet access remain unverified. This fixture evidence does not change the earlier pilot's incomplete outcome or ship the standalone Make bot UI skill. The next live pilot needs a fresh bounded scope, task and private key provisioning.
