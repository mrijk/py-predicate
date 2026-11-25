from uuid import UUID

import pytest
from more_itertools import take

from predicate import ge_p, generate_false, generate_true, gt_p, le_p, lt_p, not_in_p

_MIDDLE = UUID(int=2**127)


@pytest.mark.parametrize(
    ("predicate", "true_for"),
    [
        (ge_p(_MIDDLE), lambda uuid: uuid >= _MIDDLE),
        (gt_p(_MIDDLE), lambda uuid: uuid > _MIDDLE),
        (le_p(_MIDDLE), lambda uuid: uuid <= _MIDDLE),
        (lt_p(_MIDDLE), lambda uuid: uuid < _MIDDLE),
    ],
)
def test_generate_uuid_ordering(predicate, true_for):
    assert all(true_for(uuid) and predicate(uuid) for uuid in take(50, generate_true(predicate)))
    assert not any(predicate(uuid) for uuid in take(50, generate_false(predicate)))


@pytest.mark.parametrize(
    "predicate",
    [gt_p(UUID(int=2**128 - 1)), lt_p(UUID(int=0))],
)
def test_generate_uuid_ordering_without_values(predicate):
    assert list(generate_true(predicate)) == []


@pytest.mark.parametrize(
    "predicate",
    [ge_p(UUID(int=0)), le_p(UUID(int=2**128 - 1))],
)
def test_generate_false_uuid_ordering_without_values(predicate):
    assert list(generate_false(predicate)) == []


def test_generate_uuid_not_in():
    excluded = {UUID(int=1), UUID(int=2)}

    assert all(uuid not in excluded for uuid in take(50, generate_true(not_in_p(excluded))))
