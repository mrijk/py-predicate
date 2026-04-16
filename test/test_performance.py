"""Performance comparison: interpreted vs compiled predicates."""

from predicate import compile_predicate, eq_p, ge_le_p, ge_p, gt_p, in_p, le_p, lt_p, ne_p, optimize


def test_eval_eq_interpreted(benchmark):
    p = eq_p(42)
    benchmark(p, 42)


def test_eval_eq_compiled(benchmark):
    cp = compile_predicate(eq_p(42))
    benchmark(cp, 42)


def test_eval_and_interpreted(benchmark):
    p = gt_p(0) & lt_p(100) & ne_p(50)
    benchmark(p, 25)


def test_eval_and_compiled(benchmark):
    cp = compile_predicate(gt_p(0) & lt_p(100) & ne_p(50))
    benchmark(cp, 25)


def test_eval_range_interpreted(benchmark):
    p = ge_le_p(0, 100)
    benchmark(p, 50)


def test_eval_range_compiled(benchmark):
    cp = compile_predicate(ge_le_p(0, 100))
    benchmark(cp, 50)


def test_eval_optimize_then_interpreted(benchmark):
    p = optimize(ge_p(0) & le_p(100))
    benchmark(p, 50)


def test_eval_optimize_then_compiled(benchmark):
    cp = compile_predicate(optimize(ge_p(0) & le_p(100)))
    benchmark(cp, 50)


def test_eval_in_interpreted(benchmark):
    p = in_p({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
    benchmark(p, 5)


def test_eval_in_compiled(benchmark):
    cp = compile_predicate(in_p({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
    benchmark(cp, 5)
