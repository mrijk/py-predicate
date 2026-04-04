from itertools import repeat

from more_itertools import interleave, take

from predicate import eq_p, gt_p, lt_p, mutual_recur_p


def test_recur_zig_zag():
    predicate_up = mutual_recur_p(predicate_n=lambda x: (gt_p(x), predicate_down))
    predicate_down = mutual_recur_p(predicate_n=lambda x: (lt_p(x), predicate_up))

    predicate = predicate_up | predicate_down

    assert predicate([])
    assert predicate([1])
    assert predicate([1, 2])
    assert predicate([2, 1])
    assert predicate([1, 2, 1])
    assert predicate([2, 1, 2])
    assert not predicate([1, 2, 3])

    large_zig_zag = take(99999, interleave(repeat(0), repeat(1)))
    assert predicate(large_zig_zag)


def test_traffic_light_cycle():
    predicate_green = mutual_recur_p(predicate_n=lambda _: (eq_p("green"), predicate_yellow))
    predicate_yellow = mutual_recur_p(predicate_n=lambda _: (eq_p("yellow"), predicate_red))
    predicate_red = mutual_recur_p(predicate_n=lambda _: (eq_p("red"), predicate_green))

    predicate = predicate_green | predicate_yellow | predicate_red

    assert predicate([])
    assert predicate(["green"])
    assert predicate(["green", "yellow", "red"])
    assert predicate(["red", "green", "yellow"])

    assert not predicate(["green", "red", "yellow"])
