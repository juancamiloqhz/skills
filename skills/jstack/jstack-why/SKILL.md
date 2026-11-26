---
name: jstack-why
description: "Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Returns a cited read on decisions and tradeoffs. Use jstack-how for runtime behavior."
---

# Why

Answer from the record, not the code: read the commits and PR discussions that introduced the target and each later change, and other sources if the trail is thin. Cite what the authors wrote, mark your own inferences as inferences, and say what the record does not answer.

Run directly for the user's question or as a procedure called by a jstack-juan-mode playbook. Direct invocation is task-scoped and leaves jstack-juan-mode activation unchanged. Investigation is read-only: do not edit source, configuration or external records. Report unavailable or shallow history and inaccessible sources as gaps. Return findings without launching implementation or another playbook.
