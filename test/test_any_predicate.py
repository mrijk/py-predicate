import pytest

from predicate import any_p, is_int_p
from predicate.explain import explain


@pytest.mark.skip
def test_any_count():
    assert any_p(is_int_p).count == 1


@pytest.mark.skip
def test_any():
    any_int = any_p(is_int_p)

    assert not any_int(())
    assert any_int((1, 2, 3))
    assert any_int([1, 2, 3])
    assert any_int([None, 2, 3])


@pytest.mark.skip
def test_any_contains(p, q, r):
    any_int = any_p(is_int_p)

    assert is_int_p in any_int


@pytest.mark.skip
def test_any_explain():
    predicate = any_p(is_int_p)

    expected = {"reason": "No item matches predicate is_int_p", "result": False}

    assert explain(predicate, {"one", "two", "three"}) == expected
