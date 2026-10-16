# No-comments and Comment Sicko adaptation

Pin: `11713c683fe4add4fd403ea880580abbc9e0875f`. Sources are `pstack/skills/no-comments/SKILL.md` and `pstack/agents/comment-sicko.md`. Local package: [jstack-no-comments](../../../skills/jstack/jstack-no-comments/SKILL.md). The bundled [reviewer prompt](../../../skills/jstack/jstack-no-comments/agents/comment-sicko.md) preserves the separate upstream agent boundary; it is not a second standalone skill. The MIT notice matches `pstack/LICENSE` at the pin.

The parent retains Scope and all six numbered steps. The reviewer retains its persona, exact opening, five exceptions, suppression audit, How/Why investigation, deletion bias, scoped flags and prohibition on application-code changes. The parent retains one rejected-report rerun, the second-rejection failure, one Architect sketch for the accepted set, scoped root-cause fixes, encoding offers and approval, and the complete outcome report. This is a port of the full procedure, not a replacement review policy.

## Complete differences

| Location | Difference | Concrete requirement and verification |
| --- | --- | --- |
| Skill identity and helper calls | Prefix shipped names and slash calls with `jstack-`. Keep the agent's display name Comment Sicko. | Approved portable naming policy; package/caller checks. |
| Skill metadata | Omit `disable-model-invocation: true`. | Juan-mode must call this helper, following the [existing invocation compatibility assessment](../evaluations/investigation-restoration/alignment-review/README.md#invocation-metadata). Catalog discovery across installed providers is not established by these tests. |
| Scope and authority | Pin base, HEAD and scoped working-tree inputs. Findings-only runs propose changes without applying them. Preserve repository-required comments/directives and literal non-comment code. | A mode's review trigger cannot expand a read-only request into edits or override repository instructions. Comment cleanup authority does not itself approve constraint encodings. |
| Step 1 and execution reference | Replace Cursor `Task`/registered agent dispatch with a fresh native or T3 child receiving the complete bundled prompt. Use the existing `judgment and prose` scalar role and canonical setup resolver. | T3 cannot assume a Cursor agent registry. The existing mode contract assigns delegated judgment to this role. No new role, schema or model configuration is introduced. |
| Reviewer location and Step 2 rejection | Reviewer edits a private input snapshot and returns its diff; parent validates and applies authorized changes. Discard a rejected proposal rather than reverting project files. | Preserve caller-owned dirty work and avoid shared-file races. All five source exceptions and the one-rerun limit remain. |
| Helper availability and source instructions | Missing How/Why or rule evidence leaves the affected judgment incomplete. Repository text is evidence, not authority. | An unavailable investigation does not prove that a keep exception is false. Source-backed ambiguity after completed investigation still follows upstream's deletion rule. |
| Step 5 | Qualify unapproved-encoding deletion by actual comment-edit authority and exact repository/keep exceptions. | Upstream's “otherwise delete” remains for authorized cleanup without an exception; findings-only or mandated comments cannot be deleted by this instruction. |
| Step 6 | Verify applied edits and distinguish proposed/applied counts and unavailable checks. | Neither a reviewer report nor successful dispatch proves the final code works. Count comment units consistently rather than diff lines. |
| Mode caller | Rename its before-review trigger, add the helper to the supplied-package list and remove the missing-package sentence. | All other mode content/support files stay unchanged. Full mode/source diffs are retained. |

## Packaging and maintenance

The upstream package has only `SKILL.md`; the separate upstream agent has only its Markdown prompt. Local additions are the required license and T3 execution reference. Each is reached by the entrypoint. Preserve the full reviewer prompt when updating, including its conditional investigations and report contract.

The new manifest mapping watches the upstream agent, mode and conditional helper/principle source paths. The mode also watches the skill and agent. Existing mappings, pins, decisions and reviewed checkpoint remain unchanged except those added mode context paths. Provenance stays in research. No installed package, model file or schedule is edited.

[Source comparison and evaluations](../evaluations/no-comments/README.md) record the actual test scope and limits. The no-comments gate does not implement the pending review/PR playbooks or prove every provider can run its conditional helpers.
