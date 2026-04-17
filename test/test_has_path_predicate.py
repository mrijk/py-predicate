from predicate import eq_p, explain, ge_p, has_path_p, is_str_p
from predicate.standard_predicates import is_int_p, is_list_p


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
    has_y = eq_p("y")
    ge_2 = ge_p(13)

    predicate = has_path_p(has_x, is_list_p, has_y, ge_2)

    assert predicate({"x": [{"y": 13}]})


def test_has_path_predicate_list_first_pred_fails():
    # first_p(list) is False, but individual elements match — result must be False (and, not or)
    predicate = has_path_p(eq_p("x"), is_str_p, is_int_p)
    assert not predicate({"x": [1, 2]})


# def test_has_path_predicate_with_nested_x():
#     has_x = eq_p("x")
#     has_y = eq_p("y")
#     ge_2 = ge_p(13)
#
#     predicate = has_path_p(plus(has_x), has_y, ge_2)
#
#     assert predicate({"x": {"y": 13}})
#     assert predicate({"x": {"x": {"y": 13}}})


def test_has_path_predicate_no_dict():
    predicate = has_path_p()

    assert not predicate("foo")


def test_has_path_predicate_no_dict_explain():
    predicate = has_path_p()

    expected = {"reason": "Value foo is not a Mapping", "result": False}
    assert explain(predicate, "foo") == expected


def test_has_path_predicate_no_match_explain():
    has_x = eq_p("x")
    has_y = eq_p("y")
    y_is_13 = eq_p(13)
    predicate = has_path_p(has_x, has_y, y_is_13)

    expected = {"reason": "No key matching eq_p('x') found at path position 0", "result": False}
    assert explain(predicate, {"y": 13}) == expected


def test_has_path_predicate_non_dict_non_list_intermediate():
    has_x = eq_p("x")
    has_y = eq_p("y")
    y_is_13 = eq_p(13)
    predicate = has_path_p(has_x, has_y, y_is_13)

    # value at "x" is a string (not a dict/list), but path still has 2 elements remaining
    assert not predicate({"x": "not_a_dict"})


def test_has_path_predicate_repr():
    has_x = eq_p("x")
    predicate = has_path_p(has_x)

    assert repr(predicate) == "has_path_p(eq_p('x'))"


def test_has_path_predicate_non_dict_intermediate_explain():
    has_x = eq_p("x")
    has_y = eq_p("y")
    predicate = has_path_p(has_x, has_y)

    expected = {"reason": "Expected a Mapping at path position 1, got int", "result": False}
    assert explain(predicate, {"x": 13}) == expected
