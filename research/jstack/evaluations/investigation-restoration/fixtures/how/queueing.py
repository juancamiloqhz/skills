def enqueue(queue, owner, payload):
    key = (owner, payload)
    if key not in queue:
        queue[key] = {'attempts': 0, 'payload': payload}
    return key
