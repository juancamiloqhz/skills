Task /root/verification_maintenance_eval/ledger_export_refresh completed.

1. Feature summary: The public command is python3 ledger.py --data DIR export. Every valid export invocation prints {"error": "export entitlement unavailable"} and exits 3 before accessing data. Successful export is unreachable in this fixture. This is a source finding; I did not run the app.

2. Source entry points: ledger.py:5 requires --data; ledger.py:8 registers export; ledger.py:10 implements unconditional rejection. drive.py:28 checks exit 3, exact JSON, empty stderr, and absence of the target directory, then records verified-unreachable. All five reviewed files match their identities in revised-hashes.json.

3. Documentation drift: None for the export rejection contract. README.md:5, SKILL.md:20, and export.md:19 agree with source. "Export the current note as JSON" at export.md:5 describes intended functionality, immediately qualified as unreachable. Source contains neither an entitlement lookup nor a successful export implementation.

4. Live verification recipe: From the fixture root, run the documented doctor with a fresh evidence filename, then the export drive with another fresh evidence filename:

```bash
python3 .agents/skills/verify-ledger/scripts/drive.py doctor /absolute/evidence/doctor-export-refresh.json
python3 .agents/skills/verify-ledger/scripts/drive.py export /absolute/evidence/export-refresh.json
```

The helper invokes the public CLI against a nonexistent child of its owned temporary directory. Confirm recorded product exit 3, exact rejection JSON, empty stderr, data_created: false, outcome: "verified-unreachable", and cleanup: true; confirm retained evidence exists. Helper exit 0 means the rejection matched its contract, not that export succeeded.
