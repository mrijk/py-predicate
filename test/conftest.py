from dataclasses import dataclass

import pytest

from predicate.named_predicate import NamedPredicate
from predicate.predicate import Predicate

# Couple of pre-defined predicates as fixtures.


@pytest.fixture
def p():
    return NamedPredicate(name="p")


@pytest.fixture
def q():
    return NamedPredicate(name="q")


@pytest.fixture
def r():
    return NamedPredicate(name="r")


@pytest.fixture
def s():
    return NamedPredicate(name="s")


@pytest.fixture
def unknown_p():
    @dataclass
    class UnknownPredicate[T](Predicate[T]):
        def __call__(self, *args, **kwargs) -> bool:
            return False

    return UnknownPredicate()
