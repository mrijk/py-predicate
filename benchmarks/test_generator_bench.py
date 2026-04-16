"""Benchmarks for the value generator."""

from itertools import islice

from predicate import (
    eq_p,
    ge_le_p,
    ge_p,
    generate_true,
    in_p,
    is_list_of_p,
    le_p,
    ne_p,
    regex_p,
)

N = 20


def _take(n, predicate):
    return list(islice(generate_true(predicate), n))


def test_generate_true_eq(benchmark):
    p = eq_p(42)
    benchmark(_take, N, p)


def test_generate_true_range(benchmark):
    p = ge_le_p(0, 100)
    benchmark(_take, N, p)


def test_generate_true_ge(benchmark):
    p = ge_p(0)
    benchmark(_take, N, p)


def test_generate_true_and(benchmark):
    p = ge_p(0) & le_p(100) & ne_p(50)
    benchmark(_take, N, p)


def test_generate_true_or(benchmark):
    p = eq_p(1) | eq_p(2) | eq_p(3)
    benchmark(_take, N, p)


def test_generate_true_in(benchmark):
    p = in_p({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    benchmark(_take, N, p)


def test_generate_true_list_of(benchmark):
    p = is_list_of_p(ge_le_p(0, 100))
    benchmark(_take, N, p)


def test_generate_true_regex(benchmark):
    p = regex_p(r"[a-z]{4}")
    benchmark(_take, N, p)
