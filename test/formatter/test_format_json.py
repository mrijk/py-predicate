from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_p,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    is_falsy_p,
    is_instance_p,
    is_int_p,
    is_truthy_p,
    juxt_p,
    le_p,
    lt_p,
    ne_p,
    tee_p,
    to_json,
)
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

    assert json == {"fn": {"name": "<lambda>"}}


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
