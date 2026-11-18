from functools import partial
from itertools import islice

import pytest
import yaml

from predicate import eq_p, generate_false, generate_true, in_p, is_str_p, unique_by_p, unique_p
from predicate.explain import explain
from predicate.formatter.format_dot import to_dot
from predicate.formatter.format_json import to_json
from predicate.formatter.format_yaml import to_yaml
from predicate.formatter.from_json import from_json


@pytest.mark.parametrize(("values", "expected"), [([], True), ([1, 2, 3], True), ([1, 2, 1], False)])
def test_unique_values(values, expected):
    assert unique_p(iter(values)) is expected


def test_explain_stops_at_first_duplicate_in_a_one_shot_iterator():
    class OneShotIterator:
        def __init__(self):
            self.values = iter([1, 2, 1, 3])
            self.traversals = 0

        def __iter__(self):
            self.traversals += 1
            assert self.traversals == 1
            return self

        def __next__(self):
            return next(self.values)

    values = OneShotIterator()
    assert explain(unique_p, values) == {
        "result": False,
        "reason": "Duplicate key 1 at indices 0 and 2",
    }
    assert values.traversals == 1
    assert next(values) == 3


def test_explain_reports_success():
    assert explain(unique_p, iter([1, 2, 3])) == {"result": True}


def test_custom_key_compares_transformed_values():
    by_name = unique_by_p(str.casefold)
    assert by_name(["one", "two"])
    assert not by_name(["one", "ONE"])
    assert by_name.explain_failure(["one", "two", "ONE"]) == {"reason": "Duplicate key 'one' at indices 0 and 2"}


def test_unhashable_value_fails():
    assert explain(unique_p, [42, []]) == {"result": False, "reason": "Unhashable key [] at index 1"}


def test_unhashable_custom_key_fails():
    def tags(item):
        return item["tags"]

    by_tags = unique_by_p(tags)
    assert explain(by_tags, [{"tags": ["red"]}]) == {
        "result": False,
        "reason": "Unhashable key ['red'] at index 0",
    }


def test_error_raised_by_custom_key_propagates():
    with pytest.raises(TypeError, match="str"):
        unique_by_p(str.casefold)([123])


@pytest.mark.parametrize("candidate", [unique_p, unique_by_p(str.casefold)])
def test_true_generator_produces_multi_element_unique_lists(candidate):
    source = in_p(("alpha", "ALPHA", "beta", "gamma", "delta", "epsilon", "zeta"))
    true_values = list(islice(generate_true(candidate, value_p=source), 5))
    assert len(true_values) == 5
    assert len({len(value) for value in true_values if len(value) > 1}) > 1
    assert all(candidate(value) for value in true_values)


def test_true_generator_progresses_with_a_single_possible_key():
    true_values = list(islice(generate_true(unique_p, value_p=eq_p(7)), 5))
    assert true_values == [[], [7], [7], [7], [7]]


@pytest.mark.parametrize("candidate", [unique_p, unique_by_p(str.casefold)])
def test_false_generator_produces_duplicate_keys(candidate):
    false_values = list(islice(generate_false(candidate, value_p=is_str_p), 5))
    assert len(false_values) == 5
    assert not any(candidate(value) for value in false_values)


def test_identity_serialization():
    assert to_json(unique_p) == {"unique": None}
    assert from_json(to_json(unique_p)) is unique_p
    assert yaml.safe_load(to_yaml(unique_p)) == {"unique": None}
    assert "unique" in to_dot(unique_p).source


def test_keyed_serialization_has_no_callable_to_round_trip():
    predicate = unique_by_p(str.casefold)
    data = to_json(predicate)
    assert data == {"unique_by": {"key": "casefold"}}
    assert yaml.safe_load(to_yaml(predicate)) == data
    assert "casefold" in to_dot(predicate).source
    with pytest.raises(ValueError, match="key function required"):
        from_json(data)


def test_key_name_is_stable_for_functions_without_a_custom_name():
    assert unique_by_p(lambda value: value).key_name == "<lambda>"
    assert unique_by_p(partial(round, ndigits=1)).key_name == "partial"
