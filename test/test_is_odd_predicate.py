from predicate import Spec, exercise, is_int_p, is_odd_p


def test_is_odd():
    assert not is_odd_p(0)
    assert is_odd_p(1)


def test_is_odd_exercise():
    spec: Spec = {
        "args": {"x": is_int_p},
    }
    assert list(exercise(is_odd_p, spec))
