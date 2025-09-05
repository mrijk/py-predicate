from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum
from types import UnionType
from typing import Any, Final, Iterator, get_args, override

from predicate.helpers import join_with_or
from predicate.predicate import Predicate


@dataclass
class IsSubclassPredicate[T](Predicate[T]):
    """A predicate class that models the 'issubclass' predicate."""

    class_or_tuple: type | UnionType | tuple[Any, ...]

    def __call__(self, x: type) -> bool:
        return issubclass(x, self.class_or_tuple)

    def __repr__(self) -> str:
        match self.class_or_tuple:
            case tuple() as klasses:
                class_names = ", ".join(klass.__name__ for klass in klasses)
                return f"is_subclass_p(({class_names}))"
            case UnionType() as union_type:
                class_names = "|".join(klass.__name__ for klass in get_args(union_type))
                return f"is_subclass_p({class_names})"
            case _ as klass:
                return f"is_{klass.__name__.lower()}_p"

    @override
    def get_klass(self) -> type:
        return self.class_or_tuple  # type: ignore

    @override
    def explain_failure(self, x: T) -> dict:
        def class_names() -> Iterator[str]:
            match self.class_or_tuple:
                case tuple() as klasses:
                    for klass in klasses:
                        yield klass.__name__
                case _:
                    yield self.class_or_tuple.__name__  # type: ignore

        klasses = join_with_or(list(class_names()))

        return {"reason": f"{x} is not a subclass of type {klasses}"}


def is_subclass_p(klass: type | UnionType | tuple[Any, ...]) -> Predicate:
    """Return True if value is an instance of one of the classes, otherwise False."""
    return IsSubclassPredicate(class_or_tuple=klass)


is_enum_p: Final[Predicate] = is_subclass_p(Enum)
"""Returns True if the value is an Enum, otherwise False."""

is_int_enum_p: Final[Predicate] = is_subclass_p(IntEnum)
"""Returns True if the value is an IntEnum, otherwise False."""

is_str_enum_p: Final[Predicate] = is_subclass_p(StrEnum)
"""Returns True if the value is a StrEnum, otherwise False."""
