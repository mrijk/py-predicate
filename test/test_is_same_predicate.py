from predicate import is_same_p


def test_is_same_p_same_name(p):
    predicate = is_same_p(p)

    assert predicate(p)


def test_is_same_p_and_2(p, q):
    predicate = is_same_p(p & q)

    assert predicate(q & p)


def test_is_same_p_and_3(p, q, r):
    predicate = is_same_p(p & q & r)

    assert predicate(p & r & q)


def test_is_same_p_or(p, q):
    predicate = is_same_p(p | q)

    assert predicate(q | p)


def test_is_same_p_xor(p, q):
    predicate = is_same_p(p ^ q)

    assert predicate(q ^ p)


def test_is_same_p_fail(p, q):
    predicate = is_same_p(p)

    assert not predicate(q)
