from predicate import explain
from predicate.standard_predicates import eq_p, has_path_p, is_int_p


def test_has_path_predicate():
    has_x = eq_p("x")
    predicate = has_path_p(has_x)

    assert not predicate({})
    assert not predicate({"y": 13})
    assert predicate({"x": 13})


def test_has_path_predicate_with_value():
    has_x = eq_p("x")
    predicate = has_path_p(has_x, is_int_p)

    assert not predicate({})
    assert not predicate({"y": 13})
    assert not predicate({"x": "foo"})
    assert predicate({"x": 13})


def test_has_path_predicate_nested():
    has_x = eq_p("x")
    has_y = eq_p("y")
    y_is_13 = eq_p(13)
    predicate = has_path_p(has_x, has_y, y_is_13)

    assert not predicate({"y": 13})
    assert not predicate({"x": {"y": 42}})
    assert predicate({"x": {"y": 13}})


def test_has_path_predicate_with_list():
    has_x = eq_p("x")
    predicate = has_path_p(has_x)

    assert predicate({"x": [{"y": 13}]})


def test_has_path_predicate_no_dict():
    predicate = has_path_p()

    assert not predicate("foo")


def test_has_path_predicate_no_dict_explain():
    predicate = has_path_p()

    expected = {"reason": "Value foo is not a dict", "result": False}
    assert explain(predicate, "foo") == expected
