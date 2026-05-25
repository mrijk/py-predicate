from more_itertools import take

from predicate import all_p, are_equivalent, generate_false, generate_true
from predicate.constructor.construct import construct


def assert_generated(predicate):
    nr_of_samples = 10
    true_set = take(nr_of_samples, generate_true(predicate))
    false_set = take(nr_of_samples, generate_false(predicate))

    matched = construct(false_set=false_set, true_set=true_set)

    assert matched

    all_false = all_p(~matched)
    all_true = all_p(matched)

    assert all_false(false_set)
    assert all_true(true_set)

    return matched


def assert_generated_exact(predicate):
    matched = assert_generated(predicate)
    assert are_equivalent(predicate, matched)
