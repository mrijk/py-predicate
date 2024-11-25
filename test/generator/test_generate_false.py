import uuid
from datetime import datetime

import pytest
from more_itertools import take

from predicate import eq_p, ge_p, generate_false


@pytest.mark.parametrize("value", [2, "foo", "3.14", "complex(1, 2)"])
def test_generate_eq(value):
    predicate = eq_p(value)

    assert_generated_false(predicate)


@pytest.mark.parametrize(
    "value",
    [
        2,
        "foo",
        3.14,
        datetime.now(),
        uuid.uuid4(),
    ],
)
def test_generate_ge(value):
    predicate = ge_p(value)

    assert_generated_false(predicate)


def assert_generated_false(predicate):
    values = take(5, generate_false(predicate))
    assert values

    for value in values:
        assert not predicate(value)
