# Supplied analytics archive

Synthetic fixture. Dataset parcel.analytics.batch_sent. Schema snapshot: event_id string, recorded_at timestamp, batch_count integer. Rows are deduplicated by event_id. Do not assume example _timestamp or properties_* columns.
Creation/retention begins 2026-03-13. Daily counts: 2026-03-13=800, 2026-03-14=810. No earlier rows exist.
Instrumentation change PR #42 on 2026-03-13 introduced this event; it was not emitted before then. The step from absent events to 800/day cannot establish a usage increase.
No experiment/flag exposure dataset, pre-change batch distribution, latency measurement or notebook is included in this export. No raw SQL was executed to prepare this fixture.
