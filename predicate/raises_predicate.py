import asyncio
from dataclasses import dataclass, field
from typing import Any, Callable, Final, override

from predicate.is_async_predicate import is_async_p
from predicate.predicate import Explanation, Predicate


def _call(x: Any) -> None:
    if is_async_p(x):
        asyncio.run(x())
    else:
        x()


@dataclass
class RaisesPredicate(Predicate[Callable[..., Any]]):
    """A predicate that returns True if a callable raises an exception."""

    exception_type: type[Exception] = field(default=Exception)

    @override
    def __call__(self, x: Callable[..., Any]) -> bool:
        try:
            _call(x)
            return False
        except self.exception_type:
            return True
        except Exception:
            return False  # raised a different exception type

    @override
    def __repr__(self) -> str:
        if self.exception_type is Exception:
            return "raises_p"
        return f"raises_exception_p({self.exception_type.__name__})"

    @override
    def explain_failure(self, x: Callable[..., Any]) -> Explanation:
        """Explain why x did not raise; note that this calls x again, so side effects happen twice."""
        try:
            _call(x)
            return {"reason": "callable did not raise an exception"}
        except self.exception_type:
            return {}  # shouldn't reach here
        except Exception as e:
            return {"reason": f"raised {type(e).__name__}, expected {self.exception_type.__name__}"}


raises_p: Final = RaisesPredicate()
"""Return True if the callable raises any exception."""


def raises_exception_p(exception_type: type[Exception]) -> RaisesPredicate:
    """Return True if the callable raises the specified exception type."""
    return RaisesPredicate(exception_type=exception_type)
