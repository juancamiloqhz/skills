# TDD evaluation

Standalone `jstack-tdd` supplies pstack's focused bug-fix regression procedure. It adds a helper, not the Bug fix playbook. Five procedures remain available and 18 pending.

## Source and dependency decision

[Complete comparison](source-comparison.json) covers the entire source directory at `11713c683fe4add4fd403ea880580abbc9e0875f`, its license, the planned upstream Bug fix caller and the installed unprefixed TDD entrypoint. The local description and body are byte-identical to source. The name becomes `jstack-tdd`; `disable-model-invocation: true` is omitted for the approved catalog-based caller design. The [adaptation record](../../adaptations/tdd.md) explains that metadata exception and its provider limits.

The installed `/home/ubuntu/.agents/skills/tdd/SKILL.md` has a broader workflow, including mandatory confirmation of testing boundaries and additional references. It does not supply pstack's exact focused procedure and impractical-test alternative. It stays untouched. This comparison concerns that entrypoint, not every supporting file or arbitrary same-name package.

The manifest adds one mapping and the upstream Bug fix playbook as context, already covered by the `pstack` watch root. There are 44 mappings. Existing watches, mappings, source pins, decisions and reviewed checkpoint are unchanged. All existing package files, including Juan-mode and its five procedures, match the recorded base commit. No operational Bug fix caller is enabled.

## Cheap local regression

The [input archive](inputs.json) retains a Node CLI whose default limit is 20 and whose documented explicit zero means unlimited. The existing three-test suite passes, but `node cli.cjs --limit 0` returns `{"limit":20,"format":"json"}`. A fresh evaluator receives the defect report, exact skill path and permission to change only `options.cjs` and the existing test file. It receives no proposed fix.

The evaluator adds one public CLI regression using the existing subprocess convention. It saves the test and unchanged production source before running the focused test. That run exits 1, with actual limit 20 versus expected 0. It then changes `input.limit || 20` to `input.limit ?? 20`. The identical regression exits 0, the CLI reports limit 0 and the full suite passes all four tests.

[Raw evaluation evidence](live-evaluation.json) preserves ordered command records, actual failing and passing stage snapshots, their hashes and outputs. The source at the failing stage matches the original input; the test is identical at both stages. No existing test lines are deleted. Six nearby output/error cases match before and after. Only the two authorized files change; caller note and HEAD remain intact. No commits are created in the fixture.

## Impractical native regression

A separate fresh evaluator receives a read-only native-device-picker support bundle and a report of selection loss after the native dialog closes. The bundle lacks the vendor package and integration harness. The existing `node diagnose.cjs` command exits 2 with `Cannot find module '@vendor/device-picker'`, before any dialog opens.

The evaluator reports this as a prerequisite failure, not reproduction or a passing regression. It creates no mock, test framework or fix and preserves all source hashes. Its report names the real picker, desktop, hardware session and observable selection check needed for failing-before/passing-after evidence. The missing module is observed directly; desktop and hardware unavailability come from the fixture README and are not independently tested.

## Parent verification and limits

[Parent verification](parent-verification.json) replays the saved failing and passing states in separate directories. It reproduces the assertion failure, focused success and four-test suite success. It reruns the native prerequisite diagnostic and verifies edit scope, protected files, unchanged HEADs, installed TDD and global model configuration.

These replays establish that the saved states produce the reported outcomes. The original sequence is supported by the evaluator's stage snapshots and ordered command log; replay alone does not prove chronology. An initial parent comparison included the differing `stage` labels in the two contract records. The corrected comparison excludes only that label and compares command, working directory, exit code, stdout and stderr. The archive records this verification-script correction; evaluator evidence is unchanged.

Both exercises use explicit authoring paths. They do not prove installed discovery, other providers, the full Bug fix workflow, commit sequencing, flaky-test handling or behavior through a real native dialog. The metadata exception permits model selection but does not establish successful provider invocation. A native module-load failure is a controlled prerequisite case, not proof of the reported product defect.

[Validation](validation.json) records four packaging tests, skill validation, manifest validation, Markdown lint, relative links and whitespace checks. No shipped executable, installation, model configuration or schedule changes. Scratch fixtures and replay evidence remain under `/tmp/jstack-tdd-20261016`; archived scripts retain their original absolute paths.
