#!/usr/bin/env python3
"""Loopback-only preview fixture; public dummy key, no real webhook or task."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts/jstack"))
from bot_ui_local import Journal, make_server
from bot_ui_transport import send, write_secret
from test_bot_ui_transport import receiver

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--directory", type=Path, required=True, help="Existing private scratch directory; retained across restarts.")
parser.add_argument("--port", type=int, default=8879)
parser.add_argument("--receipt", choices=("direct", "recorded", "queued"), default="direct")
args = parser.parse_args()
journal = Journal(args.directory / "requests.sqlite", "example/fixture", 123)
key = args.directory / "key"
if not key.exists():
    write_secret(key, "public-local-ui-preview-fixture-only")


def deliver(payload):
    mode = args.directory / "drop"
    outcome = "accepted" if args.receipt == "direct" else None
    response = b'{"queued":true}' if args.receipt == "queued" else None
    with receiver(drop=mode.exists(), outcome=outcome, response=response) as (url, received):
        receipt = send(url, key, payload, allow_loopback_http=True)
    count_file = args.directory / "received-count"
    previous = int(count_file.read_text()) if count_file.exists() else 0
    count_file.write_text(str(previous + len(received)))
    return receipt


server = make_server(("127.0.0.1", args.port), [f"http://127.0.0.1:{args.port}"], journal, deliver)
print(f"Fixture only: http://127.0.0.1:{args.port}", flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
