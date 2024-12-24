from dataclasses import dataclass

import pytest

from predicate import explain
from predicate.property_predicate import property_p


@pytest.fixture
def create_foo():
    def _create_foo(bar_return):
        @dataclass
        class Foo:
            @property
            def bar(self) -> bool:
                return bar_return

        return Foo

    return _create_foo


def test_property_p(create_foo):
    klass = create_foo(True)

    predicate = property_p(klass.bar)

    foo = klass()

    assert predicate(foo)


def test_property_p_explain(create_foo):
    klass = create_foo(False)

    predicate = property_p(klass.bar)

    foo = klass()

    expected = {"reason": "Property in Object Foo returned False", "result": False}

    assert explain(predicate, foo) == expected


@pytest.mark.skip(reason="Property names were introduced in Python 3.13")
def test_property_p_explain_missing(create_foo):
    klass = create_foo(True)

    predicate = property_p(klass.bar)

    expected = {"reason": "Object int has no property bar", "result": False}

    assert explain(predicate, 1) == expected
