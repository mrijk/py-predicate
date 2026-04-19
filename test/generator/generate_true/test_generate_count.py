from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import count_p, eq_p, ge_p, generate_true


def test_generate_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert_generated_true(predicate)


def test_generate_count_includes_non_matching_items():
    """Generated iterables should include items that don't match the predicate."""
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(2))

    values = take(20, generate_true(predicate))

    assert any(len(v) > 2 for v in values), "Expected some iterables with extra non-matching items"
    for value in values:
        assert predicate(value)


def test_generate_count_zero():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(0))

    assert_generated_true(predicate)
