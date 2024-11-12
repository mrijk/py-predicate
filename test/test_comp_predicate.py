from predicate.standard_predicates import comp_p, ge_p


def test_comp_predicate():
    ge_2 = ge_p(2)

    predicate = comp_p(fn=lambda x: 2 * x, predicate=ge_2)

    assert not predicate(0)
    assert predicate(1)
