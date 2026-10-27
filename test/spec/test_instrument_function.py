import asyncio
from typing import Any

import pytest

from predicate import ge_p, is_instrumented, is_int_p
from predicate.spec.instrument import enrich_spec, instrument, instrument_function, instrument_module
from predicate.spec.spec import InvalidSpecError, Spec, SpecViolationError


def test_instrument_ok():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    max_int_with_bug(4, 3)


def test_instrument_wrong_parameter():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(
        SpecViolationError,
        match="Parameter predicate for function max_int_with_bug failed. Reason: False is not an instance of type int",
    ):
        max_int_with_bug(4, False)


def test_instrument_return_fails():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(
        SpecViolationError,
        match="Return predicate for function max_int_with_bug failed. Reason: 4 is not an instance of type int",
    ):
        max_int_with_bug(3, 4)


def test_instrument_using_func():
    from spec.test_functions.uses_max_int_with_bug import uses_max_int_with_bug

    with pytest.raises(
        SpecViolationError,
        match="Return predicate for function max_int_with_bug failed. Reason: 13 is not an instance of type int",
    ):
        uses_max_int_with_bug(3, 13)


def test_instrument_function_not_at_module_level():
    # local function is not a module-level attribute → hits the else/pass branch
    def local_func(x: int) -> int:
        return x

    spec = {"args": {"x": is_int_p}, "ret": is_int_p}
    wrapped = instrument_function(local_func, spec)
    assert wrapped(3) == 3


def test_instrument_validates_args_before_executing():
    # side_effect is set only if the function body runs
    side_effect = []

    @instrument
    def func_with_side_effect(x: int) -> int:
        side_effect.append(x)
        return x

    with pytest.raises(SpecViolationError):
        func_with_side_effect("not-an-int")

    assert side_effect == [], "function body must not execute when args are invalid"


def test_instrument_optional_ret():
    @instrument
    def add_one(x: int) -> int:
        return x + 1

    assert add_one(4) == 5


def test_instrument_fn_constraint_ok():
    @instrument({"args": {}, "fn": lambda x, y, ret: ret >= x and ret >= y})
    def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    assert max_int(3, 7) == 7


def test_instrument_fn_constraint_fails():
    @instrument({"args": {}, "fn": lambda x, y, ret: ret >= x and ret >= y})
    def broken_max(x: int, y: int) -> int:
        return x  # always returns x, violates fn when y > x

    with pytest.raises(SpecViolationError, match="fn constraint for function broken_max failed"):
        broken_max(3, 7)


def test_instrument_fn_p_constraint_ok():
    @instrument({"args": {}, "fn_p": lambda x, y: ge_p(x + y)})
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5


def test_instrument_fn_p_constraint_fails():
    @instrument({"args": {}, "fn_p": lambda x, y: ge_p(x + y)})
    def bad_add(x: int, y: int) -> int:
        return x  # returns x instead of x+y

    with pytest.raises(SpecViolationError, match="fn_p constraint for function bad_add failed"):
        bad_add(2, 3)


def test_instrument_pre_ok():
    @instrument({"args": {}, "pre": lambda lo, hi: lo <= hi})
    def make_range(lo: int, hi: int) -> range:
        return range(lo, hi)

    assert make_range(1, 3) == range(1, 3)


def test_instrument_pre_fails_before_call():
    calls = []

    @instrument({"args": {}, "pre": lambda lo, hi: lo <= hi})
    def make_range(lo: int, hi: int) -> range:
        calls.append((lo, hi))
        return range(lo, hi)

    with pytest.raises(SpecViolationError, match="pre condition for function make_range failed. Arguments: lo=3, hi=1"):
        make_range(3, 1)
    assert calls == []


def test_instrument_decorator():
    @instrument
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5

    with pytest.raises(SpecViolationError, match="Parameter predicate for function add failed"):
        add("not-an-int", 3)


def test_instrument_async_ok():
    @instrument
    async def async_add(x: int, y: int) -> int:
        return x + y

    assert asyncio.run(async_add(2, 3)) == 5


def test_instrument_async_wrong_parameter():
    @instrument
    async def async_add(x: int, y: int) -> int:
        return x + y

    with pytest.raises(SpecViolationError, match="Parameter predicate for function async_add failed"):
        asyncio.run(async_add("not-an-int", 3))


def test_instrument_async_return_fails():
    @instrument
    async def async_bad(x: int, y: int) -> int:
        return "oops"  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function async_bad failed"):
        asyncio.run(async_bad(2, 3))


def test_instrument_on_error_called_for_invalid_arg():
    errors = []

    @instrument(on_error=errors.append)
    def f(x: int) -> int:
        return 0

    result = f("oops")

    assert len(errors) == 1
    assert "Parameter predicate" in errors[0]
    assert result == 0


def test_instrument_on_error_called_for_invalid_return():
    errors = []

    @instrument(on_error=errors.append)
    def f(x: int) -> int:
        return "oops"  # type: ignore

    result = f(1)

    assert len(errors) == 1
    assert "Return predicate" in errors[0]
    assert result == "oops"


def test_instrument_on_error_with_spec():
    errors = []

    @instrument({"args": {}, "fn": lambda x, y, ret: ret >= x and ret >= y}, on_error=errors.append)
    def broken_max(x: int, y: int) -> int:
        return x

    result = broken_max(3, 7)

    assert len(errors) == 1
    assert "fn constraint" in errors[0]
    assert result == 3


def test_enrich_spec_fills_args_from_annotation() -> None:
    def add(x: int, y: int) -> int:
        return x + y

    spec: Spec = {"args": {}}
    enriched = enrich_spec(add, spec)
    assert "x" in enriched["args"]
    assert "y" in enriched["args"]


def test_enrich_spec_keeps_existing_args() -> None:
    def add(x: int, y: int) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p}}
    enriched = enrich_spec(add, spec)
    assert enriched["args"]["x"] is is_int_p
    assert "y" in enriched["args"]


def test_instrument_enriches_args_from_annotation() -> None:
    spec: Spec = {"args": {}}

    @instrument(spec)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5

    with pytest.raises(SpecViolationError, match="Parameter predicate for function add failed"):
        add("not-an-int", 3)


def test_enrich_spec_fills_ret_from_annotation() -> None:
    def add(x: int, y: int) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}}
    enriched = enrich_spec(add, spec)
    assert "ret" in enriched


def test_enrich_spec_keeps_existing_ret():
    def add(x: int, y: int) -> int:
        return x + y

    spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}
    enriched = enrich_spec(add, spec)
    assert enriched["ret"] is is_int_p


def test_enrich_spec_no_annotation_leaves_spec_unchanged() -> None:
    def add(x, y):
        return x + y

    spec: Spec = {"args": {}}
    enriched = enrich_spec(add, spec)
    assert "ret" not in enriched


def test_instrument_enriches_ret_from_annotation():
    @instrument
    def bad_add(x: int, y: int) -> int:
        return "oops"  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function bad_add failed"):
        bad_add(2, 3)


def test_instrument_union_return_type_ok():
    @instrument
    def f(x: int) -> int | str:
        return "hello"

    assert f(1) == "hello"


def test_instrument_union_return_type_fails():
    @instrument
    def f(x: int) -> int | str:
        return 3.14  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f(1)


def test_instrument_none_return_type_ok():
    @instrument
    def f(x: int) -> None:
        pass

    assert f(1) is None


def test_instrument_none_return_type_fails():
    @instrument
    def f(x: int) -> None:
        return 42  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f(1)


def test_instrument_any_return_type():
    @instrument
    def f(x: int) -> Any:
        return "anything"

    assert f(1) == "anything"


def test_instrument_literal_return_type_ok():
    from typing import Literal

    @instrument
    def f(x: int) -> Literal[1, 2, 3]:
        return 2  # type: ignore

    assert f(1) == 2


def test_instrument_literal_return_type_fails():
    from typing import Literal

    @instrument
    def f(x: int) -> Literal[1, 2, 3]:
        return 4  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f(1)


def test_instrument_list_return_type_ok():
    @instrument
    def f() -> list[int]:
        return [1, 2, 3]

    assert f() == [1, 2, 3]


def test_instrument_list_return_type_fails():
    @instrument
    def f() -> list[int]:
        return [1, "oops", 3]  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f()


def test_instrument_dict_return_type_ok():
    @instrument
    def f() -> dict[str, int]:
        return {"a": 1}

    assert f() == {"a": 1}


def test_instrument_dict_return_type_fails():
    @instrument
    def f() -> dict[str, int]:
        return {"a": "oops"}  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f()


def test_instrument_tuple_return_type_ok():
    @instrument
    def f() -> tuple[int, str]:
        return (1, "hello")

    assert f() == (1, "hello")


def test_instrument_tuple_return_type_fails():
    @instrument
    def f() -> tuple[int, str]:
        return (1, 2)  # type: ignore

    with pytest.raises(SpecViolationError, match="Return predicate for function f failed"):
        f()


def _fresh_sample_module():
    import importlib

    import spec.test_functions.sample_module as sample_module

    importlib.reload(sample_module)
    return sample_module


def test_instrument_module_instruments_all_annotated_functions():
    sample_module = _fresh_sample_module()
    instrument_module(sample_module)

    assert sample_module.add(2, 3) == 5
    assert sample_module.greet("world") == "Hello, world"

    with pytest.raises(SpecViolationError, match="Parameter predicate for function add failed"):
        sample_module.add("oops", 3)

    with pytest.raises(SpecViolationError, match="Parameter predicate for function greet failed"):
        sample_module.greet(42)


def test_instrument_module_with_pattern():
    sample_module = _fresh_sample_module()
    instrument_module(sample_module, pattern="gr*")

    assert sample_module.add(2, 3) == 5  # not instrumented, no check

    with pytest.raises(SpecViolationError, match="Parameter predicate for function greet failed"):
        sample_module.greet(42)


def test_instrument_module_skips_unannotated_functions():
    sample_module = _fresh_sample_module()
    instrument_module(sample_module)

    # no_annotations has no type hints, so passes anything
    assert sample_module.no_annotations("a", "b") == "ab"


def test_instrument_module_with_on_error():
    sample_module = _fresh_sample_module()
    errors = []
    instrument_module(sample_module, on_error=errors.append)

    sample_module.greet(42)

    assert len(errors) == 1
    assert "Parameter predicate for function greet failed" in errors[0]


def test_instrument_raises_expected_exception() -> None:
    spec: Spec = {"args": {}, "raises": ValueError}

    @instrument(spec)
    def f(x: int) -> int:
        raise ValueError("bad input")

    with pytest.raises(ValueError, match="bad input"):
        f(1)


def test_instrument_raises_unexpected_exception() -> None:
    spec: Spec = {"args": {}, "raises": ValueError}

    @instrument(spec)
    def f(x: int) -> int:
        raise TypeError("wrong type")

    with pytest.raises(SpecViolationError, match="Unexpected exception TypeError for function f. Expected: ValueError"):
        f(1)


def test_instrument_raises_no_spec_propagates() -> None:
    @instrument
    def f(x: int) -> int:
        raise RuntimeError("oops")

    with pytest.raises(RuntimeError, match="oops"):
        f(1)


def test_instrument_raises_not_raised_validates_return() -> None:
    spec: Spec = {"args": {}, "raises": ValueError}

    @instrument(spec)
    def f(x: int) -> int:
        return x * 2

    assert f(3) == 6


def test_instrument_raises_unexpected_includes_expected_type() -> None:
    spec: Spec = {"args": {}, "raises": ValueError}

    @instrument(spec)
    def f(x: int) -> int:
        raise TypeError("wrong")

    with pytest.raises(SpecViolationError, match="Expected: ValueError"):
        f(1)


def test_instrument_raises_unexpected_includes_multiple_expected_types() -> None:
    spec: Spec = {"args": {}, "raises": (ValueError, KeyError)}

    @instrument(spec)
    def f(x: int) -> int:
        raise TypeError("wrong")

    with pytest.raises(SpecViolationError, match="Expected: ValueError, KeyError"):
        f(1)


def test_instrument_fn_constraint_error_includes_arguments() -> None:
    @instrument({"args": {}, "fn": lambda x, y, ret: ret >= x and ret >= y})
    def broken_max(x: int, y: int) -> int:
        return x

    with pytest.raises(SpecViolationError, match=r"Arguments: x=3, y=7, ret=3"):
        broken_max(3, 7)


def test_instrument_function_not_double_wrapped() -> None:
    @instrument
    def f(x: int) -> int:
        return x

    wrapped_once = f
    instrument_function(f, {"args": {}})
    assert f is wrapped_once


def test_is_instrumented_true() -> None:
    @instrument
    def f(x: int) -> int:
        return x

    assert is_instrumented(f)


def test_is_instrumented_false() -> None:
    def f(x: int) -> int:
        return x

    assert not is_instrumented(f)


def test_instrument_quoted_annotations():
    @instrument
    def length(x: "str") -> "int":
        return len(x)

    assert length("ab") == 2

    with pytest.raises(SpecViolationError, match="Parameter predicate for function length failed"):
        length(1)


def test_instrument_raises_spec_violation():
    from predicate import SpecViolationError

    @instrument
    def double(x: int) -> int:
        return x * 2

    with pytest.raises(SpecViolationError, match="Parameter predicate for function double failed"):
        double("a")


def test_instrument_function_ret_name():
    @instrument({"args": {}, "fn": lambda x, ret, result: result == x, "ret_name": "result"})
    def r(x: int, ret: int) -> int:
        return ret

    assert r(1, 1) == 1
    with pytest.raises(SpecViolationError, match=r"Arguments: x=1, ret=2, result=2"):
        r(1, 2)


def test_instrument_function_ret_name_clash():
    @instrument({"args": {}, "fn": lambda x, ret: True})
    def r(x: int, ret: int) -> int:
        return x

    with pytest.raises(InvalidSpecError, match="Parameter 'ret' clashes"):
        r(1, 2)


def test_instrument_var_positional():
    @instrument
    def varargs(*args: int) -> int:
        return sum(args)

    assert varargs() == 0
    assert varargs(1, 2) == 3
    with pytest.raises(SpecViolationError, match="x is not an instance of type int"):
        varargs(1, "x")


def test_instrument_var_keyword():
    @instrument
    def varkwargs(**kwargs: int) -> int:
        return sum(kwargs.values())

    assert varkwargs() == 0
    assert varkwargs(a=1, b=2) == 3
    with pytest.raises(SpecViolationError, match="x is not an instance of type int"):
        varkwargs(a=1, b="x")
