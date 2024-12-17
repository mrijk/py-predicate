import pytest

from predicate import (
    all_p,
    always_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    ge_p,
    gt_p,
    in_p,
    is_real_subset_p,
    is_subset_p,
    le_p,
    lt_p,
    ne_p,
    neg_p,
    never_p,
    pos_p,
    zero_p,
)
from predicate.formatter.format_latex import to_latex


@pytest.mark.parametrize(
    ["predicate", "expected"],
    [
        (always_p & never_p, "True \\wedge False"),
        (always_p | never_p, "True \\vee False"),
        (always_p ^ never_p, "True \\oplus False"),
        (~always_p, "\\neg True"),
        (all_p(ge_p(2)), "\\forall x \\in S, x \\ge 2"),
        (eq_p(2), "x = 2"),
        (eq_false_p, "x = False"),
        (eq_true_p, "x = True"),
        (ge_p(2), "x \\ge 2"),
        (gt_p(2), "x \\gt 2"),
        (in_p(2, 3, 4), "x \\in \\{2, 3, 4\\}"),
        (le_p(2), "x \\le 2"),
        (lt_p(2), "x \\lt 2"),
        (ne_p(2), "x \\neq 2"),
        (neg_p, "x \\lt 0"),
        (pos_p, "x \\gt 0"),
        (zero_p, "x = 0"),
        (is_real_subset_p({1, 2, 3}), "x \\subseteq \\{1, 2, 3\\}"),
        (is_subset_p({1, 2, 3}), "x \\subset \\{1, 2, 3\\}"),
    ],
)
def test_format_latex_one_level(predicate, expected):
    assert to_latex(predicate) == expected


@pytest.mark.parametrize(
    ["predicate", "expected"],
    [
        (always_p & never_p & always_p, "True \\wedge False \\wedge True"),
        (ne_p(2) & ne_p(3), "x \\neq 2 \\wedge x \\neq 3"),
    ],
)
def test_format_latex_two_levels(predicate, expected):
    assert to_latex(predicate) == expected
