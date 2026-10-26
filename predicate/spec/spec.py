from typing import Callable, NotRequired, TypedDict

from predicate.predicate import Predicate

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
