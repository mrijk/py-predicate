import pytest

from predicate import ge_p, is_bool_p, is_float_p, is_int_p, pos_p, zero_p
from predicate.spec.exercise import Spec, exercise


def test_exercise_zero_p():
    spec: Spec = {"args": {"x": is_int_p}, "ret": is_bool_p}

    result = list(exercise(zero_p, spec=spec))

    assert result


def test_exercise_pos_p():
    spec: Spec = {"args": {"x": is_int_p | is_float_p}, "ret": is_bool_p}

    result = list(exercise(pos_p, spec=spec))

    assert result


def test_exercise_class_with_call():
    class Foo:
        def __call__(self, x: int) -> bool:
            return True

    result = list(exercise(Foo()))

    assert result


# --- exercise_class: no return annotation → ValueError ---


def test_exercise_class_no_return_annotation():
    class NoReturn:
        def __call__(self, x: int):
            return x

    with pytest.raises(ValueError, match="Not implemented yet"):
        list(exercise(NoReturn()))


# --- exercise_class: *args and **kwargs in __call__ are skipped ---


def test_exercise_class_with_var_positional():
    class VarArgs:
        def __call__(self, *args) -> int:  # unannotated *args is skipped
            return 42

    result = list(exercise(VarArgs()))
    assert result


def test_exercise_class_with_var_keyword():
    class VarKwargs:
        def __call__(self, **kwargs) -> int:  # unannotated **kwargs is skipped
            return 42

    result = list(exercise(VarKwargs()))
    assert result


# --- exercise_class: unannotated non-variadic param → ValueError ---


def test_exercise_class_unannotated_param():
    class BadSig:
        def __call__(self, x) -> int:
            return x

    with pytest.raises(ValueError, match="Not implemented yet"):
        list(exercise(BadSig()))


# --- exercise_class: Predicate used as callable (without spec) ---


def test_exercise_predicate_without_spec():
    result = list(exercise(zero_p))
    assert result


# --- exercise_class: no parameters ---


def test_exercise_class_no_params():
    class Answer:
        def __call__(self) -> int:
            return 42

    result = list(exercise(Answer()))
    assert result


# --- exercise_class: wrong return type ---


def test_exercise_class_wrong_return():
    class BadReturn:
        def __call__(self, x: int) -> int:
            return None  # type: ignore[return-value]

    with pytest.raises(AssertionError):
        list(exercise(BadReturn()))


# --- exercise_class: fn in spec ---


def test_exercise_class_with_fn_happy():
    class Doubler:
        def __call__(self, x: int) -> int:
            return x * 2

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret == x * 2}

    result = list(exercise(Doubler(), spec=spec))
    assert result


def test_exercise_class_with_fn_fail():
    class Doubler:
        def __call__(self, x: int) -> int:
            return x * 3  # wrong

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret == x * 2}

    with pytest.raises(AssertionError) as exc:
        list(exercise(Doubler(), spec=spec))
    assert exc.value.args[0].startswith("Not conform spec: fn constraint failed for inputs")


# --- exercise_class: fn_p in spec ---


def test_exercise_class_with_fn_p_happy():
    class Doubler:
        def __call__(self, x: int) -> int:
            return x * 2

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn_p": lambda x: is_int_p}

    result = list(exercise(Doubler(), spec=spec))
    assert result


def test_exercise_class_with_fn_p_fail():
    class Doubler:
        def __call__(self, x: int) -> int:
            return -abs(x) - 1  # always less than x

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn_p": lambda x: ge_p(x)}

    with pytest.raises(AssertionError) as exc:
        list(exercise(Doubler(), spec=spec))
    assert exc.value.args[0].startswith("Not conform spec:")


@pytest.mark.asyncio
async def test_exercise_async_class_with_call():
    class AsyncAdder:
        async def __call__(self, x: int) -> int:
            return x + 1

    result = [r async for r in exercise(AsyncAdder())]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_class_no_return_annotation():
    class AsyncNoReturn:
        async def __call__(self, x: int):
            return x

    with pytest.raises(ValueError, match="Not implemented yet"):
        async for _ in exercise(AsyncNoReturn()):
            pass


@pytest.mark.asyncio
async def test_exercise_async_class_with_spec():
    class AsyncAdder:
        async def __call__(self, x, y):
            return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    result = [r async for r in exercise(AsyncAdder(), spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_class_no_params():
    class AsyncAnswer:
        async def __call__(self) -> int:
            return 42

    result = [r async for r in exercise(AsyncAnswer())]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_class_wrong_return():
    class AsyncBadReturn:
        async def __call__(self, x: int) -> int:
            return None  # type: ignore[return-value]

    with pytest.raises(AssertionError):
        async for _ in exercise(AsyncBadReturn()):
            pass


@pytest.mark.asyncio
async def test_exercise_async_class_with_fn():
    class AsyncDoubler:
        async def __call__(self, x: int) -> int:
            return x * 2

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret == x * 2}

    result = [r async for r in exercise(AsyncDoubler(), spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_class_with_fn_fail():
    class AsyncDoubler:
        async def __call__(self, x: int) -> int:
            return x * 3  # wrong

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn": lambda x, ret: ret == x * 2}

    with pytest.raises(AssertionError) as exc:
        async for _ in exercise(AsyncDoubler(), spec=spec):
            pass
    assert exc.value.args[0].startswith("Not conform spec: fn constraint failed for inputs")


@pytest.mark.asyncio
async def test_exercise_async_class_with_fn_p():
    class AsyncDoubler:
        async def __call__(self, x: int) -> int:
            return x * 2

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn_p": lambda x: is_int_p}

    result = [r async for r in exercise(AsyncDoubler(), spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_class_with_fn_p_fail():
    class AsyncDoubler:
        async def __call__(self, x: int) -> int:
            return -abs(x) - 1

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p, "fn_p": lambda x: ge_p(x)}

    with pytest.raises(AssertionError) as exc:
        async for _ in exercise(AsyncDoubler(), spec=spec):
            pass
    assert exc.value.args[0].startswith("Not conform spec:")
