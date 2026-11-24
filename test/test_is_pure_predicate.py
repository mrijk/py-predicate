import os
import random
from datetime import datetime

from predicate import is_pure_p
from predicate.is_pure_predicate import find_impurity
from test import purity_helper as helper_module

counter = 0


def pure(x, y):
    return x + y


def uses_global(x):
    global counter
    counter += 1
    return x


def uses_print(x):
    print(x)  # noqa: T201
    return x


def uses_random(x):
    return x + random.random()  # noqa: S311


def uses_open(path):
    return open(path).read()


def uses_os(x):
    return os.getcwd() + x


def test_is_pure():
    assert is_pure_p(pure)
    assert is_pure_p(lambda x: x + 1)


def test_is_not_pure():
    assert not is_pure_p(uses_global)
    assert not is_pure_p(uses_print)
    assert not is_pure_p(uses_random)
    assert not is_pure_p(uses_open)
    assert not is_pure_p(uses_os)


def test_is_pure_nonlocal():
    def outer():
        n = 0

        def inner():
            nonlocal n
            n += 1

        return inner

    assert not is_pure_p(outer())


def test_is_pure_no_source():
    assert not is_pure_p(len)


def calls_impure(x):
    return uses_print(x)


def calls_calls_impure(x):
    return calls_impure(x)


def calls_pure(x):
    return pure(x, 1)


def calls_impure_via_module(x):
    return helper_module.impure_helper(x)


def recursive(n):
    return 1 if n == 0 else recursive(n - 1)


def mutual_a(n):
    return mutual_b(n)


def mutual_b(n):
    return mutual_a(n) if n else uses_print(n)


def calls_unknown(f, x):
    return f(x)


def test_transitive_impurity():
    assert not is_pure_p(calls_impure)
    assert not is_pure_p(calls_calls_impure)
    assert not is_pure_p(calls_impure_via_module)
    assert not is_pure_p(mutual_a)


def test_transitive_purity():
    assert is_pure_p(calls_pure)
    assert is_pure_p(recursive)
    assert is_pure_p(calls_unknown)  # unresolvable calls are not flagged


def test_transitive_via_closure():
    def inner(x):
        return uses_print(x)

    def outer(x):
        return inner(x)

    assert not is_pure_p(outer)


def test_find_impurity():
    assert find_impurity(pure) is None
    assert find_impurity(uses_global) == ("global-state", "global statement (test_is_pure_predicate.py:17)")
    assert find_impurity(uses_random) == ("randomness", "calls random.random (test_is_pure_predicate.py:28)")
    assert find_impurity(uses_os) == ("system", "calls os.getcwd (test_is_pure_predicate.py:36)")
    assert find_impurity(calls_impure) == (
        "io",
        "calls uses_print (test_is_pure_predicate.py:70) -> calls print (test_is_pure_predicate.py:23)",
    )
    assert find_impurity(len) == ("no-source", "no source available")


def uses_now():
    return datetime.now()


def builds_datetime():
    return datetime(2020, 1, 1)


def test_datetime():
    assert not is_pure_p(uses_now)
    assert find_impurity(uses_now).category == "time"
    assert is_pure_p(builds_datetime)
