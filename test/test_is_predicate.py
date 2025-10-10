from predicate import explain, is_p


def test_is_p_repr():
    predicate = is_p(False)
    assert repr(predicate) == "is_p(False)"


def test_is_p_false():
    predicate = is_p(False)
    assert predicate(False)


def test_is_p_true():
    predicate = is_p(True)
    assert predicate(True)


def test_is_p_int():
    predicate = is_p(13)
    assert predicate(13)


def test_is_p_empty_set():
    predicate = is_p({})
    assert not predicate({})


def test_is_p_empty_array():
    predicate = is_p([])
    assert not predicate([])


def test_is_p_explain():
    predicate = is_p({})

    expected = {"reason": "{} does not refer to {}", "result": False}
    assert explain(predicate, {}) == expected
