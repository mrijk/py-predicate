from functools import partial
from itertools import batched

from predicate import is_tuple_of_p
from predicate.explain import explain
from predicate.standard_predicates import all_p, comp_p, ge_p, is_int_p, is_str_p


def test_comp_p():
    ge_2 = ge_p(2)

    predicate = comp_p(fn=lambda x: 2 * x, predicate=ge_2)

    assert not predicate(0)
    assert predicate(1)


def test_comp_p_iterable():
    to_pairs = partial(batched, n=2)
    int_str_p = is_tuple_of_p(is_int_p, is_str_p)

    predicate = comp_p(fn=to_pairs, predicate=all_p(int_str_p))

    assert not predicate([1, 2, 3, 4])
    assert predicate([1, "foo", 2, "bar"])


def test_comp_explain():
    ge_2 = ge_p(2)

    predicate = comp_p(fn=lambda x: 2 * x, predicate=ge_2)

    expected = {"reason": {"reason": "0 is not greater or equal to 2", "result": False}, "result": False}
    assert explain(predicate, 0) == expected
