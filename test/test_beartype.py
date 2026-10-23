from typing import Annotated

import pytest
from beartype import beartype
from beartype.roar import BeartypeCallHintParamViolation, BeartypeCallHintReturnViolation
from beartype.vale import Is

from predicate import ge_le_p, is_list_of_p, is_str_p

Percentage = Annotated[int, Is[ge_le_p(0, 100)]]


@beartype
def set_volume(level: Percentage) -> Percentage:
    return level


@beartype
def broken_volume(level: int) -> Percentage:
    return level


@beartype
def join(words: Annotated[list, Is[is_list_of_p(is_str_p)]]) -> str:
    return " ".join(words)


def test_beartype_param_valid():
    assert set_volume(50) == 50


def test_beartype_param_invalid():
    with pytest.raises(BeartypeCallHintParamViolation):
        set_volume(101)


def test_beartype_return_invalid():
    with pytest.raises(BeartypeCallHintReturnViolation):
        broken_volume(-1)


def test_beartype_nested_predicate():
    assert join(["a", "b"]) == "a b"

    with pytest.raises(BeartypeCallHintParamViolation):
        join(["a", 1])
