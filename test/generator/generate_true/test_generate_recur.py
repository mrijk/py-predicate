import pytest
from more_itertools import take

from generator.generate_true.helpers import assert_generated_true
from predicate import always_true_p, eq_p, ge_p, generate_true, gt_p, is_int_p, le_p, lt_p, recur_p


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
    ],
)
def test_generate_recur(empty, predicate_1, predicate_n):
    predicate = recur_p(predicate_n=predicate_n, empty=empty, predicate_1=predicate_1)

    assert_generated_true(predicate)


def test_generate_recur_not_empty():
    predicate = recur_p(predicate_n=ge_p, empty=False)

    assert all(take(20, generate_true(predicate)))


def test_generate_recur_has_long_sequences():
    predicate = recur_p(predicate_n=ge_p)

    assert any(len(value) > 2 for value in take(20, generate_true(predicate)))
