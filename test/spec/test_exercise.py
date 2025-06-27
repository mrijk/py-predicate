import pytest

from predicate import ge_p, is_int_p, is_str_p, pos_p
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


def test_exercise_without_spec():
    def adder(x: int, y: int) -> int:
        return x + y

    result = list(exercise(adder))
    assert result
