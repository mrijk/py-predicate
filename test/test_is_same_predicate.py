import pytest

from predicate import eq_p, explain, is_same_p


@pytest.mark.skip
def test_is_same_p_repr():
    predicate = is_same_p(eq_p(2))

    assert repr(predicate) == "is_same_p(eq_p(2))"


@pytest.mark.skip
def test_is_same_p_same_name(p):
    predicate = is_same_p(p)

    assert predicate(p)


@pytest.mark.skip
def test_is_same_p_and_2(p, q):
    predicate = is_same_p(p & q)

    assert predicate(q & p)


@pytest.mark.skip
def test_is_same_p_and_3(p, q, r):
    predicate = is_same_p(p & q & r)

    assert predicate(p & r & q)


@pytest.mark.skip
def test_is_same_p_or(p, q):
    predicate = is_same_p(p | q)

    assert predicate(q | p)


@pytest.mark.skip
def test_is_same_p_xor(p, q):
    predicate = is_same_p(p ^ q)

    assert predicate(q ^ p)


@pytest.mark.skip
def test_is_same_p_fail(p, q):
    predicate = is_same_p(p)

    assert not predicate(q)

    expected = {"reason": "Predicates are not equivalent.", "result": False}
    assert explain(predicate, q) == expected


@pytest.mark.skip
def test_is_same_p_values_fail(p, q):
    predicate = is_same_p(p & q)

    assert not predicate(p | q)

    expected = {"reason": "Predicates have different truth tables.", "result": False}
    assert explain(predicate, p | q) == expected


@pytest.mark.skip
def test_is_same_p_predicates_after_rename():
    p = eq_p(2)
    q = eq_p(3)

    predicate = is_same_p(p | q)

    assert predicate(q | p)


@pytest.mark.skip
def test_is_same_p_de_morgan():
    p = eq_p(2)
    q = eq_p(3)

    predicate = is_same_p(~p & ~q)

    assert predicate(~(p | q))


@pytest.mark.skip
def test_is_same_p_predicates_fail_after_rename():
    p = eq_p(2)
    q = eq_p(3)

    predicate = is_same_p(p & q)

    assert not predicate(q | p)
