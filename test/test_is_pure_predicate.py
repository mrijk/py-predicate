import os
import random

from predicate import is_pure_p

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
