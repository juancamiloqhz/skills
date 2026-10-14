Task /root/verification_maintenance_eval/ledger_create_source completed.

1. Feature summary

`python3 ledger.py --data DIR create --body TEXT` creates the data directory if necessary, stores `{"body": TEXT}` in `note.json`, emits the same JSON, and exits 0. The body string is preserved. Existing `note.json` contents would be overwritten, so verification must use fresh owned data. All five inspected fixture files match their frozen hashes. This is source analysis; no application commands were executed.

2. Source entry points

- ledger.py:5 requires --data; ledger.py:7 registers create with required --body.
- ledger.py:12 implements directory creation, persistence, JSON output, and successful exit.
- README.md:5 documents the public command and verbatim storage contract.
- README.md:9 records the accepted migration from add to create and identity ledger 2.

3. Documentation drift

The create implementation matches the README's create contract. The verification materials retain version 1 instructions:

- create.md:5 still calls the command add.
- drive.py:22 invokes add. Source inspection predicts argument-parser rejection before the create assertions run.
- SKILL.md:14 and drive.py:17 expect ledger 1, whereas ledger.py:4 reports ledger 2.

Separately, the documented read contract promises the same verbatim body, but ledger.py:19 uppercases it. This is a source-visible product mismatch, not evidence that create storage should change. None of these predictions has been verified live by this review.

4. Live verification recipe

From the fixture root, run the public --version command and assert ledger 2. Allocate a fresh temporary directory, then invoke:

```bash
python3 ledger.py --data "$data" create --body 'Case Sensitive'
```

Capture arguments, stdout, stderr, and exit status to a unique evidence path outside that directory. Assert exit 0, parsed stdout equal to {"body":"Case Sensitive"}, and parsed $data/note.json equal to the same object. In finally, remove only the owned directory, assert its absence, and retain the evidence file. Do not use get to establish create correctness because its source currently changes case.
