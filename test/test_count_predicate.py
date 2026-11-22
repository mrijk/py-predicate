from predicate import count_p, eq_p, explain, ge_p
from predicate.count_predicate import exactly_one_p, exactly_zero_p


def test_count():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert predicate([1])


def test_count_repr():
    predicate = count_p(predicate=ge_p(1), length_p=eq_p(1))

    assert repr(predicate) == "count_p(ge_p(1), eq_p(1))"


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


def test_exactly_zero():
    predicate = exactly_zero_p(predicate=ge_p(1))

    assert predicate([])
    assert predicate([0, -1])
    assert not predicate([0, 1])


def test_count_other_length_predicate():
    predicate = count_p(predicate=ge_p(1), length_p=ge_p(2))

    assert predicate([1, 2, 0])
    assert not predicate([1, 0])


def test_count_explain_other_length_predicate():
    predicate = count_p(predicate=ge_p(1), length_p=ge_p(2))

    expected = {"reason": "Expected count ge_p(2), actual: 1", "result": False}

    assert explain(predicate, [1, 0]) == expected
