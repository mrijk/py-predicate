import asyncio
from dataclasses import dataclass, field
from typing import Any, Final, override

from predicate.is_async_predicate import is_async_p
from predicate.predicate import Predicate


def _call(x: Any) -> None:
    if is_async_p(x):
        asyncio.run(x())
    else:
        x()


@dataclass
class RaisesPredicate[T](Predicate[T]):
    """A predicate that returns True if a callable raises an exception."""

    exception_type: type[Exception] = field(default=Exception)

    def __call__(self, x: Any) -> bool:
        try:
            _call(x)
            return False
        except self.exception_type:
            return True
        except Exception:
            return False  # raised a different exception type

    def __repr__(self) -> str:
        if self.exception_type is Exception:
            return "raises_p"
        return f"raises_exception_p({self.exception_type.__name__})"

    @override
    def explain_failure(self, x: Any) -> dict:
        try:
            _call(x)
            return {"reason": "callable did not raise an exception"}
        except self.exception_type:
            return {}  # shouldn't reach here
        except Exception as e:
            return {"reason": f"raised {type(e).__name__}, expected {self.exception_type.__name__}"}


raises_p: Final[RaisesPredicate] = RaisesPredicate()
"""Return True if the callable raises any exception."""


def raises_exception_p(exception_type: type[Exception]) -> RaisesPredicate:
    """Return True if the callable raises the specified exception type."""
    return RaisesPredicate(exception_type=exception_type)
