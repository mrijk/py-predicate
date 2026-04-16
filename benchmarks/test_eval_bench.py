"""Benchmarks for predicate evaluation (calling predicates on values)."""

from predicate import (
    all_p,
    any_p,
    eq_p,
    ge_le_p,
    ge_p,
    in_p,
    is_list_of_p,
    le_p,
    ne_p,
    regex_p,
)


def test_eval_eq(benchmark):
    p = eq_p(42)
    benchmark(p, 42)


def test_eval_range(benchmark):
    p = ge_le_p(0, 100)
    benchmark(p, 50)


def test_eval_and_chain(benchmark):
    p = ge_p(0) & le_p(100) & ne_p(50)
    benchmark(p, 25)


def test_eval_or_chain(benchmark):
    p = eq_p(1) | eq_p(2) | eq_p(3) | eq_p(4) | eq_p(5)
    benchmark(p, 3)


def test_eval_not(benchmark):
    p = ~ge_p(0)
    benchmark(p, -1)


def test_eval_in(benchmark):
    p = in_p({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    benchmark(p, 5)


def test_eval_all_list(benchmark):
    p = all_p(ge_le_p(0, 100))
    data = list(range(50))
    benchmark(p, data)


def test_eval_any_list(benchmark):
    p = any_p(eq_p(99))
    data = list(range(100))
    benchmark(p, data)


def test_eval_is_list_of(benchmark):
    p = is_list_of_p(ge_p(0))
    data = list(range(100))
    benchmark(p, data)


def test_eval_regex(benchmark):
    p = regex_p(r"^\d{4}-\d{2}-\d{2}$")
    benchmark(p, "2024-01-15")


def test_eval_nested_and_or(benchmark):
    p = (ge_p(0) & le_p(50)) | (ge_p(60) & le_p(100))
    benchmark(p, 75)
