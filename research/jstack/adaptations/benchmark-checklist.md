# Benchmark checklist adaptation

The [2026-10-15 naming decision](../skill-names.md) additionally changes this package's local identity and callers. Its upstream identity, procedure and revision pin remain as recorded below.

Source: [pstack benchmark-checklist](https://github.com/cursor/plugins/blob/11713c683fe4add4fd403ea880580abbc9e0875f/pstack/skills/benchmark-checklist/SKILL.md), revision `11713c683fe4add4fd403ea880580abbc9e0875f`. Local package: [benchmark-checklist](../../../skills/jstack/jstack-benchmark-checklist/SKILL.md). The package [MIT license](../../../skills/jstack/jstack-benchmark-checklist/LICENSE) matches the pinned plugin notice, including Lauren Tan's attribution.

The source directory contains only `SKILL.md`. Its name, description, introduction, one-run ballpark exception, preparation, all seven questions, reporting rules and playbook integration bullets are preserved. No question, threshold, example or section is summarized or moved. The package needs no model resolver, new role, script or supporting reference; the caller applies it to the actual measurement.

## Complete differences

| Location | Difference and concrete reason | Verification or limit |
| --- | --- | --- |
| Frontmatter | Omit `disable-model-invocation: true` so Juan-mode and Explain the Number can discover and call it through the skill catalog. | The established [invocation compatibility exception](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata) documents the Claude guard conflict. Automatic selection remains possible; all-provider installation/discovery is unverified. |
| After introduction | Add task-scoped use, no persistent-mode/configuration change, preservation of unrelated work/processes, owned outputs and manual tool installation. | Existing host/user authority. A measurement request does not authorize stopping other workloads or installing a profiler. Missing prerequisites remain visible. |
| After Other perf material | Explain that the named Juan-mode playbooks remain unavailable and publication follows existing authority. | This standalone checklist works without a mode installation or a fabricated procedure. Its one-primary-number rule remains inline; Opening a PR, Perf issue and Hillclimb are not implemented here. |

[Source comparison and evaluation](../evaluations/benchmark-checklist/README.md) distinguish actual measurements from supplied counterexamples. The full final skill diff is recorded. No performance claim about jstack, production systems or different models follows from a synthetic fixture.

## Callers and maintenance

Juan-mode's existing mandatory measurement trigger is unchanged. Two availability sentences now list benchmark-checklist as a shipped standalone helper rather than a missing package. The comparison records the complete pinned mode diff and the exact two-sentence change against merged PR #38. All other mode instructions and supporting files remain unchanged. Explain the Number already calls the helper by catalog identity, so its body needs no edit.

The manifest adds this component at the consuming principle/mode pin, retains Explain the Number's existing context watch, adds the mode's direct helper watch, and watches the three named playbook source paths for this helper. Existing component pins, review decisions and the reviewed checkpoint remain unchanged. Research status and package listings now point to the implementation; historical audits and evaluation snapshots retain their original missing-dependency observations. Installation remains manual.

## Perf issue caller availability

Perf issue now has a Juan-mode procedure. The final availability paragraph names it as available and continues to disclose missing Hillclimb and Opening a PR. All measurement questions, preparation, reporting rules and invocation boundaries remain unchanged. The [full pinned comparison](../evaluations/perf-issue/source-comparison.json) records this one-paragraph update.
