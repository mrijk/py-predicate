import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import generate_true, in_p


def test_generate_in():
    predicate = in_p([2, 3, 4])

    assert_generated_true(predicate)


def test_generate_in_fail():
    class Contains13:
        def __contains__(self, item):
            return item == 13

    predicate = in_p(Contains13())

    with pytest.raises(ValueError, match="Can't generate true values for type Contains13"):
        take(5, generate_true(predicate))
