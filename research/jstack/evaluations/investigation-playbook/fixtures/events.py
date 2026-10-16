MAX_RECENT = 64


def accept_event(recent: dict, event: dict):
    event_id = event['id']
    if event_id in recent:
        return recent[event_id], False
    stored = dict(event)
    recent[event_id] = stored
    while len(recent) > MAX_RECENT:
        del recent[next(iter(recent))]
    return stored, True
