from predicate import all_p, ge_p, gt_p, is_int_p, le_p, lt_p, ne_p, optimize
from predicate.range_predicate import GtLtPredicate

# ---------------------------------------------------------------------------
# 1. Predicate evaluation vs. plain Python
# ---------------------------------------------------------------------------


def test_plain_python_and(benchmark):
    result = benchmark(lambda x: x > 0 and x < 10, 5)
    assert result


def test_predicate_and(benchmark):
    p = gt_p(0) & lt_p(10)
    result = benchmark(p, 5)
    assert result


# ---------------------------------------------------------------------------
# 2. Optimizer impact
# ---------------------------------------------------------------------------


def test_unoptimized_and(benchmark):
    p = gt_p(0) & lt_p(10)
    result = benchmark(p, 5)
    assert result


def test_optimized_and(benchmark):
    p = optimize(gt_p(0) & lt_p(10))
    assert isinstance(p, GtLtPredicate)
    result = benchmark(p, 5)
    assert result


# ---------------------------------------------------------------------------
# 3. Tree depth
# ---------------------------------------------------------------------------


def test_depth_2(benchmark):
    p = gt_p(0) & lt_p(10)
    result = benchmark(p, 5)
    assert result


def test_depth_4(benchmark):
    p = (gt_p(0) & lt_p(100)) & (ne_p(42) & ne_p(99))
    result = benchmark(p, 5)
    assert result


def test_depth_6(benchmark):
    p = ((gt_p(0) & lt_p(100)) & (ne_p(42) & ne_p(99))) & (ge_p(1) & le_p(98))
    result = benchmark(p, 5)
    assert result


# ---------------------------------------------------------------------------
# 4. Collection predicates
# ---------------------------------------------------------------------------


def test_all_predicate_int(benchmark):
    p = all_p(is_int_p)
    data = list(range(1, 1001))
    result = benchmark(p, data)
    assert result


def test_plain_python_all_int(benchmark):
    data = list(range(1, 1001))
    result = benchmark(lambda xs: all(isinstance(x, int) for x in xs), data)
    assert result


def test_all_predicate_gt(benchmark):
    p = all_p(gt_p(0))
    data = list(range(1, 1001))
    result = benchmark(p, data)
    assert result


def test_plain_python_all_gt(benchmark):
    data = list(range(1, 1001))
    result = benchmark(lambda xs: all(x > 0 for x in xs), data)
    assert result
