import pytest

from predicate import PredicateError, exception_p


@pytest.mark.skip
def test_exception_p():
    with pytest.raises(PredicateError):
        exception_p(13)
