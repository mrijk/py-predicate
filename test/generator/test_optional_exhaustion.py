from itertools import islice

import pytest

from predicate import always_false_p, eq_p, is_struct_p
from predicate.generator.generate_true import generate_true
from predicate.generator.helpers import sample_optional_fields


@pytest.fixture
def select_all_optional(monkeypatch):
    monkeypatch.setattr("predicate.generator.helpers.random.randint", lambda low, high: high)


def test_exhausted_optional_field_does_not_discard_other_fields(select_all_optional):
    optional = {"empty": always_false_p, "finite": eq_p(None)}
    generators = {"empty": iter(()), "finite": iter([None])}
    assert sample_optional_fields(optional, generators) == {"finite": None}
    assert sample_optional_fields(optional, generators) == {}


@pytest.mark.parametrize("required", [{}, {"name": eq_p("Ada")}])
def test_struct_generation_omits_impossible_optional_field(select_all_optional, required):
    predicate = is_struct_p(required=required, optional={"impossible": always_false_p})
    values = list(islice(generate_true(predicate), 5))
    assert len(values) == 5
    assert all(predicate(value) for value in values)
    assert all("impossible" not in value for value in values)
