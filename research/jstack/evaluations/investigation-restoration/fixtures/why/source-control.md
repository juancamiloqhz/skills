# Supplied source-control archive

Synthetic fixture, not a live forge query. Project: Parcel. Target: limiter.py, BATCH_LIMIT = 100. Introducing change on 2026-03-12: 50 -> 100.

PR #41 title: Improve batch throughput.
Author: Mira. Body, 2026-03-11: Raising the batch limit should improve throughput. References PAR-8.
Full review thread, 2026-03-12:
Reviewer Theo: Do we have performance measurements for 100?
Author Mira: No. This is the maximum accepted by the partner contract. PAR-8 is the requirement. I reused a misleading title from the draft.
Reviewer Theo: Please keep the guard against larger batches; a partner rejection retries the whole batch.
No benchmark results or end-to-end incident proof are present in this archive.
