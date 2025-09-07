import pytest

from predicate import in_p


class Contains13:
    def __contains__(self, item):
        return item == 13


def test_in_p():
    in_123 = in_p(["1", "2", "3"])

    assert in_123("1")
    assert not in_123("0")


def test_in_p_with_class():
    p = in_p(Contains13())

    assert p(13)
    assert not p(1)


def test_in_p_eq():
    p = in_p({"1", "2", "3"})
    q = in_p({"1", "2", "3"})

    assert p == q


def test_in_p_ne():
    p = in_p({"1", "2", "3"})
    q = in_p({"1", "2"})

    assert p != q


@pytest.mark.parametrize(
    "parameter, expected",
    [
        ([2, 3, 4], "in_p(2, 3, 4)"),
        (Contains13(), "in_p(Contains13())"),
    ],
)
def test_repr_in_p(parameter, expected):
    predicate = in_p(parameter)
    assert repr(predicate) == expected
