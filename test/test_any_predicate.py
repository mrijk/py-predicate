from predicate.standard_predicates import any_p, is_int_p


def test_any():
    any_int = any_p(is_int_p)

    assert any_int(()) is False
    assert any_int((1, 2, 3)) is True
    assert any_int([1, 2, 3]) is True
    assert any_int([None, 2, 3]) is True
