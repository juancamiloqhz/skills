from queueing import enqueue

def submit(account, payload, queue):
    if account.get('disabled'):
        raise PermissionError('account disabled')
    normalized = payload.strip()
    if not normalized:
        raise ValueError('empty payload')
    return enqueue(queue, account['id'], normalized)
