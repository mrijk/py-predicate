import pytest

from predicate import eq_p, ge_p, gt_lt_p, recur_p
from predicate.consumes import consumes


@pytest.mark.parametrize("iterable", [[], (), [1], (1,), [1, 2, 3], (1, 2, 3), range(200)])
@pytest.mark.skip
def test_recur_is_sorted_asc(iterable):
    predicate = recur_p(predicate_n=ge_p)
    assert predicate(iterable)


@pytest.mark.parametrize(
    "iterable",
    [
        [2, 1],
        (2, 1),
    ],
)
@pytest.mark.skip
def test_recur_is_not_sorted_asc(iterable):
    predicate = recur_p(predicate_n=ge_p)
    assert not predicate(iterable)


@pytest.mark.skip
def test_inc_by_1():
    predicate = recur_p(predicate_n=lambda x: eq_p(x + 1))

    assert predicate([])
    assert predicate([1])
    assert predicate([1, 2])
    assert predicate(range(200))
    assert not predicate([1, 3])


@pytest.mark.skip
def test_any_gap_3_or_more():
    predicate = ~recur_p(predicate_n=lambda x: gt_lt_p(lower=x - 3, upper=x + 3))

    assert not predicate([])
    assert not predicate([1])
    assert not predicate([1, 3])
    assert predicate([1, 4])
    assert predicate([4, 1])


@pytest.mark.parametrize(
    "iterable, expected_start, expected_end", [([], 0, 0), (["1"], 0, 1), ([1, 2], 0, 2), ((3, 4, 5, 6, 3, 2), 0, 4)]
)
@pytest.mark.skip
def test_all_consumes(iterable, expected_start, expected_end):
    predicate = recur_p(predicate_n=ge_p)

    consumed = list(consumes(predicate, iterable))
    expected_consumed = list(range(expected_start, expected_end + 1))

    assert consumed == expected_consumed
