# Supplied observability archive

Synthetic fixture. Service parcel-export.
Monitor MON-3, created by Mira 2026-03-13: alert if partner batch rejection exceeds 10/min; query counts rejected responses for parcel-export. Dashboard DASH-2 reuses MON-3.
Telemetry retention starts 2026-03-13, after PR #41. No traces or logs from the change window are retained. Historical searches for 2026-03-01 through 2026-03-12 return no rows for this reason.
No formal incident/postmortem is present in this export. Empty rows do not mean no prior failures occurred.
