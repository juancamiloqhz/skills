Task /root/verification_maintenance_eval/ledger_read_source completed.

1. Feature summary: get reads DIR/note.json and emits JSON without writing state. Source predicts a missing note returns {"error":"missing note"} with exit 2; an existing note returns its body uppercased, normally with exit 0. This is source analysis only; no CLI was executed.

2. Source entry points: CLI arguments and get registration are in ledger.py:5. Creation stores the original body at ledger.py:12. Missing-note handling, file loading, and uppercase output begin at ledger.py:16.

3. Drift and contract discrepancy: README.md:9 explicitly preserves the verbatim contract through migration, and read.md:5 agrees. Therefore, uppercase output is an apparent product regression, not evidence that the documented expectation should change. Separately, verification tooling is stale: SKILL.md:14 and drive.py:17 expect ledger 1; drive.py:22 invokes removed command add, preventing the read assertion from being reached. Its verbatim assertion at drive.py:27 remains consistent with the accepted contract.

4. Live verification recipe: From the fixture root, record python3 ledger.py --version and require ledger 2. Allocate a fresh owned temporary data directory, run python3 ledger.py --data DIR create --body 'Case Sensitive', then python3 ledger.py --data DIR get. Require exit 0 and decoded JSON {"body":"Case Sensitive"} for both; confirm persisted JSON remains identical. Source predicts the get assertion will fail with {"body":"CASE SENSITIVE"}. Retain commands, outputs, exit statuses, assertions, and cleanup evidence outside scratch; remove only the owned temporary directory in finally.
