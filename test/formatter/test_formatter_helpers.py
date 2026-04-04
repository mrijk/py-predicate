import pytest

from predicate.formatter.helpers import set_to_str


@pytest.mark.parametrize(
    "iterable, expected",
    [
        ([], "{}"),
        ([1], "{1}"),
        ([1, 2, 3], "{1, 2, 3}"),
        (["a", "b"], "{a, b}"),
        ((1, 2), "{1, 2}"),
    ],
)
def test_set_to_str(iterable, expected):
    assert set_to_str(iterable) == expected
