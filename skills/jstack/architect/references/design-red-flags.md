# Design red flags

Screen each candidate before synthesis. Record concrete evidence and its consequence; these are design questions, not automatic rejection rules.

| Signal | Check |
| --- | --- |
| Shallow module | Does the caller coordinate many methods or options while the module hides little complexity? |
| Information leakage | Do transport, storage or framework decisions escape into unrelated callers? |
| Temporal decomposition | Do pipeline stages split knowledge that should have one domain owner? |
| Pass-through methods | Does a layer forward calls without policy, adaptation or a useful boundary? |
| Split ownership | Can multiple writers or copied values disagree about one fact? |
| Duplicate routes | Must a change be repeated across several ways to perform the same task? Consolidate within compatibility and task scope. |
| Importable internals | Can callers bypass the intended interface? Use enforceable package boundaries where supported and state language limitations. |
| Hand-synchronized lists | Can one list be derived, or can a meaningful consistency check catch drift? |

Assume a future contributor may read only the nearest example. Prefer the shape where a locally plausible change preserves the system's invariants. Explain accepted tradeoffs instead of adding abstraction merely to clear a checklist.
