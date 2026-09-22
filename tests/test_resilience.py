from ayoris.resilience import RetryPolicy

def test_retry_policy(): RetryPolicy(3,.1).validate()
