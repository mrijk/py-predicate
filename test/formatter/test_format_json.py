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
    assert to_json(eq_p(5)) == {"eq": {"v": 5}}


def test_format_json_ge():
    assert to_json(ge_p(2)) == {"ge": {"v": 2}}


def test_format_json_gt():
    assert to_json(gt_p(2)) == {"gt": {"v": 2}}


def test_format_json_le():
    assert to_json(le_p(10)) == {"le": {"v": 10}}


def test_format_json_lt():
    assert to_json(lt_p(10)) == {"lt": {"v": 10}}


def test_format_json_ge_le():
    assert to_json(ge_le_p(1, 10)) == {"ge_le": {"lower": 1, "upper": 10}}


def test_format_json_ge_lt():
    assert to_json(ge_lt_p(1, 10)) == {"ge_lt": {"lower": 1, "upper": 10}}


def test_format_json_gt_le():
    assert to_json(gt_le_p(1, 10)) == {"gt_le": {"lower": 1, "upper": 10}}


def test_format_json_gt_lt():
    assert to_json(gt_lt_p(1, 10)) == {"gt_lt": {"lower": 1, "upper": 10}}


def test_format_json_is_instance_single():
    assert to_json(is_int_p) == {"is_instance": {"klass": ["int"]}}


def test_format_json_is_instance_multiple():
    from predicate import is_instance_p

    assert to_json(is_instance_p(int, str)) == {"is_instance": {"klass": ["int", "str"]}}


def test_format_unknown(unknown_p):
    json = to_json(unknown_p)

    assert json == {"unknown": {}}
