from predicate import eq_p
from predicate.explain import explain


def test_eq_p_int():
    eq_2 = eq_p(2)

    assert not eq_2(1)
    assert eq_2(2)


def test_eq_p_str():
    eq_foo = eq_p("foo")

    assert not eq_foo("bar")
    assert eq_foo("foo")


def test_eq_explain():
    predicate = eq_p(2)

    expected = {"reason": "3 is not equal to 2", "result": False}
    assert explain(predicate, 3) == expected
