import reactivex as rx
from reactivex.subject import Subject

from predicate import gt_p, lt_p
from predicate.rx import filter_p, partition_p, skip_while_p, take_while_p


def collect(observable):
    result = []
    observable.subscribe(result.append)
    return result


def test_filter_p():
    assert collect(rx.of(1, 2, 3, 4).pipe(filter_p(gt_p(2)))) == [3, 4]


def test_take_while_p():
    assert collect(rx.of(1, 2, 3, 1).pipe(take_while_p(lt_p(3)))) == [1, 2]


def test_take_while_p_inclusive():
    assert collect(rx.of(1, 2, 3, 1).pipe(take_while_p(lt_p(3), inclusive=True))) == [1, 2, 3]


def test_skip_while_p():
    assert collect(rx.of(1, 2, 3, 1).pipe(skip_while_p(lt_p(3)))) == [3, 1]


def test_partition_p():
    source = Subject()
    matching, non_matching = partition_p(gt_p(2))(source)
    matches, non_matches = collect(matching), collect(non_matching)

    for item in (1, 2, 3, 4):
        source.on_next(item)

    assert matches == [3, 4]
    assert non_matches == [1, 2]
