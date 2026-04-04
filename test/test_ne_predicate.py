import pytest
from helpers import exercise_predicate

from predicate import ne_p
from predicate.explain import explain


@pytest.mark.parametrize("v, valid", [(2, 3), ("foo", "bar")])
@pytest.mark.skip
def test_ne_p(v, valid):
    predicate = ne_p(v)
    assert predicate(valid)
    assert not predicate(v)


@pytest.mark.skip
def test_eq_explain():
    predicate = ne_p("foo")

    expected = {"reason": "foo is equal to 'foo'", "result": False}
    assert explain(predicate, "foo") == expected


@pytest.mark.skip
def test_ne_exercise():
    exercise_predicate(ne_p)
