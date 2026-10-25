from typing import Annotated

import pytest
from annotated_types import Predicate
from pydantic import BaseModel, ValidationError

from predicate import ge_lt_p, is_str_p


class Person(BaseModel):
    name: Annotated[str, Predicate(is_str_p)]
    age: Annotated[int, Predicate(ge_lt_p(0, 150))]


def test_annotated_types_valid():
    person = Person(name="alice", age=30)

    assert person.age == 30


def test_annotated_types_invalid():
    with pytest.raises(ValidationError):
        Person(name="alice", age=200)
