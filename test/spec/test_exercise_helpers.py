from predicate.spec.exercise_helpers import annotation_to_predicate


def test_annotation_to_predicate_set():
    predicate = annotation_to_predicate(set[int])

    assert predicate({1, 2, 3}) is True
    assert predicate({"a", "b"}) is False
    assert predicate([1, 2, 3]) is False
