# Review criteria

Apply the relevant lenses to the stated intent. A design is a proposal: identify missing contracts without pretending pseudocode has executed.

- Correctness: trace boundary values, error handling, state transitions, retries and crash recovery. Consider concurrency only when multiple actors can reach the state. Show the path that makes a failure possible.
- Root cause: inspect callers, callees and types before judging a guard, retry or cast. Prefer an enforced invariant over a convention when it addresses an actual failure.
- Structure: assess ownership, validation boundaries, data access patterns and coupling. Identify leaked internal decisions and pass-through layers. Compatibility costs depend on actual consumers and migration scope.
- Verification: distinguish behavior tests from implementation-shaped assertions and static inspection. Check actual artifacts for delegated work rather than trusting summaries. Name untraced integrations and unavailable checks.
- Complexity: look for structural simplifications that remove branches, duplicate state or unnecessary layers. Explain the maintenance cost and a concrete simpler shape; line count alone is not a blocker. Avoid speculative configuration and unnecessary abstraction.
- Security: trace an input or authority boundary to the affected operation. Explain the reachable exploit or exposure, not a generic possibility.

For code quality, prioritize meaningful simplification, cohesive modules, useful types, canonical helpers and atomic updates where partial state is a real risk. A large file or repeated conditional warrants inspection, not an automatic rewrite. Read-only review recommends changes; it does not make them.
