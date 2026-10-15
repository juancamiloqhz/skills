# Synthesis

Candidate A, from candidate-1/design.md, is the base. Both candidates independently selected the same callback shape and timing. Coordinator and cross-judge each scored A and B 20/20 against the rubric frozen before dispatch. Both preferred A for its explicit ambient-interrupt caveat. There was no scoring or base disagreement, dropout, or required structural diversity.

The final design keeps A's on_progress name and failure contract. The only graft from B is a pair of acceptance cases: a callable whose truthiness raises, and a send-raised BaseException. These strengthen checks of boundaries already present in the consensus design. B was reread before grafting; no API structure was imported.

Rejected alternatives were generators, built-in output/progress dependencies, total-based events, background workers, and a broad delivery exception handler, for the compatibility or complexity costs described in design.md. Catching only Exception would permit callback-raised base exceptions to stop delivery, contrary to the stated failure requirement. The accepted narrow BaseException catch has an explicit interrupt caveat.

All seats inherited the parent provider, model and effort. The live catalog identified Codex/gpt-6-astra. The configured judge pool had only an inherited alternative, so judging was from the same family. Labels A and B removed dispatch identity from the brief; they do not guarantee style anonymity.

Verification consisted of inspecting the synthesized design against every operation in the source and executing the unchanged source for baseline cases. Source and configuration hashes stayed unchanged. Proposed reporting behavior remains unimplemented and untested. See verification.md and baseline-observations.json.
