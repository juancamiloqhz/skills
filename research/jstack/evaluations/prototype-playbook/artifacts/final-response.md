I recommend accepting valid rows whose IDs occur only once and rejecting every row in a duplicate group. That is a design judgment based on the conflicting c1 emails in the supplied inputs.

The experiment produced these accepted rows. Row numbers start at one within each upload. Every other row was rejected.

| Input | Reject whole upload | Accept first valid occurrence | Reject duplicate groups |
| --- | --- | --- | --- |
| clean | 1, 2 | 1, 2 | 1, 2 |
| duplicate | None | 1, 3 | 3 |
| invalid | None | 1, 3 | 1, 3 |
| mixed | None | 1, 4 | 4 |

[Raw output](/tmp/jstack-prototype-live-20261016/raw-stdout.jsonl) includes the accepted data and every rejection reason. In both duplicate cases, first-valid acceptance keeps one@example.invalid and rejects replacement@example.invalid. Whole-upload rejection blocks otherwise valid rows. Rejecting duplicate groups lets unrelated valid rows proceed without choosing which conflicting email is correct.

Whole-upload rejection offers a clear all-or-nothing outcome but forces operators to correct the upload before any row proceeds. First-valid acceptance keeps more rows but lets row order choose between conflicting values. Rejecting duplicate groups requires more corrections while preserving unrelated progress. These are policy tradeoffs, not measured operator outcomes.

Model the Domain led to explicit accepted and rejected row records. Exhaust the Design Space added the third policy. Prove It Works led to running the script and inspecting its output.

The [script](/tmp/jstack-prototype-live-20261016/prototype.py) is throwaway. Its scratch directory is /tmp/jstack-prototype-live-20261016. It checks only the required nonempty-string fields and duplicates within each upload. It does not save imported records. The [procedure record](/tmp/jstack-prototype-live-20261016/procedure-record.md) names skipped steps and limitations. The design experiment is complete. Feature remains unavailable, and no real importer was implemented.
