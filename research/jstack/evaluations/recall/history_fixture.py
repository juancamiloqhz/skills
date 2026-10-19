"""Controlled history/forge responses for an agent authoring exercise, not a live adapter.

Usage: python3 history_fixture.py LOG list [CURSOR]
       python3 history_fixture.py LOG read ID [POSITION [OFFSET]]
       python3 history_fixture.py LOG state
       python3 history_fixture.py LOG shared
Every call is recorded in the assigned scratch log. Source data is immutable.
"""
import json
from pathlib import Path
import sys

log, operation, *args = sys.argv[1:]
with Path(log).open('a') as out:
    out.write(json.dumps([operation, *args]) + '\n')


def thread(identity, title, updated, workspace='/fixture/lease', **extra):
    return dict(threadId=identity, title=title, updatedAt=updated,
                projectId='lease-project', worktreePath=workspace, **extra)


if operation == 'list':
    pages = {
        '0': dict(currentThreadId='current', projectId='lease-project', nextCursor=41, threads=[
            thread('current', 'Lease work', '2026-10-19T12:00:00Z'),
            thread('noise', 'Lease evaluation test', '2026-10-19T11:00:00Z'),
            thread('other', 'Lease outage', '2026-10-19T10:00:00Z', '/fixture/other'),
            thread('old', 'Lease migration', '2026-10-01T10:00:00Z'),
        ]),
        '41': dict(currentThreadId='current', projectId='lease-project', nextCursor=None, threads=[
            thread('aaa-older', 'Lease ownership', '2026-10-16T12:00:00Z', settled=True),
            thread('zzz-newer', 'Friday follow-up', '2026-10-18T12:00:00Z', settled=False),
        ]),
    }
    result = pages[args[0] if args else '0']
elif operation == 'read':
    identity = args[0]
    position = args[1] if len(args) > 1 else '0'
    offset = args[2] if len(args) > 2 else None
    if identity == 'aaa-older':
        result = dict(hasMore=False, nextPosition=None, items=[dict(
            itemId='a1', createdAt='2026-10-16T12:00:00Z', textTruncated=False,
            text='Goal: prevent simultaneous lease holders. PR #11 merged; we thought the issue was fixed. Keep serialized owner updates. We struggled with reconnect retries. Do not widen this work to display styling.')])
    elif identity == 'zzz-newer' and position == '0':
        result = dict(hasMore=True, nextPosition=17, items=[dict(
            itemId='z1', createdAt='2026-10-18T11:30:00Z', textTruncated=False,
            text='Lease reconnect failures returned. PR #12 reverted #11. Follow-up branch fix/lease-reconnect has PR #13. Confirm current state before resuming.')])
    elif identity == 'zzz-newer' and position == '17':
        result = dict(hasMore=False, nextPosition=None, items=[dict(
            itemId='z2', createdAt='2026-10-18T12:00:00Z', textTruncated=offset is None,
            nextTextOffset=240 if offset is None else None,
            text=('Agent claimed verification passed, but the tool record continues...' if offset is None else
                  'Actual tool result: lease_check exited 2, missing verifier. No successful verification occurred. User correction: retain the failing reconnect example before changing the retry logic.'))])
    else:
        result = dict(error='Out-of-scope or nonexistent fixture chat')
elif operation == 'state':
    result = dict(observedAt='2026-10-19T12:00:00Z', repository='/fixture/lease',
                  prs={'11': {'state': 'MERGED', 'revertedBy': 12}, '12': {'state': 'MERGED'},
                       '13': {'state': 'OPEN', 'head': 'fix/lease-reconnect', 'checks': 'not run'}},
                  branch='fix/lease-reconnect', worktree='clean', ticket={'LEASE-8': 'open'})
elif operation == 'shared':
    result = dict(kind='supplied completed investigator findings; not live helper execution', sources={
        'source control': 'PR #12 reverted #11 after reconnect failures. PR #13 remains open.',
        'issue tracker': 'LEASE-8: users still report duplicate owners after reconnect.',
        'long-form documents': 'searched authorized lease docs; no results',
        'real-time team chat': 'unavailable MCP',
        'infrastructure observability': 'unavailable MCP',
        'error tracking': 'unavailable MCP',
        'product analytics warehouse': 'outside authorized fixture scope'})
else:
    raise SystemExit('Unknown operation')
print(json.dumps(result))
