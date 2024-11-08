import pytest

from predicate.standard_predicates import fn_p

# Couple of pre-defined predicates as fixtures.


@pytest.fixture
def p():
    return fn_p(lambda x: x > 2)


@pytest.fixture
def q():
    return fn_p(lambda x: x > 3)


@pytest.fixture
def r():
    return fn_p(lambda x: x > 4)


@pytest.fixture
def s():
    return fn_p(lambda x: x > 5)
