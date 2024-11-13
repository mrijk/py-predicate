import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_p,
    ge_p,
    gt_p,
    in_p,
    is_none_p,
    is_not_none_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
)
from predicate.predicate import is_empty_p


@pytest.mark.parametrize(
    ("predicate", "representation"),
    [
        (always_false_p, "always_false_p"),
        (always_true_p, "always_true_p"),
        (always_false_p & always_true_p, "always_false_p & always_true_p"),
        (always_false_p | always_true_p, "always_false_p | always_true_p"),
        (always_false_p ^ always_true_p, "always_false_p ^ always_true_p"),
        (~always_false_p, "~always_false_p"),
        (all_p(eq_p(2)), "all(eq_p(2))"),
        (any_p(eq_p(2)), "any(eq_p(2))"),
        (eq_p(2), "eq_p(2)"),
        (ge_p(2), "ge_p(2)"),
        (gt_p(2), "gt_p(2)"),
        (in_p(2, 3, 4), "in_p(2, 3, 4)"),
        (is_empty_p, "is_empty_p"),
        (is_none_p, "is_none_p"),
        (is_not_none_p, "is_not_none_p"),
        (le_p(2), "le_p(2)"),
        (lt_p(2), "lt_p(2)"),
        (ne_p(2), "ne_p(2)"),
        (not_in_p(2, 3, 4), "not_in_p(2, 3, 4)"),
    ],
)
def test_repr_standard(predicate, representation):
    assert repr(predicate) == representation


@pytest.mark.parametrize(
    ("predicate", "representation"),
    [(always_false_p & in_p(2, 3, 4) & not_in_p(3), "always_false_p & in_p(2, 3, 4) & not_in_p(3)")],
)
def test_repr_combined(predicate, representation):
    assert repr(predicate) == representation
