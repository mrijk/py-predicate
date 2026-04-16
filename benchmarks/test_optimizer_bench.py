"""Benchmarks for the predicate optimizer."""

from predicate import (
    all_p,
    always_false_p,
    always_true_p,
    eq_p,
    ge_le_p,
    ge_p,
    in_p,
    is_list_of_p,
    le_p,
    ne_p,
    not_in_p,
    optimize,
)


def test_optimize_idempotent_and(benchmark):
    """P & p => p"""
    p = eq_p(1) & eq_p(1)
    benchmark(optimize, p)


def test_optimize_and_always_true(benchmark):
    """P & True => p"""
    p = ge_p(0) & always_true_p
    benchmark(optimize, p)


def test_optimize_and_always_false(benchmark):
    """P & False => False"""
    p = ge_p(0) & always_false_p
    benchmark(optimize, p)


def test_optimize_range_from_and(benchmark):
    """ge_p(0) & le_p(10) => ge_le_p(0, 10)"""
    p = ge_p(0) & le_p(10)
    benchmark(optimize, p)


def test_optimize_and_chain(benchmark):
    """Multi-step and chain."""
    p = ge_p(0) & le_p(100) & ne_p(50)
    benchmark(optimize, p)


def test_optimize_in_intersection(benchmark):
    """in_p({1,2,3}) & in_p({2,3,4}) => in_p({2,3})"""
    p = in_p({1, 2, 3}) & in_p({2, 3, 4})
    benchmark(optimize, p)


def test_optimize_in_not_in(benchmark):
    """in_p & not_in_p => reduced in_p"""
    p = in_p({1, 2, 3, 4, 5}) & not_in_p({3, 4})
    benchmark(optimize, p)


def test_optimize_or_always_true(benchmark):
    """P | True => True"""
    p = eq_p(1) | always_true_p
    benchmark(optimize, p)


def test_optimize_or_idempotent(benchmark):
    """P | p => p"""
    p = eq_p(1) | eq_p(1)
    benchmark(optimize, p)


def test_optimize_not_always_false(benchmark):
    """~False => True"""
    p = ~always_false_p
    benchmark(optimize, p)


def test_optimize_not_not(benchmark):
    """~~p => p"""
    p = ~~ge_p(0)
    benchmark(optimize, p)


def test_optimize_all_and(benchmark):
    """all_p(p1) & all_p(p2) => all_p(p1 & p2)"""
    p = all_p(ge_p(0)) & all_p(le_p(10))
    benchmark(optimize, p)


def test_optimize_deeply_nested(benchmark):
    """Deeply nested and/or tree."""
    p = (ge_p(0) & le_p(10)) | (ge_p(20) & le_p(30)) | (ge_p(40) & le_p(50))
    benchmark(optimize, p)


def test_optimize_is_list_of_and(benchmark):
    """Nested list_of predicate optimization."""
    p = is_list_of_p(ge_p(0) & le_p(100))
    benchmark(optimize, p)


def test_optimize_complement_and(benchmark):
    """P & ~p => False"""
    base = ge_p(5)
    p = base & ~base
    benchmark(optimize, p)


def test_optimize_absorption(benchmark):
    """P & (p | q) => p  [absorption law]"""
    p = ge_le_p(0, 10)
    q = eq_p(5)
    predicate = p & (p | q)
    benchmark(optimize, predicate)
