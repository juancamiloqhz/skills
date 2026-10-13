def run_one(queue, key, deliver):
    job = queue[key]
    job['attempts'] += 1
    try:
        deliver(job['payload'])
    except TimeoutError:
        return 'retry'
    del queue[key]
    return 'sent'
