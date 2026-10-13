---
name: principle-outcome-oriented-execution
description: "Apply outcome oriented execution guidance. Use during an explicitly planned rewrite or migration."
---

# Outcome oriented execution

Define the target and verification boundaries. Temporary breakage is acceptable only inside a declared, isolated and recoverable unit, not in a live service or shared integration state by assumption. Keep focused checks while migrating and verify the combined result before delivery. A unit may contain intermediate failing states; dependent units wait for its gate.

Apply within the requested scope and existing authorization. Direct invocation does not activate juan-mode and requires no model configuration or delegation.
