from collections import OrderedDict
from datetime import date, datetime, time, timedelta
from pathlib import Path, PurePosixPath, PureWindowsPath

import pytest

from predicate import (
    is_bytes_p,
    is_date_p,
    is_frozenset_p,
    is_mapping_p,
    is_number_p,
    is_path_p,
    is_sequence_p,
    is_time_p,
    is_timedelta_p,
)

# is_bytes_p


@pytest.mark.parametrize("value", [b"hello", b"", bytes(4)])
def test_is_bytes_p_true(value):
    assert is_bytes_p(value)


@pytest.mark.parametrize("value", ["hello", bytearray(b"hello"), 42, None])
def test_is_bytes_p_false(value):
    assert not is_bytes_p(value)


# is_frozenset_p


@pytest.mark.parametrize("value", [frozenset(), frozenset({1, 2, 3})])
def test_is_frozenset_p_true(value):
    assert is_frozenset_p(value)


@pytest.mark.parametrize("value", [{1, 2}, [1, 2], (1, 2), None])
def test_is_frozenset_p_false(value):
    assert not is_frozenset_p(value)


# is_date_p


@pytest.mark.parametrize("value", [date.today(), date(2024, 1, 1), datetime.now()])
def test_is_date_p_true(value):
    # datetime is a subclass of date
    assert is_date_p(value)


@pytest.mark.parametrize("value", ["2024-01-01", 20240101, None, time(12, 0)])
def test_is_date_p_false(value):
    assert not is_date_p(value)


# is_time_p


@pytest.mark.parametrize("value", [time(0, 0), time(12, 30, 45), time(23, 59, 59, 999999)])
def test_is_time_p_true(value):
    assert is_time_p(value)


@pytest.mark.parametrize("value", [datetime.now(), "12:00", 1200, None])
def test_is_time_p_false(value):
    assert not is_time_p(value)


# is_timedelta_p


@pytest.mark.parametrize("value", [timedelta(), timedelta(days=1), timedelta(seconds=3600), timedelta(weeks=2)])
def test_is_timedelta_p_true(value):
    assert is_timedelta_p(value)


@pytest.mark.parametrize("value", [1, 3600.0, "1 day", None])
def test_is_timedelta_p_false(value):
    assert not is_timedelta_p(value)


# is_path_p


@pytest.mark.parametrize(
    "value",
    [Path("/tmp"), Path("."), Path("a/b/c"), PurePosixPath("/etc"), PureWindowsPath("C:/Windows")],  # noqa: S108
)
def test_is_path_p_true(value):
    assert is_path_p(value)


@pytest.mark.parametrize("value", ["/tmp", b"/tmp", None, 42])  # noqa: S108
def test_is_path_p_false(value):
    assert not is_path_p(value)


# is_mapping_p


@pytest.mark.parametrize("value", [{}, {"a": 1}, OrderedDict()])
def test_is_mapping_p_true(value):
    assert is_mapping_p(value)


@pytest.mark.parametrize("value", [[("a", 1)], {1, 2}, "dict", None])
def test_is_mapping_p_false(value):
    assert not is_mapping_p(value)


# is_sequence_p


@pytest.mark.parametrize("value", [[], [1, 2], (1, 2), "hello", b"bytes", range(5)])
def test_is_sequence_p_true(value):
    assert is_sequence_p(value)


@pytest.mark.parametrize("value", [{1, 2}, {}, None, 42])
def test_is_sequence_p_false(value):
    assert not is_sequence_p(value)


# is_number_p


@pytest.mark.parametrize("value", [0, 1, -1, 3.14, -2.7, 1 + 2j, 0.0])
def test_is_number_p_true(value):
    assert is_number_p(value)


@pytest.mark.parametrize("value", [True, False, "1", None, [1]])
def test_is_number_p_false(value):
    assert not is_number_p(value)
