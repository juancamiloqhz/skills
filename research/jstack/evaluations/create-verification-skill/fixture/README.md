# Pocket

Pocket is a local note CLI requiring only Python 3. It has no server, external services, credentials or package installation. Commands print JSON. A data directory must be supplied on each invocation.

## Run

From this repository root:

```sh
python3 pocket.py --version
python3 pocket.py --data-dir /tmp/pocket-example add --title 'Packing list' --body 'Passport and charger'
python3 pocket.py --data-dir /tmp/pocket-example show 1
python3 pocket.py --data-dir /tmp/pocket-example list
```

Use a fresh data directory for independent sessions. Existing user data must be preserved. Reads do not create directories or files. Writes persist in `notes.json` inside the supplied directory; IDs increase from the highest existing ID. Concurrent writes to one directory are unsupported.

Titles are trimmed; blank titles and missing note IDs are errors with nonzero exit status. The CLI does not have a delete command. Disposable session data can be removed after verification. There is no UI or existing verification harness.
