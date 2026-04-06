import pytest

from predicate import ge_p, is_int_p
from predicate.spec.instrument import instrument, instrument_function


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

    def func_with_side_effect(x: int) -> int:
        side_effect.append(x)
        return x

    spec = {"args": {"x": is_int_p}, "ret": is_int_p}
    wrapped = instrument_function(func_with_side_effect, spec)

    with pytest.raises(ValueError):
        wrapped("not-an-int")

    assert side_effect == [], "function body must not execute when args are invalid"


def test_instrument_optional_ret():
    # spec without "ret" must not raise KeyError
    def add_one(x: int) -> int:
        return x + 1

    spec = {"args": {"x": is_int_p}}
    wrapped = instrument_function(add_one, spec)
    assert wrapped(4) == 5


def test_instrument_fn_constraint_ok():
    def max_int(x: int, y: int) -> int:
        return x if x >= y else y

    spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }
    wrapped = instrument_function(max_int, spec)
    assert wrapped(3, 7) == 7


def test_instrument_fn_constraint_fails():
    def broken_max(x: int, y: int) -> int:
        return x  # always returns x, violates fn when y > x

    spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }
    wrapped = instrument_function(broken_max, spec)

    with pytest.raises(ValueError, match="fn constraint for function broken_max failed"):
        wrapped(3, 7)


def test_instrument_fn_p_constraint_ok():
    def add(x: int, y: int) -> int:
        return x + y

    spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn_p": lambda x, y: ge_p(x + y),
    }
    wrapped = instrument_function(add, spec)
    assert wrapped(2, 3) == 5


def test_instrument_fn_p_constraint_fails():
    def bad_add(x: int, y: int) -> int:
        return x  # returns x instead of x+y

    spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn_p": lambda x, y: ge_p(x + y),
    }
    wrapped = instrument_function(bad_add, spec)

    with pytest.raises(ValueError, match="fn_p constraint for function bad_add failed"):
        wrapped(2, 3)



def test_instrument_decorator():
    spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    @instrument(spec)
    def add(x: int, y: int) -> int:
        return x + y

    assert add(2, 3) == 5

    with pytest.raises(ValueError, match="Parameter predicate for function add failed"):
        add("not-an-int", 3)
