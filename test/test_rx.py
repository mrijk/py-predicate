import reactivex as rx

from predicate import gt_p
from predicate.rx import filter_p


def test_filter_p():
    result = []
    rx.of(1, 2, 3, 4).pipe(filter_p(gt_p(2))).subscribe(result.append)

    assert result == [3, 4]
