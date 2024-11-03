from helpers import is_not_p

from predicate import ge_p


def test_not():
    ge_2 = ge_p(2)
    lt_2 = ~ge_2

    assert is_not_p(lt_2)

    assert lt_2(2) is False
    assert lt_2(1) is True


def test_not_not():
    ge_2 = ge_p(2)
    ge_2_to = ~~ge_2

    assert is_not_p(ge_2_to)

    assert ge_2_to(2) is True
    assert ge_2_to(1) is False
