from itertools import repeat

from more_itertools import interleave, take

from predicate import eq_p, explain, gt_p, lt_p, mutual_recur_p


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


def test_mutual_recur_explain_empty():
    predicate = mutual_recur_p(predicate_n=lambda x: (gt_p(x), predicate), empty=False)

    assert explain(predicate, []) == {"reason": "Empty iterable is not allowed", "result": False}


def test_mutual_recur_explain_single():
    predicate = mutual_recur_p(predicate_n=lambda x: (gt_p(x), predicate), predicate_1=eq_p(1))

    expected = {"reason": {"reason": "2 is not equal to 1", "result": False}, "result": False}
    assert explain(predicate, [2]) == expected


def test_mutual_recur_explain_pair():
    predicate_up = mutual_recur_p(predicate_n=lambda x: (gt_p(x), predicate_down))
    predicate_down = mutual_recur_p(predicate_n=lambda x: (lt_p(x), predicate_up))

    expected = {"reason": {"reason": "3 is not less than 2", "result": False}, "pair": (2, 3), "result": False}
    assert explain(predicate_up, [1, 2, 3]) == expected
