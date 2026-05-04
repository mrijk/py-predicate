from more_itertools import take

from predicate import generate_true
from predicate.exception_predicate import exception_p


def test_generate_exception():
    values = take(5, generate_true(exception_p))

    assert not values
