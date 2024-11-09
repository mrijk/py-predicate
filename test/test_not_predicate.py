from helpers import is_not_p

from predicate import ge_p


def test_not():
    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    assert is_not_p(lt_2)

    assert not lt_2(2)
    assert lt_2(1)


def test_not_not():
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert is_not_p(ge_2_to)

    assert not ge_2_to(1)
    assert ge_2_to(2)
