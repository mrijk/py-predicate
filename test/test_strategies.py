import pytest
from hypothesis import given, settings

from predicate import all_p, any_p, eq_p, fn_p, ge_p, gt_p, is_even_p, is_int_p, is_str_p, le_p, lt_p
from predicate.strategies import from_predicate

predicates = [
    eq_p(5),
    ge_p(0),
    gt_p(0),
    le_p(0),
    lt_p(0),
    ge_p(0) & lt_p(100),
    gt_p(0) & le_p(100) & ge_p(10),
    ge_p(0.5) & lt_p(1.5),
    gt_p(0.0) & lt_p(1.0),
    lt_p(0) | gt_p(100),
    ge_p(0) & is_even_p,
    ge_p("b"),
    is_int_p,
    is_int_p | is_str_p,
    is_int_p & ge_p(0),
    all_p(is_int_p),
    all_p(ge_p(0) & lt_p(10)),
    all_p(all_p(is_str_p)),
    any_p(ge_p(0)),
    any_p(is_int_p),
    ~ge_p(0),
    ~eq_p(5),
    ~is_int_p,
    ~~ge_p(0),
    ~(ge_p(0) & lt_p(10)),
    ~(lt_p(0) | gt_p(100)),
    ge_p(0) & ~is_even_p,
    all_p(~eq_p(0)),
]


@pytest.mark.parametrize("predicate", predicates, ids=repr)
def test_from_predicate_satisfies_predicate(predicate):
    @settings(max_examples=50)
    @given(from_predicate(predicate))
    def check(x):
        assert predicate(x)

    check()


def test_from_predicate_merges_bounds():
    @given(from_predicate(ge_p(0) & lt_p(2)))
    def check(x):
        assert x in (0, 1)

    check()


def test_from_predicate_unsatisfiable_bounds():
    assert from_predicate(ge_p(10) & lt_p(5)).is_empty
    assert from_predicate(gt_p(3) & lt_p(4)).is_empty


def test_from_predicate_unknown_type():
    with pytest.raises(TypeError):
        from_predicate(fn_p(lambda x: x > 0))
