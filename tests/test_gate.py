import hashlib


def outcome(identity_match, statement_period_match, code_date_state, promised, source_ok=True):
    if not source_ok or not identity_match or not statement_period_match:
        return "UNRESOLVED"
    if code_date_state == "LATER" or promised:
        return "LATER_REVISION"
    if code_date_state == "WITHIN_PERIOD":
        return "ALIGNED"
    return "UNRESOLVED"


def test_fixture_hashes_are_sha256():
    assert len(hashlib.sha256(b"statement").hexdigest()) == 64


def test_temporal_outcome_rule():
    assert outcome(True, True, "LATER", True) == "LATER_REVISION"


def test_unresolved_wrong_identity():
    assert outcome(False, True, "LATER", True) == "UNRESOLVED"
