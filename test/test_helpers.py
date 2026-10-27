import pytest

from predicate import is_int_p
from predicate.helpers import first_false, join_with_or


@pytest.mark.parametrize(
    ("names", "expected"),
    [
        ([], ""),
        (["int"], "int"),
        (["int", "str"], "int or str"),
        (["int", "str", "float"], "int, str or float"),
    ],
)
def test_join_with_or(names, expected):
    assert join_with_or(names) == expected


def test_first_false():
    assert first_false([1, "a", "b"], is_int_p) == "a"


def test_first_false_none_false():
    assert first_false([1, 2], is_int_p) is None
    assert first_false([], is_int_p) is None
