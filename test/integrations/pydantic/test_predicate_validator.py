from typing import Annotated

import pytest
from pydantic import BaseModel, TypeAdapter, ValidationError

from predicate import ge_p, lt_p
from predicate.integrations.pydantic import PredicateValidator


class Model(BaseModel):
    x: Annotated[int, PredicateValidator(ge_p(0) & lt_p(100))]


def test_valid():
    assert Model(x=5).x == 5


def test_inner_type_runs_first():
    with pytest.raises(ValidationError) as e:
        Model(x="abc")
    assert e.value.errors()[0]["type"] == "int_parsing"


def test_invalid():
    with pytest.raises(ValidationError) as e:
        Model(x=100)
    error = e.value.errors()[0]
    assert error["type"] == "predicate_failed"
    assert error["ctx"]["explanation"]
    assert "Predicate failed" in error["msg"]


def test_type_adapter():
    adapter = TypeAdapter(Annotated[int, PredicateValidator(ge_p(0))])
    assert adapter.validate_python(1) == 1
    with pytest.raises(ValidationError):
        adapter.validate_python(-1)
