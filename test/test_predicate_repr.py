import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    comp_p,
    eq_p,
    ge_p,
    gt_p,
    in_p,
    is_empty_p,
    is_none_p,
    is_not_none_p,
    is_str_p,
    lazy_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    regex_p,
)
from predicate.named_predicate import NamedPredicate
from predicate.predicate import is_not_empty_p
from predicate.standard_predicates import (
    ge_le_p,
    ge_lt_p,
    gt_le_p,
    gt_lt_p,
    has_key_p,
    is_falsy_p,
    is_truthy_p,
    tee_p,
    this_p,
)


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
        (comp_p(lambda x: x, eq_p(2)), "comp_p(eq_p(2))"),
        (eq_p(2), "eq_p(2)"),
        (ge_p(2), "ge_p(2)"),
        (gt_p(2), "gt_p(2)"),
        (ge_le_p(2, 3), "ge_le_p(2, 3)"),
        (gt_le_p(2, 3), "gt_le_p(2, 3)"),
        (ge_lt_p(2, 3), "ge_lt_p(2, 3)"),
        (gt_lt_p(2, 3), "gt_lt_p(2, 3)"),
        (has_key_p("foo"), 'has_key_p("foo")'),
        (in_p(2, 3, 4), "in_p(2, 3, 4)"),
        (is_empty_p, "is_empty_p"),
        (is_not_empty_p, "is_not_empty_p"),
        (is_none_p, "is_none_p"),
        (is_not_none_p, "is_not_none_p"),
        (is_str_p, "is_str_p"),
        (is_falsy_p, "is_falsy_p"),
        (is_truthy_p, "is_truthy_p"),
        (lazy_p("ref"), 'lazy_p("ref")'),
        (le_p(2), "le_p(2)"),
        (lt_p(2), "lt_p(2)"),
        (ne_p(2), "ne_p(2)"),
        (not_in_p(2, 3, 4), "not_in_p(2, 3, 4)"),
        (regex_p("^foo.*bar$"), 'regex_p("^foo.*bar$")'),
        (tee_p(lambda x: None), "tee_p"),
        (this_p, "this_p"),
        (NamedPredicate(name="foo"), "foo"),
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
