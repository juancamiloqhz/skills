"""Synthetic Slack envelopes and fault-injecting adapters. No external I/O."""

from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, replace
import hashlib
import hmac
import json
import multiprocessing
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest

from benny_contracts import (Claim, Decision, Incomplete, Journal, NoWrite, Parent, Rejected,
                             Root, Scope, authenticate_and_normalize, compensate, triage_handoff, trusted_verdict)

SCOPE = Scope('TTEST', 'CTEST', 'ATEST')
NOW = 1700000000
SECRET = b'public-fixture-key-not-a-credential'
ROOT = Root('TTEST', 'CTEST', '1700000000.000001')
MARKERS = dict(bug='[benny:bug]', performance='[benny:performance]', other='[benny:other]')


def envelope(**event_changes):
    return dict(type='event_callback', team_id='TTEST', api_app_id='ATEST', event_id='EvTEST',
                event=dict(type='message', channel='CTEST', user='UREPORTER', ts=ROOT.ts,
                           text='Saving a draft loses its title', **event_changes))


def signed(body, timestamp=str(NOW)):
    raw = body if isinstance(body, bytes) else json.dumps(body).encode()
    signature = 'v0=' + hmac.new(SECRET, b'v0:' + timestamp.encode() + b':' + raw, hashlib.sha256).hexdigest()
    return raw, timestamp, signature


def race_receive_claim(path):
    journal = Journal(Path(path), SCOPE)
    report = journal.receive(*signed(envelope()), SECRET, now=NOW)
    return [journal.claim(report.root, stage) is not None for stage in ('triage', 'reproduce')]


class Slack:
    def __init__(self):
        self.parent = Parent(ROOT, 'https://slack.invalid/report/1')
        self.parent_reads = 0
        self.disappear_at = None
        self.inaccessible = False
        self.existing_verdict = False
        self.post_mode = 'ok'
        self.readback = True
        self.posts = []

    def read_parent(self, root):
        self.parent_reads += 1
        if self.inaccessible:
            raise PermissionError()
        return None if self.disappear_at == self.parent_reads else self.parent

    def has_verdict(self, root):
        return self.existing_verdict

    def reply(self, root, verdict):
        if self.post_mode == 'no-write':
            raise NoWrite('definitive rejection')
        self.posts.append(dict(root=asdict(root), verdict=verdict))
        if self.post_mode == 'lost':
            raise TimeoutError('response lost after posting')
        return dict(ts='1700000001.000001', thread_ts=root.ts, channel=root.channel)

    def verify_reply(self, root, receipt, verdict):
        return self.readback


class Tracker:
    def __init__(self):
        self.can_compensate = True
        self.issues = {}
        self.writes = []
        self.lose = None
        self.cancel_verified = True

    def find_source(self, permalink):
        return next((key for key, issue in self.issues.items() if permalink in issue['sources']), None)

    def create(self, permalink):
        self.writes.append('create')
        self.issues['NEW1'] = dict(sources=[permalink], state='open', owner=None, labels=['bug'], notes=[])
        if self.lose == 'create':
            raise TimeoutError('created but response lost')
        return 'NEW1'

    def add_recurrence(self, issue, permalink):
        self.writes.append('recurrence')
        self.issues[issue]['sources'].append(permalink)
        self.issues[issue]['notes'].append('Another report')
        if self.lose == 'recurrence':
            raise TimeoutError('updated but response lost')
        return dict(issue=issue, source=permalink)

    def cancel(self, issue):
        self.writes.append('cancel')
        self.issues[issue]['state'] = 'cancelled'
        if self.lose == 'cancel':
            raise TimeoutError('cancelled but response lost')
        return dict(issue=issue, state='cancelled')

    def is_cancelled(self, issue):
        return self.cancel_verified and self.issues[issue]['state'] == 'cancelled'


class IntakeTests(unittest.TestCase):
    def test_authenticated_report_keeps_string_coordinates_and_drops_untrusted_fields(self):
        body = envelope()
        body['event'].update(repository='attacker/repo', command='delete everything', url='https://invalid/')
        report = authenticate_and_normalize(*signed(body), SECRET, SCOPE, now=NOW)
        self.assertEqual(asdict(report), dict(event_id='EvTEST', root=asdict(ROOT), user='UREPORTER'))
        for fields in [dict(subtype='file_share', files=[{'id':'FTEST'}]), dict(thread_ts=ROOT.ts),
                       dict(message_ts=ROOT.ts)]:
            with self.subTest(fields=fields):
                self.assertEqual(authenticate_and_normalize(*signed(envelope(**fields)), SECRET,
                                                          SCOPE, now=NOW).root, ROOT)

    def test_authentication_rejects_altered_unsigned_stale_future_and_malformed(self):
        raw, ts, signature = signed(envelope())
        cases = [(raw+b' ', ts, signature), (raw, ts, 'v0='+'0'*64),
                 signed(envelope(), str(NOW-301)), signed(envelope(), str(NOW+301)),
                 (raw, '', signature), (raw, True, signature), (raw, ts, 'v1='+'0'*64)]
        for args in cases:
            with self.subTest(args=args[1:]), self.assertRaises(Rejected):
                authenticate_and_normalize(*args, SECRET, SCOPE, now=NOW)

    def test_scope_types_event_kinds_and_conflicting_coordinates_fail_closed(self):
        bodies = []
        for key, value in [('team_id','TOTHER'), ('api_app_id','AOTHER'), ('event_id', True),
                           ('type','url_verification'), ('event', []), ('event_id','')]:
            body = envelope(); body[key] = value; bodies.append(body)
        for key, values in {
            'channel':['COTHER', None], 'ts':[1700000000.000001, True, '', None],
            'user':['', None, False], 'thread_ts':['1699999999.000001', None, False],
            'message_ts':['1700000000.000002', True],
            'subtype':['bot_message', 'message_changed', 'message_deleted', 'message_replied', 'thread_broadcast'],
            'type':['reaction_added'], 'bot_id':['BTEST'], 'app_id':['ATEST'], 'hidden':[True],
        }.items():
            for value in values:
                body = envelope(); body['event'][key] = value; bodies.append(body)
        for body in bodies + [[], None, 1]:
            with self.subTest(body=body), self.assertRaises(Rejected):
                authenticate_and_normalize(*signed(body), SECRET, SCOPE, now=NOW)
        for raw in [b'{', b'\xff', b'{"type":"event_callback","type":"url_verification"}']:
            with self.subTest(raw=raw), self.assertRaises(Rejected):
                authenticate_and_normalize(*signed(raw), SECRET, SCOPE, now=NOW)


class JournalFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'requests.sqlite'
        self.journal = Journal(self.path, SCOPE)

    def accept(self, body=None):
        return self.journal.receive(*signed(body or envelope()), SECRET, now=NOW)

class JournalTests(JournalFixture):
    def test_invalid_intake_has_no_records_and_db_failure_never_accepts(self):
        body = envelope(); body['event']['ts'] = False
        with self.assertRaises(Rejected):
            self.accept(body)
        self.assertEqual(self.journal.evidence(ROOT), dict(stages=[], effects=[]))
        with self.journal.connect() as db:
            db.execute('DROP TABLE events')
        with self.assertRaises(sqlite3.OperationalError):
            self.accept()
        self.assertEqual(self.journal.evidence(ROOT)['stages'], [])

    def test_duplicate_events_and_root_aliases_share_two_independent_claims(self):
        self.accept(); self.accept()
        alias = envelope(); alias['event_id'] = 'EvSECOND'
        self.accept(alias)
        self.assertEqual(len(self.journal.evidence(ROOT)['stages']), 2)
        repro = self.journal.claim(ROOT, 'reproduce')
        triage = self.journal.claim(ROOT, 'triage')
        self.assertIsNotNone(repro)
        self.assertIsNotNone(triage)
        self.assertIsNone(self.journal.claim(ROOT, 'triage'))
        self.assertIsNone(self.journal.claim(ROOT, 'invalid'))
        changed = envelope(); changed['event']['ts'] = '1700000000.000002'
        with self.assertRaisesRegex(Rejected, 'different bytes'):
            self.accept(changed)
        changed = envelope(); changed['event_id'] = 'EvOTHER'; changed['event']['user'] = 'UOTHER'
        with self.assertRaisesRegex(Rejected, 'author changed'):
            self.accept(changed)

    def test_concurrent_process_delivery_and_claim_have_one_owner_per_stage(self):
        with ProcessPoolExecutor(max_workers=4, mp_context=multiprocessing.get_context('spawn')) as pool:
            results = list(pool.map(race_receive_claim, [str(self.path)] * 12))
        self.assertEqual([sum(row[i] for row in results) for i in (0,1)], [1,1])
        self.assertEqual(len(self.journal.evidence(ROOT)['stages']), 2)

    def test_restart_preserves_claim_and_pending_effect_never_replays(self):
        self.accept()
        claim = self.journal.claim(ROOT, 'triage')
        calls = []
        def lost():
            calls.append('external write')
            raise TimeoutError()
        with self.assertRaises(Incomplete):
            self.journal.effect(claim, 'verdict', dict(root=asdict(ROOT)), lost)
        reopened = Journal(self.path, SCOPE)
        self.assertIsNone(reopened.claim(ROOT, 'triage'))
        with self.assertRaisesRegex(Incomplete, 'already attempted'):
            reopened.effect(claim, 'verdict', dict(root=asdict(ROOT)), lost)
        with self.assertRaisesRegex(Incomplete, 'Unresolved'):
            reopened.finish(claim, 'delivered')
        self.assertEqual(calls, ['external write'])
        self.assertEqual(reopened.evidence(ROOT)['effects'][0][2], 'pending')
        with self.assertRaises(Rejected):
            Journal(self.path, replace(SCOPE, channel='COTHER'))
        with self.assertRaises(Incomplete):
            reopened.effect(replace(claim, owner='wrong'), 'another', {}, lambda: calls.append('wrong'))
        self.assertEqual(calls, ['external write'])

    def test_process_crash_after_effect_leaves_durable_intent_and_no_retry(self):
        self.accept()
        effect_file = self.path.parent / 'synthetic-effect.txt'
        script = """
import os, sys
from pathlib import Path
sys.path.insert(0, sys.argv[3])
from benny_contracts import Journal, Scope, Root
journal = Journal(Path(sys.argv[1]), Scope('TTEST', 'CTEST', 'ATEST'))
root = Root('TTEST', 'CTEST', '1700000000.000001')
claim = journal.claim(root, 'triage')
def crash():
    Path(sys.argv[2]).write_text('one synthetic effect')
    os._exit(17)
journal.effect(claim, 'verdict', {'root':root.key}, crash)
"""
        result = subprocess.run([sys.executable, '-B', '-c', script, str(self.path),
                                 str(effect_file), str(Path(__file__).parent)],
                                cwd=self.path.parent, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 17, result.stderr)
        reopened = Journal(self.path, SCOPE)
        self.assertIsNone(reopened.claim(ROOT, 'triage'))
        evidence = reopened.evidence(ROOT)
        self.assertEqual(evidence['effects'][0][2], 'pending')
        owner = next(row[1] for row in evidence['stages'] if row[0] == 'triage')
        with self.assertRaises(Incomplete):
            reopened.effect(Claim(ROOT, 'triage', owner), 'verdict', {},
                            lambda: effect_file.write_text('duplicated'))
        self.assertEqual(effect_file.read_text(), 'one synthetic effect')

    def test_saved_receipt_survives_restart_and_cannot_run_twice(self):
        self.accept(); claim = self.journal.claim(ROOT, 'triage')
        receipt = dict(ts='1700000001.000001')
        self.journal.effect(claim, 'verdict', {}, lambda: receipt)
        reopened = Journal(self.path, SCOPE)
        self.assertEqual(json.loads(reopened.evidence(ROOT)['effects'][0][3]), receipt)
        self.assertIsNone(reopened.claim(ROOT, 'triage'))
        self.assertEqual(reopened.finish(claim, 'delivered'), 'delivered')
        with self.assertRaises(Incomplete):
            reopened.effect(claim, 'another', {}, lambda: receipt)


class HandoffTests(JournalFixture):
    def setUp(self):
        super().setUp()
        self.accept()
        self.claim = self.journal.claim(ROOT, 'triage')
        self.slack, self.tracker = Slack(), Tracker()
        self.decision = Decision('bug', clearly_broken=True, live=True, fields_resolved=True)

    def run_handoff(self, decision=None):
        return triage_handoff(self.journal, self.claim, self.slack, self.tracker, decision or self.decision)

    def test_missing_deleted_wrong_root_or_operations_channel_produces_no_writes(self):
        for parent in [None, Parent(replace(ROOT, channel='COPS'), 'https://slack.invalid/ops'),
                       Parent(replace(ROOT, ts='1700000001.000001'), 'https://slack.invalid/reply'),
                       Parent(ROOT, '')]:
            self.slack.parent = parent
            with self.assertRaises(Incomplete):
                self.run_handoff()
            self.assertEqual(self.tracker.writes, [])
            self.assertEqual(self.slack.posts, [])
        self.assertEqual(self.journal.evidence(ROOT)['effects'], [])

    def test_inaccessible_parent_produces_no_writes(self):
        self.slack.inaccessible = True
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual((self.tracker.writes, self.slack.posts), ([], []))

    def test_other_classifications_and_unmet_creation_gates_never_create(self):
        for decision in [replace(self.decision, category='other'),
                         replace(self.decision, clearly_broken=False),
                         replace(self.decision, live=False),
                         replace(self.decision, fields_resolved=False)]:
            with self.subTest(decision=decision), tempfile.TemporaryDirectory() as directory:
                journal = Journal(Path(directory) / 'journal.sqlite', SCOPE)
                journal.receive(*signed(envelope()), SECRET, now=NOW)
                claim = journal.claim(ROOT, 'triage')
                self.assertEqual(triage_handoff(journal, claim, self.slack, self.tracker, decision), 'delivered')
                self.assertEqual(self.tracker.writes, [])

    def test_prior_verdict_suppresses_every_write(self):
        self.slack.existing_verdict = True
        self.assertEqual(self.run_handoff(), 'duplicate')
        self.assertEqual((self.tracker.writes,self.slack.posts), ([],[]))

    def test_compensation_rejects_preexisting_or_unrelated_issue_even_if_called_directly(self):
        self.existing()
        with self.assertRaises(Incomplete):
            compensate(self.journal, self.claim, self.tracker, 'EXISTING')
        self.journal.effect(self.claim, 'create', {}, lambda: 'NEW1')
        with self.assertRaises(Incomplete):
            compensate(self.journal, self.claim, self.tracker, 'EXISTING')
        self.assertEqual(self.tracker.writes, [])
        self.assertEqual(self.tracker.issues['EXISTING']['state'], 'closed')

    def test_new_bug_posts_once_with_immutable_root_and_receipts(self):
        self.assertEqual(self.run_handoff(), 'delivered')
        self.assertEqual(self.tracker.writes, ['create'])
        self.assertEqual(self.slack.posts, [dict(root=asdict(ROOT), verdict=dict(category='bug', issue='NEW1'))])
        self.assertEqual(self.slack.parent_reads, 3)
        self.assertIsNone(self.journal.claim(ROOT, 'triage'))
        self.assertEqual({row[2] for row in self.journal.evidence(ROOT)['effects']}, {'confirmed'})

    def test_unresolved_or_malformed_prepared_decision_is_not_a_creation_gate(self):
        for changes in [dict(clearly_broken='false'), dict(live=None), dict(fields_resolved=1),
                        dict(match='confident', issue=''), dict(match='possible', issue=None)]:
            with self.subTest(changes=changes), self.assertRaises(Rejected):
                replace(self.decision, **changes)
        self.assertEqual((self.tracker.writes, self.slack.posts), ([], []))

    def test_no_compensation_capability_means_no_create_or_post(self):
        self.tracker.can_compensate = False
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, [])
        self.assertEqual(self.slack.posts, [])

    def test_definite_post_failure_cancels_only_new_issue_and_verifies(self):
        self.slack.post_mode = 'no-write'
        self.assertEqual(self.run_handoff(), 'handoff-failed')
        self.assertEqual(self.tracker.writes, ['create', 'cancel'])
        self.assertEqual(self.tracker.issues['NEW1']['state'], 'cancelled')
        self.assertEqual(self.slack.posts, [])

    def test_parent_disappears_after_create_cancels_owned_issue_without_post(self):
        self.slack.disappear_at = 3
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create', 'cancel'])
        self.assertEqual(self.slack.posts, [])

    def test_lost_post_response_does_not_cancel_visible_issue_or_retry(self):
        self.slack.post_mode = 'lost'
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create'])
        self.assertEqual(len(self.slack.posts), 1)
        self.assertIsNone(Journal(self.path, SCOPE).claim(ROOT, 'triage'))
        self.assertIn(('verdict','pending'), [(row[0],row[2]) for row in self.journal.evidence(ROOT)['effects']])

    def test_lost_create_response_does_not_post_retry_or_cancel_unknown_issue(self):
        self.tracker.lose = 'create'
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create'])
        self.assertEqual(self.slack.posts, [])
        self.assertEqual(self.tracker.issues['NEW1']['state'], 'open')
        self.assertIsNone(Journal(self.path, SCOPE).claim(ROOT, 'triage'))

    def test_lost_compensation_response_stays_incomplete(self):
        self.slack.post_mode = 'no-write'; self.tracker.lose = 'cancel'
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create', 'cancel'])
        self.assertIn(('compensate','pending'), [(row[0],row[2]) for row in self.journal.evidence(ROOT)['effects']])

    def test_unverified_compensation_never_claims_completion(self):
        self.slack.post_mode = 'no-write'; self.tracker.cancel_verified = False
        with self.assertRaisesRegex(Incomplete, 'Compensation'):
            self.run_handoff()
        self.assertTrue(all(row[2] is None for row in self.journal.evidence(ROOT)['stages']))

    def test_unknown_post_readback_keeps_issue_and_claim_for_reconciliation(self):
        self.slack.readback = None
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create'])
        self.assertIsNone(Journal(self.path, SCOPE).claim(ROOT, 'triage'))

    def test_confirmed_absent_post_readback_compensates(self):
        self.slack.readback = False
        with self.assertRaises(Incomplete):
            self.run_handoff()
        self.assertEqual(self.tracker.writes, ['create', 'cancel'])

    def existing(self):
        self.tracker.issues['EXISTING'] = dict(sources=[], state='closed', owner='HUMAN',
                                             labels=['keep'], notes=[])
        return Decision('bug', match='confident', issue='EXISTING')

    def test_duplicate_adds_recurrence_and_preserves_unrelated_fields_even_on_post_failure(self):
        decision = self.existing(); self.slack.post_mode = 'no-write'
        self.assertEqual(self.run_handoff(decision), 'handoff-failed')
        self.assertEqual(self.tracker.writes, ['recurrence'])
        issue = self.tracker.issues['EXISTING']
        self.assertEqual((issue['state'],issue['owner'],issue['labels']), ('closed','HUMAN',['keep']))
        self.assertEqual(issue['sources'], ['https://slack.invalid/report/1'])

    def test_lost_recurrence_response_does_not_repeat_update_or_post(self):
        decision = self.existing(); self.tracker.lose = 'recurrence'
        with self.assertRaises(Incomplete):
            self.run_handoff(decision)
        self.assertEqual(self.tracker.writes, ['recurrence'])
        self.assertEqual(self.slack.posts, [])

    def test_possible_duplicate_posts_link_but_creates_nothing(self):
        decision = replace(self.existing(), match='possible')
        self.assertEqual(self.run_handoff(decision), 'delivered')
        self.assertEqual(self.tracker.writes, [])
        self.assertEqual(self.slack.posts[0]['verdict']['issue'], 'EXISTING')

    def test_existing_source_link_or_prior_verdict_suppresses_handoff(self):
        self.existing()
        self.tracker.issues['EXISTING']['sources'] = ['https://slack.invalid/report/1']
        self.assertEqual(self.run_handoff(), 'duplicate')
        self.assertEqual((self.tracker.writes,self.slack.posts), ([],[]))


class MarkerTests(unittest.TestCase):
    def test_trusted_bug_and_performance_require_exact_author_thread_and_one_marker(self):
        message = dict(workspace=ROOT.workspace, channel=ROOT.channel, thread_ts=ROOT.ts,
                       ts='1700000001.000001', user='UTRIAGE', text='Confirmed\n[benny:bug]')
        self.assertEqual(trusted_verdict(ROOT,[message],'UTRIAGE',MARKERS), 'bug')
        self.assertEqual(trusted_verdict(ROOT,[{**message,'text':'[benny:performance]'}],'UTRIAGE',MARKERS), 'performance')
        for changed in [dict(user='USPOOF'), dict(channel='COPS'), dict(workspace='TOTHER'),
                        dict(thread_ts='1700000000.000002'), dict(ts=ROOT.ts), dict(ts=None), dict(ts=False),
                        dict(text='[benny:other]'), dict(text='[benny:bug] [benny:other]'),
                        dict(text='[benny:bug] [benny:bug]')]:
            with self.subTest(changed=changed):
                self.assertIsNone(trusted_verdict(ROOT,[{**message,**changed}],'UTRIAGE',MARKERS))
        self.assertIsNone(trusted_verdict(ROOT,[], 'UTRIAGE',MARKERS))
        self.assertIsNone(trusted_verdict(ROOT,[message,message], 'UTRIAGE',MARKERS))


if __name__ == '__main__':
    unittest.main()
