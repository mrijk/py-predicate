import pytest

from predicate import always_false_p, eq_p, explain, ge_p, is_int_p, is_str_p, le_p, lt_p, ne_p, pos_p, zero_p
from predicate.implies import implies
from predicate.implies_predicate import implies_p


@pytest.mark.parametrize(
    "this, other",
    [
        (ge_p(2), eq_p(3)),
        (is_int_p, is_int_p),
        (is_int_p, is_str_p & is_int_p),
        (is_int_p, zero_p),
        (is_int_p, pos_p),
        (lt_p(2), le_p(1)),  # le(1) implies lt(2): 1 < 2
        (le_p(3), lt_p(2)),  # lt(2) implies le(3): 2 <= 3
        (ne_p(3), lt_p(2)),  # lt(2) implies ne(3): 2 <= 3
        (ge_p(2), always_false_p),  # always_false_p implies everything
    ],
)
@pytest.mark.skip
def test_implies_predicate_ok(this, other):
    predicate = implies_p(this)
    assert predicate(other)


@pytest.mark.parametrize(
    "this, other",
    [
        (ge_p(2), eq_p(1)),
        (is_int_p, is_str_p),
        (is_int_p, is_str_p | is_int_p),
        (ge_p(1) & le_p(5), ne_p(2)),  # default handler: implies(ne_p(2), AndPredicate)
    ],
)
@pytest.mark.skip
def test_implies_predicate_fail(this, other):
    predicate = implies_p(this)
    assert not predicate(other)


@pytest.mark.skip
def test_implies_p_explain():
    predicate = implies_p(ge_p(2))

    expected = {"reason": "eq_p(1) doesn't imply ge_p(2)", "result": False}
    assert explain(predicate, eq_p(1)) == expected


@pytest.mark.skip
def test_implies_always_false():
    # always_false_p implies everything
    assert implies(always_false_p, ge_p(2))


@pytest.mark.skip
def test_implies_p_p_explain():
    from predicate.implies import implies_p_p

    predicate = implies_p_p(ge_p(2), lt_p(2))
    expected = {"result": False, "reason": "ge_p(2) doesn't imply lt_p(2)"}
    assert explain(predicate, 5) == expected
