"""Small, dependency-free resilience primitives for API boundaries."""
from dataclasses import dataclass

@dataclass(frozen=True)
class RetryPolicy:
    attempts: int = 3
    backoff_seconds: float = 0.25

    def validate(self) -> None:
        if self.attempts < 1 or self.backoff_seconds < 0:
            raise ValueError("invalid retry policy")