from predicate import all_p, is_float_p, is_int_p, is_str_p
from predicate.constructor.helpers import predicate_match, sort_by_match


def test_predicate_match():
    predicate = all_p(is_int_p)

    false_set = [("foo", "bar")]
    true_set = [(1, 2, 3)]
    result = predicate_match(predicate, false_set=false_set, true_set=true_set)

    assert result == {
        "false_matches": 1,
        "false_misses": 0,
        "true_matches": 1,
        "true_misses": 0,
    }


def test_sort_by_match():
    all_str = all_p(is_str_p)
    all_float = all_p(is_float_p)
    all_int = all_p(is_int_p)

    predicates = [all_str, all_int, all_float]

    false_set = [("foo", "bar")]
    true_set = [(1, 2, 3, "blah")]

    result = sort_by_match(predicates, false_set=false_set, true_set=true_set)

    assert result == [all_int, all_float, all_str]
