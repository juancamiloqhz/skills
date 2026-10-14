Task /root/verification_maintenance_eval/ledger_read_refresh completed.

1. Feature summary: get reads DIR/note.json and emits a JSON body. The documented contract preserves text verbatim; the implementation uppercases it. Missing notes produce {"error":"missing note"} with exit 2. These are source findings; no CLI was run.

2. Source entry points: ledger.py:5 requires --data; ledger.py:8 registers get; ledger.py:16 handles missing notes; ledger.py:18 loads persisted JSON; ledger.py:19 applies .upper().

3. Documentation drift: README.md:5 and read.md:5 specify verbatim reads. The accepted migration explicitly preserves that contract at README.md:9. Thus the disagreement indicates an implementation defect, not evidence that documentation should adopt uppercase behavior. The helper correctly asserts case preservation at drive.py:27, consistent with SKILL.md:20.

4. Live verification recipe: From the fixture root, run the documented doctor helper with a unique absolute evidence path, then the read helper with another unique path. It creates fresh owned data through create --body 'Case Sensitive', verifies persistence, and calls public get. Expect get to emit {"body":"CASE SENSITIVE"} with exit 0, causing the helper's verbatim assertion to fail and the helper to exit 1. Confirm retained evidence reports failure and successful cleanup; rerun doctor afterward as required by the skill.
