#!/usr/bin/env python3
"""Server-side transport foundation for the proposed T3 bot UI; no scheduler setup."""

import argparse
from dataclasses import asdict, dataclass
import getpass
import hashlib
import hmac
import http.client
import ipaddress
import json
import os
from pathlib import Path
import re
import stat
import sys
import warnings
from urllib.parse import urlsplit


SIGNATURE_HEADER = "x-jstack-signature"
TIMEOUT_SECONDS = 8
MAX_BODY_BYTES = 65536


class TransportError(Exception):
    pass


def write_secret(path, value):
    """Create a private local copy of a user-provided key; never replace a file."""
    if (not value or not value.strip() or value.startswith("secret-ref:")
            or len(value.encode("utf-8")) > MAX_BODY_BYTES):
        raise TransportError("Provide a nonempty signing key of at most 64 KiB.")
    parent = path.parent.stat()
    if parent.st_uid != os.geteuid() or stat.S_IMODE(parent.st_mode) & 0o077:
        raise TransportError("The key directory must be owned by you with mode 0700.")
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except OSError:
        raise TransportError("Cannot create key file; preserve any existing file.") from None
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(value.encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
    except OSError:
        path.unlink(missing_ok=True)
        raise TransportError("Could not save signing key.") from None


def read_secret(path):
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, "rb") as stream:
            info = os.fstat(stream.fileno())
            if (not stat.S_ISREG(info.st_mode) or info.st_uid != os.geteuid()
                    or stat.S_IMODE(info.st_mode) & 0o077):
                raise TransportError("Key must be an owned, private regular file.")
            value = stream.read(MAX_BODY_BYTES + 1)
    except OSError:
        raise TransportError("Cannot read signing key file.") from None
    if (not value or not value.strip() or value.startswith(b"secret-ref:")
            or len(value) > MAX_BODY_BYTES):
        raise TransportError("Invalid signing key file.")
    try:
        value.decode("utf-8")
    except UnicodeDecodeError:
        raise TransportError("Signing key must be UTF-8 text.") from None
    return value


def encode_request(payload):
    if (not isinstance(payload, dict)
            or set(payload) != {"requestId", "action", "repository", "pr"}
            or not isinstance(payload["requestId"], str)
            or not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", payload["requestId"])
            or payload["action"] not in ("check-pr", "probe")
            or not isinstance(payload["repository"], str)
            or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", payload["repository"])
            or type(payload["pr"]) is not int or payload["pr"] < 1):
        raise TransportError("Expected requestId, action (check-pr or probe), repository and positive pr.")
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")
    if len(body) > MAX_BODY_BYTES:
        raise TransportError("Request exceeds 64 KiB.")
    return body


@dataclass(frozen=True)
class Receipt:
    request_id: str
    outcome: str
    http_status: int | None = None
    delivery_id: str | None = None


def classify_response(request_id, status, headers, body):
    outcome = headers.get("x-t3-hook-outcome")
    if status == 202:
        try:
            delivery = json.loads(body).get("deliveryId")
        except (ValueError, AttributeError, RecursionError):
            delivery = None
        if (outcome in ("accepted", "duplicate") and isinstance(delivery, str)
                and re.fullmatch(r"delivery:[A-Za-z0-9:_-]{1,160}", delivery)):
            return Receipt(request_id, outcome, status, delivery)
        if outcome == "prompt_too_long":
            return Receipt(request_id, "rejected_prompt", status)
        return Receipt(request_id, "unknown", status)
    outcomes = {401: "rejected_signature", 404: "not_found", 409: "disabled",
                410: "expired", 413: "too_large", 429: "rate_limited"}
    return Receipt(request_id, outcomes.get(status, "unknown"), status)


def send(url, secret_path, payload, *, allow_loopback_http=False):
    """One POST, no redirects/retries; an accepted receipt is never completion."""
    body = encode_request(payload)
    try:
        target = urlsplit(url)
        port = target.port
        fixture = (allow_loopback_http and target.scheme == "http"
                   and ipaddress.ip_address(target.hostname or "").is_loopback)
        if (target.scheme != "https" and not fixture) or not target.hostname:
            raise ValueError()
        if target.username or target.password or target.query or target.fragment:
            raise ValueError()
        if any(ord(c) <= 32 or ord(c) == 127 for c in url):
            raise ValueError()
    except ValueError:
        raise TransportError("Use the returned HTTPS webhook URL without credentials, query or fragment.") from None
    secret = read_secret(secret_path)
    signature = "sha256=" + hmac.new(secret, body, hashlib.sha256).hexdigest()
    connection_type = http.client.HTTPConnection if fixture else http.client.HTTPSConnection
    connection = connection_type(target.hostname, port, timeout=TIMEOUT_SECONDS)
    try:
        connection.request("POST", target.path or "/", body, {
            "Content-Type": "application/json", SIGNATURE_HEADER: signature,
        })
        response = connection.getresponse()
        response_body = response.read(MAX_BODY_BYTES + 1)
        if len(response_body) > MAX_BODY_BYTES:
            return Receipt(payload["requestId"], "unknown", response.status)
        return classify_response(payload["requestId"], response.status,
                                 {k.lower(): v for k, v in response.getheaders()}, response_body)
    except (OSError, http.client.HTTPException):
        return Receipt(payload["requestId"], "unknown")
    finally:
        connection.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init-secret", help="User runs locally in a private terminal; no key in arguments.")
    init.add_argument("path", type=Path)
    post = commands.add_parser("send", help="Send one read-only request from stdin; does not create a webhook.")
    post.add_argument("--url-file", type=Path, required=True)
    post.add_argument("--secret-file", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "init-secret":
            if not sys.stdin.isatty():
                raise TransportError("Run init-secret yourself in an interactive terminal.")
            with warnings.catch_warnings():
                warnings.simplefilter("error", getpass.GetPassWarning)
                value = getpass.getpass("Signing key (hidden): ")
                if value != getpass.getpass("Repeat key (hidden): "):
                    raise TransportError("Keys do not match; nothing saved.")
            write_secret(args.path, value)
            print("Saved private signing key. Enter the same value in T3's private secret card when requested.")
            return 0
        payload = json.loads(sys.stdin.read(MAX_BODY_BYTES + 1))
        receipt = send(args.url_file.read_text().strip(), args.secret_file, payload)
        print(json.dumps(asdict(receipt)))
        return 0 if receipt.outcome in ("accepted", "duplicate") else 1
    except getpass.GetPassWarning:
        print("Cannot hide terminal input; no key was collected.", file=sys.stderr)
    except TransportError as exc:
        print(str(exc), file=sys.stderr)
    except (OSError, ValueError, EOFError):
        print("Could not read valid request inputs; nothing is confirmed delivered.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
