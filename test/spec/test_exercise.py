import pytest

from predicate import ge_p, is_bool_p, is_float_p, is_int_p, is_str_p, pos_p, zero_p
from predicate.spec.exercise import Spec, exercise

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
    assert exc.value.args[0] == "Not conform spec, details tbd"


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
    assert exc.value.args[0] == "Not conform spec, details tbd"


# --- check_signature_against_spec: infer ret from return annotation ---


def test_exercise_infer_ret_from_annotation():
    def adder(x, y) -> int:
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}}  # type: ignore[typeddict-item]

    result = list(exercise(adder, spec=spec))
    assert result


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


def test_exercise_zero_p():
    spec: Spec = {"args": {"x": is_int_p}, "ret": is_bool_p}

    result = list(exercise(zero_p, spec=spec))

    assert result


def test_exercise_pos_p():
    spec: Spec = {"args": {"x": is_int_p | is_float_p}, "ret": is_bool_p}

    result = list(exercise(pos_p, spec=spec))

    assert result


def test_exercise_lambda():
    a_lambda = lambda x: x  # noqa: E731

    spec: Spec = {"args": {"x": is_int_p}, "ret": is_int_p}

    result = list(exercise(a_lambda, spec=spec))

    assert result


def test_exercise_class_with_call():
    class Foo:
        def __call__(self, x: int) -> bool:
            return True

    result = list(exercise(Foo()))

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
        list(exercise(max_int, spec=spec))

    assert exc.value.args[0] == "Not conform spec, details tbd"


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
        list(exercise(max_int, spec=spec))

    assert exc.value.args[0] == "Not conform spec, details tbd"


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
    assert exc.value.args[0] == "Not conform spec, details tbd"


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
    assert exc.value.args[0] == "Not conform spec, details tbd"


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
        async for _ in exercise(max_int, spec=spec):
            pass
    assert exc.value.args[0] == "Not conform spec, details tbd"


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_p():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    result = [r async for r in exercise(max_int, spec=spec)]
    assert result


@pytest.mark.asyncio
async def test_exercise_async_function_with_fn_p_fail():
    async def max_int(x: int, y: int) -> int:
        return x if x >= y else y - 1  # wrong

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p, "fn_p": lambda x, y: ge_p(x) & ge_p(y)}

    with pytest.raises(AssertionError) as exc:
        async for _ in exercise(max_int, spec=spec):
            pass
    assert exc.value.args[0] == "Not conform spec, details tbd"
