import sys

from predicate.spec.exercise_helpers import annotation_to_predicate


def test_annotation_to_predicate_set():
    predicate = annotation_to_predicate(set[int])

    assert predicate({1, 2, 3}) is True
    assert predicate({"a", "b"}) is False
    assert predicate([1, 2, 3]) is False


def test_annotation_to_predicate_frozenset():
    predicate = annotation_to_predicate(frozenset[int])

    assert predicate(frozenset({1, 2, 3})) is True
    assert predicate(frozenset({"a", "b"})) is False
    assert predicate({1, 2, 3}) is False


if sys.version_info >= (3, 15):

    def test_annotation_to_predicate_frozendict():
        predicate = annotation_to_predicate(frozendict[str, int])  # noqa: F821

        assert predicate(frozendict({"a": 1})) is True  # noqa: F821
        assert predicate(frozendict({"a": "b"})) is False  # noqa: F821
        assert predicate({"a": 1}) is False
