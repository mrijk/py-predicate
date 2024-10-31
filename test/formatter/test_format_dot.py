from predicate import always_false_p, always_true_p
from predicate.formatter.format_dot import to_dot
from predicate.predicate import FnPredicate
from predicate.standard_predicates import ne_p


def test_format_dot_false():
    predicate = always_false_p

    dot = to_dot(predicate, "test")

    assert dot


def test_format_json_true():
    predicate = always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_json_and():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_json_or():
    predicate = always_true_p | always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_json_xor():
    predicate = always_true_p ^ always_false_p

    dot = to_dot(predicate)

    assert dot


def test_format_json_not():
    predicate = ~always_true_p

    dot = to_dot(predicate)

    assert dot


def test_format_json_ne():
    predicate = ne_p(13)

    dot = to_dot(predicate)

    assert dot


def test_format_dot_optimized():
    predicate = always_true_p & always_false_p

    dot = to_dot(predicate, show_optimized=True)

    assert dot


def test_format_json_unknown():
    predicate = FnPredicate(predicate_fn=lambda x: x)

    dot = to_dot(predicate)

    assert dot
