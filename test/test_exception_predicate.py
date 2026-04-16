import pytest

from predicate import exception_p
from predicate.exception_predicate import PredicateError


def test_exception_p():
    with pytest.raises(PredicateError):
        exception_p(13)
