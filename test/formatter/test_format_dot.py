from predicate import always_false_p, always_true_p
from predicate.formatter.format_dot import to_dot
from predicate.predicate import FnPredicate
from predicate.standard_predicates import ne_p, all_p, any_p, ge_p, gt_p, le_p, lt_p, in_p, not_in_p, eq_p


def test_format_dot_false():
    predicate = always_false_p

    dot = to_dot(predicate, "test")

    assert dot


def test_format_dot_true():
    predicate = always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_and():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_or():
    predicate = always_true_p | always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_xor():
    predicate = always_true_p ^ always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_all():
    predicate = all_p(predicate=always_true_p)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_any():
    predicate = any_p(predicate=always_true_p)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_not():
    predicate = ~always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_dot_eq():
    predicate = eq_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_ge():
    predicate = ge_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_gt():
    predicate = gt_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_in():
    predicate = in_p(1, 2, 3)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_le():
    predicate = le_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_lt():
    predicate = lt_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_ne():
    predicate = ne_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_not_in():
    predicate = not_in_p(1, 2, 3)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_show_optimized():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate, show_optimized=True)

    assert dot


def test_format_dot_fn():
    predicate = FnPredicate(predicate_fn=lambda x: x)

    dot = to_dot(predicate)

    assert dot
