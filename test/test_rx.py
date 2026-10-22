import reactivex as rx
from reactivex.internal.exceptions import SequenceContainsNoElementsError
from reactivex.subject import Subject

from predicate import gt_p, lt_p
from predicate.rx import (
    all_p,
    count_p,
    filter_p,
    find_index_p,
    find_p,
    first_or_default_p,
    first_p,
    last_or_default_p,
    last_p,
    partition_p,
    single_or_default_p,
    single_p,
    skip_while_p,
    some_p,
    take_while_p,
)


def collect(observable):
    result = []
    observable.subscribe(result.append)
    return result


def collect_error(observable):
    errors = []
    observable.subscribe(on_error=errors.append)
    return errors[0]


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


def test_all_p():
    assert collect(rx.of(3, 4).pipe(all_p(gt_p(2)))) == [True]
    assert collect(rx.of(1, 4).pipe(all_p(gt_p(2)))) == [False]


def test_some_p():
    assert collect(rx.of(1, 4).pipe(some_p(gt_p(2)))) == [True]
    assert collect(rx.of(1, 2).pipe(some_p(gt_p(2)))) == [False]


def test_count_p():
    assert collect(rx.of(1, 2, 3, 4).pipe(count_p(gt_p(2)))) == [2]


def test_first_p():
    assert collect(rx.of(1, 3, 4).pipe(first_p(gt_p(2)))) == [3]


def test_first_p_none():
    assert isinstance(collect_error(rx.of(1, 2).pipe(first_p(gt_p(2)))), SequenceContainsNoElementsError)


def test_last_p():
    assert collect(rx.of(1, 3, 4).pipe(last_p(gt_p(2)))) == [4]


def test_last_p_none():
    assert isinstance(collect_error(rx.of(1, 2).pipe(last_p(gt_p(2)))), SequenceContainsNoElementsError)


def test_single_p():
    assert collect(rx.of(1, 3).pipe(single_p(gt_p(2)))) == [3]


def test_single_p_none():
    assert isinstance(collect_error(rx.of(1, 2).pipe(single_p(gt_p(2)))), SequenceContainsNoElementsError)


def test_single_p_more_than_one():
    assert str(collect_error(rx.of(3, 4).pipe(single_p(gt_p(2))))) == "Sequence contains more than one element"


def test_first_or_default_p():
    assert collect(rx.of(1, 3, 4).pipe(first_or_default_p(gt_p(2), 0))) == [3]


def test_first_or_default_p_none():
    assert collect(rx.of(1, 2).pipe(first_or_default_p(gt_p(2), 0))) == [0]


def test_last_or_default_p():
    assert collect(rx.of(1, 3, 4).pipe(last_or_default_p(gt_p(2), 0))) == [4]


def test_last_or_default_p_none():
    assert collect(rx.of(1, 2).pipe(last_or_default_p(gt_p(2), 0))) == [0]


def test_single_or_default_p():
    assert collect(rx.of(1, 3).pipe(single_or_default_p(gt_p(2), 0))) == [3]


def test_single_or_default_p_none():
    assert collect(rx.of(1, 2).pipe(single_or_default_p(gt_p(2), 0))) == [0]


def test_single_or_default_p_more_than_one():
    assert (
        str(collect_error(rx.of(3, 4).pipe(single_or_default_p(gt_p(2), 0))))
        == "Sequence contains more than one element"
    )


def test_find_p():
    assert collect(rx.of(1, 3, 4).pipe(find_p(gt_p(2)))) == [3]


def test_find_p_none():
    assert collect(rx.of(1, 2).pipe(find_p(gt_p(2)))) == [None]


def test_find_index_p():
    assert collect(rx.of(1, 3, 4).pipe(find_index_p(gt_p(2)))) == [1]


def test_find_index_p_none():
    assert collect(rx.of(1, 2).pipe(find_index_p(gt_p(2)))) == [-1]
