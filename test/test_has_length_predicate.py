from predicate import eq_p, has_length_p
from predicate.explain import explain


def test_has_length():
    of_length_1 = has_length_p(eq_p(1))

    assert of_length_1([1])
    assert of_length_1("f")


def test_has_length_false():
    of_length_1 = has_length_p(eq_p(1))

    assert not of_length_1([])
    assert not of_length_1({2, 3})
    assert not of_length_1("foobar")


def test_has_length_explain():
    predicate = has_length_p(eq_p(1))

    expected = {"reason": "Expected length eq_p(1), actual: 3", "result": False}
    assert explain(predicate, {1, 2, 3}) == expected
