import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    count_p,
    eq_p,
    exactly_n,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    has_length_p,
    has_path_p,
    implies_p,
    in_p,
    is_close_p,
    is_dict_of_p,
    is_falsy_p,
    is_instance_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_real_subset_p,
    is_real_superset_p,
    is_set_of_p,
    is_str_p,
    is_subclass_p,
    is_subset_p,
    is_superset_p,
    is_truthy_p,
    is_tuple_of_p,
    juxt_p,
    le_p,
    lt_p,
    match_p,
    ne_p,
    not_in_p,
    optional,
    regex_p,
    to_json,
)
from predicate.formatter.from_json import from_json
from predicate.is_same_predicate import is_same_p
from predicate.named_predicate import NamedPredicate
from predicate.struct_predicate import is_struct_p


@pytest.mark.parametrize(
    "predicate",
    [
        always_false_p,
        always_true_p,
        all_p(is_int_p),
        any_p(is_int_p),
        always_true_p & always_false_p,
        always_true_p | always_false_p,
        always_true_p ^ always_false_p,
        ~always_true_p,
        count_p(is_int_p, eq_p(3)),
        is_dict_of_p(("name", is_str_p)),
        eq_p(42),
        eq_p("hello"),
        exactly_n(2, is_int_p),
        ge_p(5),
        ge_le_p(lower=1, upper=10),
        ge_lt_p(lower=1, upper=10),
        gt_p(5),
        gt_le_p(lower=1, upper=10),
        gt_lt_p(lower=1, upper=10),
        has_key_p("key"),
        has_length_p(eq_p(3)),
        has_path_p(eq_p("a"), eq_p("b")),
        implies_p(always_true_p),
        in_p([1, 2, 3]),
        is_close_p(1.0, rel_tol=1e-9, abs_tol=0.0),
        is_falsy_p,
        is_int_p,
        is_instance_p(int, str),
        is_none_p,
        is_not_none_p,
        is_real_subset_p({1, 2, 3}),
        is_real_superset_p({1, 2, 3}),
        is_same_p(always_true_p),
        is_subclass_p(int),
        is_subclass_p((int, str)),
        is_subset_p({1, 2, 3}),
        is_superset_p({1, 2, 3}),
        is_truthy_p,
        juxt_p(always_true_p, always_false_p, evaluate=all_p(always_true_p)),
        le_p(10),
        is_list_of_p(is_int_p),
        lt_p(10),
        match_p(is_int_p, is_str_p),
        ne_p(7),
        not_in_p([4, 5, 6]),
        optional(is_int_p),
        regex_p(r"\d+"),
        is_set_of_p(is_int_p),
        is_struct_p(required={"name": is_str_p, "age": is_int_p}, optional={"email": regex_p(r".+@.+")}),
        is_tuple_of_p(is_int_p, is_str_p),
        NamedPredicate(name="x"),
    ],
)
def test_from_json_round_trip(predicate):
    assert from_json(to_json(predicate)) == predicate


def test_from_json_reduce_raises():
    with pytest.raises(ValueError, match="reduce_p cannot be deserialized from JSON"):
        from_json({"reduce": {"fn": "my_fn", "initial": 0}})


def test_from_json_unknown_key_raises():
    with pytest.raises(ValueError, match="Unknown predicate type"):
        from_json({"unknown_predicate_type": {}})


def test_from_json_unknown_class_raises():
    with pytest.raises(ValueError, match="Unknown class"):
        from_json({"is_instance": {"klass": ["UnknownClass"]}})
