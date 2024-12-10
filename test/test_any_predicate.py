from predicate import any_p, is_int_p
from predicate.explain import explain


def test_any():
    any_int = any_p(is_int_p)

    assert not any_int(())
    assert any_int((1, 2, 3))
    assert any_int([1, 2, 3])
    assert any_int([None, 2, 3])


def test_any_explain():
    predicate = any_p(is_int_p)

    expected = {"reason": "No item matches predicate is_int_p", "result": False}

    assert explain(predicate, {"one", "two", "three"}) == expected
