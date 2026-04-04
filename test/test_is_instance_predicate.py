import pytest
from more_itertools import one

from predicate import is_instance_p
from predicate.consumes import consumes
from predicate.explain import explain


def test_is_instance_ok():
    is_str_or_int_p = is_instance_p(str, int)

    assert is_str_or_int_p(3)
    assert is_str_or_int_p("3")


def test_is_instance_fail():
    is_str_or_int_p = is_instance_p(str, int)

    assert not is_str_or_int_p(None)
    assert not is_str_or_int_p([3])


def test_explain_single():
    predicate = is_instance_p(int)
    expected = {"reason": "None is not an instance of type int", "result": False}
    assert explain(predicate, None) == expected


def test_explain():
    predicate = is_instance_p(str, int, float)

    expected = {"reason": "None is not an instance of type str, int or float", "result": False}
    assert explain(predicate, None) == expected


@pytest.mark.parametrize("iterable, expected_end", [([], 0), ([3.14], 0), (["foo"], 1), ([1, 2], 1)])
def test_is_instance_consumes(iterable, expected_end):
    predicate = is_instance_p(str, int)

    end = one(consumes(predicate, iterable))

    assert end == expected_end


def test_is_instance_klass():
    assert is_instance_p(int).klass == (int,)
