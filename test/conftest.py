from dataclasses import dataclass

import pytest

from predicate.predicate import Predicate
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


@pytest.fixture
def unknown_p():
    @dataclass
    class UnknownPredicate[T](Predicate[T]):
        def __call__(self, *args, **kwargs) -> bool:
            return False

    return UnknownPredicate()
