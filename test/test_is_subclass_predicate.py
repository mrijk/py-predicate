import pytest

from predicate import explain, is_subclass_p


@pytest.mark.skip
def test_is_subclass_p_ok():
    predicate = is_subclass_p(object)

    assert predicate(int)


@pytest.mark.skip
def test_is_subclass_p_tuple():
    predicate = is_subclass_p((int, str))

    assert predicate(int)
    assert predicate(str)


@pytest.mark.skip
def test_is_subclass_p_fail():
    predicate = is_subclass_p(int)

    assert not predicate(str)


@pytest.mark.skip
def test_is_subclass_p_fail_tuple():
    predicate = is_subclass_p((int, str))

    assert not predicate(float)


@pytest.mark.skip
def test_is_subclass_p_tuple_explain():
    predicate = is_subclass_p((int, str))

    expected = {"reason": "<class 'float'> is not a subclass of type int or str", "result": False}

    assert explain(predicate, float) == expected


@pytest.mark.skip
def test_is_subclass_p_explain():
    predicate = is_subclass_p(int)

    expected = {"reason": "<class 'str'> is not a subclass of type int", "result": False}

    assert explain(predicate, str) == expected


@pytest.mark.parametrize(
    "parameter, expected",
    [
        (int, "is_int_p"),
        ((int, str), "is_subclass_p((int, str))"),
        (int | str, "is_subclass_p(int|str)"),
    ],
)
@pytest.mark.skip
def test_repr_enum(parameter, expected):
    predicate = is_subclass_p(parameter)

    assert repr(predicate) == expected


@pytest.mark.skip
def test_is_subclass_klass():
    assert is_subclass_p(int).klass is int
