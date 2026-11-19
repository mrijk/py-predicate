import sys
from itertools import islice

import pytest
from hypothesis import given
from hypothesis import strategies as st

import predicate
from predicate import (
    compile_predicate,
    generate_false,
    generate_true,
    is_int_str_p,
    try_compile_predicate,
)
from predicate.compile_predicate import NotCompilableError


@pytest.mark.parametrize("value", ["0", "-5", "1_000", "٠١٢", "\u20035\u2003"])
def test_accepts_integer_strings(value):
    assert is_int_str_p(value)


@pytest.mark.parametrize("value", ["", "1.0", "1e3", "0x10", "²", "1__0", "\x1c5"])
def test_rejects_invalid_strings(value):
    assert not is_int_str_p(value)


@pytest.mark.parametrize("value", [0, True, None, b"5", bytearray(b"5")])
def test_rejects_non_strings(value):
    assert not is_int_str_p(value)


def test_does_not_coerce_non_string_objects():
    class IntLike:
        def __int__(self):
            raise AssertionError("Non-string __int__ must not be called")

        def __str__(self):
            raise AssertionError("Non-string __str__ must not be called")

    assert not is_int_str_p(IntLike())


def test_accepts_string_subclasses():
    class Text(str):
        pass

    assert is_int_str_p(Text("-5"))


@given(st.text())
def test_matches_python_int(value):
    try:
        int(value)
    except ValueError:
        expected = False
    else:
        expected = True
    assert is_int_str_p(value) is expected


def test_respects_runtime_integer_length_limit():
    limit = sys.get_int_max_str_digits()
    if limit == 0:
        pytest.skip("Interpreter has no integer string conversion limit")
    assert not is_int_str_p("1" * (limit + 1))
    assert sys.get_int_max_str_digits() == limit


@pytest.mark.parametrize("generate, expected", [(generate_true, True), (generate_false, False)])
def test_generators_are_repeatable_nonempty_string_streams(generate, expected):
    for _ in range(2):
        values = list(islice(generate(is_int_str_p), 100))
        assert len(values) == 100
        assert all(isinstance(value, str) for value in values)
        assert all(is_int_str_p(value) is expected for value in values)


def test_public_export_and_fn_fallback():
    assert "is_int_str_p" in predicate.__all__
    with pytest.raises(NotCompilableError):
        compile_predicate(is_int_str_p)
    fallback = try_compile_predicate(is_int_str_p)
    assert fallback is is_int_str_p
    assert fallback("-5")
    assert not fallback("5.0")
    assert (~is_int_str_p)("5.0")
    assert (is_int_str_p & ~predicate.is_blank_p)("0")
