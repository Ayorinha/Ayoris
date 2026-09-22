"""Idempotency primitives for safe AI API retries."""
from dataclasses import dataclass

@dataclass(frozen=True)
class IdempotencyKey:
    value: str

def validate_key(key: IdempotencyKey) -> None:
    if not 8 <= len(key.value) <= 256:
        raise ValueError("idempotency key length must be between 8 and 256")
