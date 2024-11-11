import pytest

from predicate import always_false_p, always_true_p, eq_p, ge_p, gt_p, le_p, lt_p, ne_p


@pytest.mark.parametrize(
    ("predicate", "representation"),
    [
        (always_false_p, "always_false_p"),
        (always_true_p, "always_true_p"),
        (always_false_p & always_true_p, "always_false_p & always_true_p"),
        (always_false_p | always_true_p, "always_false_p | always_true_p"),
        (always_false_p ^ always_true_p, "always_false_p ^ always_true_p"),
        (~always_false_p, "~always_false_p"),
        (eq_p(2), "eq_p(2)"),
        (ge_p(2), "ge_p(2)"),
        (gt_p(2), "gt_p(2)"),
        (le_p(2), "le_p(2)"),
        (lt_p(2), "lt_p(2)"),
        (ne_p(2), "ne_p(2)"),
    ],
)
def test_repr_always_false_p(predicate, representation):
    assert repr(predicate) == representation
