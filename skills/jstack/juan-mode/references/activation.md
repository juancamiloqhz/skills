# Conversation state

Treat activation as a user instruction scoped to the current conversation. Explicit invocation turns it on, task completion leaves it on, and explicit opt-out turns it off. A request to author, review or explain juan-mode is not invocation. New conversations start inactive unless the user invokes it there. A delegated child receives only its task's relevant instructions and authority.

Retain this small record in the conversation's working state. Include it in a handoff or compaction summary when one is produced. Get the thread ID from T3 Code's current-thread configuration, not from a repository file or another task's example.

```json
{
  "juanMode": {
    "active": true,
    "threadId": "the-current-T3-thread-ID",
    "skillPath": "/absolute/path/to/juan-mode/SKILL.md"
  }
}
```

Record `active: false` on opt-out so an old activation summary cannot restore it. Keep current task and child IDs separately when work is still active. Turning the mode off changes subsequent routing and style; it does not cancel work already requested. An explicit stop request also cancels the task and reconciles its owned children and resources through the execution contract.

On resume, reconcile the record with later user messages in this conversation. The most recent explicit activation or opt-out wins. A record for another thread does not activate this one. Re-read the entrypoint at its discovered path when active instructions are no longer in context. If the path has moved, rediscover the installed skill. If activation history is unavailable, report that uncertainty instead of silently treating the conversation as active.

A saved file, this JSON shape and Cursor's `mode: true` metadata do not make a host reload the skill. Preserve the record in actual handoffs, but do not edit global instructions, repository agent files or host settings to force persistence. Conversation continuity, compaction and process restart need separate runtime evidence for each coordinating provider. Until those checks pass, describe persistence as intended behavior with unverified resume support.
