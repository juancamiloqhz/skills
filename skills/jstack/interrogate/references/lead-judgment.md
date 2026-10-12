# Lead judgment

Use conversation constraints and source evidence to assess every finding. Reviewers may lack migration context or mistake a preference for a defect. Recheck the underlying claim rather than dismissing it because it is inconvenient or came from one reviewer.

| Category | Meaning |
| --- | --- |
| Act on | A demonstrated correctness, security or material maintenance issue that should block delivery for this scope. Explain impact and the smallest useful remedy. |
| Consider | A legitimate issue whose benefit versus cost needs a decision. State the tradeoff. |
| Noted | Valid context or a low-impact concern that does not warrant action now. |
| Dismissed | Incorrect, unsupported, out of scope or merely preferential. Explain the source or constraint that resolves it. |

Preserve reviewer attribution and disagreements after deduplication. Silence is not agreement. A lone reachable defect outweighs several unsupported approvals; shared findings still require verification. Do not cap the number of real blockers to fit an output template. If only preferences remain, say that no actionable defect was established, while retaining coverage limitations. A clean review is not proof of correctness.
