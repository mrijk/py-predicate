import pytest

from predicate import not_in_p


class Contains13:
    def __contains__(self, item):
        return item == 13


def test_not_in_p():
    not_in_123 = not_in_p(["1", "2", "3"])

    assert not_in_123("0")
    assert not not_in_123("1")


@pytest.mark.parametrize(
    "parameter, expected",
    [
        ([2, 3, 4], "not_in_p(2, 3, 4)"),
        (Contains13(), "not_in_p(Contains13())"),
    ],
)
def test_repr_in_p(parameter, expected):
    predicate = not_in_p(parameter)
    assert repr(predicate) == expected
