"""Offline Benny boundary contracts. No server, scheduler, or vendor client is supplied.

The intake/journal code is executable; the handoff driver exercises prepared decisions
against injected adapters. It does not implement the agent's classification or UI work.
"""

from contextlib import contextmanager
from dataclasses import asdict, dataclass
import hashlib
import hmac
import json
from pathlib import Path
import re
import sqlite3
import uuid


class Rejected(ValueError):
    pass


class Incomplete(RuntimeError):
    pass


class NoWrite(RuntimeError):
    """An adapter has definitive evidence that its attempted write did not happen."""


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise Rejected('Duplicate JSON key')
        value[key] = item
    return value


def required_string(value):
    if not isinstance(value, str) or not value or len(value) > 256:
        raise Rejected('Missing or invalid identity')
    return value


@dataclass(frozen=True)
class Scope:
    workspace: str
    channel: str
    app: str

    def __post_init__(self):
        for value in asdict(self).values():
            required_string(value)


@dataclass(frozen=True)
class Root:
    workspace: str
    channel: str
    ts: str

    @property
    def key(self):
        return encoded(asdict(self))


@dataclass(frozen=True)
class Report:
    event_id: str
    root: Root
    user: str


def authenticate_and_normalize(raw, timestamp, signature, secret, scope, *, now):
    """Validate raw Slack signing bytes before parsing; retain only fixed-scope identity."""
    if (not isinstance(raw, bytes) or len(raw) > 1_048_576 or not secret
            or not isinstance(timestamp, str) or not re.fullmatch(r'[0-9]{1,12}', timestamp)
            or abs(now - int(timestamp)) > 300
            or not isinstance(signature, str) or not re.fullmatch(r'v0=[0-9a-f]{64}', signature)):
        raise Rejected('Invalid authentication envelope')
    expected = 'v0=' + hmac.new(secret, b'v0:' + timestamp.encode() + b':' + raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise Rejected('Signature mismatch')
    try:
        body = json.loads(raw, object_pairs_hook=unique_object)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise Rejected('Invalid JSON') from error
    if not isinstance(body, dict) or body.get('type') != 'event_callback':
        raise Rejected('Not a report callback')
    event = body.get('event')
    if (body.get('team_id') != scope.workspace or body.get('api_app_id') != scope.app
            or not isinstance(event, dict) or event.get('channel') != scope.channel):
        raise Rejected('Wrong scope')
    if (event.get('type') != 'message' or event.get('subtype') not in (None, 'file_share')
            or any(key in event for key in ('bot_id', 'bot_profile', 'app_id'))
            or event.get('hidden', False) is not False):
        raise Rejected('Not a new human report')
    ts = event.get('ts')
    if not isinstance(ts, str) or not re.fullmatch(r'[0-9]+\.[0-9]+', ts):
        raise Rejected('Timestamp must remain a string')
    if 'message_ts' in event and event['message_ts'] != ts:
        raise Rejected('Conflicting timestamp alias')
    if event.get('thread_ts', '') not in ('', ts):
        raise Rejected('Reply cannot start a report')
    return Report(required_string(body.get('event_id')), Root(scope.workspace, scope.channel, ts),
                  required_string(event.get('user')))


@dataclass(frozen=True)
class Claim:
    root: Root
    stage: str
    owner: str


class Journal:
    """Durable, non-expiring claims. An interrupted owner requires reconciliation."""

    def __init__(self, path: Path, scope: Scope):
        self.path, self.scope = path, scope
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS scope(value TEXT PRIMARY KEY);
                CREATE TABLE IF NOT EXISTS reports(root TEXT PRIMARY KEY, user TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS events(id TEXT PRIMARY KEY, digest TEXT NOT NULL, root TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS stages(root TEXT, stage TEXT, owner TEXT, outcome TEXT,
                                                  PRIMARY KEY(root, stage));
                CREATE TABLE IF NOT EXISTS effects(root TEXT, stage TEXT, name TEXT, intent TEXT,
                                                   state TEXT, receipt TEXT, PRIMARY KEY(root, stage, name));
            ''')
            db.execute('BEGIN IMMEDIATE')
            existing = db.execute('SELECT value FROM scope').fetchone()
            if existing and existing[0] != encoded(asdict(scope)):
                raise Rejected('Journal belongs to another scope')
            if not existing:
                db.execute('INSERT INTO scope VALUES (?)', (encoded(asdict(scope)),))

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        try:
            with db:
                yield db
        finally:
            db.close()

    def receive(self, raw, timestamp, signature, secret, *, now):
        report = authenticate_and_normalize(raw, timestamp, signature, secret, self.scope, now=now)
        digest = hashlib.sha256(raw).hexdigest()
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            prior = db.execute('SELECT digest FROM events WHERE id=?', (report.event_id,)).fetchone()
            if prior and prior[0] != digest:
                raise Rejected('Event ID reused with different bytes')
            saved = db.execute('SELECT user FROM reports WHERE root=?', (report.root.key,)).fetchone()
            if saved and saved[0] != report.user:
                raise Rejected('Report author changed')
            db.execute('INSERT OR IGNORE INTO reports VALUES (?, ?)', (report.root.key, report.user))
            db.execute('INSERT OR IGNORE INTO events VALUES (?, ?, ?)', (report.event_id, digest, report.root.key))
            for stage in ('triage', 'reproduce'):
                db.execute('INSERT OR IGNORE INTO stages VALUES (?, ?, NULL, NULL)', (report.root.key, stage))
        return report  # Durable intake only; no dispatch or agent completion implied.

    def claim(self, root, stage):
        owner = uuid.uuid4().hex
        with self.connect() as db:
            changed = db.execute('UPDATE stages SET owner=? WHERE root=? AND stage=? AND owner IS NULL',
                                 (owner, root.key, stage)).rowcount
        return Claim(root, stage, owner) if changed == 1 else None

    def owned(self, db, claim):
        row = db.execute('SELECT owner, outcome FROM stages WHERE root=? AND stage=?',
                         (claim.root.key, claim.stage)).fetchone()
        if row != (claim.owner, None):
            raise Incomplete('Claim is not active for this owner')

    def effect(self, claim, name, intent, call):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            self.owned(db, claim)
            try:
                db.execute('INSERT INTO effects VALUES (?, ?, ?, ?, ?, NULL)',
                           (claim.root.key, claim.stage, name, encoded(intent), 'pending'))
            except sqlite3.IntegrityError as error:
                raise Incomplete('Effect already attempted; reconcile instead of retrying') from error
        try:
            receipt = call()
            state = 'confirmed'
        except NoWrite:
            receipt, state = None, 'not-written'
        except Exception as error:
            raise Incomplete('Write result unknown; retain claim and intent') from error
        # A crash or serialization/disk error here intentionally leaves an unresolved intent.
        with self.connect() as db:
            self.owned(db, claim)
            db.execute('UPDATE effects SET state=?, receipt=? WHERE root=? AND stage=? AND name=?',
                       (state, encoded(receipt), claim.root.key, claim.stage, name))
        if state == 'not-written':
            raise NoWrite(name)
        return receipt

    def confirmed_creation(self, claim):
        with self.connect() as db:
            self.owned(db, claim)
            row = db.execute("SELECT receipt FROM effects WHERE root=? AND stage=? AND name='create' AND state='confirmed'",
                             (claim.root.key, claim.stage)).fetchone()
        if not row:
            raise Incomplete('No confirmed creation owned by this run')
        return json.loads(row[0])

    def finish(self, claim, outcome):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            self.owned(db, claim)
            if db.execute("SELECT 1 FROM effects WHERE root=? AND stage=? AND state='pending'",
                          (claim.root.key, claim.stage)).fetchone():
                raise Incomplete('Unresolved write prevents completion')
            db.execute('UPDATE stages SET outcome=? WHERE root=? AND stage=?',
                       (outcome, claim.root.key, claim.stage))
        return outcome

    def evidence(self, root):
        with self.connect() as db:
            return dict(stages=db.execute('SELECT stage, owner, outcome FROM stages WHERE root=? ORDER BY stage',
                                          (root.key,)).fetchall(),
                        effects=db.execute('SELECT name, intent, state, receipt FROM effects WHERE root=? ORDER BY name',
                                           (root.key,)).fetchall())


@dataclass(frozen=True)
class Parent:
    root: Root
    permalink: str


@dataclass(frozen=True)
class Decision:
    category: str
    match: str = 'none'
    issue: str | None = None
    clearly_broken: bool = False
    live: bool = False
    fields_resolved: bool = False

    def __post_init__(self):
        if self.category not in ('bug', 'performance', 'other') or self.match not in ('none', 'possible', 'confident'):
            raise Rejected('Unsupported prepared decision')
        if any(type(value) is not bool for value in (self.clearly_broken, self.live, self.fields_resolved)):
            raise Rejected('Creation gates must be explicit booleans')
        if self.issue is not None:
            required_string(self.issue)
        if (self.match == 'none') != (self.issue is None):
            raise Rejected('Match must identify its existing issue')


def preflight(slack, root, permalink=None):
    try:
        parent = slack.read_parent(root)
    except Exception as error:
        raise Incomplete('Source parent could not be read') from error
    if (not isinstance(parent, Parent) or parent.root != root or not parent.permalink.startswith('https://')
            or (permalink is not None and parent.permalink != permalink)):
        raise Incomplete('Source parent is missing, inaccessible, or mismatched')
    return parent.permalink


def triage_handoff(journal, claim, slack, tracker, decision):
    """Exercise only the write boundary for an already-assessed, synthetic decision.

    Adapters must distinguish definitive NoWrite from timeouts/unknown outcomes and
    provide authoritative read-back. This driver supplies no classification or prose.
    """
    if claim.stage != 'triage':
        raise Rejected('Wrong stage')
    root = claim.root
    permalink = preflight(slack, root)
    if tracker.find_source(permalink) or slack.has_verdict(root):
        return journal.finish(claim, 'duplicate')
    issue, created = decision.issue, False
    if decision.category in ('bug', 'performance'):
        if decision.match == 'confident':
            preflight(slack, root, permalink)
            journal.effect(claim, 'recurrence', dict(issue=issue, source=permalink),
                           lambda: tracker.add_recurrence(issue, permalink))
        elif decision.match == 'none' and decision.clearly_broken and decision.live and decision.fields_resolved:
            if not tracker.can_compensate:
                raise Incomplete('Cannot create without compensation capability')
            preflight(slack, root, permalink)
            issue = journal.effect(claim, 'create', dict(source=permalink),
                                   lambda: required_string(tracker.create(permalink)))
            created = True
    # A preflight failure after creation is a confirmed absence of any attempted verdict.
    try:
        preflight(slack, root, permalink)
    except Incomplete:
        if created:
            compensate(journal, claim, tracker, issue)
        raise
    verdict = dict(category=decision.category, issue=issue)
    try:
        receipt = journal.effect(claim, 'verdict', dict(root=asdict(root), **verdict),
                                 lambda: slack.reply(root, verdict))
    except NoWrite:
        if created:
            compensate(journal, claim, tracker, issue)
        return journal.finish(claim, 'handoff-failed')
    # False means authoritative absence; None or an exception means unknown, never absence.
    visible = slack.verify_reply(root, receipt, verdict)
    if visible is not True:
        if visible is False and created:
            compensate(journal, claim, tracker, issue)
        raise Incomplete('Verdict read-back did not confirm delivery')
    return journal.finish(claim, 'delivered')


def compensate(journal, claim, tracker, issue):
    if journal.confirmed_creation(claim) != issue:
        raise Incomplete('Cannot compensate an issue this run did not create')
    journal.effect(claim, 'compensate', dict(issue=issue), lambda: tracker.cancel(issue))
    if tracker.is_cancelled(issue) is not True:
        raise Incomplete('Compensation could not be verified')


def trusted_verdict(root, messages, identity, markers):
    """Interpret observed replies; no polling, posting or reproduction is performed."""
    if (set(markers) != {'bug', 'performance', 'other'}
            or any(not isinstance(value, str) or not value for value in markers.values())
            or len(set(markers.values())) != 3):
        raise Rejected('Ambiguous configured markers')
    required_string(identity)
    found = []
    for message in messages:
        if not isinstance(message, dict):
            return None
        text = message.get('text', '')
        if not isinstance(text, str):
            return None
        matches = [kind for kind, marker in markers.items() for _ in range(text.count(marker))]
        if not matches:
            continue
        if (message.get('user') != identity or message.get('channel') != root.channel
                or message.get('workspace') != root.workspace or message.get('thread_ts') != root.ts
                or not isinstance(message.get('ts'), str)
                or not re.fullmatch(r'[0-9]+\.[0-9]+', message['ts'])
                or message['ts'] == root.ts or len(matches) != 1):
            return None
        found.extend(matches)
    return found[0] if len(found) == 1 and found[0] in ('bug', 'performance') else None
