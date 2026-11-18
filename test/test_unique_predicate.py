from itertools import islice

import pytest

from predicate import generate_false, generate_true, is_str_p, unique_by_p, unique_p
from predicate.explain import explain
from predicate.formatter.format_dot import to_dot
from predicate.formatter.format_json import to_json


def test_unique_values_and_first_duplicate():
    assert unique_p([])
    assert unique_p(iter([1, 2, 3]))
    assert not unique_p((1, 2, 1))
    assert explain(unique_p, iter([1, 2, 1, 2])) == {
        "result": False,
        "reason": "Duplicate key 1 at indices 0 and 2",
    }
    assert explain(unique_p, iter([1, 2, 3])) == {"result": True}


def test_custom_key_and_unhashable_values():
    by_name = unique_by_p(str.casefold)
    assert by_name(["one", "two"])
    assert not by_name(["one", "ONE"])
    assert by_name.explain_failure(["one", "two", "ONE"]) == {"reason": "Duplicate key 'one' at indices 0 and 2"}
    assert explain(unique_p, [42, []]) == {"result": False, "reason": "Unhashable key [] at index 1"}
    assert not unique_by_p(list)(["a"])
    with pytest.raises(TypeError, match="str"):
        by_name([123])


@pytest.mark.parametrize("candidate", [unique_p, unique_by_p(str.casefold)])
def test_generators_produce_correct_values(candidate):
    true_values = list(islice(generate_true(candidate, value_p=is_str_p), 5))
    false_values = list(islice(generate_false(candidate, value_p=is_str_p), 5))
    assert len(true_values) == len(false_values) == 5
    assert all(candidate(value) for value in true_values)
    assert not any(candidate(value) for value in false_values)


def test_formatters_show_identity_or_key():
    assert to_json(unique_p) == {"unique": None}
    assert to_json(unique_by_p(str.casefold)) == {"unique_by": {"key": "casefold"}}
    assert "unique" in to_dot(unique_p).source
    assert "casefold" in to_dot(unique_by_p(str.casefold)).source
