from dataclasses import dataclass

import pytest

from predicate import is_int_p
from predicate.named_predicate import NamedPredicate
from predicate.predicate import Predicate
from predicate.spec.instrument import instrument_function
from predicate.spec.spec import Spec

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


@pytest.fixture(autouse=True)
def instrument_buggy_function():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    instrument_function(max_int_with_bug, spec=spec)
