import operator
from datetime import datetime

import pytest

from predicate import (
    explain,
    generate_false,
    generate_true,
    pair_eq_p,
    pair_ge_p,
    pair_gt_p,
    pair_le_p,
    pair_lt_p,
    pair_ne_p,
    pair_p,
    to_json,
    to_latex,
)
from predicate.formatter.from_json import from_json
from predicate.pair_predicate import PairPredicate


def test_pair_p_lt():
    predicate = pair_lt_p
    assert predicate((1, 2))
    assert not predicate((2, 1))
    assert not predicate((1, 1))


def test_pair_p_le():
    assert pair_le_p((1, 2))
    assert pair_le_p((1, 1))
    assert not pair_le_p((2, 1))


def test_pair_p_eq():
    assert pair_eq_p((3, 3))
    assert not pair_eq_p((1, 2))


def test_pair_p_ne():
    assert pair_ne_p((1, 2))
    assert not pair_ne_p((3, 3))


def test_pair_p_ge():
    assert pair_ge_p((2, 1))
    assert pair_ge_p((1, 1))
    assert not pair_ge_p((1, 2))


def test_pair_p_gt():
    assert pair_gt_p((2, 1))
    assert not pair_gt_p((1, 1))
    assert not pair_gt_p((1, 2))


def test_pair_p_lambda():
    predicate = pair_p(lambda a, b: a + b == 10)
    assert predicate((3, 7))
    assert not predicate((3, 8))


@pytest.mark.parametrize(
    "predicate, pair",
    [
        (pair_lt_p, (2, 1)),
        (pair_le_p, (2, 1)),
        (pair_eq_p, (1, 2)),
        (pair_ne_p, (3, 3)),
        (pair_ge_p, (1, 2)),
        (pair_gt_p, (1, 1)),
    ],
)
def test_pair_p_explain_failure(predicate, pair):
    result = explain(predicate, pair)
    assert result["result"] is False
    assert "reason" in result


def test_pair_p_explain_success():
    assert explain(pair_lt_p, (1, 2)) == {"result": True}


def test_pair_p_repr():
    assert repr(pair_lt_p) == "pair_p(lt)"
    assert repr(pair_le_p) == "pair_p(le)"
    assert repr(pair_eq_p) == "pair_p(eq)"
    assert repr(pair_ne_p) == "pair_p(ne)"
    assert repr(pair_ge_p) == "pair_p(ge)"
    assert repr(pair_gt_p) == "pair_p(gt)"


def test_pair_p_repr_non_default_klass():
    assert repr(pair_p(operator.lt, klass=float)) == "pair_p(lt, float)"
    assert repr(pair_p(operator.lt, klass=str)) == "pair_p(lt, str)"
    assert repr(pair_p(operator.lt, klass=datetime)) == "pair_p(lt, datetime)"


def test_pair_p_lambda_repr():
    predicate = pair_p(lambda a, b: a < b)
    assert repr(predicate) == "pair_p(<lambda>)"


def test_pair_p_is_dataclass():
    assert isinstance(pair_lt_p, PairPredicate)
    assert pair_lt_p.fn is operator.lt
    assert pair_lt_p.klass is int


def test_pair_p_klass_default_is_int():
    assert pair_p(operator.lt).klass is int


@pytest.mark.parametrize(
    "predicate, fn_name",
    [
        (pair_lt_p, "lt"),
        (pair_le_p, "le"),
        (pair_eq_p, "eq"),
        (pair_ne_p, "ne"),
        (pair_ge_p, "ge"),
        (pair_gt_p, "gt"),
    ],
)
def test_pair_p_to_json(predicate, fn_name):
    assert to_json(predicate) == {"pair": {"fn": fn_name}}


def test_pair_p_to_json_non_default_klass():
    assert to_json(pair_p(operator.lt, klass=float)) == {"pair": {"fn": "lt", "klass": "float"}}
    assert to_json(pair_p(operator.lt, klass=str)) == {"pair": {"fn": "lt", "klass": "str"}}


@pytest.mark.parametrize(
    "fn_name, predicate",
    [
        ("lt", pair_lt_p),
        ("le", pair_le_p),
        ("eq", pair_eq_p),
        ("ne", pair_ne_p),
        ("ge", pair_ge_p),
        ("gt", pair_gt_p),
    ],
)
def test_pair_p_from_json_roundtrip(fn_name, predicate):
    assert from_json({"pair": {"fn": fn_name}}) == predicate


def test_pair_p_from_json_roundtrip_with_klass():
    predicate = pair_p(operator.lt, klass=float)
    assert from_json(to_json(predicate)) == predicate


def test_pair_p_from_json_unknown_fn_raises():
    with pytest.raises(ValueError, match="unknown function"):
        from_json({"pair": {"fn": "unknown"}})


def test_pair_p_from_json_unknown_klass_raises():
    with pytest.raises(ValueError, match="unknown class"):
        from_json({"pair": {"fn": "lt", "klass": "Decimal"}})


@pytest.mark.parametrize(
    "predicate, expected_latex",
    [
        (pair_lt_p, r"x_1 \lt x_2"),
        (pair_le_p, r"x_1 \le x_2"),
        (pair_eq_p, r"x_1 = x_2"),
        (pair_ne_p, r"x_1 \neq x_2"),
        (pair_ge_p, r"x_1 \ge x_2"),
        (pair_gt_p, r"x_1 \gt x_2"),
    ],
)
def test_pair_p_to_latex(predicate, expected_latex):
    assert to_latex(predicate) == expected_latex


@pytest.mark.parametrize("predicate", [pair_lt_p, pair_le_p, pair_eq_p, pair_ne_p, pair_ge_p, pair_gt_p])
def test_pair_p_generate_true(predicate):
    values = [next(generate_true(predicate)) for _ in range(10)]
    assert all(predicate(v) for v in values)


@pytest.mark.parametrize("predicate", [pair_lt_p, pair_le_p, pair_eq_p, pair_ne_p, pair_ge_p, pair_gt_p])
def test_pair_p_generate_false(predicate):
    values = [next(generate_false(predicate)) for _ in range(10)]
    assert all(not predicate(v) for v in values)


@pytest.mark.parametrize("klass", [float, str, datetime])
def test_pair_p_generate_true_non_int_types(klass):
    predicate = pair_p(operator.lt, klass=klass)
    values = [next(generate_true(predicate)) for _ in range(10)]
    assert all(predicate(v) for v in values)


@pytest.mark.parametrize("klass", [float, str, datetime])
def test_pair_p_generate_false_non_int_types(klass):
    predicate = pair_p(operator.lt, klass=klass)
    values = [next(generate_false(predicate)) for _ in range(10)]
    assert all(not predicate(v) for v in values)
