import pytest

from predicate import is_even_p


@pytest.mark.skip
def test_is_even():
    assert is_even_p(0)
    assert not is_even_p(1)
