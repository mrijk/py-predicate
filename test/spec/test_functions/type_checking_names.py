# No `from __future__ import annotations`: on Python 3.14 annotations are evaluated lazily instead
import typing

if typing.TYPE_CHECKING:
    import collections.abc
    from fractions import Fraction

    from . import sample_module  # noqa: F401  only resolved by type_checking_namespace


def ratio(x: "Fraction") -> str:
    return str(x)


def first(values: "collections.abc.Sequence[int]") -> "int | None":
    return values[0] if values else None
