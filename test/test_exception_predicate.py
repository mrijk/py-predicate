import pytest

from predicate import PredicateError, exception_p


def test_exception_p():
    with pytest.raises(PredicateError):
        exception_p(13)
