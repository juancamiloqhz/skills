import contextlib
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

import bot_ui_transport as bot


PAYLOAD = {"requestId": "fixture-1", "action": "check-pr", "repository": "example/project", "pr": 123}
KEY = "public-fixture-only-not-a-credential-é"


@contextlib.contextmanager
def receiver(status=202, outcome="accepted", response=None, drop=False):
    seen = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def do_POST(self):
            body = self.rfile.read(int(self.headers["Content-Length"]))
            seen.append((self.path, dict(self.headers), body))
            if drop:
                self.connection.shutdown(socket.SHUT_RDWR)
                self.connection.close()
                return
            self.send_response(status)
            if outcome is not None:
                self.send_header("x-t3-hook-outcome", outcome)
            self.send_header("Location", "/must-not-follow")
            self.end_headers()
            self.wfile.write(response if response is not None else b'{"deliveryId":"delivery:fixture-1"}')

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/fixture", seen
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.key = self.root / "signing-key"
        bot.write_secret(self.key, KEY)

    def test_private_key_preserves_exact_bytes_and_existing_file(self):
        self.assertEqual(bot.read_secret(self.key), KEY.encode())
        self.assertEqual(self.key.stat().st_mode & 0o777, 0o600)
        with self.assertRaises(bot.TransportError):
            bot.write_secret(self.key, "replacement")
        self.assertEqual(self.key.read_text(), KEY)

    def test_secret_references_and_insecure_files_are_rejected(self):
        with self.assertRaises(bot.TransportError):
            bot.write_secret(self.root / "ref", "secret-ref:" + "a" * 32)
        self.key.chmod(0o644)
        with self.assertRaises(bot.TransportError):
            bot.read_secret(self.key)
        self.key.chmod(0o600)
        link = self.root / "link"
        link.symlink_to(self.key)
        with self.assertRaises(bot.TransportError):
            bot.read_secret(link)
        self.key.write_text("secret-ref:" + "a" * 32)
        with self.assertRaises(bot.TransportError):
            bot.read_secret(self.key)
        self.key.write_text(KEY)
        self.assertEqual(bot.read_secret(self.key), KEY.encode())

    def test_provisioning_requires_private_directory(self):
        self.root.chmod(0o755)
        with self.assertRaises(bot.TransportError):
            bot.write_secret(self.root / "other", KEY)
        self.assertFalse((self.root / "other").exists())
        self.root.chmod(0o700)
        bot.write_secret(self.root / "other", KEY)
        self.assertEqual(bot.read_secret(self.root / "other"), KEY.encode())

    def test_cli_rejects_piped_secret_without_echoing_it(self):
        result = subprocess.run([sys.executable, str(Path(bot.__file__)), "init-secret", str(self.root / "cli")],
                                input=KEY, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("interactive terminal", result.stderr)
        self.assertNotIn(KEY, result.stdout + result.stderr)
        self.assertFalse((self.root / "cli").exists())

    def test_cli_hidden_terminal_provisioning(self):
        import pty
        import select
        import time
        master, slave = pty.openpty()
        child = subprocess.Popen([sys.executable, str(Path(bot.__file__)), "init-secret", str(self.root / "cli")],
                                 stdin=slave, stdout=slave, stderr=slave, start_new_session=True)
        os.close(slave)
        captured = b""
        try:
            for prompt in (b"Signing key (hidden): ", b"Repeat key (hidden): "):
                deadline = time.monotonic() + 5
                while prompt not in captured:
                    if time.monotonic() >= deadline:
                        self.fail("Hidden-input prompt did not arrive")
                    if select.select([master], [], [], 0.1)[0]:
                        captured += os.read(master, 4096)
                os.write(master, KEY.encode() + b"\n")
            self.assertEqual(child.wait(timeout=5), 0)
            while select.select([master], [], [], 0.1)[0]:
                try:
                    chunk = os.read(master, 4096)
                except OSError:
                    break
                if not chunk:
                    break
                captured += chunk
            self.assertNotIn(KEY.encode(), captured)
            self.assertIn(b"Saved private signing key", captured)
            self.assertEqual(bot.read_secret(self.root / "cli"), KEY.encode())
        finally:
            if child.poll() is None:
                child.kill()
                child.wait()
            os.close(master)

    def test_wire_bytes_signature_and_delivery_receipt(self):
        with receiver() as (url, seen):
            result = bot.send(url, self.key, PAYLOAD, allow_loopback_http=True)
        self.assertEqual(result, bot.Receipt("fixture-1", "accepted", 202, "delivery:fixture-1"))
        self.assertEqual(len(seen), 1)
        path, headers, body = seen[0]
        self.assertEqual(path, "/fixture")
        self.assertEqual(body, b'{"requestId":"fixture-1","action":"check-pr","repository":"example/project","pr":123}')
        self.assertEqual(headers["x-jstack-signature"], "sha256=" + hmac.new(KEY.encode(), body, hashlib.sha256).hexdigest())
        self.assertEqual(headers["Content-Type"], "application/json")
        self.assertNotIn(KEY, json.dumps(headers) + body.decode() + str(result))
        self.assertNotIn("Authorization", headers)

    def test_failure_receipts_do_not_retry_or_follow_redirects(self):
        for status, outcome in [(401, "rejected_signature"), (404, "not_found"), (409, "disabled"),
                                (410, "expired"), (413, "too_large"), (429, "rate_limited"),
                                (302, "unknown"), (500, "unknown"), (200, "unknown")]:
            with self.subTest(status=status), receiver(status) as (url, seen):
                self.assertEqual(bot.send(url, self.key, PAYLOAD, allow_loopback_http=True),
                                 bot.Receipt("fixture-1", outcome, status))
                self.assertEqual(len(seen), 1)

    def test_202_is_not_necessarily_accepted_or_complete(self):
        for outcome, body, expected in [
            ("prompt_too_long", b'{"deliveryId":"delivery:fixture-1"}', "rejected_prompt"),
            (None, b'{"deliveryId":"delivery:fixture-1"}', "unknown"),
            ("accepted", b'{}', "unknown"),
            ("accepted", b'not-json', "unknown"),
            ("accepted", b'[]', "unknown"),
            ("accepted", b"[" * 2000 + b"0" + b"]" * 2000, "unknown"),
            ("accepted", b'x' * (bot.MAX_BODY_BYTES + 1), "unknown"),
            ("duplicate", b'{"deliveryId":"delivery:fixture-1"}', "duplicate"),
        ]:
            with self.subTest(outcome=outcome, expected=expected), receiver(202, outcome, body) as (url, seen):
                result = bot.send(url, self.key, PAYLOAD, allow_loopback_http=True)
                self.assertEqual(result.outcome, expected)
                self.assertEqual(result.request_id, "fixture-1")
                self.assertEqual(len(seen), 1)

    def test_ambiguous_disconnect_is_unknown_and_does_not_resend(self):
        with receiver(drop=True) as (url, seen):
            result = bot.send(url, self.key, PAYLOAD, allow_loopback_http=True)
            self.assertEqual(result, bot.Receipt("fixture-1", "unknown"))
            self.assertEqual(len(seen), 1)

    def test_invalid_scope_or_url_never_reaches_receiver(self):
        with receiver() as (url, seen):
            for invalid in [{**PAYLOAD, "action": "merge"}, {**PAYLOAD, "command": "run anything"},
                            {**PAYLOAD, "pr": True}, {**PAYLOAD, "requestId": "bad\nvalue"}]:
                with self.assertRaises(bot.TransportError):
                    bot.send(url, self.key, invalid, allow_loopback_http=True)
            with self.assertRaises(bot.TransportError):
                bot.send(url, self.key, PAYLOAD)
            for invalid_url in [url + "?secret=value", url + "#fragment", "http://example.com/hook", "https://u:p@example.com/hook"]:
                with self.assertRaises(bot.TransportError):
                    bot.send(invalid_url, self.key, PAYLOAD, allow_loopback_http=True)
            self.assertEqual(seen, [])
            self.assertEqual(bot.send(url, self.key, PAYLOAD, allow_loopback_http=True).outcome, "accepted")
            self.assertEqual(len(seen), 1)

    @unittest.skipUnless(os.environ.get("JSTACK_TEST_T3_RUNTIME"), "Set JSTACK_TEST_T3_RUNTIME for the pinned installed verifier probe.")
    def test_actual_wire_request_against_pinned_t3_verifier(self):
        import base64
        with receiver() as (url, seen):
            self.assertEqual(bot.send(url, self.key, PAYLOAD, allow_loopback_http=True).outcome, "accepted")
        _, headers, body = seen[0]
        probe = Path(__file__).resolve().parents[2] / "research/jstack/evaluations/bot-ui-transport/probe_runtime.mjs"
        result = subprocess.run(["node", str(probe), os.environ["JSTACK_TEST_T3_RUNTIME"]], input=json.dumps({
            "bodyBase64": base64.b64encode(body).decode(), "signature": headers["x-jstack-signature"], "secret": KEY,
        }), capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["checks"], 6)
        self.assertEqual(json.loads(result.stdout)["result"], "pass")

    def test_cli_stops_if_hidden_input_is_unavailable(self):
        import warnings
        import io
        def no_echo(prompt):
            warnings.warn("echo unavailable", bot.getpass.GetPassWarning)
            return KEY
        with patch.object(sys, "argv", ["sender", "init-secret", str(self.root / "cli")]), \
             patch.object(sys, "stdin") as stdin, patch.object(bot.getpass, "getpass", side_effect=no_echo):
            stdin.isatty.return_value = True
            error = io.StringIO()
            with contextlib.redirect_stderr(error):
                self.assertEqual(bot.main(), 2)
            self.assertIn("Cannot hide terminal input", error.getvalue())
            self.assertNotIn(KEY, error.getvalue())
            self.assertFalse((self.root / "cli").exists())

    def test_cli_reports_only_safe_receipt_for_transport_failure(self):
        target = self.root / "url"
        target.write_text("https://example.invalid/private-endpoint")
        with patch.object(sys, "argv", ["sender", "send", "--url-file", str(target), "--secret-file", str(self.key)]), \
             patch.object(sys, "stdin") as stdin, patch.object(bot.http.client, "HTTPSConnection") as connection:
            stdin.read.return_value = json.dumps(PAYLOAD)
            connection.return_value.request.side_effect = TimeoutError("must not print endpoint or secret")
            import io
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(bot.main(), 1)
            self.assertEqual(json.loads(output.getvalue()), {
                "request_id": "fixture-1", "outcome": "unknown", "http_status": None, "delivery_id": None})
            self.assertEqual(connection.call_args.kwargs["timeout"], 8)


if __name__ == "__main__":
    unittest.main()
