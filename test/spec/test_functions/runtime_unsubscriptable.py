# Annotations that only type checkers accept: evaluating them at runtime raises TypeError
from __future__ import annotations

from functools import singledispatchmethod
from typing import Any

from typing_extensions import TypeIs  # typing.TypeIs is 3.13+


def is_dispatch_method(obj: Any) -> TypeIs[singledispatchmethod[Any]]:
    return isinstance(obj, singledispatchmethod)


def misspelt(x: Intt, y: int) -> int:  # type: ignore[name-defined]  # noqa: F821
    return y
