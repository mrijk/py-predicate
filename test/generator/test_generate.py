import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    eq_p,
    fn_p,
    in_p,
    is_bool_p,
    is_complex_p,
    is_datetime_p,
    is_falsy_p,
    is_float_p,
    is_int_p,
    is_none_p,
    is_not_none_p,
    is_str_p,
    is_truthy_p,
    is_uuid_p,
    ne_p,
    not_in_p,
)
from predicate.generator.generate import generate
from predicate.standard_predicates import ge_p, gt_p, le_p, lt_p, pos_p, zero_p


@pytest.mark.parametrize(
    "predicate",
    [
        all_p(is_int_p),
        any_p(is_uuid_p),
        eq_p(2),
        ge_p(2),
        gt_p(2),
        in_p(2, 3, 4),
        is_bool_p,
        is_complex_p,
        is_datetime_p,
        is_falsy_p,
        is_float_p,
        is_none_p,
        is_not_none_p,
        is_truthy_p,
        is_int_p,
        is_uuid_p,
        is_str_p,
        is_int_p | is_str_p,
        le_p(2),
        lt_p(2),
        ne_p(2),
        not_in_p(2, "foo", 4),
        pos_p,
        zero_p,
    ],
)
def test_generate(predicate):
    assert_generated(predicate)


def test_generate_false():
    predicate = always_false_p

    with pytest.raises(ValueError):
        generate(predicate)


def test_generate_true():
    predicate = always_true_p

    assert_generated(predicate)


def test_generate_fn_p():
    predicate = fn_p(lambda _x: True)

    with pytest.raises(ValueError):
        generate(predicate)


def assert_generated(predicate):
    values = list(generate(predicate))
    assert values

    for value in values:
        assert predicate(value)
