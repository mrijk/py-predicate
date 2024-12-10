from predicate import is_instance_p
from predicate.explain import explain


def test_is_instance_p():
    is_str_or_int_p = is_instance_p(str, int)

    assert not is_str_or_int_p(None)
    assert not is_str_or_int_p([3])

    assert is_str_or_int_p(3)
    assert is_str_or_int_p("3")


def test_explain():
    predicate = is_instance_p(str, int)

    expected = {"reason": "None is not an instance of (<class 'str'>, <class 'int'>)", "result": False}
    assert explain(predicate, None) == expected
