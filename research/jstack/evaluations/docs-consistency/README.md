# Current documentation consistency

The [complete coverage audit](../../coverage-audits/2026-10-18/README.md) identified a gap between package checks and current documentation. Existing Python packaging tests validate shipped names and package-local links, but do not inspect README counts, catalog coverage or guide anchors.

The new [checker](../../../../scripts/jstack/check_docs.mjs) compares current documentation with the shipped tree. It reports file/line diagnostics for stale whole-set counts, nonexistent helper names, missing local link targets and missing Markdown heading anchors. It also requires links to every shipped skill in the root catalog and every playbook in Juan-mode's index. It exits 1 for detected drift and 0 when these checks pass.

## Source comparison and adaptations

Source: [`scripts/check-pstack-docs.mjs`](https://github.com/cursor/plugins/blob/0148b78c56c72a1b8412055913c79f767095b217/scripts/check-pstack-docs.mjs) at `0148b78c56c72a1b8412055913c79f767095b217`. Local base: `7179074ddc285100de569129d0cdd9305fcdae30`, merged PR #83. Compared the complete final script with that frozen source. The upstream MIT notice is retained in `scripts/jstack/check_docs.LICENSE`.

| Upstream behavior | Local adaptation and reason |
| --- | --- |
| Enumerate pstack skills, principles and playbooks | Enumerate `skills/jstack`, `jstack-principle-*` and Juan-mode playbooks, following the approved portable names. Team-kit helpers are already local jstack packages. |
| Read plugin README and guide pages | Read root `README.md` and `research/jstack/README.md`, the current catalog and status index. Optional top-level Markdown pages under `research/jstack/guide` receive the same checks. No guide is shipped yet, so report that coverage as pending. Dated audits, evaluations and historical roadmap sections remain outside the scan. |
| Check whole-set numeric and English-word counts | Retain the source's whole-set/subset distinction. Recognize local `packages`, `procedures`, `playbook procedures` and Juan-mode wording as well. |
| Check slash commands and allow Cursor/Claude built-ins | Check prefixed slash/dollar calls, literal jstack catalog names and `--skill` arguments. Allow other actual repository skills in installation examples. Omit unprefixed host-command checks because T3 does not supply the source's built-in command inventory. |
| Check relative links and heading anchors | Preserve the source link matching and heading slug/duplicate rules, resolving against the repository root. |
| Require README skill/playbook/agent links | Require skill directory or SKILL.md links in the root README. Require playbook links in the existing Juan-mode index and reject missing playbook targets there. Jstack has no native plugin-agent catalog to validate. |
| Validate hardcoded model names against setup text | Omit this check. Jstack resolves configured models against T3's live catalog; setup prose is not a model allowlist. No configuration or model selection changes. |
| Report command and guide coverage | Preserve counts and missing-guide mentions; explicitly disclose when no guide pages exist. |

No skill instructions, upstream pins, review decisions or reviewed checkpoint change. This maintenance script adds no provider or plugin support claim.

## Verification

Run from the repository root:

```sh
node scripts/jstack/check_docs.mjs
node --test scripts/jstack/test_check_docs.mjs
python3 -B -m unittest scripts/jstack/test_skill_packaging.py
```

Executed on Linux with Node.js v24.19.0. The current tree reports 45 skills, including 24 principles, and 23 playbooks with zero detected problems. All 20 executable checker tests and four packaging tests pass.

Tests run the actual CLI in disposable repositories, from outside their root. They cover numeric and written stale counts, all four helper-reference forms, broken guide anchors, duplicate/Unicode/formatted headings, code-fenced headings, missing local targets, omitted catalog/playbook links and nonexistent indexed playbooks. Valid subset claims, other repository skills, unchecked remote URLs and historical records pass. An absent guide is disclosed. Temporary fixtures are removed after each test; no raw logs or copied repositories are retained.

## Use and limits

Example: an edit changes the current README to say "All 24 procedures" while only 23 playbooks exist. Run the checker before opening the documentation PR; it reports that count mismatch. Correct the wording and run it again. People using installed jstack skills do not need this command or a reinstall for this change.

This is a focused static check, not a Markdown parser or proof of semantic fidelity. It retains upstream's limited inline-link, ATX-heading and simple fence parsing. It does not inspect reference-style links, validate remote destinations, arbitrary prose, live model availability or provider support. Guide completeness remains pending; if a future guide uses another location, update its discovery and tests in that guide PR. CI integration remains a separate step.
