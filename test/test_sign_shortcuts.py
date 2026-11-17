import math

import pytest

from predicate import compile_predicate, ge_p, generate_false, generate_true, le_p, non_neg_p, non_pos_p


@pytest.mark.parametrize("pred,comparison", [(non_neg_p, ge_p(0)), (non_pos_p, le_p(0))])
@pytest.mark.parametrize("value", [-math.inf, -1, -0.5, -0.0, 0, 0.5, 1, math.inf, math.nan])
def test_sign_shortcut_matches_comparison(pred, comparison, value):
    assert pred(value) == comparison(value)
    assert compile_predicate(pred)(value) == comparison(value)


@pytest.mark.parametrize("pred", [non_neg_p, non_pos_p])
def test_sign_shortcut_includes_zero(pred):
    assert pred(0)
    assert pred(-0.0)


@pytest.mark.parametrize("pred", [non_neg_p, non_pos_p])
def test_sign_shortcut_generators(pred):
    assert pred(next(generate_true(pred)))
    assert not pred(next(generate_false(pred)))
