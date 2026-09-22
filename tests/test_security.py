from ayoris.security import fingerprint_token, constant_time_match

def test_token_fingerprint_is_stable():
    assert fingerprint_token("secret") == fingerprint_token("secret")
    assert fingerprint_token("secret") != fingerprint_token("other")

def test_constant_time_match_contract():
    assert constant_time_match("abc","abc")
    assert not constant_time_match("abc","abd")
