from ayoris.idempotency import IdempotencyKey,validate_key

def test_idempotency_key_validation(): validate_key(IdempotencyKey("request-12345"))
