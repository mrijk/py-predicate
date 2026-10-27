from enum import Enum, IntFlag

import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import generate_true, is_instance_p


class Color(Enum):
    RED = 1
    GREEN = 2


class Option(IntFlag):
    A = 1
    B = 2


class NoMembers(Enum):
    pass


def test_generate_enum():
    predicate = is_instance_p(Color)

    assert_generated_true(predicate)
    assert set(take(100, generate_true(predicate))) == {Color.RED, Color.GREEN}


def test_generate_flag_combinations():
    predicate = is_instance_p(Option)

    assert_generated_true(predicate)
    assert set(take(200, generate_true(predicate))) == {Option(0), Option.A, Option.B, Option.A | Option.B}


def test_generate_enum_without_members():
    with pytest.raises(ValueError, match="NoMembers: it has no members"):
        take(1, generate_true(is_instance_p(NoMembers)))
