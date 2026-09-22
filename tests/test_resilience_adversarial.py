import pytest
from ayoris.resilience import RetryPolicy
def test_retry_policy_has_safe_upper_bound():
    with pytest.raises(ValueError): RetryPolicy(attempts=11).validate()