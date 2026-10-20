# Codex conversation after manual service recovery

On 2026-10-20, an active Juan-mode conversation completed another Investigation after a user-authorized T3 service restart. It retained the same native conversation ID and used its saved explainer model without reinvocation. Automatic recovery after stopping only the shared Codex backend failed first. These are separate outcomes.

## Environment and boundary

The test used [Start an Investigation with Juan Help](t3-thread://v1/0fdfffb0-c122-496f-a9df-cd8a37238812) on Orbit, with `codex / gpt-6.1-sol`, low reasoning effort and standard service tier. The source was clean at `8d9848bd76dddf0a3fe824b110d1333f6dd00c81`. The installed packages and saved model configuration were preserved. Temporary configuration-preflight files were allowed.

The coordinator and test conversation shared one Codex backend. A prepared operator helper checked process identity, idle conversation state, the selected native conversation and four protected file hashes before stopping that backend once. It did not start a replacement. The preparation incorrectly assumed T3 would recreate the backend on the next request and lacked a verified recovery procedure.

## Observed sequence

Positions and run ordinals below belong to the test conversation unless another conversation is named.

| Boundary | Observation |
| --- | --- |
| Run 12, 103–105 | Explicit activation for the test. Position 104 confirmed active state without starting work. The original pre-test state was inactive. |
| Backend stop, `20:02:00.987489Z` | The operator helper recorded exit zero and old PID 44273 gone from `t3code-codex-2fb6075f.scope`. This receipt established a stop only. |
| Coordinator runs 286–288 | Requests failed with `CodexAppServerProcessExitedError` against the old PID. No replacement backend handled those turns. |
| Manual service recovery, `20:09:53Z` | The user separately authorized restarting `t3code.service` in [Diagnose Codex Restart Failure](t3-thread://v1/4dff413e-5796-4970-bf72-0928c7d9095e), positions 31–43. This changed the T3 server as well as its backend. Positions 47–53 and independent coordinator inspection confirmed replacement Codex PID 291771 in `t3code-codex-216cce92.scope`, using the same Codex 0.163.0 executable. |
| Run 13, 106–120 | An ordinary source question contained no activation command or mode-state prompt. The agent selected Investigation, read current source, obtained a fresh catalog, passed model preflight and dispatched one explainer. The completed child record at 115 and notification at 117 preceded the source-cited final answer at 119. |
| Run 14, 121–123 | Explicit opt-out restored the original inactive state. Position 122 acknowledged it without starting another task. |

The ordinary question asked how `scripts/jstack/check_installation.py` distinguishes different packages from missing ones, with line citations and two limitations. Parent and child both read current source. Their answer correctly gave missing `SKILL.md` priority, explained byte comparisons, and identified ignored extra files and the working-checkout baseline. This was static source inspection, not a fresh checker execution.

The full live capability payload at 110 exactly matched the temporary catalog contents at 111. Preflight at 112 selected the unchanged global configuration and resolved `how explainer` to `codex / gpt-6.1-sol`, high reasoning effort. Dispatch at 114 confirmed that model and effort plus standard service tier. The task ID is `node:delegated-task:command%3Amcp%3A9fa8734e-1ccf-46bd-8c4b-66f7e3ddb921%3Adelegate-task%3Astatus-limitations-explainer-20261020-1`. Its backing child completed with no active run or pending requests when independently read.

The provider projection retained native conversation `01a15693-96f7-79b2-abd0-b2309dbc08d6` through the resumed task and opt-out. The installed entrypoint, activation reference, setup investigation reference and saved model configuration matched their pre-stop hashes. The temporary catalog was removed. These selected-file and activity checks do not establish a filesystem-wide audit.

## Interpretation and remaining limits

The active conversation retained routing, fresh model preflight and completed configured delegation after manual service recovery. The prompt did not remind it that Juan-mode was active. The parent did not freshly reload the mode or How entrypoint in this turn; earlier instructions remained available in the same native conversation. This does not prove rediscovery after instruction loss.

The parent claimed Unslop use without a fresh parent identity/load check. The child freshly read Unslop and its assigned How references. A [terminal reread](../investigation-completion/README.md) corrects the earlier plan assessment: item 113 contains all four steps completed before the final answer. The update changed that existing item rather than adding a later activity position. The bounded state-and-delegation result still does not certify the parent's writing check.

The failed automatic recovery is a T3 runtime observation, not a jstack fix or a source-level diagnosis of T3. Manual service recovery changed the original backend-only test conditions. One successful active continuation does not establish reliability, inactive-state recovery, interrupted-child recovery, automatic restart, machine reboot or other coordinating providers. Opt-out afterward restores the test state; it is not an inactive-state restart test. The earlier [manual compaction evidence](../conversation-compaction/README.md) remains a separate boundary.

Further automatic-recovery testing needs an isolated runtime and a verified recovery procedure. This assessment ran no further restart and made no host, installation or model changes.

## Fidelity and retention

This report changes no operational skill, source pin or reviewed checkpoint. Inspection of `pstack/skills/poteto-mode/SKILL.md` and `pstack/skills/how/SKILL.md` at pin `11713c683fe4add4fd403ea880580abbc9e0875f` confirms Cursor mode/reminder metadata and How's one-explainer simple path. The audit revision `0148b78c56c72a1b8412055913c79f767095b217` retains that child requirement. The existing [Juan-mode adaptation](../../adaptations/juan-mode.md) owns the T3 conversation-state and configuration differences. This trial evaluates them without claiming Cursor equivalence.

Retain this concise assessment and durable conversation references. The original checkpoint, stop receipt and retired helper remain in task-owned cache for reconciliation. No helper, transcript, capability catalog, hash inventory or application database is committed. Documentation checking and `git diff --check` validate the report changes, not the runtime claims.
