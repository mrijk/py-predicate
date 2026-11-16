from typing import Annotated

import pytest
from pydantic import BaseModel, TypeAdapter

from predicate import all_p, any_p, eq_p, ge_p, gt_p, in_p, is_even_p, le_p, lt_p, regex_p
from predicate.integrations.pydantic import PredicateValidator, predicate_to_json_schema


@pytest.mark.parametrize(
    "predicate, expected",
    [
        (ge_p(1), {"minimum": 1}),
        (gt_p(1), {"exclusiveMinimum": 1}),
        (le_p(1), {"maximum": 1}),
        (lt_p(1), {"exclusiveMaximum": 1}),
        (eq_p(3), {"const": 3}),
        (in_p({1}), {"enum": [1]}),
        (ge_p(0) & lt_p(100), {"minimum": 0, "exclusiveMaximum": 100}),
        (ge_p(0) & ge_p(5), {"allOf": [{"minimum": 0}, {"minimum": 5}]}),
        (lt_p(0) | gt_p(10), {"anyOf": [{"exclusiveMaximum": 0}, {"exclusiveMinimum": 10}]}),
        (~eq_p(3), {"not": {"const": 3}}),
        (regex_p("a|b"), {"pattern": "^(?:a|b)"}),
        (all_p(ge_p(0)), {"items": {"minimum": 0}}),
        (any_p(ge_p(0)), {"contains": {"minimum": 0}}),
        (eq_p(object()), {}),
        (is_even_p, {}),
        (ge_p(0) & is_even_p, {"minimum": 0}),
        (ge_p(0) | is_even_p, {}),
        (~is_even_p, {}),
    ],
)
def test_predicate_to_json_schema(predicate, expected):
    assert predicate_to_json_schema(predicate) == expected


def test_type_adapter():
    schema = TypeAdapter(Annotated[int, PredicateValidator(ge_p(0) & lt_p(100))]).json_schema()
    assert schema == {"type": "integer", "minimum": 0, "exclusiveMaximum": 100}


def test_model():
    class Model(BaseModel):
        x: Annotated[int, PredicateValidator(ge_p(0))]

    assert Model.model_json_schema()["properties"]["x"] == {"type": "integer", "minimum": 0, "title": "X"}
