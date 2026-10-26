from typing import Callable, NotRequired, TypedDict

from predicate.predicate import Predicate


class SpecViolationError(ValueError, AssertionError):
    """Raised when a function doesn't conform to its Spec.

    Subclasses ValueError (raised by instrument) and AssertionError (raised by exercise) for backwards compatibility.
    """


class InvalidSpecError(AssertionError):
    """Raised when a Spec itself is invalid, e.g. it doesn't match the function signature.

    Subclasses AssertionError for backwards compatibility.
    """


Spec = TypedDict(
    "Spec",
    {
        "args": dict[str, Predicate],
        "ret": NotRequired[Predicate],
        "pre": NotRequired[Callable[..., bool]],
        "fn": NotRequired[Callable[..., bool]],
        "fn_p": NotRequired[Callable[..., Predicate]],
        "raises": NotRequired[type[Exception] | tuple[type[Exception], ...]],
    },
)
