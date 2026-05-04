from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import count_p, eq_p, ge_p, generate_false


def test_generate_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert_generated_false(predicate)


def test_generate_count_includes_non_matching_items():
    """Generated false iterables may include items that don't match the predicate."""
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(2))

    values = take(20, generate_false(predicate))

    for value in values:
        assert not predicate(value)


def test_generate_count_zero_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(3))

    assert_generated_false(predicate)
