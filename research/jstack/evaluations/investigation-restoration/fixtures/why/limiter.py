BATCH_LIMIT = 100

def allowed(records):
    return len(records) <= BATCH_LIMIT
