import ast
import asyncio
import datetime
import logging
import re
import time
import types
from functools import partial
from typing import Any, ForwardRef, TypeVar

import pytest

from predicate import all_p, ge_p, is_dict_of_p, is_dict_p, is_empty_p, is_float_p, is_int_p, is_str_p, pos_p
from predicate.list_of_predicate import is_list_of_p
from predicate.spec.exercise import Spec, exercise
from predicate.spec.exercise_function import get_spec_from_function_annotation
from predicate.spec.spec import InvalidSpecError, SpecViolationError


def test_exercise_happy():
    def adder(x, y):
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    result = list(exercise(adder, spec=spec))
    assert result


def test_exercise_no_param_happy():
    def adder():
        return 42

    spec: Spec = {"args": {}, "ret": is_int_p}

    result = list(exercise(adder, spec=spec))
    assert result


def test_exercise_lambda():
    a_lambda = lambda x: x  # noqa: E731

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p}

    result = list(exercise(a_lambda, spec=spec))

    assert result


def test_exercise_partial_uses_wrapped_annotations():
    def add(x: int, y: int) -> int:
        return x + y

    result = list(exercise(partial(add, 1), n=3))

    assert len(result) == 3


def test_exercise_with_fn_happy():
    def max_int(x, y):
        return x if x >= y else y

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    result = list(exercise(max_int, spec=spec))
    assert result


def test_exercise_with_fn_fail():
    def max_int(x, y):
        return x if x >= y else y - 1

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    with pytest.raises(SpecViolationError, match="^Not conform spec: fn constraint failed for inputs"):
        list(exercise(max_int, spec=spec, n=100))


def test_exercise_with_fn_p_happy():
    def max_int(x, y):
        return x if x >= y else y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    result = list(exercise(max_int, spec=spec))
    assert result


def test_exercise_with_fn_p_fail():
    def max_int(x, y):
        return x if x >= y else y - 1

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    with pytest.raises(SpecViolationError, match="^Not conform spec:"):
        list(exercise(max_int, spec=spec, n=100))


def test_exercise_missing_return_annotation_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {  # type: ignore
        "args": {"x": is_int_p, "y": is_int_p},
    }

    with pytest.raises(InvalidSpecError, match="Return annotation not in spec"):
        list(exercise(adder, spec=spec))


def test_exercise_no_types_defined():
    def dup(x):
        return x

    with pytest.raises(InvalidSpecError, match="Cannot derive spec for 'dup': missing return annotation"):
        list(exercise(dup))


def test_exercise_generic_return_annotation():
    def dup[T](x: T) -> T:
        return x

    result = list(exercise(dup))
    assert result


def test_exercise_unannotated_parameter_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {
        "args": {
            "x": is_int_p,
        },
        "ret": is_int_p,
    }

    with pytest.raises(InvalidSpecError, match="Unannotated parameter 'y' not in spec"):
        list(exercise(adder, spec=spec))


def test_exercise_wrong_parameter_name():
    def adder(x, y):
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "z": is_int_p}, "ret": is_int_p}

    with pytest.raises(InvalidSpecError, match="Parameter 'z' not in function signature"):
        list(exercise(adder, spec=spec))


def test_exercise_wrong_return():
    def adder(x, y):
        return None  # Not an int!

    spec: Spec = {
        "args": {
            "x": is_int_p,
            "y": is_int_p,
        },
        "ret": is_int_p,
    }

    with pytest.raises(
        SpecViolationError,
        match=re.escape("Not conform spec: {'result': False, 'reason': 'None is not an instance of type int'}"),
    ):
        list(exercise(adder, spec=spec))


def test_exercise_with_partial_spec():
    def adder(x: int, y) -> int:
        return x + y

    spec: Spec = {
        "args": {
            "y": is_int_p,
        },
        "ret": is_int_p,
    }

    result = list(exercise(adder, spec=spec))
    assert result


def test_exercise_with_constrained_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    spec: Spec = {
        "args": {
            "x": pos_p,
            "y": is_int_p,
        },
        "ret": is_int_p,
    }

    result = list(exercise(adder, spec=spec))
    assert result


def test_exercise_with_constrained_spec_fail():
    def adder(x: int, y: int) -> int:
        return x + y

    spec: Spec = {
        "args": {
            "x": is_int_p,
            "y": is_int_p | is_str_p,
        },
        "ret": is_int_p,
    }

    with pytest.raises(InvalidSpecError, match="Spec predicate is not a constrained annotation"):
        list(exercise(adder, spec=spec))


def test_exercise_annotated_without_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    result = list(exercise(adder))
    assert result


def test_exercise_partially_annotate_without_spec():
    def adder(x: int, y) -> int:
        return x + y

    with pytest.raises(InvalidSpecError, match="Cannot derive spec for 'adder': parameter 'y' has no annotation"):
        list(exercise(adder))


def test_exercise_infer_ret_from_annotation():
    def adder(x, y) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}}

    result = list(exercise(adder, spec=spec))
    assert result


@pytest.mark.asyncio
async def test_exercise_async_happy():
    async def adder(x: int, y: int) -> int:
        return x + y

    result = [r async for r in exercise(adder)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_with_spec():
    async def adder(x, y):
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    result = [r async for r in exercise(adder, spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_no_params():
    async def answer() -> int:
        return 42

    spec: Spec = {"args": {}, "ret": is_int_p}

    result = [r async for r in exercise(answer, spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_wrong_return():
    async def adder(x: int, y: int) -> int:
        return None  # type: ignore[return-value]

    with pytest.raises(SpecViolationError):
        async for _ in exercise(adder):
            pass


@pytest.mark.asyncio
async def test_exercise_async_function_no_annotation():
    async def dup(x):
        return x

    with pytest.raises(InvalidSpecError, match="Cannot derive spec for 'dup': missing return annotation"):
        async for _ in exercise(dup):
            pass


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    result = [r async for r in exercise(max_int, spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_fail():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y - 1  # wrong

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    with pytest.raises(SpecViolationError, match="^Not conform spec: fn constraint failed for inputs"):
        async for _ in exercise(max_int, spec=spec, n=100):
            pass


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_p():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    result = [r async for r in exercise(max_int, spec=spec)]
    assert result


def test_exercise_function_typevar_param_not_in_spec():
    T = TypeVar("T")

    def identity(x: T) -> int:
        return 0

    spec: Spec = {"args": {}, "ret": is_int_p}
    with pytest.raises(InvalidSpecError, match="not in spec"):
        list(exercise(identity, spec=spec))


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_p_fail():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y - 1  # wrong

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    with pytest.raises(SpecViolationError, match="^Not conform spec:"):
        async for _ in exercise(max_int, spec=spec, n=100):
            pass


def test_exercise_with_pre():
    def span(lo, hi):
        assert lo <= hi
        return hi - lo

    spec: Spec = {"args": {"lo": is_int_p, "hi": is_int_p}, "ret": is_int_p, "pre": lambda lo, hi: lo <= hi}

    results = list(exercise(span, spec=spec))

    assert len(results) == 10
    assert all(ret >= 0 for _, ret in results)


def test_exercise_raises_spec_violation():
    from predicate import SpecViolationError

    def double(x):
        return x * 3

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret == x * 2}

    with pytest.raises(SpecViolationError, match="fn constraint failed"):
        list(exercise(double, spec=spec))


def test_exercise_raises_expected():
    def inverse(x):
        if x == 0:
            raise ZeroDivisionError
        return 1 / x

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_float_p, "raises": ZeroDivisionError}

    result = list(exercise(inverse, spec=spec, n=50))

    assert any(isinstance(r, ZeroDivisionError) for _, r in result)


def test_exercise_raises_unexpected():
    def fail(x):
        raise KeyError

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "raises": ValueError}

    with pytest.raises(SpecViolationError, match="unexpected exception KeyError"):
        list(exercise(fail, spec=spec))


def test_exercise_raises_without_spec():
    def fail(x):
        raise KeyError

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p}

    with pytest.raises(KeyError):
        list(exercise(fail, spec=spec))


@pytest.mark.asyncio
async def test_exercise_async_raises_expected():
    async def fail(x):
        raise ValueError

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "raises": (KeyError, ValueError)}

    result = [r async for r in exercise(fail, spec=spec)]

    assert all(isinstance(r, ValueError) for _, r in result)


def test_exercise_with_unsatisfiable_pre():
    def identity(x):
        return x

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "pre": lambda x: False}

    with pytest.raises(InvalidSpecError, match="Could not generate values satisfying pre after 1000 attempts"):
        list(exercise(identity, spec=spec))


def test_exercise_with_fn_ret_name():
    def r(x: int, ret: int) -> int:
        return x

    spec: Spec = {"args": {}, "fn": lambda x, ret, result: result == x, "ret_name": "result"}

    assert list(exercise(r, spec=spec, n=5))


def test_exercise_with_fn_ret_name_clash():
    def r(x: int, ret: int) -> int:
        return x

    spec: Spec = {"args": {}, "fn": lambda x, ret: True}

    with pytest.raises(InvalidSpecError, match="Parameter 'ret' clashes"):
        list(exercise(r, spec=spec, n=5))


def test_exercise_var_positional():
    def total(*xs: int) -> int:
        return sum(xs)

    assert list(exercise(total, n=3))


def test_exercise_positional_only():
    def double(x: int, /) -> int:
        return 2 * x

    assert list(exercise(double, n=3))


def test_exercise_positional_and_var_positional():
    def total(x: int, *xs: int, scale: int) -> int:
        return (x + sum(xs)) * scale

    assert list(exercise(total, n=3))


def test_exercise_var_positional_with_spec():
    def total(*xs):
        return sum(xs)

    spec: Spec = {"args": {"xs": all_p(is_int_p)}, "ret": is_int_p}

    assert list(exercise(total, spec=spec, n=3))


def test_exercise_annotation_checks_elements():
    def head(xs: list[int]) -> int:
        return xs[0] if xs else 0

    spec = get_spec_from_function_annotation(head)

    assert spec["args"]["xs"]([1, 2])
    assert not spec["args"]["xs"](["a"])


def test_exercise_constrained_element_spec():
    def total(xs: list[int]) -> int:
        return sum(xs)

    spec: Spec = {"args": {"xs": is_list_of_p(is_int_p & ge_p(0))}, "ret": ge_p(0)}

    assert list(exercise(total, spec=spec))


def test_exercise_element_spec_not_constrained_fail():
    def total(xs: list[int]) -> int:
        return sum(xs)

    spec: Spec = {"args": {"xs": is_list_of_p(is_str_p)}, "ret": is_int_p}

    with pytest.raises(InvalidSpecError, match="Spec predicate is not a constrained annotation"):
        list(exercise(total, spec=spec))


def test_exercise_var_keyword_annotation():
    def total(**kwargs: int) -> int:
        return sum(kwargs.values())

    assert list(exercise(total, n=3))


def _callee(text: str, *, end: str = "\n") -> str:
    return text + end


def test_exercise_var_keyword_defaults_to_no_keywords():
    # #306: **kwargs is usually forwarded to a callee that only takes a few keywords, so random names fail
    def proxy(text: str, **kwargs: Any) -> str:
        return _callee(text, **kwargs)

    calls = list(exercise(proxy, n=5))

    assert len(calls) == 5
    assert all(args[-1] == {} for args, _ in calls)


def test_exercise_var_keyword_named_in_spec():
    def total(**kwargs: int) -> int:
        return sum(kwargs.values())

    spec: Spec = {"args": {"kwargs": is_dict_p & (is_empty_p | is_dict_of_p((is_str_p, is_int_p)))}, "ret": is_int_p}

    assert any(args[-1] for args, _ in exercise(total, spec=spec, n=10))


def test_exercise_var_keyword_narrowed_in_spec():
    def total(**kwargs: int) -> int:
        return sum(kwargs.values())

    spec: Spec = {"args": {"kwargs": is_dict_p & is_empty_p}, "ret": is_int_p}

    assert len(list(exercise(total, spec=spec, n=5))) == 5


def _width(s: slice) -> int:
    return len(range(100)[s])


def _year(t: time.struct_time) -> str:
    return time.strftime("%Y", t)


def _offset(tz: datetime.tzinfo) -> datetime.timedelta | None:
    return datetime.datetime(2024, 1, 1, tzinfo=tz).utcoffset()


def _exception_name(e: BaseException) -> str:
    return type(e).__name__


def _code_name(c: types.CodeType) -> str:
    return c.co_name


def _ref_name(ref: ForwardRef) -> str:
    return ref.__forward_arg__


def _length(r: range) -> int:
    return len(r)


def _dump(node: ast.AST) -> str:
    return ast.dump(node)


def _signature_args(node: ast.FunctionDef) -> int:
    return len(node.args.args)


def _message(record: logging.LogRecord) -> str:
    return record.getMessage()


def _is_running(loop: asyncio.AbstractEventLoop) -> bool:
    return loop.is_running()


@pytest.mark.parametrize(
    "f",
    [
        _width,
        _year,
        _offset,
        _exception_name,
        _code_name,
        _ref_name,
        _length,
        _dump,
        _signature_args,
        _message,
        _is_running,
    ],
)
def test_exercise_stdlib_annotations(f):
    assert len(list(exercise(f, n=5))) == 5


def test_exercise_unannotated_var_args():
    def f(x: int, *args, **kwargs) -> int:
        assert args == ()
        assert kwargs == {}
        return x

    assert len(list(exercise(f, n=3))) == 3


def _snake(name: str, _pattern: re.Pattern[str] = re.compile("[a-z][A-Z]")) -> str:
    return _pattern.sub(lambda match: f"{match[0][0]}_{match[0][1]}", name)


def test_exercise_skips_private_parameters_with_default():
    values = list(exercise(_snake, n=5))

    assert len(values) == 5
    assert all(len(args) == 1 for args, _ in values)  # only `name` is generated


def test_exercise_generates_private_parameter_without_default():
    def private(_x: int) -> int:
        return _x

    assert all(args for args, _ in exercise(private, n=3))
