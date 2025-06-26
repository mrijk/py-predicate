from typing import Callable, NotRequired, TypedDict

from predicate.predicate import Predicate

Spec = TypedDict(
    "Spec",
    {
        "args": dict[str, Predicate],
        "ret": Predicate,
        "fn": NotRequired[Callable[..., bool]],
        "fn_p": NotRequired[Callable[..., Predicate]],
    },
)
