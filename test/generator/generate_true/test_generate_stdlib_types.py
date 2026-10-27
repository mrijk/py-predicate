import os
from datetime import date, datetime, time, timedelta
from pathlib import Path, PurePath, PureWindowsPath

import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import generate_true, is_instance_p


@pytest.mark.parametrize(
    "klass", [bytes, bytearray, date, time, timedelta, PurePath, Path, PureWindowsPath, os.PathLike]
)
def test_generate_stdlib_type(klass):
    assert_generated_true(is_instance_p(klass))


def test_generate_date_is_not_datetime():
    assert not any(isinstance(value, datetime) for value in take(50, generate_true(is_instance_p(date))))


def test_generate_path_keeps_class():
    assert all(type(value) is PureWindowsPath for value in take(20, generate_true(is_instance_p(PureWindowsPath))))


def test_generate_edge_cases():
    assert b"" in take(300, generate_true(is_instance_p(bytes)))
    assert timedelta(0) in take(5, generate_true(is_instance_p(timedelta)))
    assert PurePath() in take(300, generate_true(is_instance_p(PurePath)))
