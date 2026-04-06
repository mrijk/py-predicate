from predicate import any_p, is_int_p
from predicate.explain import explain


def test_any_count():
    assert any_p(is_int_p).count == 1


def test_any():
    any_int = any_p(is_int_p)

    assert not any_int(())
    assert any_int((1, 2, 3))
    assert any_int([1, 2, 3])
    assert any_int([None, 2, 3])


def test_any_contains(p, q, r):
    any_int = any_p(is_int_p)

    assert is_int_p in any_int


def test_any_explain():
    predicate = any_p(is_int_p)

    result = explain(predicate, ["one", "two", "three"])

    assert result["result"] is False
    assert len(result["failures"]) == 3
    assert result["failures"][0] == {"index": 0, "value": "one", "reason": "one is not an instance of type int"}
