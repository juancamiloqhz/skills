"""Behavior checks for the local button server and receiver recovery protocol."""

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import http.client
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

from bot_ui_local import Journal, JournalError, make_server
from bot_ui_transport import Receipt, TransportError, send, write_secret
from test_bot_ui_transport import receiver


@contextmanager
def running(journal, sender):
    server = make_server(("127.0.0.1", 0), ["http://fixture.local"], journal, sender)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server.server_address
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def request(address, method="POST", path="/requests", data=None, headers=None):
    connection = http.client.HTTPConnection(*address, timeout=10)
    body = json.dumps(data or {"requestId": "click-1"}) if method == "POST" else None
    fields = {"Host": "fixture.local", "Origin": "http://fixture.local", "Content-Type": "application/json"}
    fields.update(headers or {})
    connection.request(method, path, body, fields)
    response = connection.getresponse()
    result = response.status, dict(response.getheaders()), response.read()
    connection.close()
    return result


class LocalUITest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.journal = Journal(self.root / "requests.sqlite", "example/fixture", 123)

    def test_click_signs_fixed_payload_and_only_accepts_delivery(self):
        secret = self.root / "key"
        write_secret(secret, "public-local-ui-fixture-only")
        with receiver() as (url, seen):
            with running(self.journal, lambda payload: send(url, secret, payload, allow_loopback_http=True)) as address:
                code, _, body = request(address)
                state = json.loads(body)
                self.assertEqual(code, 200)
                self.assertEqual(state["processing"], "pending")
                self.assertEqual(state["delivery"]["outcome"], "accepted")
                request(address)
                self.assertEqual(len(seen), 1)
                self.assertEqual(json.loads(seen[0][2]), self.journal.payload("click-1"))
                for path in ("/", "/app.js", "/scope", "/requests/click-1"):
                    code, headers, body = request(address, "GET", path)
                    self.assertEqual(code, 200)
                    self.assertNotIn(b"public-local-ui-fixture-only", body)
                    self.assertNotIn(url.encode(), body)
                    self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
                self.assertEqual(request(address, "GET", "/../key")[0], 404)

    def test_scope_and_browser_boundary_reject_before_sending(self):
        calls = []
        with running(self.journal, lambda payload: calls.append(payload)) as address:
            for data in ({"requestId": "x", "repository": "other/repo"},
                         {"requestId": "x", "action": "merge"}, {"requestId": "x", "pr": 12},
                         {"requestId": "x", "url": "https://attacker"}, {"requestId": ["x"]},
                         {"requestId": "../escape"}, {"requestId": "x" * 300}):
                self.assertEqual(request(address, data=data)[0], 400)
            for headers in ({"Origin": "http://attacker"}, {"Origin": "null"},
                            {"Origin": ""}, {"Host": "attacker"}):
                self.assertEqual(request(address, headers=headers)[0], 403)
            for headers in ({"Content-Type": "text/plain"}, {"Transfer-Encoding": "chunked"}):
                self.assertEqual(request(address, headers=headers)[0], 400)
            self.assertEqual(request(address, "GET", headers={"Host": "attacker"})[0], 403)
        self.assertEqual(calls, [])
        self.assertEqual(self.journal.pending(), [])

    def test_simultaneous_duplicate_clicks_send_once(self):
        started, finish = threading.Event(), threading.Event()
        calls = []

        def sender(payload):
            calls.append(payload)
            started.set()
            if not finish.wait(5):
                raise AssertionError("test release missing")
            return Receipt(payload["requestId"], "accepted", 202, "delivery:fixture")

        with running(self.journal, sender) as address, ThreadPoolExecutor() as pool:
            first = pool.submit(request, address)
            try:
                self.assertTrue(started.wait(5))
                state = json.loads(request(address)[2])
                self.assertEqual(state["delivery"]["outcome"], "unknown")
            finally:
                finish.set()
            self.assertEqual(first.result()[0], 200)
        self.assertEqual(len(calls), 1)

    def test_disconnect_recovery_survives_restart_and_is_claimed_once(self):
        secret = self.root / "key"
        write_secret(secret, "public-local-ui-fixture-only")
        with receiver(drop=True) as (url, seen):
            with running(self.journal, lambda payload: send(url, secret, payload, allow_loopback_http=True)) as address:
                self.assertEqual(json.loads(request(address)[2])["delivery"]["outcome"], "unknown")
            self.assertEqual(len(seen), 1)
        restarted = Journal(self.journal.path, "example/fixture", 123)
        self.assertEqual(restarted.pending()[0]["payload"], self.journal.payload("click-1"))
        with ThreadPoolExecutor(max_workers=8) as pool:
            claims = list(pool.map(lambda owner: restarted.claim("click-1", owner), [f"wake-{i}" for i in range(8)]))
        self.assertEqual(sum(result["granted"] for result in claims), 1)
        owner = restarted.pending()[0]["owner"]
        self.assertFalse(restarted.claim("click-1", owner)["granted"])
        restarted.acknowledge("click-1", owner, "conversation-result-1")
        restarted.acknowledge("click-1", owner, "conversation-result-1")
        with self.assertRaises(JournalError):
            restarted.acknowledge("click-1", owner, "different-result")
        final = Journal(self.journal.path, "example/fixture", 123)
        self.assertEqual(final.pending(), [])
        self.assertEqual(final.status("click-1")["processing"], "completed")
        self.assertFalse(final.claim("click-1", "later-wake")["granted"])
        with running(final, lambda _: self.fail("must not resend after restart")) as address:
            self.assertEqual(json.loads(request(address)[2])["processing"], "completed")

    def test_crash_after_intent_or_claim_never_automatically_replays(self):
        self.journal.record("click-1")
        restarted = Journal(self.journal.path, "example/fixture", 123)
        with running(restarted, lambda _: self.fail("must reconcile instead of retry")) as address:
            self.assertEqual(json.loads(request(address)[2])["delivery"]["outcome"], "unknown")
        self.assertTrue(restarted.claim("click-1", "wake-1")["granted"])
        restarted = Journal(self.journal.path, "example/fixture", 123)
        self.assertFalse(restarted.claim("click-1", "recovery")["granted"])
        self.assertEqual(restarted.status("click-1")["processing"], "claimed")
        with self.assertRaises(JournalError):
            restarted.acknowledge("click-1", "recovery", "result")
        with self.assertRaises(JournalError):
            restarted.acknowledge("click-1", "wake-1", " ")

    def test_journal_failure_never_sends_without_persisted_intent(self):
        with running(self.journal, lambda _: self.fail("must not send")) as address:
            with patch.object(self.journal, "record", side_effect=sqlite3.OperationalError("fixture")):
                self.assertEqual(request(address)[0], 503)
        calls = []
        def sender(payload):
            calls.append(payload)
            return Receipt(payload["requestId"], "accepted", 202, "delivery:fixture")
        with running(self.journal, sender) as address:
            with patch.object(self.journal, "delivered", side_effect=sqlite3.OperationalError("fixture")):
                self.assertEqual(request(address)[0], 503)
            self.assertEqual(json.loads(request(address)[2])["delivery"]["outcome"], "unknown")
        self.assertEqual(len(calls), 1)

    def test_private_storage_and_fixed_journal_scope(self):
        self.assertEqual(self.journal.path.stat().st_mode & 0o777, 0o600)
        with self.assertRaises(JournalError):
            Journal(self.journal.path, "other/repository", 123)
        public = self.root / "public"
        public.mkdir(mode=0o755)
        with self.assertRaises(JournalError):
            Journal(public / "db", "example/fixture", 123)
        link = self.root / "link"
        link.symlink_to(self.journal.path)
        with self.assertRaises(OSError):
            Journal(link, "example/fixture", 123)
        self.journal.path.chmod(0o644)
        with self.assertRaises(JournalError):
            Journal(self.journal.path, "example/fixture", 123)

    def test_rejected_and_local_error_requests_remain_recoverable(self):
        for outcome in ("rejected_signature", "local_error"):
            def sender(payload):
                if outcome == "local_error":
                    raise TransportError("private path must not be exposed")
                return Receipt(payload["requestId"], outcome, 401)
            with running(self.journal, sender) as address:
                code, _, body = request(address, data={"requestId": outcome})
                self.assertEqual(code, 200)
                self.assertNotIn(b"private path", body)
                state = json.loads(body)
                self.assertEqual(state["delivery"]["outcome"], outcome)
                self.assertEqual(state["processing"], "pending")
        self.assertEqual(len(self.journal.pending()), 2)
        with self.assertRaises(JournalError):
            self.journal.acknowledge("local_error", None, "not claimed")

    def test_receiver_cli_drain_and_ack(self):
        self.journal.record("cli-1")
        base = [sys.executable, "-B", str(Path(__file__).with_name("bot_ui_local.py")),
                "--journal", str(self.journal.path), "--repository", "example/fixture", "--pr", "123"]
        def run(*args):
            return subprocess.run(base + list(args), capture_output=True, text=True, check=True)
        self.assertEqual(len(json.loads(run("pending").stdout)), 1)
        claim = ("claim", "--request-id", "cli-1", "--owner", "wake-1")
        self.assertTrue(json.loads(run(*claim).stdout)["granted"])
        self.assertFalse(json.loads(run(*claim).stdout)["granted"])
        run("ack", "--request-id", "cli-1", "--owner", "wake-1", "--evidence", "conversation-result")
        self.assertEqual(json.loads(run("pending").stdout), [])


if __name__ == "__main__":
    unittest.main()
