from more_itertools import take

from predicate import explain, generate_true


def assert_generated_true(predicate, **kwargs):
    values = take(5, generate_true(predicate, **kwargs))
    assert values

    for value in values:
        assert predicate(value), explain(predicate, value)
