import sys

from predicate import always_true_p, eq_p, ge_p, is_superset_p, reduce_p


def test_reduce_is_sorted_asc():
    predicate = reduce_p(fn=lambda acc, x: (x, ge_p(acc)), initial=-sys.maxsize - 1)

    assert predicate([])
    assert predicate([1])
    assert predicate([1, 2])
    assert not predicate([2, 1])


def test_is_interval_3():
    predicate = reduce_p(fn=lambda acc, x: (x, eq_p(acc + 3) if acc else always_true_p), initial=None)

    assert predicate([])
    assert predicate([1])
    assert predicate([1, 4, 7])
    assert not predicate([1, 3])


def test_is_subset():
    predicate = reduce_p(fn=lambda acc, x: (x, is_superset_p(acc)), initial=set())

    assert predicate([])
    assert predicate([{1}])
    assert predicate([{1}, {1, 3}, {1, 3, 7}])
    assert not predicate([{1}, {2, 3}])
