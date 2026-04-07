import math

import pytest

from predicate.formatter.fn_source import get_fn_source


def test_get_fn_source_lambda():
    fn = lambda x: x + 1  # noqa: E731
    result = get_fn_source(fn)
    assert "source" in result
    assert "lambda x" in result["source"]


def test_get_fn_source_named_function():
    def double(x: int) -> int:
        return x * 2

    result = get_fn_source(double)
    assert "source" in result
    assert "return x * 2" in result["source"]


def test_get_fn_source_builtin():
    result = get_fn_source(math.isfinite)
    assert "qualname" in result
    assert "isfinite" in result["qualname"]
    assert "source" not in result


def test_get_fn_source_builtin_abs():
    result = get_fn_source(abs)
    assert "qualname" in result


def test_get_fn_source_two_lambdas_same_line():
    f1, f2 = (lambda x: x + 1), (lambda x: x + 2)
    r1 = get_fn_source(f1)
    r2 = get_fn_source(f2)
    assert "source" in r1
    assert "source" in r2


@pytest.mark.parametrize(
    "fn, expected_key",
    [
        (lambda x: x > 0, "source"),
        (math.sqrt, "qualname"),
    ],
)
def test_get_fn_source_returns_expected_key(fn, expected_key):
    result = get_fn_source(fn)
    assert expected_key in result
