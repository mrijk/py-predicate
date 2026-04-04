import pytest

from predicate import is_int_p
from predicate.spec.instrument import instrument_function


@pytest.mark.skip
def test_instrument_ok():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    max_int_with_bug(4, 3)


@pytest.mark.skip
def test_instrument_wrong_parameter():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(ValueError) as exc:
        max_int_with_bug(4, False)
    assert (
        exc.value.args[0]
        == "Parameter predicate for function max_int_with_bug failed. Reason: False is not an instance of type int"
    )


@pytest.mark.skip
def test_instrument_return_fails():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    with pytest.raises(ValueError) as exc:
        max_int_with_bug(3, 4)
    assert (
        exc.value.args[0]
        == "Return predicate for function max_int_with_bug failed. Reason: 4 is not an instance of type int"
    )


@pytest.mark.skip
def test_instrument_using_func():
    from spec.test_functions.uses_max_int_with_bug import uses_max_int_with_bug

    with pytest.raises(ValueError) as exc:
        uses_max_int_with_bug(3, 13)
    assert (
        exc.value.args[0]
        == "Return predicate for function max_int_with_bug failed. Reason: 13 is not an instance of type int"
    )


@pytest.mark.skip
def test_instrument_function_not_at_module_level():
    # local function is not a module-level attribute → hits the else/pass branch
    def local_func(x: int) -> int:
        return x

    spec = {"args": {"x": is_int_p}, "ret": is_int_p}
    wrapped = instrument_function(local_func, spec)
    assert wrapped(3) == 3
