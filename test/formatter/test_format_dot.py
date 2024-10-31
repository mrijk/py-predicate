from predicate import always_false_p
from predicate.formatter.format_dot import to_dot


def test_format_dot_false():
    predicate = always_false_p

    dot = to_dot(predicate, "test")

    assert dot
