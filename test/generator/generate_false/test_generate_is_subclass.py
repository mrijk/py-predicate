import pytest
from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import generate_false, is_subclass_p


@pytest.mark.parametrize("parameter", [int, (int, str), int | str])
def test_generate_is_subclass(parameter):
    predicate = is_subclass_p(parameter)
    assert_generated_false(predicate)


def test_generate_is_subclass_none():
    predicate = is_subclass_p(object)

    values = take(5, generate_false(predicate))

    assert not values


def test_generate_false_is_subclass_of_type():
    # The metaclass `type` is its own class: a bare type.__subclasses__() call is unbound
    assert_generated_false(is_subclass_p(type))
