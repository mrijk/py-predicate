"""Tests for compile_predicate."""

import pytest

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    any_p,
    compile_predicate,
    eq_p,
    fn_p,
    ge_le_p,
    ge_lt_p,
    ge_p,
    gt_le_p,
    gt_lt_p,
    gt_p,
    has_key_p,
    in_p,
    is_bool_p,
    is_falsy_p,
    is_int_p,
    is_list_of_p,
    is_none_p,
    is_not_none_p,
    is_set_of_p,
    is_str_p,
    is_truthy_p,
    is_tuple_of_p,
    le_p,
    lt_p,
    ne_p,
    not_in_p,
    optimize,
    regex_p,
    try_compile_predicate,
)
from predicate.compile_predicate import CompiledPredicate, NotCompilableError

# --- compile_predicate returns CompiledPredicate ---


def test_compile_returns_compiled_predicate():
    cp = compile_predicate(eq_p(1))
    assert isinstance(cp, CompiledPredicate)


# --- Leaf predicates ---


def test_compile_eq():
    cp = compile_predicate(eq_p(42))
    assert cp(42)
    assert not cp(0)


def test_compile_ne():
    cp = compile_predicate(ne_p(42))
    assert cp(0)
    assert not cp(42)


def test_compile_gt():
    cp = compile_predicate(gt_p(0))
    assert cp(1)
    assert not cp(0)
    assert not cp(-1)


def test_compile_ge():
    cp = compile_predicate(ge_p(0))
    assert cp(0)
    assert cp(1)
    assert not cp(-1)


def test_compile_lt():
    cp = compile_predicate(lt_p(10))
    assert cp(9)
    assert not cp(10)


def test_compile_le():
    cp = compile_predicate(le_p(10))
    assert cp(10)
    assert cp(9)
    assert not cp(11)


def test_compile_is_none():
    cp = compile_predicate(is_none_p)
    assert cp(None)
    assert not cp(0)
    assert not cp(False)


def test_compile_is_not_none():
    cp = compile_predicate(is_not_none_p)
    assert cp(0)
    assert cp(False)
    assert not cp(None)


def test_compile_is_truthy():
    cp = compile_predicate(is_truthy_p)
    assert cp(1)
    assert cp("x")
    assert not cp(0)
    assert not cp("")


def test_compile_is_falsy():
    cp = compile_predicate(is_falsy_p)
    assert cp(0)
    assert cp("")
    assert not cp(1)
    assert not cp("x")


def test_compile_in():
    cp = compile_predicate(in_p({1, 2, 3}))
    assert cp(1)
    assert cp(3)
    assert not cp(4)


def test_compile_not_in():
    cp = compile_predicate(not_in_p({1, 2, 3}))
    assert cp(4)
    assert not cp(1)


# --- Range predicates ---


def test_compile_ge_le():
    cp = compile_predicate(ge_le_p(0, 10))
    assert cp(0)
    assert cp(5)
    assert cp(10)
    assert not cp(-1)
    assert not cp(11)


def test_compile_ge_lt():
    cp = compile_predicate(ge_lt_p(0, 10))
    assert cp(0)
    assert cp(9)
    assert not cp(10)


def test_compile_gt_le():
    cp = compile_predicate(gt_le_p(0, 10))
    assert cp(1)
    assert cp(10)
    assert not cp(0)


def test_compile_gt_lt():
    cp = compile_predicate(gt_lt_p(0, 10))
    assert cp(1)
    assert cp(9)
    assert not cp(0)
    assert not cp(10)


# --- IsInstancePredicate (delegation) ---


def test_compile_is_instance_int():
    cp = compile_predicate(is_int_p)
    assert cp(1)
    assert not cp("x")


def test_compile_is_instance_preserves_bool_int_semantics():
    """is_int_p should return False for bool values (non-standard but intentional)."""
    cp = compile_predicate(is_int_p)
    assert not cp(True)
    assert not cp(False)


def test_compile_is_instance_str():
    cp = compile_predicate(is_str_p)
    assert cp("hello")
    assert not cp(1)


def test_compile_is_bool():
    cp = compile_predicate(is_bool_p)
    assert cp(True)
    assert not cp(1)


# --- Boolean combinators ---


def test_compile_and():
    cp = compile_predicate(gt_p(0) & lt_p(10))
    assert cp(5)
    assert not cp(0)
    assert not cp(10)


def test_compile_or():
    cp = compile_predicate(eq_p(1) | eq_p(2))
    assert cp(1)
    assert cp(2)
    assert not cp(3)


def test_compile_not():
    cp = compile_predicate(~gt_p(0))
    assert cp(0)
    assert cp(-1)
    assert not cp(1)


def test_compile_xor():
    cp = compile_predicate(eq_p(1) ^ eq_p(2))
    assert cp(1)
    assert cp(2)
    assert not cp(3)


def test_compile_xor_both_true_is_false():
    # Both sides true at once: this predicate is always false for a single int value
    # but we can construct a logical case: eq_p(1) ^ eq_p(1)
    cp = compile_predicate(eq_p(1) ^ eq_p(1))
    assert not cp(1)
    assert not cp(0)


# --- Nested / combined ---


def test_compile_nested_and_or():
    cp = compile_predicate((gt_p(0) & le_p(5)) | (gt_p(10) & le_p(15)))
    assert cp(3)
    assert cp(12)
    assert not cp(0)
    assert not cp(7)


def test_compile_optimize_then_compile():
    p = optimize(ge_p(0) & le_p(10))
    cp = compile_predicate(p)
    assert cp(5)
    assert not cp(11)


# --- NotCompilableError ---


def test_compile_all():
    cp = compile_predicate(all_p(gt_p(0)))
    assert cp([1, 2, 3])
    assert not cp([1, -1, 3])
    assert cp([])


def test_compile_all_nested():
    cp = compile_predicate(all_p(gt_p(0) & lt_p(10)))
    assert cp([1, 2, 9])
    assert not cp([1, 10, 3])


def test_compile_any():
    cp = compile_predicate(any_p(gt_p(0)))
    assert cp([0, 0, 1])
    assert not cp([0, -1, 0])
    assert not cp([])


def test_compile_any_nested():
    cp = compile_predicate(any_p(gt_p(0) & lt_p(10)))
    assert cp([0, 5, 10])
    assert not cp([0, -1, 10])


def test_compile_list_of():
    cp = compile_predicate(is_list_of_p(gt_p(0)))
    assert cp([1, 2, 3])
    assert not cp([1, -1, 3])
    assert cp([])
    assert not cp("not-a-list")
    assert not cp(42)


def test_compile_list_of_nested():
    cp = compile_predicate(is_list_of_p(gt_p(0) & lt_p(10)))
    assert cp([1, 2, 9])
    assert not cp([1, 10, 3])
    assert not cp("not-a-list")


def test_compile_has_key():
    cp = compile_predicate(has_key_p("a"))
    assert cp({"a": 1})
    assert cp({"a": 1, "b": 2})
    assert not cp({"b": 1})
    assert not cp({})


def test_compile_set_of():
    cp = compile_predicate(is_set_of_p(gt_p(0)))
    assert cp({1, 2, 3})
    assert cp(set())
    assert not cp({1, -1, 3})
    assert not cp([1, 2, 3])
    assert not cp(42)


def test_compile_set_of_nested():
    cp = compile_predicate(is_set_of_p(gt_p(0) & lt_p(10)))
    assert cp({1, 2, 9})
    assert not cp({1, 10})
    assert not cp("not-a-set")


def test_compile_tuple_of():
    cp = compile_predicate(is_tuple_of_p(is_int_p, is_str_p))
    assert cp((1, "hello"))
    assert not cp((1, 2))
    assert not cp(("hello", "world"))
    assert not cp((1,))
    assert not cp((1, "hello", True))


def test_compile_tuple_of_empty():
    cp = compile_predicate(is_tuple_of_p())
    assert cp(())
    assert not cp((1,))


def test_compile_tuple_of_nested():
    cp = compile_predicate(is_tuple_of_p(gt_p(0) & lt_p(10), gt_p(100)))
    assert cp((5, 200))
    assert not cp((0, 200))
    assert not cp((5, 50))


def test_compile_fn_raises():
    with pytest.raises(NotCompilableError):
        compile_predicate(fn_p(lambda x: x > 0))


def test_compile_regex_raises():
    with pytest.raises(NotCompilableError):
        compile_predicate(regex_p(r"\d+"))


def test_compile_always_true():
    cp = compile_predicate(always_true_p)
    assert cp(0)
    assert cp(None)
    assert cp("anything")


def test_compile_always_false():
    cp = compile_predicate(always_false_p)
    assert not cp(0)
    assert not cp(None)
    assert not cp("anything")


# --- try_compile_predicate ---


def test_try_compile_compilable():
    p = gt_p(0) & lt_p(10)
    cp = try_compile_predicate(p)
    assert isinstance(cp, CompiledPredicate)
    assert cp(5)


def test_try_compile_non_compilable_returns_original():
    p = fn_p(lambda x: x > 0)
    result = try_compile_predicate(p)
    assert result is p


# --- Delegation of introspection to wrapped predicate ---


def test_compiled_repr_delegates():
    p = gt_p(0) & lt_p(10)
    cp = compile_predicate(p)
    assert repr(cp) == repr(p)


def test_compiled_count_delegates():
    p = gt_p(0) & lt_p(10)
    cp = compile_predicate(p)
    assert cp.count == p.count


def test_compiled_contains_delegates():
    inner = gt_p(0)
    p = inner & lt_p(10)
    cp = compile_predicate(p)
    assert inner in cp


def test_compiled_explain_failure_delegates():
    p = gt_p(0)
    cp = compile_predicate(p)
    assert cp.explain_failure(-1) == p.explain_failure(-1)


def test_compiled_eq_based_on_wrapped_predicate():
    p = gt_p(0)
    cp1 = compile_predicate(p)
    cp2 = compile_predicate(p)
    assert cp1 == cp2
