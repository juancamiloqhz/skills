#!/usr/bin/env python3
"""Local PR-status button and recovery journal. Does not provision a webhook."""

import argparse
from contextlib import contextmanager
from dataclasses import asdict
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import sys
from urllib.parse import urlsplit

from bot_ui_transport import Receipt, TransportError, encode_request, read_secret, send


ASSETS = Path(__file__).with_name("bot_ui_assets")
ID = re.compile(r"[A-Za-z0-9_-]{1,80}")


class JournalError(Exception):
    pass


class Journal:
    """Persist intent before delivery; one claim per request, with explicit acknowledgement."""

    def __init__(self, path, repository, pr):
        self.path = Path(path).absolute()
        self.repository, self.pr = repository, pr
        encode_request(self.payload("validation"))
        parent = self.path.parent.stat()
        if parent.st_uid != os.geteuid() or stat.S_IMODE(parent.st_mode) & 0o077:
            raise JournalError("Journal directory must be owned by you with mode 0700.")
        fd = os.open(self.path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600)
        try:
            info = os.fstat(fd)
            if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid()
                    or stat.S_IMODE(info.st_mode) & 0o077):
                raise JournalError("Journal must be an owned, private regular file.")
        finally:
            os.close(fd)
        with self.connection() as db:
            db.execute("CREATE TABLE IF NOT EXISTS scope (singleton INTEGER PRIMARY KEY CHECK(singleton=1), repository TEXT, pr INTEGER)")
            db.execute("INSERT OR IGNORE INTO scope VALUES (1, ?, ?)", (repository, pr))
            if tuple(db.execute("SELECT repository, pr FROM scope").fetchone()) != (repository, pr):
                raise JournalError("Journal belongs to a different repository or PR.")
            db.execute("""CREATE TABLE IF NOT EXISTS requests (
                id TEXT PRIMARY KEY, payload TEXT NOT NULL, delivery TEXT NOT NULL,
                owner TEXT, acknowledgement TEXT,
                created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
            )""")
            db.execute("""CREATE TABLE IF NOT EXISTS results (
                request_id TEXT PRIMARY KEY, body TEXT NOT NULL,
                saved_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
            )""")

    @contextmanager
    def connection(self):
        db = sqlite3.connect(self.path, timeout=8)
        db.row_factory = sqlite3.Row
        try:
            with db:
                db.execute("BEGIN IMMEDIATE")
                yield db
        finally:
            db.close()

    def payload(self, request_id):
        payload = {"requestId": request_id, "action": "check-pr", "repository": self.repository, "pr": self.pr}
        encode_request(payload)
        return payload

    def record(self, request_id):
        payload = encode_request(self.payload(request_id)).decode()
        unknown = json.dumps(asdict(Receipt(request_id, "unknown")))
        with self.connection() as db:
            return db.execute("INSERT OR IGNORE INTO requests(id,payload,delivery) VALUES (?,?,?)",
                              (request_id, payload, unknown)).rowcount == 1

    def delivered(self, receipt):
        with self.connection() as db:
            db.execute("UPDATE requests SET delivery=? WHERE id=?", (json.dumps(asdict(receipt)), receipt.request_id))

    def status(self, request_id):
        with self.connection() as db:
            row = db.execute("""SELECT requests.*, results.request_id AS result_id FROM requests
                                LEFT JOIN results ON results.request_id=requests.id WHERE id=?""",
                             (request_id,)).fetchone()
        if row is None:
            return None
        if row["acknowledgement"]:
            processing = "completed" if row["result_id"] else "acknowledged_without_result"
        else:
            processing = "result_saved" if row["result_id"] else "claimed" if row["owner"] else "pending"
        return {"requestId": row["id"], "delivery": json.loads(row["delivery"]), "processing": processing}

    def pending(self):
        with self.connection() as db:
            rows = db.execute("SELECT * FROM requests WHERE acknowledgement IS NULL ORDER BY created_at,id").fetchall()
        return [{"payload": json.loads(row["payload"]), "delivery": json.loads(row["delivery"]),
                 "owner": row["owner"], "createdAt": row["created_at"]} for row in rows]

    def claim(self, request_id, owner):
        if not ID.fullmatch(owner):
            raise JournalError("Owner must be 1-80 letters, digits, underscores or hyphens.")
        with self.connection() as db:
            granted = db.execute("UPDATE requests SET owner=? WHERE id=? AND owner IS NULL AND acknowledgement IS NULL",
                                 (owner, request_id)).rowcount == 1
            row = db.execute("SELECT payload FROM requests WHERE id=?", (request_id,)).fetchone()
        return {"granted": granted, "payload": json.loads(row["payload"]) if granted else None}

    def acknowledge(self, request_id, owner, evidence):
        if not evidence.strip() or len(evidence) > 2048:
            raise JournalError("Acknowledgement requires a result reference of at most 2048 characters.")
        with self.connection() as db:
            row = db.execute("SELECT owner, acknowledgement FROM requests WHERE id=?", (request_id,)).fetchone()
            if row is None or not row["owner"] or row["owner"] != owner:
                raise JournalError("Only the recorded claim owner can acknowledge a request.")
            if row["acknowledgement"] is not None and row["acknowledgement"] != evidence:
                raise JournalError("Preserve the existing acknowledgement.")
            if row["acknowledgement"] is None and db.execute(
                    "SELECT 1 FROM results WHERE request_id=?", (request_id,)).fetchone() is None:
                raise JournalError("Save the PR result before reporting and acknowledging it.")
            db.execute("UPDATE requests SET acknowledgement=? WHERE id=?", (evidence, request_id))

    def save_result(self, request_id, owner, result):
        fields = {"number", "state", "mergedAt", "mergeCommit", "headRefOid", "url"}
        if (not isinstance(result, dict) or set(result) != fields
                or type(result["number"]) is not int or result["number"] != self.pr
                or result["state"] not in ("OPEN", "CLOSED", "MERGED")
                or result["url"] != f"https://github.com/{self.repository}/pull/{self.pr}"
                or not isinstance(result["headRefOid"], str)
                or not re.fullmatch(r"[0-9a-f]{40}", result["headRefOid"])):
            raise JournalError("Expected the fixed PR's status fields from gh pr view.")
        if result["state"] == "MERGED":
            commit, merged_at = result["mergeCommit"], result["mergedAt"]
            if (not isinstance(commit, dict) or set(commit) != {"oid"}
                    or not isinstance(commit["oid"], str) or not re.fullmatch(r"[0-9a-f]{40}", commit["oid"])
                    or not isinstance(merged_at, str)
                    or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?Z", merged_at)):
                raise JournalError("Merged status requires a commit and UTC merge timestamp.")
            try:
                datetime.fromisoformat(merged_at.replace("Z", "+00:00"))
            except ValueError:
                raise JournalError("Invalid merge timestamp.") from None
        elif result["mergeCommit"] is not None or result["mergedAt"] is not None:
            raise JournalError("Unmerged status must not contain a merge commit or timestamp.")
        body = json.dumps(result, sort_keys=True, separators=(",", ":"))
        with self.connection() as db:
            row = db.execute("SELECT owner, acknowledgement FROM requests WHERE id=?", (request_id,)).fetchone()
            if row is None or not row["owner"] or row["owner"] != owner:
                raise JournalError("Only the recorded claim owner can save a result.")
            existing = db.execute("SELECT body FROM results WHERE request_id=?", (request_id,)).fetchone()
            if existing:
                if existing["body"] != body:
                    raise JournalError("Preserve the original result; do not replace it with a new check.")
            elif row["acknowledgement"] is not None:
                raise JournalError("Do not backfill an acknowledged request with a new result.")
            else:
                db.execute("INSERT INTO results(request_id,body) VALUES (?,?)", (request_id, body))

    def result(self, request_id):
        with self.connection() as db:
            row = db.execute("""SELECT requests.payload, requests.acknowledgement, results.body, results.saved_at
                                FROM requests LEFT JOIN results ON results.request_id=requests.id WHERE id=?""",
                             (request_id,)).fetchone()
        if row is None:
            return None
        return {"payload": json.loads(row["payload"]), "acknowledgement": row["acknowledgement"],
                "result": json.loads(row["body"]) if row["body"] else None, "savedAt": row["saved_at"]}


def make_server(address, origins, journal, sender):
    allowed_origins = {}
    for origin in origins:
        parsed = urlsplit(origin)
        if (parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.path or parsed.query
                or parsed.fragment or parsed.username or parsed.password or origin != f"{parsed.scheme}://{parsed.netloc}"
                or any(ord(c) <= 32 or ord(c) == 127 for c in origin)):
            raise ValueError("Origins must be exact HTTP or HTTPS origins, including non-default page ports.")
        allowed_origins.setdefault(parsed.netloc, set()).add(origin)
    if not allowed_origins:
        raise ValueError("At least one allowed page origin is required.")

    class Handler(BaseHTTPRequestHandler):
        def setup(self):
            super().setup()
            self.connection.settimeout(8)

        def log_message(self, *_args):
            pass

        def respond(self, status, data, content_type="application/json"):
            body = json.dumps(data).encode() if content_type == "application/json" else data
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
            self.end_headers()
            self.wfile.write(body)

        def boundary(self, post=False):
            hosts = self.headers.get_all("Host", [])
            if len(hosts) != 1 or hosts[0] not in allowed_origins:
                self.respond(403, {"error": "Unrecognized page host."})
                return False
            origins = self.headers.get_all("Origin", [])
            if post and (len(origins) != 1 or origins[0] not in allowed_origins[hosts[0]]):
                self.respond(403, {"error": "Same-origin page request required."})
                return False
            return True

        def do_GET(self):
            if not self.boundary():
                return
            if self.path in ("/", "/app.js"):
                name, content_type = ("index.html", "text/html; charset=utf-8") if self.path == "/" else ("app.js", "text/javascript; charset=utf-8")
                self.respond(200, (ASSETS / name).read_bytes(), content_type)
            elif self.path == "/scope":
                self.respond(200, {"repository": journal.repository, "pr": journal.pr})
            elif self.path.startswith("/requests/") and ID.fullmatch(self.path[len("/requests/"):]):
                try:
                    state = journal.status(self.path[len("/requests/"):])
                    self.respond(200 if state else 404, state or {"error": "Request not recorded."})
                except sqlite3.Error:
                    self.respond(503, {"error": "Cannot read the request journal."})
            else:
                self.respond(404, {"error": "Not found."})

        def do_POST(self):
            if not self.boundary(post=True):
                return
            if self.path != "/requests":
                self.respond(404, {"error": "Not found."})
                return
            try:
                sizes = self.headers.get_all("Content-Length", [])
                if (len(sizes) != 1 or not sizes[0].isdigit() or not 0 < int(sizes[0]) <= 256
                        or self.headers.get_all("Content-Type", []) != ["application/json"]
                        or self.headers.get("Transfer-Encoding") is not None):
                    raise ValueError()
                data = json.loads(self.rfile.read(int(sizes[0])))
                if not isinstance(data, dict) or set(data) != {"requestId"}:
                    raise ValueError()
                payload = journal.payload(data["requestId"])
            except (ValueError, TypeError, TransportError, OSError):
                self.respond(400, {"error": "Expected only a valid requestId in a small JSON object."})
                return
            try:
                if journal.record(payload["requestId"]):
                    try:
                        receipt = sender(payload)
                    except TransportError:
                        receipt = Receipt(payload["requestId"], "local_error")
                    journal.delivered(receipt)
                self.respond(200, journal.status(payload["requestId"]))
            except sqlite3.Error:
                self.respond(503, {"error": "Journal unavailable. Keep the request ID; delivery is unconfirmed."})

    return ThreadingHTTPServer(address, Handler)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--pr", type=int, required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    serve = commands.add_parser("serve")
    serve.add_argument("--bind", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8765)
    serve.add_argument("--origin", action="append", required=True)
    serve.add_argument("--url-file", type=Path, required=True)
    serve.add_argument("--secret-file", type=Path, required=True)
    commands.add_parser("pending")
    claim = commands.add_parser("claim")
    ack = commands.add_parser("ack")
    save = commands.add_parser("save-result", help="Read the bounded gh pr view JSON result from stdin.")
    read = commands.add_parser("result", help="Read the saved result without rerunning the check.")
    read.add_argument("--request-id", required=True)
    for command in (claim, ack, save):
        command.add_argument("--request-id", required=True)
        command.add_argument("--owner", required=True)
    ack.add_argument("--evidence", required=True)
    args = parser.parse_args()
    try:
        journal = Journal(args.journal, args.repository, args.pr)
        if args.command == "serve":
            url = args.url_file.read_text().strip()
            read_secret(args.secret_file)
            server = make_server((args.bind, args.port), args.origin, journal,
                                 lambda payload: send(url, args.secret_file, payload))
            try:
                print("Local button server started. Delivery acceptance is not task completion.", flush=True)
                server.serve_forever()
            finally:
                server.server_close()
        elif args.command == "pending":
            print(json.dumps(journal.pending()))
        elif args.command == "claim":
            print(json.dumps(journal.claim(args.request_id, args.owner)))
        elif args.command == "save-result":
            body = sys.stdin.read(4097)
            if len(body) > 4096:
                raise JournalError("PR status result exceeds 4096 characters.")
            journal.save_result(args.request_id, args.owner, json.loads(body))
            print(json.dumps({"saved": True}))
        elif args.command == "result":
            print(json.dumps(journal.result(args.request_id)))
        else:
            journal.acknowledge(args.request_id, args.owner, args.evidence)
            print(json.dumps({"acknowledged": True}))
        return 0
    except KeyboardInterrupt:
        return 0
    except (JournalError, TransportError) as exc:
        print(str(exc), file=sys.stderr)
    except (OSError, ValueError, RecursionError, sqlite3.Error):
        print("Local UI operation failed. Preserve the journal and reconcile pending requests.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
