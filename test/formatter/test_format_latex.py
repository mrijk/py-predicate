import pytest

from predicate import (
    all_p,
    always_p,
    any_p,
    eq_false_p,
    eq_p,
    eq_true_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
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
    to_latex,
    zero_p,
)
from predicate.implies_predicate import implies_p


@pytest.mark.parametrize(
    ["predicate", "expected"],
    [
        (always_p & never_p, "True \\wedge False"),
        (always_p | never_p, "True \\vee False"),
        (always_p ^ never_p, "True \\oplus False"),
        (~always_p, "\\neg True"),
        (all_p(ge_p(2)), "\\forall x \\in S, x \\ge 2"),
        (any_p(ge_p(2)), "\\exists x \\in S, x \\ge 2"),
        (eq_p(2), "x = 2"),
        (eq_false_p, "x = False"),
        (eq_true_p, "x = True"),
        (ge_p(2), "x \\ge 2"),
        (ge_le_p(0, 3), "0 \\le x \\le 3"),
        (ge_lt_p(0, 3), "0 \\le x \\lt 3"),
        (gt_p(2), "x \\gt 2"),
        (gt_le_p(0, 3), "0 \\lt x \\le 3"),
        (gt_lt_p(0, 3), "0 \\lt x \\lt 3"),
        (implies_p(ge_p(2)), "p \\implies x \\ge 2"),
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


def test_format_latex_unknown(unknown_p):
    with pytest.raises(ValueError):
        to_latex(unknown_p)
