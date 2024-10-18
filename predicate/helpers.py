from typing import Callable, Any


def const[T](x: T) -> Callable[[Any], T]:
    """Convert a value `x` to a function that always results in `x`.

    >>> const(1)(2)
    1
    >>> const(1)("foo")
    1
    >>> const(1)(None)
    1
    """
    return lambda *_: x