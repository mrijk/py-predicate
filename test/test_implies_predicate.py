import pytest

from predicate import eq_p, explain, ge_p, is_int_p, is_str_p, pos_p, zero_p
from predicate.implies_predicate import implies_p


@pytest.mark.parametrize(
    "this, other",
    [
        (ge_p(2), eq_p(3)),
        (is_int_p, is_int_p),
        (is_int_p, is_str_p & is_int_p),
        (is_int_p, zero_p),
        (is_int_p, pos_p),
    ],
)
def test_implies_predicate_ok(this, other):
    predicate = implies_p(this)
    assert predicate(other)


@pytest.mark.parametrize(
    "this, other",
    [
        (ge_p(2), eq_p(1)),
        (is_int_p, is_str_p),
        (is_int_p, is_str_p | is_int_p),
    ],
)
def test_implies_predicate_fail(this, other):
    predicate = implies_p(this)
    assert not predicate(other)


def test_implies_p_explain():
    predicate = implies_p(ge_p(2))

    expected = {"reason": "eq_p(1) doesn't imply ge_p(2)", "result": False}
    assert explain(predicate, eq_p(1)) == expected
