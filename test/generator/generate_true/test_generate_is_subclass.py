import abc

import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import generate_true, is_subclass_p
from predicate.predicate import Predicate


@pytest.mark.parametrize(
    "parameter",
    [
        int,
        (int, str),
        int | str,
        object,
    ],
)
def test_generate_is_subclass(parameter):
    predicate = is_subclass_p(parameter)
    assert_generated_true(predicate)


class _Concrete(Predicate):
    def __call__(self, x):
        return True


class _Abstract(abc.ABC):
    @abc.abstractmethod
    def method(self): ...


def test_generate_is_subclass_skips_abstract_classes():
    classes = take(1000, generate_true(is_subclass_p(Predicate)))

    assert Predicate not in classes
    assert _Concrete in classes


def test_generate_is_subclass_of_only_an_abstract_class_still_yields_it():
    assert take(3, generate_true(is_subclass_p(_Abstract))) == [_Abstract] * 3


def test_generate_is_subclass_of_empty_tuple():
    # Nothing is a subclass of no class: no values, instead of looping forever
    assert take(5, generate_true(is_subclass_p(()))) == []


def test_generate_is_subclass_of_type():
    # The metaclass `type` is its own class: a bare type.__subclasses__() call is unbound
    assert_generated_true(is_subclass_p(type))
