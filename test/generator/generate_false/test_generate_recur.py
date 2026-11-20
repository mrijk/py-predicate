import pytest
from more_itertools import take

from generator.generate_false.helpers import assert_generated_false
from predicate import always_true_p, eq_p, ge_p, generate_false, gt_p, is_int_p, le_p, lt_p, recur_p


@pytest.mark.parametrize(
    "empty, predicate_1, predicate_n",
    [
        (True, always_true_p, ge_p),
        (True, always_true_p, le_p),
        (True, always_true_p, gt_p),
        (True, always_true_p, lt_p),
        (True, always_true_p, eq_p),
        (True, is_int_p, ge_p),
        (False, always_true_p, ge_p),
        (False, is_int_p, ge_p),
    ],
)
def test_generate_recur(empty, predicate_1, predicate_n):
    predicate = recur_p(predicate_n=predicate_n, empty=empty, predicate_1=predicate_1)

    assert_generated_false(predicate)


def test_generate_recur_empty():
    values = take(5, generate_false(recur_p(predicate_n=ge_p, empty=False)))

    assert [] in values


def test_generate_recur_one_element():
    values = take(20, generate_false(recur_p(predicate_n=ge_p, predicate_1=is_int_p)))

    assert any(len(value) == 1 for value in values)


def test_generate_recur_broken_pair():
    values = take(20, generate_false(recur_p(predicate_n=ge_p)))

    assert any(len(value) > 1 for value in values)


def test_generate_recur_no_false_values():
    predicate = recur_p(predicate_n=lambda _: always_true_p)

    assert list(generate_false(predicate)) == []
