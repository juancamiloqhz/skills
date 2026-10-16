# Skill-authoring evaluation

Authoring or modifying a skill is the fourth internal Juan-mode procedure. It uses the host authoring guide, validates frontmatter and references, tests structural changes and preserves the requested delivery boundary. The other 19 procedures remain pending.

## Source and scope

[Complete source comparison](source-comparison.json) covers the new procedure and full mode entrypoint at `11713c683fe4add4fd403ea880580abbc9e0875f`, plus setup's entrypoint at `ccb5507cec1546dc88135c1139c811e6c59115ba`. The [adaptation record](../../adaptations/authoring-a-skill.md) accounts for every new difference. The original heading, four-step order, concise-writing paragraph and reply contract remain intact. Previous entrypoint differences retain their earlier assessments.

All existing mode/setup files except the three availability-bearing files match the merged PR #46 base recorded in the comparison. The three previous playbooks are unchanged. Licenses match their pins. The manifest adds Encode Lessons in Structure as mode context; 41 mappings, watched roots, pins, decisions and reviewed checkpoint remain unchanged.

The authoring dependency in this exercise is the advertised Codex system `skill-creator` at `/home/ubuntu/.codex/skills/.system/skill-creator/SKILL.md`. It replaces the unavailable Cursor built-in under the accepted host-authoring contract. This records one exact guide and its hash, not equivalence between every host's authoring skill.

## Structural edit

The local request adds comparison support to a release-notes skill while preserving its existing summary behavior and metadata. The supplied `release-facts` helper lives outside that skill's directory. Publication and installation are explicitly excluded. [Inputs](inputs.json) retain the request, original package, snapshots, catalog and input hashes.

[Authoring evidence](authoring-evaluation.json) preserves the edited package, actual validation, author-run examples, writing records and step statuses. The resulting router retains the summary reference and adds a comparison reference. It resolves its independent helper through the supplied catalog and reports incomplete fact-checking when the helper is absent.

The parent copies that package to a new layout and the helper to a separate directory, then supplies a new catalog. [Parent verification](parent-verification.json) checks byte-identical copies, frontmatter, package references and helper identity. A deliberately broken packaged link fails validation, as does an unavailable catalog helper. These are executed checks of a fixture-specific validator, not a new runtime validator shipped by jstack.

[Consumer evidence](consumer-evaluation.json) runs the resulting skill in a fresh agent on new June/July inputs. It receives only the copied package, independent catalog/helper and snapshots, with no authoring conclusions. The two requests exercise a single-snapshot summary and a two-snapshot comparison. Parent assessment reads the actual outputs against the supplied data. This checks behavior separately from the author agent's own examples. The consumer correctly reports the seat decrease from 10 to 6, PDF becoming available, JSON removal and Excel remaining planned, with both input paths beside each change. The summary also preserves July's available-versus-planned distinction. The three copied operational files remain byte-identical; the author added a separate validation note afterward, retained only in the author archive.

The author-run reverse case included unnecessary unchanged CSV context despite the comparison instruction. Its original output is preserved. The author also left the mode's delegated How incomplete because further delegation was explicitly prohibited, and did not invent the unavailable Feature throughput checkpoint. These limits prevent a claim of complete Juan-mode execution. Parent verification confirms all 19 recorded source/input hashes and the global configuration are unchanged.

## Wording-only edit

[Wording evidence](wording-evaluation.json) records a parent-executed edit that replaces filler with plain instructions. Both original and revised frontmatter pass the host validator. Metadata and the referenced format file remain unchanged, and package links resolve. The structural-test step is explicitly skipped because the edit preserves behavior. No runtime test or independent-agent result is claimed for this case.

The writing record retains the initial text, the concrete replacements and a meaning/wording self-audit. Both authoring cases preserve local-only delivery and report Opening a PR as an unavailable procedure. Neither claims to have run that workflow.

## Repository checks and limits

[Validation](validation.json) records four packaging tests, both changed entrypoint validators, actual manifest validation, changed Markdown lint, relative links and staged whitespace checks. The first source comparison caught an omitted setup consumer-note update; the note was corrected before the final comparison. The upstream H3 fragment uses a byte-identical temporary lint copy with MD041 disabled. No runtime scripts changed, so unrelated resolver suites are not repeated.

Raw text and commands are archived in JSON without rewriting the original responses. Scratch fixtures remain under `/tmp/jstack-authoring-20261016`, `/tmp/jstack-authoring-wording-20261016`, `/tmp/jstack-notes-consumer-20261016` and `/tmp/jstack-authoring-negative-20261016`. Scripts and catalogs retain their original absolute paths; replay elsewhere requires rebinding owned scratch paths.

These are bounded Codex authoring and consumer exercises with explicit paths and a simulated catalog. They do not establish installed host discovery, other-provider behavior, persistent activation, missing-authoring-tool recovery, autonomous skill creation or the pending Opening a PR/Eval procedures. No model configuration, schedule, installed skill or repository source is modified by the exercises.
