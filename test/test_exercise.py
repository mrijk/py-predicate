import pytest

from predicate import is_int_p
from predicate.exercise import Spec, exercise


def test_exercise_happy():
    def adder(x, y):
        return x + y

    spec: Spec = {"parameters": {"x": is_int_p, "y": is_int_p}, "returns": is_int_p}

    result = list(exercise(adder, spec=spec))
    assert result


def test_exercise_missing_unannotated_parameter_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {  # type: ignore
        "parameters": {"x": is_int_p, "y": is_int_p},
    }

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Return annotation not in spec"


def test_exercise_missing_return_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {
        "parameters": {
            "x": is_int_p,
        },
        "returns": is_int_p,
    }

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Unannotated parameter 'y' not in spec"


def test_exercise_wrong_parameter_name():
    def adder(x, y):
        return x + y

    spec: Spec = {"parameters": {"x": is_int_p, "z": is_int_p}, "returns": is_int_p}

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Parameter 'z' not in function signature"


def test_exercise_wrong_return():
    def adder(x, y):
        return None  # Not an int!

    spec: Spec = {
        "parameters": {
            "x": is_int_p,
            "y": is_int_p,
        },
        "returns": is_int_p,
    }

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Not conform spec: {'result': False, 'reason': 'None is not an instance of type int'}"


def test_exercise_without_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    result = list(exercise(adder))
    assert result
