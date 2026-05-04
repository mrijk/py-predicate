import uuid
from datetime import datetime

import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import generate_true
from predicate.not_in_predicate import not_in_p


@pytest.mark.parametrize(
    "predicate",
    [
        not_in_p([2, 3, 4]),
        not_in_p(["foo", "bar"]),
        not_in_p([1.0, 2.5, 3.14]),
        not_in_p([datetime(2024, 1, 1), datetime(2024, 6, 15)]),
        not_in_p([uuid.uuid4(), uuid.uuid4()]),
    ],
)
def test_generate_not_in(predicate):
    assert_generated_true(predicate)


def test_generate_not_in_unknown():
    predicate = not_in_p({None})
    with pytest.raises(ValueError):
        take(5, generate_true(predicate))
