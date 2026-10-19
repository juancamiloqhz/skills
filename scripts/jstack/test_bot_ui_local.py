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

PACKAGE_SCRIPTS = Path(__file__).resolve().parents[2] / "skills/jstack/jstack-make-bot-ui/scripts"
sys.path.insert(0, str(PACKAGE_SCRIPTS))

from bot_ui_local import Journal, JournalError, make_server
from bot_ui_transport import Receipt, TransportError, send, write_secret
from test_bot_ui_transport import receiver


RESULT = {"number": 123, "state": "MERGED", "mergedAt": "2026-10-19T21:03:41Z",
          "mergeCommit": {"oid": "a" * 40}, "headRefOid": "b" * 40,
          "url": "https://github.com/example/fixture/pull/123"}


@contextmanager
def running(journal, sender, origins=None):
    server = make_server(("127.0.0.1", 0), origins or ["http://fixture.local"], journal, sender)
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

    def test_proxy_origin_is_explicit_and_matches_the_request_host(self):
        calls = []
        def sender(payload):
            calls.append(payload)
            return Receipt(payload['requestId'], 'accepted', 202, 'delivery:fixture')
        with running(self.journal, sender, ['https://fixture.local', 'https://other.local']) as address:
            for fields in ({'Origin':'http://fixture.local'}, {'Origin':'https://other.local'},
                           {'Origin':'https://fixture.local:443'},
                           {'Origin':'http://fixture.local', 'X-Forwarded-Proto':'https'},
                           {'Host':'127.0.0.1', 'Origin':'https://fixture.local', 'X-Forwarded-Host':'fixture.local'}):
                self.assertEqual(request(address, headers=fields)[0], 403)
            self.assertEqual(calls, [])
            self.assertEqual(request(address, headers={'Origin':'https://fixture.local'})[0], 200)
            self.assertEqual(len(calls), 1)
        with running(self.journal, sender) as address:
            self.assertEqual(request(address, headers={'Origin':'https://fixture.local'})[0], 403)

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
        restarted.save_result("click-1", owner, RESULT)
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

    def test_saved_result_survives_lost_conversation_and_is_immutable(self):
        self.journal.record("click-1")
        self.journal.claim("click-1", "wake-1")
        with self.assertRaises(JournalError):
            self.journal.acknowledge("click-1", "wake-1", "thread:fixture;request:click-1")
        self.journal.save_result("click-1", "wake-1", RESULT)
        before = self.journal.result("click-1")
        restarted = Journal(self.journal.path, "example/fixture", 123)
        self.assertEqual(restarted.status("click-1")["processing"], "result_saved")
        self.assertEqual(restarted.result("click-1"), before)
        self.assertIsNone(before["acknowledgement"])
        self.assertFalse(restarted.claim("click-1", "replacement")["granted"])
        restarted.save_result("click-1", "wake-1", RESULT)
        self.assertEqual(restarted.result("click-1")["savedAt"], before["savedAt"])
        restarted.acknowledge("click-1", "wake-1", "thread:fixture;request:click-1")
        # The referenced conversation result is absent; the saved observation remains readable.
        recovered = Journal(self.journal.path, "example/fixture", 123)
        self.assertEqual(recovered.result("click-1")["result"], RESULT)
        self.assertEqual(recovered.result("click-1")["payload"], recovered.payload("click-1"))
        for owner, result in [("replacement", RESULT), ("wake-1", {**RESULT, "headRefOid": "c" * 40})]:
            with self.assertRaises(JournalError):
                recovered.save_result("click-1", owner, result)
        with running(recovered, lambda _: self.fail("recovery must not resend")) as address:
            state = json.loads(request(address)[2])
            self.assertEqual(state["processing"], "completed")
            self.assertNotIn("result", state)
        self.assertEqual(recovered.result("click-1")["result"], RESULT)

    def test_result_requires_owner_and_fixed_pr_status(self):
        self.journal.record("click-1")
        with self.assertRaises(JournalError):
            self.journal.save_result("click-1", None, RESULT)
        self.journal.claim("click-1", "wake-1")
        invalid = [None, [], {**RESULT, "number": True}, {**RESULT, "number": 124},
                   {**RESULT, "url": "https://github.com/other/repo/pull/123"},
                   {**RESULT, "state": "READY"}, {**RESULT, "token": "not-allowed"},
                   {**RESULT, "headRefOid": "bad"}, {**RESULT, "mergeCommit": None},
                   {**RESULT, "mergedAt": "invalidZ"}, {**RESULT, "mergedAt": "2026-10-19Z"},
                   {**RESULT, "mergedAt": "2026-02-30T10:00:00Z"}, {**RESULT, "state": "OPEN"}]
        for result in invalid:
            with self.subTest(result=result), self.assertRaises(JournalError):
                self.journal.save_result("click-1", "wake-1", result)
        self.assertIsNone(self.journal.result("click-1")["result"])
        self.assertIsNone(self.journal.result("unknown"))
        for state in ("OPEN", "CLOSED"):
            self.journal.record(state)
            self.journal.claim(state, "wake-1")
            self.journal.save_result(state, "wake-1", {**RESULT, "state": state, "mergedAt": None, "mergeCommit": None})
            self.assertEqual(self.journal.result(state)["result"]["state"], state)

    def test_old_acknowledgements_are_preserved_without_fabricating_results(self):
        self.journal.record("old")
        self.journal.claim("old", "original")
        with self.journal.connection() as db:
            db.execute("UPDATE requests SET acknowledgement='old-reference' WHERE id='old'")
            db.execute("DROP TABLE results")
        upgraded = Journal(self.journal.path, "example/fixture", 123)
        self.assertEqual(upgraded.status("old")["processing"], "acknowledged_without_result")
        self.assertEqual(upgraded.result("old")["acknowledgement"], "old-reference")
        self.assertIsNone(upgraded.result("old")["result"])
        self.assertEqual(upgraded.pending(), [])
        self.assertFalse(upgraded.claim("old", "new")["granted"])
        upgraded.acknowledge("old", "original", "old-reference")
        with self.assertRaises(JournalError):
            upgraded.save_result("old", "original", RESULT)
        with running(upgraded, lambda _: self.fail("legacy requests must not resend")) as address:
            self.assertEqual(json.loads(request(address, data={"requestId": "old"})[2])["processing"],
                             "acknowledged_without_result")

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
        base = [sys.executable, "-B", str(PACKAGE_SCRIPTS / "bot_ui_local.py"),
                "--journal", str(self.journal.path), "--repository", "example/fixture", "--pr", "123"]
        def run(*args):
            return subprocess.run(base + list(args), capture_output=True, text=True, check=True)
        self.assertEqual(len(json.loads(run("pending").stdout)), 1)
        claim = ("claim", "--request-id", "cli-1", "--owner", "wake-1")
        self.assertTrue(json.loads(run(*claim).stdout)["granted"])
        self.assertFalse(json.loads(run(*claim).stdout)["granted"])
        result_args = ["save-result", "--request-id", "cli-1", "--owner", "wake-1"]
        too_large = subprocess.run(base + result_args, input=" " * 4097, capture_output=True, text=True)
        self.assertEqual(too_large.returncode, 2)
        too_deep = subprocess.run(base + result_args, input="[" * 1500 + "0" + "]" * 1500,
                                  capture_output=True, text=True)
        self.assertEqual(too_deep.returncode, 2)
        self.assertNotIn("Traceback", too_deep.stderr)
        saved = subprocess.run(base + result_args, input=json.dumps(RESULT), capture_output=True, text=True, check=True)
        self.assertTrue(json.loads(saved.stdout)["saved"])
        self.assertEqual(json.loads(run("result", "--request-id", "cli-1").stdout)["result"], RESULT)
        run("ack", "--request-id", "cli-1", "--owner", "wake-1", "--evidence", "conversation-result")
        self.assertEqual(json.loads(run("pending").stdout), [])


if __name__ == "__main__":
    unittest.main()
