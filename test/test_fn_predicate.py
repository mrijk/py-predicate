import math

import pytest

from predicate import eq_p, explain, fn_p, is_finite_p, is_inf_p, is_int_p, is_not_none_p, is_str_p, or_p
from predicate.fn_predicate import generate_inf, undefined
from predicate.match_predicate import match_p
from predicate.predicate import predicate_partial


def test_fn_p_with_lambda():
    in_123 = fn_p(lambda x: str(x) in ["1", "2", "3"])
    exists_p = is_not_none_p & in_123

    assert not exists_p(None)
    assert not exists_p(4)
    assert exists_p(3)

    assert repr(in_123) == "fn_p(predicate_fn=<lambda>)"


def test_fn_p_with_fun():
    def func(x: int) -> bool:
        return str(x) in ["1", "2", "3"]

    in_123 = fn_p(func)

    assert in_123(3)

    assert repr(in_123) == "fn_p(predicate_fn=func)"


def test_fn_p_explain():
    predicate = fn_p(lambda x: str(x) in ["1", "2", "3"])

    expected = {"reason": "Function returned False for value 4", "result": False}
    assert explain(predicate, 4) == expected


def test_is_finite_p():
    assert not is_finite_p(math.inf)
    assert is_finite_p(13)
    assert is_finite_p(3.14)


def test_is_inf_p():
    assert not is_inf_p(13)

    assert is_inf_p(-math.inf)
    assert is_inf_p(math.inf)


def test_undefined_raises_with_message():
    with pytest.raises(ValueError, match=r"^Please register generator type$"):
        undefined()


def test_generate_inf_first_value_is_negative():
    assert next(generate_inf()) == -math.inf


def test_predicate_partial():
    partial_or = predicate_partial(or_p, eq_p(1))
    combined = partial_or(eq_p(2))
    assert combined(1)
    assert combined(2)
    assert not combined(3)


async def _async_positive(x: int) -> bool:
    return x > 0


def test_fn_p_async_true():
    assert fn_p(_async_positive)(5)


def test_fn_p_async_false():
    assert not fn_p(_async_positive)(-1)


def test_predicate_partial_with_kwargs():
    # full_match=True kwarg must be preserved; dropping **kwargs makes full_match=False (default)
    partial_match = predicate_partial(match_p, is_int_p, full_match=True)
    predicate = partial_match(is_str_p)
    assert predicate([1, "foo"])
    assert not predicate([1, "foo", "bar"])  # "bar" leftover, only caught with full_match=True
