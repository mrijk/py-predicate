from typing import TypeVar

import pytest

from predicate import ge_p, is_int_p, is_str_p, pos_p
from predicate.spec.exercise import Spec, exercise


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

    with pytest.raises(AssertionError) as exc:
        list(exercise(max_int, spec=spec, n=100))

    assert exc.value.args[0].startswith("Not conform spec: fn constraint failed for inputs")


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

    with pytest.raises(AssertionError) as exc:
        list(exercise(max_int, spec=spec, n=100))

    assert exc.value.args[0].startswith("Not conform spec:")


def test_exercise_missing_return_annotation_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {  # type: ignore
        "args": {"x": is_int_p, "y": is_int_p},
    }

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Return annotation not in spec"


def test_exercise_no_types_defined():
    def dup(x):
        return x

    with pytest.raises(ValueError, match="Not implemented yet"):
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

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Unannotated parameter 'y' not in spec"


def test_exercise_wrong_parameter_name():
    def adder(x, y):
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "z": is_int_p}, "ret": is_int_p}

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Parameter 'z' not in function signature"


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

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Not conform spec: {'result': False, 'reason': 'None is not an instance of type int'}"


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

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Spec predicate is not a constrained annotation"


def test_exercise_annotated_without_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    result = list(exercise(adder))
    assert result


def test_exercise_partially_annotate_without_specd():
    def adder(x: int, y) -> int:
        return x + y

    with pytest.raises(ValueError, match="Not implemented yet"):
        list(exercise(adder))


def test_exercise_infer_ret_from_annotation():
    def adder(x, y) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}}  # type: ignore[typeddict-item]

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

    with pytest.raises(AssertionError):
        async for _ in exercise(adder):
            pass


@pytest.mark.asyncio
async def test_exercise_async_function_no_annotation():
    async def dup(x):
        return x

    with pytest.raises(ValueError, match="Not implemented yet"):
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

    with pytest.raises(AssertionError) as exc:
        async for _ in exercise(max_int, spec=spec, n=100):
            pass
    assert exc.value.args[0].startswith("Not conform spec: fn constraint failed for inputs")


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
    with pytest.raises(AssertionError, match="not in spec"):
        list(exercise(identity, spec=spec))


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_p_fail():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y - 1  # wrong

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    with pytest.raises(AssertionError) as exc:
        async for _ in exercise(max_int, spec=spec, n=100):
            pass
    assert exc.value.args[0].startswith("Not conform spec:")
