# from predicate import is_int_p, all_p
#
#
# def test_predicate(benchmark):
#     predicate = all_p(is_int_p)
#
#     result = benchmark(predicate, [1, 2, 3])
#
#     assert result
#
# def test_old(benchmark):
#     def foo():
#         return all(isinstance(x, int) for x in [1, 2 ,3])
#
#     result = benchmark(foo)
#
#     assert result
