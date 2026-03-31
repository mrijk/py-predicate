from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    count_p,
    eq_p,
    exactly_n,
    fn_p,
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
    is_dict_of_p,
    is_even_p,
    is_falsy_p,
    is_instance_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_odd_p,
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
    tee_p,
    to_json,
)
from predicate.is_same_predicate import is_same_p
from predicate.named_predicate import NamedPredicate


def test_format_json_false():
    predicate = always_false_p

    json = to_json(predicate)

    assert json == {"false": False}


def test_format_json_true():
    predicate = always_true_p

    json = to_json(predicate)

    assert json == {"true": True}


def test_format_json_and():
    predicate = always_true_p & always_false_p

    json = to_json(predicate)

    assert json == {"and": {"left": {"true": True}, "right": {"false": False}}}


def test_format_json_or():
    predicate = always_true_p | always_false_p

    json = to_json(predicate)

    assert json == {"or": {"left": {"true": True}, "right": {"false": False}}}


def test_format_json_xor():
    predicate = always_true_p ^ always_false_p

    json = to_json(predicate)

    assert json == {
        "xor": {
            "left": {"true": True},
            "right": {"false": False},
        }
    }


def test_format_json_all():
    predicate = all_p(predicate=always_true_p)

    json = to_json(predicate)

    assert json == {"all": {"predicate": {"true": True}}}


def test_format_json_any():
    predicate = any_p(predicate=always_true_p)

    json = to_json(predicate)

    assert json == {"any": {"predicate": {"true": True}}}


def test_format_json_not():
    predicate = ~always_true_p

    json = to_json(predicate)

    assert json == {"not": {"predicate": {"true": True}}}


def test_format_json_ne():
    predicate = ne_p(13)

    json = to_json(predicate)

    assert json == {"ne": {"v": 13}}


def test_format_json_fn():
    predicate = fn_p(lambda x: x)

    json = to_json(predicate)

    assert json == {"fn": {"name": "<lambda>", "source": "lambda x: x"}}


def test_format_json_fn_named_function():
    def is_positive(x: int) -> bool:
        return x > 0

    predicate = fn_p(is_positive)
    json = to_json(predicate)

    assert json["fn"]["name"] == "is_positive"
    assert "return x > 0" in json["fn"]["source"]


def test_format_json_fn_builtin():
    import math

    predicate = fn_p(math.isfinite)
    json = to_json(predicate)

    assert json["fn"]["name"] == "isfinite"
    assert json["fn"]["qualname"] == "math.isfinite"
    assert "source" not in json["fn"]


def test_format_json_fn_is_even_p():
    json = to_json(is_even_p)

    assert json["fn"]["source"] == "lambda x: x % 2 == 0"


def test_format_json_fn_is_odd_p():
    json = to_json(is_odd_p)

    assert json["fn"]["source"] == "lambda x: x % 2 != 0"


def test_format_json_is_falsy():
    predicate = is_falsy_p

    json = to_json(predicate)

    assert json == {"is_falsy": None}


def test_format_json_is_truthy():
    predicate = is_truthy_p

    json = to_json(predicate)

    assert json == {"is_truthy": None}


def test_format_json_named():
    predicate = NamedPredicate(name="foo")

    json = to_json(predicate)

    assert json == {"variable": "foo"}


def test_format_json_tee():
    predicate = tee_p(fn=lambda _: None)

    json = to_json(predicate)

    assert json == {"tee": None}


def test_format_json_juxt():
    predicate = juxt_p(always_true_p, always_false_p, evaluate=all_p(always_true_p))

    json = to_json(predicate)

    assert json == {
        "juxt": {
            "predicates": [{"true": True}, {"false": False}],
            "evaluate": {"all": {"predicate": {"true": True}}},
        }
    }


def test_format_json_eq():
    predicate = eq_p(5)

    json = to_json(predicate)

    assert json == {"eq": {"v": 5}}


def test_format_json_ge():
    predicate = ge_p(2)

    json = to_json(predicate)

    assert json == {"ge": {"v": 2}}


def test_format_json_gt():
    predicate = gt_p(2)

    json = to_json(predicate)

    assert json == {"gt": {"v": 2}}


def test_format_json_le():
    predicate = le_p(10)

    json = to_json(predicate)

    assert json == {"le": {"v": 10}}


def test_format_json_lt():
    predicate = lt_p(10)

    json = to_json(predicate)

    assert json == {"lt": {"v": 10}}


def test_format_json_ge_le():
    predicate = ge_le_p(1, 10)

    json = to_json(predicate)

    assert json == {"ge_le": {"lower": 1, "upper": 10}}


def test_format_json_ge_lt():
    predicate = ge_lt_p(1, 10)

    json = to_json(predicate)

    assert json == {"ge_lt": {"lower": 1, "upper": 10}}


def test_format_json_gt_le():
    predicate = gt_le_p(1, 10)

    json = to_json(predicate)

    assert json == {"gt_le": {"lower": 1, "upper": 10}}


def test_format_json_gt_lt():
    predicate = gt_lt_p(1, 10)

    json = to_json(predicate)

    assert json == {"gt_lt": {"lower": 1, "upper": 10}}


def test_format_json_is_instance_single():
    predicate = is_int_p

    json = to_json(predicate)

    assert json == {"is_instance": {"klass": ["int"]}}


def test_format_json_is_instance_multiple():
    predicate = is_instance_p(int, str)

    json = to_json(predicate)

    assert json == {"is_instance": {"klass": ["int", "str"]}}


def test_format_unknown(unknown_p):
    json = to_json(unknown_p)

    assert json == {"unknown": {}}


def test_format_json_is_none():
    json = to_json(is_none_p)

    assert json == {"is_none": None}


def test_format_json_is_not_none():
    json = to_json(is_not_none_p)

    assert json == {"is_not_none": None}


def test_format_json_has_key():
    predicate = has_key_p("name")

    json = to_json(predicate)

    assert json == {"has_key": {"key": "name"}}


def test_format_json_regex():
    predicate = regex_p(r"\d+")

    json = to_json(predicate)

    assert json == {"regex": {"pattern": r"\d+"}}


def test_format_json_implies():
    predicate = implies_p(always_true_p)

    json = to_json(predicate)

    assert json == {"implies": {"predicate": {"true": True}}}


def test_format_json_has_length():
    predicate = has_length_p(eq_p(3))

    json = to_json(predicate)

    assert json == {"has_length": {"length_p": {"eq": {"v": 3}}}}


def test_format_json_count():
    predicate = count_p(is_int_p, eq_p(2))

    json = to_json(predicate)

    assert json == {"count": {"predicate": {"is_instance": {"klass": ["int"]}}, "length_p": {"eq": {"v": 2}}}}


def test_format_json_list_of():
    predicate = is_list_of_p(is_int_p)

    json = to_json(predicate)

    assert json == {"list_of": {"predicate": {"is_instance": {"klass": ["int"]}}}}


def test_format_json_set_of():
    predicate = is_set_of_p(is_int_p)

    json = to_json(predicate)

    assert json == {"set_of": {"predicate": {"is_instance": {"klass": ["int"]}}}}


def test_format_json_optional():
    predicate = optional(is_int_p)

    json = to_json(predicate)

    assert json == {"optional": {"predicate": {"is_instance": {"klass": ["int"]}}}}


def test_format_json_exactly():
    predicate = exactly_n(3, is_int_p)

    json = to_json(predicate)

    assert json == {"exactly": {"n": 3, "predicate": {"is_instance": {"klass": ["int"]}}}}


def test_format_json_tuple_of():
    predicate = is_tuple_of_p(is_int_p, is_str_p)

    json = to_json(predicate)

    assert json == {
        "tuple_of": {
            "predicates": [
                {"is_instance": {"klass": ["int"]}},
                {"is_instance": {"klass": ["str"]}},
            ]
        }
    }


def test_format_json_has_path():
    predicate = has_path_p(eq_p("a"), eq_p("b"))

    json = to_json(predicate)

    assert json == {"has_path": {"path": [{"eq": {"v": "a"}}, {"eq": {"v": "b"}}]}}


def test_format_json_match():
    predicate = match_p(is_int_p, is_str_p)

    json = to_json(predicate)

    assert json == {
        "match": {
            "predicates": [
                {"is_instance": {"klass": ["int"]}},
                {"is_instance": {"klass": ["str"]}},
            ],
            "full_match": False,
        }
    }


def test_format_json_is_subclass_single():
    predicate = is_subclass_p(int)

    json = to_json(predicate)

    assert json == {"is_subclass": {"klass": ["int"]}}


def test_format_json_is_subclass_union():
    predicate = is_subclass_p(int | str)

    json = to_json(predicate)

    assert json == {"is_subclass": {"klass": ["int", "str"]}}


def test_format_json_is_subset():
    predicate = is_subset_p({1, 2, 3})

    json = to_json(predicate)

    assert json == {"is_subset": {"v": sorted([1, 2, 3])}}


def test_format_json_is_real_subset():
    predicate = is_real_subset_p({1, 2, 3})

    json = to_json(predicate)

    assert json == {"is_real_subset": {"v": sorted([1, 2, 3])}}


def test_format_json_is_superset():
    predicate = is_superset_p({1, 2, 3})

    json = to_json(predicate)

    assert json == {"is_superset": {"v": sorted([1, 2, 3])}}


def test_format_json_is_real_superset():
    predicate = is_real_superset_p({1, 2, 3})

    json = to_json(predicate)

    assert json == {"is_real_superset": {"v": sorted([1, 2, 3])}}


def test_format_json_in():
    predicate = in_p([1, 2, 3])

    json = to_json(predicate)

    assert json == {"in": {"v": [1, 2, 3]}}


def test_format_json_not_in():
    predicate = not_in_p([1, 2, 3])

    json = to_json(predicate)

    assert json == {"not_in": {"v": [1, 2, 3]}}


def test_format_json_dict_of():
    predicate = is_dict_of_p(("name", is_str_p))

    json = to_json(predicate)

    assert json == {"dict_of": {"kv": [[{"eq": {"v": "name"}}, {"is_instance": {"klass": ["str"]}}]]}}


def test_format_json_is_same():
    predicate = is_same_p(always_true_p)

    json = to_json(predicate)

    assert json == {"is_same": {"predicate": {"true": True}}}
