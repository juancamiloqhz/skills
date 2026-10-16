# TDD adaptation

Source: `pstack/skills/tdd/SKILL.md` at `11713c683fe4add4fd403ea880580abbc9e0875f`. Local: [jstack-tdd](../../../skills/jstack/jstack-tdd/SKILL.md). The source directory contains one file. Preserve its description, six workflow steps, impractical-test alternative, guardrails and evidence-oriented reply. The package carries the exact pinned pstack MIT notice.

## Complete differences

| Location | Change | Requirement and limit |
| --- | --- | --- |
| Name | `tdd` becomes `jstack-tdd`. | User-approved portable identity policy. |
| Invocation metadata | Omit `disable-model-invocation: true`. | Bug fix's approved caller design must discover and invoke the helper. The existing [compatibility assessment](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) documents the Claude catalog-call restriction. As with How and Why, the shared helper remains eligible for model selection. This is a deliberate metadata difference, not a claim that pstack's explicit-only policy is reproduced. |

The entire body and description otherwise match upstream. The narrow trigger remains in the description. No new script, model role, test framework, permission checkpoint or mandatory test ceremony is added. Existing user scope controls whether a fix is authorized. A local regression test does not replace the future Bug fix playbook's same-interface reproduction and mechanism proof.

## Installed TDD assessment

The installed `/home/ubuntu/.agents/skills/tdd/SKILL.md` describes a broader red/green workflow with public testing boundaries, required user confirmation of those boundaries, additional test/mocking references and a separate refactoring stage. Pstack's pinned TDD skill instead defines a focused six-step bug-fix procedure and an explicit alternative when a new test is impractical. These are different procedures. Do not treat the unprefixed installation as an equivalent dependency or modify it to fit jstack.

[The complete comparison](../evaluations/tdd/source-comparison.json) retains both source hashes and the full installed-entrypoint difference. This is an assessment of that file, not an audit of its supporting package or future versions. The faithful standalone port resolves the identity and workflow mismatch. Provider installation remains manual.

## Maintenance and verification

The manifest adds one mapping with the pinned Bug fix playbook as source context. Both paths are already covered by the `pstack` watch root. Existing mappings, watches, source pins, decisions and reviewed checkpoint are unchanged. There are 44 mappings, five implemented playbooks and 18 pending procedures. No operational Juan-mode caller changes in this port; Bug fix is still unavailable.

[Evaluation and validation](../evaluations/tdd/README.md) retain a focused regression's failing-before/passing-after output and a separately unavailable native integration. Installed discovery, full-mode Bug fix, commit sequencing, concrete model selection and cross-provider invocation remain untested.
