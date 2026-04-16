from helpers import exercise_predicate

from predicate import is_close_p, to_json, to_yaml
from predicate.explain import explain


def test_is_close_default_tolerance():
    predicate = is_close_p(1.0)
    assert predicate(1.0)
    assert predicate(1.0 + 1e-10)
    assert not predicate(1.1)


def test_is_close_rel_tol():
    predicate = is_close_p(100.0, rel_tol=0.01)
    assert predicate(100.0)
    assert predicate(100.5)
    assert not predicate(102.0)


def test_is_close_abs_tol():
    predicate = is_close_p(0.0, abs_tol=1e-6)
    assert predicate(0.0)
    assert predicate(1e-7)
    assert not predicate(1e-5)


def test_is_close_negative():
    predicate = is_close_p(-1.0)
    assert predicate(-1.0)
    assert predicate(-1.0 - 1e-10)
    assert not predicate(-1.1)


def test_is_close_repr():
    predicate = is_close_p(1.0)
    assert repr(predicate) == "is_close_p(1.0, rel_tol=1e-09, abs_tol=0.0)"


def test_is_close_explain():
    predicate = is_close_p(1.0)
    result = explain(predicate, 2.0)
    assert result == {"reason": "2.0 is not close to 1.0", "result": False}


def test_is_close_to_json():
    predicate = is_close_p(1.0, rel_tol=1e-6, abs_tol=0.0)
    assert to_json(predicate) == {"is_close": {"target": 1.0, "rel_tol": 1e-6, "abs_tol": 0.0}}


def test_is_close_to_yaml():
    predicate = is_close_p(1.0)
    result = to_yaml(predicate)
    assert "is_close" in result
    assert "target" in result


def test_is_close_p_default_rel_tol():
    predicate = is_close_p(1.0)
    assert predicate.rel_tol == 1e-9


def test_is_close_p_default_abs_tol():
    predicate = is_close_p(1.0)
    assert predicate.abs_tol == 0.0


def test_is_close_exercise():
    exercise_predicate(is_close_p)
