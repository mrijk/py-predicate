from predicate import always_false_p, always_true_p
from predicate.formatter.format_json import to_json


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


def test_format_json_not():
    predicate = ~always_true_p

    json = to_json(predicate)

    assert json == {"not": {"predicate": {"true": True}}}
