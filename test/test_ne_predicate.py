from predicate import ne_p
from predicate.explain import explain


def test_ne_p_int():
    ne_2 = ne_p(2)

    assert not ne_2(2)
    assert ne_2(1)


def test_ne_p_str():
    ne_foo = ne_p("foo")

    assert not ne_foo("foo")
    assert ne_foo("bar")


def test_eq_explain():
    predicate = ne_p("foo")

    expected = {"reason": "foo is equal to foo", "result": False}
    assert explain(predicate, "foo") == expected
