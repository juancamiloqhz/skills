#!/usr/bin/env python3
"""Loopback-only preview fixture; public dummy key, no real webhook or task."""

import argparse
import http.client
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import sys
import threading

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "scripts/jstack"))
from bot_ui_local import Journal, make_server
from bot_ui_transport import send, write_secret
from test_bot_ui_transport import receiver

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--directory", type=Path, required=True, help="Existing private scratch directory; retained across restarts.")
parser.add_argument("--port", type=int, default=8879)
parser.add_argument("--receipt", choices=("direct", "recorded", "queued"), default="direct")
parser.add_argument("--mount-path", help="Test a path-stripping loopback proxy, e.g. /jstack-bot-ui/.")
parser.add_argument("--origin", action="append", help="Exact page origin for a separately authorized proxy test.")
args = parser.parse_args()
if args.mount_path and not re.fullmatch(r"/(?:[a-zA-Z0-9_-]+/)+", args.mount_path):
    parser.error("mount-path must contain slash-terminated path segments")
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


server = make_server(("127.0.0.1", 0 if args.mount_path else args.port),
                     args.origin or [f"http://127.0.0.1:{args.port}"], journal, deliver)
backend = None
if args.mount_path:
    backend = server
    class Proxy(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass

        def forward(self):
            if not self.path.startswith(args.mount_path):
                body = b"Existing application fixture"
                self.send_response(200 if self.path == '/' else 404)
                self.end_headers()
                self.wfile.write(body)
                return
            body = self.rfile.read(int(self.headers.get('Content-Length', 0)))
            connection = http.client.HTTPConnection(*backend.server_address, timeout=8)
            try:
                connection.request(self.command, '/' + self.path[len(args.mount_path):], body, dict(self.headers))
                response = connection.getresponse()
                self.send_response(response.status)
                for key, value in response.getheaders():
                    if key.lower() not in ('connection', 'transfer-encoding'):
                        self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
            finally:
                connection.close()

        do_GET = do_POST = forward

    threading.Thread(target=backend.serve_forever, daemon=True).start()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Proxy)
print(f"Fixture only: http://127.0.0.1:{args.port}{args.mount_path or '/'}", flush=True)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    server.server_close()
    if backend:
        backend.shutdown()
        backend.server_close()
