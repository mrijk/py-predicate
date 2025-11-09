import pytest

from predicate import eq_p, ge_p, gt_lt_p, recur_p


@pytest.mark.parametrize("iterable", [[], (), [1], (1,), [1, 2, 3], (1, 2, 3), range(200)])
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
def test_recur_is_not_sorted_asc(iterable):
    predicate = recur_p(predicate_n=ge_p)
    assert not predicate(iterable)


def test_inc_by_1():
    predicate = recur_p(predicate_n=lambda x: eq_p(x + 1))

    assert predicate([])
    assert predicate([1])
    assert predicate([1, 2])
    assert predicate(range(200))
    assert not predicate([1, 3])


def test_any_gap_3_or_more():
    predicate = ~recur_p(predicate_n=lambda x: gt_lt_p(lower=x - 3, upper=x + 3))

    assert not predicate([])
    assert not predicate([1])
    assert not predicate([1, 3])
    assert predicate([1, 4])
    assert predicate([4, 1])
