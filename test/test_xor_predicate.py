from predicate import ge_p


def test_xor():
    # p ^ q
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    predicate = ge_2 ^ ge_4

    assert not predicate(1)
    assert not predicate(4)
    assert predicate(2)


def test_xor_commutative():
    # p ^ q == q ^ p
    ge_2 = ge_p(2)
    ge_4 = ge_p(4)

    predicate = ge_2 ^ ge_4

    assert not predicate(1)
    assert not predicate(4)
    assert predicate(2)

    ge_4_xor_ge_4 = ge_4 ^ ge_2

    assert ge_4_xor_ge_4(1) is False
    assert ge_4_xor_ge_4(2) is True
    assert ge_4_xor_ge_4(4) is False


def test_xor_eq(p, q):
    assert p ^ q == q ^ p
