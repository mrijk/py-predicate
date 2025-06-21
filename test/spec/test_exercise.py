import pytest

from predicate import is_int_p
from predicate.spec.exercise import Spec, exercise


def test_exercise_happy():
    def adder(x, y):
        return x + y

    spec: Spec = {"args": {"x": is_int_p, "y": is_int_p}, "ret": is_int_p}

    result = list(exercise(adder, spec=spec))
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


def test_exercise_missing_unannotated_parameter_in_spec():
    def adder(x, y):
        return x + y

    spec: Spec = {  # type: ignore
        "args": {"x": is_int_p, "y": is_int_p},
    }

    with pytest.raises(AssertionError) as exc:
        list(exercise(adder, spec=spec))
    assert exc.value.args[0] == "Return annotation not in spec"


def test_exercise_missing_return_in_spec():
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


def test_exercise_without_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    result = list(exercise(adder))
    assert result
