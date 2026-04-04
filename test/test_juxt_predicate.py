from predicate import all_p, count_p, eq_p, exactly_one_p, explain, is_int_p, is_str_p, juxt_p


def test_juxt():
    p1 = is_int_p
    p2 = is_str_p
    p3 = eq_p(2)
    p4 = eq_p("foo")
    two_true = count_p(predicate=eq_p(True), length_p=eq_p(2))

    predicate = juxt_p(p1, p2, p3, p4, evaluate=two_true)

    assert predicate(2)
    assert predicate("foo")
    assert not predicate(1)
    assert not predicate("bar")


def test_juxt_repr():
    predicate = juxt_p(is_int_p, is_str_p, evaluate=exactly_one_p(predicate=eq_p(True)))
    assert repr(predicate).startswith("juxt_p(")


def test_juxt_explain():
    p1 = is_int_p
    p2 = is_str_p
    p3 = eq_p(2)
    p4 = eq_p("foo")
    two_true = count_p(predicate=eq_p(True), length_p=eq_p(2))

    predicate = juxt_p(p1, p2, p3, p4, evaluate=two_true)

    result = explain(predicate, 3)

    assert result == {
        "result": False,
        "results": [True, False, False, False],
        "evaluate": {"result": False, "reason": "Expected count eq_p(2), actual: 1"},
    }


def test_juxt_iterables():
    all_int = all_p(is_int_p)
    three_zeros = count_p(predicate=eq_p(0), length_p=eq_p(3))
    one_true = exactly_one_p(predicate=eq_p(True))

    predicate = juxt_p(all_int, three_zeros, evaluate=one_true)

    assert predicate([1, 2, 3, 4])
    assert predicate([1, 0, 2, 0, 3])

    assert not predicate([1, 0, 2, 0, 3, 0])
