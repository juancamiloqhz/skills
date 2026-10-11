# Upstream attribution

Adapted from Lauren Tan's pstack `create-verification-skill` at `cursor/plugins` revision `ccb5507cec1546dc88135c1139c811e6c59115ba`, inspected on 2026-10-10.

- [Generator](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/create-verification-skill/SKILL.md).
- [Feature map index](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/create-verification-skill/references/feature-map-example/README.md), [creation example](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/create-verification-skill/references/feature-map-example/create-note.md), and [search example](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/skills/create-verification-skill/references/feature-map-example/search.md).
- [MIT license](https://github.com/cursor/plugins/blob/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack/LICENSE); Lauren Tan's notice is retained in this skill's `LICENSE`.

The adaptation retains repository inspection, project-local generation, the feature-map shape, real user-path proof, and evidence surviving cleanup. It replaces the fixed Cursor output directory with an explicit destination or repository convention, defaulting to `.agents/skills`. It uses T3's browser operations when applicable, allows ordinary subprocesses for noninteractive CLIs, and respects user-controlled installation.

The feature-map contract is expressed as a standalone reference rather than shipping a fictional app's commands. Normal skill discovery is retained so setup's optional offer can reach the generator; discovery is not authorization to generate or execute it. The optional offer belongs to the separate `setup-jstack` skill. The upstream maintenance command is not implemented. No automatic model selection or agent delegation is required. This is not an official Cursor, pstack, or T3 integration.
