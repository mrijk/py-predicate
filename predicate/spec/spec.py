from typing import Callable, NotRequired, TypedDict

from predicate.predicate import Predicate


class SpecViolationError(Exception):
    """Raised when a function doesn't conform to its Spec."""


class InvalidSpecError(Exception):
    """Raised when a Spec itself is invalid, e.g. it doesn't match the function signature."""


class UnresolvedAnnotationWarning(UserWarning):
    """Issued when an annotation can't be evaluated at runtime and is treated as Any."""


Spec = TypedDict(
    "Spec",
    {
        "args": dict[str, Predicate],
        "ret": NotRequired[Predicate],
        "ret_name": NotRequired[str],
        "pre": NotRequired[Callable[..., bool]],
        "fn": NotRequired[Callable[..., bool]],
        "fn_p": NotRequired[Callable[..., Predicate]],
        "raises": NotRequired[type[Exception] | tuple[type[Exception], ...]],
    },
)
