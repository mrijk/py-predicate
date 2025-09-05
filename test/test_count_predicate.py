from predicate import count_p, eq_p, explain, ge_p
from predicate.count_predicate import exactly_one_p


def test_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert predicate([1])


def test_count_false():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert not predicate([1, 3])
    assert not predicate([0])


def test_count_explain():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    expected = {"reason": "Expected count eq_p(1), actual: 2", "result": False}

    assert explain(predicate, [1, 3]) == expected


def test_exactly_one():
    predicate = exactly_one_p(predicate=ge_p(1))

    assert predicate([1])
    assert not predicate([1, 1])
