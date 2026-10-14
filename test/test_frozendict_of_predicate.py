import sys

import pytest

from predicate import eq_p, explain, is_frozendict_of_p, is_int_p, is_str_p


def test_is_frozendict_of_p_not_a_frozendict():
    predicate = is_frozendict_of_p(("x", is_str_p))

    assert not predicate({"x": "foo"})
    assert not predicate("x")


def test_is_frozendict_of_explain_not_a_frozendict():
    predicate = is_frozendict_of_p(("x", is_int_p))

    expected = {"reason": "{'x': 1} is not an instance of a frozendict", "result": False}
    assert explain(predicate, {"x": 1}) == expected


def test_is_frozendict_of_p_repr():
    predicate = is_frozendict_of_p(("x", is_int_p), (is_str_p, is_str_p))

    assert repr(predicate) == "is_frozendict_of_p(('x', is_int_p), (is_str_p, is_str_p))"


if sys.version_info >= (3, 15):

    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (frozendict(), False),  # noqa: F821
            (frozendict({1: "foo"}), False),  # noqa: F821
            (frozendict({"y": "foo"}), False),  # noqa: F821
            (frozendict({"x": "foo"}), True),  # noqa: F821
        ],
    )
    def test_is_frozendict_of_p(value, expected):
        predicate = is_frozendict_of_p((eq_p("x"), is_str_p))

        assert predicate(value) is expected

    def test_is_frozendict_of_explain():
        predicate = is_frozendict_of_p(("x", is_int_p), (eq_p("y"), is_str_p))

        expected = {"key": "x", "value": "foo", "reason": "foo is not an instance of type int", "result": False}
        assert explain(predicate, frozendict({"x": "foo", "y": "bar"})) == expected  # noqa: F821
