from dataclasses import dataclass

from predicate import explain
from predicate.property_predicate import property_p


def test_property_p():
    @dataclass
    class Foo:
        @property
        def bar(self) -> bool:
            return True

    predicate = property_p(Foo.bar)

    foo = Foo()

    assert predicate(foo)


def test_property_p_explain():
    @dataclass
    class Foo:
        @property
        def bar(self) -> bool:
            return False

    predicate = property_p(Foo.bar)

    foo = Foo()

    assert not predicate(foo)

    expected = {"reason": "tbd", "result": False}

    assert explain(predicate, foo) == expected
