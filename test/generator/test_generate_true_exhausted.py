from more_itertools import take

from predicate import (
    always_false_p,
    always_true_p,
    count_p,
    eq_p,
    exactly_n,
    generate_false,
    generate_true,
    is_dict_of_p,
    match_p,
    recur_p,
    repeat,
    star,
)


def test_generate_sequence_with_unsatisfiable_predicate_ends_cleanly():
    # An exhausted inner generator must end the outer one, not raise RuntimeError (PEP 479)
    for predicate in (
        match_p(eq_p(1), exactly_n(2, always_false_p)),
        match_p(exactly_n(2, always_false_p), eq_p(1)),
        match_p(repeat(1, 3, always_false_p), eq_p(1)),
        match_p(star(always_false_p), eq_p(1)),
    ):
        assert isinstance(take(5, generate_true(predicate)), list)


def test_generate_count_with_unsatisfiable_length_ends_cleanly():
    assert take(5, generate_true(count_p(length_p=always_false_p, predicate=eq_p(1)))) == []


def test_generate_false_count_with_unsatisfiable_length_ends_cleanly():
    assert take(5, generate_false(count_p(length_p=always_true_p, predicate=eq_p(1)))) == []


def test_generate_false_dict_of_with_unsatisfiable_generator_ends_cleanly():
    # always_true_p can't be false, so there is no false key to generate
    assert isinstance(take(5, generate_false(is_dict_of_p((always_true_p, always_true_p)))), list)


def test_generate_recur_with_unsatisfiable_start_ends_cleanly():
    assert take(5, generate_true(recur_p(lambda x: always_true_p, predicate_1=always_false_p))) == []
