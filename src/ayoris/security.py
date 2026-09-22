from dataclasses import dataclass
from hashlib import sha256
import hmac

@dataclass(frozen=True)
class RequestIdentity:
    subject: str
    token_fingerprint: str

def fingerprint_token(token: str) -> str:
    if not token: raise ValueError("token is required")
    return sha256(token.encode("utf-8")).hexdigest()

def constant_time_match(provided: str, expected: str) -> bool:
    return bool(provided) and bool(expected) and hmac.compare_digest(provided, expected)
