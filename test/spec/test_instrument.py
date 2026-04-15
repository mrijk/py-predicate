import asyncio
from typing import Any

import pytest

from predicate import Spec, ge_p, is_int_p
from predicate.spec.instrument import enrich_spec, instrument, instrument_function


def test_instrument_ok():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    max_int_with_bug(4, 3)


def test_instrument_wrong_parameter():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(ValueError) as exc:
        max_int_with_bug(4, False)
    assert (
        exc.value.args[0]
        == "Parameter predicate for function max_int_with_bug failed. Reason: False is not an instance of type int"
    )


def test_instrument_return_fails():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(ValueError) as exc:
        max_int_with_bug(3, 4)
    assert (
        exc.value.args[0]
        == "Return predicate for function max_int_with_bug failed. Reason: 4 is not an instance of type int"
    )


def test_instrument_using_func():
    from spec.test_functions.uses_max_int_with_bug import uses_max_int_with_bug

    with pytest.raises(ValueError) as exc:
        uses_max_int_with_bug(3, 13)
    assert (
        exc.value.args[0]
        == "Return predicate for function max_int_with_bug failed. Reason: 13 is not an instance of type int"
    )


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

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    def func_with_side_effect(x: int) -> int:
        side_effect.append(x)
        return x

    with pytest.raises(ValueError):
        func_with_side_effect("not-an-int")

    assert side_effect == [], "function body must not execute when args are invalid"


def test_instrument_optional_ret():
    # spec without "ret" must not raise KeyError
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def add_one(x: int) -> int:
        return x + 1

    assert add_one(4) == 5


def test_instrument_fn_constraint_ok():
    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    @instrument(spec)
    def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    assert max_int(3, 7) == 7


def test_instrument_fn_constraint_fails():
    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    @instrument(spec)
    def broken_max(x: int, y: int) -> int:
        return x  # always returns x, violates fn when y > x

    with pytest.raises(ValueError, match="fn constraint for function broken_max failed"):
        broken_max(3, 7)


def test_instrument_fn_p_constraint_ok():
    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn_p": lambda x, y: ge_p(x + y),
    }

    @instrument(spec)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5


def test_instrument_fn_p_constraint_fails():
    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn_p": lambda x, y: ge_p(x + y),
    }

    @instrument(spec)
    def bad_add(x: int, y: int) -> int:
        return x  # returns x instead of x+y

    with pytest.raises(ValueError, match="fn_p constraint for function bad_add failed"):
        bad_add(2, 3)


def test_instrument_decorator():
    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5

    with pytest.raises(ValueError, match="Parameter predicate for function add failed"):
        add("not-an-int", 3)


def test_instrument_async_ok():
    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    async def async_add(x: int, y: int) -> int:
        return x + y

    assert asyncio.run(async_add(2, 3)) == 5


def test_instrument_async_wrong_parameter():
    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    async def async_add(x: int, y: int) -> int:
        return x + y

    with pytest.raises(ValueError, match="Parameter predicate for function async_add failed"):
        asyncio.run(async_add("not-an-int", 3))


def test_instrument_async_return_fails():
    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    async def async_bad(x: int, y: int) -> int:
        return "oops"  # type: ignore

    with pytest.raises(ValueError, match="Return predicate for function async_bad failed"):
        asyncio.run(async_bad(2, 3))


def test_enrich_spec_fills_args_from_annotation():
    def add(x: int, y: int) -> int:
        return x + y

    spec: Spec = {"args": {}}
    enriched = enrich_spec(add, spec)
    assert "x" in enriched["args"]
    assert "y" in enriched["args"]


def test_enrich_spec_keeps_existing_args():
    def add(x: int, y: int) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p}}
    enriched = enrich_spec(add, spec)
    assert enriched["args"]["x"] is is_int_p
    assert "y" in enriched["args"]


def test_instrument_enriches_args_from_annotation():
    spec: Spec = {"args": {}}

    @instrument(spec)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5

    with pytest.raises(ValueError, match="Parameter predicate for function add failed"):
        add("not-an-int", 3)


def test_enrich_spec_fills_ret_from_annotation():
    def add(x: int, y: int) -> int:
        return x + y

    spec: dict = {"args": {"x": is_int_p, "y": is_int_p}}
    enriched = enrich_spec(add, spec)
    assert "ret" in enriched


def test_enrich_spec_keeps_existing_ret():
    def add(x: int, y: int) -> int:
        return x + y

    spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}
    enriched = enrich_spec(add, spec)
    assert enriched["ret"] is is_int_p


def test_enrich_spec_no_annotation_leaves_spec_unchanged():
    def add(x, y):
        return x + y

    spec: dict = {"args": {}}
    enriched = enrich_spec(add, spec)
    assert "ret" not in enriched


def test_instrument_enriches_ret_from_annotation():
    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}}

    @instrument(spec)
    def bad_add(x: int, y: int) -> int:
        return "oops"  # type: ignore

    with pytest.raises(ValueError, match="Return predicate for function bad_add failed"):
        bad_add(2, 3)


def test_instrument_union_return_type_ok():
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> int | str:
        return "hello"

    assert f(1) == "hello"


def test_instrument_union_return_type_fails():
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> int | str:
        return 3.14  # type: ignore

    with pytest.raises(ValueError, match="Return predicate for function f failed"):
        f(1)


def test_instrument_none_return_type_ok():
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> None:
        pass

    assert f(1) is None


def test_instrument_none_return_type_fails():
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> None:
        return 42  # type: ignore

    with pytest.raises(ValueError, match="Return predicate for function f failed"):
        f(1)


def test_instrument_any_return_type():
    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> Any:
        return "anything"

    assert f(1) == "anything"


def test_instrument_literal_return_type_ok():
    from typing import Literal

    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> Literal[1, 2, 3]:
        return 2  # type: ignore

    assert f(1) == 2


def test_instrument_literal_return_type_fails():
    from typing import Literal

    spec: Spec = {"args": {"x": is_int_p}}

    @instrument(spec)
    def f(x: int) -> Literal[1, 2, 3]:
        return 4  # type: ignore

    with pytest.raises(ValueError, match="Return predicate for function f failed"):
        f(1)
