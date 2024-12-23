from predicate import explain, is_int_p, is_list_of_p, is_none_p, is_set_of_p, is_str_p
from predicate.in_predicate_predicate import in_predicate_p


def test_in_predicate_predicate():
    tree = is_str_p | is_list_of_p(is_int_p) | is_set_of_p(is_none_p)

    in_tree = in_predicate_p(tree)

    assert in_tree(is_none_p)
    assert in_tree(tree)
    assert in_tree(is_str_p)
    assert in_tree(is_int_p)
    assert in_tree(is_list_of_p(is_int_p))


def test_in_predicate_predicate_unordered(p, q, r):
    tree = p & q & r

    in_tree = in_predicate_p(tree)

    assert in_tree(p & q)
    assert in_tree(q & p)


def test_in_predicate_predicate_repr():
    tree = is_str_p | is_list_of_p(is_int_p) | is_set_of_p(is_none_p)

    in_tree = in_predicate_p(tree)

    assert repr(in_tree) == "in_predicate_p(is_str_p | is_list_of_p(is_int_p) | is_set_of_p(is_none_p))"


def test_in_predicate_predicate_explain():
    tree = is_str_p | is_int_p

    in_tree = in_predicate_p(tree)

    expected = {"reason": "is_none_p is not part of predicate is_str_p | is_int_p", "result": False}
    assert explain(in_tree, is_none_p) == expected
