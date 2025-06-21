import pytest

from predicate import is_int_p
from predicate.spec.instrument import instrument_function
from predicate.spec.spec import Spec


@pytest.fixture(autouse=True)
def instrument_buggy_function():
    from spec.test_functions.max_int_with_bug import max_int_with_bug

    spec: Spec = {
        "args": {"x": is_int_p, "y": is_int_p},
        "ret": is_int_p,
        "fn": lambda x, y, ret: ret >= x and ret >= y,
    }

    instrument_function(max_int_with_bug, spec=spec)


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
