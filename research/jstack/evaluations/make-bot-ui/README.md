# Make bot UI packaging assessment

Date: 2026-10-19. This unit packages the tested helpers as explicit `jstack-make-bot-ui`, with the six upstream phases, private setup, a receiver template and recovery instructions. Its bundled action is a fixed read-only GitHub PR-status query; it does not provide arbitrary custom actions. Installation and live service setup are separate.

## Changes and source comparison

Moved the existing transport, journal server and two page assets into the skill's `scripts/` directory. The transport docstring now describes the shipped helper; executable behavior is unchanged. Tests and the current local preview fixture use the package path. There are no duplicate compatibility helpers. Historical reports retain their original paths and commits.

The entrypoint preserves every phase heading and order from `pstack/skills/make-bot-ui/SKILL.md` at `0148b78c56c72a1b8412055913c79f767095b217`. The license matches pstack's MIT license. [The adaptation record](../../adaptations/make-bot-ui.md) accounts for the T3 tool, provisioning, protocol, recovery, tailnet and packaging substitutions. The receiver template generalizes the successful PR #113 prompt, including claim ownership, durable result before publication, acknowledgement after publication and a single bounded drain. Its larger 20-record cap reports overflow as incomplete. No live webhook or model configuration is created by this packaging work.

## Reproduce

```sh
JSTACK_TEST_T3_RUNTIME=/path/to/the/reviewed/t3 \
  python3 -B -m unittest discover -s scripts/jstack -p 'test_bot_ui_*.py'
python3 -B -m unittest discover -s scripts/jstack -p test_skill_packaging.py
node scripts/jstack/check_docs.mjs
node --check skills/jstack/jstack-make-bot-ui/scripts/bot_ui_assets/app.js
```

Omitting the runtime environment variable skips only the installed-verifier probe; it cannot establish live signature integration. The new package test copies only the installed skill to a temporary directory with a space in its path. An isolated interpreter imports its helpers, serves page/JS/scope, accepts a fixed click twice with one send, and exits. A separate CLI process reads the same journal. Scratch is removed after the test. This checks the distribution boundary without installing into a user's skill directories.

## Evidence and limits

All 28 bot UI tests passed with the installed T3 verifier, including the isolated-copy test. All four catalog/package tests passed. Manifest validation, receiver-template substitution, exact source headings/license comparison, documentation links, JavaScript syntax and diff checks passed. The current preview fixture also loads from the relocated helpers.

The [real webhook/recovery trial](../bot-ui-recovery-pilot/results.md) verified private provisioning, a signed ignored probe, unsigned rejection, one receiving conversation, failed-request draining, result publication/acknowledgement, later-turn saved-result redisplay and local-server restart. It did not induce a new conversation rollback. The [private HTTPS pilot](../bot-ui-tailnet-readiness/README.md) separately verified the actual proxy path, user-reported laptop click, preserved T3 routes and complete targeted cleanup with dummy delivery. These are component/live evidence from the preceding commits, not a new end-to-end run of this written entrypoint.

The current package has 57 catalog entries, including 54 pstack mappings and three team-kit helpers. All top-level pstack skill names in the frozen coverage audit now have mappings except the intentionally external Unslop. This does not establish full behavioral equivalence, provider support, Benny automation or plugin-distribution parity. Direct HTTP/IP peer deployment, general custom actions and automatic rollback recovery remain unverified. The default direct-HTTP instructions remain source-aligned; the tested HTTPS path requires an explicit user request and compatible host policy.

The next use should load the installed entrypoint and follow its full setup on an explicitly requested task. Missing T3 tools, Connect URL, credentials, host access or proof of receiving execution must remain incomplete. No active pilot service, secret, journal or raw transcript is included in the package.
