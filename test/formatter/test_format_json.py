from dataclasses import dataclass

from predicate import Predicate, all_p, always_false_p, always_true_p, any_p, fn_p, is_falsy_p, ne_p, to_json
from predicate.named_predicate import NamedPredicate
from predicate.standard_predicates import is_truthy_p, tee_p


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


def test_format_unknown():
    @dataclass
    class UnknownPredicate[T](Predicate[T]):
        def __call__(self, *args, **kwargs) -> bool:
            return False

    predicate = UnknownPredicate()

    json = to_json(predicate)

    assert json == {"unknown": {}}
