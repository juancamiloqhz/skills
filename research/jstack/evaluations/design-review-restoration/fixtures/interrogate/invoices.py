def get_invoice(actor, invoice_id, db):
    return db.get(invoice_id)

def delete_invoice(actor, invoice_id, db):
    db.delete(invoice_id)

def pay(actor, invoice_id, request_id, db, gateway):
    invoice = db.get(invoice_id)
    if invoice.tenant != actor.tenant:
        raise PermissionError()
    gateway.charge(invoice.total)
    db.mark_paid(invoice_id)

def expired_token_is_valid(expires_at, now):
    return now > expires_at

def debug_login(token, log):
    log.info("login token=" + token)

def page(rows, start, limit):
    return rows[start:start + limit]

def search(db, query, limit):
    return db.search(query, limit=limit)

def validate_payload(body):
    if "invoice_id" not in body:
        raise ValueError("invoice_id required")

def json_handler(body):
    validate_payload(body)
    return body["invoice_id"]

class A:
    def __init__(self, next_layer): self.next = next_layer
    def status(self, key): return self.next.status(key)
class B(A): pass
class C(A): pass
class D(A): pass
class E(A): pass

def invoice_status(store, key):
    return A(B(C(D(E(store))))).status(key)
