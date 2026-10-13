# Jstack adaptation records

Source pins and adaptation rationale live here instead of inside installed skill packages. The [upstream manifest](../upstream.json) maps each component to its record. The 24 principle records remain in [principle adaptations](../principle-adaptations.md).

On 2026-10-13, the 12 foundation/helper records moved from `skills/jstack/<name>/references/upstream.md` to this directory. Existing rationale is preserved as a record of the implementation, not blanket approval. The [fidelity audit](../fidelity-audits/2026-10-13/README.md) identifies remaining structural and behavioral corrections.

## Packaging correction

The move follows the explicit [provenance policy](../upstream-fidelity.md#provenance-location). Each mapped component retains its exact upstream path and `adaptedFrom` pin. Compared the 12 pinned entrypoints and plugin MIT notices with the final local packages. The removed local provenance records and attribution-only paragraphs are jstack additions, not upstream workflow steps. Operational scope, dependency discovery, model configuration, procedure instructions and all package licenses remain intact. Setup's mixed heading becomes `Scope`; its authorization and no-delegation instructions remain.

Research links and the manifest now point here. Relative links inside moved records resolve to the same licenses and operational references. Historical audit paths, evaluation hashes and checkpoint records remain dated evidence of their original files. Neither relocation nor a prior merged rationale resolves the audit's outstanding behavior questions.

Validation for this correction checks all 12 packages in isolated temporary directories with the skill validator and relative-file links, compares their licenses byte-for-byte with the exact pinned upstream notices, validates the manifest, and checks Markdown and whitespace. This is packaging validation; no workflow execution or installed-provider discovery is claimed.
